"""Hortelã Magenta · fase 2 · gera os modelos (template) das páginas novas e aplica as alterações comuns às existentes.

Uso: python3 -I gerar.py <dir-modelos-originais> <media-info.json> <oldproj.json> <dir-saida>
Escreve <dir-saida>/<pagina>.html (template, com os uuid dos recursos do pacote) e <dir-saida>/rotas.json.
"""
from estilos import media_local
import json
import re
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import Media, load_tpl, set_seo, set_main, set_page_current, set_pidx, IMG, SITE  # noqa: E402
import blocos as B  # noqa: E402
from comum import normalizar, fix_existing_seo  # noqa: E402
from dados_projetos import projetos, ORDER, NAMES, CARD, SVC  # noqa: E402
import blocos_servico as BS  # noqa: E402
from dados_servicos import servicos  # noqa: E402
from dados_landings import landings  # noqa: E402
import blocos_artigo as BA  # noqa: E402
import extras  # noqa: E402
from dados_aux import PRIVACIDADE, COOKIES, mapa, obrigado, erro404  # noqa: E402
from urllib.parse import quote  # noqa: E402

SRC, INFO, PROJ, OUT = sys.argv[1:5]
os.makedirs(OUT, exist_ok=True)
M = Media(INFO, PROJ)
EXISTING = ['home', 'servicos', 'branding', 'design-web', 'projetos', 'camolas', 'sobre', 'blog', 'artigo', 'contacto']
ROUTES = {}   # caminho canónico -> ficheiro do pacote (sem .html)
LOCAL_OG = '/wp-content/uploads/hm-media/'


def LI(slug, name):
    """Imagem de uma landing (copiada para hm-media/hortelamagenta.pt/<landing>/): devolve o caminho local e regista as medidas."""
    stem = os.path.splitext(name)[0]
    for u, i in M.info.items():
        rel = i['rel']
        if rel.startswith('hortelamagenta.pt/' + slug + '/') and os.path.splitext(os.path.basename(rel))[0] == stem:
            loc = '/wp-content/uploads/hm-media/' + rel
            M.info.setdefault(loc, i)
            return loc
    raise KeyError(slug + ' ' + name)


def og_local(url):
    if not url:
        return None
    loc = url if url.startswith('/wp-content/') else M.local(url)
    loc = media_local(loc)  # remoto sem medidas em media-info: a cópia de hm-media (antes saía SITE + URL absoluto: domínio duplicado)
    return SITE + loc if loc.startswith('/') else loc


def write(name, t):
    assert '{{ ' in t  # sanity: ainda é um modelo do desenho
    open(os.path.join(OUT, name + '.html'), 'w', encoding='utf-8').write(t)


# ------------------------------------------------------------------------------------------- projetos
def build_projeto(slug, p, base):
    t = base
    path = '/projetos/' + slug
    t = set_seo(t, p['title'], p['desc'], path, [('Início', '/'), ('Projetos', '/projetos'), (p['name'], path)],
                og_img=og_local(p['cover'][0]),
                extra_ld=[{"@context": "https://schema.org", "@type": "CreativeWork", "name": p['name'], "url": SITE + path,
                           "creator": {"@type": "Organization", "name": "Hortelã Magenta", "url": SITE + "/"},
                           "description": p['desc']}])
    parts = [B.proj_header(M, p), B.proj_sobre(p, [SVC[k] for k in p.get('services', [])])]
    pidx = []
    if p.get('ident'):
        parts.append(B.proj_identidade(M, p['ident']))
        pidx.append(('identidade', 'Identidade'))
    if p.get('apps'):
        parts.append(B.proj_lp(M, p['apps']))
        pidx.append(('aplicacoes', p['apps'].get('nav', p['apps']['eyebrow'].split(' ')[0])))
    if p.get('ads'):
        parts.append(B.proj_anuncios(M, p['ads']))
        pidx.append(('anuncios', p['ads'].get('nav', 'Anúncios')))
    if p.get('site'):
        parts.append(B.proj_filme(p['site'], sec_id='site', label='05 Site'))
        pidx.append(('site', 'Site'))
    if p.get('film'):
        parts.append(B.proj_filme(p['film']))
        pidx.append(('filme', 'Vídeo'))
    if p.get('gallery'):
        parts.append(B.proj_marquee(M, p['gallery'], sec_id='galeria-projeto'))
        pidx.append(('galeria-projeto', p['gallery'].get('nav', 'Galeria')))
    if p.get('testimonial'):
        parts.append(B.proj_testemunho(M, p['testimonial']))
    i = ORDER.index(slug)
    others = [ORDER[(i + k) % len(ORDER)] for k in range(1, 6)]
    parts.append(B.proj_mais(M, [(NAMES[o], '/projetos/' + o, CARD[o]) for o in others]))
    parts.append(B.contacto('Falemos da comunicação de que a sua marca precisa.', p['contact'], 'Falar sobre a minha marca'))
    t = set_main(t, alternar_tons('\n\n'.join(parts)))
    t = set_pidx(t, pidx)
    t = t.replace(' data-lp=""', ' data-lpf="p"')  # «Aplicações»: movimento contínuo (capa-fix), sem paragens
    t = normalizar(t)
    return t


