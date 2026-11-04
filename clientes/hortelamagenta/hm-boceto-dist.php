<?php
/**
 * Hortelã Magenta · boceto desempaquetado (rendimiento)
 *
 * Los HTML de hm-paginas/ son paquetes autoextraíbles de Claude Design: ~0,5 MB con React, el runtime,
 * las fuentes y algunas imágenes en base64 que el navegador descomprime en blobs y monta antes de pintar.
 * Aquí se desempaquetan una vez en el servidor:
 *   hm-paginas/dist/<pagina>.html   el mismo documento que montaba el cargador, sin el paso de descompresión
 *   hm-paginas/dist/a/<hash>.<ext>  React, runtime, fuentes e imágenes como archivos estáticos (compartidos
 *                                   entre páginas y con caché de un año: el nombre cambia si cambia el contenido)
 * Las imágenes y vídeos enlazados de hortelamagenta.pt (y nostalgia./adrepes.pt) se copian a
 * uploads/hm-media/ (las JPG/PNG como WebP) con hm_media_mirror(); mientras falte alguna, la página
 * sigue usando las URL remotas.
 * Si se sustituye un HTML de hm-paginas/, su versión dist se regenera sola y se vacía la caché de WP Rocket.
 */
defined( 'ABSPATH' ) || exit;

const HM_DIST_VER = 2;

function hm_dist_dir() {
	return get_stylesheet_directory() . '/hm-paginas/dist';
}
function hm_dist_url() {
	return wp_make_link_relative( get_stylesheet_directory_uri() ) . '/hm-paginas/dist';
}
function hm_media_dir() {
	$u = wp_get_upload_dir();
	return $u['basedir'] . '/hm-media';
}
function hm_media_url() {
	$u = wp_get_upload_dir();
	return wp_make_link_relative( $u['baseurl'] ) . '/hm-media';
}

/** Orígenes remotos cuyos medios se copian al servidor (ruta local: hm-media/<host><ruta>). */
function hm_media_prefixes() {
	return array(
		'https://hortelamagenta.pt/media/',
		'https://nostalgia.hortelamagenta.pt/old/wp-content/',
		'https://www.adrepes.pt/wp-content/uploads/',
		'https://www.minhaterra.pt/wst/images/',
		'https://www.coprate.pt/images/',
	);
}

/** manifest, ext_resources y template de un paquete. */
function hm_bundle_parts( $html ) {
	$get = static function ( $type ) use ( $html ) {
		$open = '<script type="__bundler/' . $type . '">';
		$a    = strpos( $html, $open );
		$b    = false === $a ? false : strpos( $html, '</script>', $a );
		if ( false === $b ) {
			return null;
		}
		$a += strlen( $open );
		return json_decode( trim( substr( $html, $a, $b - $a ) ), true );
	};
	return array( $get( 'manifest' ), $get( 'ext_resources' ) ?: array(), $get( 'template' ) );
}

/** Medios remotos que usa un template: URL completas y concatenaciones tipo IMG + 'ruta'. */
function hm_media_refs( $tpl ) {
	$refs = array();
	foreach ( hm_media_prefixes() as $p ) {
		preg_match_all( '#' . preg_quote( $p, '#' ) . '[^\s\'"()<>,`\\\\]+#', $tpl, $m );
		foreach ( $m[0] as $u ) {
			$refs[ $u ] = 1;
		}
	}
	if ( preg_match_all( '#const\s+(\w+)\s*=\s*[\'"](https://[^\'"]+/)[\'"]#', $tpl, $consts, PREG_SET_ORDER ) ) {
		foreach ( $consts as $c ) {
			preg_match_all( '#\b' . preg_quote( $c[1], '#' ) . '\s*\+\s*[\'"]([^\'"]+)[\'"]#', $tpl, $m );
			foreach ( $m[1] as $rel ) {
				$refs[ $c[2] . $rel ] = 1;
			}
		}
	}
	$out = array();
	foreach ( array_keys( $refs ) as $u ) {
		if ( preg_match( '#\.(jpe?g|png|gif|webp|svg|mp4|webm)$#i', (string) parse_url( $u, PHP_URL_PATH ) ) ) {
			$out[] = $u;
		}
	}
	return $out;
}

/** Ruta relativa a hm-media de un medio remoto (JPG/PNG pasan a WebP). */
function hm_media_local( $remote ) {
	$p   = parse_url( $remote );
	$rel = $p['host'] . $p['path'];
	return preg_replace( '#\.(jpe?g|png)$#i', '.webp', $rel );
}

/**
 * Copia al servidor los medios remotos de todas las páginas. Reanudable: salta lo ya copiado y para
 * a los $max_seconds (devuelve cuántos quedan). Al terminar regenera las páginas y vacía la caché.
 */
