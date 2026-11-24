// tour: recorre una página haciendo scroll y guarda capturas de la ventana en una hoja de contactos
// node tour.js <dir> <ruta> <out.png> [--desk] [--step=900] [--cols=4] [--max=40]
const { chromium, devices } = require('playwright');
const fs = require('fs'), path = require('path');
const ORIGIN = 'https://hortelamagenta.inboost.marketing';
const [dir, route, out, ...rest] = process.argv.slice(2);
const flags = Object.fromEntries(rest.filter(a => a.startsWith('--')).map(a => { const [k, v] = a.slice(2).split('='); return [k, v === undefined ? true : v]; }));
const FIX = process.env.FIX;
const PAGES = JSON.parse(fs.readFileSync(path.join(dir, 'routes.json'), 'utf8'));
const TYPES = { '.js': 'application/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.mp4': 'video/mp4', '.gif': 'image/gif' };
(async () => {
  const browser = await chromium.launch();
  const desk = !!flags.desk;
  const ctx = await browser.newContext(desk ? { viewport: { width: +(flags.w||1440), height: +(flags.h||900) } } : { ...devices['iPhone 13'], deviceScaleFactor: 1 });
  const page = await ctx.newPage(); const errors = [];
  page.on('pageerror', e => errors.push(String(e).slice(0, 300)));
  page.on('console', m => { if (m.type() === 'error' && !/Failed to load resource/.test(m.text())) errors.push('console: ' + m.text().slice(0, 200)); });
  await page.route('**/*', async r => {
    const u = new URL(r.request().url());
    if (u.origin !== ORIGIN) return r.abort();
    const key = u.pathname.replace(/\/+$/, '') || '/';
    if (PAGES[key]) {
      let html = fs.readFileSync(path.join(dir, PAGES[key] + '.html'), 'utf8');
      if (FIX && fs.existsSync(path.join(FIX,'hm-entradilla-movil.html'))) html = html.replace('</x-dc>', '</x-dc>' + fs.readFileSync(path.join(FIX,'hm-entradilla-movil.html'),'utf8'));
      if (FIX) html = html.replace(/<\/head>/i, '<link rel="stylesheet" href="/__fix/hm-boceto-fix.css"><script src="/__fix/hm-boceto-fix.js" defer></script></head>');
      return r.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body: html });
    }
    const fp = u.pathname.startsWith('/__fix/') ? path.join(FIX, u.pathname.slice(7)) : path.join(dir, 'site', decodeURIComponent(u.pathname));
    if (fs.existsSync(fp) && fs.statSync(fp).isFile()) return r.fulfill({ status: 200, contentType: TYPES[path.extname(fp)] || 'application/octet-stream', body: fs.readFileSync(fp) });
    return r.fulfill({ status: 404, body: '' });
  });
  await page.goto(ORIGIN + route, { waitUntil: 'load', timeout: 60000 });
  await page.waitForTimeout(+(flags.wait || 2500));
  const H = await page.evaluate(() => document.documentElement.scrollHeight);
  const vh = await page.evaluate(() => innerHeight), vw = await page.evaluate(() => innerWidth);
  const step = +(flags.step || vh), max = +(flags.max || 40);
  const shots = [];
  for (let y = 0, i = 0; y < H && i < max; y += step, i++) {
    await page.evaluate(y => scrollTo(0, y), y); await page.waitForTimeout(+(flags.pause || 700));
    shots.push(await page.screenshot());
  }
  const m = await page.evaluate(() => ({ docW: document.documentElement.scrollWidth, vw: innerWidth, H: document.documentElement.scrollHeight }));
  console.log(JSON.stringify({ shots: shots.length, ...m, errors }));
  // contact sheet via a blank page
  const cols = +(flags.cols || 4), scale = +(flags.scale || 0.3);
  const tw = Math.round(vw * scale), th = Math.round(vh * scale);
  const imgs = shots.map(b => 'data:image/png;base64,' + b.toString('base64'));
  const p2 = await ctx.newPage();
  await p2.setViewportSize({ width: cols * (tw + 6), height: Math.ceil(imgs.length / cols) * (th + 6) });
  await p2.setContent('<body style="margin:0;background:#888;display:flex;flex-wrap:wrap;gap:6px">' + imgs.map(s => `<img src="${s}" style="width:${tw}px;height:${th}px">`).join('') + '</body>');
  await p2.waitForTimeout(300);
  await p2.screenshot({ path: out, fullPage: true });
  await browser.close();
})();