# ------------------------------------------------------------------------------------------- serviços
KIND_BG = {'frase': '#e8eced', 'faq': '#f6f7f8'}


def blocks_html(blocks, slug):
    out = []
    # faixa de imagens logo a seguir a outra secção: o mesmo fundo e sem espaço entre as duas (parecem um só bloco)
    for i, (kind, b) in enumerate(blocks):
        if kind in ('imagens', 'galeria') and i and not b.get('title'):
            pk, pb = blocks[i - 1]
            b.setdefault('bg', pb.get('bg') or KIND_BG.get(pk, '#ffffff'))
            b['joined'] = True
    for i, (kind, b) in enumerate(blocks):
        sid = b.get('id', '%s-%d' % (kind, i + 1))
        label = '%02d %s' % (i + 2, b.get('eyebrow', kind).replace('&', 'e'))
        bg = b.get('bg')
        if kind == 'texto':
            out.append(BS.texto(b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'lista':
            out.append(BS.lista(b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'panels':
            out.append(BS.panels(M, b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'frase':
            out.append(BS.frase(b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'citacao':
            out.append(BS.testemunho(M, b, sec_id=sid, label=label, bg=bg or '#ffffff'))
        elif kind == 'filme':
            out.append(B.proj_filme(b, sec_id=sid, label=label, svc=True))
        elif kind == 'chips':
            out.append(BS.chips(b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'marquee':
            out.append(B.proj_marquee(M, b, sec_id=sid, label=label, drag_attr='data-mq-drag', svc=True))
        elif kind == 'imagens':
            out.append(BS.imagens(M, b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'linhas':
            out.append(BS.linhas(b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'ambito':
            out.append(BS.ambito(b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'galeria':
            out.append(BS.galeria(M, b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'premios':
            out.append(BS.premios(M, b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'links':
            out.append(BS.links_rel(b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'mais':
            out.append(B.proj_mais(M, b['items']))
        else:
            raise ValueError(kind)
    # antes de «Mais projetos» (que tem o seu próprio espaço por cima) a secção anterior não leva o espaço inferior inteiro
    kinds = [k for k, _ in blocks]
    for i in range(len(out) - 1):
        if kinds[i + 1] in ('imagens', 'galeria') and blocks[i + 1][1].get('joined'):
            out[i] = out[i].replace(f'padding:var(--sp-block) {B.PAD} var(--sp-block) {B.PAD}', f'padding:var(--sp-block) {B.PAD} clamp(28px,3.5vw,56px) {B.PAD}', 1)
        if kinds[i + 1] == 'mais':
            out[i] = out[i].replace(f'padding:var(--sp-block) {B.PAD} var(--sp-block) {B.PAD}', f'padding:var(--sp-block) {B.PAD} var(--sp-title) {B.PAD}', 1)
    return out



# Fundos (2026-11-26): duas secções seguidas nunca com o mesmo fundo (o espaço de cada uma somava-se num vazio enorme
# e as faixas fundiam-se). A faixa de fotos «junta» (data-hm-joined) acompanha a secção anterior; os painéis abertos
# (data-step-v) usam cinzentos diferentes do fundo da sua secção.
_GREYS = {'#e8eced', '#dde3e7', '#f6f7f8'}
_TONE = {'soft': '#f6f7f8', 'blue': '#e8eced', 'mist': '#dde3e7'}
# franjas: cada uma com um tom diferente (nunca o do fundo da secção) e na ordem de Branding: claro, médio, escuro, …
_STRIPS = {'#ffffff': ['#e8eced', '#dde3e7', '#a6b4c1', '#cbd4db', '#b9c5cf'],
           '#e8eced': ['#f6f7f8', '#dde3e7', '#a6b4c1', '#cbd4db', '#b9c5cf'],
           '#f6f7f8': ['#e8eced', '#dde3e7', '#a6b4c1', '#cbd4db', '#b9c5cf'],
           '#dde3e7': ['#f6f7f8', '#e8eced', '#a6b4c1', '#cbd4db', '#b9c5cf']}
_STRIP_RE = re.compile(r'(<div data-t="(\d+)" data-x="\d+" role="button"[^>]*?background:)(#[0-9a-fA-F]{6})')


def pintar_franjas(body, bg):
    pal = _STRIPS.get(bg)
    return _STRIP_RE.sub(lambda mm: mm.group(1) + pal[int(mm.group(2)) % len(pal)], body) if pal else body


def franjas_existentes(html):
    """Páginas do desenho original (Branding): o mesmo critério nas franjas dos painéis."""
    ms = list(re.finditer(r'<section\b[^>]*>', html))
    out, pos = [], 0
    for k, m in enumerate(ms):
        end = ms[k + 1].start() if k + 1 < len(ms) else len(html)
        body = html[m.end():end]
        if 'data-step-v=""' in body:
            c, _ = _sec_color(m.group(0))
            body = pintar_franjas(body, c)
        out.append(html[pos:m.end()] + body)
        pos = end
    out.append(html[pos:])
    return ''.join(out)


def _sec_color(tag):
    m = re.search(r'background:\s*([^;"]+)', tag)
    if not m:
        return None, None
    v = m.group(1).strip()
    if v.startswith('var(--sf)'):
        tm = re.search(r'data-tone="(\w+)"', tag)
        return (_TONE.get(tm.group(1), 'dark') if tm else '#ffffff'), v
    if v.startswith('var(--bg)'):
        return '#ffffff', v
    if v.lower() in ('#1c1b23', '#141319'):
        return 'dark', v
    return v.lower(), v


def alternar_fundos(html):
    ms = list(re.finditer(r'<section\b[^>]*>', html))
    out, pos, prev = [], 0, None
    for k, m in enumerate(ms):
        end = ms[k + 1].start() if k + 1 < len(ms) else len(html)
        tag, body = m.group(0), html[m.end():end]
        out.append(html[pos:m.start()])
        pos = end
        if 'data-screen-label="01 ' in tag:
            prev = None
            out.append(tag + body)
            continue
        c, raw = _sec_color(tag)
        new = c
        if 'data-hm-joined' in tag and prev and prev != 'dark':
            new = prev
        elif c and c != 'dark' and c == prev:
            new = '#ffffff' if c in _GREYS else '#f6f7f8'
        if new != c and raw:
            tag = tag.replace('background:' + raw, 'background:' + new, 1)
        if new in _STRIPS and 'data-step-v=""' in body:
            body = pintar_franjas(body, new)
        prev = new or prev
        out.append(tag + body)
    out.append(html[pos:])
    return ''.join(out)


def alternar_tons(html):
    """Fichas de projeto: o mesmo critério, trocando o tom (data-tone) de uma secção igual à anterior."""
    ms = list(re.finditer(r'<section\b[^>]*>', html))
    out, pos, prev = [], 0, None
    for m in ms:
        tag = m.group(0)
        out.append(html[pos:m.start()])
        pos = m.end()
        tm = re.search(r'data-tone="(\w+)"', tag)
        c, _ = _sec_color(tag)
        if '{{' in tag:
            c = None
        if tm and tm.group(1) in _TONE and c == prev:
            nt = 'blue' if tm.group(1) == 'soft' else 'soft'
            tag = tag.replace('data-tone="%s"' % tm.group(1), 'data-tone="%s"' % nt, 1)
            c = _TONE[nt]
        elif not tm and c == prev == '#ffffff' and 'background:var(--bg)' in tag:
            # ex.: «Fotografia» e «Projetos», ambas brancas: «Projetos» passa ao cinzento claro
            tag = tag.replace('background:var(--bg)', 'background:var(--sf)', 1).replace('<section ', '<section data-tone="soft" ', 1)
            c = _TONE['soft']
        prev = c
        out.append(tag)
    out.append(html[pos:])
    return ''.join(out)


def build_servico(slug, d, base, crumbs_parent=('Serviços', '/servicos'), schema_type='Service'):
    t = base
    crumbs = [('Início', '/')] + ([crumbs_parent] if crumbs_parent else []) + [(d['name'] if 'crumb' not in d else d['crumb'], d['path'])]
    ld = []
    if schema_type:
        ld.append({"@context": "https://schema.org", "@type": schema_type, "name": d['title'].split(' | ')[0], "url": SITE + d['path'], "description": d['desc'],
                   "provider": {"@type": "Organization", "name": "Hortelã Magenta", "url": SITE + "/"}, "areaServed": "PT"})
    if d.get('faq'):
        ld.append(BS.faq_ld(d['faq']['items']))
    t = set_seo(t, d['title'], d['desc'], d['path'], crumbs, og_img=og_local(d.get('og')), extra_ld=ld, robots=d.get('robots'))
    if d.get('nocanonical'):
        import re as _re
        t = _re.sub(r'<link rel="canonical" href="[^"]*">\n?', '', t, count=1)
        t = _re.sub(r'<meta property="og:url" content="[^"]*">\n?', '', t, count=1)
        t = _re.sub(r'<script type="application/ld\+json">.*?</script>\n?', '', t, count=1, flags=_re.S)
    cta_href = '/contacto'
    if d.get('form_servico'):
        cta_href = '/contacto?servico=' + quote(d['form_servico'])
        h = d['hero']
        if h['cta'][0] == '/contacto':
            h['cta'] = (cta_href, h['cta'][1])
    # A cabeçalho funde-se (data-veil) com a secção seguinte, como em Branding: as duas com o mesmo cinzento (#e8eced).
    # Se a primeira secção já tiver fundo próprio, o véu usa essa cor.
    blocks = d.get('blocks', [])
    if blocks:
        k0, b0 = blocks[0]
        if k0 == 'mais':  # «Mais projetos» tem o fundo do tema (branco)
            d['hero'].setdefault('veil', 'var(--bg)')
        elif b0.get('bg'):
            d['hero'].setdefault('veil', b0['bg'])
        else:
            b0['bg'] = d['hero'].get('veil', '#e8eced')
    parts = [BS.hero(d['hero'])] + blocks_html(blocks, slug)
    if d.get('trabalhos'):
        parts.append(BS.trabalhos(M, d['trabalhos']))
    if d.get('testimonial'):
        parts.append(BS.testemunho(M, d['testimonial']))
    if d.get('faq'):
        parts.append(BS.faq(d['faq'], 'faq-' + slug.replace('servico-', '').replace('lp-', '')))
    c = d['contact']
    parts.append(BS.contacto_s(c[0], c[1], c[2], cta_href))
    t = set_main(t, alternar_fundos('\n\n'.join(parts)))
    t = tone_vars(t)
    t = set_page_current(t, d.get('current', d['name']))
    t = normalizar(t)
    return t


def clear_nav_current(t):
    """Tira a marca de página atual do menu principal (herdada do modelo de base)."""
    import re as _re
    a = t.index('<nav aria-label="Principal"')
    b = t.index('</nav>', a)
    nav = _re.sub(r' aria-current="page"( style="position:relative; color:inherit; text-decoration:none; padding:10px 0;">[^<]*<span data-nu="" aria-hidden="true" style="[^"]*?)transform:scaleX\(1\);([^"]*)" data-keep="1">',
                  r'\1transform:scaleX(0);\2">', t[a:b])
    return t[:a] + nav + t[b:]


def build_legal(name, d, base, robots=None):
    t = clear_nav_current(base)
    t = set_seo(t, d['title'], d['desc'], d['path'], [('Início', '/'), (d['h1'], d['path'])], robots=robots)
    parts = [BA.header(d), BA.corpo(d), BS.contacto_s('Diga-nos, onde quer chegar?', 'Tem alguma questão sobre esta página ou sobre um projeto? Fale connosco.', 'Falar connosco')]
    t = set_main(t, '\n\n'.join(parts), main_attrs='id="top"')
    t = set_page_current(t, '')
    t = normalizar(t)
    return t


def tone_vars(t):
    """Variáveis de cor (--bg, --sf, --ink, data-tone...) do modelo de Camolas, para os blocos de projeto usados noutras bases."""
    if '--sf:' in t[:t.index('</helmet>')]:
        return t
    c = load_tpl(SRC, 'camolas')
    a = c.index('<style>:root{--bg:')
    b = c.index('</style>', a) + 8
    return t.replace('</helmet>', c[a:b] + '\n</helmet>', 1)


def main():
    base_proj = load_tpl(SRC, 'camolas')
    P = projetos(M)
    for slug, p in P.items():
        write('projeto-' + slug, build_projeto(slug, p, base_proj))
        ROUTES['/projetos/' + slug] = 'projeto-' + slug
    base_svc = load_tpl(SRC, 'branding')
    for slug, d in servicos(M).items():
        write(slug, build_servico(slug, d, base_svc))
        ROUTES[d['path']] = slug
    for slug, d in landings(M, LI).items():
        write(slug, build_servico(slug, d, base_svc))
        ROUTES[d['path']] = slug
    base_art = load_tpl(SRC, 'artigo')
    for name, d, rb in [('politica-privacidade', PRIVACIDADE, 'noindex, follow'), ('politica-cookies', COOKIES, 'noindex, follow'), ('mapa-do-site', mapa(), None)]:
        write(name, build_legal(name, d, base_art, rb))
        ROUTES[d['path']] = name
    write('obrigado', build_servico('obrigado', obrigado(M), base_svc, crumbs_parent=None, schema_type=None))
    ROUTES['/obrigado'] = 'obrigado'
    write('404', build_servico('404', erro404(M), base_svc, crumbs_parent=None, schema_type=None))
    # páginas existentes: alterações comuns + conteúdo
    for n in EXISTING:
        t = load_tpl(SRC, n)
        t = fix_existing_seo(n, t)
        t = normalizar(t)
        if hasattr(extras, n.replace('-', '_')):
            t = getattr(extras, n.replace('-', '_'))(t)
        # galerias que se deslocam ao descer: movimento contínuo (data-lpf, em capa-fix) em vez das paragens do data-lp
        t = t.replace(' data-lp=""', ' data-lpf="p"' if n == 'camolas' else ' data-lpf=""')
        if n == 'branding':
            t = franjas_existentes(t)
        write(n, t)
    json.dump(ROUTES, open(os.path.join(OUT, 'rotas.json'), 'w'), indent=1, ensure_ascii=False)
    print('ok', len(ROUTES), 'páginas novas;', len(EXISTING), 'existentes normalizadas')


main()
