<?php
/**
 * Hortelã Magenta · mapa de URL do site novo (fase 2, 2026-11-24).
 *
 * 'paginas'    caminho canónico => pacote de hm-paginas/. A barra final faz parte da URL canónica:
 *              as páginas da web atual (Kirby) não levam barra (/projetos/camolas); as cinco landings levam
 *              (/design-rotulos-vinho/), como na web atual. A variante contrária redireciona com 301.
 * 'noindex'    páginas servidas mas fora do sitemap e com noindex (legais, obrigado, 404).
 * 'redirects'  caminho antigo => destino (301). Inclui a versão inglesa (não há versão EN no site novo),
 *              os redirecionamentos que a web atual já fazia e URL propostas no plano SEO.
 * 'prefixos'   prefixo => destino (301) para rotas nativas do WordPress que não fazem parte do site.
 */
defined( 'ABSPATH' ) || exit;

function hm_rutas() {
	static $r = null;
	if ( null !== $r ) {
		return $r;
	}
	$r = array(
		'paginas'   => array(
			''                                            => 'home.html',
			'servicos'                                    => 'servicos.html',
			'servicos/branding'                           => 'branding.html',
			'servicos/design-web'                         => 'design-web.html',
			'servicos/design-grafico-e-editorial'         => 'servico-grafico-editorial.html',
			'servicos/campanhas-e-redes-sociais'          => 'servico-campanhas.html',
			'servicos/fotografia-e-video'                 => 'servico-fotografia-video.html',
			'servicos/avenca-comunicacao-360'             => 'servico-avenca.html',
			'servicos/coaching-de-marcas'                 => 'servico-coaching.html',
			'projetos'                                    => 'projetos.html',
			'projetos/camolas'                            => 'camolas.html',
			'projetos/consulai'                           => 'projeto-consulai.html',
			'projetos/knowledgebiz'                       => 'projeto-knowledgebiz.html',
			'projetos/queijaria-da-sao'                   => 'projeto-queijaria-da-sao.html',
			'projetos/hospital-garcia-de-orta'            => 'projeto-hospital-garcia-de-orta.html',
			'projetos/croma'                              => 'projeto-croma.html',
			'projetos/alinea'                             => 'projeto-alinea.html',
			'projetos/livro-vilamoura'                    => 'projeto-livro-vilamoura.html',
			'projetos/farinhas-firmos'                    => 'projeto-farinhas-firmos.html',
			'projetos/alsil'                              => 'projeto-alsil.html',
			'projetos/documentos-normativos-imt'          => 'projeto-documentos-normativos-imt.html',
			'projetos/camara-municipal-de-almada-roteiro' => 'projeto-camara-municipal-de-almada-roteiro.html',
			'projetos/imperalum'                          => 'projeto-imperalum.html',
			'design-rotulos-vinho/'                       => 'lp-rotulos-vinho.html',
			'design-comunicacao-industria/'               => 'lp-industria.html',
			'branding-clinicas-dentarias/'                => 'lp-clinicas-dentarias.html',
			'design-administracao-publica/'               => 'lp-administracao-publica.html',
			'design-de-eventos/'                          => 'lp-eventos.html',
			'sobre'                                       => 'sobre.html',
			'blog'                                        => 'blog.html',
			'blog/quanto-custa-um-site'                   => 'artigo.html',
			'contacto'                                    => 'contacto.html',
			'obrigado'                                    => 'obrigado.html',
			'politica-de-privacidade'                     => 'politica-privacidade.html',
			'politica-de-cookies'                         => 'politica-cookies.html',
			'mapa-do-site'                                => 'mapa-do-site.html',
		),
		'noindex'   => array( 'obrigado', 'politica-de-privacidade', 'politica-de-cookies' ),
		'redirects' => array(
			// web atual (Kirby): alias e redirecionamentos que já existiam
			'inicio'                                  => '/',
			'home'                                    => '/',
			'portfolio'                               => '/projetos',
			'contactos'                               => '/contacto',
			'contacts'                                => '/contacto',
			'pedir-orcamento'                         => '/contacto',
			// WordPress: artigo publicado fora de /blog e páginas de rascunho
			'quanto-custa-um-site'                    => '/blog/quanto-custa-um-site',
			'privacy-policy'                          => '/politica-de-privacidade',
			// versão inglesa da web atual -> equivalente em português
			'en'                                      => '/',
			'en/projects'                             => '/projetos',
			'en/projects/consulai'                    => '/projetos/consulai',
			'en/projects/knowledgebiz'                => '/projetos/knowledgebiz',
			'en/projects/queijaria-da-sao'            => '/projetos/queijaria-da-sao',
			'en/projects/camolas'                     => '/projetos/camolas',
			'en/projects/garcia-de-orta-hospital'     => '/projetos/hospital-garcia-de-orta',
			'en/projects/croma'                       => '/projetos/croma',
			'en/projects/alinea'                      => '/projetos/alinea',
			'en/projects/vilamoura-book'              => '/projetos/livro-vilamoura',
			'en/projects/farinhas-firmos'             => '/projetos/farinhas-firmos',
			'en/projects/alsil'                       => '/projetos/alsil',
			'en/projects/normative-documents-imt'     => '/projetos/documentos-normativos-imt',
			'en/projects/camara-municipal-de-almada-roteiro' => '/projetos/camara-municipal-de-almada-roteiro',
			'en/projects/imperalum'                   => '/projetos/imperalum',
			'en/services'                             => '/servicos',
			'en/about'                                => '/sobre',
			'en/contact'                              => '/contacto',
			'en/privacy-policy'                       => '/politica-de-privacidade',
			// URL propostas no plano SEO (documentos de conteúdos) -> páginas publicadas
			'branding-para-empresas'                  => '/servicos/branding',
			'websites-para-empresas'                  => '/servicos/design-web',
			'criacao-de-lojas-online'                 => '/servicos/design-web',
			'design-grafico'                          => '/servicos/design-grafico-e-editorial',
			'design-editorial'                        => '/servicos/design-grafico-e-editorial',
			'design-de-embalagens'                    => '/servicos/design-grafico-e-editorial',
			'producao-de-video'                       => '/servicos/fotografia-e-video',
			'fotografia-de-produto'                   => '/servicos/fotografia-e-video',
			'fotografia-corporativa'                  => '/servicos/fotografia-e-video',
			'campanhas-digitais'                      => '/servicos/campanhas-e-redes-sociais',
			'gestao-de-redes-sociais'                 => '/servicos/campanhas-e-redes-sociais',
			'guias/quanto-custa-um-site'              => '/blog/quanto-custa-um-site',
			'servicos/avencas-mensais'                => '/servicos/avenca-comunicacao-360',
			'servicos/avenca-mensal-360'              => '/servicos/avenca-comunicacao-360',
			'servicos/coaching'                       => '/servicos/coaching-de-marcas',
		),
		'prefixos'  => array(
			'en/'       => '/',
			'category/' => '/blog',
			'tag/'      => '/blog',
			'author/'   => '/sobre',
		),
	);
	return $r;
}
