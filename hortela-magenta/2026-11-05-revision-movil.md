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
