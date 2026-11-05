/* Hortelã Magenta · correções sobre o boceto (versão móvel até 767 px). Sem dependências.
   1. Menu móvel: marca a página atual (e a secção a que pertence); Serviços e Projetos dobrados, com botão + para abrir.
   2. Textos laterais dos blocos fixados (data-marca / data-device): visíveis como fundo decorativo também no telemóvel.
   3. Painéis de processo (data-step-v): a troca é suave, como no computador (o painel aberto fecha-se enquanto o conteúdo
      se desvanece; o novo abre-se com a imagem a entrar e o texto a subir).
   4-8 (2026-11-05): opiniões com a cortada esbatida, carrossel de rótulos, cortinas horizontais (Camolas),
      pré-carga dos vídeos e barra «Neste projeto» no telemóvel.
   9-11 (2026-11-05, 3.ª ronda): vídeos e capturas leves no telemóvel, barra «Pedir orçamento · Ligar», fotografias
      variadas na galeria filtrada de Projetos.
   12 (2026-11-05, 4.ª ronda): setas nas opiniões e nos filtros de Projetos; pósteres e versões leves de todos os vídeos. */
(function () {
  if (window.__hmFix) return; window.__hmFix = 1;
  var D = document, W = window;
  var MQ = W.matchMedia ? W.matchMedia('(max-width: 767px)') : { matches: W.innerWidth <= 767 };
  var RED = W.matchMedia && W.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var EASE = 'cubic-bezier(.76,0,.24,1)';
  function clamp(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }
  function sm(x) { return x * x * (3 - 2 * x); }

  /* 1. menu móvel */
  var here = location.pathname.replace(/\/?$/, '/');
  here = { '/inicio/': '/', '/quanto-custa-um-site/': '/blog/quanto-custa-um-site/' }[here] || here;
  var secM = here.match(/^\/[^\/]+\//), sec = secM ? secM[0] : '';
  function markMenu() {
    var m = D.querySelector('[data-mobile]'); if (!m || here === '/') return;
    m.querySelectorAll('nav a[href]').forEach(function (a) {
      var h = a.getAttribute('href') || '', cur = h === here || (h === sec && a.parentElement && a.parentElement.tagName === 'NAV');
      if (cur && !a.hasAttribute('data-hm-cur')) { a.setAttribute('data-hm-cur', ''); if (h === here) a.setAttribute('aria-current', 'page'); }
      else if (!cur && a.hasAttribute('data-hm-cur')) a.removeAttribute('data-hm-cur');
    });
  }
  /* o menu é redesenhado pelo desenho quando abre: tudo idempotente, e o botão procura a lista pelo id ao ser tocado */
  function toggleSub(e) {
    e.preventDefault(); e.stopPropagation();
    var b = e.currentTarget, sub = D.getElementById(b.getAttribute('aria-controls')), a = b.previousElementSibling;
    if (!sub) return;
    var open = b.getAttribute('aria-expanded') !== 'true', name = a ? a.textContent.trim() : '';
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
    b.setAttribute('aria-label', (open ? 'Esconder ' : 'Mostrar ') + name);
    var s = sub.style; clearTimeout(sub.__t);
    if (open) {
      sub.classList.add('hm-open'); s.height = '0px'; var h = sub.scrollHeight; void sub.offsetHeight; s.height = h + 'px';
      sub.__t = setTimeout(function () { s.height = 'auto'; }, RED ? 0 : 320);
    } else {
      s.height = sub.scrollHeight + 'px'; void sub.offsetHeight; sub.classList.remove('hm-open'); s.height = '0px';
    }
  }
  function subMenus() {
    var nav = D.querySelector('[data-mobile] nav'); if (!nav) return;
    [].slice.call(nav.children).forEach(function (sub) {
      if (sub.tagName !== 'DIV') return;
      var a = sub.previousElementSibling, b = null;
      if (a && a.tagName === 'BUTTON') { b = a; a = a.previousElementSibling; }
      if (!a || a.tagName !== 'A') return;
      var id = 'hm-sub-' + (a.getAttribute('href') || '').replace(/[^a-z0-9]+/gi, '');
      if (sub.id !== id) sub.id = id;
      if (!a.classList.contains('hm-has-sub')) a.classList.add('hm-has-sub');
      if (!b) {
        b = D.createElement('button'); b.type = 'button'; b.className = 'hm-sub-btn';
        b.setAttribute('aria-expanded', 'false'); b.setAttribute('aria-label', 'Mostrar ' + a.textContent.trim());
        nav.insertBefore(b, sub);
      }
      b.setAttribute('aria-controls', id);
      if (!b.__hm) { b.__hm = 1; b.addEventListener('click', toggleSub); }
      if (!sub.classList.contains('hm-sub')) {
        sub.classList.add('hm-sub');
        if (b.getAttribute('aria-expanded') === 'true') { sub.classList.add('hm-open'); sub.style.height = 'auto'; }
      }
    });
  }

  /* 2. textos laterais */
  var secs = [];
  function sides() {
    D.querySelectorAll('[data-marca],[data-device]').forEach(function (el) {
      if (el.__hmS) return;
      var s = [].slice.call(el.querySelectorAll('[data-dev-side]')); if (s.length < 2) return;
      el.__hmS = 1; s[0].setAttribute('data-hm-side', 'l'); s[1].setAttribute('data-hm-side', 'r');
      secs.push({ el: el, l: s[0], r: s[1], vl: -1, vr: -1 });
    });
  }
  var tick = 0;
  function frame() {
    tick = 0; railTick(); ctaTick(); if (!MQ.matches) return;
    var vh = W.innerHeight;
    secs.forEach(function (o) {
      var r = o.el.getBoundingClientRect(); if (r.bottom < -vh || r.top > 2 * vh) return;
      var p = clamp(-r.top / Math.max(1, r.height - vh));
      var end = RED ? 1 : 1 - sm(clamp((p - .88) / .1));
      var l = Math.round((RED ? 1 : sm(clamp((p - .1) / .06))) * end * 100) / 100, rr = Math.round(end * 100) / 100;
      if (l !== o.vl) { o.vl = l; o.l.style.setProperty('--hm-so', l); }
      if (rr !== o.vr) { o.vr = rr; o.r.style.setProperty('--hm-so', rr); }
    });
  }
  function req() { if (!tick) tick = requestAnimationFrame(frame); }

  /* 3. painéis de processo */
  function fade(el, from, to, o) { if (el && el.animate) return el.animate([from, to], o); }
  function steps() {
    D.querySelectorAll('[data-step-v]').forEach(function (root) {
      if (root.__hmA) return; root.__hmA = 1;
      root.addEventListener('click', function (e) {
        if (!MQ.matches || RED) return;
        var t = e.target.closest('[data-t]'); if (!t || t.parentElement !== root || t.getAttribute('aria-expanded') === 'true') return;
        var ps = [].filter.call(root.children, function (c) { return c.hasAttribute('data-t'); });
        var olds = ps.filter(function (p) { return p.getAttribute('aria-expanded') === 'true' || p.classList.contains('hm-closing'); });
        var h0 = ps.map(function (p) { return p.offsetHeight; });
        var top0 = t.getBoundingClientRect().top;
        ps.forEach(function (p, i) {
          if (p.__tr === undefined) p.__tr = p.style.transition;
          p.style.setProperty('transition', 'height .85s ' + EASE + ', background-color .6s ease', 'important');
          p.style.setProperty('height', h0[i] + 'px', 'important');
        });
        olds.forEach(function (p) { p.classList.add('hm-closing'); });
        setTimeout(function () {
          /* o desenho já trocou aria-expanded: medir a altura final do novo painel */
          var h1 = ps.map(function (p) { return p.getAttribute('aria-expanded') === 'true' ? p.scrollHeight : 64; });
          void root.offsetHeight;
          var dy = 0, ti = ps.indexOf(t);
          ps.forEach(function (p, i) { p.style.setProperty('height', h1[i] + 'px', 'important'); if (i < ti) dy += h1[i] - h0[i]; });
          /* saída: o conteúdo do painel que fecha desvanece */
          olds.forEach(function (p) {
            if (p === t) return;
            [].forEach.call(p.children, function (c) {
              if (c.tagName === 'IMG') fade(c, { opacity: 1, transform: 'scale(1)' }, { opacity: 0, transform: 'scale(1.04)' }, { duration: 500, easing: 'ease', fill: 'both' });
              else if (c.tagName === 'DIV') fade(c, { opacity: 1, transform: 'none' }, { opacity: 0, transform: 'translate3d(0,-10px,0)' }, { duration: 300, easing: 'ease', fill: 'both' });
            });
          });
          /* entrada: imagem com fundido e zoom suave, texto a subir (os mesmos tempos do computador) */
          [].forEach.call(t.children, function (c) {
            if (c.tagName === 'IMG') fade(c, { opacity: 0, transform: 'scale(1.08)' }, { opacity: 1, transform: 'scale(1)' }, { duration: 1100, delay: 100, easing: 'ease', fill: 'backwards' });
            else if (c.tagName === 'DIV') fade(c, { opacity: 0, transform: 'translate3d(0,16px,0)' }, { opacity: 1, transform: 'none' }, { duration: 800, delay: 300, easing: 'cubic-bezier(.2,.7,.2,1)', fill: 'backwards' });
          });
          var top1 = top0 + dy;
          if (top1 < 80) W.scrollBy({ top: top1 - 88, behavior: 'smooth' });
          clearTimeout(root.__hmT);
          root.__hmT = setTimeout(function () {
            ps.forEach(function (p) {
              p.classList.remove('hm-closing'); p.style.removeProperty('height');
              p.style.removeProperty('transition'); if (p.__tr) p.style.transition = p.__tr;
              if (p.getAttribute('aria-expanded') !== 'true') [].forEach.call(p.children, function (c) { if (c.getAnimations) c.getAnimations().forEach(function (a) { a.cancel(); }); });
            });
          }, 900);
        }, 0);
      }, true);
    });
  }


  /* 4. (2026-11-05) opiniões: a que fica cortada à direita, esbatida (hm-peek) até entrar inteira */
  var IO = 'IntersectionObserver' in W;
  function peeks() {
    if (!IO) return;
    D.querySelectorAll('[data-op-tabs]').forEach(function (list) {
      if (list.__hmP) return; list.__hmP = 1;
      var o = new IntersectionObserver(function (es) {
        es.forEach(function (e) { var rb = e.rootBounds; e.target.classList.toggle('hm-peek', e.intersectionRatio < .92 && (!rb || e.boundingClientRect.right > rb.right - 2)); });
      }, { root: list, threshold: [0, .25, .5, .75, .92, 1] });
      [].forEach.call(list.children, function (t) { if (t.getAttribute('role') === 'tab') o.observe(t); });
    });
  }

  /* 5. galerias horizontais: nº de cartões (Camolas · rótulos usa-o para o texto fixo ocupar toda a fila) */
  function lpN() {
    D.querySelectorAll('[data-lp-track]').forEach(function (t) {
      var n = 0; [].forEach.call(t.children, function (c) { if (c.tagName === 'ARTICLE') n++; });
      if (n && t.__hmN !== n) { t.__hmN = n; t.style.setProperty('--hm-n', n); }
    });
  }

  /* 6. Camolas · identidade (só Camolas; Branding também tem #identidade): no telemóvel as cortinas abrem-se na horizontal (faixas) em vez de colunas */
  function curtains() {
    D.querySelectorAll('section#identidade[data-tone] [data-step]:not([data-step-v]) > div:first-child > div[data-x]').forEach(function (el) {
      var off = el.getAttribute('data-off') || '';
      if (el.__hmOff === undefined) el.__hmOff = off;
      var want = MQ.matches ? el.__hmOff.replace(/inset\(0 (\S+) 0 (\S+)\)/, 'inset($2 0 $1 0)') : el.__hmOff;
      if (off === want) return;
      el.setAttribute('data-off', want);
      var m = want.match(/clip-path:\s*([^;]+)/);
      if (m && el.style.zIndex === '1') el.style.clipPath = m[1];
    });
  }

  /* 7. vídeos com preload="none": começam a carregar ecrã e meio antes de aparecerem (o desenho só os pedia ao chegar) */
  var vio = IO ? new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return;
      var v = e.target; vio.unobserve(v);
      if (v.getAttribute('preload') !== 'none') return;
      v.setAttribute('preload', 'auto');
      var r = v.getBoundingClientRect();
      try { if (v.paused && v.readyState === 0 && (r.top > W.innerHeight || r.bottom < 0)) v.load(); } catch (x) {}
    });
  }, { rootMargin: '100% 0px 100% 0px' }) : null;
  function vids() {
    if (!vio) return;
    D.querySelectorAll('video').forEach(function (v) { if (MQ.matches) movil(v); });
    D.querySelectorAll('video[preload="none"]').forEach(function (v) { if (!v.__hmV) { v.__hmV = 1; vio.observe(v); } });
  }

  /* 8. Camolas · barra «Neste projeto»: o desenho só a mostra a partir de 900 px; aqui também no telemóvel */
  var rail = null, railA = [], railS = [];
  function railTick() {
    if (W.innerWidth >= 900) return;
    if (!rail || !rail.isConnected) { rail = D.querySelector('[data-pidx]'); railA = []; railS = []; } if (!rail) return;
    if (!railA.length) { railA = [].slice.call(rail.querySelectorAll('[data-pidx-a]')); railS = railA.map(function (a) { return D.querySelector(a.getAttribute('href')); }); }
    var vh = W.innerHeight, f = railS[0], l = railS[railS.length - 1]; if (!f || !l) return;
    var show = f.getBoundingClientRect().top < vh * .6 && l.getBoundingClientRect().bottom > vh * .4;
    if (rail.__hmShow !== show) { rail.__hmShow = show; rail.classList.toggle('hm-show', show); }
    if (!show) return;
    var act = 0; railS.forEach(function (s, k) { if (s && s.getBoundingClientRect().top <= vh * .45) act = k; });
    if (rail.__hmAct === act) return; rail.__hmAct = act;
    railA.forEach(function (a, k) { if (k === act) { a.setAttribute('data-hm-on', ''); a.setAttribute('aria-current', 'true'); } else { a.removeAttribute('data-hm-on'); a.removeAttribute('aria-current'); } });
    var li = railA[act].parentElement;
    rail.scrollTo({ left: Math.max(0, li.offsetLeft - (rail.clientWidth - li.offsetWidth) / 2), behavior: RED ? 'auto' : 'smooth' });
  }


  /* 9. (2026-11-05, 3.ª ronda) telemóvel: vídeos mais leves e capturas novas do site da Adega Camolas (uploads/hm-media/movil/) */
  var MV = '/wp-content/uploads/hm-media/movil/';
  var VMAP = {
    'hortela_magenta-showreel-clip_2025.mp4': 'showreel-clip-2025-movil',
    'hortelamagenta_portfolio_marca_camolas_video.mp4': 'camolas-filme-movil',
    'hortelamagenta-joao-bordeira-filme-camolas-design-label-small.mp4': 'camolas-joao-bordeira-movil',
    'hortelamagenta_portfolio_marca_camolas_catalogo.mp4': 'camolas-catalogo-movil',
    'hortelamagenta_portfolio_marca_camolas_site_04.mp4': 'camolas-site-04-movil',
    'hortelamagenta_portfolio_marca_alsilgroup_estacionario.mp4': 'alsil-estacionario-movil',
    'hortelamagenta_portfolio_marca_farinhafirmos_farinha_sacos_03.mp4': 'farinha-sacos-movil',
    'hortelamagenta_portfolio_marca_alsilgroup_video.mp4': 'alsil-video-mini',
    'HM-reel_2020.mp4': 'hm-reel-2020-movil'
  };
  /* cinta de miniaturas de Design Web (#conteudos): versões ainda mais pequenas */
  var MINI = { 'camolas-filme-movil': 'camolas-filme-mini', 'camolas-joao-bordeira-movil': 'camolas-joao-bordeira-mini' };
  var SMAP = { '99266298c7a73406.jpg': 'camolas-site-vinhos-movil.webp', '26d667bc8ea1fccf.jpg': 'camolas-site-regiao-movil.webp', '4c058854c64f119c.jpg': 'camolas-site-experiencias-movil.webp' };
  function movil(v) {
    var src = v.getAttribute('src') || '', f = src.split('/').pop(), name = src.indexOf(MV) === 0 ? f.replace(/\.mp4$/, '') : VMAP[f];
    if (!name) return;
    if (MINI[name] && v.closest('#conteudos')) name = MINI[name];
    if (!v.getAttribute('poster')) v.setAttribute('poster', MV + 'posters/' + name + '.webp');
    if (src === MV + name + '.mp4') return;
    var playing = !v.paused; v.setAttribute('src', MV + name + '.mp4');
    if (playing) { var pr = v.play && v.play(); if (pr && pr.catch) pr.catch(function () {}); }
  }
  function shots() {
    if (!MQ.matches) return;
    D.querySelectorAll('#digital picture source[srcset]').forEach(function (s) {
      var f = (s.getAttribute('srcset') || '').split('/').pop();
      if (!SMAP[f]) return;
      s.setAttribute('srcset', MV + SMAP[f]); s.setAttribute('type', 'image/webp'); s.setAttribute('width', '390'); s.setAttribute('height', '3200');
    });
  }

  /* 10. barra fixa «Pedir orçamento · Ligar» no telemóvel (aparece depois do primeiro ecrã; some no rodapé e em /contacto/) */
  var cta = null;
  function ctaBar() {
    if (cta || here.indexOf('/contacto/') === 0 || !D.body) return;
    cta = D.createElement('nav'); cta.className = 'hm-cta'; cta.setAttribute('aria-label', 'Contacto rápido');
    cta.innerHTML = '<a class="hm-cta-main" href="/contacto/">Pedir orçamento</a>' +
      '<a href="tel:+351211806292" aria-label="Ligar para a Hortelã Magenta: (+351) 211 806 292"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>Ligar</a>';
    D.body.appendChild(cta);
  }
  function ctaTick() {
    if (!cta) return;
    var on = false;
    if (MQ.matches && !D.querySelector('[data-mobile][aria-hidden="false"]')) {
      var vh = W.innerHeight, ft = D.querySelector('footer[data-screen-label], [data-screen-label*="Footer"]'), ct = D.getElementById('contacto');
      on = W.scrollY > vh * .6;
      if (on && ft && ft.getBoundingClientRect().top < vh) on = false;
      if (on && ct) { var r = ct.getBoundingClientRect(); if (r.top < vh * .7 && r.bottom > vh * .3) on = false; }
      /* secções de ecrã inteiro com botões em baixo (galeria de trabalhos, showreel): a barra não as tapa */
      if (on) [].forEach.call(D.querySelectorAll('#trabalhos-galeria, [data-reel]'), function (z) { var q = z.getBoundingClientRect(); if (q.top < vh - 60 && q.bottom > 80) on = false; });
    }
    if (cta.__on !== on) { cta.__on = on; cta.classList.toggle('hm-on', on); D.documentElement.classList.toggle('hm-cta-up', on); }
  }

  /* 11. Projetos · galeria filtrada: quando um projeto se repete, mostra outra fotografia do mesmo projeto */
  var PFX = '/wp-content/uploads/hm-media/hortelamagenta.pt/media/pages/projetos/';
  var POOL = {"livro-vilamoura":["09122571f9-1701272616/livro-vilamoura-cover-1800x.webp","6edf468bf6-1701272616/livro-vilamoura-img_02-950x.webp"],"imperalum":["7bae5f7d33-1739317592/hortelamagenta_portfolio_marca_imperalum_estacionario_01-1900x.webp","f3800cf11d-1739317292/hortelamagenta_portfolio_marca_imperalum_foto_01-1900x.webp","14bf0e96c3-1740759289/hortelamagenta_portfolio_marca_imperalum_banner_02-2400x.webp"],"knowledgebiz":["321a9cd129-1711539290/hortelamagenta_portfolio_marca_knowledgebiz_estacionario-1900x.webp","ee282865f6-1711539355/hortelamagenta_portfolio_marca_knowledgebiz_site_01-1900x.webp","41d543fd60-1711376064/hortelamagenta_portfolio_marca_knowledgebiz_banner-1900x.webp","acb8f0ddc8-1712331803/hortelamagenta_portfolio_marca_knowledgebiz_site_03-1900x.webp"],"camara-municipal-de-almada-roteiro":["ca85983fc0-1737996772/hortelamagenta_portfolio_marca_camera-municipal-de-almada_roteiro_capa-1200x.webp"],"consulai":["f492899131-1721829424/hortelamagenta_portfolio_marca_consulai_estacionario-1900x.webp","555bf500a9-1721821692/hortelamagenta_portfolio_marca_consulai_bottle-1900x.webp"],"farinhas-firmos":["7f27a0d0e0-1733915142/hortelamagenta_portfolio_marca_farinhafirmos_site_05-1900x.webp","12345640cf-1733915142/hortelamagenta_portfolio_marca_farinhafirmos_fabrica_09-950x.webp","20cfd38b8a-1733915142/hortelamagenta_portfolio_marca_farinhafirmos_calendario-1900x.webp","fd75baaf78-1736160048/hortelamagenta_portfolio_marca_farinhafirmos_fabrica-1900x.webp","e3a534ab47-1733915142/firmos_20210825_0055_hr_lr-1900x.webp","16f823843a-1733915142/hortelamagenta_portfolio_marca_farinhafirmos_redessociais_02-1900x.webp","0d8085f2b6-1733915142/hortelamagenta_portfolio_marca_farinhafirmos_farinha_sacos_02-1900x.webp","0d8085f2b6-1733915142/hortelamagenta_portfolio_marca_farinhafirmos_farinha_sacos_02-2400x.webp","8519297690-1733915142/hortelamagenta_portfolio_marca_farinhafirmos_fabrica_11-950x.webp"],"alinea":["0551698f70-1712332751/hortelamagenta_portfolio_alinea_capa-1200x.webp","6d50161d47-1710332766/hortelamagenta_portfolio_alinea_foto_01-950x.webp","33c4775e47-1710332840/hortelamagenta_portfolio_alinea_site_03-1900x.webp","dbafb4fd83-1710332713/hortelamagenta_portfolio_alinea_foto_03-950x.webp","07b0800a86-1710332776/hortelamagenta_portfolio_alinea_foto_02-950x.webp","8fb573ecfc-1710332790/hortelamagenta_portfolio_alinea_site_01-1900x.webp","9de4876d63-1710332653/hortelamagenta_portfolio_alinea_estacionario-1900x.webp"],"hospital-garcia-de-orta":["f7fbbaa315-1718375214/hortelamagenta_portfolio_marca_hgo_foto_01-950x.webp","c27930cb86-1736937441/hortelamagenta_portfolio_marca_hgo_capa-1200x.webp"],"documentos-normativos-imt":["ed2aa16f83-1736435754/hortelamagenta_portfolio_marca_imt_fasciaculo_capa-1200x.webp","2017b46299-1736432908/hortelamagenta_portfolio_marca_imt_fasciaculo_livro_01-1900x.webp"],"croma":["9377ea8d5d-1716976133/hortelamagenta_portfolio_marca_croma_foto-1900x.webp","78fb3bf26c-1716976201/hortelamagenta_portfolio_marca_croma_banner_02-2400x.webp"],"alsil":["d2144ed056-1734532126/alsilgroup_portfolio_marca_display-2400x.webp","be5cc9f6bd-1734959174/alsilgroup_portfolio_marca_stand-1900x.webp","979b7fe850-1734105167/hortelamagenta_portfolio_marca_alsilgroup_fabrica_01-1900x.webp","9c1cb9e731-1734105140/hortelamagenta_portfolio_marca_alsilgroup_cartao-de-visita-1900x.webp","2a93ca4ffe-1734715205/hortelamagenta_portfolio_marca_alsilgroup_fabrica_08-950x.webp","c2f6dc93f5-1734526716/hortelamagenta_portfolio_marca_alsilgroup_fabrica_04-950x.webp"],"camolas":["8ff25d922e-1736263859/hortelamagenta_portfolio_marca_camolas_garrafeira_02-1900x.webp","8065f08070-1736418209/hortelamagenta_portfolio_marca_camolas_cobaia_01-1900x.webp","be69d0f63a-1736268673/hortelamagenta_portfolio_marca_camolas_garrafeira_03-950x.webp","bd22f22426-1740738083/hortelamagenta_portfolio_marca_camolas_site_01-1900x.webp","93fc94cba4-1736267817/hortelamagenta_portfolio_marca_camolas_site_02-1900x.webp","0a24e03049-1740739416/hortelamagenta_portfolio_marca_camolas_monocasta_syrah_01-950x.webp","77614d917d-1736329416/hortelamagenta_portfolio_marca_camolas_grande-escolha_01-1900x.webp","2d4be057fa-1736177003/hortelamagenta_portfolio_marca_camolas_rollup-1900x.webp","b13a072826-1736418294/hortelamagenta_portfolio_marca_camolas_cobaia_03-1900x.webp","feffce8393-1736335730/hortelamagenta_portfolio_marca_camolas_moscatel-5-anos_04-1900x.webp"],"queijaria-da-sao":["bec50ba50e-1725318903/hortelamagenta_portfolio_marca_queijariadasao_site_01-1900x.webp","4146df1010-1725294355/hortelamagenta_portfolio_marca_queijariadasao_foto_06-1900x.webp","d71896b407-1725371731/hortelamagenta_portfolio_marca_queijariadasao_rotulos-1900x.webp","7686824007-1725283017/hortelamagenta_portfolio_marca_queijariadasao_veiculo-1900x.webp","57a9fce544-1725292582/hortelamagenta_portfolio_marca_queijariadasao_site_02-1900x.webp","dcbe49e55a-1725292989/hortelamagenta_portfolio_marca_queijariadasao_foto_05-1900x.webp"]};
  var used = {};
  function variety() {
    if (!MQ.matches) return;
    var mad = D.querySelector('[data-mad]'); if (!mad) return;
    if (!mad.__hmMo && W.MutationObserver) { mad.__hmMo = new MutationObserver(function () { used = {}; setTimeout(variety, 0); }); mad.__hmMo.observe(mad, { childList: true }); }
    mad.querySelectorAll('[data-madf] > a[aria-hidden="true"]').forEach(function (a) {
      if (a.__hmV) return; a.__hmV = 1;
      var m = (a.getAttribute('href') || '').match(/\/projetos\/([^\/?#]+)/); if (!m || !POOL[m[1]]) return;
      var slug = m[1], list = POOL[slug], img = a.querySelector('img'); if (!img) return;
      var cur = img.getAttribute('src') || '';
      /* roda pelas fotografias do projeto, a começar pelas que ainda não apareceram (a capa já está à vista) */
      var u = used[slug] || (used[slug] = { n: 0, cover: cur.split('/').pop() });
      var opts = list.filter(function (f) { return f.split('/').pop() !== u.cover; }); if (!opts.length) return;
      var f = opts[u.n++ % opts.length];
      img.removeAttribute('srcset'); img.setAttribute('src', PFX + slug + '/' + f);
    });
  }


  /* 12. (2026-11-05, 4.ª ronda) setas: opiniões (anterior/seguinte) e filtros de Projetos (deslizar a fila) */
  var SVG_L = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>';
  var SVG_R = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';
  function mkArrows(labelPrev, labelNext) {
    var n = D.createElement('div'); n.className = 'hm-arrows';
    n.innerHTML = '<button type="button" aria-label="' + labelPrev + '">' + SVG_L + '</button><button type="button" aria-label="' + labelNext + '">' + SVG_R + '</button>';
    return n;
  }
  function opArrows() {
    D.querySelectorAll('[data-op-tabs]').forEach(function (list) {
      /* um só par de setas por lista: se o desenho voltou a pintar a lista, as setas antigas saem */
      [].forEach.call(list.parentNode.querySelectorAll(':scope > .hm-arrows'), function (o) { if (o.__list !== list) o.remove(); });
      if (list.__hmArr && list.__hmArr.isConnected) return;
      var nav = mkArrows('Opinião anterior', 'Opinião seguinte'), b = nav.children; nav.__list = list;
      list.parentNode.insertBefore(nav, list.nextSibling); list.__hmArr = nav;
      function tabs() { return [].filter.call(list.children, function (t) { return t.getAttribute('role') === 'tab'; }); }
      function cur() { var t = tabs(); for (var i = 0; i < t.length; i++) if (t[i].getAttribute('aria-selected') === 'true') return i; return 0; }
      function show(i) { var t = tabs(); if (!t[i]) return; list.scrollTo({ left: t[i].offsetLeft - t[0].offsetLeft, behavior: RED ? 'auto' : 'smooth' }); }
      function state() { var i = cur(), n = tabs().length; b[0].disabled = i <= 0; b[1].disabled = i >= n - 1; }
      function go(d) { var t = tabs(), i = Math.max(0, Math.min(t.length - 1, cur() + d)); if (t[i]) { t[i].click(); show(i); } setTimeout(state, 50); }
      b[0].addEventListener('click', function () { go(-1); }); b[1].addEventListener('click', function () { go(1); });
      if (W.MutationObserver) new MutationObserver(function () { state(); }).observe(list, { attributes: true, subtree: true, attributeFilter: ['aria-selected'] });
      state();
    });
  }
  function filterArrows() {
    D.querySelectorAll('#filtros ol[role="group"]').forEach(function (ol) {
      var g = ol.parentNode; if (!g) return;
      [].forEach.call(g.querySelectorAll(':scope > .hm-arrows'), function (o) { if (o.__list !== ol) o.remove(); });
      if (ol.__hmArr && ol.__hmArr.isConnected) return;
      var name = (g.querySelector(':scope > p') || {}).textContent || '';
      var nav = mkArrows('Ver opções anteriores de ' + name.trim(), 'Ver mais opções de ' + name.trim()), b = nav.children;
      nav.__list = ol; g.appendChild(nav); ol.__hmArr = nav;
      function state() { var max = ol.scrollWidth - ol.clientWidth - 2; b[0].disabled = ol.scrollLeft <= 2; b[1].disabled = ol.scrollLeft >= max; }
      b[0].addEventListener('click', function () { ol.scrollBy({ left: -ol.clientWidth * .7, behavior: RED ? 'auto' : 'smooth' }); });
      b[1].addEventListener('click', function () { ol.scrollBy({ left: ol.clientWidth * .7, behavior: RED ? 'auto' : 'smooth' }); });
      ol.addEventListener('scroll', state, { passive: true }); W.addEventListener('resize', state); state();
    });
  }

  function init() { markMenu(); subMenus(); sides(); steps(); peeks(); lpN(); curtains(); vids(); shots(); ctaBar(); variety(); opArrows(); filterArrows(); req(); }
  /* o desenho é montado por JS: repetir até aparecer e quando o menu se abre */
  var n = 0, iv = setInterval(function () { init(); if (++n > 20) clearInterval(iv); }, 250);
  D.addEventListener('click', function () { setTimeout(function () { markMenu(); subMenus(); opArrows(); filterArrows(); }, 60); }, true);
  [6000, 10000].forEach(function (t) { setTimeout(function () { opArrows(); filterArrows(); vids(); }, t); });
  W.addEventListener('scroll', req, { passive: true });
  W.addEventListener('resize', function () { curtains(); req(); });
  if (D.readyState !== 'loading') init(); else D.addEventListener('DOMContentLoaded', init);
})();
