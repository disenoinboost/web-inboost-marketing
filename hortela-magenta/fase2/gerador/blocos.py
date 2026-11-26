"""Blocos do desenho (marcação copiada dos modelos de Claude Design, com os mesmos estilos em linha e atributos data-*
que os efeitos de hm-fx-projeto.js / hm-fx-servico.js / hm-movil.css reconhecem)."""
from base import esc, att

PAD = 'clamp(16px,4vw,64px)'
DASH = '<span style="color:#D82E87;">—</span>'
DASH_A = '<span aria-hidden="true" style="color:#D82E87;">—</span>'


def link_u(href, label, extra=''):
    return ('<a href="' + att(href) + '" style="font-size:18px; color:var(--ink,#1C1B23); text-decoration:none; border-bottom:1px solid #D82E87; padding-bottom:4px;' + extra + '">' + esc(label) + '</a>')


def img_tag(M, url, alt, style, eager=False, extra=''):
    d = M.wh(url)
    wh = (' width="%d" height="%d"' % d) if d else ''
    load = ' fetchpriority="high" decoding="async"' if eager else ' loading="lazy" decoding="async"'
    return '<img' + extra + ' src="' + att(url) + '" alt="' + att(alt) + '"' + wh + load + ' style="' + style + '">'


# Imagem inteira numa caixa de proporção qualquer (sem cortes em nenhum ecrã):
# gráficos de fundo liso -> contain sobre a cor da borda; fotografias -> contain sobre uma cópia desfocada da própria imagem.
def fit_box(M, url, alt, pos='50% 50%', force=None, eager=False, extra=''):
    e = M.edge(url)
    flat = bool(e) and e[1] <= 60
    if force == 'cover':
        return '', img_tag(M, url, alt, 'display:block; width:100%; height:100%; object-fit:cover; object-position:' + pos + ';', eager=eager, extra=extra)
    if flat or force == 'flat':
        bg = 'background:' + (e[0] if e else 'var(--ph)') + ';'
        return bg, img_tag(M, url, alt, 'position:relative; display:block; width:100%; height:100%; object-fit:contain;', eager=eager, extra=extra)
    blur = img_tag(M, url, '', 'position:absolute; inset:0; display:block; width:100%; height:100%; object-fit:cover; filter:blur(26px) saturate(1.05); transform:scale(1.2); opacity:.85;', extra=' aria-hidden="true"')
    main = img_tag(M, url, alt, 'position:relative; display:block; width:100%; height:100%; object-fit:contain;', eager=eager, extra=extra)
    return 'background:' + (e[0] if e else 'var(--ph)') + ';', blur + main


# =====================================================================================  PROJETO (modelo: Camolas)
def proj_header(M, p):
    cats = [c.strip() for c in p['cats'].split(',')]
    half = (len(cats) + 1) // 2
    l1 = ', '.join(cats[:half]) + (',' if len(cats) > half else '')
    l2 = ', '.join(cats[half:])
    lines = '<span style="display:block; overflow:hidden;"><span data-hl="0.45" style="display:block; transform:none;">' + esc(l1) + '</span></span>'
    if l2:
        lines += '<span style="display:block; overflow:hidden;"><span data-hl="0.55" style="display:block; transform:none;">' + esc(l2) + '</span></span>'
    cover, calt = p['cover']
    return f'''<section data-cursor-bg="light" id="topo" data-screen-label="01 Cabeçalho" style="position:relative; z-index:2; padding:var(--sp-hdr) {PAD} 0 {PAD}; background:var(--bg); color:var(--ink);">
  <div style="display:flex; justify-content:space-between; align-items:baseline; gap:24px; flex-wrap:wrap; font-size:18px; color:var(--mu);">
    <span data-hl-fade="0.1" data-hl-from="translateY(14px)" style="opacity:1; transform:none;">{DASH} Projeto</span>
    <a href="/projetos" data-hl-fade="0.2" data-hl-from="translateY(14px)" style="opacity:1; transform:none; color:var(--mu); text-decoration:none; border-bottom:1px solid #D82E87; padding-bottom:3px;">Todos os projetos</a>
  </div>
  <h1 data-fw="200@458:100" style="margin:clamp(16px,2.4vw,32px) 0 0; font-weight:100; font-size:{p.get('h1size','clamp(36px,8.64vw,160px)')}; line-height:.84; letter-spacing:-0.05em;"><span style="display:block; overflow:hidden; padding:.24em 0 .16em; margin:-.24em 0 -.16em;"><span data-hl="0.2" style="display:block; transform:none;">{esc(p['name'])}</span></span></h1>
  <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr)); gap:20px clamp(32px,5vw,96px); margin-top:clamp(28px,4vw,56px); align-items:start;">
    <p style="margin:0; font-size:18px; line-height:1.5; color:var(--mu);">{lines}</p>
    <p data-type="load" style="margin:0; max-width:34ch; font-size:clamp(20px,1.7vw,26px); line-height:1.45; color:var(--ink);"><span>{esc(p['lead'])}</span></p>
  </div>
  <figure style="position:relative; z-index:2; margin:var(--sp-title) 0 0; aspect-ratio:2/1; overflow:hidden; background:var(--ph);"><div data-hl-fade="0.6" data-hl-from="scale(1.12)" style="position:absolute; inset:0; opacity:1; transform:none;">{img_tag(M, cover, calt, 'display:block; width:100%; height:100%; object-fit:cover; object-position:' + p.get('cover_pos', '50% 50%') + ';', eager=True)}</div></figure>
  <div data-stripes="" data-tone="blue" aria-hidden="true" style="position:absolute; inset:0; z-index:1; overflow:hidden; pointer-events:none;"><span data-stripe="" data-veil="" style="position:absolute; left:0; right:0; bottom:0; height:200%; background:linear-gradient(to top, var(--sf) 50%, transparent 100%); transform:translate3d(0,100%,0); will-change:transform;"></span></div>
</section>'''


