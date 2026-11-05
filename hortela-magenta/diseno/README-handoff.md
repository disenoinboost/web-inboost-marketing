# Handoff: web Hortelã Magenta → WordPress + Divi 5

## Overview
The site has 10 pages: Home, Serviços, Branding, Design Web, Projetos, Projeto (Camolas), Sobre, Blog, Artigo and Contacto.
- **Desktop:** has every effect: cursor, page transitions, pinned blocks, galleries, lightbox, testimonials, team, menu and filters.
- **Mobile:** has its own version, up to 767 px.
- **Performance:** layout reads are cached, the cursor does not run on touch screens and headers fade with opacity. Details below.

The site is already live as a mockup at https://hortelamagenta.inboost.marketing/ via `wordpress/` (each page served as-is). The job now is to turn it into the final site in Divi 5 with editable modules, keeping the design and effects identical.

## About the design files
- **`fuente/*.dc.html` — design references.** Each one is an HTML prototype with a logic class: `class Component extends DCLogic`, which works like a React class component; `renderVals()` provides the template values. They show exactly the intended look and behavior, but they are not code to copy into WordPress: they depend on `support.js`, the runtime that renders `{{ }}` holes, `<sc-for>` and `<sc-if>`.
  - In Divi, rebuild the **markup** with modules (Section / Row / Column / Text / Image / Code) and the same inline styles or equivalent classes.
  - Turn each page's logic class into **plain JS**: one file per page or one shared file, loaded from the child theme. See "Logic to migrate" below.
- **`fuente/hm-fx-servico.js` and `fuente/hm-fx-projeto.js` — ready for production.** They are vanilla JS with no dependencies, so they can be loaded as-is. They activate on `data-*` attributes: if a Divi module has the same attributes and structure, the effect works.
- **`fuente/hm-lightbox.js` and `fuente/hm-perf.js` — ready for production.** Also vanilla JS, loaded as-is.
- **`fuente/hm-movil.css` — ready for production.** Plain CSS for mobile, loaded as-is.

## Fidelity
**High-fidelity.** Final colors, type, spacing and animations; recreate them pixel-perfect. Every rule (sizes, weights, spacing, behavior on each block) is in `REGLAS-DEL-PROYECTO.md` and is binding: read it before you start.

## Pages (source file → WordPress URL)
| File | URL | WP export |
|---|---|---|
| Home Hortela Magenta v3.dc.html | / | home.html |
| Servicos.dc.html | /servicos/ | servicos.html |
| Branding.dc.html | /servicos/branding/ | branding.html |
| Design-Web.dc.html | /servicos/design-web/ | design-web.html |
| Projetos.dc.html | /projetos/ | projetos.html |
| Projeto.dc.html | /projetos/camolas/ | camolas.html |
| Sobre.dc.html | /sobre/ | sobre.html |
| Blog.dc.html | /blog/ | blog.html |
| Artigo.dc.html | /blog/quanto-custa-um-site/ | artigo.html |
| Contacto.dc.html | /contacto/ | contacto.html |

Every page shares the same header (with the mega menu and the Projetos dropdown), the mobile menu (`[data-mobile]`), the footer, the progress bar (`[data-progress]`), the page transition (`[data-pt]`) and the pink cursor. Blocks and their behavior are in `REGLAS-DEL-PROYECTO.md`; the exact markup is in each `.dc.html`, labelled with `data-screen-label`.

## Design tokens
- **Colors:**
  - Ink: `#1C1B23`.
  - Background: white `#FFFFFF`, `#FAFAF8` and greys `#e8eced` / `#f6f7f8` / `#dde3e7`.
  - Text: `#4A4743`; muted `#6E6A63` / `#8A857D`; footer `#9C978E`.
  - Pink accent: `#D82E87`, for the accent only (dash, underline, cursor, progress, asterisks), never for numbers.
- **Type:** Google Fonts **«Spartan»** (not League Spartan), weights 100/200/300/400 only.
  - Headings ≥40 px weight 100; 22–39 px weight 200; body 300; bold 400.
  - Body text 18 px / 1.5. 16 px only for captions, counters, dates and footer.
  - The weight of large headings is set in CSS with `data-fw="200@1372:100"` (base weight, then another weight from that viewport width). The rules are in the `<style>` of each helmet.
- **Spacing:** `--sp-block` 126 / 84 px (mobile 64 px), `--sp-title` 64 / 40 px (mobile 32 px), `--sp-hdr` = `max(clamp(112px, 100vh − 560px, 150px), 27vh − 44px)`.
- **Radii:** 0 on almost everything; circles for the cursor, dots and the gallery «+» button.

