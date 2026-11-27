"""Alterações comuns a todas as páginas (existentes e novas): ligações, menus e rodapé.

- Ligações para a web antiga (https://hortelamagenta.pt/projetos/x, landings, política) passam a internas.
- URL internas sem barra final, como as da web atual (/servicos, /projetos/camolas). As landings mantêm a barra.
- Gráfico + Editorial, Campanhas & Redes Sociais, Fotografia & Vídeo e Avenças passam das âncoras de /servicos
  às suas páginas; Coaching de Marcas entra nos menus e no rodapé.
- Menu móvel: todos os projetos debaixo de «Projetos». Seletor «EN» retirado (não há versão inglesa).
Só se toca no que vem depois de </helmet> (canonical, og:url e JSON-LD ficam como estão ou são definidos à parte).
"""
import json
import re

from base import PROJ_SLUGS, LANDINGS, att, esc
from dados_projetos import ORDER, NAMES, CARD
from estilos import normalizar_antetitulos, dicas_galerias, og_imagens_locais

NEW_SVC = {
    '/servicos#design-grafico-e-editorial': '/servicos/design-grafico-e-editorial',
    '/servicos#campanhas-e-redes-sociais': '/servicos/campanhas-e-redes-sociais',
    '/servicos#fotografia-e-video': '/servicos/fotografia-e-video',
    '/servicos#avencas-mensais': '/servicos/avenca-comunicacao-360',
}


def _links(b):
    # web antiga -> interno
    b = re.sub(r'https://(?:www\.)?hortelamagenta\.pt/projetos/([a-z0-9-]+)(?=["\'])',
               lambda m: '/projetos/' + m.group(1) if m.group(1) in PROJ_SLUGS else m.group(0), b)
    b = b.replace("'https://hortelamagenta.pt/projetos/' +", "'/projetos/' +")
    for lp in LANDINGS:
        b = re.sub(r'https://(?:www\.)?hortelamagenta\.pt/' + lp + r'/?(?=["\'])', '/' + lp + '/', b)
    b = b.replace('href="https://hortelamagenta.pt/politica-de-privacidade"', 'href="/politica-de-privacidade"')
    b = b.replace('href="https://hortelamagenta.pt/projetos"', 'href="/projetos"')
    b = b.replace('href="https://hortelamagenta.pt/servicos"', 'href="/servicos"')
    b = b.replace('href="https://hortelamagenta.pt/sobre#equipa"', 'href="/sobre#equipa"')
    # sem barra final nas rotas internas (entre aspas, com âncora opcional)
    b = re.sub(r'(?<=["\'])/(servicos|projetos|sobre|blog|contacto)((?:/[a-z0-9-]+)*)/(?=(?:#[a-z0-9-]*)?["\'](?!\s*\+))', r'/\1\2', b)
    # âncoras de /servicos -> páginas próprias
    for a, n in NEW_SVC.items():
        b = re.sub(re.escape(a) + r'(?=["\'])', n, b)
    return b


MOB_SUB = '<a href="{h}" style="color:#9C978E; text-decoration:none; font-size:18px; font-weight:300; line-height:1.4; padding:5px 0;">{l}</a>'
SERVICES_MENU = [
    ('/servicos/branding', 'Branding'), ('/servicos/design-web', 'Design Web'),
    ('/servicos/design-grafico-e-editorial', 'Gráfico + Editorial'),
    ('/servicos/campanhas-e-redes-sociais', 'Campanhas &amp; Redes Sociais'),
    ('/servicos/fotografia-e-video', 'Fotografia &amp; Vídeo'),
    ('/servicos/avenca-comunicacao-360', 'Avenças mensais'),
    ('/servicos/coaching-de-marcas', 'Coaching de Marcas'),
]


def _menus(b):
    # menu móvel · Serviços
    i = b.find('<nav aria-label="Menu"')
    if i >= 0:
        j = b.index('</nav>', i)
        nav = b[i:j]
        a = nav.index('<a href="/servicos"')
        a = nav.index('<div', a)
        a2 = nav.index('>', a) + 1
        c = nav.index('</div>', a2)
        subs = '\n      ' + '\n      '.join(MOB_SUB.format(h=h, l=l) for h, l in SERVICES_MENU) + '\n    '
        nav = nav[:a2] + subs + nav[c:]
        # menu móvel · Projetos (todos)
        a = nav.index('<a href="/projetos"')
        a = nav.index('<div', a)
        a2 = nav.index('>', a) + 1
        c = nav.index('</div>', a2)
        # mesma prioridade que o menu do computador (os seis destacados) e depois os restantes, pela ordem da página Projetos
        top = ['camolas', 'queijaria-da-sao', 'farinhas-firmos', 'alsil', 'hospital-garcia-de-orta', 'livro-vilamoura']
        mob = top + [s for s in ORDER if s not in top]
        subs = '\n      ' + '\n      '.join(MOB_SUB.format(h='/projetos/' + s, l=esc(NAMES[s])) for s in mob) + '\n    '
        nav = nav[:a2] + subs + nav[c:]
        b = b[:i] + nav + b[j:]
    # rodapé · coluna Serviços
    i = b.find('<footer')
    if i >= 0:
        a = b.index('<a href="/servicos" style="display:block; margin:0 0 20px;', i)
        a = b.index('<div', a)
        a2 = b.index('>', a) + 1
        c = b.index('</div>', a2)
        foot = '\n        ' + '\n        '.join('<a href="%s" style="color:#FFFFFF; text-decoration:none;">%s</a>' % (h, l) for h, l in SERVICES_MENU) + '\n      '
        b = b[:a2] + foot + b[c:]
        # rodapé · ligações legais
        b = b.replace('<a href="https://www.livroreclamacoes.pt/Inicio/" style="color:#FFFFFF; font-weight:400; text-decoration:none;">Livro de Reclamações</a>',
                      '<a href="/politica-de-cookies" style="color:#FFFFFF; font-weight:400; text-decoration:none;">Política de Cookies</a>\n      ' + COOKIE_BTN + '\n      <a href="/mapa-do-site" style="color:#FFFFFF; font-weight:400; text-decoration:none;">Mapa do site</a>\n      <a href="https://www.livroreclamacoes.pt/Inicio/" target="_blank" rel="noopener" style="color:#FFFFFF; font-weight:400; text-decoration:none;">Livro de Reclamações</a>', 1)
    # cabeçalho · seletor EN (não existe versão inglesa)
    b = re.sub(r'\s*<a data-intro="" href="https://hortelamagenta\.pt/en"[^>]*>EN</a>', '<span hidden></span>', b, count=1)
    return b


