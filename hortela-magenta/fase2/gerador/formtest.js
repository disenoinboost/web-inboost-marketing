const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const ORIGIN = 'https://hortelamagenta.inboost.marketing'; const dir = process.argv[2];
const PAGES = JSON.parse(fs.readFileSync(path.join(dir, 'routes.json'), 'utf8'));
(async () => { const b = await chromium.launch(); const p = await (await b.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
  let posted = null; const errs = []; p.on('pageerror', e => errs.push(String(e)));
  await p.route('**/*', async r => { const u = new URL(r.request().url()); if (u.origin !== ORIGIN) return r.abort();
    if (u.pathname === '/wp-json/hm/v1/contacto') { posted = r.request().postData(); return r.fulfill({ status: 200, contentType: 'application/json', body: '{"ok":true}' }); }
    const key = u.pathname.replace(/\/+$/, '') || '/'; if (PAGES[key]) return r.fulfill({ status: 200, contentType: 'text/html', body: fs.readFileSync(path.join(dir, PAGES[key] + '.html'), 'utf8') });
    const fp = path.join(dir, 'site', decodeURIComponent(u.pathname)); if (fs.existsSync(fp) && fs.statSync(fp).isFile()) return r.fulfill({ status: 200, body: fs.readFileSync(fp) }); return r.fulfill({ status: 404, body: '' }); });
  await p.goto(ORIGIN + '/contacto?servico=' + encodeURIComponent('Gráfico + Editorial'), { waitUntil: 'load' }); await p.waitForTimeout(2500);
  const pre = await p.evaluate(() => { const s = document.getElementById('servico'); return s ? s.options[s.selectedIndex].text : 'sem select'; });
  await p.fill('#nome', 'Teste'); await p.fill('#email', 'teste@exemplo.pt'); await p.fill('#mensagem', 'Olá');
  await p.locator('input[type=checkbox]').first().check({ force: true }); await p.waitForTimeout(3200);
  await Promise.all([p.waitForURL('**/obrigado', { timeout: 15000 }).catch(() => {}), p.click('form button[type=submit]')]);
  await p.waitForTimeout(1500);
  console.log(JSON.stringify({ preselecionado: pre, url: p.url(), enviado: posted ? posted.replace(/-{6,}[^\n]*\n/g, '').replace(/Content-Disposition: form-data; name=/g, '').replace(/\r?\n\r?\n/g, '=').replace(/\r?\n/g, ' | ').slice(0, 400) : null, errs }, null, 1));
  await b.close(); })();
