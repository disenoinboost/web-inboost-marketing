# Optimización de /agencia-seo/ — registro

- **Fecha de trabajo:** 2026-10-09
- **Estado:** propuesta v1 pendiente de aprobación (no aplicada al original, no publicada en producción)

## Páginas

| Rol | URL | ID WordPress | Estado |
|---|---|---|---|
| Original de trabajo (laura) | https://laura.inboost.marketing/agencia-seo/ | 277 (page) | publish · modificada 2026-10-07 09:13:30 |
| Copia de revisión v1 | https://laura.inboost.marketing/?page_id=1848&preview=true (requiere sesión de WordPress) | 1848 (page) | draft · slug temporal `agencia-seo-revision` |
| Equivalente en producción | https://inboost.marketing/agencia-seo/ | — | indexada, canonical propia, último rastreo 2026-09-30 |
| URL final prevista | https://inboost.marketing/agencia-seo/ | — | sin cambio de slug |

Evidencia de equivalencia: mismo slug y mismo servicio. Además, el mapa de redirecciones de laura (`ib_redirects`) envía a `/agencia-seo/` las URL `servicios/posicionamiento-web`, `especialista-seo`, `agencia-especialista-seo`, `contratar-seo` y `optimizacion-on-page`.

Metadatos de identificación de la copia (no visibles): `_ib_review_of=277`, `_ib_review_version=v1`, `_ib_review_date=2026-10-09`, `_ib_review_status=pendiente de aprobación`.

Huella del original antes de cualquier cambio: `md5(post_content)=54b2500abd03f19208757717c7ad26c7` (89.529 bytes), `md5(_ib_faq)=ac89429ada5b269981e4076d89b2ae76`.

## Plantilla y configuración relevantes

- Divi 5.7.4 (D5 activo). Plantilla efectiva: Theme Builder "Global Inboost" (cabecera 34, pie 35, cuerpo = contenido de la página). Sin asignaciones por ID para esta página.
- Tema hijo: el JSON-LD de Yoast está desactivado (`wpseo_json_ld_output`). El tema imprime `FAQPage` desde la meta `_ib_faq` y `Service` desde `_ib_service`, con la meta description de Yoast como descripción.
- laura: `blog_public=0` (noindex global en desarrollo). La copia lleva además noindex/nofollow propio de revisión, que **no** se traslada al original.

## Datos

### Google Search Console (sc-domain:inboost.marketing, filtro página = https://inboost.marketing/agencia-seo/)

Extracción: 2026-10-09. Último día con datos: 2026-10-06.

| Periodo | Clics | Impresiones | CTR | Posición media |
|---|---|---|---|---|
| 2026-07-09 → 2026-10-06 (90 días) | 1 | 5.377 | 0,02 % | 80,0 |
| 2026-04-10 → 2026-07-08 (90 días previos) | 1 | 8.626 | 0,01 % | 72,7 |

- Desde el 2026-08-22 la URL pasa de unas 100 impresiones diarias a 0–3. El total del dominio se mantiene estable (5.000–7.000 diarias), así que la caída es propia de esta URL.
- Histórico mensual: junio de 2025 tuvo 58.667 impresiones (posición 48). Desde entonces el descenso es continuo.
- Consultas con más impresiones (90 días): agencia seo 621 (pos. 73,7) · contratar agencia seo 391 (89,6) · agencia de seo 351 (82,9) · agencias de seo 334 (78,6) · agencia marketing seo 229 (79,3) · empresa de seo 211 (82,5) · agencia seo marketing 165 (70,2) · servicios de seo 163 (91,7) · agencia seo b2b 143 (87,9) · agencia seo pamplona 118 (83,4).
- Marca: sin volumen relevante (solo consultas `site:` y "inboost marketing", con 3 impresiones en el periodo previo).
- Las filas por consulta suman 0 clics por anonimización. No se fuerza la cuadratura con el total.

### DataForSEO (Google Ads search volume, España, español, extracción 2026-10-09, meses 2025-09 → 2026-08)

| Consulta | Volumen medio | Nota |
|---|---|---|
| agencia seo / agencias seo | 4.400 | Google agrupa ambas. Meses recientes: 1.900–2.900. Septiembre de 2025 (14.800) es anómalo e infla la media |
| servicios seo | 720 | |
| agencia de seo | 590 | |
| empresa seo | 590 | |
| agencia posicionamiento web | 390 | |
| agencia posicionamiento seo | 390 | |
| empresa posicionamiento web | 260 | |
| servicios de seo | 260 | |
| agencia seo pamplona | 140 | intención local → /posicionamiento-web-pamplona/ |
| contratar agencia seo | 50 | |
| que es una agencia seo | 20 | |

Las variantes no se suman: comparten intención.

SERP "agencia seo" (2026-10-09):
- España, escritorio: pack local, páginas de servicio de agencias (agenciaseo.eu, millennialsconsulting.es, arimetrics.com, seo-madrid.com), comparativas de "mejores agencias SEO" (rodanet.com, pacoruben.com, sayonara.es) y una guía (sedestral.com).
- Pamplona, móvil: Sortlist en primera posición, PAA ("¿Qué es una agencia de SEO?", "¿Cuánto cuesta una agencia SEO?"), carrusel "Empresas" en el que aparece Inboost Marketing y páginas de servicio (themediapower.com, bigseo.com, dobuss.es).

