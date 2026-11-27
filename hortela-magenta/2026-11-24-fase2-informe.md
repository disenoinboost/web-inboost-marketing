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

## 11. Ronda 2026-11-24 (noche): fichas, landings y columnas

**Fichas de proyecto (las 12, mismo criterio para todas):**
- **Imágenes de la web actual:** ya se usaban todas salvo variantes de logotipo. Ahora entran los GIF animados de Alsil, Imperalum, Knowledgebiz y Queijaria, las versiones clara y oscura de Imperalum y Knowledgebiz y la construcción del logotipo de Imperalum. Los vídeos de Vimeo (Alinea y Vilamoura) siguen enlazados.
- **Recortes:**
  - En Identidade las imágenes se encajan siempre enteras: los gráficos de fondo liso, sobre su propio color; las fotografías, sobre una copia desenfocada.
  - En Aplicações cada tarjeta toma la proporción de su imagen.
  - Se cortaban por `object-fit: cover` en cajas de proporción fija (2:1 y 3:2) y, en el móvil, por una regla de Camolas de la capa de corrección (ahora limitada con `data-hm-fit`).
- **Imágenes partidas** (`hm-media/split/`, hechas en el servidor a partir de la copia local):
  - Queijaria: saco y caja (antes «Merchandising»); logotipo sobre amarillo y sobre azul.
  - Croma: t-shirt y pins.
  - Los pins de HGO se muestran enteros (el patrón de abajo forma parte de la pieza).
- **Secciones nuevas, con el componente de Camolas:**
  - «Anúncios e redes sociais» (lista con imagen fija que cambia) en las 12. Cuando no hay anuncios, la sección lleva el título de lo que sí hay: «Cartazes e digital» en Knowledgebiz, «O livro por dentro» en Vilamoura, «Mapas e desdobrável» en Almada, etc.
  - «O site» (vídeo que crece) en Knowledgebiz, Queijaria, Alinea, Farinhas Firmos y Alsil. Los vídeos de la web actual ya son mockups con dispositivos, por eso no van dentro del marco de navegador de Camolas. Para hacerlo exactamente como en Camolas harían falta capturas completas de esos sites, y antes confirmar que siguen siendo diseño de Hortelã.
  - Textos nuevos: describen solo lo que se ve o reutilizan frases de la web actual.
- **Testemunhos:** solo hay de Consulai, Farinhas Firmos e IMT. Los demás de /sobre son de otros clientes (Inframoura, Stericycle, Adrepes, Coprate, Mafraria, Homesphere, Tavira Lawyers). Para el resto de fichas, pedir citas al cliente.

**Servicios y landings:**
- **Carruseles que no se arrastraban** (Rótulos, Clínicas, Adm. pública, Eventos, Indústria): en las páginas de servicio el arrastre del marquee se activa con `data-mq-drag` (fx-servico) y llevaban `data-drag` (el de las fichas).
- **Hueco blanco al final del carrusel:** el conjunto de imágenes se repite hasta pasar del ancho de la pantalla.
- **Titulares largos** (Avença, Coaching, Adm. pública, Rótulos, Indústria): ocupan también la columna derecha, por encima del texto pequeño. Avença y Coaching tienen líneas propias para ese formato (`display_wide`).
- **Texto sobre imagen** («O que fazemos» de Gráfico + Editorial y el resto de paneles): degradado más oscuro bajo el texto y texto en blanco puro.
- **Más fotografía** con proyectos reales y enlace a cada uno:
  - Adm. pública: IMT, Almada, HGO y Vilamoura.
  - Eventos: CROMA y stands de Alsil.
  - Rótulos: Camolas.
  - Clínicas: sus dos imágenes pasan a una franja grande fija (eran un carrusel de dos imágenes repetidas).
  - Clínicas no tiene más material real. Las clínicas Alinea («premium oral care») tienen fotografías muy buenas, pero su ficha L03 pide confirmación antes de presentarlas como caso dental.
- **Prémios:** las dos imágenes se ven enteras sobre su color, en tarjetas que ocupan todo el ancho.
- **Indústria y Rótulos:** menos espacio antes de «Mais projetos». Se sumaban los rellenos de las dos secciones.
- **Imagen rota en vivo:** la de Filipe Palhoça en el portafolio de Rótulos (el archivo estaba guardado como `.jpg_id-6329`). Copiada con su nombre.

