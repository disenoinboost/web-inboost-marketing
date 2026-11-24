# Hortelã Magenta · Fase 2: web completa (2026-11-24)

**Sitio:** https://hortelamagenta.inboost.marketing (entorno de trabajo, ahora con `noindex` automático fuera de hortelamagenta.pt).
**Fuentes:**
- Web actual hortelamagenta.pt (Kirby, PT + EN), rastreada desde el servidor.
- Wayback Machine.
- Paquete «03-Contenidos» (21 Word).
- Words de Gonçalo «Avença Mensal 360°» y «Coaching de Marcas».

## Resumen

- **26 páginas nuevas** con el diseño de Claude Design:
  - 12 fichas de proyecto, 5 servicios y las 5 landings de especialidad.
  - Política de Privacidade, Política de Cookies, Mapa do site, Obrigado y 404 propia.
- **Páginas existentes:** se han completado las 10 que ya había (enlaces, menús, pie, contenidos provisionales y formulario).
- **URL de la web actual:** todas tienen destino.
  - Las portuguesas conservan exactamente su URL, incluida la barra final.
  - Las inglesas redirigen con 301 a su equivalente en portugués.
  - No queda ninguna URL de la web actual que dé 404.
- **Verificación local:** 37 rutas × móvil y PC = 74 pruebas, con 0 errores JS, 0 desbordes horizontales, 1 H1 por página, todas las imágenes con ALT y 0 enlaces internos rotos.
- **Verificación en vivo:**
  - 36 URL responden 200, con título y canonical propios.
  - Las variantes y alias responden 301 y las rutas inexistentes, 404 con la página del diseño.
  - `/sitemap.xml` lista 33 URL indexables.
- **Formulario:** probado de punta a punta (envío real, email enviado, validación, campo trampa y salto a /obrigado).

## 1. Inventario de URL de la web actual

Rastreo completo desde el servidor:
- El sitemap XML (36 URL, PT y EN).
- Todos los enlaces internos de cada página.
- Las URL citadas en los Word.
- Las 1.459 URL históricas de Wayback (~730 comprobadas una a una contra producción).

**Resultado:** 43 páginas vivas, 2 redirecciones existentes y un alias.
- Las 5 landings **no estaban en el sitemap ni enlazadas** desde ninguna página; solo se encontraron por los Word.
- Las URL históricas (WordPress antiguo, PHP anterior, `/portfolio/<proyecto>`…) **ya daban 404** en la web actual, así que no se pierde nada nuevo.

