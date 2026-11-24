"""Hortelã Magenta · fase 2 · gera os modelos (template) das páginas novas e aplica as alterações comuns às existentes.

Uso: python3 -I gerar.py <dir-modelos-originais> <media-info.json> <oldproj.json> <dir-saida>
Escreve <dir-saida>/<pagina>.html (template, com os uuid dos recursos do pacote) e <dir-saida>/rotas.json.
"""
import json
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
    return SITE + (url if url.startswith('/wp-content/') else M.local(url))


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
    t = set_main(t, '\n\n'.join(parts))
    t = set_pidx(t, pidx)
    t = normalizar(t)
    return t


# ------------------------------------------------------------------------------------------- serviços
def blocks_html(blocks, slug):
    out = []
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
            out.append(B.proj_filme(b, sec_id=sid, label=label))
        elif kind == 'chips':
            out.append(BS.chips(b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'marquee':
            out.append(B.proj_marquee(M, b, sec_id=sid, label=label))
        elif kind == 'premios':
            out.append(BS.premios(M, b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'links':
            out.append(BS.links_rel(b, sid, label, **({'bg': bg} if bg else {})))
        elif kind == 'mais':
            out.append(B.proj_mais(M, b['items']))
        else:
            raise ValueError(kind)
    return out


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
    parts = [BS.hero(d['hero'])] + blocks_html(d.get('blocks', []), slug)
    if d.get('trabalhos'):
        parts.append(BS.trabalhos(M, d['trabalhos']))
    if d.get('testimonial'):
        parts.append(BS.testemunho(M, d['testimonial']))
    if d.get('faq'):
        parts.append(BS.faq(d['faq'], 'faq-' + slug.replace('servico-', '').replace('lp-', '')))
    c = d['contact']
    parts.append(BS.contacto_s(c[0], c[1], c[2], cta_href))
    t = set_main(t, '\n\n'.join(parts))
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
        write(n, t)
    json.dump(ROUTES, open(os.path.join(OUT, 'rotas.json'), 'w'), indent=1, ensure_ascii=False)
    print('ok', len(ROUTES), 'páginas novas;', len(EXISTING), 'existentes normalizadas')


main()
