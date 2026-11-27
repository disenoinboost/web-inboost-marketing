<?php
// Hortelã Magenta · «faststart» de MP4 sem recomprimir (como qt-faststart): põe o índice (moov) antes dos dados (mdat),
// para o vídeo começar a tocar sem descarregar o ficheiro inteiro («carrega aos solavancos»). 2026-11-27.
// Pegar como `code` de novamira/execute-php SEM a linha <?php, depois de definir:
//   $DIR    pasta base (p. ex. wp_upload_dir()['basedir'] . '/hm-media/')
//   $GRAVAR false: só lista os que precisam; true: grava (cópia em uploads/hm-media-bak-faststart/, tmp + rename)
// Também se usa em local (php faststart.php <entrada.mp4> <saida.mp4>) para testar.
function hm_fs_atoms( $d, $start, $end ) {
	$out = array(); $p = $start;
	while ( $p + 8 <= $end ) {
		$sz = unpack( 'N', substr( $d, $p, 4 ) )[1]; $ty = substr( $d, $p + 4, 4 ); $hd = 8;
		if ( 1 === $sz ) { $sz = unpack( 'J', substr( $d, $p + 8, 8 ) )[1]; $hd = 16; }
		elseif ( 0 === $sz ) { $sz = $end - $p; }
		if ( $sz < $hd || $p + $sz > $end ) return false;
		$out[] = array( $ty, $p, $sz, $hd ); $p += $sz;
	}
	return $out;
}
function hm_fs_patch( &$m, $start, $end, $delta, &$n ) {
	$kids = hm_fs_atoms( $m, $start, $end ); if ( false === $kids ) return false;
	foreach ( $kids as list( $ty, $p, $sz, $hd ) ) {
		if ( in_array( $ty, array( 'trak', 'mdia', 'minf', 'stbl', 'edts', 'mvex' ), true ) ) {
			if ( false === hm_fs_patch( $m, $p + $hd, $p + $sz, $delta, $n ) ) return false;
		} elseif ( 'stco' === $ty || 'co64' === $ty ) {
			$c = unpack( 'N', substr( $m, $p + $hd + 4, 4 ) )[1]; $q = $p + $hd + 8; $w = 'stco' === $ty ? 4 : 8;
			for ( $i = 0; $i < $c; $i++, $q += $w ) {
				if ( 4 === $w ) { $v = unpack( 'N', substr( $m, $q, 4 ) )[1] + $delta; if ( $v > 0xFFFFFFFF ) return false; $m = substr_replace( $m, pack( 'N', $v ), $q, 4 ); }
				else { $v = unpack( 'J', substr( $m, $q, 8 ) )[1] + $delta; $m = substr_replace( $m, pack( 'J', $v ), $q, 8 ); }
				$n++;
			}
		}
	}
	return true;
}
/** Devolve o MP4 com o moov à frente, null se já estiver bem, false se não souber tratá-lo. */
function hm_faststart( $d ) {
	$top = hm_fs_atoms( $d, 0, strlen( $d ) ); if ( ! $top ) return false;
	$im = $id = null; foreach ( $top as $i => $a ) { if ( 'moov' === $a[0] && null === $im ) $im = $i; if ( 'mdat' === $a[0] && null === $id ) $id = $i; }
	if ( null === $im || null === $id ) return false;
	if ( $im < $id ) return null;
	$moov = substr( $d, $top[ $im ][1], $top[ $im ][2] ); if ( 8 !== $top[ $im ][3] ) return false;
	foreach ( hm_fs_atoms( $moov, 8, strlen( $moov ) ) as $k ) if ( 'cmov' === $k[0] ) return false; // moov comprimido
	$n = 0; if ( ! hm_fs_patch( $moov, 8, strlen( $moov ), strlen( $moov ), $n ) || ! $n ) return false;
	$out = ''; $done = false;
	foreach ( $top as $i => $a ) {
		if ( $i === $im ) continue;
		if ( ! $done && ! in_array( $a[0], array( 'ftyp', 'uuid' ), true ) ) { $out .= $moov; $done = true; }
		$out .= substr( $d, $a[1], $a[2] );
	}
	return strlen( $out ) === strlen( $d ) ? $out : false;
}
if ( PHP_SAPI === 'cli' && isset( $argv[2] ) && realpath( $argv[0] ) === realpath( __FILE__ ) ) {
	$r = hm_faststart( file_get_contents( $argv[1] ) ); if ( is_string( $r ) ) file_put_contents( $argv[2], $r ); echo null === $r ? "ja estava\n" : ( false === $r ? "falhou\n" : "ok\n" ); exit;
}
if ( isset( $DIR ) ) {
	$res = array( 'feitos' => array(), 'ja' => 0, 'falhas' => array() );
	$it = new RecursiveIteratorIterator( new RecursiveDirectoryIterator( $DIR, FilesystemIterator::SKIP_DOTS ) );
	foreach ( $it as $f ) {
		if ( 'mp4' !== strtolower( $f->getExtension() ) ) continue;
		$path = $f->getPathname(); $d = file_get_contents( $path ); $r = hm_faststart( $d ); $rel = substr( $path, strlen( $DIR ) );
		if ( null === $r ) { $res['ja']++; continue; }
		if ( false === $r ) { $res['falhas'][] = $rel; continue; }
		if ( $GRAVAR ) {
			$bak = wp_upload_dir()['basedir'] . '/hm-media-bak-faststart/' . $rel; wp_mkdir_p( dirname( $bak ) ); if ( ! file_exists( $bak ) ) copy( $path, $bak );
			file_put_contents( $path . '.tmp', $r ); rename( $path . '.tmp', $path );
		}
		$res['feitos'][] = $rel . ' (' . round( strlen( $d ) / 1048576, 1 ) . ' MB)';
	}
	return $res;
}
