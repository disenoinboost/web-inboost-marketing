<?php
// Solo hace falta si el contenedor NO puede acceder a laura.inboost.marketing (red bloqueada).
// Pegar como `code` de novamira/execute-php (sin la línea <?php) tras fetch_html.php, con el mismo $urls.
// Devuelve HTML + CSS/JS/fuentes/imágenes del propio sitio, comprimidos (unos 3,5 MB): python3 -I tools/unpack.py
$urls = [
	'orig' => home_url( '/SLUG-ORIGINAL/' ),
	'prop' => home_url( '/?page_id=ID-COPIA&preview=true' ),
];
$host   = parse_url( home_url(), PHP_URL_HOST );
$cookie = new WP_Http_Cookie( [ 'name' => LOGGED_IN_COOKIE, 'value' => wp_generate_auth_cookie( 1, time() + 600, 'logged_in' ), 'domain' => $host ] );
$re     = '#(?:href|src)=[\'"](https?://' . preg_quote( $host, '#' ) . '/[^\'"\s>]+)#';
$out    = [ 'html' => [], 'files' => [], 'missing' => [] ];
$paths  = [];
foreach ( $urls as $k => $u ) {
	$h = wp_remote_retrieve_body( wp_remote_get( $u, [ 'cookies' => [ $cookie ], 'sslverify' => false, 'timeout' => 60 ] ) );
	$out['html'][ $k ] = base64_encode( gzencode( $h, 9 ) );
	preg_match_all( $re, $h, $m );
	foreach ( $m[1] as $a ) {
		$p = parse_url( html_entity_decode( $a ), PHP_URL_PATH );
		if ( $p ) {
			$paths[ $p ] = 1;
		}
	}
}
$skip  = '#(admin-bar|adminbar|dashicons|wp-login\.php|lottie|script-library-woo|woocommerce|mediaelement|comment-reply|/$)#';
$queue = array_keys( $paths );
$seen  = [];
while ( $queue ) {
	$p = array_shift( $queue );
	if ( isset( $seen[ $p ] ) || preg_match( $skip, $p ) ) {
		continue;
	}
	$seen[ $p ] = 1;
	$fp         = ABSPATH . ltrim( rawurldecode( $p ), '/' );
	if ( ! is_file( $fp ) ) {
		$out['missing'][] = $p;
		continue;
	}
	$c                  = file_get_contents( $fp );
	$out['files'][ $p ] = base64_encode( gzencode( $c, 9 ) );
	if ( '.css' === substr( $p, -4 ) ) {
		preg_match_all( '#url\(\s*[\'"]?([^)\'"]+)[\'"]?\s*\)#', $c, $cu );
		foreach ( $cu[1] as $ref ) {
			if ( 0 === strpos( $ref, 'data:' ) || preg_match( '#^https?://#', $ref ) ) {
				continue;
			}
			$ref = preg_replace( '/[?#].*$/', '', $ref );
			if ( '/' === $ref[0] ) {
				$queue[] = $ref;
				continue;
			}
			$st = [];
			foreach ( explode( '/', dirname( $p ) . '/' . $ref ) as $seg ) {
				if ( '' === $seg || '.' === $seg ) {
					continue;
				}
				'..' === $seg ? array_pop( $st ) : $st[] = $seg;
			}
			$queue[] = '/' . implode( '/', $st );
		}
	}
}
return $out;
