// Batería de regresión: cada corrección pedida por Laura se comprueba aquí antes de subir.
// node bateria.js [filtro-de-ruta]   (DIR=dist, FIX=capa-fix; LIVE=1 para probar el sitio publicado)
const { chromium, devices } = require('playwright'); const fs = require('fs'), path = require('path');
const ORIGIN = 'https://hortelamagenta.inboost.marketing', S = '/tmp/claude-0/-home-user-web-inboost-marketing/8ac7a14c-9ecb-54c6-b461-e5d9e459bd0f/scratchpad';
const DIR = process.env.DIR || S + '/dist4', FIX = process.env.FIX || '/home/user/web-inboost-marketing/hortela-magenta/capa-fix', LIVE = !!process.env.LIVE;
const TYPES = { '.js': 'application/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.webp': 'image/webp', '.gif': 'image/gif', '.png': 'image/png', '.jpg': 'image/jpeg' };
const PAGES = JSON.parse(fs.readFileSync(path.join(DIR, 'routes.json'), 'utf8'));
const only = process.argv[2];
const DEV = {
  movil: { ...devices['iPhone 13'], deviceScaleFactor: 1 },
  movil360: { viewport: { width: 360, height: 780 }, isMobile: true, hasTouch: true, deviceScaleFactor: 1 },
  tablet: { viewport: { width: 820, height: 1180 }, isMobile: true, hasTouch: true, deviceScaleFactor: 1 },
  pc: { viewport: { width: 1440, height: 900 } },
  portatil: { viewport: { width: 1280, height: 720 } },
};
const results = []; let fails = 0;
function rep(dev, route, name, ok, info) { results.push({ dev, route, name, ok, info }); if (!ok) fails++; console.log((ok ? '  ok   ' : '  FALLA') + ' ' + dev.padEnd(9) + route.padEnd(44) + name + (info ? ' · ' + info : '')); }

async function open(b, dev, route) {
  const ctx = await b.newContext(DEV[dev]); const p = await ctx.newPage(); const errs = []; const miss = [];
  p.on('pageerror', e => errs.push(String(e).slice(0, 140)));
  if (!LIVE) await p.route('**/*', async r => { const u = new URL(r.request().url()); if (u.origin !== ORIGIN) { miss.push(r.request().url()); return r.abort(); } const key = u.pathname.replace(/\/+$/, '') || '/';
    if (PAGES[key] && r.request().resourceType() === 'document') { let h = fs.readFileSync(path.join(DIR, PAGES[key] + '.html'), 'utf8'); if (fs.existsSync(path.join(FIX, 'hm-entradilla-movil.html'))) h = h.replace('</x-dc>', '</x-dc>' + fs.readFileSync(path.join(FIX, 'hm-entradilla-movil.html'), 'utf8')); h = h.replace(/<\/head>/i, '<link rel="stylesheet" href="/__fix/hm-boceto-fix.css"><script src="/__fix/hm-boceto-fix.js" defer></script></head>'); return r.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body: h }); }
    const fp = u.pathname.startsWith('/__fix/') ? path.join(FIX, u.pathname.slice(7)) : path.join(DIR, 'site', decodeURIComponent(u.pathname));
    if (fs.existsSync(fp) && fs.statSync(fp).isFile()) return r.fulfill({ status: 200, contentType: TYPES[path.extname(fp).toLowerCase()] || 'application/octet-stream', body: fs.readFileSync(fp) });
    miss.push(r.request().url()); return r.fulfill({ status: 404, body: '' }); });
  await p.goto(ORIGIN + route, { waitUntil: 'load', timeout: 90000 }); await p.waitForTimeout(1800);
  p.__miss = miss; return { ctx, p, errs };
}
async function walk(p, step = 700) { const H = await p.evaluate(() => document.documentElement.scrollHeight); for (let y = 0; y < H; y += step) { await p.evaluate(y => scrollTo(0, y), y); await p.waitForTimeout(35); } await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(300); }
async function toEl(p, sel, frac = 0) { return p.evaluate(([sel, frac]) => { const e = document.querySelector(sel); if (!e) return false; const t = e.getBoundingClientRect().top + scrollY; scrollTo(0, t + (e.offsetHeight - innerHeight) * frac); return true; }, [sel, frac]); }

