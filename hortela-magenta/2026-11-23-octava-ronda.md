# Hortelã Magenta · 8.ª ronda: cambios aprobados por Gonçalo y Vítor (2026-11-23)

Petición: tarea de ClickUp «Hortela Magenta - Cambios web 23 nov» (mensaje de Dani en el chat del cliente), con las indicaciones de Laura: espaciado de las cifras y capturas enteras de adegacamolas.pt para «Digital · O site».

Sitio: https://hortelamagenta.inboost.marketing. Las páginas salen de los paquetes de Claude Design (`hm-paginas/*.html`), más la capa propia (`assets/hm-boceto-fix.css/.js`, fuente en `capa-fix/`).

## Cómo se ha hecho

- **Textos y estructura:** se cambian dentro de los paquetes, en su template. Las ediciones están en `paquetes/*.json` y son reaplicables si llega un kit nuevo.
  - `textos.json`: 20 ediciones.
  - `medios.json`: 13 ediciones.
  - `capturas.json`: 9 ediciones.
  - En local se aplican al dist con `paquetes/aplicar.py`. En el servidor, con `paquetes/aplicar.php`, que compara cuántas veces aparece cada texto, recodifica con `JSON_HEX_TAG` y comprueba el resultado antes de escribirlo.
  - Copias en el servidor: `hm-paginas-bak/2026-11-23-antes-8a-ronda/` (las 10 páginas) y `hm-paginas-bak/2026-11-23-antes-8a-ronda-capturas/` (camolas, servicos, design-web).
- **Estilos y comportamiento:** en la capa (`capa-fix/`). Se sube con un parche (old → new) y se verifica el md5.
  - Publicada: css `cecd3999…`, js `5f822ef2…`, servida con `v=1795436228`.
  - Copias: `hm-boceto-fix.*.bak-20261123-*`.

## Hecho

