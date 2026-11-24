<?php
/**
 * Hortelã Magenta · boceto (kit de Claude Design)
 * Sirve las páginas del diseño (con todos los efectos) en sus URLs de WordPress.
 * Los HTML van en /wp-content/themes/divi-child/hm-paginas/. Si falta un archivo, se muestra la página de Divi.
 * Para ver o editar la versión de Divi de una página (con sesión iniciada), añade ?divi a la URL.
 *
 * Fase 2 (2026-11-24): mapa de URL en hm-rutas.php (páginas, redirecciones 301, barra final canónica de cada URL),
 * 404 propia (hm-paginas/404.html), sitemap.xml generado a partir del mapa, formulario de contacto (hm-formulario.php)
 * y noindex en cualquier dominio que no sea el de producción.
 */
require_once get_stylesheet_directory() . '/hm-boceto-dist.php';
require_once get_stylesheet_directory() . '/hm-rutas.php';
if ( is_readable( get_stylesheet_directory() . '/hm-formulario.php' ) ) {
	require_once get_stylesheet_directory() . '/hm-formulario.php';
}

/** Dominio de producción: fuera de él (p. ej. hortelamagenta.inboost.marketing) todo va con noindex. */
function hm_es_produccion() {
	$h = strtolower( (string) ( $_SERVER['HTTP_HOST'] ?? '' ) );
	return in_array( $h, array( 'hortelamagenta.pt', 'www.hortelamagenta.pt' ), true );
}
add_action( 'send_headers', function () {
	if ( ! hm_es_produccion() ) {
		header( 'X-Robots-Tag: noindex, nofollow', true );
	}
} );

/** Sitemaps de WordPress desactivados: el sitemap del sitio es /sitemap.xml (páginas del mapa de URL). */
add_filter( 'wp_sitemaps_enabled', '__return_false' );
add_filter( 'robots_txt', function ( $out ) {
	return rtrim( $out ) . "\nSitemap: " . home_url( '/sitemap.xml' ) . "\n";
}, 20 );

function hm_redirect( $to, $code = 301 ) {
	$qs = (string) parse_url( $_SERVER['REQUEST_URI'], PHP_URL_QUERY );
	if ( $qs && false === strpos( $to, '?' ) && 0 === strpos( $to, '/' ) ) {
		$to .= '?' . $qs;
	}
	if ( ! defined( 'DONOTCACHEPAGE' ) ) define( 'DONOTCACHEPAGE', true );
	wp_redirect( 0 === strpos( $to, '/' ) ? home_url( $to ) : $to, $code, 'Hortela Magenta' );
	exit;
}

/** Sirve un paquete de hm-paginas/ (versión desempaquetada) con su capa de correcciones. */
function hm_servir( $archivo, $status = 200 ) {
	if ( ! defined( 'DONOTROCKETOPTIMIZE' ) ) define( 'DONOTROCKETOPTIMIZE', true );
	if ( 200 !== $status && ! defined( 'DONOTCACHEPAGE' ) ) define( 'DONOTCACHEPAGE', true );
	status_header( $status );
	header( 'Content-Type: text/html; charset=utf-8' );
	if ( ! hm_es_produccion() ) {
		header( 'X-Robots-Tag: noindex, nofollow', true );
	}
	// Versión desempaquetada (hm-boceto-dist.php): HTML normal + archivos estáticos, la cachea WP Rocket sin optimizarla.
	// ?paquete (con sesión) sirve el paquete original para comparar.
	$dist = ( isset( $_GET['paquete'] ) && is_user_logged_in() ) ? false : hm_dist_get( $archivo );
	if ( $dist ) {
		$dist = hm_fix_inject( $dist );
		global $wp_query;
		if ( $wp_query && 200 === $status ) {
			$wp_query->is_404 = false; // rutas sin página en WP: que WP Rocket también las cachee
		}
		echo $dist;
		exit;
	}
	if ( ! defined( 'DONOTCACHEPAGE' ) ) define( 'DONOTCACHEPAGE', true );
	$html = file_get_contents( $archivo );
	// Quitar la pantalla de carga del exportador (las letras grandes "hm" y el texto "Unpacking...").
	$html = preg_replace( '#<div id="__bundler_thumbnail">.*?</div>#s', '<div id="__bundler_thumbnail"></div>', $html, 1 );
	$fix = '<style>#__bundler_loading{display:none!important}#__bundler_thumbnail{background:#FFFFFF}html.hm-pt-in #__bundler_thumbnail,html.hm-pt-in body{background:#1C1B23!important}</style>'
		. '<script>try{if(sessionStorage.getItem("hm-pt")==="1")document.documentElement.classList.add("hm-pt-in")}catch(e){}</script>';
	$html = preg_replace( '#</head>#i', $fix . '</head>', $html, 1 );
	echo $html;
	exit;
}