function hm_media_mirror( $max_seconds = 25 ) {
	require_once ABSPATH . 'wp-admin/includes/file.php';
	$t0   = microtime( true );
	$refs = array();
	foreach ( glob( get_stylesheet_directory() . '/hm-paginas/*.html' ) as $f ) {
		list( , , $tpl ) = hm_bundle_parts( file_get_contents( $f ) );
		if ( is_string( $tpl ) ) {
			foreach ( hm_media_refs( $tpl ) as $u ) {
				$refs[ $u ] = 1;
			}
		}
	}
	$dir  = hm_media_dir();
	$dims = get_option( 'hm_media_dims', array() );
	$res  = array( 'total' => count( $refs ), 'done' => 0, 'pending' => 0, 'fail' => array(), 'bytes_in' => 0, 'bytes_out' => 0 );
	foreach ( array_keys( $refs ) as $u ) {
		$rel  = hm_media_local( $u );
		$dest = $dir . '/' . $rel;
		if ( file_exists( $dest ) ) {
			continue;
		}
		if ( microtime( true ) - $t0 > $max_seconds ) {
			$res['pending']++;
			continue;
		}
		wp_mkdir_p( dirname( $dest ) );
		$tmp = download_url( $u, 120 );
		if ( is_wp_error( $tmp ) ) {
			$res['fail'][ $u ] = $tmp->get_error_message();
			continue;
		}
		$res['bytes_in'] += filesize( $tmp );
		if ( substr( $rel, -5 ) === '.webp' && ! preg_match( '#\.webp$#i', $u ) ) {
			$ed = wp_get_image_editor( $tmp );
			if ( is_wp_error( $ed ) ) {
				$res['fail'][ $u ] = $ed->get_error_message();
				@unlink( $tmp );
				continue;
			}
			$s = $ed->get_size();
			if ( $s['width'] > 1900 ) {
				$ed->resize( 1900, null );
				$s = $ed->get_size();
			}
			$ed->set_quality( 74 );
			$saved = $ed->save( $dest . '.tmp.webp', 'image/webp' );
			@unlink( $tmp );
			if ( is_wp_error( $saved ) ) {
				$res['fail'][ $u ] = $saved->get_error_message();
				continue;
			}
			rename( $saved['path'], $dest );
			$dims[ $rel ] = array( $s['width'], $s['height'] );
		} else {
			copy( $tmp, $dest . '.tmp' );
			rename( $dest . '.tmp', $dest );
			@unlink( $tmp );
		}
		$res['bytes_out'] += filesize( $dest );
		$res['done']++;
	}
	update_option( 'hm_media_dims', $dims, false );
	if ( ! $res['pending'] && ( $res['done'] || ! empty( $res['fail'] ) ) ) {
		hm_dist_reset();
	}
	return $res;
}

/** Borra las páginas dist (se regeneran en la siguiente visita) y vacía la caché de WP Rocket. */
function hm_dist_reset() {
	foreach ( glob( hm_dist_dir() . '/*.html' ) as $f ) {
		@unlink( $f );
	}
	if ( function_exists( 'rocket_clean_domain' ) ) {
		rocket_clean_domain();
	}
}