**Columnas:** todas las secciones de dos columnas de servicios y landings (texto, listas, preguntas, «Para quem», enlaces, cabecera de paneles y frase) usan la misma rejilla 5:7. La columna derecha empieza en el mismo punto en todas y se apilan por debajo de ~800 px.

**Verificación:**
- En local, con las imágenes reales traídas del servidor: las 12 fichas por secciones en PC y Queijaria en móvil; arrastre comprobado por código en 5 páginas; regresión de 36 rutas × 2 sin errores JS ni desbordes.
- En vivo: 36 rutas en 200 y ninguna imagen referenciada que falte en el servidor.

## 12. Ronda 2026-11-24 (última): titulares, fotos y entrelíneas

**Titulares de servicios y landings:**
- Todos usan el tamaño y la estructura de Branding: misma fórmula de tamaño, título en la columna izquierda y texto pequeño abajo a la derecha. Los de la ronda anterior usaban otra fórmula y salían más grandes en pantallas medianas.
- **3 líneas (como Branding y Design Web):** el antetítulo queda a la misma altura en 1280, 1440, 1536 y 1920 px. Afecta a Rótulos, Clínicas, Indústria, Eventos, Campanhas y Fotografia.
- **Líneas largas:** pueden pasar a la columna derecha (`width:max-content`) solo si quedan por encima del texto pequeño. La última línea siempre cabe a la izquierda. Comprobado línea a línea en 6 tamaños de pantalla (de 1100×760 a 1920×1080): ninguna toca el texto pequeño.
- **4 líneas:** Avença, Coaching y Administração pública no caben en 3 líneas a ese tamaño sin pisar el texto pequeño, y Gráfico + Editorial se queda en 4 líneas cortas, como el diseño original. En esas cuatro el antetítulo queda ~60 px más arriba. Para igualarlas habría que acortar el titular (cambio de texto, a validar con el cliente).

**Fotos:**
- Avença: dos franjas de trabajos (Consulai, Alinea y Farinhas Firmos; CROMA, Queijaria e Imperalum). Los pies dicen el proyecto y la pieza; no dicen que sean clientes de avença.
- Coaching: fotos del ateliê del archivo de la web antigua (post-its, pruebas de trabajos, el espacio). Son de 2016 y de 1024 px.
- Clínicas: franja con el rebranding del Hospital Garcia de Orta (identidad en salud), debajo de las dos imágenes de clínica.

**Franjas de fotos:** cuando siguen a un texto (Adm. pública, Eventos, Avença…) van pegadas, con el mismo fondo y sin espacio por encima.

**Entrelíneas:**
- Títulos de sección: de .95–.98 a 1.04–1.06.
- Títulos de la lista con imagen: de 1 a 1.1.
- Datos del proyecto (Cliente, Serviços…): de 1.12 a 1.25.
- Pies de foto: subrayado separado del texto y entrelínea de 1.7, para que no se toquen al partirse en dos líneas.

**Verificación:** regresión de 36 rutas × 2 sin errores ni desbordes; en vivo, 36 rutas en 200 y ninguna imagen referenciada que falte.

