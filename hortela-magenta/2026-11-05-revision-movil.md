# Hortelã Magenta · revisión móvil de Laura (2026-11-05)

Sitio: https://hortelamagenta.inboost.marketing (páginas servidas desde los paquetes de Claude Design, `hm-paginas/`).
Todo va en la capa propia `wp-content/themes/divi-child/assets/hm-boceto-fix.css` y `.js` (se inyecta al servir cada página y sobrevive a kits nuevos). Copia de esta versión en `capa-fix/`. Copias previas en el servidor: `hm-boceto-fix.css.bak-20261105-082625` y `hm-boceto-fix.js.bak-20261105-082728`.

## Hecho

| Punto | Causa | Cambio |
|---|---|---|
| Logo distinto con el menú abierto | El panel tenía 20 px de margen y logo de 150 px; la cabecera 16 px y 148 px | Mismo margen, alto y ancho; la × queda donde el ☰ |
| Home · «Showreel» encima de «Veja o showreel» | El título sube 67 px con el scroll | Sin desplazamiento en móvil |
| Home · vídeo lento | MP4 con el índice (moov) al final y `preload="none"` | Faststart sin recomprimir en 7 MP4 (originales en `uploads/hm-media-bak-2026-11-05/`) + precarga 1,5 pantallas antes |
| Títulos de servicios | 25 px y corte de palabra | 21 px en una línea (H1 37 px) |
| Opiniones (Home, Serviços, Sobre) | Pestañas de 170 px: 2 exactas | 2,5 por pantalla; la cortada, borrosa y atenuada hasta entrar |
| FAQ | Preguntas a 25 px, casi como el H2 | 19 px y menos relleno |
| Branding / Design Web · Trabalhos | Galería fijada con scroll; el texto de entrada lo tapaba el primer cartón | Carrusel con el dedo (scroll-snap), texto completo, «Deslize para o lado →», botón «Ver projeto →», nombres a 26 px que pueden partirse |
| Design Web · Âmbito | Filas de 44 px | 10 px más de aire arriba y abajo |
| Projetos · galería | Columnas de 96 px con 28 px de hueco, más bajas que el marco: no se movían | Huecos de 8 px, columnas de 119 px y marco de 150vw: se mueven con el scroll |
| Projetos · índice | Mayúsculas | Minúsculas |
| Camolas · título y entradilla | 62 px y 20 px | 37 px y 16 px (como Branding); servicios a 14 px |
| Camolas · identidade | Escenario vertical de 608 px: imágenes recortadas | Cortinas horizontales: imagen entera 3:2 arriba y lista 01-04 debajo |
| Camolas · rótulos | Galería fijada con scroll | Carrusel con el dedo; el texto queda fijo arriba |
| Camolas · filme | Mismo problema de MP4 | Faststart + precarga |
| Camolas · barra «Neste projeto» | El diseño solo la muestra desde 900 px | Visible en móvil a 13 px, con la sección actual marcada |
| Camolas · mais projetos | 2 columnas de 405 px | 1 columna de 150 px |
| Sobre · Hortelanices (PC y móvil) | 19 fotos montadas en JS con un prefijo: el espejo no las descargó (404) | Descargadas al servidor (máx. 1200 px, JPG q80) |
| Blog · barra de temas | 18 px | 14 px |
| Artículo · entradilla | 24 px | 16 px (el título ya medía 37 px, igual que Branding) |
| PC · menú | Logo 274 px, menú 19,6 px | Logo 230 px, menú 17 px, «Pedir orçamento» 18 px; desplegables de Serviços y Projetos más compactos |

## Pendiente

- **Camolas · O site:** las capturas móviles del diseño miden 390 px de ancho (`dist/a/99266298c7a73406.jpg`, `26d667bc8ea1fccf.jpg`, `4c058854c64f119c.jpg`); en pantallas 3x se ven borrosas. Hacen falta capturas de 1170 px de ancho de adegacamolas.pt (vinhos, regiao-vinhas, experiencias). Desde esta sesión no se llega a esa web ni al servidor para subir imágenes grandes, y el servicio de capturas externo devolvió solo la verificación de edad.
- **Vídeos más ligeros para móvil:** el servidor no tiene ffmpeg; el showreel (1080p, 7 MB) y el filme de Camolas (13 MB) bajarían a la mitad o menos con versiones 720p.

