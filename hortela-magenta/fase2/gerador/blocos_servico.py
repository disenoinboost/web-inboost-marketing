"""Blocos das páginas de serviço e das landings (modelo: Branding). Marcação estática com os atributos que
hm-fx-servico.js reconhece (data-rotbox, data-step-v, data-lp, data-acc, data-colorize, data-rise...)."""
from base import esc, att
from blocos import img_tag, fit_box
from estilos import PAD, DASH, DASH_A, INK, TX, MU, eyebrow  # sistema de desenho comum
SR = 'position:absolute; width:1px; height:1px; margin:-1px; padding:0; border:0; overflow:hidden; clip:rect(0 0 0 0); clip-path:inset(50%); white-space:nowrap;'

# Rejilla comum das secções de duas colunas: esquerda e direita na proporção 5:7 (ver estilos.py)
from estilos import ROW, COL_L, COL_R  # noqa: E402


def _ulink(href, label, op=''):
    return f'<a href="{att(href)}" style="font-size:18px; color:{INK}; text-decoration:none; border-bottom:1px solid #D82E87; padding-bottom:4px;{op}">{esc(label)}</a>'


def hero(h):
    """h: crumbs [(nome, href)], h1 (texto), display: linhas (lista de str) + rot (lista de palavras rotativas) ou None,
    display_is_h1 (bool), intro, cta (href,label), cta2 (href,label), since (bool)."""
    crumbs = ''
    for i, (n, href) in enumerate(h['crumbs']):
        if i:
            crumbs += '<span aria-hidden="true" style="color:#D82E87;">—</span>'
        crumbs += f'<a href="{att(href)}" style="color:inherit; text-decoration:none;">{esc(n)}</a>' if href else f'<span aria-current="page">{esc(n)}</span>'
    lines = ''
    delays = [0.15, 0.27, 0.39, 0.51, 0.63]
    disp = h['display']
    # Sempre a estrutura e o tamanho de letra de Branding (3 linhas, antetítulo à mesma altura).
    # Títulos longos: as linhas de cima podem passar para a coluna da direita (width:max-content); a última fica à esquerda,
    # para não tocar no texto pequeno, que está em baixo à direita.
    wide = False
    for i, l in enumerate(disp):
        last = i == len(disp) - 1
        inner = esc(l)
        if last and h.get('rot'):
            words = h['rot']
            rw = ''.join(f'<span data-rw="" style="grid-area:1/1; display:block; width:max-content; transform:{"none" if j == 0 else "translateY(135%)"};">{esc(w)}</span>' for j, w in enumerate(words))
            inner = (esc(l) + ' ' if l else '') + f'<span data-rotbox="3400" style="display:inline-grid; overflow:hidden; line-height:1.02; padding:.24em 0 .24em; margin:-.24em 0 -.24em;">{rw}</span>'
        lines += f'<span aria-hidden="true" style="display:block; overflow:hidden; padding:.24em 0 .16em; margin:-.24em 0 -.16em;"><span data-hl="{delays[min(i, 4)]}" style="display:block; transform:none; ">{inner}</span></span>'
    full = ' '.join(l for l in disp if l) + ((' ' + h['rot'][0]) if h.get('rot') else '')
    disp_style = 'margin:0 0 0 -0.04em; font-weight:100; letter-spacing:-0.055em; line-height:1; font-size:clamp(45px, min(6.88vw, var(--hdr-fit), calc(33.3vh - 120px)), 99px);'
    disp_style += f' width:max-content; max-width:calc(100vw - 2 * {PAD});'
    # antetítulo numa só linha sempre que caiba no ecrã (2026-11-26: «Design de Comunicação para Administração Pública em Portugal»)
    eyebrow_style = f'margin:0 0 clamp(20px,3.5vh,40px); font-size:18px; font-weight:300; letter-spacing:.1em; text-transform:uppercase; color:{MU}; width:max-content; max-width:calc(100vw - 2 * {PAD}); '
    if h.get('display_is_h1'):
        top = f'<p style="{eyebrow_style}">{DASH_A} {esc(h["eyebrow"])}</p><h1 style="{disp_style}"><span style="{SR}">{esc(full)}</span>{lines}</h1>'
    else:
        top = f'<h1 style="{eyebrow_style}">{DASH_A} {esc(h["h1"])}</h1><p style="{disp_style}"><span style="{SR}">{esc(full)}</span>{lines}</p>'
    segs = ''
    if h.get('rot'):
        segs = '<div aria-hidden="true" style="display:flex; gap:8px;">' + ''.join(
            f'<span data-rseg="" data-on="background:#D82E87" data-off="background:rgba(28,27,35,.12)" style="display:block; width:40px; height:1.5px; background:{"#D82E87" if j == 0 else "rgba(28,27,35,.12)"}; transition:background 0.2s ease;"></span>' for j in range(len(h['rot']))) + '</div>'
    else:
        segs = '<div aria-hidden="true" style="display:flex; gap:8px;"><span style="display:block; width:40px; height:1.5px; background:#D82E87;"></span></div>'
    cta2 = f'<a href="{att(h["cta2"][0])}" style="font-size:18px; color:{INK}; text-decoration:none; opacity:.72;">{esc(h["cta2"][1])}</a>' if h.get('cta2') else ''
    since = f'<div data-hl-fade=".8" data-hl-from="translateY(12px)" style="display:flex; flex-direction:column; gap:16px; opacity:1; transform:none;">{segs}<span style="font-size:18px; color:{MU};">Desde 2007</span></div>'
    intro = f'<p data-type="load" style="margin:0; font-size:18px; line-height:1.5; color:{TX}; margin-bottom:26px;"><span data-split-src="">{esc(h["intro"])}</span></p><div data-hl-fade="1.1" data-hl-from="translateY(12px)" style="display:flex; gap:28px; flex-wrap:wrap; align-items:baseline;  opacity:1; transform:none;">{_ulink(h["cta"][0], h["cta"][1])}{cta2}</div>'
    if wide:
        body = (f'<div style="flex:1 0 auto; display:flex; flex-direction:column; justify-content:center; gap:clamp(28px,5vh,56px);">'
                f'<div>{top}</div>'
                f'<div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:flex-end; gap:clamp(24px,4vh,40px) clamp(32px,5vw,96px);">'
                f'<div style="flex:1 1 220px; min-width:0;">{since}</div><div style="flex:0 1 440px; min-width:0;">{intro}</div></div></div>')
    else:
        body = (f'<div style="flex:1 0 auto; display:flex; flex-wrap:wrap; align-items:stretch; gap:clamp(24px,4vh,40px) clamp(32px,5vw,96px);">\n'
                f'<div style="flex:1 1 var(--hdr-lb); min-width:0; display:flex; flex-direction:column; gap:clamp(24px,4vh,40px);">\n'
                f'<div style="margin:auto 0;">{top}</div>\n{since}\n</div>\n'
                f'<div style="flex:0 1 440px; display:flex; flex-direction:column; justify-content:flex-end;">{intro}</div>\n</div>')
    return f'''<section data-cursor-bg="light" data-screen-label="01 Cabeçalho" style="position:relative; background:#ffffff; color:{INK}; min-height:100svh; box-sizing:border-box; display:flex; flex-direction:column; gap:clamp(20px,4vh,44px); padding:var(--sp-hdr) {PAD} clamp(28px,6vh,56px) {PAD}; overflow:hidden;">
<div><nav aria-label="Breadcrumb" style="display:flex;  gap:10px; flex-wrap:wrap; font-size:18px; color:{MU};">{crumbs}</nav></div>
{body}
<div data-stripes="" aria-hidden="true" style="position:absolute; inset:0; z-index:5; overflow:hidden; pointer-events:none;"><span data-stripe="" data-veil="" style="position:absolute; left:0; right:0; bottom:0; height:200%; background:linear-gradient(to top, {h.get("veil", "#e8eced")} 50%, transparent 100%); transform:translate3d(0,100%,0); will-change:transform;"></span></div></section>'''


