// Mide FCP/LCP/TBT de la portada (paquete vs desempaquetada) con throttling tipo Lighthouse móvil.
const { execSync } = require('child_process');
const { chromium } = require(execSync('npm root -g').toString().trim() + '/playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const DIR = process.argv[2], RUNS = +(process.argv[3] || 3);
const TYPES = { '.js': 'text/javascript', '.woff2': 'font/woff2', '.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp' };
const zlib = require('zlib');
function server(root, port) {
  return new Promise(r => {
    const s = http.createServer((req, res) => {
      const u = decodeURIComponent(new URL(req.url, 'http://x').pathname);
      let fp = u === '/' ? path.join(DIR, root) : path.join(DIR, 'site', u);
      if (!fs.existsSync(fp)) { res.writeHead(404); return res.end(); }
      const ext = path.extname(fp);
      let body = fs.readFileSync(fp); const h = { 'content-type': TYPES[ext] || 'text/html; charset=utf-8' };
      if (!['.jpg', '.png', '.webp', '.woff2'].includes(ext)) { body = zlib.gzipSync(body); h['content-encoding'] = 'gzip'; }
      res.writeHead(200, h); res.end(body);
    }).listen(port, () => r(s));
  });
}
const STUB = fs.readFileSync(path.join(DIR, 'assets/5f7190ae-745a-465d-8638-1c559b7ba9fa.jpg'));
(async () => {
  const srv = [await server('home.html', 8101), await server('dist.html', 8102)];
  const browser = await chromium.launch();
  const out = { bundle: [], dist: [] };
  for (let i = 0; i < RUNS; i++) for (const [name, port] of [['bundle', 8101], ['dist', 8102]]) {
    const ctx = await browser.newContext({ viewport: { width: 412, height: 823 }, deviceScaleFactor: 1.75, isMobile: true, hasTouch: true });
    const page = await ctx.newPage();
    const errors = []; page.on('response', r => { if (r.status() >= 400) errors.push(r.status() + ' ' + r.url().slice(-70)); });
    page.on('pageerror', e => errors.push(String(e).slice(0, 160)));
    await page.route(/^https?:\/\/(?!127\.0\.0\.1)/, r => r.request().resourceType() === 'image' ? r.fulfill({ status: 200, contentType: 'image/jpeg', body: STUB }) : r.abort());
    await page.addInitScript(() => {
      window.__m = { lt: [], lcp: 0, fcp: 0 };
      new PerformanceObserver(l => l.getEntries().forEach(e => window.__m.lt.push([e.startTime, e.duration]))).observe({ type: 'longtask', buffered: true });
      new PerformanceObserver(l => l.getEntries().forEach(e => { window.__m.lcp = e.startTime; window.__m.lcpEl = (e.element && (e.element.tagName + '.' + (e.element.className || '').toString().slice(0, 30))) || e.url; })).observe({ type: 'largest-contentful-paint', buffered: true });
      new PerformanceObserver(l => l.getEntries().forEach(e => { if (e.name === 'first-contentful-paint') window.__m.fcp = e.startTime; })).observe({ type: 'paint', buffered: true });
    });
    const cdp = await ctx.newCDPSession(page);
    await cdp.send('Network.enable');
    await cdp.send('Network.emulateNetworkConditions', { offline: false, latency: 150, downloadThroughput: 1638.4 * 1024 / 8, uploadThroughput: 675 * 1024 / 8 });
    await cdp.send('Emulation.setCPUThrottlingRate', { rate: 4 });
    let bytes = 0; cdp.on('Network.loadingFinished', e => bytes += e.encodedDataLength);
    const t0 = Date.now();
    await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'load', timeout: 120000 });
    await page.waitForTimeout(8000);
    const m = await page.evaluate(() => window.__m);
    const tbt = m.lt.filter(([s, d]) => s + d > m.fcp).reduce((a, [s, d]) => a + Math.max(0, d - 50), 0);
    const ltSum = m.lt.reduce((a, [, d]) => a + d, 0);
    const vis = await page.evaluate(() => ({ h: document.documentElement.scrollHeight, w: document.documentElement.scrollWidth, h1: (document.querySelector('h1') || {}).textContent }));
    out[name].push({ fcp: Math.round(m.fcp), lcp: Math.round(m.lcp), lcpEl: m.lcpEl, tbt: Math.round(tbt), longTasks: m.lt.length, ltSum: Math.round(ltSum), kb: Math.round(bytes / 1024), errors, ...vis });
    if (i === 0) await page.screenshot({ path: path.join(DIR, `shot-${name}.png`) });
    await ctx.close();
  }
  console.log(JSON.stringify(out, null, 1));
  await browser.close(); srv.forEach(s => s.close());
})();