| URL actual | Página | Estado en la web actual |
|---|---|---|
| `/` | Início | 200 |
| `/projetos` | Projetos | 200 |
| `/projetos/consulai` | Consulai | 200 |
| `/projetos/knowledgebiz` | Knowledgebiz | 200 |
| `/projetos/queijaria-da-sao` | Queijaria da São | 200 |
| `/projetos/camolas` | Camolas | 200 |
| `/projetos/hospital-garcia-de-orta` | Hospital Garcia de Orta | 200 |
| `/projetos/croma` | Croma | 200 |
| `/projetos/alinea` | Alinea | 200 |
| `/projetos/livro-vilamoura` | Livro Vilamoura | 200 |
| `/projetos/farinhas-firmos` | Farinhas Firmos | 200 |
| `/projetos/alsil` | Alsilgroup | 200 |
| `/projetos/documentos-normativos-imt` | Documentos Normativos IMT | 200 |
| `/projetos/camara-municipal-de-almada-roteiro` | Câmara Municipal de Almada | 200 |
| `/projetos/imperalum` | Imperalum | 200 |
| `/servicos` | Serviços | 200 |
| `/sobre` | Sobre | 200 |
| `/contacto` | Contacto | 200 |
| `/politica-de-privacidade` | Política de Privacidade (noindex) | 200 |
| `/design-rotulos-vinho/` | Design de Rótulos para Vinhos (landing, fuera del sitemap y sin enlaces) | 200 |
| `/design-comunicacao-industria/` | Design de Comunicação para a Indústria (landing, fuera del sitemap y sin enlaces) | 200 |
| `/branding-clinicas-dentarias/` | Branding para Clínicas Dentárias (landing, fuera del sitemap y sin enlaces) | 200 |
| `/design-administracao-publica/` | Design para Administração Pública (landing, fuera del sitemap y sin enlaces) | 200 |
| `/design-de-eventos/` | Design de Comunicação para Eventos (landing, fuera del sitemap y sin enlaces) | 200 |
| `/en` | Versión inglesa | 200 |
| `/en/projects` | Versión inglesa | 200 |
| `/en/projects/consulai` | Versión inglesa | 200 |
| `/en/projects/knowledgebiz` | Versión inglesa | 200 |
| `/en/projects/queijaria-da-sao` | Versión inglesa | 200 |
| `/en/projects/camolas` | Versión inglesa | 200 |
| `/en/projects/garcia-de-orta-hospital` | Versión inglesa | 200 |
| `/en/projects/croma` | Versión inglesa | 200 |
| `/en/projects/alinea` | Versión inglesa | 200 |
| `/en/projects/vilamoura-book` | Versión inglesa | 200 |
| `/en/projects/farinhas-firmos` | Versión inglesa | 200 |
| `/en/projects/alsil` | Versión inglesa | 200 |
| `/en/projects/normative-documents-imt` | Versión inglesa | 200 |
| `/en/projects/camara-municipal-de-almada-roteiro` | Versión inglesa | 200 |
| `/en/projects/imperalum` | Versión inglesa | 200 |
| `/en/services` | Versión inglesa | 200 |
| `/en/about` | Versión inglesa | 200 |
| `/en/contact` | Versión inglesa | 200 |
| `/en/privacy-policy` | Versión inglesa | 200 |
| `/home` | Alias de la portada | 200 (duplicado) |
| `/portfolio`, `/portfolio/` | Redirección existente | 301 → /projetos |
| `/contactos` | Redirección existente | 301 → /contacto |

## 2. Páginas del sitio nuevo (36 + 404)

| Grupo | URL |
|---|---|
| Principales | `/` · `/servicos` · `/projetos` · `/sobre` · `/blog` · `/contacto` |
| Servicios | `/servicos/branding` · `/servicos/design-web` · `/servicos/design-grafico-e-editorial` · `/servicos/campanhas-e-redes-sociais` · `/servicos/fotografia-e-video` · `/servicos/avenca-comunicacao-360` · `/servicos/coaching-de-marcas` |
| Proyectos (13) | `/projetos/camolas` · `consulai` · `knowledgebiz` · `queijaria-da-sao` · `hospital-garcia-de-orta` · `croma` · `alinea` · `livro-vilamoura` · `farinhas-firmos` · `alsil` · `documentos-normativos-imt` · `camara-municipal-de-almada-roteiro` · `imperalum` |
| Especialidades | `/design-rotulos-vinho/` · `/design-comunicacao-industria/` · `/branding-clinicas-dentarias/` · `/design-administracao-publica/` · `/design-de-eventos/` |
| Blog | `/blog` · `/blog/quanto-custa-um-site` |
| Legales y auxiliares | `/politica-de-privacidade` (noindex) · `/politica-de-cookies` (noindex) · `/mapa-do-site` · `/obrigado` (noindex) · 404 en cualquier URL inexistente |

## 3. Correspondencia URL antigua → URL nueva

