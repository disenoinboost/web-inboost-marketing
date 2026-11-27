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