def panels(M, b, sec_id, label, bg='#ffffff'):
    """Painéis que se abrem (data-step-v), como «Ponto de partida» de Branding. b: eyebrow, title, text, cta, items[img,title,text,cap,pos]."""
    n = len(b['items'])
    bgs = ['#e8eced', '#dde3e7', '#f6f7f8', '#e8eced', '#dde3e7']
    ps = ''
    for i, it in enumerate(b['items']):
        on = i == 0
        lab = f'{i + 1:02d} · {it.get("short", it["title"])}'
        imgst = f'position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:{it.get("pos", "50% 0")}; {"opacity:1;" if on else "opacity:0; transform:scale(1.08);"} transition:opacity .8s ease, transform 1.2s ease;'
        d = M.wh(it['img'])
        wh = (' width="%d" height="%d"' % d) if d else ''
        cap = f'<p style="margin:14px 0 0; font-size:18px; letter-spacing:.06em; text-transform:uppercase; color:rgba(250,250,248,.65);">{esc(it["cap"])}</p>' if it.get('cap') else ''
        ps += f'''
    <div data-t="{i}" data-x="{i}" role="button" aria-expanded="{"true" if on else "false"}" tabindex="0" aria-label="{att(lab)}" data-on="flex-grow:5" data-off="flex-grow:1" style="position:relative; flex:{5 if on else 1} 1 0; min-width:0; min-height:0; overflow:hidden; background:{bgs[i % 5]}; transition:flex-grow .9s cubic-bezier(.76,0,.24,1);">
      <img data-x="{i}" data-on="opacity:1;transform:scale(1)" data-off="opacity:0;transform:scale(1.08)" src="{att(it["img"])}" alt="{att(it.get("alt", ""))}"{wh} loading="lazy" style="{imgst}">
      <span aria-hidden="true" data-x="{i}" data-on="opacity:1" data-off="opacity:0" style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(20,19,25,0) 15%, rgba(20,19,25,.5) 45%, rgba(20,19,25,.92) 100%); opacity:{1 if on else 0}; transition:opacity .6s;"></span>
      <p data-vl="" data-x="{i}" data-on="opacity:0" data-off="opacity:1" aria-hidden="true" style="position:absolute; left:20px; bottom:24px; margin:0; writing-mode:vertical-rl; transform:rotate(180deg); font-size:22px; font-weight:200; white-space:nowrap; color:{INK}; opacity:{0 if on else 1}; transition:opacity .4s;"><span style="color:inherit;">{i + 1:02d}</span> · {esc(it.get("short", it["title"]))}</p>
      <div data-x="{i}" data-on="opacity:1;transform:none" data-off="opacity:0;transform:translateY(16px)" style="position:absolute; left:clamp(20px,2.4vw,36px); right:clamp(20px,2.4vw,36px); bottom:clamp(20px,2.4vw,32px); color:#FAFAF8; {"opacity:1;" if on else "opacity:0; transform:translateY(16px);"} transition:opacity .6s ease .25s, transform .8s cubic-bezier(.2,.7,.2,1) .25s;">
        <p style="margin:0 0 10px; font-size:16px; font-variant-numeric:tabular-nums; color:rgba(250,250,248,.6); font-weight:400;">{i + 1:02d} / {n:02d}</p>
        <h3 data-fw="200" style="margin:0 0 12px; font-size:clamp(28px,2.08vw,32px); font-weight:200; letter-spacing:-0.03em; line-height:1.05;">{esc(it["title"])}</h3>
        <p style="margin:0; max-width:440px; font-size:18px; line-height:1.5; color:#FAFAF8; text-shadow:0 1px 12px rgba(20,19,25,.45);">{esc(it["text"])}</p>
        {cap}
      </div>
    </div>'''
    cta = _ulink(b['cta'][0], b['cta'][1]) if b.get('cta') else ''
    text = f'<p style="margin:0 0 26px; font-size:18px; line-height:1.5; color:{TX}; text-wrap:pretty;">{esc(b["text"])}</p>' if b.get('text') else ''
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-screen-label="{label}" style="background:{bg}; padding:var(--sp-block) {PAD} var(--sp-block) {PAD};">
  <div style="{ROW} align-items:flex-end;">
    <div style="{COL_L}">
      <p style="margin:0 0 24px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{MU};">{DASH_A} {esc(b["eyebrow"])}</p>
      <h2 style="margin:0; max-width:14ch; font-weight:100; font-size:clamp(40px,4.48vw,80px); letter-spacing:-0.05em; line-height:1.05;">{esc(b["title"])}</h2>
    </div>
    <div style="{COL_R}"><div style="max-width:52ch;">
      {text}
      {cta}
    </div></div>
  </div>
  <div data-step="0" data-step-v="" data-hover="" style="display:flex; gap:10px; height:clamp(540px,66vh,700px); margin-top:var(--sp-title);">{ps}
    </div>
