"""Hortelã Magenta · fase 2 · utilidades comuns do gerador de páginas.

Os modelos (template) vêm dos pacotes de Claude Design (hm-paginas/*.html, parte __bundler/template).
As páginas novas partem de um modelo existente (cabeçalho, menus, rodapé e lógica intactos) e substituem
apenas o SEO do <helmet>, o conteúdo de <main> e alguns dados da lógica.
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://hortelamagenta.pt'
IMG = 'https://hortelamagenta.pt/media/pages/projetos/'

PROJ_SLUGS = ['camolas', 'consulai', 'knowledgebiz', 'queijaria-da-sao', 'hospital-garcia-de-orta', 'croma', 'alinea',
              'livro-vilamoura', 'farinhas-firmos', 'alsil', 'documentos-normativos-imt',
              'camara-municipal-de-almada-roteiro', 'imperalum']
LANDINGS = ['design-rotulos-vinho', 'design-comunicacao-industria', 'branding-clinicas-dentarias',
            'design-administracao-publica', 'design-de-eventos']


def esc(s):
    return html.escape(s, quote=False)


def att(s):
    return html.escape(s, quote=True)


class Media:
    """Medidas e caminhos locais dos medios (media-info.json, gerado no servidor a partir de hm-media)."""

    def __init__(self, info_path, proj_path):
        self.info = json.load(open(info_path, encoding='utf-8'))
        self.proj = json.load(open(proj_path, encoding='utf-8'))

    def find(self, slug, key, kind='img'):
        for m in self.proj[slug]['media']:
            if kind == 'img' and m['t'] == 'img' and key in m['src']:
                return m['src']
            if kind == 'video' and m['t'] == 'video' and (key in m['src'] or key in m['poster']):
                return m['src'], m['poster']
        raise KeyError(slug + ' ' + key)

    def wh(self, url):
        i = self.info.get(url)
        if i and i.get('wh'):
            return i['wh'][0], i['wh'][1]
        return None

    def ratio(self, url):
        d = self.wh(url)
        return '%d/%d' % d if d else '16/9'

    def local(self, url):
        i = self.info.get(url)
        return '/wp-content/uploads/hm-media/' + i['rel'] if i else url


def load_tpl(d, name):
    return open(os.path.join(d, name + '.html'), encoding='utf-8').read()


def split_helmet(t):
    i = t.index('</helmet>')
    return t[:i], t[i:]


# ---------------------------------------------------------------- SEO do helmet
def set_seo(t, title, desc, path, crumbs, og_img=None, robots=None, extra_ld=None):
    """path: caminho canónico ('/projetos/consulai'). crumbs: [(nome, caminho), ...] para o BreadcrumbList."""
    h, rest = split_helmet(t)
    url = SITE + path if path != '/' else SITE + '/'
    h = re.sub(r'<title>.*?</title>', '<title>' + esc(title) + '</title>', h, count=1, flags=re.S)
    h = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="' + att(desc) + '">', h, count=1)
    h = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="' + att(url) + '">', h, count=1)
    h = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="' + att(title) + '">', h, count=1)
    h = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="' + att(desc) + '">', h, count=1)
    h = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="' + att(url) + '">', h, count=1)
    if og_img:
        h = re.sub(r'<meta property="og:image" content="[^"]*">', '<meta property="og:image" content="' + att(og_img) + '">', h, count=1)
    if robots:
        h = h.replace('<link rel="canonical"', '<meta name="robots" content="' + att(robots) + '">\n<link rel="canonical"', 1)
    ld = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": (SITE + p if p != '/' else SITE + '/')} for i, (n, p) in enumerate(crumbs)]}]
    if extra_ld:
        ld += extra_ld
    h = re.sub(r'<script type="application/ld\+json">.*?</script>',
               lambda m: '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '</script>',
               h, count=1, flags=re.S)
    return h + rest


def set_main(t, inner, main_attrs=None):
    a = t.index('<main')
    b = t.index('>', a) + 1
    c = t.index('</main>', b)
    open_tag = t[a:b] if main_attrs is None else '<main ' + main_attrs + '>'
    return t[:a] + open_tag + '\n' + inner + '\n' + t[c:]


def set_page_current(t, current):
    return re.sub(r'("current":")[^"]*(")', lambda m: m.group(1) + current + m.group(2), t, count=1)


def set_pidx(t, items):
    """Barra flutuante «Neste projeto» (Camolas). items: [(ancora, rótulo)]; vazio = remove a barra."""
    a = t.find('<nav data-pidx=')
    if a < 0:
        return t
    b = t.index('</nav>', a) + 6
    if not items:
        return t[:a] + t[b:]
    li = ''.join(
        '\n    <li><a data-pidx-a="" href="#' + att(h) + '" style="display:flex; flex-direction:row; align-items:center; gap:8px; min-height:44px; padding:0 2px; color:rgba(28,27,35,.7); text-decoration:none; white-space:nowrap; transition:color 0.2s ease;"><span aria-hidden="true" style="display:block; width:7px; height:7px; border-radius:50%; border:1px solid rgba(28,27,35,.45); background:transparent; transition:background 0.2s, border-color 0.2s, transform .3s;"></span><span style="font-size:18px; white-space:nowrap;">' + esc(l) + '</span></a></li>'
        for h, l in items)
    nav = t[a:b]
    i = nav.index('<ol')
    i = nav.index('>', i) + 1
    j = nav.index('</ol>')
    return t[:a] + nav[:i] + li + '\n  ' + nav[j:] + t[b:]


def words_split(text, maxw=None):
    return text.split()


def sentences(text):
    parts = re.split(r'(?<=[.!?…])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ«“"])', text.strip())
    return [p for p in parts if p]
