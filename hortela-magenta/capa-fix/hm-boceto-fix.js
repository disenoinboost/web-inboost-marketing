/* Hortelã Magenta · correções sobre o boceto (versão móvel até 767 px). Sem dependências.
   1. Menu móvel: marca a página atual (e a secção a que pertence); Serviços e Projetos dobrados, com botão + para abrir.
   2. Textos laterais dos blocos fixados (data-marca / data-device): visíveis como fundo decorativo também no telemóvel.
   3. Painéis de processo (data-step-v): a troca é suave, como no computador (o painel aberto fecha-se enquanto o conteúdo
      se desvanece; o novo abre-se com a imagem a entrar e o texto a subir).
   4-8 (2026-11-05): opiniões com a cortada esbatida, carrossel de rótulos, cortinas horizontais (Camolas),
      pré-carga dos vídeos e barra «Neste projeto» no telemóvel. */
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
    tick = 0; railTick(); if (!MQ.matches) return;
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
        es.forEach(function (e) { e.target.classList.toggle('hm-peek', e.intersectionRatio < .92); });
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

  /* 6. Camolas · identidade: no telemóvel as cortinas abrem-se na horizontal (faixas) em vez de colunas */
  function curtains() {
    D.querySelectorAll('#identidade [data-step] > div:first-child > div[data-x]').forEach(function (el) {
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
  }, { rootMargin: '150% 0px 150% 0px' }) : null;
  function vids() {
    if (!vio) return;
    D.querySelectorAll('video[preload="none"]').forEach(function (v) { if (!v.__hmV) { v.__hmV = 1; vio.observe(v); } });
  }

  /* 8. Camolas · barra «Neste projeto»: o desenho só a mostra a partir de 900 px; aqui também no telemóvel */
  var rail = null, railA = [], railS = [];
  function railTick() {
    if (W.innerWidth >= 900) return;
    rail = rail || D.querySelector('[data-pidx]'); if (!rail) return;
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

  function init() { markMenu(); subMenus(); sides(); steps(); peeks(); lpN(); curtains(); vids(); req(); }
  /* o desenho é montado por JS: repetir até aparecer e quando o menu se abre */
  var n = 0, iv = setInterval(function () { init(); if (++n > 20) clearInterval(iv); }, 250);
  D.addEventListener('click', function () { setTimeout(function () { markMenu(); subMenus(); }, 0); }, true);
  W.addEventListener('scroll', req, { passive: true });
  W.addEventListener('resize', function () { curtains(); req(); });
  if (D.readyState !== 'loading') init(); else D.addEventListener('DOMContentLoaded', init);
})();
