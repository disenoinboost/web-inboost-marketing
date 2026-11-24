<?php
// Hortelã Magenta · fase 2 · instala ficheiros do tema filho a partir do repositório (PHP, CSS, JS), com cópia e verificação.
// Pegar como `code` de novamira/execute-php SEM a linha <?php, depois de definir:
//   $BASE    URL raw da pasta hortela-magenta/fase2/ num commit
//   $FICH    array origem (relativa a $BASE) => array( destino relativo ao tema filho, md5 )
// Os PHP passam por `php -l` antes de substituir o original (se a sintaxe falhar, não se toca no tema).
$t   = get_stylesheet_directory() . '/';
$cli = file_exists( '/opt/plesk/php/8.5/bin/php' ) ? '/opt/plesk/php/8.5/bin/php' : null;
$res = array();
foreach ( $FICH as $src => $info ) {
	list( $dst, $md5 ) = $info;
	$r    = wp_remote_get( $BASE . $src, array( 'timeout' => 30 ) );
	$body = is_wp_error( $r ) ? '' : wp_remote_retrieve_body( $r );
	if ( md5( $body ) !== $md5 ) { $res[ $dst ] = 'md5 distinto'; continue; }
	$tmp = $t . $dst . '.tmp-' . uniqid();
	wp_mkdir_p( dirname( $t . $dst ) );
	file_put_contents( $tmp, $body );
	if ( substr( $dst, -4 ) === '.php' ) {
		if ( ! $cli ) { @unlink( $tmp ); $res[ $dst ] = 'sem php-cli para verificar'; continue; }
		$lint = shell_exec( escapeshellarg( $cli ) . ' -l ' . escapeshellarg( $tmp ) . ' 2>&1' );
		if ( false === strpos( (string) $lint, 'No syntax errors' ) ) { @unlink( $tmp ); $res[ $dst ] = 'sintaxe: ' . trim( (string) $lint ); continue; }
	}
	if ( file_exists( $t . $dst ) ) {
		copy( $t . $dst, $t . $dst . '.bak-' . gmdate( 'Ymd-His' ) );
	}
	rename( $tmp, $t . $dst );
	$res[ $dst ] = 'ok ' . md5_file( $t . $dst );
}
clearstatcache();
return $res;
