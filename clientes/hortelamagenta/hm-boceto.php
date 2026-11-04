<?php
/**
 * Hortelã Magenta · boceto (kit de Claude Design)
 * Sirve las 10 páginas del diseño tal cual (con todos los efectos) en sus URLs de WordPress.
 * Los HTML van en /wp-content/themes/divi-child/hm-paginas/. Si falta un archivo, se muestra la página de Divi.
 * Para ver o editar la versión de Divi de una página, añade ?divi a la URL.
 */
require_once get_stylesheet_directory() . '/hm-boceto-dist.php';

add_action( 'template_redirect', function () {
	if ( is_admin() || wp_doing_ajax() || isset( $_GET['et_fb'] ) || isset( $_GET['divi'] ) || isset( $_GET['preview'] ) || is_preview() ) {
		return;
	}
	$hm_paginas = array(
		''                          => 'home.html',
		'inicio'                    => 'home.html',
		'servicos'                  => 'servicos.html',
		'servicos/branding'         => 'branding.html',
		'servicos/design-web'       => 'design-web.html',
		'projetos'                  => 'projetos.html',
		'projetos/camolas'          => 'camolas.html',
		'sobre'                     => 'sobre.html',
		'blog'                      => 'blog.html',
		'blog/quanto-custa-um-site' => 'artigo.html',
		'quanto-custa-um-site'      => 'artigo.html',
		'contacto'                  => 'contacto.html',
	);
	$ruta = trim( (string) parse_url( $_SERVER['REQUEST_URI'], PHP_URL_PATH ), '/' );
	if ( ! isset( $hm_paginas[ $ruta ] ) ) {
		return;
	}
	$archivo = get_stylesheet_directory() . '/hm-paginas/' . $hm_paginas[ $ruta ];
	if ( ! is_readable( $archivo ) ) {
		return;
	}
	if ( ! defined( 'DONOTROCKETOPTIMIZE' ) ) define( 'DONOTROCKETOPTIMIZE', true );
	status_header( 200 );
	header( 'Content-Type: text/html; charset=utf-8' );
	// Versión desempaquetada (hm-boceto-dist.php): HTML normal + archivos estáticos, la cachea WP Rocket sin optimizarla.
	// ?paquete sirve el paquete original para comparar.
	$dist = isset( $_GET['paquete'] ) ? false : hm_dist_get( $archivo );
	if ( $dist ) {
		global $wp_query;
		if ( $wp_query ) {
			$wp_query->is_404 = false; // rutas sin página en WP (p. ej. /blog/quanto-custa-um-site/): que WP Rocket también las cachee
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
}, 0 );