### SE Ranking

No disponible: no hay conector de SE Ranking en esta sesión.

## Decisión

- **Intención:** comercial con investigación previa. Quien busca está comparando agencias y necesita saber qué hace una agencia SEO, cómo trabaja, qué pruebas tiene y cuánto cuesta.
- **Función:** página de servicio. Se conserva y se mejora; no se reenfoca ni se consolida.
- **Foco:** "agencia seo" (+ agencias seo, agencia de seo). Secundarias: empresa seo, servicios seo, agencia de posicionamiento web/seo, contratar agencia seo.
- **Temas que pertenecen a otras URL:** Pamplona → /posicionamiento-web-pamplona/; local → /agencia-seo-local/; consultoría → /consultor-seo/; auditoría → /auditoria-seo/.

## Cambios de la v1 frente al original

1. **H1:** pasa a "Agencia SEO que convierte búsquedas en…". Se mantiene el rotador.
2. **Texto del hero:** define la entidad: "Somos una agencia SEO de Pamplona que trabaja con empresas de toda España…".
3. **CTA:** se unifica en "Solicitar consultoría gratis" (el hero decía "Solicitar auditoría", etiqueta que usa el servicio de pago /auditoria-seo/).
4. **Sección 01:** incluye una definición clara de qué hace una agencia SEO.
5. **Sección 02:** enlace a /migraciones-seo/.
6. **Sección 03:** "Optimización continua" (ya cubierta por el proceso) se sustituye por "Autoridad y enlaces". La página prometía tres frentes (técnico, contenido y autoridad) y no listaba la autoridad. "SEO on page" pasa a "SEO on-page".
7. **Sección 05:** se retiran las cifras "+180 %" y "+65 %" ("media a 12 meses"), que no tienen fuente verificable. Se sustituyen por tres reseñas públicas de Google ya publicadas en producción y en /opiniones/, con enlaces a todas las reseñas y a /casos-de-exito/, y por la frase "nadie puede garantizar una posición".
8. **Nueva sección 06 "Qué exigir a una agencia SEO antes de firmar":**
   - Fuentes: /tarifas/ (desde 300 €/mes, sin permanencia con 30 días de aviso, informe mensual), FAQ de tarifas de producción (6 meses recomendados) y /nosotros/ (mismo interlocutor, alcance acordado).
   - Las secciones siguientes se renumeran.
9. **Especialidades:** se añaden Posicionamiento web en Pamplona y Migraciones SEO.
10. **FAQ:**
    - La respuesta de precio contradecía /tarifas/ ("no publicamos una tarifa cerrada"); ahora remite a ella.
    - Nueva pregunta "¿Trabajáis solo con empresas de Pamplona?".
    - Se ajusta la respuesta sobre IA.
    - La meta `_ib_faq` de la copia se regenera a partir del acordeón visible (11 preguntas).
11. **CTA final:** "¿Empezamos por una consultoría?".
12. **Yoast:**
    - Title: sin cambios ("Agencia SEO: posicionamiento web para empresas | Inboost").
    - Meta description nueva: "Agencia SEO para empresas de toda España: SEO técnico, contenidos y enlaces en un plan medido por solicitudes, no por visitas. Pide tu consultoría gratis."
    - Focus keyphrase: "agencia seo".

## Verificación

- Renderizado con Chromium del HTML servido por WordPress y de sus CSS/JS reales, a 1440 px y 390 px, en ambas páginas. Sin errores de JavaScript, sin desplazamiento horizontal y sin módulos ocultos.
- En las capturas se ocultan la barra de administración y el banner de cookies, y se emula `prefers-reduced-motion`.
- La vista previa sin sesión devuelve 404. La copia no está en el sitemap ni en los menús.
- Todos los enlaces internos apuntan a páginas publicadas.
- JSON-LD de la copia: FAQPage con 11 preguntas y Service con la nueva descripción.
- El original 277 sigue sin cambios.

## Pendiente o fuera de alcance

- No se pudieron consultar en vivo las fuentes de Google (developers.google.com está bloqueado por la red de la sesión).
- Observaciones globales, que no se han tocado:
  - El pie (plantilla 35) genera los H2 "in·boost" e "inboostinboost".
  - /tarifas/ incluye una "garantía de satisfacción de 60 días" y "resultado esperado Top 5 en 4–6 meses", que conviene alinear con el mensaje de no garantizar posiciones.
  - /nosotros/ muestra un texto provisional de foto ("Foto del equipo · 1200 × 1500 · alt: …").

## Aplicación tras el OK (alcance previsto)

Solo sobre la ID 277 de laura:

1. Copia de seguridad en metadatos de la 277 de `post_content`, `_ib_faq`, `_yoast_wpseo_metadesc` y `_yoast_wpseo_focuskw`.
2. Contenido Divi de la v1 aprobada.
3. Meta description y focus keyphrase.
4. `_ib_faq` de la v1.

Se mantienen ID, slug, estado, fecha, autor, title, robots y canonical de la 277. No se traslada el noindex de revisión. Después se limpia la caché de esa URL y se verifica el resultado. La publicación en producción requiere una autorización aparte.
