// mede a velocidade das capturas de «O site» (Camolas): node osite.js <vw> <vh> <mob 0|1> [shotsdir]
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const ORIGIN = 'https://hortelamagenta.inboost.marketing', S = '/tmp/claude-0/-home-user-web-inboost-marketing/8ac7a14c-9ecb-54c6-b461-e5d9e459bd0f/scratchpad';
const DIR = process.env.DIR || S + '/dist4', FIX = process.env.FIX || '/home/user/web-inboost-marketing/hortela-magenta/capa-fix';
const TYPES = { '.js': 'application/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg' };
const [VW, VH, MOB, OUT] = process.argv.slice(2);
(async () => { const b = await chromium.launch(); const PAGES = JSON.parse(fs.readFileSync(path.join(DIR, 'routes.json'), 'utf8'));
  const ctx = await b.newContext(MOB === '1' ? { viewport: { width: +VW, height: +VH }, isMobile: true, hasTouch: true, deviceScaleFactor: 1 } : { viewport: { width: +VW, height: +VH } });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.route('**/*', async r => { const u = new URL(r.request().url()); if (u.origin !== ORIGIN) return r.abort(); const key = u.pathname.replace(/\/+$/, '') || '/';
    if (PAGES[key] && r.request().resourceType() === 'document') { let h = fs.readFileSync(path.join(DIR, PAGES[key] + '.html'), 'utf8'); h = h.replace(/<\/head>/i, '<link rel="stylesheet" href="/__fix/hm-boceto-fix.css"><script src="/__fix/hm-boceto-fix.js" defer></script></head>'); return r.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body: h }); }
    const fp = u.pathname.startsWith('/__fix/') ? path.join(FIX, u.pathname.slice(7)) : path.join(DIR, 'site', decodeURIComponent(u.pathname));
    if (fs.existsSync(fp) && fs.statSync(fp).isFile()) return r.fulfill({ status: 200, contentType: TYPES[path.extname(fp).toLowerCase()] || 'application/octet-stream', body: fs.readFileSync(fp) });
    return r.fulfill({ status: 404, body: '' }); });
  await p.goto(ORIGIN + '/projetos/camolas/', { waitUntil: 'load' }); await p.waitForTimeout(2500);
  const top = await p.evaluate(() => { const r = document.querySelector('#digital'); return { top: r.getBoundingClientRect().top + scrollY, h: r.offsetHeight }; });
  const vh = +VH, step = Math.round(vh * 0.05); let prev = null; const rate = {}, dist = {}; let shotN = 0;
  for (let y = top.top - vh; y < top.top + top.h; y += step) {
    await p.evaluate(y => scrollTo(0, y), y); await p.waitForTimeout(30);
    const m = await p.evaluate(() => [...document.querySelectorAll('#digital [data-hm-shot]')].filter(s => s.offsetParent).map(s => s.getBoundingClientRect().top));
    if (prev) m.forEach((t, i) => { const d = prev[i] - t; if (d > 0.5) { rate[i] = Math.max(rate[i] || 0, d / step); dist[i] = (dist[i] || 0) + step; } });
    prev = m;
    if (OUT && (y - (top.top - vh)) % (step * 20) === 0) { fs.mkdirSync(OUT, { recursive: true }); await p.screenshot({ path: OUT + '/' + String(shotN++).padStart(2, '0') + '.jpg', quality: 60 }); }
  }
  const info = await p.evaluate(() => [...document.querySelectorAll('#digital [data-hm-shot]')].filter(s => s.offsetParent).map(s => s.scrollHeight));
  console.log((MOB === '1' ? 'movil ' : 'pc    ') + VW + 'x' + VH, 'secção', Math.round(top.h / vh * 100) + 'vh', 'capturas', JSON.stringify(info), 'vel. máx (×scroll)', JSON.stringify(Object.values(rate).map(v => +v.toFixed(2))), 'scroll em movimento (ecrãs)', JSON.stringify(Object.values(dist).map(v => +(v / vh).toFixed(1))), errs.length ? 'ERROS ' + errs : '0 erros');
  await b.close(); })();