</section>'''


def lista(b, sec_id, label, bg='#ffffff'):
    """Lista editorial estática (mesma composição das perguntas frequentes: coluna lateral + linhas).
    b: eyebrow, title, text, items [(titulo, texto)], numbered, cta, foot."""
    rows = ''
    for i, it in enumerate(b['items']):
        t, d = it[0], it[1] if len(it) > 1 else ''
        num = f'<span style="flex:none; min-width:2.2em; font-size:16px; font-variant-numeric:tabular-nums; color:{MU}; padding-top:.5em;">{i + 1:02d}</span>' if b.get('numbered', True) else ''
        desc = f'<p style="margin:12px 0 0; max-width:60ch; font-size:18px; line-height:1.5; color:{TX}; text-wrap:pretty;">{esc(d)}</p>' if d else ''
        rows += f'''
      <li data-rise="{min(i, 6) * 0.05:.2f}" style="display:flex; gap:clamp(12px,1.6vw,28px); align-items:flex-start; border-top:1px solid rgba(28,27,35,.14); padding:clamp(22px,2.2vw,32px) 0;">{num}<div style="min-width:0;"><h3 data-fw="300@1195:200" style="margin:0; font-size:clamp(21px,1.8vw,28px); font-weight:200; letter-spacing:-0.02em; line-height:1.28;">{esc(t)}</h3>{desc}</div></li>'''
    text = f'<p style="margin:0; max-width:34ch; font-size:18px; font-weight:300; line-height:1.5; color:{TX};">{esc(b["text"])}</p>' if b.get('text') else ''
    cta = f'<p style="margin:28px 0 0;">{_ulink(b["cta"][0], b["cta"][1])}</p>' if b.get('cta') else ''
    foot = f'<p data-rise="" style="margin:clamp(24px,3vw,40px) 0 0; max-width:60ch; font-size:18px; line-height:1.5; color:{TX};">{esc(b["foot"])}</p>' if b.get('foot') else ''
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-screen-label="{label}" style="background:{bg}; padding:var(--sp-block) {PAD} var(--sp-block) {PAD};">
  <div style="{ROW} row-gap:48px;">
    <div data-faq-side="" style="{COL_L} position:sticky; top:clamp(100px,14vh,140px);">
      <p style="margin:0 0 28px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{MU};">{DASH_A} {esc(b["eyebrow"])}</p>
      <h2 style="margin:0 0 28px; font-size:clamp(40px,3.84vw,74px); font-weight:100; letter-spacing:-0.05em; line-height:1.06;">{esc(b["title"])}</h2>
      {text}{cta}
    </div>
    <div style="{COL_R}">
      <ul style="list-style:none; margin:0; padding:0; border-bottom:1px solid rgba(28,27,35,.14);">{rows}
      </ul>{foot}
    </div>
  </div>
</section>'''


def texto(b, sec_id, label, bg='#ffffff'):
    """Bloco de texto em duas colunas: título grande à esquerda, parágrafos à direita."""
    import re as _re
    fmt = lambda p: _re.sub(r'\*\*(.+?)\*\*', r'<strong style="font-weight:400; color:#1C1B23;">\1</strong>', _re.sub(r'_(.+?)_', r'<em>\1</em>', esc(p)))
    paras = ''.join(f'<p data-rise="{min(i, 4) * 0.05:.2f}" style="margin:0 0 22px; font-size:18px; line-height:1.5; color:{TX}; text-wrap:pretty;">{fmt(p)}</p>' for i, p in enumerate(b['paras']))
    cta = _ulink(b['cta'][0], b['cta'][1]) if b.get('cta') else ''
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-screen-label="{label}" style="background:{bg}; padding:var(--sp-block) {PAD} var(--sp-block) {PAD};">
  <div style="{ROW}">
    <div style="{COL_L}">
      <p style="margin:0 0 24px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{MU};">{DASH_A} {esc(b["eyebrow"])}</p>
      <h2 style="margin:0; max-width:15ch; font-weight:100; font-size:clamp(40px,4.48vw,80px); letter-spacing:-0.05em; line-height:1.05;">{esc(b["title"])}</h2>
    </div>
    <div style="{COL_R} padding-top:clamp(0px,1vw,12px);"><div style="max-width:62ch;">{paras}{cta}</div></div>
  </div>
</section>'''


def frase(b, sec_id, label, bg='#e8eced'):
    """Frase destacada (como «Uma agência de comunicação, não só de sites» de Design Web)."""
    side = ''
    if b.get('text') or b.get('cta'):
        t = f'<p style="margin:0 0 22px; font-size:18px; line-height:1.5; color:{TX};">{esc(b["text"])}</p>' if b.get('text') else ''
        c = _ulink(b['cta'][0], b['cta'][1]) if b.get('cta') else ''
        side = f'<div style="{ROW} margin-top:clamp(32px,4vw,56px);"><div aria-hidden="true" style="{COL_L}"></div><div style="{COL_R}"><div style="max-width:52ch;">{t}{c}</div></div></div>'
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-screen-label="{label}" style="position:relative; padding:var(--sp-block) {PAD} var(--sp-block) {PAD}; background:{bg}; color:{INK};">{eyebrow(esc(b["eyebrow"]))}<h2 data-colorize="" style="margin:0; max-width:20ch; font-size:clamp(40px,4.64vw,74px); font-weight:100; letter-spacing:-0.05em; line-height:1.04;">{esc(b["title"])}</h2>{side}</section>'''