| Página | Cambio |
|---|---|
| Home y Sobre · cifras 2007 · 572 · 2893 | La Spartan no tiene cifras tabulares y el contador daba a cada columna el ancho del «0». Ahora cada columna mide lo que avanza su cifra (CSS `:has(> [data-dg="N"])`, en em). Recorta solo en vertical (`overflow-y: clip`) |
| Tipografía general (768–1919 px) | Los títulos en vw van del 85 % a 1280 px al 100 % a 1920 px: `calc(1,3·c·vw − 5,76·c px)`, con el máximo del diseño, generado para cada clamp. El texto corrido pasa de 16 px (1280) a 18 px (1920) con interlineado 1,6. Los títulos fijos de 28 px van de 24 a 28 px. A partir de 1920 px (iMac) no cambia nada; el móvil tampoco |
| Home · cabecera | «Moita, Portugal — desde 2007» → «Desde 2007» |
| Home · Serviços | 6.º servicio «Avenças mensais», solo en la lista (no en el menú). Texto provisional a partir de las respuestas de Gonçalo (doc de ClickUp «Documento»). Enlaza a /contacto/ con «Falar sobre uma avença». **Hay que revisarlo con el Word «Avença Mensal 360» cuando llegue** |
| Home · Sobre a Hortelã Magenta | «Somos uma equipa criativa…»: `clamp(22px,1,68vw,32px)` y 1,2 → `clamp(20px,1,4vw,26px)` y 1,45 |
| Todas · bloque de contacto | «Estúdio» → «Sede» |
| Todas · pie | «Política de Privacidade», «Livro de Reclamações» y «© 2026» pasan de 16 a 14 px (excepción pedida a la regla de 16 px) |
| Design Web | Cabecera: «Desde 2007». Fuera los bloques `#atividade` («O que o site deve explicar», puntos 01–04) y `#processo` («Como organizamos o projeto»). Se mantiene «O que determina o âmbito» |
| Design Web · Trabalhos | El fondo pasa del rótulo `garrafeira_01` al site de Farinhas Firmos (`farinhafirmos_site_06`). La tarjeta 3, Alinea, pasa a Palmela Experiences: montaje de PC y móvil con capturas propias (sin la cinta de «Black Friday»), etiquetas «Website › Enoturismo», texto provisional y enlace a palmelaexperiences.pt. También se cambian los datos de la galería |
| Branding · cabecera | Fuera «Moita, Portugal — desde 2007» |
| Serviços · Design Web | Captura de Camolas → recorte 4:5 de la captura nueva de adegacamolas.pt en móvil |
| Serviços · Campanhas & Redes Sociais | Los carteles de Croma pasan a sus publicaciones en redes (`croma_rs_01`). El stand de Stockfer/Alsil pasa a las publicaciones de Consulai (`consulai_redes_sociais_02`), con su pie. Las de Farinhas Firmos (`redessociais_02`) ya eran publicaciones reales y se quedan |
| Serviços · Fotografia & Vídeo | Alinea: de 950 px a la versión más grande de hortelamagenta.pt (1023 px), en WebP q90 en lugar de q74 |
| Camolas · Rótulos e packaging | Se añaden 5 trabajos (06–10): Cobaia (caja), Grande Escolha (rótulo), Garrafeira (caja), Monocasta Syrah (rótulo) y Moscatel de Setúbal |
| Camolas · Anúncios e redes sociais | Se mantiene la cuadrícula. Roll-up → «25 anos», catálogo → «Cobaia» (imagen de campaña), bases para copo → «Prémio». Textos provisionales |
| Camolas · O site | Capturas de **página entera** de adegacamolas.pt (Vinhos, Região e Vinhas, Experiências) a 2x, para PC (1440 px) y móvil (390 px), en tramos WebP de menos de 4.000 px (`uploads/hm-media/site-camolas/`). `[data-hm-shot="pc"\|"m"]`. Alto de la sección: 1000vh en PC y 1400vh en móvil. JS 17: los tramos pasan de lazy a eager a pantalla y media |
| Sobre | Debajo de «Transparência», fuera la frase «Acreditamos genuinamente…». Showreels: pestañas «2025 · 2020» junto al botón del sonido (JS 16, clic delegado). PC: vídeos completos. Móvil: versiones ligeras; la de 2025 no tiene sonido, así que al activarlo pasa a la completa |
| Contacto · selector | + «Avenças mensais» y «Coaching de Marcas» |

## Medios

- **Capturas:** adegacamolas.pt (cookie `age_gate=1`, Locomotive Scroll desactivado) y palmelaexperiences.pt.
  - Hechas en local con el servidor como pasarela.
  - Transferidas por la rama (commits `e5d222b` y `23e4c3d`) y verificadas con md5.
  - JPEG a 1x para Laura en el scratchpad de la sesión.
- **Imágenes nuevas de hortelamagenta.pt:** copiadas con `hm_media_mirror()`, 12 en total.
- **Sin usar en el servidor:** `site-camolas/camolas-site-regiao-fundo.webp` (fondo descartado porque su titular chocaba con el texto de la galería).

## Verificación

- **Local, sobre las páginas regeneradas por el servidor:** 10 páginas en móvil y PC (20 pruebas), con 0 errores, sin desborde y con la capa cargada.
- **En vivo:**
  - Las 10 URL responden 200 con `v=1795436228`.
  - El md5 de la capa servida es igual al local.
  - Los tramos, el montaje y las imágenes nuevas responden 200 `image/webp`.

## Pendiente (material o decisión de Dani/Gonçalo)

- **Words de Gonçalo:** «Avença Mensal 360» y «Coaching de Marcas». No están en ClickUp ni en la demo. Los textos de la avença y de los anuncios de Camolas son provisionales.
- **Clientes con avença:** confirmar si se pueden nombrar en la Home.
- **Foto de Alinea en mayor resolución:** la web solo tiene 1023 px.
- **Más anuncios y publicaciones reales de Camolas:** en hortelamagenta.pt solo están el banner de 25 anos, el del premio y los de Cobaia.
- **Decisiones abiertas de Dani, sin tocar en esta ronda:** vídeo de la Home en móvil, formato de los proyectos de Branding en móvil, y los campos del formulario y la ubicación de la sede.

