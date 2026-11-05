<?php
// Hortelã Magenta · trae al contenedor las páginas servidas (dist) y sus recursos, para probarlas en local.
// Pegar como `code` de novamira/execute-php (conector Novamira - Hortel Magenta), SIN la línea <?php.
// Dos llamadas: primero con $parte = 'html', después con $parte = 'assets' (cada respuesta se guarda en un archivo).
// Desempaquetar cada una con: python3 -I tools/unpack.py <archivo-del-resultado> <dir>
//   -> <dir>/<pagina>.html  y  <dir>/site/<ruta>   (formato de tools/unpack.py)
// Las imágenes de uploads/hm-media no se traen (pesan mucho); en local salen como hueco gris.
$parte = 'html';

$base = get_stylesheet_directory();
$out  = array( 'html' => array(), 'files' => array(), 'missing' => array() );
if ( 'html' === $parte ) {
	foreach ( glob( $base . '/hm-paginas/*.html' ) as $f ) {
		$h = hm_dist_get( $f ); // genera dist si falta
		if ( $h ) {
			$out['html'][ basename( $f, '.html' ) ] = base64_encode( gzencode( $h, 9 ) );
		} else {
			$out['missing'][] = basename( $f );
		}
	}
} else {
	$rel = wp_make_link_relative( get_stylesheet_directory_uri() );
	foreach ( glob( $base . '/hm-paginas/dist/a/*.{js,woff2,svg,css}', GLOB_BRACE ) as $f ) {
		$out['files'][ $rel . '/hm-paginas/dist/a/' . basename( $f ) ] = base64_encode( gzencode( file_get_contents( $f ), 9 ) );
	}
	foreach ( array( 'hm-boceto-fix.css', 'hm-boceto-fix.js' ) as $n ) {
		if ( is_readable( $base . '/assets/' . $n ) ) {
			$out['files'][ $rel . '/assets/' . $n ] = base64_encode( gzencode( file_get_contents( $base . '/assets/' . $n ), 9 ) );
		}
	}
}
return $out;
