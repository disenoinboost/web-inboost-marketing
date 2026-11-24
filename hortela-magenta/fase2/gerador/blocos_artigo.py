"""Cabeçalho e corpo de artigo (modelo: Artigo) para as páginas legais e o mapa do site."""
from base import esc, att
from blocos import PAD

P_ST = 'margin:0 0 26px; font-size:18px; font-weight:300; line-height:1.5; color:#3A3833;'
A_ST = 'color:#1C1B23; text-decoration:none; border-bottom:1px solid #D82E87;'


def _inline(h):
    # o conteúdo já vem em HTML controlado (links e <strong>): só se dá estilo às ligações
    return h.replace('<a href=', '<a style="' + A_ST + '" href=').replace('<strong>', '<strong style="font-weight:400; color:#1C1B23;">')


def header(d):
    return f'''<header data-hero="" data-screen-label="01 Cabeçalho" style="background:#ffffff; padding:var(--sp-hdr) {PAD} var(--sp-title) {PAD}; text-align:center; display:flex; flex-direction:column; align-items:center;">
  <nav aria-label="Breadcrumb" data-hl-fade="" style="margin-bottom:clamp(28px,5vh,56px);"><ol style="list-style:none; margin:0; padding:0; display:flex; flex-wrap:wrap; justify-content:center; gap:10px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:#6E6A63;"><li><a href="/" style="color:#6E6A63; text-decoration:none;">Início</a></li><li aria-hidden="true" style="color:#D82E87;">—</li><li aria-current="page" style="color:#1C1B23;">{esc(d["h1"])}</li></ol></nav>
  <h1 style="margin:0; max-width:17ch; font-size:clamp(40px,4.64vw,83px); font-weight:100; letter-spacing:-0.05em; line-height:1.04; color:#1C1B23; text-wrap:balance;"><span data-hl="" style="display:block;">{esc(d["h1"])}</span></h1>
  <p data-hl-fade="" style="margin:clamp(24px,4vh,40px) 0 0; max-width:44ch; font-size:clamp(24px,1.9vw,32px); font-weight:200; line-height:1.35; letter-spacing:-0.01em; color:#4A4743; text-wrap:pretty;">{esc(d["lead"])}</p>
</header>'''


def corpo(d, toc_label='Nesta página'):
    toc = ''.join(f'''
          <li><a data-toc="" href="#{sid}" style="position:relative; display:block; font-size:18px; font-weight:300; line-height:1.4; color:rgba(28,27,35,.55); text-decoration:none; transition:color 0.2s ease;"><span aria-hidden="true" style="position:absolute; left:-26px; top:7px; width:7px; height:7px; border-radius:50%; background:#ffffff; border:1px solid rgba(28,27,35,.35); transition:background 0.2s, border-color 0.2s, transform .3s;"></span>{esc(title)}</a></li>''' for sid, title, _ in d['sections'])
    body = ''
    for i, (sid, title, items) in enumerate(d['sections']):
        top = '0' if i == 0 else 'clamp(48px,7vh,72px)'
        body += f'\n      <h2 data-fw="200" id="{sid}" style="margin:{top} 0 20px; scroll-margin-top:120px; font-size:clamp(30px,2.08vw,35px); font-weight:200; letter-spacing:-0.035em; line-height:1.1;">{esc(title)}</h2>'
        for kind, v in items:
            if kind == 'p':
                body += f'\n      <p style="{P_ST}">{_inline(v)}</p>'
            elif kind == 'ul':
                li = ''.join(f'<li style="position:relative; padding-left:32px; margin-bottom:14px;"><span aria-hidden="true" style="position:absolute; left:0; top:.72em; width:16px; height:1px; background:#D82E87;"></span>{_inline(x)}</li>' for x in v)
                body += f'\n      <ul style="list-style:none; margin:0 0 26px; padding:0; font-size:18px; font-weight:300; line-height:1.5; color:#3A3833;">{li}</ul>'
            elif kind == 'links':
                li = ''.join(f'<li style="border-top:1px solid rgba(28,27,35,.12);"><a href="{att(h)}"' + (' target="_blank" rel="noopener"' if h.startswith('http') else '') + f' style="display:flex; justify-content:space-between; gap:16px; padding:14px 0; color:#1C1B23; text-decoration:none; font-size:18px; font-weight:300;" style-hover="color:#D82E87;">{esc(l)}<span aria-hidden="true" style="color:#D82E87;">→</span></a></li>' for h, l in v)
                body += f'\n      <ul style="list-style:none; margin:0 0 26px; padding:0; border-bottom:1px solid rgba(28,27,35,.12);">{li}</ul>'
    return f'''<section data-cursor-bg="light" id="c1" data-screen-label="02 Corpo" style="background:#ffffff; padding:var(--sp-block) {PAD} var(--sp-block) {PAD};">
  <div style="display:flex; flex-wrap:wrap; gap:48px clamp(40px,5vw,96px); align-items:flex-start;">
    <aside data-faq-side="" aria-label="{att(toc_label)}" style="flex:0 1 260px; position:sticky; top:120px;">
      <div style="margin-bottom:26px; padding-bottom:18px; border-bottom:1px solid rgba(28,27,35,.12);">
        <p style="margin:0; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:#6E6A63;">{esc(toc_label)}</p>
      </div>
      <nav data-toc-nav="" aria-label="Índice" style="position:relative; padding-left:26px; margin-bottom:40px;">
        <span aria-hidden="true" style="position:absolute; left:3px; top:10px; bottom:10px; width:1px; background:rgba(28,27,35,.14);"></span>
        <span data-read-fill="" aria-hidden="true" style="position:absolute; left:3px; top:10px; width:1px; height:0; background:#1C1B23;"></span>
        <ol style="list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:20px;">{toc}
        </ol>
      </nav>
    </aside>
    <div style="flex:1 1 560px; min-width:0;"><div data-article-body="" style="max-width:clamp(820px, 52vw, 1040px); margin:0 auto; min-width:0;">{body}
    </div></div>
  </div>
</section>'''