def trabalhos(M, b, sec_id='trabalhos'):
    """Introdução + galeria escura fixada com cartões de projeto (como «Trabalhos de branding»)."""
    intro = f'''<section data-cursor-bg="light" id="{sec_id}" data-screen-label="04 Trabalhos · introdução" style="position:relative; padding:var(--sp-block) {PAD} var(--sp-title) {PAD}; background:#f6f7f8; color:{INK};"><div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:flex-end; gap:28px 64px;"><div style="flex:1 1 340px; min-width:0;">{eyebrow("Projetos")}<h2 style="margin:0; max-width:12ch; font-size:clamp(40px,4.96vw,80px); font-weight:100; letter-spacing:-0.05em; line-height:1.06; color:{INK};">{esc(b["title"])}</h2></div><div style="flex:1 1 340px; max-width:480px; min-width:0;"><p data-rise="" style="margin:0 0 24px; font-size:18px; line-height:1.5; color:{TX};">{esc(b["text"])}</p>{_ulink("/projetos", "Ver todos os projetos →")}</div></div></section>'''
    cols = [('#4A4743', '#FAFAF8', 'rgba(250,250,248,.35)'), ('#a6b4c1', INK, 'rgba(28,27,35,.3)'), ('#dde3e7', INK, 'rgba(28,27,35,.3)'),
            ('#1C1B23', '#FAFAF8', 'rgba(250,250,248,.35)'), ('#e8eced', INK, 'rgba(28,27,35,.3)')]
    n = len(b['items'])
    arts = ''
    for i, it in enumerate(b['items']):
        bg, fg, ln = cols[i % len(cols)]
        tags = ''.join(f'<span style="display:flex; justify-content:space-between; gap:8px; padding:6px 0; border-bottom:1px solid {ln}; font-size:18px; white-space:nowrap;">{esc(t)}<span aria-hidden="true">›</span></span>' for t in it['tags'][:2])
        href = att(it['href'])
        arts += f'<article data-lpp="" data-cursor-bg="solid" style="position:relative; flex:none; width:min(86vw,760px); height:100%; background:{bg}; color:{fg}; overflow:hidden;"><div data-lpi="" style="position:absolute; left:0; top:0; width:100%; height:min(56%, calc(100% - 330px)); overflow:hidden; clip-path:inset(0 0 27.8% 0); -webkit-clip-path:inset(0 0 27.8% 0);">{img_tag(M, it["img"], it["alt"], "display:block; width:100%; height:100%; object-fit:cover; object-position:" + it.get("pos", "50% 50%") + "; transform:scale(1.08); transform-origin:50% 0;")}</div><div data-lpd="" style="position:absolute; left:clamp(20px,3vw,40px); top:calc(min(56%, calc(100% - 330px)) + 22px); display:grid; grid-template-columns:repeat(2,minmax(0,170px)); gap:6px 24px; opacity:0; transform:translateY(10px); transition:opacity .6s ease, transform .7s cubic-bezier(.2,.7,.2,1);">{tags}</div><a data-lpd="" data-lp-plus="" data-cursor="Ver projeto" href="{href}" aria-label="Ver projeto {att(it["name"])}" style="position:absolute; right:clamp(20px,3vw,40px); top:calc(min(56%, calc(100% - 330px)) + 20px); width:48px; height:48px; border-radius:50%; border:1px solid {ln}; display:grid; place-items:center; color:inherit; text-decoration:none; font-size:22px; font-weight:200; opacity:0; transform:translateY(10px); background:transparent; transition:opacity .6s ease, transform .7s cubic-bezier(.2,.7,.2,1), background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease;"><svg width="16" height="16" sc-camel-view-box="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true" style="display:block;"><path d="M8 2v12M2 8h12"></path></svg></a><p data-lpd="" style="position:absolute; left:clamp(20px,3vw,40px); right:clamp(20px,3vw,40px); top:calc(min(56%, calc(100% - 330px)) + 76px); margin:0; max-width:520px; font-size:18px; line-height:1.5; opacity:0; transform:translateY(10px); transition:opacity .6s ease .08s, transform .7s cubic-bezier(.2,.7,.2,1) .08s;">{esc(it["desc"])}</p><a data-lpt="" data-cursor="Ver projeto" href="{href}" style="position:absolute; left:clamp(20px,3vw,40px); bottom:52px; color:inherit; text-decoration:none; font-size:clamp(40px,3.68vw,51px); font-weight:100; letter-spacing:-0.045em; line-height:1; white-space:nowrap; opacity:.15; filter:blur(10px);">{esc(it["name"])}</a><p data-lpd="" style="position:absolute; left:clamp(20px,3vw,40px); bottom:22px; margin:0; font-size:16px; opacity:0; transform:translateY(10px); transition:opacity .6s ease, transform .7s cubic-bezier(.2,.7,.2,1);">{i + 1} / {n}</p></article>'
    gal = f'''<section data-cursor-bg="dark" id="{sec_id}-galeria" data-lpf="" data-tone="dark" data-dark="" data-screen-label="05 Trabalhos · galeria" style="position:relative; background:#1C1B23; color:#FAFAF8;">
<div data-lp-st="" style="position:sticky; top:0; height:100vh; min-height:620px; overflow:hidden;">
  {img_tag(M, b["bg"], "", "position:absolute; inset:0; width:100%; height:100%; object-fit:cover;")}
  <span data-lp-ov="" aria-hidden="true" style="position:absolute; inset:0; background:#141319; opacity:.3;"></span>
  <div data-lp-ct="" style="position:absolute; inset:0; display:flex; flex-direction:column; justify-content:space-between; padding:var(--sp-block) {PAD} clamp(32px,6vh,56px) {PAD};">
    <div style="display:flex; flex-wrap:wrap; gap:12px 48px; font-size:18px;"><span><span style="color:#D82E87;">—</span> {esc(b["title"].rstrip("."))}</span><span style="opacity:.7;">Continue a descer</span></div>
    <p style="margin:0; max-width:15ch; font-size:clamp(40px,4vw,61px); font-weight:100; letter-spacing:-0.045em; line-height:1.04;">{esc(b["statement"])}</p>
  </div>
  <div data-lp-track="" data-lb="" style="position:absolute; left:0; top:0; height:100%; display:flex; padding-left:min(84vw,1200px); will-change:transform;">{arts}</div>
</div>
</section>'''
    return intro + '\n\n' + gal


