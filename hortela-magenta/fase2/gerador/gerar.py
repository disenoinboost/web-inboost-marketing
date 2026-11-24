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

SRC, INFO, PROJ, OUT = sys.argv[1:5]
os.makedirs(OUT, exist_ok=True)
M = Media(INFO, PROJ)
EXISTING = ['home', 'servicos', 'branding', 'design-web', 'projetos', 'camolas', 'sobre', 'blog', 'artigo', 'contacto']
ROUTES = {}   # caminho canónico -> ficheiro do pacote (sem .html)
LOCAL_OG = '/wp-content/uploads/hm-media/'


def og_local(url):
    return SITE + M.local(url) if url else None


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


def main():
    base_proj = load_tpl(SRC, 'camolas')
    P = projetos(M)
    for slug, p in P.items():
        write('projeto-' + slug, build_projeto(slug, p, base_proj))
        ROUTES['/projetos/' + slug] = 'projeto-' + slug
    # páginas existentes: alterações comuns
    for n in EXISTING:
        t = load_tpl(SRC, n)
        t = fix_existing_seo(n, t)
        t = normalizar(t)
        write(n, t)
    json.dump(ROUTES, open(os.path.join(OUT, 'rotas.json'), 'w'), indent=1, ensure_ascii=False)
    print('ok', len(ROUTES), 'páginas novas;', len(EXISTING), 'existentes normalizadas')


main()