def _ink(text, keys):
    on = esc(text)
    off = esc(text)
    for k in keys:
        on = on.replace(esc(k), '<span data-k="">' + esc(k) + '</span>', 1)
        off = off.replace(esc(k), '<span style="font-weight:300;">' + esc(k) + '</span>', 1)
    return on, off


def proj_sobre(p, services_links):
    dl = ''
    for i, (dt, dd) in enumerate(p['facts']):
        d = '' if i == 0 else ' data-draw-d="%.2f"' % (i * .12)
        dl += f'\n    <div><span data-draw="x"{d} style="display:block; height:1px; background:var(--ink);"></span><dt style="margin:18px 0 12px; font-size:18px; color:var(--mu);">{esc(dt)}</dt><dd style="margin:0; font-size:clamp(26px,2.4vw,36px); line-height:1.25; letter-spacing:-0.03em; font-weight:200;">{esc(dd)}</dd></div>'
    on, off = _ink(p['ink'], p.get('keys', []))
    rest = ''
    if p.get('more'):
        rest = f'<p data-rise="0.1" style="margin:0; max-width:44ch; font-size:18px; line-height:1.5; color:var(--tx); text-wrap:pretty;">{esc(p["more"])}</p>'
    links = ''
    if services_links:
        items = ''.join('<li style="margin:0;">' + link_u(h, l + ' →') + '</li>' for h, l in services_links)
        links = f'''
  <div data-rise="0.1" style="margin-top:var(--sp-block); display:flex; flex-wrap:wrap; align-items:baseline; gap:18px 40px;"><p style="margin:0; font-size:18px; color:var(--mu);">{DASH} Serviços neste projeto</p><ul style="list-style:none; margin:0; padding:0; display:flex; flex-wrap:wrap; gap:14px 32px;">{items}</ul></div>'''
    return f'''<section data-cursor-bg="light" id="sobre" data-tone="blue" data-screen-label="02 Sobre o projeto" style="padding:var(--sp-block) {PAD} var(--sp-block) {PAD}; background:var(--sf); color:var(--ink);">
  <dl style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,250px),1fr)); gap:clamp(32px,4vw,64px); margin:0;">{dl}
  </dl>
  <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr)); gap:28px clamp(32px,5vw,96px); margin-top:var(--sp-block); align-items:start;">
    <div style="min-width:0;"><sc-if value="{{{{ inkOn }}}}" hint-placeholder-val="{{{{ true }}}}"><p data-ink="" style="margin:0; font-size:clamp(24px,2.3vw,34px); line-height:1.3; letter-spacing:-0.02em; font-weight:200; text-wrap:pretty;">{on}</p></sc-if><sc-if value="{{{{ inkOff }}}}" hint-placeholder-val="{{{{ false }}}}"><p style="margin:0; font-size:clamp(24px,2.3vw,34px); line-height:1.3; letter-spacing:-0.02em; font-weight:200; text-wrap:pretty;">{off}</p></sc-if></div>
    {rest}
  </div>{links}
</section>'''