// ---------- comprobaciones que valen para cualquier página ----------
const GENERAL = () => {
  const out = {}; const vw = innerWidth;
  out.ancho = document.documentElement.scrollWidth <= vw;
  out.imgRotas = [...document.images].filter(i => i.complete && i.currentSrc && i.naturalWidth === 0 && !(window.__hmLocal404 || []).includes(i.currentSrc)).map(i => i.currentSrc.split('/').pop()).slice(0, 4);
  // fondos: dos secciones seguidas con el mismo color (sólo secciones de primer nivel con color propio)
  const col = e => { const c = getComputedStyle(e).backgroundColor; return (c === 'rgba(0, 0, 0, 0)' || c === 'transparent') ? null : c; };
  const secs = [...document.querySelectorAll('main section, x-dc section, body section')].filter(s => !s.parentElement.closest('section') && s.offsetHeight > 120 && getComputedStyle(s).display !== 'none');
  const uniq = [...new Set(secs)]; const pares = [];
  for (let i = 1; i < uniq.length; i++) { const a = col(uniq[i - 1]), b = col(uniq[i]); const la = uniq[i - 1].getAttribute('data-screen-label') || '', lb = uniq[i].getAttribute('data-screen-label') || ''; /* «06 Filme» + «06 Filme · João Bordeira»: o mesmo capítulo do desenho */
    if (a && b && a === b && !(la && lb.indexOf(la) === 0) && !uniq[i].hasAttribute('data-hm-joined') /* fotos coladas ao texto de cima (sem título): continuação da mesma secção */ && !uniq[i].hasAttribute('data-veil') && !uniq[i - 1].querySelector('[data-veil]')) pares.push((uniq[i - 1].id || uniq[i - 1].getAttribute('data-screen-label') || '?') + '|' + (uniq[i].id || uniq[i].getAttribute('data-screen-label') || '?')); }
  out.fondosIguales = pares;
  // franjas (pestañas de color de los paneles): distintas entre sí y del fondo de su sección
  const fr = [];
  document.querySelectorAll('section').forEach(s => { const ds = [...s.querySelectorAll(':scope div[data-t][data-x][role="button"]')].filter(d => d.closest('section') === s); if (ds.length < 2) return;
    const bg = getComputedStyle(s).backgroundColor, cs = ds.map(d => getComputedStyle(d).backgroundColor);
    if (new Set(cs).size !== cs.length) fr.push((s.id || '?') + ': repetidas ' + cs.join(' '));
    if (cs.includes(bg)) fr.push((s.id || '?') + ': igual al fondo ' + bg);
    /* «parece el mismo color aunque no lo sean»: cada par de tonos (y cada tono con el fondo) separados al menos 20 puntos RGB */
    const rgb = c => (c.match(/\d+/g) || []).slice(0, 3).map(Number), dist = (x, y) => { const p = rgb(x), q = rgb(y); return Math.abs(p[0] - q[0]) + Math.abs(p[1] - q[1]) + Math.abs(p[2] - q[2]); };
    const all = cs.concat([bg]); for (let i = 0; i < all.length; i++) for (let j = i + 1; j < all.length; j++) if (all[i] !== all[j] && dist(all[i], all[j]) < 20) fr.push((s.id || '?') + ': tonos casi iguales ' + all[i] + ' ~ ' + all[j]); });
  out.franjas = fr;
  // migas en una línea (móvil)
  const bc = document.querySelector('nav[aria-label="Breadcrumb"]');
  const bcl = bc && (bc.querySelector('ol') || bc); out.migas = bc ? (bcl.getBoundingClientRect().height <= parseFloat(getComputedStyle(bcl).fontSize) * 2.2) : null;
  /* acentos das maiúsculas sem cortar (overflow:hidden com entrelinha justa cortava «INÍCIO») */
  out.migasAcento = bc ? [bc, bcl].every(e => getComputedStyle(e).overflow === 'visible' || parseFloat(getComputedStyle(e).lineHeight) / parseFloat(getComputedStyle(e).fontSize) >= 1.45) : null;
  // vídeos con póster
  out.sinPoster = [...document.querySelectorAll('video')].filter(v => !v.getAttribute('poster') && !v.closest('[data-hm-no-poster]')).length;
  return out;
};