def testemunho(M, t, sec_id='testemunho', label='06 Testemunho', bg='#ffffff'):
    link = f'<a href="{att(t["href"])}" style="font-size:18px; color:{INK}; text-decoration:none; border-bottom:1px solid #D82E87; padding-bottom:4px;">{esc(t.get("link_label", "Ver o projeto →"))}</a>' if t.get('href') else ''
    eyebrow = t.get('eyebrow', 'O que dizem sobre nós')
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-screen-label="{label}" style="background:{bg}; padding:var(--sp-block) {PAD} var(--sp-block) {PAD};">
  <div style="display:flex; flex-wrap:wrap; gap:clamp(48px,6vw,112px); align-items:center;">
    <figure style="flex:999 1 520px; min-width:0; margin:0;">
      <p style="margin:0 0 24px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{MU};">{DASH_A} {esc(eyebrow)}</p>
      <p data-colorize="" style="margin:0; max-width:13ch; font-size:clamp(40px,4.48vw,80px); font-weight:100; letter-spacing:-0.05em; line-height:1.05; text-wrap:balance;">{esc(t["headline"])}</p>
      <blockquote data-rise="" style="margin:clamp(28px,4vh,44px) 0 0; max-width:56ch; font-size:18px; line-height:1.5; color:{TX}; text-wrap:pretty;"><span aria-hidden="true" style="color:#D82E87;">«</span>{esc(t["quote"])}<span aria-hidden="true" style="color:#D82E87;">»</span></blockquote>
      <figcaption data-rise="" style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:baseline; gap:12px 32px; margin-top:clamp(28px,4vh,44px); max-width:56ch;">
        <span style="display:flex; flex-direction:column; gap:6px;"><span style="display:flex; align-items:baseline; gap:12px; flex-wrap:wrap;"><span aria-hidden="true" style="color:#D82E87;">—</span><span style="font-size:18px; font-weight:400; color:{INK};">{esc(t["name"])}</span><span style="font-size:18px; color:rgba(28,27,35,.6);">{esc(t["company"])}</span></span><span style="padding-left:26px; font-size:18px; line-height:1.5; color:rgba(28,27,35,.6);">{esc(t["role"])}</span></span>
        {link}
      </figcaption>
    </figure>
    <figure data-reveal="up" style="flex:1 1 320px; max-width:480px; margin:0;">
      <div style="aspect-ratio:4 / 5; overflow:hidden; background:#EEEDEA;">{img_tag(M, t["img"], t["img_alt"], "display:block; width:100%; height:100%; object-fit:cover; object-position:" + t.get("pos", "50% 50%") + ";")}</div>
      <figcaption style="padding-top:12px; font-size:16px; font-weight:400; color:rgba(28,27,35,.6);">{esc(t["caption"])}</figcaption>
    </figure>
  </div>
</section>'''


def faq(b, prefix, sec_id='perguntas', label='07 Perguntas', bg='#f6f7f8'):
    items = ''
    for i, (q, a) in enumerate(b['items']):
        k = f'{prefix}-{i + 1}'
        items += f'''
      <div data-acc="" style="border-top:1px solid rgba(28,27,35,.14);">
        <h3 style="margin:0; font-weight:300;"><button data-fw="300@1195:200" type="button" data-acc-btn="" id="{k}-b" aria-controls="{k}" aria-expanded="false" style="width:100%; display:flex; justify-content:space-between; align-items:center; gap:24px; background:none; border:0; padding:clamp(22px,2.2vw,32px) 0; font:inherit; font-size:clamp(21px,1.8vw,28px); font-weight:200; letter-spacing:-0.02em; line-height:1.28; color:{INK}; text-align:left; cursor:pointer;">{esc(q)}<span aria-hidden="true" style="flex:none; display:flex; align-items:center; justify-content:center; width:24px; height:24px;"><span data-acc-ico="" data-on="background:#D82E87;border-color:#D82E87;transform:scale(1.15)" data-off="background:transparent;border-color:rgba(28,27,35,.3);transform:none" style="display:block; width:14px; height:14px; border-radius:50%; border:1px solid rgba(28,27,35,.3); background:transparent; transform:none; transition:background 0.2s ease, border-color 0.2s ease, transform .45s cubic-bezier(.76,0,.24,1);"></span></span></button></h3>
        <div data-acc-panel="" id="{k}" role="region" aria-labelledby="{k}-b" style="display:grid; grid-template-rows:0fr; transition:grid-template-rows 0.3s cubic-bezier(.76,0,.24,1);"><div style="overflow:hidden;"><p style="margin:0; padding:0 0 clamp(24px,2.4vw,34px); max-width:60ch; font-size:18px; line-height:1.5; color:{TX};">{esc(a)}</p></div></div>
      </div>'''
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-screen-label="{label}" style="background:{bg}; padding:var(--sp-block) {PAD} var(--sp-block) {PAD};">
  <div style="{ROW} row-gap:48px;">
    <div data-faq-side="" style="{COL_L} position:sticky; top:clamp(100px,14vh,140px);">
      <p style="margin:0 0 28px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{MU};">{DASH_A} Perguntas frequentes</p>
      <h2 style="margin:0 0 28px; font-size:clamp(40px,3.84vw,74px); font-weight:100; letter-spacing:-0.05em; line-height:1.06;">{esc(b["title"])}</h2>
      <p style="margin:0; max-width:34ch; font-size:18px; font-weight:300; line-height:1.5; color:{TX};">{esc(b["text"])}</p>
    </div>
    <div data-acc-group="" style="{COL_R} display:flex; flex-direction:column; border-bottom:1px solid rgba(28,27,35,.14);">{items}
    </div>
  </div>
</section>'''


