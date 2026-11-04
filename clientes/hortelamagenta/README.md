# Hortelã Magenta (hortelamagenta.inboost.marketing): rendimiento del boceto

Fecha: 4 de noviembre de 2026. Conector: Novamira Hortel Magenta.

## Punto de partida (PageSpeed móvil de la portada: 49)

`hm-boceto.php` sirve en las 10 rutas los HTML exportados de Claude Design (`hm-paginas/*.html`). Esos archivos son **paquetes autoextraíbles**:

- Pesan unos 0,5 MB y llevan React, el runtime DC, las fuentes y algunas imágenes en base64.
- Al cargar, el navegador los descomprime en URL `blob:`, reemplaza el documento entero y React pinta la página. Hasta entonces no se ve nada.
- Llevaban `DONOTCACHEPAGE`, así que WP Rocket no los cacheaba: unos 750 ms de respuesta del servidor.
- Las imágenes y los vídeos se enlazaban desde hortelamagenta.pt (Kirby) y nostalgia.hortelamagenta.pt en JPG de 1900 px y sin caché. Además, se romperán cuando el dominio cambie de servidor.

Esto explica las auditorías: FCP 2,9 s, LCP 4,5 s, TBT 1.970 ms, los scripts `blob:`, React, los 49,6 KiB de `@font-face` (fuentes en data: URI) y la falta de caché de 1,2 MB de imágenes.

## Cambio aplicado (sin cambio visual)

- **`hm-boceto-dist.php`** (nuevo, en el tema hijo) desempaqueta cada paquete una vez en el servidor:
  - `hm-paginas/dist/<pagina>.html`: el mismo documento que montaba el cargador.
  - `hm-paginas/dist/a/<hash>.<ext>`: React, runtime, fuentes e imágenes como archivos estáticos, compartidos entre páginas y con `Cache-Control: max-age=31536000, immutable` (`.htaccess` en la carpeta).
  - Inyecta `window.__resources` para que React salga del servidor y no de unpkg, y para que el runtime no vuelva a pedir la página.
  - Precarga React, ReactDOM y la fuente latin.
- **Medios:** `hm_media_mirror()` copia a `uploads/hm-media/<host>/<ruta>` las 99 imágenes y vídeos remotos:
  - Imágenes JPG/PNG pasan a WebP con calidad 74 (6,3 MB en total; p. ej. 309 KB → 115 KB).
  - Los vídeos se copian tal cual (116 MB).
  - El HTML y el JS (`const IMG = …` + `IMG + 'ruta'`) apuntan a las copias.
  - `og:image` sigue absoluta a hortelamagenta.pt.
  - Al logo de ADREPES se le añaden `width` y `height`.
- **`hm-boceto.php`:**
  - Sirve la versión dist y quita `DONOTCACHEPAGE`: WP Rocket la cachea y mantiene `DONOTROCKETOPTIMIZE` para no tocar el JS.
  - Marca `is_404 = false` para que también se cachee /blog/quanto-custa-um-site/.
  - `?paquete` sirve el paquete original para comparar; `?divi` sigue igual.
  - Copia de seguridad: `hm-boceto.php.bak-20261104-104027`.
- **Si se vuelve a exportar un HTML** a `hm-paginas/`, su versión dist se regenera sola y un `init` vacía la caché de WP Rocket en la primera visita sin caché (con sesión, admin o cron). Si cambian las imágenes de los paquetes, hay que ejecutar `wp eval 'echo wp_json_encode(hm_media_mirror(600));'`.

## Verificación

- Las 10 rutas responden 200 con la versión dist.
- **Respuesta del servidor:** de 640-805 ms a 23-44 ms desde la caché de WP Rocket.
- En las 10 páginas, todas las rutas locales existen: 211 imágenes del JS y las del HTML, con WebP y caché de 1 año.
- No queda ningún medio remoto fuera de `<meta>`.
- **Medición local** con `perf.js` (móvil 412 px, CPU 4x, 150 ms RTT y 1,6 Mbps; sin el TTFB real):

| | FCP | LCP | TBT | Transferido |
|---|---|---|---|---|
| Paquete (con imágenes simuladas) | 1,8-2,9 s | 2,7-4,9 s | 600-1.440 ms | 1.064 KB |
| Dist (imágenes WebP reales) | 1,65-2,1 s | 1,65-2,1 s | 0 ms | 631 KB |

- La captura móvil de la dist es idéntica al paquete.

## v3 (tras PageSpeed 84: FCP 1,6 s · LCP 2,0 s · TBT 580 ms · CLS 0)

- **Scripts:** el runtime y los JS propios del paquete (carga diferida, efectos, lightbox) van con `defer`. Un `<style>x-dc{display:none}</style>` en el `<head>` sustituye la ocultación que antes hacía el runtime.
- **Preconnects:** se quitan los de Google Fonts, porque las fuentes son locales.
- **Comprobación:** inicio, branding, camolas, design-web y sobre, en móvil (390 px) y escritorio (1.440 px). Sin errores de JS ni 404 y sin desborde horizontal; el runtime, `HMPerf`, los efectos y el lightbox se cargan. Las 10 rutas están otra vez en caché (unos 25 ms).
- **Copias de seguridad:** `hm-boceto-dist.php.bak-*` en el tema.

## Al reexportar desde Claude Design (adaptación móvil en curso)

- Basta con sustituir el HTML en `hm-paginas/` con el mismo nombre: la versión dist y la caché se regeneran solas. Todo lo de este archivo se vuelve a aplicar en cada exportación.
- Si el diseño usa imágenes nuevas de hortelamagenta.pt, se quedan remotas hasta ejecutar `wp eval 'echo wp_json_encode(hm_media_mirror(600));'`.
- Una ruta nueva se añade a `$hm_paginas` en `hm-boceto.php`.
- Lo que queda depende del propio diseño; corregirlo en la fuente, porque la exportación lo sobrescribe:
  - **TBT y reflow forzado:** vienen de la lógica del componente (React pinta todo; el cursor y los efectos de scroll leen medidas del layout).
  - **Contraste:** `span.sc-interp` son las palabras del texto que se ilumina con el scroll, que empiezan en gris claro.
  - **Agentic Browsing:** `article#op-panel-1` lleva un `role` que `<article>` no admite (usar `<div role="tabpanel">`).
  - **Animaciones:** hay 10 animaciones no compuestas (propiedades distintas de transform u opacity).
  - **Cabecera móvil:** «Pedir orçamento» se corta a 390-412 px.

## Pendiente / siguiente paso

- **Renderizado:** React sigue pintando toda la página en el navegador, con unos 0,8 s de CPU (a 4x) antes de la primera pintura. Para bajar más haría falta HTML prerenderizado (la versión Divi o una instantánea SSR).
- **Tamaño de las imágenes:** son de 1900 px sin `srcset`; en móvil sobran. Siguiente mejora: variantes de 800 px y `srcset` en las plantillas.
- **Cabecera móvil:** a 412 px, el botón «Pedir orçamento» se corta por la derecha (también en el paquete original).
- **Indexación:** `blog_public=1` en el subdominio de trabajo; el canonical apunta a hortelamagenta.pt.