| URL antigua | URL nueva | Tipo |
|---|---|---|
| `/` | `/` | Mismo URL |
| `/projetos` | `/projetos` | Mismo URL |
| `/projetos/consulai` | `/projetos/consulai` | Mismo URL · ficha nueva |
| `/projetos/knowledgebiz` | `/projetos/knowledgebiz` | Mismo URL · ficha nueva |
| `/projetos/queijaria-da-sao` | `/projetos/queijaria-da-sao` | Mismo URL · ficha nueva |
| `/projetos/camolas` | `/projetos/camolas` | Mismo URL (ya existía en el diseño) |
| `/projetos/hospital-garcia-de-orta` | `/projetos/hospital-garcia-de-orta` | Mismo URL · ficha nueva |
| `/projetos/croma` | `/projetos/croma` | Mismo URL · ficha nueva |
| `/projetos/alinea` | `/projetos/alinea` | Mismo URL · ficha nueva |
| `/projetos/livro-vilamoura` | `/projetos/livro-vilamoura` | Mismo URL · ficha nueva |
| `/projetos/farinhas-firmos` | `/projetos/farinhas-firmos` | Mismo URL · ficha nueva |
| `/projetos/alsil` | `/projetos/alsil` | Mismo URL · ficha nueva |
| `/projetos/documentos-normativos-imt` | `/projetos/documentos-normativos-imt` | Mismo URL · ficha nueva |
| `/projetos/camara-municipal-de-almada-roteiro` | `/projetos/camara-municipal-de-almada-roteiro` | Mismo URL · ficha nueva |
| `/projetos/imperalum` | `/projetos/imperalum` | Mismo URL · ficha nueva |
| `/servicos` | `/servicos` | Mismo URL |
| `/sobre` | `/sobre` | Mismo URL |
| `/contacto` | `/contacto` | Mismo URL |
| `/politica-de-privacidade` | `/politica-de-privacidade` | Mismo URL · página nueva (texto actual) |
| `/design-rotulos-vinho/` | `/design-rotulos-vinho/` | Mismo URL con barra final · recreada en el diseño nuevo |
| `/design-comunicacao-industria/` | `/design-comunicacao-industria/` | Mismo URL con barra final · recreada en el diseño nuevo |
| `/branding-clinicas-dentarias/` | `/branding-clinicas-dentarias/` | Mismo URL con barra final · recreada en el diseño nuevo |
| `/design-administracao-publica/` | `/design-administracao-publica/` | Mismo URL con barra final · recreada en el diseño nuevo |
| `/design-de-eventos/` | `/design-de-eventos/` | Mismo URL con barra final · recreada en el diseño nuevo |
| `/en` | `/` | 301 (no hay versión inglesa) |
| `/en/projects` | `/projetos` | 301 (no hay versión inglesa) |
| `/en/projects/consulai` | `/projetos/consulai` | 301 (no hay versión inglesa) |
| `/en/projects/knowledgebiz` | `/projetos/knowledgebiz` | 301 (no hay versión inglesa) |
| `/en/projects/queijaria-da-sao` | `/projetos/queijaria-da-sao` | 301 (no hay versión inglesa) |
| `/en/projects/camolas` | `/projetos/camolas` | 301 (no hay versión inglesa) |
| `/en/projects/garcia-de-orta-hospital` | `/projetos/hospital-garcia-de-orta` | 301 (no hay versión inglesa) |
| `/en/projects/croma` | `/projetos/croma` | 301 (no hay versión inglesa) |
| `/en/projects/alinea` | `/projetos/alinea` | 301 (no hay versión inglesa) |
| `/en/projects/vilamoura-book` | `/projetos/livro-vilamoura` | 301 (no hay versión inglesa) |
| `/en/projects/farinhas-firmos` | `/projetos/farinhas-firmos` | 301 (no hay versión inglesa) |
| `/en/projects/alsil` | `/projetos/alsil` | 301 (no hay versión inglesa) |
| `/en/projects/normative-documents-imt` | `/projetos/documentos-normativos-imt` | 301 (no hay versión inglesa) |
| `/en/projects/camara-municipal-de-almada-roteiro` | `/projetos/camara-municipal-de-almada-roteiro` | 301 (no hay versión inglesa) |
| `/en/projects/imperalum` | `/projetos/imperalum` | 301 (no hay versión inglesa) |
| `/en/services` | `/servicos` | 301 (no hay versión inglesa) |
| `/en/about` | `/sobre` | 301 (no hay versión inglesa) |
| `/en/contact` | `/contacto` | 301 (no hay versión inglesa) |
| `/en/privacy-policy` | `/politica-de-privacidade` | 301 (no hay versión inglesa) |
| `/home`, `/inicio` | `/` | 301 |
| `/portfolio` | `/projetos` | 301 (se mantiene) |
| `/contactos`, `/contacts` | `/contacto` | 301 (se mantiene) |