COACH = ("      { n: '07', name: 'Coaching de Marcas', short: 'Sessões para clarificar posicionamento, identidade e comunicação.', "
         "desc: 'Às vezes, a sua marca só precisa de ser ouvida. Fazemos as perguntas certas e ajudamos a marca a encontrar as suas próprias respostas.', "
         "chips: ['Escuta', 'Diagnóstico', 'Clarificação', 'Direção'], cta: 'Explorar Coaching de Marcas', "
         "img: 'https://hortelamagenta.pt/media/pages/projetos/alinea/9de4876d63-1710332653/hortelamagenta_portfolio_alinea_estacionario-1900x.jpg', "
         "megaSize: 'clamp(22px,1.9vw,30px)', href: '/servicos/coaching-de-marcas' },\n")


def _logic(b):
    # serviços do menu de PC (lista JS)
    b = b.replace("cta: 'Ver serviços', img: U.camLabel", "cta: 'Explorar Gráfico + Editorial', img: U.camLabel")
    b = b.replace("cta: 'Ver serviços', img: U.ffSocial", "cta: 'Explorar Campanhas & Redes Sociais', img: U.ffSocial")
    b = b.replace("cta: 'Ver serviços', img: U.ffFab", "cta: 'Explorar Fotografia & Vídeo', img: U.ffFab")
    b = b.replace("megaSize: 'clamp(22px,1.9vw,30px)', href: '/servicos/avenca-comunicacao-360' },\n    ].map(",
                  "megaSize: 'clamp(22px,1.9vw,30px)', href: '/servicos/avenca-comunicacao-360' },\n" + COACH + "    ].map(")
    b = b.replace("cta: 'Ver serviços', img: 'https://hortelamagenta.pt/media/pages/projetos/camolas/34c1b44fdb-1735900095/hortelamagenta_portfolio_marca_camolas_estacionario-1900x.jpg'",
                  "cta: 'Explorar Avenças mensais', img: 'https://hortelamagenta.pt/media/pages/projetos/camolas/34c1b44fdb-1735900095/hortelamagenta_portfolio_marca_camolas_estacionario-1900x.jpg'")
    b = b.replace('"Ficha de projeto"', '"Branding"')
    return b


# Botão do rodapé que volta a abrir o painel de consentimento do Complianz (o JS do Complianz 7 escuta button.cmplz-manage-consent).
COOKIE_BTN = ('<button type="button" class="cmplz-manage-consent hm-cookies" style="appearance:none; -webkit-appearance:none; background:none; border:0; '
              'padding:0; margin:0; font:inherit; letter-spacing:inherit; text-transform:inherit; color:#FFFFFF; font-weight:400; cursor:pointer;">'
              'Preferências de cookies</button>')

# Valores do ajuste «identidadeFundo» do modelo Camolas (só no código): em português.
PT_PROPS = [('Gris claro', 'Cinza claro'), ('Gris oscuro', 'Cinza escuro'), ("'Negro'", "'Preto'"), ('&quot;Negro&quot;', '&quot;Preto&quot;'), ('"Negro"', '"Preto"')]


def normalizar(t):
    i = t.index('</helmet>')
    h, b = t[:i], t[i:]
    b = normalizar_antetitulos(b)  # sistema de desenho comum (estilos.py)
    b = dicas_galerias(b)  # aviso «Arraste/Deslize… · Clique/Toque… para ampliar» por baixo das galerias
    # morada: o cid dos modelos do desenho abria outra empresa (Fitplace Calpe); a ligação certa é a da web antiga («Direções»)
    b = b.replace('https://www.google.com/maps?cid=12848211740159704585', 'https://maps.app.goo.gl/iV6yJoYW8JyYDM898')
    # botão escuro de contacto: o mesmo peso de letra em todas as páginas (a página inicial tinha 400; as outras 300)
    b = b.replace('font-size:18px; font-weight:400; box-shadow:0 14px 30px -16px rgba(28,27,35,.55);', 'font-size:18px; font-weight:300; box-shadow:0 14px 30px -16px rgba(28,27,35,.55);')
    b = _links(b)
    b = _menus(b)
    b = _logic(b)
    for a, n in PT_PROPS:
        b = b.replace(a, n)
    h = og_imagens_locais(h, 'https://hortelamagenta.pt')  # imagem de partilha: cópia local, não a web antiga
    return h + b


def fix_existing_seo(name, t):
    """Canonical de Branding e Design Web apontava para URL de uma proposta SEO (/branding-para-empresas,
    /websites-para-empresas) que não é onde a página se publica: passa à URL real."""
    m = {'branding': ('/branding-para-empresas', '/servicos/branding'), 'design-web': ('/websites-para-empresas', '/servicos/design-web')}
    if name in m:
        a, n = m[name]
        t = t.replace('https://hortelamagenta.pt' + a, 'https://hortelamagenta.pt' + n)
    return t