## Verificación

Render local con Chromium (390×844 y 1440×900) de las 10 páginas: ancho del documento = ventana, 0 errores JS; escritorio sin cambios salvo el menú. En el servidor: las 4 páginas probadas responden 200 con la versión nueva de la capa y las fotos de Hortelanices 200 `image/jpeg`. WP Rocket vaciado (`hm_dist_reset()`).

## Segunda ronda (2026-11-05, tarde)

Copia previa en el servidor: `hm-boceto-fix.css.bak-20261105-091715`.

| Punto | Antes | Ahora |
|---|---|---|
| Título de cabecera en PC (1440 px) | Camolas 124 px, Branding/Design Web 98, artículo 67, resto 83 | Todos 83 px (`clamp(40px, 5.76vw, 102px)`; Branding y Design Web conservan el límite de su columna). «Hospital Garcia de Orta» cabe en una línea a 1440 y 1110 px. La Home no se toca |
| Título de cabecera en móvil | 37 px, hasta 4 líneas (Serviços, Contacto, Projetos, Blog) | 30 px a 390 px (`clamp(26px, 7.7vw, 34px)`), máximo 3 líneas en todas |
| Antetítulo de Branding/Design Web en PC | Centrado en la altura: 125 px bajo las migas | Justo debajo de las migas |
| Entradilla de la ficha de proyecto en PC | 24,5 px (servicios 18) | 18 px como las demás (servicios 16) |
| Entradilla del artículo en PC | 27 px | 18 px |
| Home · botones del showreel en móvil | «Ver completo com som» en 3 líneas y fuera de la caja | «Showreel» encima; los dos botones en una línea a 14 px |

## Tercera ronda (2026-11-05, móvil salvo indicación)

Copias previas en el servidor: `hm-boceto-fix.css/.js.bak-20261105-<hora>` y `hm-boceto.php.bak-20261105-<hora>`.

| Punto | Cambio |
|---|---|
| Home · servicios | Mismo estilo que el índice de Projetos: número de 16 px en gris, título a 28 px, 16 px de aire y líneas arriba y abajo |
| Barra «Pedir orçamento · Ligar» | Nueva barra fija abajo en móvil (como la de Camolas). Aparece tras el primer pantallazo y se oculta en el pie, en «Contacto», en el showreel y en la galería de trabajos. Sube las otras barras (blog, filtros de Projetos, Camolas). No se muestra en /contacto/ ni en PC |
| Branding / Design Web · Trabalhos | Vuelve el diseño original (pantalla completa, fondo, texto de entrada, tarjetas altas); se pasa con el dedo (scroll-snap) y lleva «Ver projeto →» en lugar del +; nombre a 30 px que puede partirse |
| Branding / Design Web · cabecera | En móvil solo la primera frase de la entradilla (script en línea tras `</x-dc>`, `assets/hm-entradilla-movil.html`): cabe en 664 px (antes 767 y 695) |
| Branding · Ponto de partida | Causa: mis reglas de las cortinas de Camolas usaban `#identidade`, que también existe en Branding. Ahora solo `section#identidade[data-tone] [data-step]:not([data-step-v])` |
| Camolas · rótulos | Las reglas de tarjetas de Branding también les afectaban: el nombre vuelve a estar pegado a la izquierda, el número a la derecha y 16 px bajo la imagen |
| Camolas · identidade | Imagen a `cover`, ocupa todo el hueco 3:2 |
| Camolas · O site | Capturas nuevas de adegacamolas.pt a 2x (780×6400; primeros 3.200 px de cada página, porque Vinhos mide 30.600 px y Região 16.190). La sección mide el doble (1000vh) para que pasen más despacio. Nota: Experiências muestra «Temporariamente Encerrado» en la web actual |
| Vídeos | Versiones ligeras solo en móvil, sin audio (en la web van silenciados): showreel 7,0 → 2,1 MB (720p), filme 13,5 → 3,4 MB, João Bordeira 9,3 → 1,8 MB (540p). En `uploads/hm-media/movil/` |
| Favicon | El de hortelamagenta.pt (`favicon.png`, `safari-mask-icon.svg`), más `/favicon.ico` y `apple-touch-icon.png` de 180 px generado desde el SVG |
| Projetos · galería | A pantalla completa (100svh), con columnas a 120vw para que sean más altas que el marco y se muevan |
| Projetos · filtro | Cuando un proyecto se repite, sale otra foto del mismo proyecto (rotando si tiene pocas). Solo en móvil, como lo demás |

