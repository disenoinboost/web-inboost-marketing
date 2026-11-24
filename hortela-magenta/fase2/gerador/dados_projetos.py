"""Fichas de projeto. Textos: hortelamagenta.pt/projetos/<slug> (descrição do projeto, categorias, imagens e vídeos).
Os títulos e as legendas dos blocos descrevem apenas o que se vê em cada imagem; os testemunhos são os de /sobre."""

# ordem da página Projetos (PAGE.items do desenho) + capas usadas nos cartões
ORDER = ['hospital-garcia-de-orta', 'croma', 'alinea', 'livro-vilamoura', 'farinhas-firmos', 'alsil',
         'documentos-normativos-imt', 'camara-municipal-de-almada-roteiro', 'imperalum', 'camolas', 'consulai',
         'knowledgebiz', 'queijaria-da-sao']
NAMES = {'hospital-garcia-de-orta': 'Hospital Garcia de Orta', 'croma': 'Croma', 'alinea': 'Alinea', 'livro-vilamoura': 'Livro Vilamoura',
         'farinhas-firmos': 'Farinhas Firmos', 'alsil': 'Alsilgroup', 'documentos-normativos-imt': 'Documentos Normativos IMT',
         'camara-municipal-de-almada-roteiro': 'Câmara Municipal de Almada', 'imperalum': 'Imperalum', 'camolas': 'Camolas',
         'consulai': 'Consulai', 'knowledgebiz': 'Knowledgebiz', 'queijaria-da-sao': 'Queijaria da São'}
CARD = {
    'hospital-garcia-de-orta': 'https://hortelamagenta.pt/media/pages/projetos/hospital-garcia-de-orta/c27930cb86-1736937441/hortelamagenta_portfolio_marca_hgo_capa-1200x.jpg',
    'croma': 'https://hortelamagenta.pt/media/pages/projetos/croma/78fb3bf26c-1716976201/hortelamagenta_portfolio_marca_croma_banner_02-2400x.jpg',
    'alinea': 'https://hortelamagenta.pt/media/pages/projetos/alinea/0551698f70-1712332751/hortelamagenta_portfolio_alinea_capa-1200x.jpg',
    'livro-vilamoura': 'https://hortelamagenta.pt/media/pages/projetos/livro-vilamoura/09122571f9-1701272616/livro-vilamoura-cover-1800x.jpg',
    'farinhas-firmos': 'https://hortelamagenta.pt/media/pages/projetos/farinhas-firmos/0d8085f2b6-1733915142/hortelamagenta_portfolio_marca_farinhafirmos_farinha_sacos_02-2400x.jpg',
    'alsil': 'https://hortelamagenta.pt/media/pages/projetos/alsil/d2144ed056-1734532126/alsilgroup_portfolio_marca_display-2400x.jpg',
    'documentos-normativos-imt': 'https://hortelamagenta.pt/media/pages/projetos/documentos-normativos-imt/ed2aa16f83-1736435754/hortelamagenta_portfolio_marca_imt_fasciaculo_capa-1200x.jpg',
    'camara-municipal-de-almada-roteiro': 'https://hortelamagenta.pt/media/pages/projetos/camara-municipal-de-almada-roteiro/ca85983fc0-1737996772/hortelamagenta_portfolio_marca_camera-municipal-de-almada_roteiro_capa-1200x.jpg',
    'imperalum': 'https://hortelamagenta.pt/media/pages/projetos/imperalum/14bf0e96c3-1740759289/hortelamagenta_portfolio_marca_imperalum_banner_02-2400x.jpg',
    'camolas': 'https://hortelamagenta.pt/media/pages/projetos/camolas/68a9f929cc-1736418280/hortelamagenta_portfolio_marca_camolas_cobaia_02-1900x.jpg',
    'consulai': 'https://hortelamagenta.pt/media/pages/projetos/consulai/555bf500a9-1721821692/hortelamagenta_portfolio_marca_consulai_bottle-1900x.jpg',
    'knowledgebiz': 'https://hortelamagenta.pt/media/pages/projetos/knowledgebiz/41d543fd60-1711376064/hortelamagenta_portfolio_marca_knowledgebiz_banner-1900x.jpg',
    'queijaria-da-sao': 'https://hortelamagenta.pt/media/pages/projetos/queijaria-da-sao/d71896b407-1725371731/hortelamagenta_portfolio_marca_queijariadasao_rotulos-1900x.jpg',
}

SVC = {
    'branding': ('/servicos/branding', 'Branding'),
    'web': ('/servicos/design-web', 'Design Web'),
    'grafico': ('/servicos/design-grafico-e-editorial', 'Gráfico + Editorial'),
    'campanhas': ('/servicos/campanhas-e-redes-sociais', 'Campanhas & Redes Sociais'),
    'foto': ('/servicos/fotografia-e-video', 'Fotografia & Vídeo'),
    'industria': ('/design-comunicacao-industria/', 'Design para a indústria'),
    'publica': ('/design-administracao-publica/', 'Design para a administração pública'),
    'eventos': ('/design-de-eventos/', 'Design para eventos'),
}