## 4. Páginas creadas desde cero

| Página | Composición (bloques del diseño) | Contenido |
|---|---|---|
| 12 fichas de proyecto | Modelo de Camolas: cabecera con foto, «Sobre o projeto» con datos, identidad con pestañas, galería horizontal fijada, vídeo que crece, carrusel con lightbox, testimonio, «Mais projetos» y contacto. Barra «Neste projeto» | Descripción, categorías, imágenes y vídeos de cada ficha actual. Testimonios reales de /sobre en Consulai, Farinhas Firmos e IMT. Enlaces a los servicios y especialidades de cada caso |
| Gráfico + Editorial | Cabecera con palabras rotativas, texto, paneles, lista editorial, trabajos, testimonio (IMT), FAQ y contacto | Los 4 servicios actuales (Packaging, Folhetos e Brochuras, Catálogos e Publicações, Decoração de Ambientes) y los Word S06/S07 adaptados a PT-PT |
| Campanhas & Redes Sociais | Cabecera, paneles, frase destacada, trabajos, testimonio (Consulai) y contacto | Textos actuales de Campanhas Digitais y Redes Sociais. Planteada **dentro de la comunicación global** (avença), como pide la ficha H02 |
| Fotografia & Vídeo | Cabecera, paneles, vídeo corporativo (Farinhas Firmos), lista, trabajos, testimonio, FAQ y contacto | Los 4 servicios actuales (Institucional e Ambiente, Produto, Packshot, Motion Graphics) y los Word S03/S04 adaptados |
| Avença Mensal 360° | Cabecera con el H1 del Word, textos, lista «O que inclui» (9), paneles «Porquê» (4), frase, FAQ y contacto | Word de Gonçalo, literal. Title, meta, H1, H2 y FAQ los del Word |
| Coaching de Marcas | Cabecera, texto, cita de Gonçalo con su foto, listas «Para quem é» y «Como funciona», frase, FAQ y contacto | Word de Gonçalo, literal |
| Política de Cookies | Modelo de artículo (índice lateral) | Texto de cookies de la política actual y del panel de preferencias actual. Lista real de lo que guarda el sitio nuevo (verificado en el código) |
| Mapa do site | Modelo de artículo | Todas las páginas por secciones |
| Obrigado | Cabecera («Obrigado. Recebemos a sua mensagem / ideia / história.») y proyectos | Nueva |
| 404 | Cabecera creativa («Esta página saiu para uma reunião / a gráfica / um café / outro projeto.»), enlaces útiles, proyectos y contacto | Nueva. Se sirve con estado 404 en cualquier URL inexistente |

Recreadas en el diseño nuevo a partir de la web actual (mismo contenido íntegro y misma URL):
- **Las 5 landings.** Se añaden migas, enlaces a los casos reales (Camolas, Alsil, Farinhas Firmos, Imperalum, Queijaria da São, IMT, Almada, HGO y Croma) y a los servicios, y «Conheça também», según las fichas L01–L05.
- **La Política de Privacidade.**

## 5. Páginas existentes completadas o corregidas

