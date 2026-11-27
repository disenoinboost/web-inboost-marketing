"""Sistema de desenho comum da Hortelã Magenta (2026-11-27).

Uma só fonte para as medidas, as cores, a escala tipográfica e os componentes repetidos de todas as páginas geradas
(serviços, landings, fichas de projeto, legais) e para as regras com que se normalizam as páginas do desenho original
(Início, Serviços, Branding, Design Web, Camolas, Sobre, Blog, Contacto). Os valores são os do desenho original;
o que aqui se fixa é que o mesmo papel tenha sempre o mesmo estilo em toda a web.

Medidas que vivem no CSS (variáveis definidas pelos modelos e por capa-fix/hm-boceto-fix.css):
  --sp-block   espaço vertical de cada secção (126 px no computador, 64 px no telemóvel)
  --sp-title   espaço entre o cabeçalho de uma secção e o seu conteúdo (64 px)
  --sp-hdr     espaço por cima do cabeçalho de página (por baixo do menu)
"""
import re

# --- cores -----------------------------------------------------------------------------------------------------------
INK = '#1C1B23'        # texto principal, botões
TX = '#4A4743'         # texto corrido
MU = '#6E6A63'         # antetítulos, números, legendas
MAGENTA = '#D82E87'    # traço dos antetítulos, sublinhados, foco
GREY_SOFT = '#f6f7f8'  # fundos: tom «soft»
GREY_BLUE = '#e8eced'  # fundos: tom «blue» (o da cabeçalho e do contacto)
GREY_MIST = '#dde3e7'  # fundos: tom «mist»
LINE = 'rgba(28,27,35,.12)'  # linhas separadoras

# --- espaço e rejilha ------------------------------------------------------------------------------------------------
PAD = 'clamp(16px,4vw,64px)'      # margem lateral de todas as secções
SP_BLOCK = 'var(--sp-block)'
SP_TITLE = 'var(--sp-title)'
# duas colunas 5:7 (esquerda: antetítulo + título; direita: texto/lista); abaixo de ~840 px empilham
ROW = 'display:flex; flex-wrap:wrap; align-items:flex-start; gap:32px clamp(40px,6vw,120px);'
COL_L = 'flex:5 1 300px; min-width:0;'
COL_R = 'flex:7 1 420px; min-width:0;'

# --- tipografia (papéis) ---------------------------------------------------------------------------------------------
# Antetítulo de secção (por cima de um título): maiúsculas espaçadas com o traço magenta.
EYEBROW = f'font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{MU};'
# Etiqueta (não encabeça um título: «Serviços neste projeto», «Mais projetos»…): frase normal.
LABEL = f'font-size:18px; color:{MU};'
H2_SECTION = 'font-size:clamp(40px,4.48vw,80px); font-weight:100; letter-spacing:-0.05em; line-height:1.05;'   # títulos de secção (serviços, landings)
H2_PROJECT = 'font-size:clamp(40px,5.12vw,80px); font-weight:100; letter-spacing:-0.05em; line-height:1.04;'   # títulos de secção das fichas (Camolas)
H2_SIDE = 'font-size:clamp(40px,3.84vw,74px); font-weight:100; letter-spacing:-0.05em; line-height:1.06;'      # coluna lateral (perguntas, listas)
H2_STATEMENT = 'font-size:clamp(40px,4.64vw,74px); font-weight:100; letter-spacing:-0.05em; line-height:1.04;' # frase destacada
BODY = f'font-size:18px; line-height:1.5; color:{TX};'

DASH = f'<span style="color:{MAGENTA};">—</span>'
DASH_A = f'<span aria-hidden="true" style="color:{MAGENTA};">—</span>'

# --- movimento -------------------------------------------------------------------------------------------------------
EASE_OUT = 'cubic-bezier(.22,1,.36,1)'
EASE_IO = 'cubic-bezier(.76,0,.24,1)'


def eyebrow(text_html, mb='24px', color=MU):
    """Antetítulo de secção (o texto já vem escapado)."""
    return f'<p style="margin:0 0 {mb}; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{color};">{DASH_A} {text_html}</p>'


# Antetítulos em frase normal que estão logo por cima de um título (h1/h2): passam ao estilo de antetítulo de secção.
# Só há duas formas no projeto (desenho original e blocos copiados dele): cor fixa (#6E6A63) e cor da secção (var(--mu)).
_ANTE = re.compile(r'<p style="margin:0 0 18px; font-size:18px; color:(#6E6A63|var\(--mu\));">(\s*<span[^>]*>—</span>[^<]{1,80}</p>\s*<h[12]\b)')