const lineas = (sel, root = document) => [...root.querySelectorAll(sel)].filter(e => e.offsetParent || getComputedStyle(e).position === 'fixed').map(e => {
  const cs = getComputedStyle(e), r = document.createRange(); r.selectNodeContents(e); const rects = [...r.getClientRects()].filter(x => x.width > 1);
  const tops = new Set(rects.map(x => Math.round(x.top / 4))); const box = e.getBoundingClientRect(); const tw = r.getBoundingClientRect().width;
  return { t: e.textContent.trim().slice(0, 40), lines: tops.size, fs: parseFloat(cs.fontSize), overflow: tw > box.width + 1 || e.scrollWidth > e.clientWidth + 1, h: box.height };
});

(async () => {
  const b = await chromium.launch();
  const routes = Object.keys(PAGES).filter(r => !only || r.includes(only));
  // 1) generales: todas las rutas en móvil, tablet y PC
  for (const dev of (process.env.GEN === '0' ? [] : ['movil', 'tablet', 'pc'])) for (const route of routes) {
    const { ctx, p, errs } = await open(b, dev, route); await walk(p);
    /* em local, as imagens de fora (hortelamagenta.pt) e as que só existem no servidor não contam: a prova LIVE=1 apanha-as */
    await p.evaluate(m => { window.__hmLocal404 = m; }, p.__miss || []);
    const g = await p.evaluate(GENERAL);
    const probs = [];
    if (!g.ancho) probs.push('desborda en horizontal');
    if (errs.length) probs.push('errores JS ' + JSON.stringify(errs));
    if (g.imgRotas.length) probs.push('imágenes rotas ' + g.imgRotas.join(','));
    if (g.fondosIguales.length) probs.push('secciones seguidas con el mismo fondo ' + g.fondosIguales.join(' '));
    if (g.franjas.length) probs.push('franjas ' + g.franjas.join(' / '));
    if (dev !== 'pc' && g.migas === false) probs.push('migas en 2 líneas');
    if (g.migasAcento === false) probs.push('migas: acentos de mayúsculas recortados');
    if (dev === 'movil' && g.sinPoster) probs.push(g.sinPoster + ' vídeos sin póster (móvil)');
    rep(dev, route, 'general (ancho, errores, imágenes, fondos, franjas, migas, pósters)', !probs.length, probs.join(' · '));
    await ctx.close();
  }
  const has = r => routes.includes(r);
  const projs = routes.filter(r => r.startsWith('/projetos/') && r !== '/projetos/');

  const SOLO = process.env.SOLO; const run = k => !SOLO || k.includes(SOLO);
  // 2) Camolas · Rótulos: nombres en una línea en móvil (Laura, 2026-11-27)
  if (run('rotulos')) if (has('/projetos/camolas')) for (const dev of ['movil', 'movil360']) {
    const { ctx, p } = await open(b, dev, '/projetos/camolas'); await walk(p);
    const L = await p.evaluate(`(${lineas.toString()})('#rotulos [data-lpt]')`);
    const bad = L.filter(x => x.lines > 1 || x.overflow);
    rep(dev, '/projetos/camolas', 'Rótulos: nombres en una sola línea', L.length > 0 && !bad.length, bad.map(x => x.t + ' ' + x.lines + 'l').join(', ') || L.length + ' nombres a ' + L[0].fs.toFixed(1) + 'px');
    // O site: sin etiqueta de esquina en móvil
    const esq = await p.evaluate(() => { const e = document.querySelector('#digital span[data-x][data-on]'); return e ? getComputedStyle(e.parentElement).display : 'none'; });
    // la etiqueta de la esquina está dentro del div:has(>span[data-x][data-on]) (la otra, la de la barra de dirección, también tiene data-on)
    const esq2 = await p.evaluate(() => [...document.querySelectorAll('#digital div')].filter(d => d.querySelector(':scope > span[data-x][data-on]')).map(d => getComputedStyle(d).display));
    rep(dev, '/projetos/camolas', 'O site: sin etiqueta «01 Vinhos» en la esquina', esq2.every(d => d === 'none'), JSON.stringify(esq2));
    await ctx.close();
  }
  // 3) Camolas · O site: las tres capturas a la misma velocidad, ≤ 4× el scroll (Laura, 2026-11-27)
  if (run('osite')) if (has('/projetos/camolas')) for (const dev of ['movil', 'tablet', 'pc', 'portatil']) {
    const { ctx, p } = await open(b, dev, '/projetos/camolas');
    const top = await p.evaluate(() => { const r = document.querySelector('#digital'); return { top: r.getBoundingClientRect().top + scrollY, h: r.offsetHeight }; });
    const vh = DEV[dev].viewport.height, step = Math.round(vh * 0.05); let prev = null; const rate = {};
    for (let y = top.top - vh; y < top.top + top.h; y += step) { await p.evaluate(y => new Promise(res => { scrollTo(0, y); requestAnimationFrame(() => requestAnimationFrame(res)); }), y);
      const m = await p.evaluate(() => [...document.querySelectorAll('#digital [data-hm-shot]')].filter(s => s.offsetParent).map(s => s.getBoundingClientRect().top));
      if (prev) m.forEach((t, i) => { const d = prev[i] - t; if (d > 0.5) rate[i] = Math.max(rate[i] || 0, d / step); }); prev = m; }
    const v = Object.values(rate);
    rep(dev, '/projetos/camolas', 'O site: velocidad de las capturas ≤ 4× el scroll', v.length === 3 && v.every(x => x <= 4.0), v.map(x => x.toFixed(1) + '×').join(' / '));
    await ctx.close();
  }
  // 4) Branding y Design Web · Trabajos: nombres en una línea en móvil
  if (run('trabalhos')) for (const r of ['/servicos/branding', '/servicos/design-web']) if (has(r)) for (const dev of ['movil', 'movil360']) {
    const { ctx, p } = await open(b, dev, r); await walk(p);
    const L = await p.evaluate(`(${lineas.toString()})('#trabalhos-galeria [data-lpt], [data-hm-scroll] [data-lpt]')`);
    const bad = L.filter(x => x.lines > 1 || x.overflow);
    rep(dev, r, 'Trabajos: nombres en una sola línea', L.length > 0 && !bad.length, bad.map(x => x.t).join(', ') || L.length + ' nombres');
    await ctx.close();
  }
  // 5) Fichas de proyecto
  if (run('fichas')) for (const r of projs) {
    // 5a) móvil: Aplicaciones en carrusel, todas las imágenes a la misma altura; la sección siguiente no se sube encima
    for (const dev of ['movil', 'pc']) {
      const { ctx, p } = await open(b, dev, r); await walk(p);
      const ap = await p.evaluate(() => { const s = document.querySelector('#aplicacoes, #rotulos'); if (!s) return null;
        const hs = [...s.querySelectorAll('[data-lpi]')].map(e => Math.round(e.getBoundingClientRect().height)); const nx = s.nextElementSibling;
        return { hs, gap: nx ? Math.round(nx.getBoundingClientRect().top - s.getBoundingClientRect().bottom) : 0, pb: parseFloat(getComputedStyle(s.querySelector('[data-lp-st]') || s).paddingBottom) }; });
      if (ap) { const mn = Math.min(...ap.hs), mx = Math.max(...ap.hs);
        rep(dev, r, 'Aplicaciones/Rótulos: imágenes a la misma altura', mx - mn <= 3, ap.hs.join(','));
        rep(dev, r, 'Aplicaciones/Rótulos: la sección siguiente no se sube', ap.gap >= -1, 'separación ' + ap.gap + 'px, margen inferior ' + ap.pb + 'px'); }
      // 5b) «Más proyectos»: en móvil todos a color con nombre y «Ver projeto»
      if (dev === 'movil') {
        const mp = await p.evaluate(() => [...document.querySelectorAll('section[data-screen-label="09 Projetos"] [data-step] > a')].map(a => {
          const img = a.querySelector('div[data-x]'), sp = a.querySelectorAll(':scope > span'); const cs = img ? getComputedStyle(img) : null;
          return { cor: cs ? (+cs.opacity > 0.95) : false, nome: sp[3] ? +getComputedStyle(sp[3]).opacity > 0.9 && sp[3].textContent.trim().length > 1 : false, ver: sp[4] ? +getComputedStyle(sp[4]).opacity > 0.9 : false }; }));
        rep(dev, r, '«Mais projetos»: todos a color, con nombre y «Ver projeto»', mp.length > 0 && mp.every(x => x.cor && x.nome && x.ver), mp.length + ' tarjetas' + (mp.some(x => !x.cor) ? ' · alguna en gris' : '') + (mp.some(x => !x.nome || !x.ver) ? ' · sin nombre o sin «Ver projeto»' : ''));
        // 5c) O site / Filme: la leyenda por debajo del vídeo
        const gr = await p.evaluate(() => [...document.querySelectorAll('[data-grow]')].map(s => s.id || s.getAttribute('data-screen-label')));
        for (const gid of gr) {
          await p.evaluate(g => { const s = [...document.querySelectorAll('[data-grow]')].find(x => (x.id || x.getAttribute('data-screen-label')) === g); scrollTo(0, s.getBoundingClientRect().top + scrollY + s.offsetHeight - innerHeight - 10); }, gid); await p.waitForTimeout(700);
          const g = await p.evaluate(g => { const s = [...document.querySelectorAll('[data-grow]')].find(x => (x.id || x.getAttribute('data-screen-label')) === g); const ui = s.querySelector('[data-grow-ui]'); const v = s.querySelector('video, iframe, img');
            if (!ui || !v) return null; const vr = v.getBoundingClientRect(), ur = ui.getBoundingClientRect(); const gh = parseFloat(getComputedStyle(s).getPropertyValue('--hm-gh')); /* vídeo em object-fit: a parte visível é centro ± --hm-gh */
            return { vb: Math.round(gh ? Math.min(vr.bottom, (vr.top + vr.bottom) / 2 + gh) : vr.bottom), ut: Math.round(ur.top) }; }, gid);
          if (g) rep(dev, r, 'Vídeo «' + gid + '»: la leyenda queda debajo del vídeo', g.ut >= g.vb - 2, 'vídeo acaba ' + g.vb + ', leyenda empieza ' + g.ut);
        }
      }
      await ctx.close();
    }
    // tablet: «Mais projetos» a color con nombre
    const { ctx, p } = await open(b, 'tablet', r); await walk(p);
    const mp = await p.evaluate(() => [...document.querySelectorAll('section[data-screen-label="09 Projetos"] [data-step] > a')].map(a => { const img = a.querySelector('div[data-x]'), sp = a.querySelectorAll(':scope > span'); return (img ? +getComputedStyle(img).opacity > 0.95 : false) && (sp[3] ? +getComputedStyle(sp[3]).opacity > 0.9 : false) && (sp[4] ? +getComputedStyle(sp[4]).opacity > 0.9 : false); }));
    rep('tablet', r, '«Mais projetos»: todos a color, con nombre y «Ver projeto»', mp.length > 0 && mp.every(Boolean), mp.length + ' tarjetas');
    await ctx.close();
  }
  // 6) Listas desplegables (Âmbito): número y título centrados, texto separado de las líneas, efecto de escritura
  if (run('ambito')) for (const r of routes) {
    const html = fs.readFileSync(path.join(DIR, PAGES[r] + '.html'), 'utf8'); if (!html.includes('data-hm-amb')) continue;
    for (const dev of ['pc', 'movil']) {
      const { ctx, p } = await open(b, dev, r); await walk(p);
      await p.evaluate(() => { const g = document.querySelector('[data-hm-amb]'); scrollTo(0, g.getBoundingClientRect().top + scrollY - 120); }); await p.waitForTimeout(500);
      const btn = await p.$('[data-hm-amb] h3 button'); if (dev === 'pc') await btn.hover(); else if (await btn.getAttribute('aria-expanded') !== 'true') await btn.tap(); await p.waitForTimeout(1500);
      const a = await p.evaluate(() => { const g = document.querySelector('[data-hm-amb]'); const bt = g.querySelector('h3 button'); const sp = bt.querySelectorAll(':scope > span'); const r0 = sp[0].getBoundingClientRect(), r1 = (bt.querySelector('[data-acc-ico]') || sp[1]).getBoundingClientRect();
        const words = g.querySelectorAll('[data-on*="blur"], [data-on*="opacity"]').length; const panel = bt.closest('h3').nextElementSibling; const pr = panel ? panel.getBoundingClientRect() : null; const txt = panel ? panel.querySelector('p, ul') : null; const tr = txt ? txt.getBoundingClientRect() : null;
        const ico = bt.querySelector('[data-acc-ico]') || sp[1]; const rg = document.createRange(); rg.selectNodeContents(ico); const l1 = [...rg.getClientRects()].filter(x => x.width > 4)[0]; const rn = document.createRange(); rn.selectNodeContents(sp[0]); const n1 = [...rn.getClientRects()].filter(x => x.width > 2)[0];
        /* desenho: o número assenta na linha de base da 1.ª linha do título (Spartan: descendente 0,257 em) */
        const base = (r, el) => r.bottom - 0.257 * parseFloat(getComputedStyle(el).fontSize);
        const ctr = tr && pr && innerWidth >= 768 ? Math.round(Math.abs((bt.getBoundingClientRect().top + bt.getBoundingClientRect().bottom) / 2 - (tr.top + tr.bottom) / 2)) : 0;
        return { dc: Math.round(Math.abs(base(n1, sp[0]) - base(l1, ico))), ctr, words, abaixo: pr && tr ? Math.round(pr.bottom - tr.bottom) : null, acima: pr && tr ? Math.round(tr.top - pr.top) : null }; });
      rep(dev, r, 'Desplegables: número en la línea del título, título centrado con el texto, texto con aire y escritura palabra a palabra', a.dc <= 4 && a.ctr <= 24 && a.words > 5 && (a.abaixo === null || a.abaixo >= 12) && (a.acima === null || a.acima >= 8), 'número ' + a.dc + 'px · centro ' + a.ctr + 'px · palabras ' + a.words + ' · aire arriba ' + a.acima + ' abajo ' + a.abaixo);
      await ctx.close();
    }
  }
  // 7) Coaching «Como funciona» y Sobre «Valores»: título centrado verticalmente con el texto
  if (run('linhas')) for (const [r, sel] of [['/servicos/coaching-de-marcas', 'li'], ['/sobre', 'li']]) if (has(r)) for (const dev of ['pc', 'movil']) {
    const { ctx, p } = await open(b, dev, r); await walk(p);
    const d = await p.evaluate(() => [...document.querySelectorAll('li')].filter(li => li.querySelector(':scope > h3') && li.querySelector(':scope > p, :scope > div > p') && getComputedStyle(li).display.includes('grid')).map(li => { const h = li.querySelector(':scope > h3'), t = li.querySelector(':scope > p, :scope > div > p'); const a = h.getBoundingClientRect(), c = t.getBoundingClientRect(); return Math.round(Math.abs((a.top + a.bottom) / 2 - (c.top + c.bottom) / 2)); }));
    if (dev === 'pc') rep(dev, r, 'Filas: título centrado con el texto', d.length > 0 && d.every(x => x <= 10), d.join(',') + ' px');
    await ctx.close();
  }
  // 8) Contacto: dirección en 3 líneas, misma letra que las otras columnas
  if (run('contacto')) if (has('/contacto')) for (const dev of ['pc', 'portatil']) {
    const { ctx, p } = await open(b, dev, '/contacto'); await walk(p);
    const c = await p.evaluate(() => { const a = [...document.querySelectorAll('a')].find(x => /Bombarda/.test(x.textContent)); if (!a) return null; const r = document.createRange(); r.selectNodeContents(a); const n = new Set([...r.getClientRects()].filter(x => x.width > 1).map(x => Math.round(x.top / 4))).size;
      const others = [...document.querySelectorAll('p, a')].filter(x => x.offsetParent && !x.closest('footer') && /^(Conte-nos|Instagram|LinkedIn)/.test(x.textContent.trim())).map(x => getComputedStyle(x).fontSize); return { n, fs: getComputedStyle(a).fontSize, others: [...new Set(others)] }; });
    rep(dev, '/contacto', 'Dirección en 3 líneas y misma letra que las columnas Orçamentos y Redes', c && c.n === 3 && c.others.length === 1 && c.others[0] === c.fs, JSON.stringify(c));
    await ctx.close();
  }
  // 9) Lightbox: la X sin borde rosa
  if (run('lightbox')) for (const r of ['/servicos/fotografia-e-video']) if (has(r)) {
    const { ctx, p } = await open(b, 'pc', r); await walk(p);
    await p.evaluate(() => { const e = document.querySelector('[data-lb] img, [data-lb]'); e.scrollIntoView({ block: 'center' }); }); await p.waitForTimeout(600);
    const el = await p.$('[data-lb] img'); if (el) { await el.click({ force: true }); await p.waitForTimeout(900); }
    const x = await p.evaluate(() => { const x = document.querySelector('[data-lb-x]'); if (!x) return null; const cs = getComputedStyle(x); return { ol: cs.outlineStyle === 'none' || parseFloat(cs.outlineWidth) === 0, bs: cs.boxShadow }; });
    rep('pc', r, 'Lightbox: la X sin borde de foco', x && x.ol && (x.bs === 'none' || !x.bs), JSON.stringify(x));
    await ctx.close();
  }
  // 10) Cursor grande: letra 12,5 px
  if (run('cursor')) if (has('/servicos/branding')) {
    const { ctx, p } = await open(b, 'pc', '/servicos/branding'); await walk(p);
    await p.evaluate(() => { const e = document.querySelector('[data-cursor]'); e.scrollIntoView({ block: 'center' }); }); await p.waitForTimeout(500);
    const bx = await p.evaluate(() => { const r = document.querySelector('[data-cursor]').getBoundingClientRect(); return [r.left + r.width / 2, r.top + r.height / 2]; });
    await p.mouse.move(bx[0] - 20, bx[1] - 20); await p.mouse.move(bx[0], bx[1], { steps: 6 }); await p.waitForTimeout(700);
    const f = await p.evaluate(() => { const c = [...document.querySelectorAll('div')].find(d => d.style.position === 'fixed' && d.style.width === '96px' && /50%/.test(d.style.borderRadius) && d.firstElementChild && d.textContent.trim()); return c ? getComputedStyle(c.firstElementChild).fontSize : null; });
    rep('pc', '/servicos/branding', 'Cursor grande: texto a 12,5 px', f === '12.5px', String(f));
    await ctx.close();
  }
  // 11) /servicos: el índice con más aire arriba; Administración pública: antetítulo en una línea
  if (run('indice')) if (has('/servicos')) { const { ctx, p } = await open(b, 'pc', '/servicos');
    const pt = await p.evaluate(() => { const s = document.querySelector('[data-screen-label="02 Acesso rápido"]'); return s ? parseFloat(getComputedStyle(s).paddingTop) : null; });
    rep('pc', '/servicos', 'Índice de servicios: margen superior ≥ 48 px', pt >= 48, pt + 'px'); await ctx.close(); }
  const adm = routes.find(r => /administracao-publica/.test(r));
  if (run('admin')) if (adm) for (const dev of ['pc', 'portatil']) { const { ctx, p } = await open(b, dev, adm);
    const e = await p.evaluate(() => { const pr = [...document.querySelectorAll('h1, p')].find(x => /^—\s*Design de Comunica/.test(x.textContent.trim())); if (!pr) return null; const r = document.createRange(); r.selectNodeContents(pr); return new Set([...r.getClientRects()].filter(x => x.width > 1).map(x => Math.round(x.top / 4))).size; });
    rep(dev, adm, 'Antetítulo «— Design de Comunicação…» en una línea', e === 1, e + ' líneas'); await ctx.close(); }
  // 12) Menú móvil: los 6 proyectos principales primero (comprobación en el HTML)
  { const h = fs.readFileSync(path.join(DIR, PAGES['/'] + '.html'), 'utf8'); const m = h.match(/pjItems:\s*(\[\[.*?\]\])/); const order = m ? JSON.parse(m[1]).map(x => x[1].split('/').pop()) : [];
    const top = ['camolas', 'queijaria-da-sao', 'farinhas-firmos', 'alsil', 'hospital-garcia-de-orta', 'livro-vilamoura'];
    rep('html', '/', 'Menú móvil: proyectos principales primero', top.every((s, i) => order[i] === s), order.slice(0, 7).join(',')); }
  // 13) Galerías continuas: ninguna galería «a golpes» (data-lp sin data-lpf)
  { const bad = routes.filter(r => /data-lp="/.test(fs.readFileSync(path.join(DIR, PAGES[r] + '.html'), 'utf8')));
    rep('html', '*', 'Galerías continuas (sin data-lp a golpes)', !bad.length, bad.join(', ')); }
  // 14) Títulos de cabecera en móvil: mismo tamaño, máximo 3 líneas (salvo las landings, que Laura acepta en 4)
  if (run('cabeceras')) { const sizes = {}; for (const r of ['/servicos', '/servicos/branding', '/servicos/design-web', '/projetos', '/projetos/alsil', '/sobre', '/blog', '/contacto'].filter(has)) {
      const { ctx, p } = await open(b, 'movil', r); const h = await p.evaluate(() => { const e = [...document.querySelectorAll('main h1, main h2, main [data-hero-display], main [style*="hdr-fit"]')].filter(e => e.offsetParent && e.getBoundingClientRect().top < innerHeight).sort((a, b) => parseFloat(getComputedStyle(b).fontSize) - parseFloat(getComputedStyle(a).fontSize))[0]; if (!e) return null; const tops = []; const tw = document.createTreeWalker(e, NodeFilter.SHOW_TEXT); let n;
        /* só o texto visível (sem as cópias aria-hidden nem as palavras escondidas do efeito) */
        while ((n = tw.nextNode())) { const el = n.parentElement; if (!n.textContent.trim() || el.closest('[aria-hidden="true"]')) continue; let o = 1, q = el; while (q && q !== e.parentElement) { o *= +getComputedStyle(q).opacity; q = q.parentElement; } if (o < 0.1) continue;
          const rg = document.createRange(); rg.selectNodeContents(n); [...rg.getClientRects()].filter(x => x.width > 6).forEach(x => { if (!tops.some(t => Math.abs(t - x.top) < x.height / 2)) tops.push(x.top); }); } return { fs: Math.round(parseFloat(getComputedStyle(e).fontSize)), lines: tops.length }; }); sizes[r] = h ? h.fs + 'px/' + h.lines + 'l' : '-'; await ctx.close(); }
    const fsz = new Set(Object.values(sizes).map(x => x.split('/')[0])); const many = Object.values(sizes).filter(x => parseInt(x.split('/')[1]) > 3);
    rep('movil', 'cabeceras', 'Títulos de cabecera: mismo tamaño y ≤ 3 líneas', fsz.size === 1 && !many.length, JSON.stringify(sizes)); }

  fs.writeFileSync(S + '/bateria-ultima.json', JSON.stringify(results, null, 1));
  console.log('\n' + (fails ? 'FALLAN ' + fails + ' de ' + results.length : 'TODO BIEN: ' + results.length + ' comprobaciones'));
  await b.close();
})();