def proj_identidade(M, b, sec_id='identidade', label='03 Identidade'):
    tabs = b['tabs']
    n = len(tabs)
    panes = ''
    btns = ''
    caps_l = ''
    caps_r = ''
    for i, t in enumerate(tabs):
        url, title, sub, desc = t['img'], t['title'], t.get('sub', ''), t.get('desc', '')
        l, r = i * 100 / n, 100 - (i + 1) * 100 / n
        off = 'clip-path:inset(0 %g%% 0 %g%%);z-index:1' % (r, l)
        init = '' if i == 0 else ' clip-path:inset(0 %g%% 0 %g%%);' % (r, l)
        bgs, inner = fit_box(M, url, t.get('alt', title), t.get('pos', '50% 50%'), t.get('fit'))
        panes += f'\n    <div data-x="{i}" data-on="clip-path:inset(0 0 0 0);z-index:2" data-off="{off}" style="position:absolute; inset:0; overflow:hidden;{init} {bgs} transition:clip-path 1s cubic-bezier(.76,0,.24,1);">{inner}</div>'
        bl = '' if i == 0 else ' border-left:1px solid rgba(250,250,248,.28);'
        pressed = 'true' if i == 0 else 'false'
        btns += f'\n      <button type="button" data-t="{i}" aria-pressed="{pressed}" style="display:flex; flex-direction:column; justify-content:flex-end; gap:8px; padding:clamp(12px,1.6vw,24px); border:0;{bl} background:transparent; color:#FAFAF8; text-align:left; cursor:pointer; font-family:inherit;"><span data-x="{i}" data-on="opacity:1;transform:none" data-off="opacity:.6;transform:translateY(6px)" style="font-size:16px; transition:opacity .4s ease, transform .6s cubic-bezier(.2,.7,.2,1);">{i + 1:02d}</span><span data-fw="300@1075:200" data-x="{i}" data-on="opacity:1;transform:none" data-off="opacity:.6;transform:translateY(6px)" style="font-size:clamp(20px,2vw,30px); font-weight:200; letter-spacing:-0.02em; transition:opacity .4s ease, transform .6s cubic-bezier(.2,.7,.2,1);">{esc(title)}</span></button>'
        hid = '' if i == 0 else ' opacity:0; transform:translateY(12px);'
        caps_l += f'<div data-x="{i}" data-on="opacity:1;transform:none" data-off="opacity:0;transform:translateY(12px)" style="grid-area:1/1;{hid} transition:opacity .5s ease, transform .8s cubic-bezier(.2,.7,.2,1);"><p style="margin:0; font-size:clamp(24px,2.4vw,36px); line-height:1.05; letter-spacing:-0.035em; font-weight:200;">{esc(title)}</p>' + (f'<p style="margin:8px 0 0; font-size:18px; color:var(--mu);">{esc(sub)}</p>' if sub else '') + '</div>'
        if desc:
            caps_r += f'<p data-x="{i}" data-on="opacity:1;transform:none" data-off="opacity:0;transform:translateY(12px)" style="grid-area:1/1; margin:0; max-width:46ch; font-size:18px; line-height:1.5; color:var(--tx); text-wrap:pretty;{hid} transition:opacity .5s ease .1s, transform .8s cubic-bezier(.2,.7,.2,1) .1s;">{esc(desc)}</p>'
    intro = f'<p data-rise="" style="margin:0; max-width:32ch; font-size:18px; line-height:1.5; color:var(--tx);">{esc(b["intro"])}</p>' if b.get('intro') else ''
    right = f'<div style="display:grid;">{caps_r}</div>' if caps_r else ''
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-tone="{{{{ identTone }}}}" data-hm-fit="" data-screen-label="{label}" style="padding:var(--sp-block) {PAD} var(--sp-block) {PAD}; background:var(--sf); color:var(--ink); transition:background-color 0.2s ease, color 0.2s ease;">
  <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:flex-end; gap:24px 64px; margin-bottom:var(--sp-title);">
    <h2 data-words="" style="margin:0; font-size:clamp(40px,5.12vw,80px); line-height:1.04; letter-spacing:-0.05em; font-weight:100;">{esc(b["title"])}</h2>
    {intro}
  </div>
  <div data-step="0" data-hover="" data-auto="4800">
  <div style="position:relative; height:clamp(300px,min(72vh,56vw),820px); overflow:hidden; background:var(--ph);">{panes}
    <div aria-hidden="true" style="position:absolute; inset:0; z-index:3; pointer-events:none; background:linear-gradient(180deg, rgba(20,19,25,0) 58%, rgba(20,19,25,.62) 100%);"></div>
    <div style="position:absolute; inset:0; z-index:4; display:grid; grid-template-columns:repeat({n},minmax(0,1fr));">{btns}
    </div>
  </div>
  <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr)); gap:12px clamp(24px,4vw,64px); margin-top:clamp(20px,3vw,36px); align-items:start;"><div style="display:grid;">{caps_l}</div>{right}</div>
  </div>
