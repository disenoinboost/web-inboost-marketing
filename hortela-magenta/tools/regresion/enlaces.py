"""Inventario de enlaces de las plantillas publicadas (fase2/modelos): internos, externos, web antigua, anclas.
Uso: python3 -I enlaces.py <dir-modelos> <routes.json> <salida.json>"""
import html, json, os, re, sys
from collections import defaultdict

d, routes_f, out = sys.argv[1], sys.argv[2], sys.argv[3]
routes = json.load(open(routes_f))
known = {k.rstrip('/') or '/' for k in routes}
page_of = {v: k for k, v in routes.items()}
A = re.compile(r'''<a\b[^>]*?\bhref\s*=\s*["']([^"']+)["']''', re.I)
SRC = re.compile(r'''\b(?:src|poster|data-src)\s*=\s*["']([^"'{}]+)["']''', re.I)
SRCSET = re.compile(r'''\bsrcset\s*=\s*["']([^"']+)["']''', re.I)
JSONURL = re.compile(r'''["'](https?://[^"'\s<>\\]+|/(?:projetos|servicos|sobre|blog|contacto|design-|branding-|politica|mapa|obrigado)[^"'\s<>\\]*)["']''')
IDS = re.compile(r'''\bid\s*=\s*["']([^"'{}]+)["']''')
res = {'internos': defaultdict(set), 'externos': defaultdict(set), 'antiga_paginas': defaultdict(set), 'antiga_media': defaultdict(set),
       'anclas_rotas': defaultdict(set), 'tel_mail': defaultdict(set), 'recursos_ext': defaultdict(set)}
for f in sorted(os.listdir(d)):
    if not f.endswith('.html'):
        continue
    name = f[:-5]
    route = page_of.get(name, name)
    t = open(os.path.join(d, f), encoding='utf-8').read()
    ids = set(IDS.findall(t))
    hrefs = set(html.unescape(h) for h in A.findall(t)) | set(html.unescape(h) for h in JSONURL.findall(t))
    srcs = set(html.unescape(s) for s in SRC.findall(t))
    for ss in SRCSET.findall(t):
        for part in ss.split(','):
            u = part.strip().split(' ')[0]
            if u:
                srcs.add(html.unescape(u))
    for h in hrefs:
        if '{{' in h:
            continue
        if h.startswith(('tel:', 'mailto:')):
            res['tel_mail'][h].add(route)
        elif h.startswith('#'):
            if len(h) > 1 and h[1:] not in ids:
                res['anclas_rotas'][h].add(route)
        elif re.match(r'https?://(www\.)?hortelamagenta\.pt', h):
            (res['antiga_media'] if '/media/' in h else res['antiga_paginas'])[h].add(route)
        elif h.startswith('http'):
            res['externos'][h].add(route)
        elif h.startswith('/'):
            res['internos'][h].add(route)
    for s in srcs:
        if '{{' in s or s.startswith('data:'):
            continue
        if re.match(r'https?://(www\.)?hortelamagenta\.pt', s):
            res['antiga_media'][s].add(route)
        elif s.startswith('http'):
            res['recursos_ext'][s].add(route)
out_d = {k: {u: sorted(v) for u, v in sorted(m.items())} for k, m in res.items()}
# internos: o caminho sem âncora/parâmetros existe no mapa de rotas?
paths = defaultdict(set)
for u, pages in out_d['internos'].items():
    p = u.split('#')[0].split('?')[0]
    paths[p.rstrip('/') or '/'].update(pages)
out_d['internos_desconhecidos'] = {p: sorted(v) for p, v in sorted(paths.items()) if p not in known and not p.startswith('/wp-content') and not p.startswith('/wp-json')}
out_d['internos_caminhos'] = sorted(paths)
json.dump(out_d, open(out, 'w'), ensure_ascii=False, indent=1)
for k in ('internos', 'externos', 'antiga_paginas', 'antiga_media', 'anclas_rotas', 'tel_mail', 'recursos_ext', 'internos_desconhecidos'):
    print(k.ljust(24), len(out_d[k]))