def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def chips(b, sec_id, label, bg='#ffffff'):
    """Lista curta («Para quem desenhamos?»): título à esquerda, itens grandes à direita."""
    li = ''.join(f'<li data-rise="{min(i, 6) * 0.05:.2f}" style="border-top:1px solid rgba(28,27,35,.14); padding:clamp(18px,2vw,28px) 0; font-size:clamp(24px,2.4vw,38px); font-weight:200; letter-spacing:-0.035em; line-height:1.1;">{esc(x)}</li>' for i, x in enumerate(b['items']))
    text = f'<p style="margin:0; max-width:34ch; font-size:18px; font-weight:300; line-height:1.5; color:{TX};">{esc(b["text"])}</p>' if b.get('text') else ''
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-screen-label="{label}" style="background:{bg}; padding:var(--sp-block) {PAD} var(--sp-block) {PAD};">
  <div style="{ROW}">
    <div style="{COL_L}"><p style="margin:0 0 28px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{MU};">{DASH_A} {esc(b["eyebrow"])}</p><h2 style="margin:0 0 24px; font-size:clamp(40px,3.84vw,74px); font-weight:100; letter-spacing:-0.05em; line-height:1.06;">{esc(b["title"])}</h2>{text}</div>
    <ul style="{COL_R} list-style:none; margin:0; padding:0; border-bottom:1px solid rgba(28,27,35,.14);">{li}</ul>
  </div>
</section>'''


def premios(M, b, sec_id='premios', label='Prémios', bg='#ffffff'):
    def _box(it):
        bgs, inner = fit_box(M, it['img'], it['alt'])
        return f'<div style="position:relative; aspect-ratio:4/3; overflow:hidden; {bgs}">{inner}</div>'
    cards = ''.join(f'<figure data-rise="{i * 0.1:.1f}" style="margin:0; flex:1 1 280px; min-width:0;">{_box(it)}<figcaption style="margin-top:16px;"><p style="margin:0; font-size:clamp(22px,1.9vw,30px); font-weight:200; letter-spacing:-0.03em; line-height:1.1;">{esc(it["title"])}</p><p style="margin:8px 0 0; font-size:18px; color:{MU};">{esc(it["sub"])}</p></figcaption></figure>' for i, it in enumerate(b['items']))
    quote = f'<p data-rise="" style="margin:var(--sp-title) 0 0; max-width:40ch; font-size:clamp(24px,2.3vw,34px); font-weight:200; letter-spacing:-0.02em; line-height:1.3;">{esc(b["quote"])}</p>' if b.get('quote') else ''
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-screen-label="{label}" style="background:{bg}; padding:var(--sp-block) {PAD} var(--sp-block) {PAD};">
  <p style="margin:0 0 24px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{MU};">{DASH_A} {esc(b["eyebrow"])}</p>
  <h2 style="margin:0 0 var(--sp-title); max-width:14ch; font-weight:100; font-size:clamp(40px,4.48vw,80px); letter-spacing:-0.05em; line-height:1.05;">{esc(b["title"])}</h2>
  <div style="display:flex; flex-wrap:wrap; gap:40px clamp(24px,4vw,64px);">{cards}</div>{quote}
</section>'''


def links_rel(b, sec_id='especialidades', label='Especialidades', bg='#ffffff'):
    li = ''.join(f'<li data-rise="{min(i, 6) * 0.05:.2f}" style="border-top:1px solid rgba(28,27,35,.14);"><a href="{att(h)}" style="display:flex; justify-content:space-between; align-items:baseline; gap:24px; padding:clamp(18px,2vw,26px) 0; color:{INK}; text-decoration:none; font-size:clamp(22px,2vw,32px); font-weight:200; letter-spacing:-0.03em; line-height:1.1;">{esc(l)}<span aria-hidden="true" style="font-size:18px; color:#D82E87;">→</span></a></li>' for i, (h, l) in enumerate(b['items']))
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-screen-label="{label}" style="background:{bg}; padding:var(--sp-block) {PAD} var(--sp-block) {PAD};">
  <div style="{ROW}">
    <div style="{COL_L}"><p style="margin:0 0 24px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{MU};">{DASH_A} {esc(b["eyebrow"])}</p><h2 style="margin:0; font-size:clamp(34px,2.88vw,51px); font-weight:100; letter-spacing:-0.045em; line-height:1;">{esc(b["title"])}</h2></div>
    <ul style="{COL_R} list-style:none; margin:0; padding:0; border-bottom:1px solid rgba(28,27,35,.14);">{li}</ul>
  </div>
</section>'''


def contacto_s(title, text, cta_label, cta_href='/contacto', label='08 Contacto'):
    """Contacto com cores fixas (modelo Branding)."""
    from blocos import contacto
    return contacto(title, text, cta_label, cta_href, tone_attr='', bg='#e8eced', ink=INK, mu=MU, tx=TX, label=label)


def imagens(M, b, sec_id, label, bg='#ffffff'):
    """Faixa de fotografias de projetos reais, à mesma altura e sem cortes (cada uma com a sua proporção); legenda com ligação.
    b: items [img, alt, cap, href], eyebrow/title opcionais."""
    figs = ''
    for i, it in enumerate(b['items']):
        w, h = M.wh(it['img']) or (4, 3)
        r = w / h
        cap = ''
        if it.get('cap'):
            inner = f'<a href="{att(it["href"])}" style="color:{INK}; text-decoration:underline; text-decoration-color:#D82E87; text-decoration-thickness:1px; text-underline-offset:5px;">{esc(it["cap"])}</a>' if it.get('href') else esc(it['cap'])
            cap = f'<figcaption style="margin-top:14px; font-size:18px; line-height:1.7; color:{MU};">{inner}</figcaption>'
        figs += (f'<figure data-rise="{min(i, 4) * 0.08:.2f}" style="margin:0; flex:{r:.3f} 1 calc({r:.3f} * 230px); min-width:0;">'
                 f'<div data-cursor-bg="solid" style="aspect-ratio:{w}/{h}; overflow:hidden; background:#f6f7f8;">{img_tag(M, it["img"], it["alt"], "display:block; width:100%; height:100%; object-fit:cover;")}</div>{cap}</figure>')
    head = ''
    if b.get('title'):
        head = (f'<p style="margin:0 0 24px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{MU};">{DASH_A} {esc(b.get("eyebrow", ""))}</p>'
                f'<h2 style="margin:0 0 var(--sp-title); max-width:18ch; font-weight:100; font-size:clamp(40px,4.48vw,80px); letter-spacing:-0.05em; line-height:1.05;">{esc(b["title"])}</h2>')
    pad = 'var(--sp-block)'
    top = '0px' if b.get('joined') else pad
    jn = ' data-hm-joined=""' if b.get('joined') else ''
    return f'''<section data-cursor-bg="light" id="{sec_id}"{jn} data-screen-label="{label}" style="background:{bg}; padding:{top} {PAD} {pad} {PAD};">
  {head}<div style="display:flex; flex-wrap:wrap; align-items:flex-start; gap:28px clamp(12px,1.6vw,24px);">{figs}</div>