</section>'''


def proj_lp(M, b, sec_id='aplicacoes', label='04 Aplicações', tone='soft'):
    """Galeria horizontal fixada (data-lp), como «Rótulos e packaging» de Camolas."""
    arts = ''
    for i, it in enumerate(b['items']):
        url, title = it['img'], it['title']
        w, h = M.wh(url) or (3, 2)
        # altura comum a todos os cartões; a largura segue a proporção da imagem (limitada ao ecrã)
        arts += f'<article data-lpp="" data-cursor-bg="solid" style="flex:none; width:calc(clamp(240px,30.67vw,480px) * {w / h:.4f});"><div data-lpi="" style="aspect-ratio:{w}/{h}; overflow:hidden; background:var(--ph); clip-path:inset(0 0 27.8% 0);">{img_tag(M, url, it.get("alt", title), "display:block; width:100%; height:100%; object-fit:cover; transform:scale(1.04);")}</div><div style="display:flex; justify-content:space-between; align-items:baseline; gap:16px; margin-top:16px;"><h3 data-lpt="" style="margin:0; font-size:clamp(24px,2.4vw,36px); line-height:1.05; letter-spacing:-0.035em; font-weight:200; opacity:.15;">{esc(title)}</h3><span data-lpd="" style="font-size:16px; color:inherit; opacity:0; transform:translateY(10px); transition:opacity .5s ease, transform .6s cubic-bezier(.2,.7,.2,1);">{i + 1:02d}</span></div></article>'
    link = ''
    if b.get('link'):
        link = f'<a href="{att(b["link"][0])}" style="display:inline-block; margin-top:24px; font-size:18px; color:var(--ink); text-decoration:none; border-bottom:1px solid #D82E87; padding-bottom:4px;">{esc(b["link"][1])}</a>'
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-lp="" data-tone="{tone}" data-screen-label="{label}" style="position:relative; background:var(--sf); color:var(--ink);">
  <div data-lp-st="" style="position:sticky; top:0; height:100vh; overflow:hidden; display:flex; align-items:center;">
    <div data-lp-track="" data-lb="" style="display:flex; align-items:center; gap:clamp(20px,3vw,48px); width:max-content; padding:60px {PAD} 0;">
      <div style="flex:none; width:clamp(260px,30vw,440px);">
        <p style="margin:0 0 18px; font-size:18px; color:var(--mu);">{DASH} {esc(b["eyebrow"])}</p>
        <h2 style="margin:0; font-size:clamp(40px,4.32vw,67px); line-height:1.04; letter-spacing:-0.05em; font-weight:100;">{esc(b["title"])}</h2>
        {link}
      </div>
      {arts}
    </div>
  </div>
</section>'''