| Página | Cambio |
|---|---|
| Todas (10) | Enlaces a la web antigua (`https://hortelamagenta.pt/projetos/…`, landings, política) → enlaces internos. Enlaces internos sin barra final (igual que el canonical). Menú de PC: Gráfico + Editorial, Campanhas, Fotografia y Avenças llevan a sus páginas, y entra Coaching. Menú móvil: los 13 proyectos bajo «Projetos» y Coaching bajo «Serviços». Pie: Coaching, Política de Cookies y Mapa do site. Fuera el selector «EN» (no hay versión inglesa) |
| Branding y Design Web | El canonical apuntaba a `/branding-para-empresas` y `/websites-para-empresas`, URL que no existen. Ahora es la URL real |
| Serviços | «Explorar …» en Gráfico + Editorial, Campanhas, Fotografia y Avenças (antes «Pedir orçamento»). Nueva sección 07 «Coaching de Marcas» con la misma composición que Avenças. Contadores a «/ 07» |
| Home | El servicio Avenças enlaza a su página (nota del Word de Gonçalo) |
| Blog | Se mantienen las 6 tarjetas de ejemplo del diseño para ver cómo queda el blog (petición de Laura). Son temas propuestos sin artículo escrito: las seis llevan a «Quanto custa um site para empresas?», el único artículo real. Las 6 entradas de WordPress que tenían solo el extracto (ID 180–185) pasan a borrador; las tarjetas no dependen de ellas |
| Artigo | «Continue a ler» mostraba 3 artículos inexistentes. Ahora «Continue a explorar», con Design Web, Knowledgebiz y Farinhas Firmos |
| Contacto | El formulario no enviaba nada. Ahora envía de verdad y lleva a /obrigado. Tiene campo trampa, mensaje de error y preselección del servicio con `?servico=` |
| Capa de correcciones (JS) | El menú móvil marca la página actual también con URL sin barra final. La barra «Pedir orçamento · Ligar» no sale en /contacto ni en /obrigado |

## 6. Redirecciones 301

Activas en `hm-rutas.php`. Valen igual en producción y son reaplicables.

- **Barra final:** cada URL tiene una sola forma canónica y la otra redirige.
  - `/servicos/` → `/servicos`.
  - `/design-rotulos-vinho` → `/design-rotulos-vinho/`.
- **Versión inglesa (19 URL):**
  - `/en` → `/`.
  - `/en/projects` → `/projetos`.
  - `/en/projects/<slug>` → `/projetos/<slug>`. Cambian tres: `garcia-de-orta-hospital` → `hospital-garcia-de-orta`, `vilamoura-book` → `livro-vilamoura` y `normative-documents-imt` → `documentos-normativos-imt`.
  - `/en/services` → `/servicos`, `/en/about` → `/sobre`, `/en/contact` → `/contacto` y `/en/privacy-policy` → `/politica-de-privacidade`.
  - Cualquier otra `/en/...` → `/`.
- **Que ya existían o son alias:**
  - `/portfolio` → `/projetos`.
  - `/contactos` y `/contacts` → `/contacto`.
  - `/home` e `/inicio` → `/`.
  - `/pedir-orcamento` → `/contacto`.
- **WordPress:**
  - `/quanto-custa-um-site` → `/blog/quanto-custa-um-site`.
  - `/privacy-policy` → `/politica-de-privacidade`.
  - `/category/*` y `/tag/*` → `/blog`.
  - `/author/*` → `/sobre`.
  - Entradas, adjuntos y feeds → 404 del diseño.
- **URL propuestas en el plan SEO de los Word:**
  - `/branding-para-empresas` → `/servicos/branding`.
  - `/websites-para-empresas` y `/criacao-de-lojas-online` → `/servicos/design-web`.
  - `/design-grafico`, `/design-editorial` y `/design-de-embalagens` → `/servicos/design-grafico-e-editorial`.
  - `/producao-de-video`, `/fotografia-de-produto` y `/fotografia-corporativa` → `/servicos/fotografia-e-video`.
  - `/campanhas-digitais` y `/gestao-de-redes-sociais` → `/servicos/campanhas-e-redes-sociais`.
  - `/guias/quanto-custa-um-site` → `/blog/quanto-custa-um-site`.
- **Medios de Kirby:** `/media/...` → copia local en `uploads/hm-media/` (para imágenes indexadas y enlaces externos).

## 7. Contenidos o datos que necesitan confirmación

- **Textos adaptados de los Word en español (pendientes de aprobación según los propios Word):**
  - Gráfico + Editorial (S06/S07).
  - Fotografia & Vídeo (S03/S04).
  - Partes de Campanhas.
  - Dani revisa el texto y Gonçalo valida las prestaciones: preparación de archivos, producción e impresión, versiones digitales, logística de sesiones y vídeo.
