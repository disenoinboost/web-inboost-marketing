# Inboost: optimización de URLs en laura.inboost.marketing

Laura (Inboost) pide optimizar una URL a la vez con su "prompt maestro". Trabaja de forma autónoma, sin preguntas de descubrimiento. Este archivo reúne lo ya verificado para no redescubrirlo. Registro de cada URL trabajada: `optimizaciones/<slug>.md`.

## Preferencias de Laura

- **Copia de revisión:** página nueva con slug `propuesta-<slug-original>` (ej. `/propuesta-agencia-seo/`) y estado **privado**, para que tenga URL real visible solo con sesión. Además: Yoast noindex/nofollow y metas `_ib_review_of`, `_ib_review_version`, `_ib_review_date`, `_ib_review_status`. Nunca tocar el original antes del OK.
- **Excepción:** /agencia-seo/ (277) ya tiene su copia v1 como borrador en la ID 1848 (`?page_id=1848&preview=true`). No cambiarla salvo que lo pida.
- **Entrega:** primero los enlaces (actual · propuesta · editar) con la URL de la propuesta bien visible y el acceso que requiere. Después la comparativa breve y la frase de cierre del prompt.
- **Ritmo:** pocas llamadas y agrupadas, avisos cortos de avance. No hacer esperar con investigación redundante.

## Sitio laura (entorno de trabajo)

- **Software:** WordPress 7.1.3 · PHP 8.5 · Divi 5.7.4 (D5) con tema Divi Child · Yoast 28.6 · WP Rocket · Imagify · Complianz · Business Reviews Bundle · Novamira Pro.
- **Indexación:** `blog_public=0` (noindex global). La producción es inboost.marketing.
- **Theme Builder:**
  - "Global Inboost" (36) por defecto: cabecera 34, pie 35, cuerpo = contenido.
  - Plantillas específicas: entradas (293), legales (295, ID 280-282), categorías (364) y 404 (765).
- **Tema hijo (`inc/inboost-seo-pages.php`):**
  - El JSON-LD de Yoast está desactivado.
  - Imprime `FAQPage` desde la meta `_ib_faq` (JSON `[[pregunta, respuesta_html], …]`) y `Service` desde `_ib_service`, con la meta description de Yoast como descripción.
  - Al cambiar el FAQ visible, regenerar `_ib_faq` desde el acordeón con PHP y `wp_slash(wp_json_encode(...))`.
- **Redirecciones:** opción `ib_redirects` (ruta → destino); conviene leerla para ver equivalencias con producción. URL retiradas: opción `ib_gone`.
- **Estilos:** `assets/inboost-pages.css` define las clases reutilizables, que se asignan en Divi → Atributos HTML → Class:
  - `ib-crumbs`, `ib-rot2` (rotador de 4 `<em>`), `ib-serp`, `ib-dots` (señales), `ib-rows`/`ib-row` (filas editoriales).
  - `ib-links` (lista con flecha), `ib-reviews` (tarjetas de reseña), `ib-incl-grid` (3 columnas con check; usar `<h3>` para mantener la jerarquía), `ib-chips`, `ib-check`, `ib-steps`.
  - `<em class="ib-fill">` para la palabra en lima, `ib-scrub` para el titular que se ilumina.
- **Presets Divi habituales:**

| Elemento | Preset |
|---|---|
| Sección | `e294226a-59ab-425d-8f49-278abda6afd9` |
| Fila | `f68c440d-b059-45a3-8acc-ab979e43140a` |
| Eyebrow `<em>NN</em>Texto` | `3c17c8a5-92ff-47cf-ba02-200b69e769ac` |
| Texto | `3fba6898-406a-4c5a-8535-35d78d46f3b8` |
| Texto pequeño | `0c53e329-5509-48e7-9ce0-92379b2cb41a` |
| H2 | `b0e7a9a6-f330-4079-954f-7d4c5c54105e` |
| H1 de hero / CTA | `6e25ce9f-5bfe-48d7-9e51-8bc38e301af3` |
| H3 de fila | `3ff2bec7-2f59-4cf5-a0d0-31ee89fdacd4` |
| Botón principal | `1066b235-542e-482e-95dc-8b49c9c885d9` |
| Botón secundario | `524073b3-50b5-4b2f-b99a-4cfdd42cc25e` |

- **Colores globales:**

| Uso | Variable |
|---|---|
| Línea | `var(--gcid-b9d8c99d-bcc6-4e22-b075-06517950484c)` |
| Fondo | `var(--gcid-b719a11a-75ca-4dab-91c3-2dfd7a0094e2)` |
| Atenuado | `var(--gcid-d87c0bee-40fb-4130-86cf-570b00706c7e)` |
| Lima | `var(--gcid-primary-color)` |

- **Identidad Inboost 2026:** Inter · #9EFF00 · #0A0F1D · #161B2A · #2E3548 · #FFFFFF.

## Hechos de negocio verificados (se pueden publicar)