</section>'''


def _escrita(txt):
    """Texto que se escreve palavra a palavra ao abrir (como a lista de serviços da página inicial): cada palavra passa de
    transparente e desfocada a nítida, com .018 s entre palavras; ao fechar desaparece de uma vez."""
    out = []
    for j, w in enumerate(txt.split()):
        out.append(f'<span data-acc-ico="" data-on="opacity:1;filter:blur(0px);transition-delay:{.08 + j * .018:.3f}s" data-off="opacity:0;filter:blur(4px);transition-delay:0s" style="opacity:0; filter:blur(4px); transition:opacity .35s ease, filter .3s ease;">{esc(w)} </span>')
    return ''.join(out)


def ambito(b, sec_id, label, bg='#ffffff'):
    """Lista em linhas grandes que se abrem (como «Âmbito e orçamento» de Design Web): número + palavra grande à esquerda;
    ao abrir (passar o cursor ou tocar), a palavra acende e o texto aparece à direita com o traço magenta.
    Usa o acordeão do desenho (data-acc, fx-servico); a abertura ao passar o cursor está em capa-fix (data-hm-amb).
    b: eyebrow, title, text, items [(titulo, texto)], cta, foot, hint ('etapa', 'tema'…).
    Aberta, a linha ganha espaço por cima e por baixo, com as mesmas medidas da lista de serviços da página inicial.
    padding-top:.23em na palavra: na Spartan sobram ~.27em por baixo da linha de base e ~.04em por cima das maiúsculas;
    assim o espaço visível por cima e por baixo da palavra fica igual."""
    rows = ''
    for i, it in enumerate(b['items']):
        t, d = it[0], it[1] if len(it) > 1 else ''
        k = f'{sec_id}-{i + 1}'
        op = ' data-acc-open=""' if i == 0 else ''
        rows += f'''
    <div data-acc=""{op} data-on="padding-top:clamp(16px,2vw,32px);padding-bottom:clamp(16px,2vw,32px)" data-off="padding-top:0px;padding-bottom:0px" style="border-top:1px solid rgba(28,27,35,.12); display:flex; flex-wrap:wrap; align-items:center; column-gap:clamp(16px,4vw,80px); transition:padding .45s cubic-bezier(.33,1,.68,1);">
      <h3 style="margin:0; flex:1 1 480px; min-width:0; font-weight:300;"><button type="button" data-acc-btn="" id="{k}-b" aria-controls="{k}" aria-expanded="false" style="display:flex; align-items:baseline; gap:clamp(12px,1.6vw,28px); width:100%; background:none; border:0; padding:clamp(8px,1.1vw,16px) 0; font:inherit; text-align:left; cursor:pointer; color:{INK};"><span style="flex:none; min-width:1.6em; font-size:16px; font-variant-numeric:tabular-nums; color:{MU}; font-weight:300;">{i + 1:02d}</span><span data-acc-ico="" data-on="color:#1C1B23" data-off="color:rgba(28,27,35,.26)" style="min-width:0; padding-top:.23em; font-size:clamp(36px,4.6vw,80px); font-weight:100; letter-spacing:-0.05em; line-height:1.14; color:rgba(28,27,35,.26); transition:color .35s ease; text-wrap:balance;">{esc(t)}</span></button></h3>
      <div data-acc-panel="" id="{k}" role="region" aria-labelledby="{k}-b" style="flex:0 1 440px; min-width:0; display:grid; grid-template-rows:0fr; transition:grid-template-rows .45s cubic-bezier(.33,1,.68,1);"><div style="overflow:hidden; min-height:0;"><div style="padding:clamp(10px,1.2vw,20px) 0 clamp(18px,2vw,32px);"><span data-acc-ico="" data-on="transform:scaleX(1)" data-off="transform:scaleX(0)" aria-hidden="true" style="display:block; width:32px; height:1px; margin-bottom:18px; background:#D82E87; transform-origin:0 50%; transform:scaleX(0); transition:transform .9s cubic-bezier(.22,1,.36,1);"></span><p style="margin:0; max-width:420px; font-size:18px; line-height:1.5; color:{TX}; text-wrap:pretty;">{_escrita(d)}</p></div></div></div>
    </div>'''
    side = ''
    if b.get('text'):
        side += f'<p style="margin:0 0 22px; font-size:18px; line-height:1.5; color:{TX};">{esc(b["text"])}</p>'
    if b.get('foot'):
        side += f'<p style="margin:0 0 22px; font-size:18px; line-height:1.5; color:{TX};">{esc(b["foot"])}</p>'
    if b.get('cta'):
        side += _ulink(b['cta'][0], b['cta'][1])
    side = f'<div style="flex:0 1 440px; min-width:0;">{side}</div>' if side else ''
    hint = b.get('hint', 'etapa')
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-screen-label="{label}" style="position:relative; background:{bg}; padding:var(--sp-block) {PAD} var(--sp-block) {PAD}; color:{INK};">
  <div style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:24px clamp(40px,6vw,120px);">
    <div style="flex:1 1 420px; min-width:0;"><p style="margin:0 0 24px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{MU};">{DASH_A} {esc(b["eyebrow"])}</p><h2 style="margin:0; max-width:14ch; font-size:clamp(40px,4.48vw,80px); font-weight:100; letter-spacing:-0.05em; line-height:1.05;">{esc(b["title"])}</h2></div>
    {side}
  </div>
  <p style="margin:clamp(48px,6vw,88px) 0 var(--sp-title) 0; text-align:right; font-size:18px; color:rgba(28,27,35,.6);"><span data-hm-hint-fine="">Passe o cursor sobre cada {hint}</span><span data-hm-hint-touch="">Toque em cada {hint}</span></p>
  <div data-acc-group="" data-hm-amb="" style="border-bottom:1px solid rgba(28,27,35,.12);">{rows}
  </div>
</section>'''