- **Campanhas & Redes Sociais:**
  - La ficha H02 dice que el cliente excluyó captar encargos aislados de marketing digital, y la página lo presenta así.
  - Gonçalo decide si se mantiene indexable o solo enlazada desde Avenças.
- **Avença y Coaching:** texto literal de los Word «para revisión». Pendiente el OK final y si se pueden nombrar los clientes con avença (no se ha nombrado ninguno).
- **Pies e ALT de las fichas:** describen lo que se ve en cada imagen (p. ej. «Estacionário», «Roll-ups»). Hay que revisarlos, sobre todo los títulos de pestañas como «Universo» o «Construção».
- **Alinea:** la web actual dice «premium oral care». La ficha L03 pide no presentarla como caso dental sin confirmación, así que no se enlaza desde la landing de clínicas. Confirmar.
- **Landing de clínicas dentales:**
  - Sus dos imágenes (`dental_clinic_*.png`) parecen ilustrativas y no de un proyecto propio. Confirmar autoría.
  - No hay caso dental acreditado.
- **Landings:** se conservan las afirmaciones comerciales actuales, por ejemplo «eleva o seu valor percebido» o «experiência comprovada». Confirmar los premios IWSC 2024 y Mutante Awards 2025.
- **Legales:**
  - La política de privacidad usa `info@hortelamagenta.com` (dominio .com). Confirmar el email y si se añade el NIF o los datos registrales.
  - La Política de Cookies es nueva (ahora con Complianz, GTM/GA4 y el píxel de Meta) y necesita validación jurídica.
  - No existe «Aviso legal» en la web actual y no se ha inventado. En Portugal las sociedades deben identificarse en su web (Código das Sociedades Comerciais, art. 171.º; a validar jurídicamente): denominación, sede, conservatória del registro, número de matrícula/NIPC y capital social. Si venden a consumidores, también la información de resolución alternativa de litigios (RAL). Pedir esos datos al cliente para añadir una sección «Informação legal».
- **Vídeos de Vimeo** (Alinea y Livro Vilamoura): se enlazan, no se incrustan, para no instalar cookies de terceros sin consentimiento.
- **Versión inglesa:** la web actual tiene 19 páginas en inglés indexables. El diseño nuevo es solo en portugués. Ahora redirigen (301). Decidir si se rehace una versión EN.
- **Blog:** solo hay un artículo real. Ni la web actual (no tiene blog) ni la archivada en nostalgia.hortelamagenta.pt (portfolio, servicios, equipo y Hortelanices) tienen artículos que migrar. Las 6 tarjetas de ejemplo siguen a la vista y llevan al artículo real: antes de publicar, hay que escribir esos artículos o quitar las tarjetas (`extras._blog_sem_exemplos` en el generador). Material de partida: S02 para naming, manual y rebranding, S01, S04, el Word de avença y la guía A02.
- **No creadas por falta de contenido real (los Word lo indican):** no son páginas de la web actual, sino propuestas del plan de contenidos SEO de Inboost (paquete «03-Contenidos»). Para hacerlas hace falta material del cliente:
  - Páginas locales `/criacao-de-sites-lisboa` y `/criacao-de-sites-algarve` (G01/G02): confirmar que trabajan y atienden clientes en Lisboa y el Algarve, y al menos un proyecto o caso de cada zona (con permiso para citarlo).
  - Guía `/guias/manual-identidade-visual` (A02): un manual de identidad real que se pueda enseñar (o partes), con autorización del cliente final.
- **Pendientes de rondas anteriores:** la foto original de Alinea y más anuncios de Camolas.

## 8. Errores detectados y corregidos