def proj_filme(b, sec_id='filme', label='06 Filme'):
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-tone="soft" data-grow="center" data-screen-label="{label}" style="position:relative; height:240vh; background:var(--sf); color:var(--ink); transition:background-color 0.2s ease, color 0.2s ease;">
  <div style="position:sticky; top:0; height:100vh; overflow:hidden;">
    <div data-grow-fade="" style="position:absolute; left:0; right:0; top:0; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:flex-start; gap:12px 48px; padding:calc(84px + clamp(16px,4vh,48px)) {PAD} 0;">
      <h2 style="margin:0; font-size:clamp(40px,5.12vw,80px); line-height:1.04; letter-spacing:-0.05em; font-weight:100;">{esc(b["title"])}</h2>
      <p style="margin:0; max-width:30ch; font-size:18px; line-height:1.5; color:var(--tx);">{esc(b["text"])}</p>
    </div>
    <div aria-hidden="true" style="position:absolute; inset:0; display:grid; place-items:center; overflow:hidden; pointer-events:none;"><span data-fw="100" style="font-size:clamp(96px,16vw,300px); font-weight:100; letter-spacing:-0.06em; line-height:.85; white-space:nowrap; color:var(--ln);">{esc(b["word"])}</span></div>
    <div data-grow-media="" data-cursor-bg="solid" style="position:absolute; inset:0; clip-path:inset(30vh 33vw 30vh 33vw); background:{b.get("bg", "#000")};"><video data-video="" src="{att(b["src"])}" poster="{att(b["poster"])}" muted="" loop="" playsinline="" preload="none" aria-label="{att(b["aria"])}" style="display:block; width:100%; height:100%; object-fit:{b.get("fit", "cover")}; transform:scale({b.get("scale", "1.18")});"></video></div>
    <div data-grow-ui="" style="position:absolute; left:{PAD}; right:{PAD}; bottom:clamp(20px,3vw,40px); display:flex; justify-content:space-between; gap:16px; font-size:16px; color:#FAFAF8; opacity:0; transition:opacity .6s ease;"><span>{esc(b["label"])}</span><span>{esc(b.get("kind", "Vídeo"))}</span></div>
  </div>
</section>'''


def _marquee_item(M, it, hidden=False):
    h = 'clamp(200px,24vw,360px)'
    if it.get('video'):
        ratio = M.ratio(it['poster'])
        aria = 'aria-hidden="true"' if hidden else 'aria-label="' + att(it['alt']) + '"'
        return f'<video data-video="" {aria} src="{att(it["video"])}" poster="{att(it["poster"])}" muted="" loop="" playsinline="" preload="none" style="display:block; flex:none; height:{h}; width:auto; aspect-ratio:{ratio}; object-fit:cover; background:var(--ph);"></video>'
    ratio = M.ratio(it['img'])
    alt = '' if hidden else it['alt']
    extra = ' aria-hidden="true"' if hidden else ''
    return img_tag(M, it['img'], alt, f'display:block; flex:none; height:{h}; width:auto; aspect-ratio:{ratio}; object-fit:cover; background:var(--ph);', extra=extra)


def proj_marquee(M, b, sec_id=None, label='07 Fotografia', drag_attr='data-drag'):
    items = b['items']
    # largura estimada de um conjunto (altura máx. 360 px); repetir até ~2800 px para o ciclo nunca mostrar o fim
    est = sum(360 * M.ratio_f(it['poster'] if it.get('video') else it['img']) + 18 for it in items) or 1
    reps = max(1, -(-2800 // int(est)))
    track = '\n      '.join([_marquee_item(M, it) for it in items] + [_marquee_item(M, it, hidden=True) for it in items * (reps - 1)])
    dup = '\n      '.join(_marquee_item(M, it, hidden=True) for it in items * reps)
    sid = f' id="{sec_id}"' if sec_id else ''
    link = ''
    if b.get('link'):
        link = f'\n  <p style="margin:var(--sp-title) 0 0; padding:0 {PAD};">{link_u(b["link"][0], b["link"][1])}</p>'
    return f'''<section data-cursor-bg="light"{sid} data-screen-label="{label}" style="padding:var(--sp-block) 0 var(--sp-block) 0; background:var(--bg); color:var(--ink); overflow:hidden;">
  <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:flex-end; gap:24px 64px; padding:0 {PAD}; margin-bottom:var(--sp-title);">
    <h2 data-words="" style="margin:0; font-size:clamp(40px,5.12vw,80px); line-height:1.04; letter-spacing:-0.05em; font-weight:100;">{esc(b["title"])}</h2>
    <p data-rise="" style="margin:0; max-width:30ch; font-size:18px; line-height:1.5; color:var(--tx);">{esc(b["intro"])}</p>
  </div>
  <div data-cursor="Arraste" data-lb="" style="overflow:hidden;">
    <div data-marquee="-1" data-speed="0.45" {drag_attr}="" style="display:flex; gap:clamp(10px,1.2vw,18px); width:max-content; padding-right:clamp(10px,1.2vw,18px);">
      {track}
      {dup}
    </div>
  </div>{link}
