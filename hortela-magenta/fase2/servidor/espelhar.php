<?php
// Hortelã Magenta · fase 2: copia para uploads/hm-media/ uma lista explícita de medios remotos (mesmo formato que hm_media_mirror:
// JPG/PNG -> WebP q74, máx. 1900 px; GIF/MP4/WebP tal qual) e guarda as medidas em hm_media_dims. Reanudável.
// Pegar como `code` de novamira/execute-php SEM a linha <?php, depois de definir $URLS (array) e $MAX (segundos).
require_once ABSPATH . 'wp-admin/includes/file.php';
$t0 = microtime( true ); $dir = hm_media_dir(); $dims = get_option( 'hm_media_dims', array() );
$res = array( 'total' => count( $URLS ), 'done' => 0, 'skip' => 0, 'pending' => 0, 'fail' => array() );
foreach ( $URLS as $u ) {
	$p = parse_url( $u ); $path = $p['path'];
	$rel = $p['host'] . preg_replace( '#[^A-Za-z0-9/._-]+#', '-', rawurldecode( $path ) );
	$rel = preg_replace( '#\.(jpe?g|png)$#i', '.webp', preg_replace( '#\.jpg_id=\d+$#', '.jpg', $rel ) );
	$dest = $dir . '/' . $rel;
	if ( file_exists( $dest ) ) {
		if ( ! isset( $dims[ $rel ] ) && preg_match( '#\.(webp|gif|jpe?g|png)$#i', $dest ) ) { $s = @getimagesize( $dest ); if ( $s ) $dims[ $rel ] = array( $s[0], $s[1] ); }
		$res['skip']++; continue;
	}
	if ( microtime( true ) - $t0 > $MAX ) { $res['pending']++; continue; }
	wp_mkdir_p( dirname( $dest ) );
	$tmp = download_url( str_replace( ' ', '%20', $u ), 180 );
	if ( is_wp_error( $tmp ) ) { $res['fail'][ $u ] = $tmp->get_error_message(); continue; }
	if ( substr( $rel, -5 ) === '.webp' && ! preg_match( '#\.webp$#i', $path ) ) {
		$ed = wp_get_image_editor( $tmp );
		if ( is_wp_error( $ed ) ) { $res['fail'][ $u ] = $ed->get_error_message(); @unlink( $tmp ); continue; }
		$s = $ed->get_size(); if ( $s['width'] > 1900 ) { $ed->resize( 1900, null ); $s = $ed->get_size(); }
		$ed->set_quality( 74 ); $saved = $ed->save( $dest . '.tmp.webp', 'image/webp' ); @unlink( $tmp );
		if ( is_wp_error( $saved ) ) { $res['fail'][ $u ] = $saved->get_error_message(); continue; }
		rename( $saved['path'], $dest ); $dims[ $rel ] = array( $s['width'], $s['height'] );
	} else {
		copy( $tmp, $dest . '.tmp' ); rename( $dest . '.tmp', $dest ); @unlink( $tmp );
		if ( preg_match( '#\.(gif|webp)$#i', $dest ) ) { $s = @getimagesize( $dest ); if ( $s ) $dims[ $rel ] = array( $s[0], $s[1] ); }
	}
	$res['done']++;
}
update_option( 'hm_media_dims', $dims, false );
$res['secs'] = round( microtime( true ) - $t0 );
return $res;