Transferencia: los vídeos y capturas se subieron a esta rama y el servidor los descargó de raw.githubusercontent.com con md5. Después se quitaron del árbol del repositorio (siguen en el historial, commit 48a180f).

## Cuarta ronda (2026-11-05, móvil)

Copias previas en el servidor: `hm-boceto-fix.css/.js.bak-20261105-104300`.

| Punto | Cambio |
|---|---|
| Barra «Pedir orçamento · Ligar» | No se veía: `.hm-cta { display: none }` (para escritorio) iba después del bloque móvil. Ahora va dentro de `@media (min-width: 768px)`. Comprobado con el HTML servido: visible a 390 px |
| Barra «Neste projeto» (Camolas) | El JS guardaba una referencia que quedaba obsoleta al repintar el diseño; ahora vuelve a buscarla (`isConnected`) |
| Opiniones (Home, Serviços, Sobre) | Mismo diseño que Sobre: sin imagen ni logotipo, cita a 26 px junto a la persona (separación de 20 px), citas largas recortadas (5 líneas en Home/Serviços, 4 en Sobre, que conserva «Ler mais»), sin altura mínima de pantalla. Dos nombres nítidos y solo el de la derecha esbatido; los nombres encajan a la izquierda (scroll-snap). Flechas anterior/siguiente debajo de los nombres |
| Home · servicios | Relleno 18/14 px en lugar de 16/16: el texto quedaba 3,6 px más cerca de la línea de arriba |
| Projetos · filtros | Flechas a la altura de «Disciplina» y «Setor», a la derecha; desplazan la fila y se atenúan en los extremos |
| Vídeos | Póster (imagen fija) en todos los vídeos en móvil, para que no haya cuadros negros mientras carga. Versiones ligeras nuevas: catálogo y site de Camolas, estacionario y vídeo de Alsil, sacos de Farinhas Firmos (de 0,6–18 MB a 51–171 KB), showreel 2020 de Sobre (20,2 → 3,6 MB, con audio). En la cinta de Design Web («Conteúdos», 12 vídeos), versiones mini de 12 s (60–210 KB). Precarga a 1 pantalla en lugar de 1,5 |

Medios en `uploads/hm-media/movil/` (y `movil/posters/`), transferidos por la rama y verificados con md5. Se borró `uploads/hm-tmp-camolas/` (temporal de la ronda 3).

## Quinta ronda (móvil)

- **Flechas** (opiniones de Home/Serviços/Sobre y filtros de Projetos): sin marco, trazo fino y largo (44 × 12 px, 1,2 px) al estilo de theconcretehome.com; zona táctil de 52 × 44 px; desactivada al 25 %; al pulsar pasa a magenta y se desplaza 4 px en su dirección. En filtros, centradas con «Disciplina» y «Setor» y alineadas a la derecha.
- **Vídeos enteros en 16:9, sin recorte**, manteniendo el efecto de entrada:
  - Home · showreel: se mantiene la ventana que se abre desde abajo y el zoom 1,18 → 1. El vídeo pasa a `contain` y su posición vertical acompaña la apertura (de abajo al centro, `--hm-oy` calculado en `reelFit()` con la misma fórmula del diseño). Al final, el vídeo queda centrado y «Showreel» con los botones justo debajo.
  - Camolas · Filme: misma idea (ventana centrada); «Adega Camolas · Vídeo» justo debajo.
  - Camolas · Anúncios (catálogo) y Design Web · Conteúdos: las cajas con vídeo pasan de 4:3 o 3:4 a 16:9.
  - João Bordeira y la cinta de Fotografia de Camolas ya eran 16:9: sin cambios.