</section>'''


def _swap_media(M, it, inline=False):
    """Conteúdo da caixa 4:3 do bloco «Anúncios»: imagem inteira (ver fit_box) ou vídeo."""
    if it.get('video'):
        bg = 'background:' + ((M.edge(it['poster']) or ('#000', 0))[0]) + ';'
        v = f'<video data-video="" src="{att(it["video"])}" poster="{att(it["poster"])}" muted="" loop="" playsinline="" preload="none" aria-label="{att(it.get("alt", it["title"]))}" style="position:relative; display:block; width:100%; height:100%; object-fit:contain;"></video>'
        return bg, v
    return fit_box(M, it['img'], it.get('alt', it['title']), force=it.get('fit'), extra=' data-zoom=""' if inline else '')


def proj_anuncios(M, b, sec_id='anuncios', label='08 Anúncios', tone='soft'):
    """Lista com imagem fixa que muda ao percorrer (data-swap), como «Anúncios e redes sociais» de Camolas."""
    items = b['items']
    n = len(items)
    arts, imgs = '', ''
    for i, it in enumerate(items):
        last = i == n - 1
        bgi, inner_i = _swap_media(M, it, inline=True)
        bgm, inner_m = _swap_media(M, it)
        mh = '31vh' if last else '62vh'
        al = 'flex-end' if last else 'center'
        bb = ' border-bottom:1px solid var(--ln);' if last else ''
        tags = f'<p style="margin:10px 0 0; font-size:18px; color:var(--mu);">{esc(it["tags"])}</p>' if it.get('tags') else ''
        arts += (f'\n      <article data-swap-txt="" data-on="opacity:1" data-off="opacity:.25" style="min-height:{mh}; display:flex; align-items:{al}; gap:20px; border-top:1px solid var(--ln);{bb} transition:opacity .5s ease;">'
                 f'<div data-m="swap-inline" data-cursor-bg="solid" data-reveal="random" style="display:none; position:relative; aspect-ratio:4/3; overflow:hidden; {bgi}">{inner_i}</div>'
                 f'<div style="display:flex; flex-direction:column; gap:14px;"><span style="font-size:16px; color:inherit;">{i + 1:02d}</span><div>'
                 f'<h3 data-fw="200@1235:100" style="margin:0; font-size:clamp(32px,3.2vw,48px); line-height:1.1; letter-spacing:-0.045em; font-weight:100;">{esc(it["title"])}</h3>'
                 f'<p style="margin:14px 0 0; max-width:34ch; font-size:18px; line-height:1.5; color:var(--tx); text-wrap:pretty;">{esc(it["text"])}</p>{tags}</div></div></article>')
        imgs += f'\n        <div data-swap-img="" data-cursor-bg="solid" style="position:absolute; inset:0; overflow:hidden; {bgm}">{inner_m}</div>'
    intro = f'\n  <p data-rise="" style="margin:calc(var(--sp-title) * -0.5) 0 var(--sp-title); max-width:46ch; font-size:18px; line-height:1.5; color:var(--tx);">{esc(b["intro"])}</p>' if b.get('intro') else ''
    return f'''<section data-cursor-bg="light" id="{sec_id}" data-tone="{tone}" data-swap="" data-hm-fit="" data-screen-label="{label}" style="padding:var(--sp-block) {PAD} var(--sp-block) {PAD}; background:var(--sf); color:var(--ink); transition:background-color 0.2s ease, color 0.2s ease;">
  <h2 data-words="" style="margin:0 0 var(--sp-title) 0; max-width:14ch; font-size:clamp(40px,5.12vw,80px); line-height:1.04; letter-spacing:-0.05em; font-weight:100;">{esc(b["title"])}</h2>{intro}
  <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr)); gap:clamp(32px,5vw,96px); align-items:start;">
    <div>{arts}
    </div>
    <div data-m="swap-media" style="position:sticky; top:clamp(96px,16vh,160px);">
      <div style="position:relative; aspect-ratio:4/3; overflow:hidden; background:var(--ph);">{imgs}
      </div>
      <p style="display:flex; justify-content:space-between; margin:16px 0 0; font-size:18px; color:var(--mu);"><span style="color:color-mix(in srgb, var(--ink) 60%, transparent); font-weight:400;"><span data-swap-n="">01</span> / {n:02d}</span><span>{esc(b.get("caption", b["title"]))}</span></p>
    </div>
  </div>
