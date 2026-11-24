# Hortelã Magenta · web en hortelamagenta.inboost.marketing

Proyecto de Laura (Inboost) para el cliente Hortelã Magenta (agencia de diseño de Moita, Portugal; textos en portugués de Portugal).
El `CLAUDE.md` de la raíz es de otro proyecto (optimización de URL de Inboost): su flujo no aplica aquí.

## Cómo está montado

- **Sitio:** https://hortelamagenta.inboost.marketing. Tiene WordPress 7.1, PHP 8.5, Divi 5.7.4 con tema Divi Child y WP Rocket.
- **Conector:** **Novamira - Hortel Magenta** (`mcp__Novamira_-_Hortel_Magenta__*`). Casi todo se hace con `novamira/execute-php`.
- **Lo que se sirve no es Divi.** Las 10 URL públicas sirven el **boceto**: paquetes HTML exportados de Claude Design.
  - Están en `wp-content/themes/divi-child/hm-paginas/*.html`.
  - `?divi` enseña la página de Divi (ID 131-139). Es de una versión antigua del diseño y no hay que tocarla: se rehará en Divi al final.
- **`hm-boceto.php`** (tema hijo, cargado desde `functions.php`) enruta las URL a los paquetes:
  - `/`, `/servicos/`, `/servicos/branding/`, `/servicos/design-web/`, `/projetos/`, `/projetos/camolas/`, `/sobre/`, `/blog/`, `/blog/quanto-custa-um-site/`, `/contacto/`.
  - Al servir, `hm_fix_inject()` añade la **capa de correcciones** antes de `</head>`.
- **`hm-boceto-dist.php`** desempaqueta cada paquete en `hm-paginas/dist/<pagina>.html`, con los recursos en `dist/a/<sha1[:16]>.<ext>`.
  - Copia los medios remotos (hortelamagenta.pt, nostalgia.hortelamagenta.pt…) a `uploads/hm-media/` como WebP con calidad 74 y un máximo de 1900 px de ancho, con `hm_media_mirror()`.
  - `hm_dist_reset()` borra los dist (se regeneran en la siguiente visita) y vacía WP Rocket.
- **Memoria en el sitio:** Novamira guarda una nota en la memoria ID 195 (`novamira/memory-get`).

## Capa de correcciones (lo que cambiamos nosotros)

- **Archivos:**
  - En el sitio: `wp-content/themes/divi-child/assets/hm-boceto-fix.css` y `hm-boceto-fix.js`.
  - La fuente está en **`hortela-magenta/capa-fix/`**, y hay que mantener las dos versiones iguales.
  - Sobreviven a kits nuevos del diseño.
- **Subir:** `python3 -I hortela-magenta/tools/hm_push.py hortela-magenta/capa-fix` (o, si pesa mucho, un parche old → new con verificación de md5, como en la 8.ª ronda). Imprime el `code` para `novamira/execute-php`, que sube los dos archivos, verifica el md5 y vacía las cachés.
- **Contenido actual (ya publicado y aprobado):**
  - **Menú móvil `[data-mobile]`:**
    - Marca la página actual con `data-hm-cur`.
    - Serviços y Projetos salen plegados, con botón «+» (`.hm-sub-btn` / `.hm-sub`).
  - **Textos laterales de `[data-marca]`/`[data-device]`** (Branding «Suportes», Design Web «Responsivo»): visibles en móvil como fondo detrás de las piezas.
  - **Paneles `[data-step-v]`** («Ponto de partida» en Branding, «Processo» en Design Web): transición suave al cambiar.
  - **Artículo:** la firma va pegada a la entradilla.
- **Correcciones dentro de los paquetes** (hay que repetirlas si llega un kit nuevo sin ellas):
  - En el CSS móvil, `[data-header] > div:first-child` → `div:first-of-type` (3 veces por página).
  - Textos, estructura e imágenes de la 8.ª ronda: `paquetes/2026-11-23-*.json`. Se prueban en local con `paquetes/aplicar.py` y se aplican en el servidor con `paquetes/aplicar.php`.

## Probar en local (el contenedor NO llega al sitio: proxy 403)

1. En `novamira/execute-php`, pega `hortela-magenta/tools/hm_pull.php` sin la línea `<?php`.
   - Haz dos llamadas, con `$parte='html'` y después con `$parte='assets'`.
   - La respuesta se guarda en un archivo de tool-results.
2. Desempaqueta cada respuesta con `python3 -I tools/unpack.py <archivo> <dir>`, usando el mismo `<dir>` para las dos.
3. Ejecuta las pruebas:
   - `node hortela-magenta/tools/hm_serve.js <dir> reg`: las 10 páginas en móvil y PC (errores, desborde, capa cargada).
   - `… shot /servicos/branding/ out.png --at='#identidade:0'`: captura de un bloque.
   - `… run <ruta> guion.js`: interacciones con Playwright, como `page.tap`.
   - Siempre se usa la capa LOCAL de `hortela-magenta/capa-fix/` (o la carpeta de la variable `FIX`). Las imágenes de hm-media no se traen y salen grises.