def galeria(M, b, sec_id, label, bg='#e8eced'):
    """Galeria em filas que andam sozinhas, se arrastam e abrem em grande (como «Conteúdos» de Design Web).
    b: eyebrow, title, text, links [(href, label)], rows [[{img, alt} | {video, poster, alt}]]; sem title = faixa simples."""
    def cell(it, hidden=False):
        src = it['poster'] if it.get('video') else it['img']
        r = max(.66, min(1.8, M.ratio_f(src)))
        box = f'flex:none; height:clamp(150px,17vw,250px); aspect-ratio:{r:.3f}; margin-right:16px; overflow:hidden; background:#EEEDEA;'
        if it.get('video'):
            inner = f'<video data-video="" src="{att(it["video"])}" poster="{att(it["poster"])}" muted="" loop="" playsinline="" preload="none" aria-hidden="true" style="display:block; width:100%; height:100%; object-fit:cover;"></video>'
        else:
            inner = img_tag(M, it['img'], '' if hidden else it.get('alt', ''), 'display:block; width:100%; height:100%; object-fit:cover;')
        return f'<div style="{box}">{inner}</div>'
    speeds = [('-1', '.45'), ('1', '.35'), ('-1', '.4')]
    rows = ''
    for k, row in enumerate(b['rows']):
        d, sp = speeds[k % 3]
        # duas metades iguais (o marquee do desenho volta ao início a meio da largura); cada metade com ≥ ~2600 px
        est = sum(min(1.8, max(.66, M.ratio_f(it['poster'] if it.get('video') else it['img']))) * 250 + 16 for it in row) or 1
        reps = max(1, -(-2600 // int(est)))
        half = ''.join(cell(it, hidden=(j >= len(row))) for j, it in enumerate(row * reps))
        rows += f'<div aria-hidden="true" style="overflow:hidden;"><div data-mq-drag="" data-lb="" data-cursor="Arraste" data-marquee="{d}" data-speed="{sp}" style="display:flex; width:max-content; will-change:transform;">{half}{half}</div></div>'
    head = ''
    if b.get('title'):
        links = ''.join(_ulink(h, l) if i == 0 else f'<a href="{att(h)}" style="font-size:18px; color:{INK}; text-decoration:none; opacity:.72;">{esc(l)}</a>' for i, (h, l) in enumerate(b.get('links', [])))
        links = f'<div style="display:flex; flex-wrap:wrap; gap:16px 28px;">{links}</div>' if links else ''
        head = f'''<div style="padding:0 {PAD}; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:flex-end; gap:24px 64px; margin-bottom:var(--sp-title);"><div style="flex:1 1 420px; min-width:0;"><p style="margin:0 0 24px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{MU};">{DASH_A} {esc(b["eyebrow"])}</p><h2 style="margin:0; max-width:14ch; font-size:clamp(40px,4.48vw,80px); font-weight:100; letter-spacing:-0.05em; line-height:1.05;">{esc(b["title"])}</h2></div><div style="flex:0 1 460px; min-width:0;"><p style="margin:0 0 24px; font-size:18px; line-height:1.5; color:{TX};">{esc(b["text"])}</p>{links}</div></div>'''
    top = '0px' if b.get('joined') else 'var(--sp-block)'
    jn = ' data-hm-joined=""' if b.get('joined') else ''
    return f'''<section data-cursor-bg="light" id="{sec_id}"{jn} data-screen-label="{label}" style="position:relative; padding:{top} 0 var(--sp-block) 0; background:{bg}; color:{INK}; overflow:hidden;">{head}<div style="display:flex; flex-direction:column; gap:16px;">{rows}</div></section>'''


def linhas(b, sec_id, label, bg='#ffffff'):
    """Linhas sempre visíveis, como «Uma forma de estar descontraída» de Sobre: número e palavra grande à esquerda, texto à
    direita, centrado na vertical com a palavra (padding-top:.23em compensa o espaço que a Spartan deixa por baixo da linha de base).
    b: eyebrow, title, text, foot, cta, items [(titulo, texto)]."""
    li = ''.join(f'''
    <li data-rise="{min(i, 6) * 0.05:.2f}" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(min(100%,320px),1fr)); gap:12px clamp(32px,5vw,96px); align-items:center; padding:clamp(22px,3vw,40px) 0; border-bottom:1px solid rgba(28,27,35,.12);"><h3 style="margin:0; padding-top:.23em; display:flex; align-items:baseline; gap:clamp(16px,2vw,28px); font-size:clamp(40px,5.12vw,94px); font-weight:100; letter-spacing:-0.055em; line-height:1;"><span style="font-size:16px; letter-spacing:0; color:{MU}; font-variant-numeric:tabular-nums; font-weight:300;">{i + 1:02d}</span>{esc(it[0])}</h3><p style="margin:0; max-width:46ch; font-size:18px; font-weight:300; line-height:1.5; color:{TX}; text-wrap:pretty;">{esc(it[1])}</p></li>''' for i, it in enumerate(b['items']))
    side = ''
    for k in ('text', 'foot'):
        if b.get(k):
            side += f'<p style="margin:0 0 22px; font-size:18px; line-height:1.5; color:{TX};">{esc(b[k])}</p>'
    if b.get('cta'):
        side += _ulink(b['cta'][0], b['cta'][1])
    side = f'<div style="flex:0 1 440px; min-width:0;">{side}</div>' if side else ''
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-screen-label="{label}" style="position:relative; background:{bg}; padding:var(--sp-block) {PAD} var(--sp-block) {PAD}; color:{INK};">
  <div style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:24px clamp(40px,6vw,120px); margin-bottom:var(--sp-title);">
    <div style="flex:1 1 420px; min-width:0;"><p style="margin:0 0 24px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{MU};">{DASH_A} {esc(b["eyebrow"])}</p><h2 style="margin:0; max-width:14ch; font-size:clamp(40px,4.48vw,80px); font-weight:100; letter-spacing:-0.05em; line-height:1.05;">{esc(b["title"])}</h2></div>
    {side}
  </div>
  <ul style="list-style:none; margin:0; padding:0; border-top:1px solid rgba(28,27,35,.12);">{li}
  </ul>
</section>'''