## Ajustes de Laura (2026-11-23, tarde)

| Punto | Causa | Cambio |
|---|---|---|
| Camolas · Anúncios: franjas crema | 25 anos, Prémio y Frase usaban `object-fit: contain` | Todas las imágenes del bloque con `cover` (capa) |
| Camolas · Anúncios: el 05 pegado abajo | El diseño daba al último `min-height: 31vh` y `align-items: flex-end` | En PC, `62vh` y centrado como los demás (capa) |
| Home · cifras: margen desigual | Arriba `clamp(12px,2vh,20px)` y abajo el gap de la columna. Medido: 11 frente a 28 px en móvil y 16 frente a 36 en PC | `padding-top: calc(clamp(20px,3vh,36px) + 10px)`. Resultado: 28/28 en móvil y 35/36 en PC (capa, solo `#sobre` de la Home) |
| Design Web · transición de la cabecera | Al bajar, el velo (`data-veil`) pinta la cabecera de `#e8eced`, el color del bloque «Atividade» que se quitó. El bloque siguiente, «Responsivo», es `#f6f7f8` | El velo usa el color del bloque siguiente cuando este es `#responsivo` (capa). Igual que en Branding (velo y «Suportes» del mismo color) |
| Design Web · fondo de «Trabalhos de criação web» | `farinhafirmos_site_06` era demasiado claro para tanto texto | `camolas_site_04.jpg` (2400 px, fondo casi negro, el site a la derecha) |
| Serviços · Web design (Camolas) | El recorte 4:5 de 780 px se ampliaba a 724 px CSS de ancho (borroso) y no seguía el estilo de las otras | Montaje propio de 1450×1812 con el estilo de `farinhafirmos_site_05`: PC y móvil de adegacamolas.pt/vinhos sobre fondo oscuro con bloque arena, a partir de las capturas a 2x (`site-camolas/camolas-site-mockup-4x5.webp`) |
| Serviços · Fotografia: Alinea borrosa | Las fotos de Alinea en hortelamagenta.pt son como mucho de 1023×682. La `foto_03` tiene márgenes blancos (la foto útil es de unos 490×680). El hueco mide 724 px CSS | Pasa a una foto de producto nítida: Queijaria da São (`queijariadasao_foto_06`, 1900 px, WebP q88), con su pie. Si se quiere Alinea, hace falta el original |

- **Ediciones de paquetes:** `paquetes/2026-11-23-ajustes.json` (4).
- **Copias:** `hm-paginas-bak/2026-11-23-antes-8a-ronda-ajustes/`.
- **Capa:** css `d1360f50…`, servida con `v=1795439334`.
- **Pruebas en local:** 20 de 20 sin errores ni desborde.
- **En vivo:** páginas 200, md5 de la capa igual y medios 200.
- **Serviços · Web design (después):** el borde blanco de las pantallas se confundía con la web. El montaje pasa a `camolas-site-mockup-4x5-v2.webp`, con monitor y móvil negros (bisel, cámara e isla). La versión 1 se borró del servidor.
- **Serviços · Web design (v3):** el resto de la página sale pegado por debajo del monitor y del móvil, sin hueco, como en las otras muestras (`camolas-site-mockup-4x5-v3.webp`). La v2 se borró del servidor.

## Words de Gonçalo (2026-11-24)

Laura pasa «Avença Mensal 360» y «Coaching de Marcas». Son textos completos de página de servicio (URL, title, meta, H1, apartados, CTA y FAQ) y están en el chat de la sesión, no en el repo (es público y son borradores para revisión).
- **Home · «Avenças mensais»:** el texto provisional se sustituye por uno sacado del Word: «O departamento de comunicação da sua empresa, só que do lado de fora. Para PME e marcas com atividade nacional e internacional: marca, imagem gráfica, textos, web, fotografia, vídeo e redes sociais, com reuniões regulares e um valor mensal fixo.»
  - El enlace pasa a «Marcar conversa» (el botón que propone el Word; «Quero um departamento de comunicação» ocupaba dos líneas en móvil) y sigue llevando a /contacto/.
  - `paquetes/2026-11-24-avenca.json`. Copia: `hm-paginas-bak/2026-11-24-antes-avenca/`.