def projetos(M):
    f = M.find
    I = lambda s, k: f(s, k)
    V = lambda s, k: f(s, k, 'video')

    def vid(s, k, alt):
        src, poster = V(s, k)
        return {'video': src, 'poster': poster, 'alt': alt}

    P = {}

    # --------------------------------------------------------------- Consulai
    s = 'consulai'
    P[s] = dict(
        name='Consulai', cats='Branding, Design Gráfico, Digital, Editorial',
        title='Consulai | Projetos | Hortelã Magenta',
        desc='Identidade visual e comunicação da CONSULAI: um logótipo redesenhado com sol, água e amor, materiais para eventos, editorial, merchandising e redes sociais.',
        lead='A CONSULAI, consultora líder nos setores agroalimentar, agrícola e florestal em Portugal, contou com a nossa experiência para atualizar a sua identidade visual e otimizar a sua comunicação.',
        facts=[('Cliente', 'CONSULAI'), ('Serviços', 'Branding, Design Gráfico, Digital, Editorial'), ('Setor', 'Agroalimentar, agrícola e florestal')],
        ink='Usámos sol, água e amor para redesenhar o logótipo e enriquecer a marca com elementos gráficos complementares.',
        keys=['sol, água e amor', 'elementos gráficos complementares'],
        more='De seguida, desenvolvemos uma estratégia de comunicação completa, que abrange materiais para eventos, anúncios publicitários, projetos editoriais, peças de merchandising, uma abordagem renovada para as redes sociais e novos materiais de comunicação interna.',
        cover=(I(s, 'consulai_slogan_foto'), 'Campanha «Na natureza do seu negócio» da CONSULAI'),
        services=['branding', 'grafico', 'campanhas'],
        ident=dict(title='Identidade visual', intro='Sol, água e amor no logótipo e em todos os elementos da marca.', tabs=[
            dict(img=I(s, 'consulai_logo_01'), title='Logótipo', sub='Rebranding', desc='O logótipo redesenhado, aplicado sobre o verde da marca.'),
            dict(img=I(s, 'consulai_logo_cores'), title='Cores', sub='Paleta', desc='As versões da marca em fundos claros e escuros.'),
            dict(img=I(s, 'consulai_font'), title='Tipografia', sub='Família tipográfica'),
            dict(img=I(s, 'consulai_icons-950x'), title='Elementos', sub='Grafismos complementares', desc='Elementos gráficos que enriquecem a marca e se repetem nas aplicações.', pos='50% 30%'),
        ]),
        apps=dict(eyebrow='Comunicação', title='Uma estratégia de comunicação completa', items=[
            dict(img=I(s, 'consulai_estacionario'), title='Estacionário'),
            dict(img=I(s, 'consulai_folhete'), title='Folheto'),
            dict(img=I(s, 'consulai_banner-1900x'), title='Anúncios'),
            dict(img=I(s, 'consulai_banner_02'), title='Campanha'),
            dict(img=I(s, 'consulai_rollup'), title='Roll-ups'),
            dict(img=I(s, 'consulai_badge'), title='Crachá', pos='50% 40%'),
            dict(img=I(s, 'consulai_bag'), title='Saco'),
            dict(img=I(s, 'consulai_bottle'), title='Garrafa'),
            dict(img=I(s, 'consulai_wall_logo'), title='Sinalética'),
        ]),
        gallery=dict(title='Digital e redes sociais', intro='Uma abordagem renovada para as redes sociais.', items=[
            vid(s, 'consulai_rs_01', 'Publicações da CONSULAI nas redes sociais'),
            dict(img=I(s, 'consulai_redes_sociais_02'), alt='Grelha de publicações da CONSULAI'),
            vid(s, 'consulai_logo_03', 'Animação do logótipo da CONSULAI'),
            dict(img=I(s, 'consulai_icons_02'), alt='Elementos gráficos da CONSULAI'),
            dict(img=I(s, 'consulai_slogan_foto'), alt='«Na natureza do seu negócio» — campanha da CONSULAI'),
        ]),
        testimonial=dict(headline='Respeito, Confiança e Profissionalismo.', quote='Encontrámos a Hortelã Magenta, por um acaso, no meio de diversas outras empresas de comunicação, em 2014. Mas desde logo percebemos que queríamos trabalhar com eles. Temos desenvolvido uma relação que assenta em 3 pilares fundamentais: Respeito, Confiança e Profissionalismo. Muito obrigada a toda a equipa e por todo o vosso trabalho!',
                         name='Marta Mendes', company='CONSULAI', role='Consultora Sénior, Inovação e Investigação · Coordenadora de Comunicação Institucional',
                         img=I(s, 'consulai_bag'), img_alt='Saco com a identidade da CONSULAI'),
        contact='Conte-nos o que faz a sua empresa, em que momento está a marca e o que precisa de comunicar: identidade, materiais para eventos, publicações ou redes sociais. Se já tem uma imagem, partilhe-a também para conhecermos o ponto de partida.',
    )

    # --------------------------------------------------------------- Knowledgebiz
    s = 'knowledgebiz'
    P[s] = dict(
        name='Knowledgebiz', cats='Branding, Design Gráfico, Digital',
        title='Knowledgebiz | Projetos | Hortelã Magenta',
        desc='Rebranding da Knowledgebiz: uma marca impactante e atual, aplicada a estacionário, folhetos, cartazes, roll-ups e a um website que reforça a presença online.',
        lead='O rebranding da Knowledgebiz, uma empresa de referência em inovação tecnológica, foi uma oportunidade para reposicionar a marca para o futuro.',
        facts=[('Cliente', 'Knowledgebiz'), ('Serviços', 'Branding, Design Gráfico, Digital'), ('Setor', 'Inovação tecnológica')],
        ink='A nova marca é impactante e atual, transmitindo dinamismo e conectividade digital.',
        keys=['impactante e atual', 'conectividade digital'],
        more='Estendemos a nova identidade visual a vários materiais, incluindo estacionário, folhetos, cartazes e roll-ups, bem como um website, capaz de potenciar a presença online da marca.',
        cover=(I(s, 'knowledgebiz_estacionario'), 'Estacionário da Knowledgebiz com a nova identidade'),
        services=['branding', 'web', 'grafico'],
        ident=dict(title='Identidade visual', intro='Uma marca que transmite dinamismo e conectividade digital.', tabs=[
            dict(img=I(s, 'knowledgebiz_logo_04'), title='Logótipo', sub='Rebranding', desc='A nova assinatura «Innovate your life».'),
            dict(img=I(s, 'knowledgebiz_logo_01'), title='Símbolo', sub='Construção'),
            dict(img=I(s, 'knowledgebiz_logo_03'), title='Tipografia', sub='Família tipográfica'),
            dict(img=I(s, 'knowledgebiz_cor'), title='Cores', sub='Paleta'),
        ]),
        apps=dict(eyebrow='Aplicações', title='A nova identidade em vários materiais', items=[
            dict(img=I(s, 'knowledgebiz_estacionario'), title='Estacionário'),
            dict(img=I(s, 'knowledgebiz_banner'), title='Cartazes'),
            dict(img=I(s, 'knowledgebiz_bloco-de-notas'), title='Bloco de notas'),
            dict(img=I(s, 'knowledgebiz_id-badge'), title='Crachá'),
            dict(img=I(s, 'knowledgebiz_icons'), title='Ícones'),
            dict(img=I(s, 'knowledgebiz_mobile_01'), title='Digital'),
        ]),
        gallery=dict(title='Website', intro='Um website capaz de potenciar a presença online da marca.', link=('/servicos/design-web', 'Criação de sites para empresas →'), items=[
            dict(img=I(s, 'knowledgebiz_site_01'), alt='Website da Knowledgebiz em computador e telemóvel'),
            vid(s, 'knowledgebiz_site_02', 'Navegação no website da Knowledgebiz'),
            dict(img=I(s, 'knowledgebiz_site_05'), alt='Páginas do website da Knowledgebiz'),
            vid(s, 'knowledgebiz_mobile_02', 'Website da Knowledgebiz em telemóvel'),
            dict(img=I(s, 'knowledgebiz_site_03'), alt='Página de contacto do website da Knowledgebiz'),
            dict(img=I(s, 'knowledgebiz_foto'), alt='Fotografia de equipa da Knowledgebiz'),
        ]),
        contact='Conte-nos o que faz a sua empresa e em que momento está a marca. Se o projeto inclui um site, partilhe também o endereço atual para conhecermos o ponto de partida.',
    )

    # --------------------------------------------------------------- Queijaria da São
    s = 'queijaria-da-sao'
    P[s] = dict(
        name='Queijaria da São', cats='Branding, Vídeo, Fotografia, Digital, Design Gráfico', h1size='clamp(36px,7.2vw,140px)',
        title='Queijaria da São | Projetos | Hortelã Magenta',
        desc='Com 50 anos de história, a Queijaria da São modernizou a imagem sem esquecer a tradição: logótipo, rótulos, packaging, fardas, redes sociais, website e vídeo.',
        lead='Com 50 anos de história, a Queijaria da São convidou-nos a modernizar a sua imagem sem esquecer a tradição.',
        facts=[('Cliente', 'Queijaria da São'), ('Serviços', 'Branding, Vídeo, Fotografia, Digital, Design Gráfico'), ('História', '50 anos')],
        ink='Criámos um novo logótipo, mais atual, apelativo e acolhedor, bem como uma forma de comunicar.',
        keys=['mais atual, apelativo e acolhedor', 'uma forma de comunicar'],
        more='Atualizou-se o estacionário gráfico, os rótulos, o packaging, as fardas e as embalagens originais. Desenvolvemos também a comunicação nas redes sociais, o website e um vídeo institucional que reflete a paixão e o saber-fazer da marca.',
        cover=(I(s, 'queijariadasao_foto_06'), 'Queijo da Queijaria da São fotografado sobre ardósia'),
        services=['branding', 'foto', 'web', 'industria'],
        ident=dict(title='Identidade visual', intro='Um logótipo mais atual, apelativo e acolhedor, sem esquecer a tradição.', tabs=[
            dict(img=I(s, 'queijariadasao_logo_01'), title='Logótipo', sub='Antes e depois', desc='Da marca anterior ao novo logótipo.'),
            dict(img=I(s, 'queijariadasao_logo_02'), title='Cores', sub='Paleta'),
            dict(img=I(s, 'queijariadasao_animais'), title='Ilustração', sub='Tipografia e animais'),
            dict(img=I(s, 'queijariadasao_logo_04'), title='Universo', sub='Imagem da marca'),
        ]),
        apps=dict(eyebrow='Packaging e aplicações', title='Rótulos, embalagens e fardas', link=('/design-comunicacao-industria/', 'Design para a indústria →'), items=[
            dict(img=I(s, 'queijariadasao_rotulos'), title='Rótulos'),
            dict(img=I(s, 'queijariadasao_cartao'), title='Cartão de visita'),
            dict(img=I(s, 'queijariadasao_foto_05'), title='Embalagens'),
            dict(img=I(s, 'queijariadasao_merchandising_01'), title='Fardas', pos='50% 30%'),
            dict(img=I(s, 'queijariadasao_merchandising_02'), title='Merchandising'),
            dict(img=I(s, 'queijariadasao_rollup'), title='Roll-ups'),
            dict(img=I(s, 'queijariadasao_veiculo'), title='Viatura'),
        ]),
        film=dict(src=V(s, 'super-short-queijaria')[0], poster=V(s, 'super-short-queijaria')[1], title='Vídeo institucional', text='A paixão e o saber-fazer da marca.', word='Queijaria da São', label='Queijaria da São', aria='Vídeo institucional da Queijaria da São'),
        gallery=dict(title='Fotografia e digital', intro='Fotografia de produto, redes sociais e website.', items=[
            dict(img=I(s, 'queijariadasao_foto_02'), alt='Queijos frescos da Queijaria da São'),
            dict(img=I(s, 'queijariadasao_foto_03'), alt='Embalagem de queijo da Queijaria da São'),
            vid(s, 'queijariadasao_queijos', 'Queijo da Queijaria da São em fundo claro'),
            dict(img=I(s, 'queijariadasao_foto_01'), alt='Produção na Queijaria da São'),
            vid(s, 'queijariadasao_post', 'Publicações da Queijaria da São nas redes sociais'),
            dict(img=I(s, 'queijariadasao_site_01'), alt='Website da Queijaria da São'),
            vid(s, 'queijariadasao_site_03', 'Navegação no website da Queijaria da São'),
            dict(img=I(s, 'queijariadasao_site_02'), alt='Páginas do website da Queijaria da São'),
        ]),
        contact='Conte-nos a história da sua marca e o que precisa de comunicar: rótulos e embalagens, fotografia, vídeo ou site. Se já tem uma imagem, partilhe-a também para conhecermos o ponto de partida.',
    )

    # --------------------------------------------------------------- Hospital Garcia de Orta
    s = 'hospital-garcia-de-orta'
    P[s] = dict(
        name='Hospital Garcia de Orta', cats='Branding, Design Gráfico', h1size='clamp(36px,6.4vw,124px)',
        title='Hospital Garcia de Orta | Projetos | Hortelã Magenta',
        desc='Rebranding do Hospital Garcia de Orta: a ligação ao rio Tejo, a humanização da marca num coração e a assinatura «A referência a Sul».',
        lead='Os valores de uma marca devem refletir a sua identidade e estrutura.',
        facts=[('Cliente', 'Hospital Garcia de Orta'), ('Serviços', 'Branding, Design Gráfico'), ('Posicionamento', '«A referência a Sul»')],
        ink='Para o Hospital Garcia de Orta, era importante manter a conexão com o rio Tejo. A humanização da marca foi simbolizada por um coração, dando-lhe nova vida.',
        keys=['a conexão com o rio Tejo', 'um coração'],
        more='O rebranding exige total compromisso da agência, especialmente em organizações com 30 anos de história. É essencial entender o funcionamento da instituição, respeitar o passado e potenciar o futuro. Em parceria com o Conselho de Administração, a frase «A referência a Sul» reforça o posicionamento da marca no mercado.',
        cover=(I(s, 'hgo_logo_04'), 'Aplicação da nova marca do Hospital Garcia de Orta'),
        services=['branding', 'grafico', 'publica'],
        ident=dict(title='Identidade visual', intro='O rio Tejo e um coração na nova marca.', tabs=[
            dict(img=I(s, 'hgo_logo_02'), title='Símbolo', sub='Rio e coração', desc='A humanização da marca, simbolizada por um coração.'),
            dict(img=I(s, 'hgo_logo_cor'), title='Cores', sub='Paleta'),
            dict(img=I(s, 'hgo_frase'), title='Assinatura', sub='«A referência a Sul»', desc='A frase que reforça o posicionamento da marca.', ph=True),
            dict(img=I(s, 'hgo_logo_01'), title='Logótipo', sub='Versão principal', ph=True),
        ]),
        apps=dict(eyebrow='Aplicações', title='Uma marca com nova vida', link=('/design-administracao-publica/', 'Design para a administração pública →'), items=[
            dict(img=I(s, 'hgo_estacionario'), title='Estacionário'),
            dict(img=I(s, 'hgo_a4'), title='Papel de carta'),
            dict(img=I(s, 'hgo_badge'), title='Crachá'),
            dict(img=I(s, 'hgo_pin'), title='Pins'),
            dict(img=I(s, 'hgo_rollup'), title='Roll-up'),
            dict(img=I(s, 'hgo_ilustracao-1900x'), title='Ilustração'),
        ]),
        gallery=dict(title='Ilustração e fotografia', intro='Respeitar o passado e potenciar o futuro.', items=[
            dict(img=I(s, 'hgo_ilustracao_02'), alt='Ilustração com o hospital e a cidade'),
            dict(img=I(s, 'hgo_foto_01'), alt='Equipa do Hospital Garcia de Orta'),
            dict(img=I(s, 'hgo_logo_03'), alt='Animação do símbolo do Hospital Garcia de Orta'),
            dict(img=I(s, 'hgo_logo_04'), alt='Marca do Hospital Garcia de Orta aplicada'),
        ]),
        contact='Conte-nos o que faz a sua instituição, em que momento está a marca e o que precisa de comunicar. Se já tem uma imagem, partilhe-a também para conhecermos o ponto de partida.',
    )

    # --------------------------------------------------------------- Croma
    s = 'croma'
    P[s] = dict(
        name='Croma', cats='Branding, Digital, Vídeo',
        title='Croma | Projetos | Hortelã Magenta',
        desc='Identidade visual do CROMA, Ciclo de Música Contemporânea de Oeiras: um logótipo irreverente, cartazes, anúncios, merchandising, redes sociais e vídeos para TV.',
        lead='A missão era clara: criar uma identidade visual atual e dinâmica para o CROMA – Ciclo de Música Contemporânea de Oeiras.',
        facts=[('Cliente', 'CROMA'), ('Serviços', 'Branding, Digital, Vídeo'), ('Evento', 'Ciclo de Música Contemporânea de Oeiras')],
        ink='Desenvolvemos um logótipo irreverente e cativante que transmite a energia e a singularidade do evento.',
        keys=['irreverente e cativante', 'a energia e a singularidade'],
        more='O CROMA tem como objetivo promover a música contemporânea portuguesa. Com o objetivo de amplificar a presença da marca e atrair público, criámos uma série de materiais promocionais, como cartazes, anúncios, merchandising, conteúdos para as redes sociais e vídeos institucionais para TV.',
        cover=(I(s, 'croma_banner_04'), 'Identidade do CROMA projetada em palco'),
        services=['branding', 'campanhas', 'foto', 'eventos'],
        ident=dict(title='Identidade visual', intro='A energia e a singularidade do evento num logótipo.', tabs=[
            dict(img=I(s, 'croma_logo_02'), title='Logótipo', sub='Animação', desc='Um logótipo irreverente e cativante.', ph=True),
            dict(img=I(s, 'croma_cor'), title='Cores', sub='Paleta'),
            dict(img=I(s, 'croma_font'), title='Tipografia', sub='Artico'),
            dict(img=I(s, 'croma_foto'), title='Música', sub='Fotografia'),
        ]),
        apps=dict(eyebrow='Materiais promocionais', title='Amplificar a presença da marca', link=('/design-de-eventos/', 'Design de comunicação para eventos →'), items=[
            dict(img=I(s, 'croma_banner_01'), title='Cartazes'),
            dict(img=I(s, 'croma_banner_02'), title='Série de cartazes'),
            dict(img=I(s, 'croma_banner_03'), title='Mupi'),
            dict(img=I(s, 'croma_programa'), title='Programa'),
            dict(img=I(s, 'croma_tickets'), title='Bilhetes'),
            dict(img=I(s, 'croma_badge'), title='Credenciais'),
            dict(img=I(s, 'croma_bag'), title='Saco'),
            dict(img=I(s, 'croma_tshirt_pin'), title='T-shirt e pins'),
        ]),
        film=dict(src=V(s, 'croma-2023')[0], poster=V(s, 'croma-2023')[1], title='Vídeo para TV', text='Um dos vídeos institucionais criados para televisão.', word='CROMA', label='CROMA', aria='Vídeo institucional do CROMA para televisão'),
        gallery=dict(title='Redes sociais', intro='Conteúdos para atrair público.', items=[
            dict(img=I(s, 'croma_rs_01'), alt='Publicações do CROMA nas redes sociais'),
            vid(s, 'croma_rs_02', 'Publicação animada do CROMA em telemóvel'),
            dict(img=I(s, 'croma_logo_01'), alt='Animação do logótipo do CROMA'),
            dict(img=I(s, 'croma_banner_04'), alt='Identidade do CROMA em palco'),
        ]),
        contact='Conte-nos o que vai acontecer, para quem e onde: identidade, cartazes, materiais impressos, redes sociais ou vídeo. Com essa base ajudamos a definir o trabalho.',
    )

    # --------------------------------------------------------------- Alinea
    s = 'alinea'
    P[s] = dict(
        name='Alinea', cats='Branding, Digital, Fotografia, Vídeo, Design Gráfico',
        title='Alinea | Projetos | Hortelã Magenta',
        desc='Desde 2017 parceiros da Alinea – premium oral care. Um rebranding inspirado no mar, na fluidez das formas e no mantra «menos é mais».',
        lead='Uma história que vai além do design: um percurso de crescimento sustentável, construído com profissionalismo e confiança.',
        facts=[('Cliente', 'Alinea – premium oral care'), ('Serviços', 'Branding, Digital, Fotografia, Vídeo, Design Gráfico'), ('Parceria', 'Desde 2017')],
        ink='Entre as inúmeras ações gráficas que o grupo nos confia diariamente, destacamos o Rebranding – um projeto inspirado no mar, na fluidez das formas e no nosso mantra: «menos é mais».',
        keys=['inspirado no mar', '«menos é mais»'],
        more='Desde 2017, somos Alinea – premium oral care. Mais do que uma agência, somos parceiros. Mais do que fornecedores, somos clientes. E, inevitavelmente, a amizade tornou-se parte deste caminho. A simplicidade tornou-se a essência da marca, traduzindo visualmente a sofisticação e excelência que definem a Alinea.',
        cover=(I(s, 'alinea_estacionario'), 'Estacionário da Alinea'),
        services=['branding', 'web', 'foto'],
        ident=dict(title='Identidade visual', intro='A simplicidade como essência da marca.', tabs=[
            dict(img=V(s, 'alinea_logo')[1], title='Logótipo', sub='Rebranding', desc='Um rebranding inspirado no mar e na fluidez das formas.'),
            dict(img=I(s, 'alinea_simbolo'), title='Símbolo', sub='Versões'),
            dict(img=V(s, 'alinea_padrao')[1], title='Padrão', sub='Elemento gráfico'),
            dict(img=I(s, 'alinea_cores'), title='Cores', sub='Paleta'),
        ]),
        apps=dict(eyebrow='Aplicações', title='As ações gráficas de todos os dias', items=[
            dict(img=I(s, 'alinea_cartao'), title='Cartões de visita'),
            dict(img=I(s, 'alinea_estacionario'), title='Estacionário'),
            dict(img=I(s, 'alinea_anuncio'), title='Anúncio'),
            dict(img=I(s, 'alinea_flyer'), title='Flyer'),
            dict(img=I(s, 'alinea_saco'), title='Saco'),
            dict(img=I(s, 'alinea_banner'), title='Mupi'),
        ]),
        gallery=dict(title='Fotografia, vídeo e digital', intro='Imagem própria, redes sociais e website.', link=('https://vimeo.com/915134544', 'Ver o filme da Alinea no Vimeo →'), items=[
            dict(img=I(s, 'alinea_foto_01'), alt='Receção de uma clínica Alinea'),
            dict(img=I(s, 'alinea_foto_02'), alt='Consultório de uma clínica Alinea'),
            vid(s, 'alinea_redes_sociais', 'Publicações da Alinea nas redes sociais'),
            dict(img=I(s, 'alinea_site_01'), alt='Website da Alinea'),
            vid(s, 'alinea_site_02', 'Navegação no website da Alinea'),
            dict(img=I(s, 'alinea_site_03'), alt='Website da Alinea em computador e telemóvel'),
            vid(s, 'alinea_site_04', 'Website da Alinea em vários ecrãs'),
            dict(img=I(s, 'alinea_foto_03'), alt='Espaço de uma clínica Alinea'),
        ]),
        contact='Conte-nos o que faz a sua empresa, em que momento está a marca e o que precisa de comunicar. Se já tem uma imagem, partilhe-a também para conhecermos o ponto de partida.',
    )

    # --------------------------------------------------------------- Livro Vilamoura
    s = 'livro-vilamoura'
    P[s] = dict(
        name='Livro Vilamoura', cats='Editorial',
        title='Livro Vilamoura | Projetos | Hortelã Magenta',
        desc='Livro Vilamoura: um projeto editorial de linguagem simples, sem ser simplista, que levou ao limite a produção gráfica, com cadernos diferentes em papel, textura e dimensão.',
        lead='Um projeto desafiante, de linguagem simples, sem ser simplista, onde levámos ao limite a possibilidade técnica de produção gráfica.',
        facts=[('Projeto', 'Livro Vilamoura'), ('Serviço', 'Design Editorial'), ('Produção', 'Cadernos com papéis, texturas e dimensões diferentes')],
        ink='Criou-se interatividade, ainda que analógica, entre leitor e a estória, fazendo os cadernos casarem matematicamente com o desenrolar da ação e diferenciando-os em papel, texturas e dimensão.',
        keys=['interatividade, ainda que analógica', 'casarem matematicamente'],
        cover=(I(s, 'livro-vilamoura-cover'), 'Livro Vilamoura nas mãos de um leitor'),
        services=['grafico', 'publica'],
        apps=dict(eyebrow='O livro', title='Cadernos que acompanham a ação', link=('/servicos/design-grafico-e-editorial', 'Design gráfico e editorial →'), items=[
            dict(img=I(s, 'livro-vilamoura-img_01'), title='Abertura'),
            dict(img=I(s, 'livro-vilamoura-img_04'), title='Índice'),
            dict(img=I(s, 'livro-vilamoura-img_05'), title='Cadernos'),
            dict(img=I(s, 'livro-vilamoura-img_06'), title='Retratos'),
            dict(img=I(s, 'livro-vilamoura-img_07'), title='Paginação'),
            dict(img=I(s, 'livro-vilamoura-img_08'), title='Paisagem'),
            dict(img=I(s, 'livro-vilamoura-img_09'), title='Capa e lombada'),
        ]),
        gallery=dict(title='Produção gráfica', intro='Papéis, texturas e dimensões diferentes.', link=('https://vimeo.com/395402280', 'Ver o vídeo do livro no Vimeo →'), items=[
            dict(img=I(s, 'livro-vilamoura-img_02'), alt='Leitor a folhear o Livro Vilamoura'),
            dict(img=I(s, 'livro-vilamoura-img_03'), alt='Páginas interiores do Livro Vilamoura'),
            dict(img=I(s, 'livro-vilamoura-img_10'), alt='Livro Vilamoura sobre uma mesa'),
            dict(img=I(s, 'livro-vilamoura-cover'), alt='Capa do Livro Vilamoura'),
        ]),
        contact='Conte-nos que publicação está a preparar, a extensão aproximada, o estado dos conteúdos e a data prevista. Com essa informação definimos o trabalho editorial.',
    )

    # --------------------------------------------------------------- Farinhas Firmos
    s = 'farinhas-firmos'
    P[s] = dict(
        name='Farinhas Firmos', cats='Branding, Design Gráfico, Vídeo, Fotografia, Digital',
        title='Farinhas Firmos | Projetos | Hortelã Magenta',
        desc='Um projeto 360º para o 30.º aniversário da Farinhas Firmos: marca, estacionário, packaging, redes sociais, website, sessões fotográficas e vídeo corporativo.',
        lead='Respeitar o passado, celebrar o trigésimo aniversário e evoluir.',
        facts=[('Cliente', 'Farinhas Firmos'), ('Serviços', 'Branding, Design Gráfico, Vídeo, Fotografia, Digital'), ('Ocasião', '30.º aniversário')],
        ink='Um projeto 360º, que muda a forma como a Farinhas Firmos se apresenta aos clientes. Marca, estacionário, merchandising, packaging, presença digital nas redes sociais e website.',
        keys=['projeto 360º', 'se apresenta aos clientes'],
        more='Através de sessões fotográficas impactantes e da produção de um vídeo corporativo, transmitimos com emoção os valores e a missão da empresa.',
        cover=(I(s, 'farinhafirmos_fabrica-1900x'), 'Fábrica da Farinhas Firmos entre campos'),
        services=['branding', 'web', 'foto', 'industria'],
        film=dict(src=V(s, '30_anosfirmos')[0], poster=V(s, '30_anosfirmos')[1], title='Vídeo corporativo', text='Os valores e a missão da empresa, transmitidos com emoção.', word='Farinhas Firmos', label='Farinhas Firmos', aria='Vídeo corporativo dos 30 anos da Farinhas Firmos'),
        ident=dict(title='Identidade visual', intro='Respeitar o passado e evoluir.', tabs=[
            dict(img=I(s, 'farinhafirmos_simbolo'), title='Símbolo', sub='Rebranding', ph=True),
            dict(img=I(s, 'farinhafirmos_cor'), title='Cores', sub='Paleta'),
            dict(img=I(s, 'farinhafirmos_font'), title='Tipografia', sub='Din Pro'),
            dict(img=I(s, 'farinhafirmos_farinha_sacos_02-1900x'), title='Packaging', sub='Sacos de farinha', desc='A nova marca aplicada à gama de farinhas.'),
        ]),
        apps=dict(eyebrow='Packaging e aplicações', title='Uma nova forma de se apresentar', link=('/design-comunicacao-industria/', 'Design para a indústria →'), items=[
            dict(img=I(s, 'farinhafirmos_farinha_sacos_02.gif'), title='Embalagem'),
            dict(img=V(s, 'farinha_sacos_03')[1], title='Gama de farinhas'),
            dict(img=I(s, 'farinhafirmos_flyer'), title='Folhetos'),
            dict(img=I(s, 'farinhafirmos_calendario'), title='Calendário'),
            dict(img=I(s, 'farinhafirmos_redessociais_02'), title='Redes sociais'),
        ]),
        gallery=dict(title='Fotografia e website', intro='Sessões fotográficas e presença digital.', items=[
            dict(img=I(s, 'firmos_20210825'), alt='Armazém da Farinhas Firmos'),
            dict(img=I(s, 'farinhafirmos_fabrica_11'), alt='Interior da fábrica da Farinhas Firmos'),
            dict(img=I(s, 'farinhafirmos_fabrica_09'), alt='Silos da Farinhas Firmos'),
            vid(s, 'farinhafirmos_redessociais_01', 'Publicação animada da Farinhas Firmos nas redes sociais'),
            vid(s, 'farinhafirmos_site_01', 'Abertura do website da Farinhas Firmos'),
            dict(img=I(s, 'farinhafirmos_site_05'), alt='Website da Farinhas Firmos em computador e telemóvel'),
            dict(img=I(s, 'farinhafirmos_site_06'), alt='Páginas do website da Farinhas Firmos'),
            vid(s, 'farinhafirmos_site_02', 'Navegação no website da Farinhas Firmos'),
        ]),
        testimonial=dict(headline='Sempre disponíveis e com soluções completas.', quote='Nos últimos anos tivemos a oportunidade de trabalhar com a agência Hortelã Magenta. Nas diversas solicitações e situações de trabalho desenvolvidas, encontramos uma equipa continuamente motivada para colaborar, para discutir e compartilhar ideias e para transformar problemas em oportunidades. Sempre disponíveis e com soluções completas, diferenciam-se pela sua imagem única, e o entusiasmo e atenção ao detalhe no trabalho que apresentam fazem com que a sua marca seja sentida em qualquer projeto que lhes seja contratado. Recomendam-se vivamente!',
                         name='Luís Firmo', company='Farinhas Firmos', role='RH e I&D, Gestor Projeto',
                         img=I(s, 'farinhafirmos_fabrica_11'), img_alt='Interior da fábrica da Farinhas Firmos'),
        contact='Conte-nos o que faz a sua empresa e o que quer comunicar: uma data especial, uma nova gama ou toda a imagem. Podemos trabalhar a marca, o packaging, a fotografia, o vídeo e o site num mesmo projeto.',
    )

    # --------------------------------------------------------------- Alsil
    s = 'alsil'
    P[s] = dict(
        name='Alsilgroup', cats='Branding, Digital, Fotografia, Vídeo, Design Gráfico',
        title='Alsilgroup | Projetos | Hortelã Magenta',
        desc='Para o 100.º aniversário do Alsil Group, uma identidade moderna e coesa, inspirada em formas geométricas e numa gama cromática vibrante, dos cartões de visita aos stands.',
        lead='O Alsil Group, especialmente dedicado à indústria metalomecânica, inclui as marcas Alsil, Stockfer, Hstools e Triaxis.',
        facts=[('Cliente', 'Alsil Group'), ('Serviços', 'Branding, Digital, Fotografia, Vídeo, Design Gráfico'), ('Ocasião', '100.º aniversário')],
        ink='Para celebrar o seu 100.º aniversário, desenvolvemos uma nova identidade com uma linguagem gráfica moderna e coesa, inspirada em formas geométricas e acompanhada por uma gama cromática vibrante.',
        keys=['moderna e coesa', 'formas geométricas', 'gama cromática vibrante'],
        more='O resultado é uma imagem global mais forte e atual, que se estende a todos os materiais de comunicação, desde os distintos cartões de visita até aos espaços impactantes em exposições internacionais.',
        cover=(I(s, 'alsilgroup_fabrica_01'), 'Fábrica do Alsil Group'),
        services=['branding', 'web', 'foto', 'industria'],
        ident=dict(title='Identidade visual', intro='Uma linguagem gráfica comum às marcas do grupo.', tabs=[
            dict(img=I(s, 'alsilgroup_logo_02'), title='Logótipo', sub='Alsil Group', desc='A marca do grupo, na versão principal.'),
            dict(img=I(s, 'alsilgroup_logo_05'), title='Símbolos', sub='Formas geométricas', desc='Os símbolos das marcas, a partir das mesmas formas geométricas.'),
            dict(img=I(s, 'alsilgroup_cor'), title='Cores', sub='Uma cor por marca', desc='Uma gama cromática vibrante que distingue cada marca.'),
            dict(img=I(s, 'alsilgroup_portfolio_marca_font'), title='Tipografia', sub='Família tipográfica'),
        ]),
        apps=dict(eyebrow='Comunicação', title='Dos cartões de visita às exposições internacionais', link=('/design-comunicacao-industria/', 'Design para a indústria →'), items=[
            dict(img=I(s, 'alsilgroup_cartao-de-visita'), title='Cartões de visita'),
            dict(img=V(s, 'alsilgroup_estacionario')[1], title='Estacionário'),
            dict(img=I(s, 'alsilgroup_portfolio_marca_calendario'), title='Calendário'),
            dict(img=V(s, 'alsilgroup_flyer')[1], title='Folheto'),
            dict(img=I(s, 'badge_cracha'), title='Crachá'),
            dict(img=I(s, 'alsilgroup_portfolio_marca_display'), title='Display'),
            dict(img=I(s, 'alsilgroup_portfolio_marca_stand'), title='Stand'),
        ]),
        film=dict(src=V(s, 'alsilgroup_video')[0], poster=V(s, 'alsilgroup_video')[1], title='Vídeo', text='As marcas do grupo com a nova identidade.', word='Alsil Group', label='Alsil Group', aria='Vídeo com as marcas do Alsil Group'),
        gallery=dict(title='Fotografia e digital', intro='A fábrica, as pessoas e o site.', items=[
            dict(img=I(s, 'alsilgroup_fabrica_02'), alt='Montagem de peças na fábrica do Alsil Group'),
            dict(img=I(s, 'alsilgroup_fabrica_07'), alt='Técnico na fábrica do Alsil Group'),
            dict(img=I(s, 'alsilgroup_fabrica_04'), alt='Máquinas na fábrica do Alsil Group'),
            dict(img=I(s, 'alsilgroup_fabrica_06'), alt='Maquinação de uma peça metálica'),
            dict(img=I(s, 'alsilgroup_fabrica_08'), alt='Equipa do Alsil Group na fábrica'),
            vid(s, 'alsilgroup_site', 'Website do Alsil Group'),
            dict(img=I(s, 'phone-mockup-hand'), alt='Website do Alsil Group em telemóvel'),
            vid(s, 'alsilgroup_logo_01', 'Animação do logótipo do Alsil Group'),
        ]),
        contact='Conte-nos o que faz a sua empresa e o que precisa de comunicar: marca, catálogos, stands, fotografia, vídeo ou site. Com essa base ajudamos a definir o trabalho.',
    )

    # --------------------------------------------------------------- IMT
    s = 'documentos-normativos-imt'
    P[s] = dict(
        name='Documentos Normativos IMT', cats='Editorial, Design Gráfico', h1size='clamp(36px,6.4vw,124px)',
        title='Documentos Normativos IMT | Projetos | Hortelã Magenta',
        desc='Quatro documentos normativos para arruamentos urbanos, desenvolvidos para o IMT, que equilibram a complexidade técnica com clareza e harmonia visual.',
        lead='Neste projeto para o IMT (Instituto da Mobilidade e dos Transportes), desenvolveram-se quatro documentos normativos para aplicação em arruamentos urbanos.',
        facts=[('Cliente', 'IMT — Instituto da Mobilidade e dos Transportes'), ('Serviços', 'Editorial, Design Gráfico'), ('Âmbito', 'Quatro documentos normativos')],
        ink='O principal desafio foi equilibrar a complexidade técnica com a clareza e harmonia visual.',
        keys=['a complexidade técnica', 'clareza e harmonia visual'],
        more='Atribuiu-se uma cor distinta a cada documento para facilitar a sua consulta, e enriquecemos o conteúdo com ilustrações técnicas, tabelas e elementos gráficos com uma linguagem coesa, de forma a tornar a leitura mais fluída, intuitiva e agradável.',
        cover=(I(s, 'imt_fasciaculo_livro_02'), 'Os quatro documentos normativos do IMT, cada um com a sua cor'),
        services=['grafico', 'publica'],
        apps=dict(eyebrow='Os documentos', title='Uma cor para cada documento', link=('/servicos/design-grafico-e-editorial', 'Design gráfico e editorial →'), items=[
            dict(img=I(s, 'imt_fasciaculo_livro_01'), title='Páginas interiores'),
            dict(img=I(s, 'imt_fasciaculo_foto_01'), title='Documento 1'),
            dict(img=I(s, 'imt_fasciaculo_livro_05'), title='Documento 2'),
            dict(img=I(s, 'imt_fasciaculo_livro_06'), title='Tabelas e ilustrações'),
            dict(img=V(s, 'livro_07_hortela-magenta-instituto-da-mobilidade-e-transportes-web')[1], title='Ilustrações técnicas'),
            dict(img=I(s, 'imt_fasciaculo_livro_04'), title='Leitura'),
        ]),
        gallery=dict(title='Ilustração técnica', intro='Uma linguagem gráfica coesa em todos os documentos.', items=[
            dict(img=I(s, 'imt_fasciaculo_grafismo-1900x'), alt='Ilustrações técnicas dos documentos normativos do IMT'),
            dict(img=I(s, 'imt_fasciaculo_grafismo_02'), alt='Pictograma animado dos documentos do IMT'),
            vid(s, 'livro_07_hortela-magenta-instituto-da-mobilidade-e-transportes.mp4', 'Páginas interiores dos documentos do IMT'),
            vid(s, 'livro_07_hortela-magenta-instituto-da-mobilidade-e-transportes-web', 'Abertura de um documento normativo do IMT'),
        ]),
        testimonial=dict(headline='Muito satisfeitos com a qualidade do produto final.', quote='A Hortelã Magenta trabalhou com o IMT e com o LNEC na reconceção gráfica do «Documento Normativo para Arruamentos Urbanos» e podemos dizer que ficámos muito satisfeitos com a qualidade do produto final e com o profissionalismo da equipa ao longo do trabalho.',
                         name='Rui Velasco', company='IMT', role='Diretor de Serviços de Estudos, Avaliação e Prospetiva',
                         img=I(s, 'imt_fasciaculo_foto_01'), img_alt='Documento normativo do IMT'),
        contact='Conte-nos que documento ou publicação precisa de preparar, para quem e em que formato. Revemos o estado dos conteúdos e ajudamos a organizar a informação.',
    )

    # --------------------------------------------------------------- Almada
    s = 'camara-municipal-de-almada-roteiro'
    P[s] = dict(
        name='Câmara Municipal de Almada', cats='Editorial, Fotografia', h1size='clamp(36px,6.4vw,124px)',
        title='Câmara Municipal de Almada | Projetos | Hortelã Magenta',
        desc='Roteiro turístico para a Câmara Municipal de Almada: uma brochura-roteiro e um desdobrável de bolso para redescobrir uma cidade cultural banhada pelo Tejo.',
        lead='Quantas vezes passamos pelos mesmos lugares sem realmente os conhecer?',
        facts=[('Cliente', 'Câmara Municipal de Almada'), ('Serviços', 'Editorial, Fotografia'), ('Peças', 'Brochura-roteiro e desdobrável de bolso')],
        ink='O desenvolvimento de um roteiro turístico para a Cidade de Almada levou-nos a redescobrir os seus pontos de interesse, uma cidade cultural vibrante banhada pelo Tejo.',
        keys=['redescobrir os seus pontos de interesse', 'banhada pelo Tejo'],
        more='Nasceu assim uma brochura-roteiro e um desdobrável de bolso, pensados para guiar tanto os visitantes mais curiosos como os locais que ainda têm recantos por explorar. Almada, onde cada esquina conta uma história.',
        cover=(I(s, 'roteiro_foto_01'), 'Almada vista do Tejo'),
        services=['grafico', 'foto', 'publica'],
        apps=dict(eyebrow='Brochura e desdobrável', title='Almada, onde cada esquina conta uma história', link=('/design-administracao-publica/', 'Design para a administração pública →'), items=[
            dict(img=I(s, 'roteiro_livro_01'), title='Brochura-roteiro'),
            dict(img=I(s, 'roteiro_livro_02'), title='Páginas interiores'),
            dict(img=I(s, 'roteiro_livro_03'), title='Pontos de interesse'),
            dict(img=I(s, 'roteiro_livro_04'), title='Índice'),
            dict(img=I(s, 'roteiro_mapa_01'), title='Mapa'),
            dict(img=I(s, 'roteiro_mapa_02'), title='Desdobrável de bolso'),
        ]),
        gallery=dict(title='Fotografia', intro='Uma cidade cultural vibrante banhada pelo Tejo.', items=[
            dict(img=I(s, 'roteiro_foto_02'), alt='Ponte 25 de Abril vista de Almada'),
            dict(img=I(s, 'roteiro_foto_03'), alt='Monumento em Almada'),
            dict(img=I(s, 'roteiro_foto_04'), alt='Páginas do roteiro com fotografias de Almada'),
            dict(img=I(s, 'roteiro_foto_05'), alt='Visitante com o desdobrável de bolso de Almada'),
            dict(img=I(s, 'roteiro_foto_01'), alt='Cais de Almada e o Tejo'),
        ]),
        contact='Conte-nos que publicação ou material informativo precisa de preparar e para quem. Revemos os conteúdos disponíveis e ajudamos a organizar a informação.',
    )

    # --------------------------------------------------------------- Imperalum
    s = 'imperalum'
    P[s] = dict(
        name='Imperalum', cats='Branding, Editorial, Design Gráfico',
        title='Imperalum | Projetos | Hortelã Magenta',
        desc='Novo posicionamento gráfico para a Imperalum, líder nacional em produtos betuminosos para impermeabilização: rebranding, comunicação de produto e editorial.',
        lead='A Imperalum é líder no mercado nacional de produtos betuminosos para impermeabilização e destaca-se como um dos principais fabricantes da Península Ibérica.',
        facts=[('Cliente', 'Imperalum'), ('Serviços', 'Branding, Editorial, Design Gráfico'), ('História', 'Mais de 50 anos')],
        ink='Para esta empresa com mais de 50 anos de história, desenvolvemos um novo posicionamento gráfico, respeitando a sua identidade enquanto modernizámos a sua comunicação.',
        keys=['novo posicionamento gráfico', 'respeitando a sua identidade'],
        more='O rebranding impulsionou uma revisão estratégica da comunicação dos produtos, alinhando-os com a atualidade.',
        cover=(I(s, 'imperalum_foto_02'), 'Edifício com cobertura verde'),
        services=['branding', 'grafico', 'industria'],
        ident=dict(title='Identidade visual', intro='Respeitar a identidade e modernizar a comunicação.', tabs=[
            dict(img=I(s, 'imperalum_logo_05'), title='Logótipo', sub='Rebranding', desc='A nova marca, com a assinatura «Soluções com futuro».'),
            dict(img=I(s, 'imperalum_logo_02'), title='Construção', sub='Símbolo'),
            dict(img=I(s, 'imperalum_cor_01'), title='Cores', sub='Paleta'),
            dict(img=I(s, 'imperalum_font_01'), title='Tipografia', sub='Família tipográfica'),
        ]),
        apps=dict(eyebrow='Comunicação', title='A comunicação dos produtos, alinhada com a atualidade', link=('/design-comunicacao-industria/', 'Design para a indústria →'), items=[
            dict(img=I(s, 'imperalum_estacionario_01'), title='Estacionário'),
            dict(img=I(s, 'imperalum_estacionario_02'), title='Pastas e documentos'),
            dict(img=I(s, 'imperalum_hhh_01'), title='Folheto'),
            dict(img=V(s, 'imperalum_livro_01')[1], title='Catálogo'),
            dict(img=I(s, 'imperalum_banner_01'), title='Outdoor'),
            dict(img=I(s, 'imperalum_banner_02'), title='Montras'),
            dict(img=V(s, 'imperalum_lata_03')[1], title='Embalagem'),
            dict(img=I(s, 'imperalum_logo_07'), title='Fachada'),
        ]),
        gallery=dict(title='Produto e aplicações', intro='O rebranding aplicado aos produtos e aos espaços.', items=[
            dict(img=I(s, 'imperalum_lata_01'), alt='Embalagem New Imper da Imperalum'),
            dict(img=I(s, 'imperalum_lata_02'), alt='Embalagem da Imperalum sobre fundo azul'),
            vid(s, 'imperalum_lata_03', 'Embalagem New Imper NGP Tech'),
            dict(img=I(s, 'imperalum_id_06'), alt='Crachá da Imperalum'),
            dict(img=I(s, 'imperalum_bag_01'), alt='Saco da Imperalum'),
            dict(img=I(s, 'imperalum_estacionario_03'), alt='Bloco de notas da Imperalum'),
            vid(s, 'imperalum_livro_01', 'Catálogo da Imperalum'),
            dict(img=I(s, 'imperalum_foto_01'), alt='Coberturas verdes em edifícios'),
        ]),
        contact='Conte-nos o que faz a sua empresa e o que precisa de comunicar: marca, comunicação de produto, catálogos ou embalagens. Com essa base ajudamos a definir o trabalho.',
    )
    return P
