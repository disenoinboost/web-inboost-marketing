// reg: todas las rutas de routes.json en móvil y PC: errores JS, ancho del documento, enlaces internos rotos, imgs sin alt
const { chromium, devices } = require('playwright'); const fs = require('fs'), path = require('path');
const ORIGIN = 'https://hortelamagenta.inboost.marketing'; const dir = process.argv[2]; const only = process.argv[3];
const FIX = process.env.FIX; const PAGES = JSON.parse(fs.readFileSync(path.join(dir, 'routes.json'), 'utf8'));
const TYPES = { '.js': 'application/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.webp': 'image/webp', '.gif': 'image/gif', '.png': 'image/png', '.jpg': 'image/jpeg' };
const known = new Set(Object.keys(PAGES).map(k => k.replace(/\/+$/, '') || '/'));
(async () => {
  const b = await chromium.launch(); const bad = {};
  for (const desk of [false, true]) for (const route of Object.keys(PAGES)) {
    if (only && !route.includes(only)) continue;
    const ctx = await b.newContext(desk ? { viewport: { width: 1440, height: 900 } } : { ...devices['iPhone 13'], deviceScaleFactor: 1 });
    const p = await ctx.newPage(); const errors = [];
    p.on('pageerror', e => errors.push(String(e).slice(0, 160)));
    await p.route('**/*', async r => { const u = new URL(r.request().url()); if (u.origin !== ORIGIN) return r.abort(); const key = u.pathname.replace(/\/+$/, '') || '/';
      if (PAGES[key] && r.request().resourceType() === 'document') { let h = fs.readFileSync(path.join(dir, PAGES[key] + '.html'), 'utf8'); if (FIX) { if (fs.existsSync(path.join(FIX, 'hm-entradilla-movil.html'))) h = h.replace('</x-dc>', '</x-dc>' + fs.readFileSync(path.join(FIX, 'hm-entradilla-movil.html'), 'utf8')); h = h.replace(/<\/head>/i, '<link rel="stylesheet" href="/__fix/hm-boceto-fix.css"><script src="/__fix/hm-boceto-fix.js" defer></script></head>'); } return r.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body: h }); }
      const fp = u.pathname.startsWith('/__fix/') ? path.join(FIX, u.pathname.slice(7)) : path.join(dir, 'site', decodeURIComponent(u.pathname));
      if (fs.existsSync(fp) && fs.statSync(fp).isFile()) return r.fulfill({ status: 200, contentType: TYPES[path.extname(fp)] || 'application/octet-stream', body: fs.readFileSync(fp) });
      return r.fulfill({ status: 404, body: '' }); });
    await p.goto(ORIGIN + (route === '/' ? '/' : route), { waitUntil: 'load', timeout: 60000 }); await p.waitForTimeout(1800);
    const H = await p.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < H; y += 900) { await p.evaluate(y => scrollTo(0, y), y); await p.waitForTimeout(40); }
    const m = await p.evaluate(() => ({ vw: innerWidth, docW: document.documentElement.scrollWidth,
      links: [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href')),
      noalt: [...document.images].filter(i => !i.hasAttribute('alt')).length,
      h1: [...document.querySelectorAll('h1')].map(h => h.textContent.trim().slice(0, 60)),
      title: document.title }));
    const internal = m.links.filter(h => h && h.startsWith('/') && !h.startsWith('//') && !h.startsWith('/wp-content'));
    const broken = [...new Set(internal.map(h => h.split('#')[0].split('?')[0]).filter(h => !known.has(h.replace(/\/+$/, '') || '/')))];
    const slashy = [...new Set(internal.filter(h => /^\/(servicos|projetos|sobre|blog|contacto)(\/[a-z0-9-]+)*\/(#|$)/.test(h)))];
    const ext = [...new Set(m.links.filter(h => /hortelamagenta\.pt\/(?!media)/.test(h || '')))];
    broken.forEach(h => { bad[h] = (bad[h] || new Set()).add(route); });
    console.log((desk ? 'pc    ' : 'movil ') + route.padEnd(46), m.docW === m.vw ? 'ancho ok' : 'DESBORDA ' + m.docW, errors.length ? 'ERR ' + JSON.stringify(errors) : '0 err', 'h1:' + m.h1.length, m.noalt ? 'sin-alt:' + m.noalt : '', slashy.length ? 'BARRA:' + slashy.join(',') : '', ext.length ? 'ANTIGA:' + ext.join(',') : '');
    await ctx.close();
  }
  console.log('ENLACES SIN PÁGINA:', JSON.stringify(Object.fromEntries(Object.entries(bad).map(([k, v]) => [k, [...v].length]))));
  await b.close();
})();