- **Para la fase siguiente:** las dos páginas de servicio. URL propuestas: `/servicos/avenca-comunicacao-360/` y `/servicos/coaching-de-marcas/`. Cuando existan, el enlace de la Home y las opciones del selector de Contacto deberán apuntar a ellas.
- **Pendiente de Dani tras recibir los Words:** foto original de Alinea, más anuncios reales de Camolas y confirmar si se pueden nombrar los clientes con avença.

## «Avenças mensais» con los demás servicios (2026-11-24)

| Dónde | Cambio |
|---|---|
| Menú de PC (desplegable de Serviços, las 10 páginas) | 6.º elemento en la lista JS `services`, con la descripción corta «O departamento de comunicação da sua empresa.» y la imagen del estacionario de Camolas. Enlaza a `/servicos/#avencas-mensais` |
| Menú de PC · enlaces | Gráfico + Editorial, Campanhas y Fotografia llevaban a la web antigua (`https://hortelamagenta.pt/servicos`, fallo del diseño). Ahora van a su sección de /servicos/ |
| Menú móvil y pie (las 10 páginas) | + «Avenças mensais» → `/servicos/#avencas-mensais` |
| Home · lista de servicios | Avenças sale de la misma lista que los demás (fuera el `concat` provisional). Enlace «Ver serviços» → `/servicos/#avencas-mensais` |
| Serviços | La frase de la cabecera incluye «Avenças mensais». En «Acceso rápido», 06. Contadores «0N / 06». Nueva sección `#avencas-mensais` («06 / 06»), con texto del Word (párrafo, 5 puntos y CTA «Marcar conversa →» a /contacto/) e imágenes de clientes de larga duración (estacionario de Camolas, banner de Consulai y display de Alsil). Va con fondo `#f6f7f8`, alternando con Fotografia |

- **Ediciones de paquetes:** `paquetes/2026-11-24-avencas-menu.json` (55).
- **Copias:** `hm-paginas-bak/2026-11-24-antes-avencas-menu/`.
- **Imágenes nuevas copiadas:** con `hm_media_mirror()`.
- **Pruebas en local:** 20 de 20 sin errores. El desplegable de PC muestra 6 servicios, igual que el menú móvil y el pie.
- **En vivo:** páginas 200, enlaces a `#avencas-mensais` presentes y ningún enlace a la web antigua.

## «Desde 2007» en todas las cabeceras y nombres de Trabalhos en móvil (2026-11-24)

- **«Moita, Portugal — desde 2007» → «Desde 2007»:** en Serviços, Projetos, Sobre, Blog y Contacto (antes ya estaban la Home y Design Web). En Branding vuelve «Desde 2007», que se había quitado.
  - `paquetes/2026-11-24-desde-2007.json`. Copia: `hm-paginas-bak/2026-11-24-antes-desde-2007/`.
- **Branding y Design Web · Trabalhos (móvil):** a 30 px, «Palmela Experiences» (9,95 em) se partía en dos líneas y se pegaba al texto de arriba. Ahora todos los nombres van a `min(26px, (86vw − 40px) / 10,4)` y en una línea: 26 px a 390 px y unos 22,6 px a 320 px. Afecta también a la copia con scroll de Branding. Capa: css `c6659970…`.
- **«Somos uma equipa…» (Home):** ya estaba hecho desde la ronda (móvil de 22 a 20 px; PC 1440 de 24 a 20 px; pantallas grandes de 32 a 26 px; interlineado de 1,2 a 1,45). Se le pasa a Laura una comparación de antes y después.