## Lecciones aprendidas (evitan horas)

- **Transferencias:** para subir o bajar archivos grandes, usa gzip + base64 + md5 dentro de `execute-php`. Los resultados de más de ~60 KB se guardan en un archivo: léelo con Python o jq.
- **El menú móvil se vuelve a pintar al abrirse** (runtime React del diseño).
  - Todo cambio de DOM debe ser idempotente.
  - Engancha cada listener una sola vez, con una marca en el elemento.
  - Busca los objetivos por id en el momento del evento.
- **`hm-movil.css` usa `!important`:**
  - Para ganarle, usa más especificidad (`html body …`) y `!important`.
  - Las animaciones WAAPI no pueden con `!important`. Usa estilo en línea con `setProperty(..., 'important')` más transiciones CSS (las transiciones sí ganan a `!important`).
  - En Safari no animes con variables CSS: usa valores en línea.
- **`hm-fx-servico.js` / `hm-fx-projeto.js` reescriben estilos en línea en cada frame** (opacidad, transform…). Para controlarlos, usa CSS `!important` y, si hace falta, una variable CSS que fije tu propio JS.
- **Breakpoints:** el móvil va hasta **767 px**, y el menú de hamburguesa también sale en tablet.
- **Reducir movimiento:** el diseño respeta `prefers-reduced-motion` y quita las animaciones. Con «Reducir movimiento» activado en el iPhone, todo se ve sin efectos; es a propósito.
- **Medios remotos:** `hm_media_refs()` solo detecta URL completas y `CONST + 'literal'`.
  - El dist solo pasa a local los medios de una página si están copiados **todos** los de esa página.
- **Atributos útiles del diseño:**

| Atributo | Qué es |
|---|---|
| `[data-header]` | Cabecera |
| `[data-mobile]` | Menú móvil |
| `[data-step-v]` | Paneles |
| `[data-lb]`, `[data-drag]`, `[data-track]` | Carruseles de fotos con lightbox |
| `[data-lp]` | Galería horizontal fijada |
| `[data-ops]` | Opiniones |
| `#filtros` | Filtros de Projetos |
| `[data-faq-side]` | Columna lateral de las FAQ |
| `data-screen-label` | Nombre de cada bloque, p. ej. «07 Processo» |

- **Reglas de diseño (vinculantes):** `diseno/REGLAS-DEL-PROYECTO.md`. También están `diseno/README-handoff.md` (entrega para Divi) y `diseno/hm-movil.css` (CSS móvil del diseño).
  - Texto nunca de menos de 16 px.
  - Rosa `#D82E87` solo como acento.
  - Fuente Spartan con pesos de 100 a 400.

## Hallazgos ya hechos sobre la lista pendiente

- **Hortelanices (Sobre)** no carga en PC ni en móvil.
  - Las fotos se construyen en JS como `HB + p`: `const HB='https://nostalgia.hortelamagenta.pt/old/wp-content/uploads/'` y arrays `['2016/12/x.jpg', w, h, 'texto']`.
  - Por eso **no se copiaron** a hm-media y se piden a nostalgia.hortelamagenta.pt.
  - Hay que comprobar desde el servidor si responden (`wp_remote_head`).
  - Después, ampliar `hm_media_refs()` para recoger también rutas relativas `AAAA/MM/*.jpg|png` cuando la constante base se use con variable. A continuación, `hm_media_mirror()` y `hm_dist_reset()`.
  - Si nostalgia no responde, buscar las imágenes en otro sitio o pedírselas a Laura.

## Cambios pedidos por Laura (5-nov-2026), ya hechos (ver `2026-11-05-revision-movil.md`; la 8.ª ronda, en `2026-11-23-octava-ronda.md`)

- **Global:**
  - El logo cambia entre la pantalla normal y el menú abierto: tiene que ser igual (tamaño y posición).
  - Opiniones abajo (home, sobre y cualquier página con opiniones): no se entiende que es un carrusel.
    - Que se vean 2 y media.
    - La media tarjeta, cortada y algo borrosa, como cuando haces scroll después.
  - FAQ más pequeñas en todas las páginas: ahora tienen el mismo tamaño que el título.
- **Home:**
  - El vídeo del showreel tarda en cargar.
  - Al hacer scroll, «Showreel» y «Veja o showreel» se montan uno encima del otro.
  - Títulos de servicios más pequeños: que quepan en una línea y no sean más grandes que el título principal.
- **Branding y Design Web, Proyectos:**
  - Carrusel deslizable con el dedo en vez de scroll.
  - Se corta el primer texto.
  - Botón o enlace claro para ir al proyecto (quitar el «+», que no es intuitivo).
  - Los nombres de los proyectos se cortan: más pequeños.
- **Design Web, Âmbito:** el texto del listado queda muy pegado a las líneas superior e inferior.
- **Projetos:**
  - La galería no se mueve: tiene que moverse como en PC, sin dejar huecos, para que las imágenes se vean más grandes.
  - En el índice, lo que se hizo en cada proyecto, en minúsculas.
