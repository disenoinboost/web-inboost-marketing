# Hortelã Magenta · Sistema de diseño común

Fuente única: `fase2/gerador/estilos.py` (generador) y el bloque `:root` de `capa-fix/hm-boceto-fix.css` (CSS global). Las páginas del diseño original (Início, Serviços, Branding, Design Web, Camolas, Sobre, Blog, Contacto) se normalizan a las mismas reglas en `comum.normalizar`.

## Regla general

Un mismo papel tiene siempre el mismo estilo en todas las páginas. Las diferencias entre componentes solo existen cuando son decisiones de diseño, por ejemplo la escala propia de las fichas de proyecto.

## Espacio y rejilla

| Token | Valor | Uso |
|---|---|---|
| `--sp-block` | 126 px escritorio y tablet · 64 px móvil | Espacio arriba y abajo de cada sección |
| `--sp-title` | 64 px | Entre la cabecera de una sección y su contenido |
| `PAD` / `--hm-pad` | `clamp(16px,4vw,64px)` | Margen lateral de todas las secciones |
| `ROW` · `COL_L` · `COL_R` | Columnas 5:7, hueco `clamp(40px,6vw,120px)` | Secciones de dos columnas; se apilan por debajo de unos 840 px |

**Fondos:**
- Dos secciones seguidas nunca comparten fondo.
- Las franjas de fotos pegadas a su texto siguen el color de la sección anterior.

## Tipografía (por papel)

| Papel | Estilo |
|---|---|
| Antetítulo de sección (encima de un h1/h2) | 18 px, MAYÚSCULAS, espaciado .1em, color `#6E6A63`, raya magenta |
| Etiqueta (no encabeza un título: «Serviços neste projeto», «Mais projetos») | 18 px, frase normal, `#6E6A63` |
| H2 de sección (servicios, landings) | `clamp(40px,4.48vw,80px)` · 100 · -0.05em |
| H2 de sección de ficha de proyecto | `clamp(40px,5.12vw,80px)` |
| H2 de columna lateral (preguntas, listas) | `clamp(40px,3.84vw,74px)` |
| H2 de frase destacada | `clamp(40px,4.64vw,74px)` con iluminado al hacer scroll |
| Texto | 18 px / 1.5, `#4A4743` |
| Enlace subrayado | 18 px, borde inferior magenta de 1 px |
| Botón oscuro de contacto | 64 px de alto, fondo `#1C1B23`, letra 18 px · 300 |

## Colores

| Token | Color |
|---|---|
| `--hm-ink` | `#1C1B23` |
| `--hm-tx` | `#4A4743` |
| `--hm-mu` | `#6E6A63` |
| `--hm-magenta` | `#D82E87` |

**Grises de fondo:**
- `--hm-soft`: `#f6f7f8`
- `--hm-blue`: `#e8eced`
- `--hm-mist`: `#dde3e7`

## Movimiento

**Curvas:**
- `--hm-ease-out`: `cubic-bezier(.22,1,.36,1)`
- `--hm-ease-io`: `cubic-bezier(.76,0,.24,1)`

**Tiempos:** 0,2 s, 0,45 s y 0,9 s.

**Efectos y dónde se usan:**

| Efecto | Atributo y uso |
|---|---|
| Entrada al hacer scroll | `data-rise` en listas y textos |
| Iluminado de titulares | `data-colorize` en frases destacadas |
| Galerías que avanzan con el scroll | `data-lpf`: «Trabalhos» y «Aplicações» |
| Filas de fotos que se arrastran | `data-marquee` + `data-mq-drag` |
| Desplegables | `data-acc`, con escritura palabra a palabra al abrir |
| Cursor grande | Círculo de 96 px con texto de 12,5 px |
| Fundido de imágenes al cargar | 0,6 s |