/** sitemap.xml a partir del mapa de URL (solo páginas indexables con paquete). */
function hm_sitemap_xml() {
	$r   = hm_rutas();
	$dir = get_stylesheet_directory() . '/hm-paginas/';
	$out = '<?xml version="1.0" encoding="UTF-8"?>' . "\n" . '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
	foreach ( $r['paginas'] as $ruta => $f ) {
		if ( in_array( rtrim( $ruta, '/' ), $r['noindex'], true ) || ! is_readable( $dir . $f ) ) {
			continue;
		}
		$loc  = home_url( '/' . $ruta );
		$loc  = '' === $ruta ? home_url( '/' ) : ( '/' === substr( $ruta, -1 ) ? trailingslashit( $loc ) : untrailingslashit( $loc ) );
		$out .= '  <url><loc>' . esc_url( $loc ) . '</loc><lastmod>' . gmdate( 'Y-m-d', filemtime( $dir . $f ) ) . '</lastmod></url>' . "\n";
	}
	$out .= '</urlset>' . "\n";
	if ( ! defined( 'DONOTCACHEPAGE' ) ) define( 'DONOTCACHEPAGE', true );
	status_header( 200 );
	header( 'Content-Type: application/xml; charset=utf-8' );
	echo $out;
	exit;
}

add_action( 'template_redirect', function () {
	if ( is_admin() || wp_doing_ajax() || isset( $_GET['et_fb'] ) || is_preview() || isset( $_GET['preview'] ) ) {
		return;
	}
	if ( isset( $_GET['divi'] ) && is_user_logged_in() ) {
		return;
	}
	if ( function_exists( 'is_robots' ) && is_robots() ) {
		return;
	}
	if ( function_exists( 'is_favicon' ) && is_favicon() ) {
		return;
	}
	$r    = hm_rutas();
	$dir  = get_stylesheet_directory() . '/hm-paginas/';
	$path = rawurldecode( (string) parse_url( $_SERVER['REQUEST_URI'], PHP_URL_PATH ) );
	$path = preg_replace( '#/{2,}#', '/', $path );
	$k    = trim( $path, '/' );
	$slash = '' !== $k && '/' === substr( $path, -1 );

	if ( 'sitemap.xml' === $k ) {
		hm_sitemap_xml();
	}

	// páginas del mapa: barra final canónica
	$canon = null;
	if ( isset( $r['paginas'][ $k ] ) ) {
		$canon = $k;
	} elseif ( isset( $r['paginas'][ $k . '/' ] ) ) {
		$canon = $k . '/';
	}
	if ( null !== $canon && is_readable( $dir . $r['paginas'][ $canon ] ) ) {
		$want_slash = '/' === substr( $canon, -1 );
		if ( '' !== $k && $want_slash !== $slash ) {
			hm_redirect( '/' . $canon );
		}
		hm_servir( $dir . $r['paginas'][ $canon ] );
	}

	// redirecciones 301
	if ( isset( $r['redirects'][ $k ] ) ) {
		hm_redirect( $r['redirects'][ $k ] );
	}
	foreach ( $r['prefixos'] as $p => $to ) {
		if ( 0 === strpos( $k . '/', $p ) ) {
			hm_redirect( $to );
		}
	}
	// medios de la web anterior (Kirby, /media/...) -> copia local en hm-media, si existe
	if ( 0 === strpos( $k, 'media/' ) && preg_match( '#\.(jpe?g|png|gif|webp|mp4)$#i', $k ) ) {
		$rel = 'hortelamagenta.pt/' . preg_replace( '#\.(jpe?g|png)$#i', '.webp', $k );
		if ( file_exists( hm_media_dir() . '/' . $rel ) ) {
			hm_redirect( hm_media_url() . '/' . $rel );
		}
	}

	// cualquier otra URL pública: 404 con la página del diseño (también entradas, adjuntos, archivos y feeds de WP)
	if ( is_readable( $dir . '404.html' ) && ( is_404() || is_singular() || is_archive() || is_feed() || is_search() || is_attachment() || '' !== $k ) ) {
		hm_servir( $dir . '404.html', 404 );
	}
}, 0 );