1. **Canonical de Branding y Design Web:** apuntaba a URL inexistentes.
2. **Duplicados por barra final:** `/servicos` y `/servicos/` respondían 200 los dos. También en la web actual: `/projetos/camolas` y `/projetos/camolas/`.
3. **Enlaces a la web antigua:** había 163 en las plantillas (cuerpo y lógica). En producción habrían funcionado solo por casualidad; en el entorno de trabajo llevaban fuera.
4. **Selector «EN»:** llevaba a una versión que no existe en el sitio nuevo.
5. **Contenido provisional:**
   - «Continue a ler» con artículos inexistentes.
   - 6 entradas vacías publicadas en WordPress (ahora en borrador).
6. **Formulario de contacto:** simulaba el envío.
7. **Rutas nativas de WordPress:** entradas, adjuntos, categorías y feeds eran públicos con la plantilla antigua de Divi. El sitemap de WordPress listaba las páginas Divi con otras URL.
8. **Indexación del entorno de trabajo:** era indexable (`blog_public=1` y sin noindex). Ahora lleva `X-Robots-Tag: noindex` en cualquier dominio que no sea hortelamagenta.pt (se desactiva solo en producción).
9. **`?divi` y `?paquete`:** eran accesibles para cualquiera. Ahora solo con sesión.
10. **Menús incompletos:** el menú móvil «Projetos» solo tenía Camolas, y el menú de PC llevaba tres servicios a anclas.
11. **Peso de los paquetes:** llevaban imágenes incrustadas que no usaban. Design Web pasa de 3,2 MB a 1 MB y Camolas, de 2,2 MB a 0,4 MB.

## 9. Pendiente antes de publicar

1. **Aprobaciones:** validar los textos del punto 7 (Dani en ES y PT; Gonçalo, los hechos).
2. **Formulario:**
   - Definir el destinatario con `update_option('hm_form_to', 'email-de-hortela')`. Ahora llega al email de administración de WordPress.
   - Comprobar la entrega del correo en el servidor de producción (SPF/DKIM o SMTP).
3. **Analítica y consentimiento** (hecho en la ronda del punto 10; quedan estos pasos):
   - **GTM-KXHQKJMV:** incluye dos etiquetas HTML de píxel de Meta (1075614403527200 y 1791344078253720) que disparan PageView sin condición. En GTM, añadirles «Configuración de consentimiento → requerir `ad_storage`» (o el activador `cmplz_event_marketing`) para que respeten el banner. GA4 ya respeta el Consent Mode.
   - **Site Kit:** conectar con la cuenta de Google del cliente (Search Console y GA4) cuando el dominio sea hortelamagenta.pt. Sus etiquetas están bloqueadas por código para no duplicar GA4; no hace falta tocar «colocar fragmento».
   - **WP Mail SMTP:** configurar el buzón de envío (ahora usa `mail()` de PHP).
   - **Wordfence:** completar la instalación con una licencia gratuita (pide un email de Inboost) y poner un email de alertas. El cortafuegos está en modo aprendizaje (lo normal la primera semana).
4. **Migración del dominio:**
   - Apuntar hortelamagenta.pt a este WordPress y cambiar `home` y `siteurl`.
   - Redirigir www → sin www y http → https (el servidor actual ya lo hace).
   - Confirmar que `X-Robots-Tag` desaparece y que robots.txt y sitemap usan el dominio final.
5. **Medios:**
   - Están todos copiados en local (`hm_media_mirror`: 0 pendientes), así que las páginas no dependen del servidor antiguo.
   - Tras el cambio de DNS, comprobar que `/media/...` de Kirby llega a WordPress y redirige a la copia local.
   - Los `og:image` de algunas páginas existentes apuntan a hortelamagenta.pt/media o a nostalgia; conviene pasarlos a la copia local.
6. **Search Console:**
   - Enviar `/sitemap.xml`.
   - Retirar el hreflang EN.
   - Seguir cobertura, 404 y las consultas de las landings durante 30, 60 y 90 días.
7. **Pruebas tras el cambio:**
   - Las 36 URL, las 301 de la tabla del punto 6 y el formulario real en producción.
   - Vaciar WP Rocket.
8. **Divi:** el README de la fase 1 prevé rehacer las páginas en Divi al final. Si se hace, conservar el mapa de URL (`hm-rutas.php`) y los bloques de datos del generador como fuente de contenido.