- Publicado desde el commit 3767e42 (css 25a3fb08…, js 645843c2…). Copias en el servidor: `hm-boceto-fix.*.bak-20261105-110656`. `hm_dist_reset()` y WP Rocket vaciados; páginas servidas con `v=1793876816`.
- **Ajuste:** el fondo de la ventana del showreel (Home) y del Filme (Camolas) pasa de negro a gris claro `#E8ECED` (el de Manifesto, Projetos y Contacto). "Showreel", "Adega Camolas · Vídeo" y los botones pasan a tinta: "Pausa / Play" con borde fino y "Ver completo com som" en oscuro. Con la ventana abierta, el diseño ponía la cabecera en oscuro; ahora queda clara (clase `hm-reel-claro`, calculada en `reelFit()`). Publicado desde el commit 43e993d (css 4c503a9a…, js 4987f005…). Copias: `bak-20261105-111640`. Páginas servidas con `v=1793877400`.

## Favicon (todas las páginas)

- El favicon ya estaba en las páginas del diseño desde la tercera ronda (el mismo `favicon.png` que hortelamagenta.pt, md5 idéntico), pero apuntaba a `/favicon.ico`. Antes de existir ese archivo, WordPress redirigía `/favicon.ico` a su logo "W", así que el navegador seguía mostrando el icono guardado: la dirección era la misma.
- **Cambios:**
  - Nueva función `hm_favicon_tags()` en `hm-boceto.php`, con `?v=20261105b` para que el navegador vuelva a descargar el icono. La usan las páginas del diseño (`hm_fix_inject`) y, mediante `wp_head`, también las que pinta WordPress (artículos, categorías, autor y 404), siempre que no haya un Site Icon definido.
  - Se añade `assets/favicon.svg` (copia en `capa-fix/favicon.svg`): el mismo "hm" en vector, tomado del `safari-mask-icon.svg` original. Es oscuro en pestañas claras y `#E8ECED` en pestañas oscuras, donde el PNG original casi no se ve.
  - Etiquetas: `/favicon.ico?v=…` con `sizes="32x32"`, `favicon.svg`, `apple-touch-icon.png` y `mask-icon`.
- Comprobado en `/`, `/projetos/camolas/`, `/blog/`, `/category/branding/`, un artículo y un 404: las cuatro etiquetas están en todas. Copia de seguridad: `hm-boceto.php.bak-20261105-113138`.

## Sobre · «Também confiaram em nós»

- Los nombres se reducen para que destaquen menos. Antes eran 20 px en móvil y 20–28 px en ordenador (`clamp(20px, 1.7vw, 28px)`).
- **Ordenador y tableta:** `clamp(16px, 1.25vw, 18px)`, y la lista pasa bajo el rótulo cuando no tiene al menos 700 px al lado (`flex-basis: 700px`). Líneas: 3 a 768, 900, 1024, 1280, 1366 y 1440 px; 2 a 1100–1200 y 1920 px. Antes eran 4 a 1440 px.
- **Móvil:** 15 px, 6 líneas a 390 px (antes 8 líneas y 276 px de alto; ahora 147 px). Con los 14 nombres, 3 líneas a 390 px exigirían letra de unos 10 px.
- Publicado desde el commit c150eaf (css 8d349bd3…). Copia: `bak-20261105-114236`. `/sobre/` se sirve con `v=1793878957`.
- **Orden sin huecos:** `packClients()` (JS) mide los nombres y los reparte en el mínimo número de líneas posible, con líneas de longitud parecida. El reparto parte de colocar primero los nombres más largos y se mejora con intercambios. Se recalcula al cambiar el ancho y al cargar la tipografía. El orden se aplica con `order` y los saltos de línea con `margin-right` en el último nombre de cada línea, mediante una hoja `<style id="hm-pack">` (si el diseño vuelve a pintar la lista, no se pierde). El separador "·" pasa a `li::after` y se oculta al final de cada línea.
- **Resultado:** móvil a 390 px, 5 líneas llenas al 98–99 % (antes 6). Ordenador a 1440 px, 3 líneas al 76–78 %; a 1280 px, 3 al 80–82 %; a 1920 px, 2 al 78 %.
- Publicado desde el commit 273cff9 (css c21c922b…, js 6a5fbf44…). Copia: `bak-20261105-114745`. `/sobre/` se sirve con `v=1793879265`.

## Sexta ronda

