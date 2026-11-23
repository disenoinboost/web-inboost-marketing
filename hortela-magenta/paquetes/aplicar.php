<?php
// Hortelã Magenta · aplica listas de edições (JSON, as mesmas de aplicar.py) ao template dos pacotes hm-paginas/*.html.
// Pegar como `code` de novamira/execute-php SEM a linha <?php, depois de definir $EDICOES_GZ_B64 (gzip+base64 do JSON) e $GRAVAR.
// $GRAVAR = false: só verifica (quantas vezes aparece cada texto). true: cópia em hm-paginas-bak/<data>/ e grava (tmp + rename).
// O template é recodificado com JSON_HEX_TAG (< e > como </>): nunca fecha o <script> do pacote.
$edicoes = json_decode( gzdecode( base64_decode( $EDICOES_GZ_B64 ) ), true );
$dir = get_stylesheet_directory() . '/hm-paginas/';
$res = array( 'ok' => 0, 'falhas' => array(), 'paginas' => array() );
$tpls = array(); $raw = array();
foreach ( $edicoes as $e ) {
	$p = $e['page'];
	if ( ! isset( $tpls[ $p ] ) ) {
		$raw[ $p ] = file_get_contents( $dir . $p . '.html' );
		list( , , $tpls[ $p ] ) = hm_bundle_parts( $raw[ $p ] );
	}
	$t = $tpls[ $p ]; $why = $e['why'] ?? '';
	if ( 'replace' === $e['op'] ) {
		$n = substr_count( $t, $e['old'] );
		if ( $n !== $e['count'] ) { $res['falhas'][] = "$p · $why · $n"; continue; }
		$t = str_replace( $e['old'], $e['new'], $t );
	} elseif ( 'regex' === $e['op'] ) {
		$re = '~' . str_replace( '~', '\~', $e['pattern'] ) . '~u';
		$n = preg_match_all( $re, $t );
		if ( $n !== $e['count'] ) { $res['falhas'][] = "$p · $why · regex $n"; continue; }
		$t = preg_replace( $re, $e['new'], $t );
	} elseif ( 'insert_after' === $e['op'] ) {
		$a = strpos( $t, $e['anchor'] ); $b = false === $a ? false : strpos( $t, $e['marker'], $a );
		if ( false === $b || substr_count( $t, $e['anchor'] ) !== 1 ) { $res['falhas'][] = "$p · $why · insert"; continue; }
		$b += strlen( $e['marker'] ); $t = substr( $t, 0, $b ) . $e['text'] . substr( $t, $b );
	} else {
		$a = strpos( $t, $e['start'] ); $b = false === $a ? false : strpos( $t, $e['end'], $a );
		if ( false === $b || substr_count( $t, $e['start'] ) !== 1 ) { $res['falhas'][] = "$p · $why · cut"; continue; }
		$t = substr( $t, 0, $a ) . substr( $t, $b + strlen( $e['end'] ) );
	}
	$tpls[ $p ] = $t; $res['ok']++;
}
if ( $GRAVAR && ! $res['falhas'] ) {
	$bak = get_stylesheet_directory() . '/hm-paginas-bak/' . gmdate( 'Y-m-d' ) . '-antes-' . $ETIQUETA;
	wp_mkdir_p( $bak );
	foreach ( $tpls as $p => $t ) {
		if ( ! file_exists( "$bak/$p.html" ) ) copy( $dir . $p . '.html', "$bak/$p.html" );
		$open = '<script type="__bundler/template">'; $a = strpos( $raw[ $p ], $open ) + strlen( $open ); $b = strpos( $raw[ $p ], '</script>', $a );
		$enc = json_encode( $t, JSON_HEX_TAG | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
		$new = substr( $raw[ $p ], 0, $a ) . $enc . substr( $raw[ $p ], $b );
		list( , , $chk ) = hm_bundle_parts( $new );
		if ( $chk !== $t ) { $res['falhas'][] = "$p · recodificação não confere"; continue; }
		$tmp = $dir . $p . '.html.tmp'; file_put_contents( $tmp, $new ); rename( $tmp, $dir . $p . '.html' );
		$res['paginas'][ $p ] = md5( $new );
	}
}
return $res;
