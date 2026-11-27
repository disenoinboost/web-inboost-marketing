<?php
// Hortelã Magenta · fase 2 · monta pacotes hm-paginas/<pagina>.html a partir de modelos (template) publicados no repositório.
// Pegar como `code` de novamira/execute-php SEM a linha <?php, depois de definir:
//   $BASE     URL raw da pasta hortela-magenta/fase2/ num commit (https://raw.githubusercontent.com/.../<commit>/hortela-magenta/fase2/)
//   $PAGINAS  array de nomes (sem .html) a montar a partir de $BASE.'modelos/<nome>.html'
//   $MD5      array nome => md5 do modelo (verificação da transferência)
//   $ETIQUETA texto para a pasta de cópias (hm-paginas-bak/<data>-antes-<etiqueta>/)
//   $GRAVAR   false: só verifica; true: grava (tmp + rename) e limpa dist/WP Rocket no fim.
//   $ANTES    (2026-11-27) array nome => md5 do modelo que o servidor DEVE ter agora (o de fase2/modelos/md5.json no commit
//             anterior). Se o servidor tiver outro, essa página NÃO se grava: outra sessão mudou-a entretanto e é preciso
//             trazer essa versão e fundir antes de subir (assim nenhuma sessão com uma cópia antiga pisa correções).
// O manifest de cada pacote junta só os recursos (uuid) que o modelo usa, tirados dos pacotes existentes.
$dir = get_stylesheet_directory() . '/hm-paginas/';
$res = array( 'ok' => array(), 'falhas' => array() );
// 1) união dos recursos de todos os pacotes existentes
$union = array(); $ext = null; $shell = null;
foreach ( glob( $dir . '*.html' ) as $f ) {
	$raw = file_get_contents( $f );
	list( $man, $e ) = hm_bundle_parts( $raw );
	if ( is_array( $man ) ) {
		$union += $man;
	}
	if ( 'contacto.html' === basename( $f ) ) {
		$shell = $raw; $ext = $e;
	}
}
if ( ! $shell ) return 'sem pacote base (contacto.html)';
$enc = static function ( $v ) {
	return json_encode( $v, JSON_HEX_TAG | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
};
$swap = static function ( $raw, $type, $json ) {
	$open = '<script type="__bundler/' . $type . '">';
	$a    = strpos( $raw, $open ) + strlen( $open );
	$b    = strpos( $raw, '</script>', $a );
	return substr( $raw, 0, $a ) . $json . substr( $raw, $b );
};
$bak = get_stylesheet_directory() . '/hm-paginas-bak/' . gmdate( 'Y-m-d' ) . '-antes-' . $ETIQUETA;
foreach ( $PAGINAS as $p ) {
	$r = wp_remote_get( $BASE . 'modelos/' . $p . '.html', array( 'timeout' => 30 ) );
	$t = is_wp_error( $r ) ? '' : wp_remote_retrieve_body( $r );
	if ( '' === $t || md5( $t ) !== ( $MD5[ $p ] ?? '' ) ) { $res['falhas'][] = "$p · transferência (md5)"; continue; }
	if ( false === strpos( $t, '<x-dc>' ) || false === stripos( $t, '<head' ) ) { $res['falhas'][] = "$p · não é um modelo"; continue; }
	$man = array();
	foreach ( $union as $uuid => $entry ) {
		if ( false !== strpos( $t, $uuid ) ) {
			$man[ $uuid ] = $entry;
		}
	}
	preg_match( '#<title>(.*?)</title>#s', $t, $tm );
	$new = $swap( $shell, 'manifest', $enc( $man ) );
	$new = $swap( $new, 'ext_resources', $enc( $ext ) );
	$new = $swap( $new, 'template', $enc( $t ) );
	$new = preg_replace( '#(<head>\s*<meta charset="utf-8">\s*<title>).*?(</title>)#s', '${1}' . str_replace( '$', '\$', $tm[1] ?? 'Hortelã Magenta' ) . '${2}', $new, 1 );
	list( , , $chk ) = hm_bundle_parts( $new );
	if ( $chk !== $t ) { $res['falhas'][] = "$p · recodificação não confere"; continue; }
	if ( isset( $ANTES[ $p ] ) && file_exists( $dir . $p . '.html' ) ) {
		list( , , $cur ) = hm_bundle_parts( file_get_contents( $dir . $p . '.html' ) );
		if ( md5( $cur ) !== $ANTES[ $p ] && md5( $cur ) !== md5( $t ) ) { $res['falhas'][] = "$p · o servidor tem outra versão (" . md5( $cur ) . '): não gravado'; continue; }
	}
	if ( $GRAVAR ) {
		if ( file_exists( $dir . $p . '.html' ) ) {
			wp_mkdir_p( $bak );
			if ( ! file_exists( "$bak/$p.html" ) ) copy( $dir . $p . '.html', "$bak/$p.html" );
		}
		$tmp = $dir . $p . '.html.tmp';
		file_put_contents( $tmp, $new );
		rename( $tmp, $dir . $p . '.html' );
	}
	$res['ok'][ $p ] = array( 'kb' => round( strlen( $new ) / 1024 ), 'recursos' => count( $man ) );
}
if ( $GRAVAR && $res['ok'] ) {
	clearstatcache();
	hm_dist_reset();
}
return $res;