## Interactions and behavior
See `REGLAS-DEL-PROYECTO.md` (transitions, cursor, pinned blocks, galleries, lightbox, testimonials, team, forms, filters, mobile). Key parameters:
- **Page transition:** ink panel from a random side (never the same as last time), `.875s ease`, white logo centred. On the new page it follows the same direction and the visible blocks move with it (10vh vertical / 6vw horizontal).
- **Heading entrance:** lines rise with a fade, `1.5s`, delay `.7s`.
- **Cursor:** pink ball. On links and buttons, layers with `mix-blend-mode: difference` + `screen` on light backgrounds and `lighten` on dark. The tone comes from `data-cursor-bg="light|dark|solid"` on each block (not `data-cursor`, which is the large cursor's label). On touch screens no cursor listener is registered.
- **Horizontal gallery (`data-lp`):** each panel pauses centred before moving on.
- **Lightbox (`data-lb`):** drag carousel; a click without dragging opens the photo.
- **Mobile (up to 767 px):** everything in `hm-movil.css`. The pinned blocks that don't work on mobile are redesigned there (described at the end of the rules).

## Performance (already applied in the design — keep it in Divi)
- **No double render.** `narrow` starts at `innerWidth < 900` in the initial state, and the clock comes pre-filled.
- **Idempotent helmet scripts.** They carry a flag in `window` (`__hmS0`, `__hmS1`, `__hmS2`). The `[data-fw]` script was removed and replaced by CSS.
- **Cached reads.**
  - `this.rc(el)` caches positions relative to the document; elements inside a sticky or fixed block are read at the start of the frame, before any write. `this.lp(el,'offsetHeight')` caches sizes.
  - Everything is recalculated only on `resize`, `load`, `fonts.ready` or via the `ResizeObserver` on `body`.
  - In `hm-fx-*.js` the same applies with `R(el)` and `Rpre()`.
- **Cursor without layout reads.** No `getComputedStyle` or `elementsFromPoint`: it reads `data-cursor-bg`.
- **Header without color animation.** Layers `[data-hbg="l|d|s"]` fade with opacity instead of animating `background`. Color transitions are ≤ .2 s, `grid-template-rows` / `filter` transitions ≤ .3 s.
- **Contrast.** The words that light up on scroll start at `#6E6A63` (≥ 4.5:1 on a light background).
- **ARIA.** Tab panels are `<div role="tabpanel">`.
- **Loading.**
  - Images for menus and moving galleries use `data-src`, loaded by `hm-perf.js`.
  - Videos use `preload="none"`.
  - Keep the attributes `data-src`, `data-autoplay`, `data-header`, `data-mobile` and `data-wake`.
- **WP Rocket.** Exclude `hm-fx-*.js`, `hm-perf.js` and `hm-lightbox.js` from "Delay JS" and from combining/minifying, if anything breaks. Don't apply WP Rocket lazy load to images that have `data-src`.

## Logic to migrate (from the DCLogic class to plain JS)
Each page has the same base, with methods in its class:
- **Shared:** `frame()` loop (rAF), cursor, header (hide on scroll down / tone over dark blocks), mega menu, mobile menu (`setMobile`), progress bar, page transition, intro animations, reveals, marquee, counters.
- **Home:** showreel that grows, project panels (`fp`), testimonials (`setupOp` / `opTick`, 4 lines with «Ler mais», scrollable tabs), brand wall, services (`svcHit`).
- **Sobre:** team (`tmPick` / `tmDur`, auto-advance, pause on hover over the strip), Hortelanices (drag + lightbox).
- **Projetos and Blog:** filters (floating bar).
- **Artigo:** index with reading progress.
- **Contacto:** form.

**Important:** some methods are only called from others (e.g. `ring` in Contacto, `tmPick` and `tmDur` in Sobre). When you move code around, check that none get lost.

## Assets
- **Photos and videos:** `https://hortelamagenta.pt/media/pages/projetos/…`, built as `const IMG = 'https://hortelamagenta.pt/media/pages/projetos/'` + literal path, or as a full URL.
  - Don't change how these URLs are built.
  - For production, upload them to the WordPress Media Library.
- **Images from the old site (Sobre / Hortelanices and some testimonials):** `https://nostalgia.hortelamagenta.pt/old/wp-content/uploads/…` with `referrerpolicy="no-referrer"`. Better to upload them to the Media Library.
- **Logo and local images:** `assets/logo-hm.svg` and `assets/` (client logos, site screenshots).

## Files
- `fuente/` — design source (10 `.dc.html` files, `support.js`, `hm-fx-servico.js`, `hm-fx-projeto.js`, `hm-perf.js`, `hm-lightbox.js`, `hm-movil.css`, `assets/`).
- `REGLAS-DEL-PROYECTO.md` — every design and behavior rule (in Spanish). **Binding.**
- `wordpress/` — the current mockup: `hm-paginas/*.html` (each page self-contained) + `hm-boceto.php` (serves them on their URLs) + `LEEME.txt`.

To view the source in a browser, open any `fuente/*.dc.html` from a local server (e.g. `npx serve fuente`) so the relative paths resolve.
