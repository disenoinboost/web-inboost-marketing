// Renderiza páginas de laura.inboost.marketing con Chromium y saca capturas comparables.
//
// Uso: node tools/render.js <dir> <nombre>=<url> [<nombre>=<url> ...]
//   <dir>/<nombre>.html  HTML servido por WordPress (lo obtiene tools/fetch_html.php con sesión
//                        del lado del servidor, así el borrador se ve sin exponer credenciales).
//   <dir>/site/...       espejo opcional de recursos (tools/bundle_assets.php). Si un recurso no
//                        está en el espejo se pide a la red; si la red está bloqueada, se responde 404.
// Salida: <dir>/shots/<nombre>-<desktop|mobile>-{hero,full,sNN}.png y <dir>/report.json
const { execSync } = require('child_process');
const { chromium } = require(execSync('npm root -g').toString().trim() + '/playwright');
const fs = require('fs'), path = require('path');

const [dir, ...pairs] = process.argv.slice(2);
const pages = Object.fromEntries(pairs.map(p => { const i = p.indexOf('='); return [p.slice(0, i), p.slice(i + 1)]; }));
const ORIGIN = process.env.ORIGIN || 'https://laura.inboost.marketing';
const TYPES = { '.css': 'text/css', '.js': 'application/javascript', '.woff2': 'font/woff2', '.woff': 'font/woff', '.ttf': 'font/ttf', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.gif': 'image/gif' };
// Solo para las capturas: oculta la barra de administración y el banner de cookies.
const HIDE = '#wpadminbar{display:none!important} html{margin-top:0!important} .cmplz-cookiebanner,#cmplz-manage-consent{display:none!important}';
const VIEWPORTS = { desktop: { width: 1440, height: 900 }, mobile: { width: 390, height: 844 } };

(async () => {
  fs.mkdirSync(path.join(dir, 'shots'), { recursive: true });
  const browser = await chromium.launch();
  const report = {};
  for (const [vp, size] of Object.entries(VIEWPORTS)) {
    for (const [name, url] of Object.entries(pages)) {
      const ctx = await browser.newContext({ viewport: size, isMobile: vp === 'mobile', hasTouch: vp === 'mobile', reducedMotion: 'reduce' });
      const page = await ctx.newPage();
      const missing = new Set(), errors = [];
      page.on('pageerror', e => errors.push(String(e).slice(0, 200)));
      await page.route('**/*', async route => {
        const req = route.request(), u = new URL(req.url());
        if (req.resourceType() === 'document' && u.origin === ORIGIN) {
          return route.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body: fs.readFileSync(path.join(dir, name + '.html')) });
        }
        if (u.origin === ORIGIN) {
          const fp = path.join(dir, 'site', decodeURIComponent(u.pathname));
          if (fs.existsSync(fp) && fs.statSync(fp).isFile()) {
            return route.fulfill({ status: 200, contentType: TYPES[path.extname(fp).toLowerCase()] || 'application/octet-stream', body: fs.readFileSync(fp) });
          }
        }
        try { return await route.continue(); } catch { missing.add(u.origin === ORIGIN ? u.pathname : u.host); return route.fulfill({ status: 404, body: '' }); }
      });
      page.on('requestfailed', r => missing.add(new URL(r.url()).pathname));
      await page.goto(url, { waitUntil: 'load', timeout: 90000 });
      await page.addStyleTag({ content: HIDE });
      await page.waitForTimeout(1500);
      const h = await page.evaluate(() => document.documentElement.scrollHeight);
      for (let y = 0; y < h; y += Math.floor(size.height * 0.6)) { await page.evaluate(y => window.scrollTo(0, y), y); await page.waitForTimeout(200); }
      await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(1000);
      await page.screenshot({ path: path.join(dir, 'shots', `${name}-${vp}-hero.png`) });
      await page.screenshot({ path: path.join(dir, 'shots', `${name}-${vp}-full.png`), fullPage: true });
      report[`${name}-${vp}`] = { ...(await page.evaluate(() => {
        const vis = el => { const r = el.getBoundingClientRect(), cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
        return {
          docW: document.documentElement.scrollWidth, winW: innerWidth, height: document.documentElement.scrollHeight,
          title: document.title, desc: document.querySelector('meta[name=description]')?.content,
          robots: document.querySelector('meta[name=robots]')?.content, canonical: document.querySelector('link[rel=canonical]')?.href || null,
          headings: [...document.querySelectorAll('h1,h2,h3,h4')].filter(vis).map(h => h.tagName + ': ' + h.textContent.replace(/\s+/g, ' ').trim().slice(0, 90)),
          links: [...new Set([...document.querySelectorAll('.et-l--post a[href]')].map(a => a.getAttribute('href')))],
          sections: [...document.querySelectorAll('.et-l--post .et_pb_section')].map(s => { const r = s.getBoundingClientRect(); return { top: Math.round(r.top + scrollY), h: Math.round(r.height) }; }),
          hiddenModules: [...document.querySelectorAll('.et-l--post .et_pb_module')].filter(m => parseFloat(getComputedStyle(m).opacity) < 0.1 && m.getBoundingClientRect().height > 0).length,
          ldjson: [...document.querySelectorAll('script[type="application/ld+json"]')].map(s => s.textContent.slice(0, 300)),
        };
      })), missing: [...missing], errors };
      const n = await page.evaluate(() => document.querySelectorAll('.et-l--post .et_pb_section').length);
      for (let i = 0; i < n; i++) {
        await page.evaluate(i => { const s = document.querySelectorAll('.et-l--post .et_pb_section')[i]; window.scrollTo(0, s.getBoundingClientRect().top + scrollY); }, i);
        await page.waitForTimeout(600);
        await page.screenshot({ path: path.join(dir, 'shots', `${name}-${vp}-s${String(i).padStart(2, '0')}.png`) });
      }
      await ctx.close();
    }
  }
  fs.writeFileSync(path.join(dir, 'report.json'), JSON.stringify(report, null, 1));
  await browser.close();
  for (const [k, v] of Object.entries(report)) console.log(k, 'docW', v.docW, 'winW', v.winW, 'errores', v.errors.length, 'ocultos', v.hiddenModules, 'faltan', v.missing.length);
})().catch(e => { console.error(e); process.exit(1); });
