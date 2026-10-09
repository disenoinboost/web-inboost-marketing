<?php
// Pegar como `code` de novamira/execute-php (sin la línea <?php).
// Descarga el HTML real de las URL indicadas con una sesión de administrador creada en el propio
// servidor (la cookie nunca sale de WordPress) y lo devuelve comprimido. La respuesta suele guardarse
// en un archivo de tool-results; se descomprime con: python3 -I tools/unpack.py <archivo> <dir>
$urls = [
	'orig' => home_url( '/SLUG-ORIGINAL/' ),
	'prop' => home_url( '/?page_id=ID-COPIA&preview=true' ),
];
$cookie = new WP_Http_Cookie( [
	'name'   => LOGGED_IN_COOKIE,
	'value'  => wp_generate_auth_cookie( 1, time() + 600, 'logged_in' ),
	'domain' => parse_url( home_url(), PHP_URL_HOST ),
] );
$out = [ 'html' => [] ];
foreach ( $urls as $k => $u ) {
	$r = wp_remote_get( $u, [ 'cookies' => [ $cookie ], 'sslverify' => false, 'timeout' => 60 ] );
	$out['html'][ $k ] = is_wp_error( $r ) ? '' : base64_encode( gzencode( wp_remote_retrieve_body( $r ), 9 ) );
}
return $out;