- **Mano de "deslizar"** (móvil): Branding y Design Web · Trabalhos, y Camolas · Rótulos.
  - Icono de línea (mano con el dedo y flecha doble, trazo 1,3) dentro de un círculo translúcido de 68 px con desenfoque. Al entrar la galería en pantalla aparece, se desplaza de derecha a izquierda con el dedo "pulsado" y desaparece, tres veces seguidas.
  - En cuanto la persona desliza la galería ya no vuelve a salir.
  - En Trabalhos queda centrada al 58 % de alto; en Rótulos, sobre la primera imagen.
  - `hands()` en JS: quita las manos que quedan sueltas cuando el diseño vuelve a pintar la galería. Animación `@keyframes hm-hand`; con movimiento reducido, sin animación.
- **Camolas · cabecera** (PC y móvil): la foto pasa a `z-index: 0` y el velo degradado del diseño (`data-veil`) la cubre al bajar, igual que al fondo.
- **Camolas** (móvil): se oculta la barra flotante de secciones (`[data-pidx]`).
- **Sobre · Equipa:**
  - **PC:** el nombre grande de fondo pasa despacio en fila (cuatro copias, `translate` −25 % en bucle, unos 42 px/s).
  - **Móvil:** el mismo efecto como fondo por detrás del cargo, el nombre y la cita (`::before` del bloque de texto, 150 px, `#d6dce0`, unos 34 px/s).
  - La duración se calcula por nombre para que todos vayan a la misma velocidad. Con movimiento reducido, quieto.
- **Home · showreel** (móvil): vuelve a pantalla completa (vídeo recortado, fondo oscuro, cabecera oscura), como lo tenía el diseño. El Filme de Camolas sigue entero sobre gris, para comparar. Se retira `reelFit()`.
- Publicado desde el commit 45991c7 (css 730f121e…, js a9745a9d…). Copia: `bak-20261105-152647`. Páginas servidas con `v=1793892408`.

## Séptima ronda (móvil, 2026-11-06)

- **Home · segundo showreel:** justo debajo del showreel a pantalla completa, el mismo vídeo entero sobre gris `#E8ECED`. La ventana se abre al bajar, igual que el Filme de Camolas, y debajo quedan "Showreel", "Pausa / Play" y "Ver completo com som".
  - Se monta en la plantilla antes de que el diseño la pinte (`hm-entradilla-movil.html`) y la anima `reel2()`. Usa la versión ligera `showreel-clip-2025-movil.mp4` con su póster.
  - La barra "Pedir orçamento · Ligar" se oculta mientras está en pantalla.
- **Branding · Trabalhos:**
  - La galería de deslizar se queda quieta 35 % de pantalla (sección de 135svh con el bloque fijo) y encaja al llegar (`scroll-snap-type: y proximity` en la página, `scroll-snap-align: start`).
  - Debajo, una copia (`#trabalhos-galeria-scroll`, `data-hm-scroll`, creada en la plantilla) con la navegación original del diseño: avanza al bajar y se detiene con cada proyecto centrado. También encaja al llegar.
  - La copia lleva los mismos ajustes de tamaño que la de deslizar (texto de 30 px, nombre de proyecto completo, botón "Ver projeto") y conserva las animaciones del diseño.
  - Design Web sin cambios.
- **Camolas · Identidade visual:** los botones 01–04 toman las medidas de la lista de servicios de la home: rejilla de 44 px + 1fr, separación de 20 px, relleno de 18/14 px, número de 16 px en `#6E6A63`, texto de 28 px y peso 200, líneas `rgba(28,27,35,.12)` y filas de 61 px.
- **Camolas · Rótulos:** flechas finas, las mismas de las opiniones, a la derecha en la línea de "Design de rótulos de vinho →", además de la mano. Avanzan una etiqueta y se atenúan en los extremos.
- **Camolas · Anúncios:** el diseño abría las imágenes cuando aún estaban por debajo de la pantalla (`rootMargin 10%`). Ahora se quedan cerradas hasta que llegan al 55 % de la altura de la pantalla, la altura de los ojos, y entonces se abren desde un lado al azar con el zoom del diseño (`lateAds()`).
- Publicado desde el commit 6d633df (css f3e35a2c…, js fc7c19b5…, script temprano 8a18193c…). Copias: `bak-20261106-090913`. Páginas servidas con `v=1793956154`. Comprobado también con el HTML servido.
