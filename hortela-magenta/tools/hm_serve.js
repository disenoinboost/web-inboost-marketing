// Hortelã Magenta · banco de pruebas local con Chromium (el contenedor no llega al sitio: proxy 403).
// Sirve las páginas traídas con hm_pull.php + unpack.py bajo el origen real y les añade la capa de
// correcciones LOCAL (hortela-magenta/fix/, o la carpeta de la variable FIX), así se prueba antes de subir.
//
// Uso:
//   node hortela-magenta/tools/hm_serve.js <dir> reg
//        las 10 páginas en móvil (iPhone 13) y escritorio (1440x900): errores JS, ancho del documento, capa cargada
//   node hortela-magenta/tools/hm_serve.js <dir> shot <ruta> <salida.png> [--desk] [--full] [--at=<selector>:<fracción>] [--wait=ms]
//        captura; --at desplaza al bloque <selector> y avanza la fracción (0..1) de su recorrido fijado
//   node hortela-magenta/tools/hm_serve.js <dir> run <ruta> <guion.js> [--desk]
//        guion.js: module.exports = async (page, { shot, H }) => { ... }   (H = helper de capturas)
const { chromium, devices } = require('playwright');
const fs = require('fs'), path = require('path');

const ORIGIN = 'https://hortelamagenta.inboost.marketing';
const PAGES = { '/': 'home', '/servicos/': 'servicos', '/servicos/branding/': 'branding', '/servicos/design-web/': 'design-web', '/projetos/': 'projetos', '/projetos/camolas/': 'camolas', '/sobre/': 'sobre', '/blog/': 'blog', '/blog/quanto-custa-um-site/': 'artigo', '/contacto/': 'contacto' };
const TYPES = { '.js': 'application/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.mp4': 'video/mp4' };
const FIX = process.env.FIX || path.join(__dirname, '..', 'fix');
const [dir, cmd, ...rest] = process.argv.slice(2);
const flags = Object.fromEntries(rest.filter(a => a.startsWith('--')).map(a => { const [k, v] = a.slice(2).split('='); return [k, v === undefined ? true : v]; }));
const args = rest.filter(a => !a.startsWith('--'));

async function open(browser, urlPath, desk) {
  const ctx = await browser.newContext(desk ? { viewport: { width: 1440, height: 900 } } : { ...devices['iPhone 13'], deviceScaleFactor: 1 });
  const page = await ctx.newPage(); const errors = [];
  page.on('pageerror', e => errors.push(String(e).slice(0, 200)));
  await page.route('**/*', async route => {
    const u = new URL(route.request().url());
    if (u.origin !== ORIGIN) return route.abort();
    if (PAGES[u.pathname]) {
      let html = fs.readFileSync(path.join(dir, PAGES[u.pathname] + '.html'), 'utf8');
      html = html.replace(/<\/head>/i, '<link rel="stylesheet" href="/__fix/hm-boceto-fix.css"><script src="/__fix/hm-boceto-fix.js" defer></script></head>');
      return route.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body: html });
    }
    const fp = u.pathname.startsWith('/__fix/') ? path.join(FIX, u.pathname.slice(7)) : path.join(dir, 'site', decodeURIComponent(u.pathname));
    if (fs.existsSync(fp) && fs.statSync(fp).isFile()) return route.fulfill({ status: 200, contentType: TYPES[path.extname(fp)] || 'application/octet-stream', body: fs.readFileSync(fp) });
    return route.fulfill({ status: 404, body: '' });
  });
  await page.goto(ORIGIN + urlPath, { waitUntil: 'load', timeout: 60000 });
  await page.waitForTimeout(+(flags.wait || 2500));
  return { ctx, page, errors };
}
async function at(page, spec) {
  const i = spec.lastIndexOf(':'), sel = spec.slice(0, i), f = +spec.slice(i + 1);
  await page.evaluate(([sel, f]) => { const el = document.querySelector(sel); const top = el.getBoundingClientRect().top + scrollY; scrollTo(0, top + Math.max(0, el.offsetHeight - innerHeight) * f); }, [sel, f]);
  await page.waitForTimeout(1200);
}

(async () => {
  const browser = await chromium.launch();
  if (cmd === 'reg') {
    for (const desk of [false, true]) for (const p of Object.keys(PAGES)) {
      const { ctx, page, errors } = await open(browser, p, desk);
      const h = await page.evaluate(() => document.documentElement.scrollHeight);
      for (let y = 0; y < h; y += 700) { await page.evaluate(y => scrollTo(0, y), y); await page.waitForTimeout(60); }
      const m = await page.evaluate(() => ({ fix: !!window.__hmFix, vw: innerWidth, docW: document.documentElement.scrollWidth }));
      console.log((desk ? 'pc    ' : 'movil ') + PAGES[p].padEnd(11), m.fix ? 'capa ok' : 'SIN CAPA', m.docW === m.vw ? 'ancho ok' : 'DESBORDA ' + m.docW + '>' + m.vw, errors.length ? 'ERRORES ' + JSON.stringify(errors) : '0 errores');
      await ctx.close();
    }
  } else if (cmd === 'shot') {
    const { ctx, page, errors } = await open(browser, args[0], !!flags.desk);
    if (flags.at) await at(page, flags.at);
    await page.screenshot({ path: args[1], fullPage: !!flags.full });
    console.log('ok', args[1], errors.length ? errors : '');
    await ctx.close();
  } else if (cmd === 'run') {
    const { ctx, page, errors } = await open(browser, args[0], !!flags.desk);
    const H = { at: spec => at(page, spec), shot: (file, o = {}) => page.screenshot({ path: file, ...o }) };
    await require(path.resolve(args[1]))(page, H);
    console.log(errors.length ? 'errores: ' + JSON.stringify(errors) : '0 errores');
    await ctx.close();
  } else {
    console.log('comandos: reg | shot | run (ver cabecera del archivo)');
  }
  await browser.close();
})();
