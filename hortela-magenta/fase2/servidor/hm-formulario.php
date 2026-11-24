<?php
/**
 * Hortelã Magenta · formulário de contacto (fase 2, 2026-11-24).
 *
 * POST /wp-json/hm/v1/contacto (FormData do formulário de /contacto). Valida, guarda cada pedido no WordPress
 * (Pedidos de contacto, tipo hm_pedido, só visível no painel) e envia um email com Reply-To do remetente.
 * Destinatário: opção hm_form_to (por omissão, o email do administrador). Antes de publicar: definir o email
 * da Hortelã Magenta com update_option( 'hm_form_to', '...' ) e confirmar que o servidor envia correio.
 * Proteção: campo isco «empresa_url» vazio, tempo mínimo de preenchimento e limite de 5 envios por IP em 10 minutos.
 */
defined( 'ABSPATH' ) || exit;

add_action( 'init', function () {
	register_post_type( 'hm_pedido', array(
		'labels'          => array( 'name' => 'Pedidos de contacto', 'singular_name' => 'Pedido de contacto', 'menu_name' => 'Pedidos de contacto' ),
		'public'          => false,
		'show_ui'         => true,
		'show_in_menu'    => true,
		'menu_icon'       => 'dashicons-email-alt',
		'supports'        => array( 'title', 'editor' ),
		'capability_type' => 'post',
		'capabilities'    => array( 'create_posts' => 'do_not_allow' ),
		'map_meta_cap'    => true,
	) );
} );

add_action( 'rest_api_init', function () {
	register_rest_route( 'hm/v1', '/contacto', array(
		'methods'             => 'POST',
		'permission_callback' => '__return_true',
		'callback'            => 'hm_form_receber',
	) );
} );

function hm_form_receber( WP_REST_Request $req ) {
	$f   = static function ( $k, $max = 200 ) use ( $req ) {
		return mb_substr( trim( sanitize_text_field( (string) $req->get_param( $k ) ) ), 0, $max );
	};
	$err = static function ( $msg, $code = 400 ) {
		return new WP_REST_Response( array( 'ok' => false, 'erro' => $msg ), $code );
	};
	if ( '' !== (string) $req->get_param( 'empresa_url' ) ) {
		return new WP_REST_Response( array( 'ok' => true ), 200 ); // isco preenchido: robô
	}
	$t0 = (int) $req->get_param( 't0' );
	if ( $t0 && ( time() - $t0 ) < 3 ) {
		return $err( 'Envio demasiado rápido.' );
	}
	$ip  = preg_replace( '/[^0-9a-f:.]/i', '', (string) ( $_SERVER['REMOTE_ADDR'] ?? '' ) );
	$key = 'hm_form_' . md5( $ip );
	$n   = (int) get_transient( $key );
	if ( $n >= 5 ) {
		return $err( 'Demasiados envios. Tente mais tarde ou ligue-nos.', 429 );
	}
	$d = array(
		'nome'       => $f( 'nome', 120 ),
		'email'      => sanitize_email( (string) $req->get_param( 'email' ) ),
		'telefone'   => $f( 'telefone', 40 ),
		'website'    => esc_url_raw( (string) $req->get_param( 'website' ) ),
		'localidade' => $f( 'localidade', 120 ),
		'servico'    => $f( 'servico', 80 ),
		'orcamento'  => $f( 'orcamento', 80 ),
		'prazo'      => $f( 'prazo', 80 ),
		'origem'     => $f( 'origem', 80 ),
		'mensagem'   => mb_substr( trim( sanitize_textarea_field( (string) $req->get_param( 'mensagem' ) ) ), 0, 5000 ),
		'pagina'     => $f( 'pagina', 200 ),
	);
	if ( '' === $d['nome'] || ! is_email( $d['email'] ) || '' === $d['mensagem'] ) {
		return $err( 'Preencha o nome, um email válido e a mensagem.' );
	}
	set_transient( $key, $n + 1, 10 * MINUTE_IN_SECONDS );

	$labels = array( 'nome' => 'Nome', 'email' => 'Email', 'telefone' => 'Telefone', 'website' => 'Website', 'localidade' => 'Localidade',
		'servico' => 'Serviço', 'orcamento' => 'Orçamento orientativo', 'prazo' => 'Prazo', 'origem' => 'Como chegou à Hortelã Magenta?',
		'mensagem' => 'Mensagem', 'pagina' => 'Página' );
	$txt = '';
	foreach ( $labels as $k => $l ) {
		if ( '' !== $d[ $k ] ) {
			$txt .= $l . ': ' . $d[ $k ] . "\n";
		}
	}
	$id = wp_insert_post( array(
		'post_type'    => 'hm_pedido',
		'post_status'  => 'private',
		'post_title'   => $d['nome'] . ' · ' . ( $d['servico'] ? $d['servico'] : 'Contacto' ) . ' · ' . wp_date( 'Y-m-d H:i' ),
		'post_content' => $txt,
	) );
	if ( $id && ! is_wp_error( $id ) ) {
		foreach ( $d as $k => $v ) {
			update_post_meta( $id, '_hm_' . $k, $v );
		}
	}
	$to   = get_option( 'hm_form_to', get_option( 'admin_email' ) );
	$sent = wp_mail( $to, 'Novo contacto pelo site · ' . $d['nome'], $txt . "\n— Enviado a partir de " . home_url( '/' ),
		array( 'Reply-To: ' . $d['nome'] . ' <' . $d['email'] . '>' ) );
	if ( $id && ! is_wp_error( $id ) ) {
		update_post_meta( $id, '_hm_email_enviado', $sent ? 'sim' : 'não' );
	}
	return new WP_REST_Response( array( 'ok' => true ), 200 );
}