/** Correcciones propias sobre el boceto (assets/hm-boceto-fix.css y .js): se añaden al servir cada página, así sobreviven a nuevas exportaciones de hm-paginas. */
function hm_fix_inject( $html ) {
	$dir  = get_stylesheet_directory() . '/assets/';
	$uri  = wp_make_link_relative( get_stylesheet_directory_uri() ) . '/assets/';
	// Entradilla curta no telemóvel (Branding, Design Web): script em linha logo a seguir ao desenho, antes de o runtime o montar (2026-11-05)
	if ( is_readable( $dir . 'hm-entradilla-movil.html' ) && false !== ( $p = stripos( $html, '</x-dc>' ) ) ) {
		$html = substr_replace( $html, file_get_contents( $dir . 'hm-entradilla-movil.html' ), $p + 7, 0 );
	}
	$tags = '';
	// Favicon de hortelamagenta.pt (2026-11-05)
	$tags .= hm_favicon_tags();
	if ( is_readable( $dir . 'hm-boceto-fix.css' ) ) {
		$tags .= '<link rel="stylesheet" href="' . esc_attr( $uri . 'hm-boceto-fix.css?v=' . filemtime( $dir . 'hm-boceto-fix.css' ) ) . '">';
	}
	if ( is_readable( $dir . 'hm-boceto-fix.js' ) ) {
		$tags .= '<script src="' . esc_attr( $uri . 'hm-boceto-fix.js?v=' . filemtime( $dir . 'hm-boceto-fix.js' ) ) . '" defer></script>';
	}
	return $tags ? preg_replace( '#</head>#i', $tags . '</head>', $html, 1 ) : $html;
}

/** Favicon de hortelamagenta.pt (2026-11-05). ?v= obriga o navegador a ir buscar o ícone novo. */
function hm_favicon_tags() {
	$uri = wp_make_link_relative( get_stylesheet_directory_uri() ) . '/assets/';
	$v   = '?v=20261105b';
	return '<link rel="icon" href="/favicon.ico' . $v . '" sizes="32x32">'
		. '<link rel="icon" type="image/svg+xml" href="' . esc_attr( $uri . 'favicon.svg' . $v ) . '">'
		. '<link rel="apple-touch-icon" href="' . esc_attr( $uri . 'apple-touch-icon.png' . $v ) . '">'
		. '<link rel="mask-icon" href="' . esc_attr( $uri . 'safari-mask-icon.svg' . $v ) . '" color="#1C1B23">';
}
/* páginas que o WordPress pinta (artigos, categorias, autor, 404): o mesmo favicon */
add_action( 'wp_head', function () { if ( ! get_option( 'site_icon' ) ) { echo hm_favicon_tags() . "\n"; } }, 2 );