- Inboost tiene sede en Pamplona y trabaja con empresas de toda España en remoto (FAQ de portada).
- **CTA del sitio:** "Solicitar consultoría gratis" → `/contacto/`. "Solicitar auditoría" es del servicio de pago /auditoria-seo/; no mezclarlos.
- **Tarifas** (/tarifas/ en laura y producción):
  - SEO web desde 300 €/mes; SEO local desde 250 €/mes.
  - Sin permanencia, con 30 días de aviso.
  - En producción se recomiendan 6 meses mínimo.
- **/nosotros/:** "Acordamos el alcance antes de empezar", el mismo interlocutor de principio a fin y datos de las propias cuentas del cliente.
- **Reseñas públicas de Google** (mismas en producción y /opiniones/):
  - JRC Proyectos (2021), Pedro Miguel Arnedo (2022) y Silvia Cifuentes (2022).
  - Enlace a todas: `https://search.google.com/local/reviews?placeid=ChIJ-Sq4NfWSUA0RHKCMNUItTPI`
- **/casos-de-exito/** (clientes que autorizan): Fisioterapia Lepol, Autoescuela San Andrés, Shiva & Shakti, Inniauto, Sparta Sport Center, Centro Albea, Laverde y Teja, Clínica veterinaria Gous, Ventanas Varona, Muebles Molinero Cózar, Novophysio.

## No usar como hechos

- Contadores "+180 % visitas" y "+65 % solicitudes · media a 12 meses" (maqueta sin fuente).
- Cifras de /nosotros/ (212 clientes, 14 años, 6 profesionales): página con elementos provisionales.
- Garantías de /tarifas/ ("devolvemos el 100 %", "Top 5 en 4-6 meses").
- No reintroducir Kit Digital, Kit Consulting ni la vacante de especialista SEO (páginas 495 y 503 en borrador, ya retiradas).

## Conectores y datos

- **GSC:** propiedad `sc-domain:inboost.marketing`. Datos con unos 3 días de retraso; comprobar el último día con `dimensions:["date"]`. Filtrar la página con `equals` y la URL de producción completa.
- **DataForSEO:**
  - `location_code 2724`, `language_code "es"`.
  - En modo AI devuelve como mucho 10 palabras clave por petición: partir las listas.
  - Google Ads agrupa variantes (agencia seo/agencias seo); no sumarlas.
  - Septiembre de 2025 tiene un pico anómalo en todos los volúmenes.
- **SE Ranking:** sin conector en estas sesiones.
- **Novamira laura:**
  - `novamira/divi-get-content` recorta los atributos de más de unos 2.000 caracteres ("…[truncated]"; p. ej. el `css.freeForm` de secciones con animaciones). Antes de reescribir un módulo así, leer el valor completo con PHP (`parse_blocks`).
  - `create-post` no acepta metas `_et_pb_*`.
  - Escribir Divi solo con `divi-set-content`, `divi-add-module` o `divi-edit-module`.
- **Red de la sesión:** el contenedor puede no llegar a laura.inboost.marketing, inboost.marketing ni developers.google.com (proxy 403). Leer páginas desde el servidor con `novamira/execute-php` + `wp_remote_get`.

## Flujo rápido (orden y llamadas agrupadas)

1. **En paralelo:**
   - Novamira: ID, metas, plantilla y `divi-get-content include_attrs` del original.
   - Yoast `get-post-seo`.
   - GSC: totales de la página en los dos periodos de 90 días, consultas e histórico diario.
   - DataForSEO: volumen (≤10 por llamada) y SERP de España.
   - `execute-php`: título, H y metas de producción con `wp_remote_get`.
2. **Decidir** el enfoque y redactar los cambios sobre el árbol real con un script Python. Partir del JSON de `divi-get-content`, guardado en el scratchpad.
3. **Crear la copia:** `create-post` (página, `status: private`, `slug: propuesta-<slug>`, metas `_ib_*`).
   - **Opción rápida:** `divi-create-library-item` del original (página entera) → `divi-apply-library-item` en la copia → `divi-delete-library-item`. Después, solo `divi-edit-module`/`divi-add-module` en los módulos que cambian.
   - **Alternativa:** `divi-set-content` con las primeras secciones y `divi-add-module` por sección.
4. **Configurar:** Yoast de la copia (title, description, keyword, noindex/nofollow) y `_ib_faq` regenerado con PHP.
5. **Verificar:**
   - `tools/fetch_html.php` (y `tools/bundle_assets.php` si la red está bloqueada) → `tools/unpack.py` → `node tools/render.js <dir> orig=<url> prop=<url>` → `tools/compare.py`.
   - Comprobar: ancho del documento = ventana, 0 errores y 0 módulos ocultos.
   - Con PHP: sin sesión responde 404, fuera del sitemap y de los menús, enlaces internos publicados y huella `md5` del original sin cambios.
6. **Registrar y entregar:** escribir `optimizaciones/<slug>.md`, hacer commit y entregar.