- **Camolas:**
  - Título «Camolas» y entradilla del mismo tamaño que en Branding. «Branding, Design Gráfico, Vídeo, Fotografia, Digital», más pequeño que la entradilla.
  - Bloque de identidad visual: en móvil no se adapta. Probar las cortinas en horizontal en vez de en vertical, para que se vean las imágenes enteras.
  - «Rótulos e packaging»: que se pase deslizando con el dedo (carrusel), no con scroll.
  - «O site»: imágenes borrosas. Rehacerlas a partir de la web original o subirlas con más calidad (revisar la conversión WebP de 1900 px y q74 de `hm_media_mirror`).
  - «Filme»: el vídeo carga a golpes. Revisar si el MP4 tiene el moov al final (sin faststart), el tamaño y `preload`.
  - Volver a poner la barra inferior de navegación rápida entre secciones (en móvil se quitó), más pequeña para que quepan varias palabras.
  - «Mais projetos»: una sola columna y menos altos.
- **Sobre:** Hortelanices no carga las imágenes (**PC y móvil**). Opiniones: ver Global.
- **Blog:** barra inferior de categorías más pequeña, para que quepan varias palabras.
- **Artículo:** título y entradilla del mismo tamaño que en Branding (y que en Camolas).
- **PC:** en el menú de escritorio, un poco más pequeños el logo, el texto y el desplegable.

Forma de trabajar con Laura: en español, directo, avisos cortos de avance. Antes de publicar, probar en local (móvil y PC, 0 errores, sin desborde). Después de publicar, comprobar en vivo con `wp_remote_get` y dar a Laura la lista de lo hecho.

## Fase 2 (2026-11-24): web completa

Informe: `2026-11-24-fase2-informe.md`. Código: `fase2/`.

- **36 URL servidas + 404.** Además de las 10 de la fase 1: 12 fichas de proyecto, 5 servicios (Gráfico + Editorial, Campanhas & Redes Sociais, Fotografia & Vídeo, Avença 360°, Coaching de Marcas), las 5 landings de especialidad, Política de Privacidade, Política de Cookies, Mapa do site, Obrigado y 404.
- **Mapa de URL:** `hm-rutas.php` en el tema hijo (fuente: `fase2/servidor/hm-rutas.php`). Páginas, redirecciones 301 y prefijos.
  - Barra final canónica por URL, como en la web actual: sin barra (`/projetos/camolas`), salvo las landings (`/design-rotulos-vinho/`). La otra variante redirige con 301.
  - Versión inglesa `/en/...` → equivalente en portugués (301). Rutas nativas de WordPress (entradas, adjuntos, feeds) → 404 del diseño; categorías → /blog; autor → /sobre.
  - `/media/...` de Kirby → copia local en hm-media (301), para enlaces e imágenes indexadas.
- **`hm-boceto.php` (servidor):** usa el mapa, sirve `hm-paginas/404.html` con estado 404, genera `/sitemap.xml` (sitemaps de WordPress desactivados), `?divi` y `?paquete` solo con sesión, y `X-Robots-Tag: noindex` en cualquier dominio que no sea hortelamagenta.pt.
- **Formulario:** `hm-formulario.php`, `POST /wp-json/hm/v1/contacto`. Guarda cada pedido en «Pedidos de contacto» (tipo `hm_pedido`) y envía un email a `hm_form_to` (por omisión, el email de administración). Después lleva a `/obrigado`. Las páginas de servicio enlazan `/contacto?servico=…` y el formulario preselecciona el servicio.
- **Generador** (`fase2/gerador/`, Python): monta los modelos (template) de las páginas nuevas a partir de los existentes, con los bloques del diseño (Camolas para proyectos, Branding para servicios, landings, 404 y obrigado, Artigo para legales y mapa) y aplica a todas las páginas los cambios comunes (`comum.py`: enlaces internos sin barra, menús, pie) y de contenido (`extras.py`).
  - Datos: `dados_projetos.py`, `dados_servicos.py`, `dados_landings.py`, `dados_aux.py`.
  - Uso: traer los modelos originales (`template` de cada paquete) y `media-info.json`; `python3 gerar.py <modelos> media-info.json oldproj.json <salida>`; probar con `dist_local.py` + Chromium.
  - **Si llega un kit nuevo de Claude Design:** volver a ejecutar el generador sobre los modelos nuevos (las páginas existentes reciben otra vez `comum.py` y `extras.py`).
- **Desplegar:** subir los modelos a `fase2/modelos/` (con `md5.json`), hacer push y ejecutar `fase2/servidor/construir.php` en `novamira/execute-php`. El script los descarga de raw.githubusercontent.com, compone cada paquete solo con los recursos que usa, deja copia en `hm-paginas-bak/<fecha>-antes-<etiqueta>/` y vacía dist y WP Rocket. Los PHP se instalan con `fase2/servidor/implantar.php`, que hace `php -l` antes de sustituir.
- **Medios:** los 266 de las fichas y landings ya están en `uploads/hm-media/`, con `fase2/servidor/espelhar.php`.