## 10. Ronda 2026-11-24 (tarde): portugués, plugins y cookies

**Idioma:**
- WordPress pasa a `pt_PT` (paquete de idioma instalado). Los usuarios 1 y 2 conservan el escritorio en español.
- Revisión del texto visible, atributos (`alt`, `aria-label`, `title`, `placeholder`) y salida de plugins de las 37 páginas servidas: sin castellano. Los textos del formulario, del correo y de los mensajes de error ya estaban en portugués.
- Único resto encontrado: los valores internos del ajuste de fondo de las fichas de proyecto («Gris claro / Gris oscuro / Negro», no visibles). Ahora son «Cinza claro / Cinza escuro / Preto».

**Plugins instalados y activos** (wordpress.org, con traducciones pt_PT y es_ES):

| Plugin | Versión | Configuración |
|---|---|---|
| Complianz | 7.5.7 | Región UE; banner propio (Spartan, esquinas rectas, #1C1B23 y #D82E87) con textos PT-PT; categorías Necessários, Estatísticas y Marketing; GTM-KXHQKJMV con Consent Mode v2; políticas propias (/politica-de-cookies y /politica-de-privacidade) |
| Yoast SEO | 28.9 | Sitemaps XML desactivados (el sitio usa su propio /sitemap.xml). No controla el SEO de las páginas del diseño: título, descripción, canonical y JSON-LD van en cada paquete |
| Site Kit by Google | 1.192.0 | Sin conectar (pendiente). Etiquetas bloqueadas por código para no duplicar GA4 |
| WP Mail SMTP | 4.10.4 | Sin credenciales (pendiente) |
| Wordfence | 9.1.1 | Cortafuegos en modo aprendizaje; sin licencia (pendiente) |
| WP Rocket | 3.21.1 | Ya estaba |

- **Schema Pro:** no instalado. Es de pago (hace falta el zip y la licencia de Inboost). Las páginas ya llevan su JSON-LD en el paquete.

**Salida de plugins en las páginas del diseño:**
- Las páginas del diseño se sirven antes de `wp_head()`, así que ningún plugin llegaba a ellas.
- `hm-boceto.php` ejecuta ahora `wp_head`/`wp_footer` solo con las funciones de Complianz y Site Kit (más las de WordPress que imprimen sus estilos y scripts) e inyecta el resultado. Yoast, Divi y el resto quedan fuera.
- **GTM solo se carga en hortelamagenta.pt:** en el entorno de trabajo, las visitas de revisión no entran en GA4 ni en los píxeles.
- Sin meta «generator».

**Pie de todas las páginas:** botón «Preferências de cookies» entre «Política de Cookies» y «Mapa do site». Reabre el panel de Complianz.

**Política de Cookies:** describe lo que se instala de verdad:
- Necesarias: `cmplz_*` 365 días y el `sessionStorage` del sitio.
- Estadísticas: `_ga` y `_ga_*` de GA4 vía GTM.
- Marketing: `_fbp` del píxel de Meta.
- También explica el Consent Mode, los terceros (Google y Meta, con transferencias bajo el Data Privacy Framework) y cómo cambiar la elección.

**Verificación:**
- En vivo: 36 rutas en 200 y la 404 en 404, todas con `lang="pt-PT"`, banner y botón del pie.
  - Sin GTM fuera de producción; en producción simulada, GTM sale con el consentimiento denegado por defecto.
  - `/sitemap.xml` en 200 y `/sitemap_index.xml` en 404.
  - El formulario REST sigue respondiendo con Wordfence activo.
  - El enlace del banner dice «Política de Privacidade».
- En local (Chromium, móvil y PC):
  - El banner aparece.
  - «Ver preferências» muestra las 3 categorías.
  - «Recusar» guarda la negativa (`cmplz_statistics=deny`, `cmplz_marketing=deny`).
  - El botón del pie reabre el panel y «Aceitar» guarda `allow`.
  - 0 errores JS y sin desborde horizontal.

