"""Converte os modelos gerados em páginas «dist» locais (como hm_dist_build no servidor) para as testar com o Chromium.
Uso: python3 -I dist_local.py <dir-modelos> <manifests.json> <dir-dist>   (escreve <dir-dist>/<pagina>.html e routes.json)
"""
import json
import os
import re
import sys

TPL, MAN, DST = sys.argv[1:4]
man = json.load(open(MAN))
EXT = {'text/javascript': 'js', 'application/javascript': 'js', 'image/svg+xml': 'svg', 'font/woff2': 'woff2', 'image/jpeg': 'jpg', 'image/png': 'png'}
uu = {}
for page in man.values():
    for u, (mime, size, sha) in page['man'].items():
        uu[u] = '/wp-content/themes/divi-child/hm-paginas/dist/a/%s.%s' % (sha, EXT.get(mime, 'bin'))
res = {'https://unpkg.com/react@18.3.1/umd/react.production.min.js': uu['aa77ae4c-49f5-4957-a1e6-5c4df4018e50'],
       'https://unpkg.com/react-dom@18.3.1/umd/react-dom.production.min.js': uu['feb8ddc9-d056-4d91-ad01-915cd0f20e5f'],
       'assets/logo-hm.svg': uu['959ea1b6-addf-411e-aa55-d4c1822f6839']}
PREF = {'https://hortelamagenta.pt/media/': '/wp-content/uploads/hm-media/hortelamagenta.pt/media/',
        'https://nostalgia.hortelamagenta.pt/old/wp-content/': '/wp-content/uploads/hm-media/nostalgia.hortelamagenta.pt/old/wp-content/'}
os.makedirs(DST, exist_ok=True)
routes = json.load(open(os.path.join(TPL, 'rotas.json'))) if os.path.exists(os.path.join(TPL, 'rotas.json')) else {}
base_routes = {'/': 'home', '/servicos': 'servicos', '/servicos/branding': 'branding', '/servicos/design-web': 'design-web',
               '/projetos': 'projetos', '/projetos/camolas': 'camolas', '/sobre': 'sobre', '/blog': 'blog',
               '/blog/quanto-custa-um-site': 'artigo', '/contacto': 'contacto'}
allr = dict(base_routes)
for k, v in routes.items():
    allr[k.rstrip('/') or '/'] = v
for f in os.listdir(TPL):
    if not f.endswith('.html'):
        continue
    t = open(os.path.join(TPL, f), encoding='utf-8').read()
    for u, p in uu.items():
        t = t.replace(u, p)
    head = '<style>x-dc{display:none!important}</style><script>window.__resources=' + json.dumps(res) + ';</script>'
    t = re.sub(r'<head\b[^>]*>', lambda m: m.group(0) + head, t, count=1)
    t = re.sub(r'<script\b(?![^>]*\b(?:defer|async|type=))([^>]*\ssrc="/wp-content/themes/divi-child/hm-paginas/dist/a/[^"]+\.js"[^>]*)>', r'<script defer\1>', t)

    def med(m):
        u = m.group(0)
        for a, b in PREF.items():
            if u.startswith(a):
                u = b + u[len(a):]
        return re.sub(r'\.(jpe?g|png)$', '.webp', u, flags=re.I)
    t = re.sub(r'https://(?:hortelamagenta\.pt/media|nostalgia\.hortelamagenta\.pt/old/wp-content)/[^\s\'"()<>,`\\]+', med, t)
    open(os.path.join(DST, f), 'w', encoding='utf-8').write(t)
json.dump(allr, open(os.path.join(DST, 'routes.json'), 'w'), indent=1)
print('dist ok', len(allr), 'rotas')