</section>'''


def proj_testemunho(M, t, tone='mist', label='08b Testemunho'):
    img = img_tag(M, t['img'], t['img_alt'], 'display:block; width:100%; height:100%; object-fit:cover;')
    return f'''<section data-cursor-bg="light" id="testemunho" data-tone="{tone}" data-screen-label="{label}" style="background:var(--sf); color:var(--ink); padding:var(--sp-block) {PAD} var(--sp-block) {PAD};">
  <div style="display:flex; flex-wrap:wrap; gap:clamp(48px,6vw,112px); align-items:center;">
    <figure style="flex:999 1 520px; min-width:0; margin:0;">
      <p style="margin:0 0 24px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:var(--mu);">{DASH_A} O que diz o cliente</p>
      <p data-rise="" style="margin:0; max-width:13ch; font-size:clamp(40px,4.48vw,80px); font-weight:100; letter-spacing:-0.05em; line-height:1.04; text-wrap:balance;">{esc(t["headline"])}</p>
      <blockquote data-rise="0.1" style="margin:clamp(28px,4vh,44px) 0 0; max-width:56ch; font-size:18px; line-height:1.5; color:var(--tx); text-wrap:pretty;"><span aria-hidden="true" style="color:#D82E87;">«</span>{esc(t["quote"])}<span aria-hidden="true" style="color:#D82E87;">»</span></blockquote>
      <figcaption data-rise="0.2" style="margin-top:clamp(28px,4vh,44px); display:flex; flex-direction:column; gap:6px;"><span style="display:flex; align-items:baseline; gap:12px; flex-wrap:wrap;"><span aria-hidden="true" style="color:#D82E87;">—</span><span style="font-size:18px; font-weight:400;">{esc(t["name"])}</span><span style="font-size:18px; color:var(--mu);">{esc(t["company"])}</span></span><span style="padding-left:26px; font-size:18px; line-height:1.5; color:color-mix(in srgb, var(--ink) 70%, transparent);">{esc(t["role"])}</span></figcaption>
    </figure>
    <figure data-rise="0.1" style="flex:1 1 320px; max-width:480px; margin:0;">
      <div style="aspect-ratio:4 / 5; overflow:hidden; background:#5f6859;">{img}</div>
    </figure>
  </div>
</section>'''


def proj_mais(M, others):
    """«Mais projetos» (5 painéis com data-step). others: [(nome, href, img)]."""
    n = len(others)
    cards = ''
    for i, (name, href, img) in enumerate(others):
        on = i == 0
        d = M.wh(img)
        wh = (' width="%d" height="%d"' % d) if d else ''
        cards += f'''
    <a href="{att(href)}" data-t="{i}" data-cursor="Ver projeto" style="position:relative; display:block; overflow:hidden; background:#2a2a2c; color:#FAFAF8; text-decoration:none;" style-hover="color:#FAFAF8"><img src="{att(img)}" alt=""{wh} loading="lazy" decoding="async" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; filter:grayscale(1) brightness(.92);"><div data-x="{i}" data-on="opacity:1;transform:scale(1.04)" data-off="opacity:0;transform:scale(1)" style="position:absolute; inset:0;{' transform:scale(1.04);' if on else ' opacity:0;'} transition:opacity .8s ease, transform 1.6s cubic-bezier(.2,.7,.2,1);"><img src="{att(img)}" alt=""{wh} loading="lazy" decoding="async" style="display:block; width:100%; height:100%; object-fit:cover;"></div><span aria-hidden="true" style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(20,19,25,.28) 0%, rgba(20,19,25,0) 26%, rgba(20,19,25,0) 40%, rgba(20,19,25,.84) 100%);"></span><span data-x="{i}" data-on="transform:scaleX(1)" data-off="transform:scaleX(0)" aria-hidden="true" style="position:absolute; left:0; right:0; top:0; height:2px; background:#D82E87; transform-origin:0 50%; transform:scaleX({1 if on else 0}); transition:transform .9s cubic-bezier(.76,0,.24,1);"></span><span style="position:absolute; left:clamp(14px,1.6vw,24px); top:clamp(14px,1.6vw,24px); font-size:16px;">{i + 1:02d}</span><span data-x="{i}" data-on="transform:translateY(-40px)" data-off="transform:none" style="position:absolute; left:clamp(14px,1.6vw,24px); right:clamp(14px,1.6vw,24px); bottom:clamp(18px,2.2vw,32px); font-size:clamp(22px,2vw,30px); line-height:1.1; letter-spacing:-0.03em; font-weight:200;{' transform:translateY(-40px);' if on else ''} transition:transform .9s cubic-bezier(.76,0,.24,1);">{esc(name)}</span><span data-x="{i}" data-on="opacity:1;transform:none" data-off="opacity:0;transform:translateY(12px)" style="position:absolute; left:clamp(14px,1.6vw,24px); bottom:clamp(18px,2.2vw,32px); font-size:18px; border-bottom:1px solid #D82E87; padding-bottom:3px;{'' if on else ' opacity:0; transform:translateY(12px);'} transition:opacity .6s ease .2s, transform .8s cubic-bezier(.2,.7,.2,1) .2s;">Ver projeto →</span></a>'''
    return f'''<section data-cursor-bg="light" data-screen-label="09 Projetos" style="padding:var(--sp-block) {PAD} var(--sp-block) {PAD}; background:var(--bg); color:var(--ink);">
  <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:baseline; gap:12px 32px; margin-bottom:clamp(20px,3vw,36px);"><p style="margin:0; font-size:18px; color:var(--mu);">{DASH} Mais projetos</p><a href="/projetos" style="font-size:18px; color:var(--ink); text-decoration:none; border-bottom:1px solid #D82E87; padding-bottom:3px;">Ver todos os projetos →</a></div>
  <div data-step="0" data-hover="" data-auto="3400" data-n="{n}" style="display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); grid-auto-rows:clamp(240px,48vh,520px); gap:1px; background:var(--bg);">{cards}
  </div>