/** Desempaqueta un paquete de hm-paginas/ en dist/. Devuelve el HTML o false si no es un paquete válido. */
function hm_dist_build( $src ) {
	list( $man, $ext, $tpl ) = hm_bundle_parts( file_get_contents( $src ) );
	if ( ! is_array( $man ) || ! is_string( $tpl ) || stripos( $tpl, '<head' ) === false ) {
		return false;
	}
	$adir = hm_dist_dir() . '/a';
	if ( ! wp_mkdir_p( $adir ) ) {
		return false;
	}
	if ( ! file_exists( $adir . '/.htaccess' ) ) {
		file_put_contents( $adir . '/.htaccess', "<IfModule mod_headers.c>\nHeader set Cache-Control \"public, max-age=31536000, immutable\"\n</IfModule>\n" );
	}
	$types = array(
		'text/javascript' => 'js', 'application/javascript' => 'js', 'text/css' => 'css', 'image/svg+xml' => 'svg',
		'image/jpeg' => 'jpg', 'image/png' => 'png', 'image/webp' => 'webp', 'image/gif' => 'gif', 'image/avif' => 'avif',
		'font/woff2' => 'woff2', 'font/woff' => 'woff', 'video/mp4' => 'mp4',
	);
	$map = array();
	foreach ( $man as $uuid => $e ) {
		$bin = base64_decode( (string) ( $e['data'] ?? '' ), true );
		if ( false !== $bin && ! empty( $e['compressed'] ) ) {
			$bin = gzdecode( $bin );
		}
		if ( false === $bin ) {
			return false;
		}
		$name = substr( sha1( $bin ), 0, 16 ) . '.' . ( $types[ strtolower( (string) ( $e['mime'] ?? '' ) ) ] ?? 'bin' );
		if ( ! file_exists( "$adir/$name" ) ) {
			$tmp = "$adir/$name." . uniqid() . '.tmp';
			file_put_contents( $tmp, $bin );
			rename( $tmp, "$adir/$name" );
		}
		$map[ $uuid ] = hm_dist_url() . '/a/' . $name;
	}
	$tpl = strtr( $tpl, $map );

	// Lo que el cargador inyectaba: mapa de recursos (React local, logo...). Sin él, el runtime vuelve a pedir la página.
	$res = array();
	foreach ( $ext as $r ) {
		if ( isset( $r['id'], $r['uuid'], $map[ $r['uuid'] ] ) ) {
			$res[ $r['id'] ] = $map[ $r['uuid'] ];
		}
	}
	$head = '<script>window.__resources=' . wp_json_encode( $res, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_HEX_TAG ) . ';</script>';
	// React y ReactDOM los inyecta el runtime: precargarlos para que bajen en paralelo con él.
	foreach ( $res as $id => $u ) {
		if ( preg_match( '#/react(-dom)?@[\d.]+/umd/#', $id ) ) {
			$head .= '<link rel="preload" as="script" href="' . esc_attr( $u ) . '">';
		}
	}
	if ( preg_match( '#/\* latin \*/\s*@font-face\s*\{[^}]*?url\("([^"]+\.woff2)"\)#', $tpl, $fm ) ) {
		$head .= '<link rel="preload" as="font" type="font/woff2" href="' . esc_attr( $fm[1] ) . '" crossorigin>';
	}

	// Medios remotos -> copias locales (solo si están todas; las <meta> como og:image siguen absolutas).
	$refs = hm_media_refs( $tpl );
	$mdir = hm_media_dir();
	$ok   = (bool) $refs;
	foreach ( $refs as $u ) {
		if ( ! file_exists( $mdir . '/' . hm_media_local( $u ) ) ) {
			$ok = false;
			break;
		}
	}
	if ( $ok ) {
		// Dos pasadas: primero la extensión (.jpg -> .webp) sobre la URL remota, después el origen -> ruta local.
		$pairs = array();
		$tails = array();
		foreach ( hm_media_prefixes() as $p ) {
			$pu          = parse_url( $p );
			$pairs[ $p ] = hm_media_url() . '/' . $pu['host'] . $pu['path'];
		}
		foreach ( $refs as $u ) {
			$path = (string) parse_url( $u, PHP_URL_PATH );
			$tail = implode( '/', array_slice( explode( '/', $path ), -2 ) );
			$new  = preg_replace( '#\.(jpe?g|png)$#i', '.webp', $tail );
			if ( $new !== $tail ) {
				$tails[ $tail ] = $new;
			}
		}
		$dims  = get_option( 'hm_media_dims', array() );
		$parts = preg_split( '#(<meta\b[^>]*>)#i', $tpl, -1, PREG_SPLIT_DELIM_CAPTURE );
		foreach ( $parts as $i => $part ) {
			if ( $i % 2 ) {
				continue;
			}
			// <img> con URL remota fija y sin medidas: añadir width/height reales (evita saltos de diseño).
			$part = preg_replace_callback(
				'#<img\b(?![^>]*\swidth=)([^>]*\ssrc=")(https://[^"]+)"#i',
				static function ( $m ) use ( $dims ) {
					$d = $dims[ hm_media_local( $m[2] ) ] ?? null;
					return $d ? '<img width="' . (int) $d[0] . '" height="' . (int) $d[1] . '"' . $m[1] . $m[2] . '"' : $m[0];
				},
				$part
			);
			$parts[ $i ] = strtr( strtr( $part, $tails ), $pairs );
		}
		$tpl = implode( '', $parts );
		if ( ! file_exists( $mdir . '/.htaccess' ) ) {
			file_put_contents( $mdir . '/.htaccess', "<IfModule mod_headers.c>\nHeader set Cache-Control \"public, max-age=31536000\"\n</IfModule>\n" );
		}
	}

	$tpl  = preg_replace_callback( '#<head\b[^>]*>#i', static fn( $m ) => $m[0] . $head, $tpl, 1 );
	$tpl  = rtrim( $tpl ) . "\n<!-- hm-dist:" . HM_DIST_VER . ' -->';
	$dst  = hm_dist_dir() . '/' . basename( $src );
	$tmp  = $dst . '.' . uniqid() . '.tmp';
	file_put_contents( $tmp, $tpl );
	rename( $tmp, $dst );
	return $tpl;
}

/** HTML desempaquetado de una página (lo genera si falta o si el paquete es más nuevo). */
function hm_dist_get( $src ) {
	$dst = hm_dist_dir() . '/' . basename( $src );
	if ( is_readable( $dst ) && filemtime( $dst ) >= filemtime( $src ) ) {
		$h = file_get_contents( $dst );
		if ( str_ends_with( $h, '<!-- hm-dist:' . HM_DIST_VER . ' -->' ) ) {
			return $h;
		}
	}
	return hm_dist_build( $src );
}

/* Si cambia algún paquete de hm-paginas/, vaciar la caché de WP Rocket (las páginas en caché no pasan por PHP). */
add_action( 'init', function () {
	$now = array();
	foreach ( glob( get_stylesheet_directory() . '/hm-paginas/*.html' ) ?: array() as $f ) {
		$now[ basename( $f ) ] = filemtime( $f ) . ':' . filesize( $f );
	}
	$was = get_option( 'hm_dist_src' );
	if ( $now !== $was ) {
		update_option( 'hm_dist_src', $now, false );
		if ( is_array( $was ) && function_exists( 'rocket_clean_domain' ) ) {
			rocket_clean_domain();
		}
	}
} );