def normalizar_antetitulos(html):
    return _ANTE.sub(lambda m: f'<p style="margin:0 0 24px; font-size:18px; letter-spacing:.1em; text-transform:uppercase; color:{m.group(1)};">{m.group(2)}', html)


# ---------------------------------------------------------------------------------------------------------------------------
# Aviso das galerias que se arrastam e abrem em grande (2026-11-27, pedido de Laura: «que sepa el usuario»).
# Por baixo de cada galeria com arrastar (data-drag / data-mq-drag) e ampliar (data-lb): fichas, serviços, landings,
# Design Web · Conteúdos, Sobre · Hortelanices e Camolas · Fotografia. O texto muda com o tipo de ecrã (rato / táctil),
# com as mesmas marcas data-hm-hint-fine / data-hm-hint-touch das linhas que se abrem.
DICA_GALERIA = (f'<p data-hm-gal-hint="" style="margin:clamp(16px,2vw,24px) 0 0; padding:0 {PAD}; font-size:18px; font-weight:400; '
                f'color:color-mix(in srgb, {INK} 60%, transparent);"><span aria-hidden="true" style="color:{MAGENTA};">↔</span> '
                '<span data-hm-hint-fine="">Arraste para ver mais · Clique para ampliar</span>'
                '<span data-hm-hint-touch="">Deslize para ver mais · Toque para ampliar</span></p>')
_SEC = re.compile(r'<section\b.*?</section>', re.S)
_CAMOLAS_HINT = re.compile(r'<p style="margin:clamp\(16px,2vw,24px\) 0 0; padding:0 clamp\(16px,4vw,64px\);[^"]*"><span aria-hidden="true" style="color:#D82E87;">↔</span> Arraste para ver mais</p>')
_SOBRE_HINT = '<p style="margin:14px 0 0; font-size:18px; color:rgba(28,27,35,.6); font-weight:400;">Arraste para ver mais →</p>'


def dicas_galerias(html):
    """Põe DICA_GALERIA no fim de cada secção que tem uma galeria de arrastar e ampliar (uma só vez por secção).
    Substitui os avisos antigos («Arraste para ver mais» de Camolas por baixo e de Sobre no cabeçalho)."""
    def sec(m):
        s = m.group(0)
        if 'data-lb=""' not in s or not re.search(r'data-(?:mq-)?drag=""', s) or 'data-hm-gal-hint' in s:
            return s
        s = s.replace(_SOBRE_HINT, '')
        if _CAMOLAS_HINT.search(s):
            return _CAMOLAS_HINT.sub(DICA_GALERIA, s, count=1)
        return s[:-len('</section>')].rstrip() + '\n  ' + DICA_GALERIA + '\n</section>'
    return _SEC.sub(sec, html)


# ---------------------------------------------------------------------------------------------------------------------------
# Imagens de partilha (og:image) apontam para a cópia local em hm-media, como as imagens da página (2026-11-27).
# A mesma regra de hm_media_local() (hm-boceto-dist.php): hm-media/<host><caminho>, JPG/PNG passam a WebP.
_MEDIA_PREFIXOS = ('https://hortelamagenta.pt/media/', 'https://nostalgia.hortelamagenta.pt/old/wp-content/',
                   'https://www.adrepes.pt/wp-content/uploads/', 'https://www.minhaterra.pt/wst/images/', 'https://www.coprate.pt/images/')


def media_local(url):
    """Caminho local (/wp-content/uploads/hm-media/...) de um medio remoto copiado; devolve o URL tal qual se não for um deles."""
    if not url or not url.startswith(_MEDIA_PREFIXOS):
        return url
    rest = url.split('://', 1)[1]
    return '/wp-content/uploads/hm-media/' + re.sub(r'\.(jpe?g|png)$', '.webp', rest, flags=re.I)


def og_imagens_locais(head, site):
    """og:image dos modelos do desenho (Início, Branding, Sobre…): da web antiga para a cópia local, no domínio de produção."""
    def r(m):
        u = m.group(1)
        if u.startswith(site + 'https://'):  # domínio repetido (gerado antes com SITE + URL absoluto)
            u = u[len(site):]
        loc = media_local(u)
        return '<meta property="og:image" content="' + (site + loc if loc.startswith('/') else loc) + '">'
    return re.sub(r'<meta property="og:image" content="([^"]*)">', r, head)