</section>'''


def contacto(title, text, cta_label, cta_href='/contacto', tone_attr='data-tone="blue"', bg='var(--sf)', ink='var(--ink)', mu='var(--mu)', tx='var(--tx)', label='10 Contacto'):
    return f'''<section data-cursor-bg="light" id="contacto" {tone_attr} data-screen-label="{label}" style="background:{bg}; color:{ink}; padding:var(--sp-block) {PAD} var(--sp-block) {PAD};">
  <p style="margin:0 0 32px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{mu};">{DASH_A} Contacto</p>
  <h2 data-colorize="" style="margin:0; font-weight:100; font-size:clamp(40px,5.28vw,102px); letter-spacing:-0.05em; line-height:.95; max-width:15ch; text-wrap:balance;">{esc(title)}</h2>
  <p style="margin:clamp(24px,3vw,40px) 0 0; max-width:52ch; font-size:18px; font-weight:300; line-height:1.5; color:{tx}; text-wrap:pretty;">{esc(text)}</p>
  <div style="margin-top:var(--sp-title); display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr)); gap:32px; align-items:end;">
    <div><a href="{att(cta_href)}" data-cursor="Falar" style="display:inline-flex; align-items:center; gap:14px; height:64px; padding:0 32px; border-radius:0; background:#1C1B23; color:#ffffff; text-decoration:none; font-size:18px; font-weight:300; box-shadow:0 14px 30px -16px rgba(28,27,35,.55);" style-hover="background:#4A4743; color:#ffffff;">{esc(cta_label)} <span aria-hidden="true">→</span></a></div>
    <div>
      <p style="margin:0 0 6px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{mu};">Telefone</p>
      <a href="tel:+351211806292" style="font-size:clamp(26px,2.2vw,36px); letter-spacing:-0.02em; color:{ink}; text-decoration:none; font-weight:200;">(+351) 211 806 292</a>
      <p style="margin:4px 0 0; font-size:18px; color:{mu};">Chamada para rede fixa nacional</p>
    </div>
    <div>
      <p style="margin:0 0 6px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{mu};">Sede</p>
      <a href="https://www.google.com/maps?cid=12848211740159704585" target="_blank" rel="noopener" style="display:block; margin:0; font-size:18px; line-height:1.5; color:{ink}; text-decoration:none;" style-hover="color:#D82E87;">R. Dr. Miguel Bombarda nº 88<br>2860-461 Moita, Portugal</a>
    </div>
  </div>
</section>'''