**Transición de la cabecera (blanco → gris):** al hacer scroll, el velo de la cabecera (`data-veil`) la pinta con el color de la sección siguiente, como en Branding. En servicios y landings el velo era gris (#e8eced) y la sección siguiente blanca, así que la cabecera pasaba a gris y luego saltaba a blanco. Ahora la primera sección de cada página toma el gris del velo (o el velo toma el color de la sección, si esta ya trae uno propio). En Obrigado la sección siguiente es blanca y el velo pasa a blanco. En Serviços se probó igual, pero así la fusión no se veía; desde el 2026-11-26 el velo vuelve a ser gris y la fila «Branding» toma ese gris. Comprobado en las 32 páginas con cabecera de ese tipo.

**Galería «Trabalhos» (2026-11-26):**
- **Dónde:** Gráfico + Editorial, Campanhas y Fotografia & Vídeo.
- **Problema:** el componente `data-lp` del diseño para en cada tarjeta. Al medirlo, 14 de cada 40 pasos de scroll no movían la galería, de ahí la sensación de ir a golpes.
- **Solución:** estas tres usan ahora `data-lpf`, implementado en `capa-fix/hm-boceto-fix.js`, con los mismos efectos pero avance continuo: unos 89 px por paso, ninguno parado.
- **Ampliado el 2026-11-26** a Branding, Design Web, «Rótulos» de Camolas y «Aplicações» de las 12 fichas. Ya no queda ninguna galería con paradas (ver sección 14).

## 13. Ronda 2026-11-26: fondos, franjas, espaciado y cursor

**Espaciado entre secciones (todas las páginas generadas):**
- **Regla:** dos secciones seguidas nunca comparten fondo. Si coinciden, la segunda cambia: de un gris pasa a blanco y del blanco pasa a #f6f7f8. Así cada frontera es «126 px · cambio de color · 126 px», como en Branding.
- **Antes:** con el mismo fondo se sumaban los dos rellenos y se veía un hueco en blanco de 212–252 px. Era el caso de la franja «Imperalum · Outdoor» antes de «Departamento externo», o de los paneles antes de «Design editorial».
- **Franjas de fotos pegadas a un texto:** siguen al color de la sección anterior y ahora terminan con el mismo espacio que el resto de secciones (126 px); antes eran 86 px.
- **Fichas de proyecto:** el mismo criterio con los tonos. «Anúncios» ya no repite el tono de «Aplicações», y «Mais projetos» pasa a gris claro cuando le precede «Fotografia», que es blanca.
- **Auditoría:** se midió cada frontera en 36 rutas. Ya no queda ningún par con el mismo fondo, salvo las franjas de fotos pegadas a su texto, que son intencionadas.
- **Fuera del cambio:** las páginas de diseño original (portada, Branding, Design Web, Sobre) no se tocan.

**Franjas de los paneles:** en Campanhas y Fotografia el fondo de la sección es gris (#e8eced) y la primera franja (o la cuarta) tenía ese mismo color, así que se fundía. Ahora las franjas usan grises distintos del fondo de su sección (revisado después en la sección 14).

**Serviços:** vuelve la fusión gris de la cabecera; la fila «Branding» pasa a gris para continuarla.

**Cursor grande** («Ver projeto», «Arraste», «Falar»…): el texto pasa de 16 a 12,5 px. «Ver projeto» medía 96 px, lo mismo que el círculo; ahora mide 75 px. La regla está en `capa-fix/hm-boceto-fix.css` y vale para toda la web.

**Antetítulo del hero:** ocupa una sola línea siempre que cabe. En Administração Pública es así desde 1024 px; en tablet y móvil se parte en líneas. Los titulares de 4 líneas se quedan como están (validado por Laura).

**Verificación:**
- Regresión local: 36 rutas × 2 (ordenador y móvil), ancho correcto y 0 errores.
- En vivo: 25 plantillas reconstruidas y CSS con md5 comprobado; marcadores nuevos presentes en las páginas servidas.

## 14. Ronda 2026-11-26 (tarde): galerías continuas, tonos de las franjas e índice de Serviços

**Galerías que se mueven al hacer scroll, ahora todas continuas:**
- **Dónde:** «Trabalhos» de Branding y Design Web, «Rótulos» de Camolas y el carrusel de materiales («Aplicações», «Materiais promocionais»…) de las 12 fichas. Se suman a las tres de servicios que ya lo eran.
- **Cómo:** `data-lp` → `data-lpf`. Los efectos son los del diseño, pero sin paradas: 0 de 40 pasos de scroll parados en las cuatro galerías medidas.
- **Fichas y Camolas** usan `data-lpf="p"`, que reproduce cómo revela los paneles el diseño de las fichas: los últimos se completan al final del recorrido.
- **Rendimiento:** la animación se detiene cuando la galería está quieta y vuelve con el scroll.
- **Móvil:** no cambia. Las galerías de deslizar (Trabalhos, Rótulos) siguen siendo nativas; la copia de Branding que avanza al bajar y las «Aplicações» pasan también a movimiento continuo.

**Franjas de los paneles:** antes la 1.ª y la 4.ª tenían el mismo tono, también en Branding. Ahora cada franja tiene un tono propio, nunca el del fondo, en el orden de Branding (claro, medio, oscuro…):
- Sobre gris: #f6f7f8, #dde3e7, #a6b4c1, #cbd4db, #b9c5cf.
- Sobre blanco: #e8eced, #dde3e7, #a6b4c1, #cbd4db, #b9c5cf.
- Afecta a Branding, Gráfico + Editorial, Campanhas, Fotografia, Avença, Rótulos, Indústria y Eventos.

**Serviços · índice de servicios:** margen interior superior de 44 a 72 px. Por debajo no cambia.

**Verificación:**
- Regresión local: 36 rutas × 2 sin errores ni desbordes.
- En vivo: JS (md5 566713b8…) y 23 plantillas desplegados; atributos y colores nuevos comprobados en las páginas servidas.

## 15. Ronda 2026-11-26 (noche): páginas más visuales y arreglos

**Componentes nuevos, tomados de Design Web:**
- **Filas que se abren** (bloque `ambito`, como «Âmbito e orçamento»):
  - Número y palabra grande; al pasar el cursor (o tocar en móvil) la palabra se ilumina y aparece el texto con el trazo magenta.
  - Está en Coaching («Como funciona»), Gráfico + Editorial («Design editorial»), Fotografia («Como trabalhamos») y en los procesos de Rótulos, Indústria, Clínicas («Método»), Administração Pública y Eventos («O ciclo contínuo»).
- **Galería tipo «Conteúdos»** (bloque `galeria`): tres filas que avanzan solas, se arrastran y se amplían al pulsar, todas con piezas reales de los proyectos.
  - Campanhas: publicaciones, anuncios y outdoors.
  - Fotografia: fábricas, productos, personas y espacios, con algunos vídeos.
  - Avença: estacionario, redes sociales, sitios, fotografía y embalaje.
- **Coaching sin galería:** solo hay 5 fotos del ateliê, antiguas (2016) y de poca calidad; montada, la galería quedaba pobre. Se queda la franja de 3 fotos. Si hay fotos de sesiones o del ateliê actual, se monta igual.

**Arreglos:**
- **HGO · roll-up:** la imagen original traía una franja blanca de 171 px arriba. Se ha recortado y centrado en el servidor (`hm-media/split/hgo-rollup.webp`, 924×935).
- **Fichas de proyecto y Camolas · galería fija** («Aplicações»/«Rótulos»): la pantalla fija ocupaba 100vh con el contenido centrado y dejaba ~235 px de vacío arriba. Ahora arranca a 126 px, como el resto de secciones, y se fija centrada mientras avanza.
- **Sobre · opinión de Mafraria:** la foto apuntaba a `assets/clientes/mafraria.jpg`, que no venía en el paquete del diseño. Ahora usa una pieza de la propia marca de la mediateca («Um café singular»).
- **Imágenes rotas:** escaneadas las 1.014 referencias de imagen de las 36 páginas; no queda ninguna rota.
- **Imágenes en negro y de golpe:** las fotos de las opiniones se cargaban en diferido sobre fondo oscuro; ahora se precargan al acercarse la sección. Además, toda imagen visible entra con un fundido de 0,6 s.
- **Contacto · dirección:** de 4 líneas a 2, con la letra algo menor y sin cortes dentro de cada línea.

**Verificación:**
- Regresión: 36 rutas × 2 sin errores ni desbordes.
- Espaciado: sin secciones seguidas con el mismo fondo, salvo las franjas pegadas a su texto.
- En vivo: 13 plantillas, CSS y JS desplegados con md5 comprobado.

## 16. Ronda 2026-11-26 (cierre): móvil, contacto, lightbox y «Como funciona»

- **Fichas · «Aplicações»:** todas las imágenes tienen la misma altura, en escritorio y en móvil. El ancho tenía un tope (84vw / 940 px) que encogía las imágenes anchas: en móvil medían entre 164 y 240 px de alto y ahora todas 240 px. Se ha comprobado en los 12 proyectos.
- **HGO · roll-up:** la página publicada usa la imagen recortada desde la ronda anterior. Si aún se ve la franja, es la caché del navegador.
- **Migas de pan en móvil:** siempre en una línea (15 px). Si el último nivel no cabe, termina en «…»; solo pasa con «Campanhas & Redes Sociais».
- **Menú móvil · Projetos:** primero los seis destacados del menú de escritorio (Camolas, Queijaria da São, Farinhas Firmos, Alsilgroup, Hospital Garcia de Orta y Livro Vilamoura) y después el resto.
- **«O site» / «Filme» en móvil:** el pie se colocaba suponiendo un vídeo 16:9 y en los vídeos más altos quedaba encima. Ahora va debajo, calculado con la proporción real de cada vídeo.
- **Contacto:** la dirección usa la misma letra que «Orçamentos» y «Redes» (20–26 px), en tres líneas.
- **Lightbox:** sin el recuadro rosa en la X ni en las flechas. Era el estilo de foco, porque la X recibe el foco al abrirse.
- **Coaching · «Como funciona»:** pasa de desplegable a filas siempre visibles, como en Sobre. Cada paso lleva más texto, todo sacado del Word de Gonçalo (de las respuestas de las preguntas frecuentes).
- **Título y texto centrados en vertical:** en Coaching, en «Uma forma de estar descontraída» (Sobre) y en los desplegables al abrirse. La palabra lleva `padding-top:.23em` porque la tipografía Spartan deja ~0,27em por debajo de la línea base y ~0,04em por encima de las mayúsculas.
- **Verificación:** regresión de 36 rutas × 2 sin errores; 37 plantillas, CSS y JS desplegados con md5 comprobado.
- **Fichas · «Aplicações» en móvil:** pasan a ser un carrusel de deslizar con el dedo, como «Rótulos» de Camolas, con el título fijo arriba, la mano de aviso y las flechas. Fijada, la galería quedaba a media pantalla y la sección siguiente subía por debajo antes de soltarla. Ahora la sección termina con su margen normal (64 px en móvil). En escritorio no cambia.

## 17. Auditoría integral y sistema de diseño (2026-11-27)

**Método:**
- Script de auditoría (`hmtools/audit.js`) sobre las 36 rutas en escritorio (1440×900), tablet (820×1180) y móvil (390×844), con scroll completo antes de medir.
- Qué mide:
  - Fondos y paddings de cada sección.
  - Alineación con la rejilla.
  - Tipografía por papel: H1, H2, H3, antetítulo, texto, enlaces y botones.
  - Desbordes horizontales.
  - Solapes de texto, con un detector que tiene en cuenta recortes y opacidades.
  - Efectos que se quedan sin activar.
  - Imágenes rotas.
  - Errores JS.
  - Cabecera y footer.
- Además: hojas de capturas en tablet, capturas de los cambios, regresión `reg.js` y diff del HTML generado antes y después.

**Lo que ya estaba bien:**
- Ningún error JS ni desborde horizontal en las 108 combinaciones.
- Ningún efecto atascado.
- Cabecera (81/65 px) y footer idénticos en todas las páginas.
- 223 de 266 secciones con 126 px (64 px en móvil). Las demás son excepciones justificadas: cabeceras, franjas pegadas a su texto y galerías fijas.

**Problemas encontrados y corregidos en su origen:**
1. **Antetítulos:** 32 antetítulos en minúscula encima de un título, en Branding, Design Web, Camolas, fichas, landings y frases destacadas, frente a MAYÚSCULAS en el resto. Regla: el antetítulo que encabeza un título va en mayúsculas espaciadas, y las etiquetas siguen en frase normal. Se aplica en `comum.normalizar` (`estilos.normalizar_antetitulos`) y en los bloques del generador.
2. **Bloques de las fichas reutilizados en servicios y landings** (portfolio y vídeo): título a 66 px (escala de proyecto) en lugar de 58 px, y sin antetítulo. Ahora llevan la escala de sección y el antetítulo «Projetos».
3. **«Para quem» y «Conheça também»:** hueco entre columnas de hasta 140 px frente a los 120 px de la rejilla común, así que la columna derecha empezaba en otro punto. Ahora usan la rejilla común.
4. **Tablet ~768–840 px:** la columna lateral fija de listas y preguntas seguía fija con las columnas apiladas y se montaba sobre la lista (Avença, Coaching, landings, Branding y Design Web). El JS la marca `data-hm-stacked` y deja de ser fija.
5. **Tablet táctil · «Mais projetos»:** solo la primera tarjeta salía a color y con nombre. Ahora salen todas, como en el móvil.
6. **Home · Showreel:** el antetítulo quedaba debajo del titular gigante cuando este sube con el scroll. Ahora el antetítulo copia su desplazamiento, con 48 px constantes entre ambos.
7. **Botón de contacto de la home:** grosor 400 frente a 300 en el resto.
8. **«Conheça también»:** era la única lista sin animación de entrada.

**Sistema de diseño:**
- `fase2/gerador/estilos.py` es la fuente única de colores, espaciado, rejilla 5:7, escala tipográfica por papel y antetítulos. Los bloques importan de ahí.
- Bloque `:root` en `capa-fix/hm-boceto-fix.css` con los mismos tokens.
- Documentación en `SISTEMA-DE-DISENO.md`.

**Control final:**
- Nueva auditoría completa: sin incidencias, salvo un falso positivo (un enlace del blog que se parte en dos líneas).
- Regresión: 36 × 2 sin errores.
- 27 plantillas, CSS y JS desplegados, comprobados en las páginas servidas.

**No verificado:**
- La web publicada en un navegador real: el contenedor no llega al dominio, así que todo se ha renderizado en local con las mismas plantillas y el mismo CSS/JS, y en el servidor se han comprobado las marcas en el HTML servido.
- Fotos y logos que no hay en local (equipo de Sobre, logos de Serviços) y vídeos: el escaneo del servidor no encontró ninguna imagen rota.
- Safari/iOS y tablet en horizontal.
- Estados hover uno a uno.


## 18. Regresiones de Camolas y batería de pruebas (2026-11-27)

**Qué falló y por qué:**
1. **Camolas · «Rótulos e packaging» en el móvil:** los nombres largos («Grande Escolha · rótulo», «Monocasta Syrah · rótulo») salían en 2 líneas. El ajuste de tamaño de una línea solo se había hecho en los Trabajos de Branding y Design Web, y Rótulos seguía a 25 px. La auditoría no lo detectó porque no buscaba saltos de línea en los títulos de las galerías.
   - Arreglo: la letra se ajusta al ancho de la tarjeta (`min(24.96px, (78vw − 42px) / 12,4)`), en una línea: 21 px a 390 px y 19 px a 360 px.
2. **Camolas · «O site» bajaba muy rápido:** en la 8.ª ronda se pusieron capturas de página entera de adegacamolas.pt (Vinhos ~30.000 px en el móvil), pero cada página conservaba un tramo fijo del recorrido. Vinhos corría a 16× la velocidad del dedo en el móvil y a 8× en el PC; Experiências, a 3×.
   - Arreglo: el andamento se calcula ahora en `hm-boceto-fix.js` («O site») con la altura real de cada captura. Las tres van a velocidad constante (~3,5× el scroll, con arranque y frenada suaves) en móvil, tablet y PC.
   - La coreografía es la misma del diseño: la moldura crece, el título se va, cortinas entre páginas, dirección y barra rosa.
   - En el generador, la sección pasa a `data-hm-scrub`/`data-hm-sstep` (hook `camolas()` en `extras.py`) para que los efectos del diseño no la muevan dos veces.
3. **Migas en las páginas legales y el mapa del sitio (móvil):** son una lista (`nav > ol`, 18 px) que la regla de una línea no cubría: «Início — Política de Privacidade» salía en 2 líneas.
   - Además, en todas las migas del móvil el `overflow:hidden` cortaba el acento de las mayúsculas («INICIO», «POLITICA»).
   - Arreglo: la misma regla para la lista y entrelínea de 1,6.

**Batería de regresión (`scratchpad/hmtools/bateria.js`):** comprueba cada corrección pedida y se pasa antes de cada subida.
- **General, en las 36 rutas × móvil, tablet y PC:**
  - sin desbordamiento horizontal ni errores JS, sin imágenes rotas;
  - sin dos secciones seguidas con el mismo fondo (salvo un mismo capítulo o fotos pegadas a su texto);
  - franjas distintas entre sí y del fondo, con al menos 20 puntos RGB de diferencia;
  - migas en una línea y sin acentos cortados;
  - pósters en los vídeos del móvil.
- **Camolas:**
  - Rótulos en una línea (390 y 360 px);
  - «O site» ≤ 4× el scroll (móvil, tablet, PC y portátil);
  - sin la etiqueta de esquina en el móvil.
- **Branding y Design Web:** nombres de Trabajos en una línea (390 y 360 px).
- **Fichas:**
  - Aplicaciones/Rótulos con todas las imágenes a la misma altura (móvil y PC);
  - la sección siguiente no se sube;
  - «Mais projetos» a color con nombre y «Ver projeto» (móvil y tablet);
  - la leyenda de «O site»/«Filme» debajo del vídeo.
- **Desplegables:**
  - número y título alineados;
  - aire por encima y por debajo del texto;
  - efecto de escritura.
- **Filas de Coaching y Sobre:** título centrado con el texto.
- **Contacto:** dirección en 3 líneas con la misma letra.
- **Fotos ampliadas:** la X sin borde.
- **Cursor:** 12,5 px.
- **Servicios:** índice de Serviços con margen superior.
- **Administração Pública:** antetítulo en una línea.
- **Menú móvil:** los 6 proyectos principales primero.
- **Galerías:** todas continuas.
- **Cabeceras del móvil:** mismo tamaño en los títulos.
