// Banner de Complianz tal como lo sirve la web (copia bajada del servidor): node cmplz_render.js <dir-copia> <etiqueta>
// Visitante nuevo (sin cookies cmplz_*). Mide alto, filas de botones, texto cortado, X, cabecera, la vista «Ver preferências»
// y si el banner queda por encima de la barra «Pedir orçamento · Ligar».
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const ORIGIN = 'https://hortelamagenta.inboost.marketing', S = '/tmp/claude-0/-home-user-web-inboost-marketing/8ac7a14c-9ecb-54c6-b461-e5d9e459bd0f/scratchpad';
const [MIR, LABEL, PAGE] = process.argv.slice(2); const FIX = '/home/user/web-inboost-marketing/hortela-magenta/capa-fix';
const TYPES = { '.js': 'application/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg', '.gif': 'image/gif' };
const SIZES = process.env.ACCEPT ? [[375, 812, 1]] : [[320, 700, 1], [375, 812, 1], [488, 900, 1], [768, 1024, 1], [1280, 800, 0]];
(async () => { const b = await chromium.launch(); const out = {};
  for (const [w, h, mob] of SIZES) {
    const ctx = await b.newContext(mob ? { viewport: { width: w, height: h }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 } : { viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(String(e).slice(0, 120)));
    await p.route('**/*', async r => { const u = new URL(r.request().url());
      if (u.host === 'unpkg.com' && /\/react(-dom)?@/.test(u.pathname)) return r.fulfill({ status: 200, contentType: 'application/javascript', body: fs.readFileSync(path.join(S, 'dist4/site/wp-content/themes/divi-child/hm-paginas/dist/a', /react-dom/.test(u.pathname) ? 'feb8ddc9d0566a4f.js' : 'aa77ae4c49f525bc.js')) });
      if (u.origin !== ORIGIN) return r.abort();
      if (r.request().resourceType() === 'document') return r.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body: fs.readFileSync(path.join(MIR, (PAGE || 'alsil') + '.html'), 'utf8') });
      if (u.pathname.startsWith('/wp-json') || u.pathname.includes('admin-ajax')) return r.fulfill({ status: 200, contentType: 'application/json', body: '{}' });
      let fp = path.join(MIR, 'site', decodeURIComponent(u.pathname));
      if (!fs.existsSync(fp)) fp = u.pathname.includes('/assets/hm-boceto-fix.') ? path.join(FIX, path.basename(u.pathname)) : path.join(S, 'dist4', 'site', decodeURIComponent(u.pathname));
      if (fs.existsSync(fp) && fs.statSync(fp).isFile()) return r.fulfill({ status: 200, contentType: TYPES[path.extname(fp).toLowerCase()] || 'application/octet-stream', body: fs.readFileSync(fp) });
      return r.fulfill({ status: 404, body: '' }); });
    await p.goto(ORIGIN + '/projetos/alsil/', { waitUntil: 'load' });
    await p.waitForSelector('.cmplz-cookiebanner.cmplz-show', { timeout: 15000 }).catch(() => {}); await p.waitForTimeout(1500);
    const measure = () => p.evaluate(() => { const bn = document.querySelector('.cmplz-cookiebanner'); if (!bn) return null; const r = bn.getBoundingClientRect();
      const vis = e => e && e.offsetParent !== null && getComputedStyle(e).display !== 'none' && getComputedStyle(e).visibility !== 'hidden';
      const btns = [...bn.querySelectorAll('.cmplz-buttons .cmplz-btn')].filter(vis).map(x => { const q = x.getBoundingClientRect(); return { t: x.textContent.trim(), top: Math.round(q.top), w: Math.round(q.width), cut: x.scrollWidth > x.clientWidth + 1, fs: getComputedStyle(x).fontSize, ls: getComputedStyle(x).letterSpacing }; });
      const rows = new Set(btns.map(x => x.top)).size;
      const links = [...bn.querySelectorAll('.cmplz-links.cmplz-documents li')].filter(vis).map(li => { const rg = document.createRange(); rg.selectNodeContents(li); return new Set([...rg.getClientRects()].filter(q => q.width > 1).map(q => Math.round(q.top))).size; });
      return { h: Math.round(r.height), w: Math.round(r.width), top: Math.round(r.top), z: getComputedStyle(bn).zIndex, btns, rows, x: vis(bn.querySelector('.cmplz-close')), header: vis(bn.querySelector('.cmplz-header')), dividers: [...bn.querySelectorAll('.cmplz-divider')].filter(vis).length, linkLines: links, fit: r.left >= 0 && r.right <= innerWidth + 0.5 }; });
    const m1 = await measure(); await p.screenshot({ path: `${S}/cmplz_${LABEL}_${w}.png` });
    if (process.env.ACCEPT) { await p.click('.cmplz-cookiebanner .cmplz-accept'); await p.waitForTimeout(800); await p.evaluate(() => scrollTo(0, innerHeight * 1.6)); await p.waitForTimeout(1000);
      const after = await p.evaluate(() => { const c = document.querySelector('.hm-cta'); const bn = document.querySelector('.cmplz-cookiebanner'); return { banner: bn.className.replace(/\s+/g, ' '), ctaVisible: !!c && getComputedStyle(c).visibility === 'visible' && +getComputedStyle(c).opacity > .9, cookie: document.cookie.split('; ').filter(x => x.startsWith('cmplz_')).join('; ') }; });
      console.log('tras aceptar', JSON.stringify(after)); await p.screenshot({ path: `${S}/cmplz_${LABEL}_aceptado.png` }); await ctx.close(); continue; }
    // barra «Pedir orçamento · Ligar»: aparece tras el primer pantallazo; el banner debe quedar por encima
    await p.evaluate(() => scrollTo(0, innerHeight * 1.6)); await p.waitForTimeout(900);
    const cta = await p.evaluate(() => { const c = document.querySelector('.hm-cta'); const bn = document.querySelector('.cmplz-cookiebanner'); if (!c || !bn || getComputedStyle(c).visibility === 'hidden' || +getComputedStyle(c).opacity < .5) return { visible: false };
      const cr = c.getBoundingClientRect(), br = bn.getBoundingClientRect(); const over = !(cr.bottom <= br.top || cr.top >= br.bottom || cr.right <= br.left || cr.left >= br.right);
      const top = document.elementFromPoint(cr.left + cr.width / 2, cr.top + cr.height / 2); return { visible: true, overlap: over, bannerOnTop: over ? !!(top && top.closest('.cmplz-cookiebanner')) : null, gap: Math.round(br.top - cr.bottom) }; });
    await p.screenshot({ path: `${S}/cmplz_${LABEL}_${w}_cta.png` });
    await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(300);
    let m2 = null; const vp = await p.$('.cmplz-cookiebanner .cmplz-view-preferences'); if (vp && await vp.isVisible()) { await vp.click(); await p.waitForTimeout(900); m2 = await measure(); await p.screenshot({ path: `${S}/cmplz_${LABEL}_${w}_pref.png` }); }
    out[w] = { banner: m1, cta, prefs: m2, errs };
    console.log(String(w).padEnd(5), JSON.stringify({ h: m1 && m1.h, rows: m1 && m1.rows, btns: m1 && m1.btns.map(x => x.t + (x.cut ? '(CORTADO)' : '') + ' ' + x.w + 'px'), x: m1 && m1.x, header: m1 && m1.header, div: m1 && m1.dividers, links: m1 && m1.linkLines, z: m1 && m1.z, cta, prefs: m2 && { h: m2.h, rows: m2.rows, btns: m2.btns.map(x => x.t + (x.cut ? '(CORTADO)' : '')) }, errs: errs.length }));
    await ctx.close(); }
  fs.writeFileSync(`${S}/cmplz_${LABEL}.json`, JSON.stringify(out, null, 1)); await b.close(); })();
