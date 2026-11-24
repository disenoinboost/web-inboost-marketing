"""Landings de especialidade (URL com barra final, como na web atual). Texto: as landings atuais de hortelamagenta.pt
(conteúdo íntegro, só com correções evidentes). Melhorias das fichas L01–L05: entrada a partir de Serviços e da Home,
casos reais ligados (Camolas, Alsil, Farinhas Firmos, Imperalum, Queijaria da São, IMT, Almada, Hospital Garcia de Orta,
Croma) e regresso aos serviços relacionados."""
from dados_projetos import NAMES, CARD

LANDS = [('/design-rotulos-vinho/', 'Design de Rótulos para Vinhos'), ('/design-comunicacao-industria/', 'Design de Comunicação para a Indústria'),
         ('/branding-clinicas-dentarias/', 'Branding para Clínicas Dentárias'), ('/design-administracao-publica/', 'Design para Administração Pública'),
         ('/design-de-eventos/', 'Design de Comunicação para Eventos')]


def landings(M, LI):
    """LI(slug, nome_do_ficheiro) devolve a URL local da imagem da landing (registada em M)."""
    I = lambda s, k: M.find(s, k)
    CAM = lambda k: next(u for u in M.info if u.startswith('/wp-content/uploads/hm-media/') and '/camolas/' in u and k in u)
    tile = lambda s: (NAMES[s], '/projetos/' + s, CARD[s])
    # fotografia de projetos reais para as faixas «imagens» (cada uma liga ao projeto)
    foto = lambda url, alt, cap, slug: dict(img=url, alt=alt, cap=cap, href='/projetos/' + slug)
    others = lambda path: dict(eyebrow='Conheça também', title='Outras especialidades', items=[(h, l) for h, l in LANDS if h != path] + [('/servicos', 'Todos os serviços')])
    L = {}

    # ===================================================================== Rótulos de vinho
    s = 'design-rotulos-vinho'
    L['lp-rotulos-vinho'] = dict(
        path='/design-rotulos-vinho/', name='Rótulos para Vinhos', current='Branding',
        title='Design de Rótulos para Vinhos | Hortelã Magenta',
        desc='Design de rótulos e packaging para vinhos em Portugal: identidade vínica, rótulos, caixas e acabamentos. Projetos premiados como os da Adega Camolas.',
        og=LI(s, 'hortelamagenta_portfolio_marca_camolas_grande-escolha_01-1900x2850-q90.webp'),
        hero=dict(crumbs=[('Início', '/'), ('Serviços', '/servicos'), ('Rótulos para vinhos', None)],
                  h1='Design de Rótulos para Vinhos em Portugal', display=['Rótulos que', 'diferenciam, valorizam e', 'posicionam marcas.'],
                  intro='No setor dos vinhos, a qualidade já não é o único fator de decisão. A história, a textura, a tipografia e o encanto visual comunicam-se antes de a rolha ser aberta. O seu rótulo é a prova narrativa.',
                  cta=('/contacto', 'Fale connosco →'), cta2=('#portfolio', 'Ver portfólio')),
        blocks=[
            ('lista', dict(eyebrow='Porquê', title='Porque o design de rótulos é decisivo', text='Rigor editorial e sofisticação no mercado vitivinícola.', items=[
                ('Impacto na decisão de compra', 'Em milésimos de segundo, a atenção do consumidor é disputada. A estética define a escolha na prateleira.'),
                ('Diferenciação e destaque', 'Escape dos clichés clássicos. Apele a novos mercados com visuais arrojados, intemporais e distintos.'),
                ('Posicionamento de preço', 'Uma garrafa revestida por um design premium eleva o seu valor percebido.'),
                ('Coerência de marca', 'Cada garrafa é um embaixador do seu legado e deve espelhar com exatidão a qualidade que encerra.'),
            ])),
            ('panels', dict(eyebrow='O que fazemos', title='Da fundação da marca vínica aos acabamentos.', text='Da fundação da marca vínica até aos acabamentos de impressão nas suas garrafas.', cta=('/servicos/design-grafico-e-editorial', 'Packaging e design gráfico →'), items=[
                dict(short='Rótulos', title='Design de Rótulos', text='Desenho minimalista e sofisticado para edições normais ou reservas exclusivas.', img=LI(s, 'hortelamagenta_portfolio_marca_camolas_grande-escolha_01-1900x2850-q90.webp'), cap='Imagem · Adega Camolas', pos='50% 50%'),
                dict(short='Identidade', title='Identidade Vínica', text='Criação do universo da marca, paletas cromáticas e logótipos para adegas e produtores.', img='https://hortelamagenta.pt/media/pages/projetos/camolas/5d5f15c3a2-1735900038/hortelamagenta_portfolio_marca_camolas_logo_02-1900x.jpg', cap='Imagem · Adega Camolas', pos='50% 50%'),
                dict(short='Packaging', title='Packaging Global', text='Expansão visual para caixas de cartão, tubos premium, cápsulas e sleeves decorativas.', img=LI(s, 'hortelamagenta_portfolio_marca_camolas_garrafeira_03-1023x1023-q90.webp'), cap='Imagem · Adega Camolas', pos='50% 50%'),
                dict(short='Mercados', title='Mercados Internacionais', text='Adaptação cultural, naming e storytelling visual otimizados para atrair importadores.', img=LI(s, 'hortelamagenta_portfolio_marca_camolas_moscatel-5-anos_05-1900x2853-q90.webp'), cap='Imagem · Adega Camolas', pos='50% 50%'),
            ])),
            ('marquee', dict(id='portfolio', title='O nosso portfólio', intro='Excelência materializada nas prateleiras e garrafeiras.', items=[
                dict(img=LI(s, 'filipe_palhoca_merlot.webp'), alt='Design minimalista e editorial de rótulo de vinho'),
                dict(img=LI(s, 'hortelamagenta_portfolio_marca_camolas_grande-escolha_01-1900x2850-q90.webp'), alt='Design de rótulo Camolas Grande Escolha'),
                dict(img=LI(s, 'Hortelamagenta_hortela-magenta-filipe-palhoca-vinhos-srah-touriganacional-labelwine-rotulos-portuguese-wine-vinho-portuges-peninsula-setubal_01.jpg'), alt='Design de rótulo Filipe Palhoça Vinhos'),
                dict(img=LI(s, 'siria-2020-6-baixa-1023x1532-q90.webp'), alt='Design de rótulo de vinho Síria 2020'),
                dict(img=LI(s, 'hortelamagenta_portfolio_marca_camolas_garrafeira_03-1023x1023-q90.webp'), alt='Packaging e rótulo Camolas Garrafeira'),
                dict(img=LI(s, '16.webp'), alt='Design de rótulo Vinho do Porto General Silveira – Quinta do Valdalagea'),
                dict(img=LI(s, 'hortelamagenta_portfolio_marca_camolas_moscatel-5-anos_04-1900x4560-q90.webp'), alt='Detalhe de design de rótulo Camolas Moscatel'),
                dict(img=LI(s, 'hortelamagenta_portfolio_marca_camolas_moscatel-5-anos_05-1900x2853-q90.webp'), alt='Detalhe de packaging de vinho Camolas Moscatel'),
            ], link=('/projetos/camolas', 'Ver o projeto da Adega Camolas →'))),
            ('premios', dict(eyebrow='Reconhecimento', title='Prémios e Reconhecimento', bg='#f6f7f8', items=[
                dict(img=LI(s, 'hortelamagenta_portfolio_marca_camolas_award-IWSC-wines.webp'), alt='Prémio de Design de Vinho – IWSC 2024', title='Prémio de Design', sub='International Wine & Spirit Competition 2024'),
                dict(img=LI(s, 'Mutante-Awards-2025.webp'), alt='Prémio de Design At Wine – Mutante Awards 2025', title='2 Prémios de Design', sub='Mutante Awards – Design at Wine 2025'),
            ], quote='«Gostamos de vinho e gostamos de design. Dificilmente separamos os dois, mas isso são problemas nossos ;)»')),
            ('frase', dict(eyebrow='Resultados', title='Design é posicionamento. Perceção cria valor e impulsiona as vendas nas prateleiras.', text='Resultados que um bom rótulo traz.')),
            ('imagens', dict(items=[
                foto(CAM('camolas_garrafeira_01'), 'Garrafeira da Adega Camolas', 'Adega Camolas · Garrafeira', 'camolas'),
                foto(CAM('camolas_espumante'), 'Espumante da Adega Camolas', 'Adega Camolas · Espumante', 'camolas'),
                foto(CAM('camolas_monocasta_syrah_03'), 'Monocasta Syrah da Adega Camolas', 'Adega Camolas · Monocasta Syrah', 'camolas'),
            ])),
            ('chips', dict(eyebrow='Para quem', title='Para quem desenhamos?', items=['Adegas históricas e modernas', 'Produtores de vinho independentes', 'Marcas premium e edições limitadas', 'Projetos virados para a exportação'])),
            ('lista', dict(eyebrow='Processo', title='O nosso processo', bg='#f6f7f8', items=[
                ('Análise de mercado', 'Analisamos o posicionamento, a concorrência direta e os objetivos comerciais.'),
                ('Conceito criativo', 'Desenvolvemos narrativas únicas ancoradas na história do produtor.'),
                ('Desenvolvimento', 'Materializamos conceitos em propostas visuais premium, selecionando papéis e tipografias.'),
                ('Produção', 'Acompanhamos testes nas gráficas, relevos, vernizes e a aplicação final nas garrafas.'),
            ])),
            ('texto', dict(eyebrow='Hortelã Magenta', title='Porque escolher a Hortelã Magenta', paras=[
                'Abordagem estratégica aliada à sensibilidade estética. Substituímos imagens saturadas de vinhas e barris por design tipográfico, materiais orgânicos de alta qualidade e uma experiência global orientada para marcas premium, com experiência em projetos editoriais.',
                'Projetos de identidade visual premiados internacionalmente no setor dos vinhos.'], cta=('/servicos/branding', 'Branding e identidade →'))),
            ('mais', dict(items=[tile('camolas'), tile('queijaria-da-sao'), tile('farinhas-firmos')])),
            ('links', others('/design-rotulos-vinho/')),
        ],
        contact=('Vamos criar um rótulo que se destaque?', 'Conte-nos que vinho ou gama quer apresentar, em que mercados e que materiais já tem. Com essa base ajudamos a definir o trabalho.', 'Entrar em contacto'),
    )

    # ===================================================================== Indústria
    s = 'design-comunicacao-industria'
    L['lp-industria'] = dict(
        path='/design-comunicacao-industria/', name='Comunicação para a Indústria', current='Branding',
        title='Design de Comunicação para a Indústria | Hortelã Magenta',
        desc='Identidade corporativa, catálogos técnicos, fotografia, vídeo e websites B2B para empresas industriais. Casos como Alsil Group, Farinhas Firmos e Imperalum.',
        og=LI(s, 'alsilgroup_portfolio_marca_display-1900x3040-q90.webp'),
        hero=dict(crumbs=[('Início', '/'), ('Serviços', '/servicos'), ('Indústria', None)],
                  h1='Design de Comunicação para a Indústria', display=['Complexidade técnica', 'em comunicação clara', 'e diferenciadora.'],
                  intro='Num setor onde a prova do valor técnico é tantas vezes dificultada pela complexidade da oferta, o design de comunicação para a indústria garante a clareza. Diferenciar as suas máquinas ou serviços em mercados ultracompetitivos impacta diretamente a perceção de sofisticação pelo seu cliente.',
                  cta=('/contacto', 'Fale connosco →'), cta2=('#portfolio', 'Ver casos práticos')),
        blocks=[
            ('lista', dict(eyebrow='Porquê', title='Porque o design é crítico na indústria', text='Rigor técnico traduzido em comunicação visual clara.', items=[
                ('Comunicação técnica clara', 'Tornamos inteligíveis e visualmente sofisticados os seus catálogos técnicos e apresentações industriais.'),
                ('Diferenciação competitiva', 'Posicionamento diferenciador num mercado onde as propostas concorrentes carecem de identidade e distinção visual.'),
                ('Suporte às equipas comerciais', 'Ferramentas visuais premium (apresentações, brochuras) que apoiam os seus comerciais em qualquer negociação internacional.'),
                ('Valorização da marca', 'Um design gráfico superior alinha a perceção externa à excelência interna do seu produto.'),
            ])),
            ('panels', dict(eyebrow='A nossa intervenção', title='Da base da marca aos mercados internacionais.', text='Da base da vossa marca ao suporte total para mercados internacionais.', cta=('/servicos/branding', 'Branding e identidade →'), items=[
                dict(short='Identidade', title='Identidade corporativa', text='Redesign e otimização de logótipos e universo visual de empresas do setor.', img=I('alsil', 'alsilgroup_cartao-de-visita'), cap='Imagem · Alsil Group', pos='50% 50%'),
                dict(short='Institucional', title='Comunicação institucional', text='Vídeos institucionais, tom de voz e fotografias profissionais.', img=I('farinhas-firmos', 'farinhafirmos_fabrica_11'), cap='Imagem · Farinhas Firmos', pos='50% 40%'),
                dict(short='Editorial', title='Design editorial', text='Estudo modular para catálogos, manuais, packaging e dossiers técnicos.', img=LI(s, '03-hortela-magenta-imporquimica-catalogo-editorial.webp'), cap='Imagem · Imporquímica', pos='50% 50%'),
                dict(short='Digital', title='Digital & Vendas', text='Websites B2B com navegação orientada ao produto e apoio contínuo em documentação comercial.', img=LI(s, '05-hortela-magenta-scada-produtos.webp'), cap='Imagem · Scada', pos='50% 50%'),
            ])),
            ('marquee', dict(id='portfolio', title='Casos práticos', intro='Implementações focadas no rigor do setor B2B.', items=[
                dict(img=LI(s, 'alsilgroup_portfolio_marca_display-1900x3040-q90.webp'), alt='Design industrial da marca Alsil em grande formato'),
                dict(img=LI(s, 'hortelamagenta_portfolio_marca_alsilgroup_fabrica_02-1023x1116-q90.webp'), alt='Fotografia industrial e instalações corporativas Alsil'),
                dict(img=LI(s, 'hortelamagenta_hortela-magenta-eurobatata-cebola-batata-portuguese-portuges-packaging-embalagem_icon_branding_05.webp'), alt='Design de embalagens Eurobatata'),
                dict(img=LI(s, 'RWA_natal_02.webp'), alt='Comunicação corporativa e visual para a indústria'),
                dict(img=LI(s, '03-hortela-magenta-imporquimica-catalogo-editorial.webp'), alt='Catálogo industrial editorial Imporquímica'),
                dict(img=LI(s, '05-hortela-magenta-scada-produtos.webp'), alt='Comunicação digital e interfaces SCADA para a indústria'),
                dict(img=LI(s, '16-scaled.webp'), alt='Design de comunicação industrial Farinhas Firmos e Alsil'),
            ])),
            ('frase', dict(eyebrow='Clareza', title='Complexidade não é confusão. Design é clareza estratégica.', text='Comunicar melhor é vender melhor. Somos um motor silencioso nas grandes transações B2B, apoiando a comunicação industrial das empresas.')),
            ('chips', dict(eyebrow='Para quem', title='Para quem desenhamos?', items=['Indústria metalomecânica', 'Robótica e automação', 'Indústria alimentar', 'Empresas B2B técnicas e engenharia'])),
            ('lista', dict(eyebrow='Processo', title='O nosso processo', bg='#f6f7f8', items=[
                ('Diagnóstico e análise técnica', 'Mergulhamos nas especificações do seu produto e entendemos a audiência e o canal.'),
                ('Estratégia de comunicação', 'Definimos o posicionamento industrial e um plano de ação estruturado.'),
                ('Desenvolvimento criativo', 'Materializamos conceitos em propostas visuais rigorosas sem sacrificar a estética.'),
                ('Implementação', 'Lançamento em feiras internacionais, roll-out digital e acompanhamento.'),
            ])),
            ('texto', dict(eyebrow='Hortelã Magenta', title='Porque escolher a Hortelã Magenta', paras=[
                'Temos uma experiência comprovada em comunicação industrial. A nossa capacidade de simplificar o complexo e a proximidade com equipas técnicas permitem uma abordagem de gestão de design à medida do seu setor.'], cta=('/servicos/design-web', 'Websites para empresas →'))),
            ('mais', dict(items=[tile('alsil'), tile('farinhas-firmos'), tile('imperalum'), tile('queijaria-da-sao')])),
            ('links', others('/design-comunicacao-industria/')),
        ],
        contact=('Vamos comunicar melhor a sua indústria?', 'Soluções de design e comunicação técnica premium e direcionadas. Conte-nos o que produz, para quem e em que mercados.', 'Entrar em contacto'),
    )

    # ===================================================================== Clínicas dentárias
    s = 'branding-clinicas-dentarias'
    L['lp-clinicas-dentarias'] = dict(
        path='/branding-clinicas-dentarias/', name='Branding para Clínicas Dentárias', current='Branding',
        title='Branding para Clínicas Dentárias | Hortelã Magenta',
        desc='Branding para clínicas dentárias em Portugal: identidade visual, aplicação no espaço, comunicação digital e posicionamento para clínicas que valorizam a qualidade.',
        og=LI(s, 'dental_clinic_premium.webp'),
        hero=dict(crumbs=[('Início', '/'), ('Serviços', '/servicos'), ('Clínicas dentárias', None)],
                  h1='Branding para Clínicas Dentárias em Portugal', display=['A identidade', 'do seu espaço,', 'à altura da clínica.'],
                  intro='No setor da saúde dentária, a competência clínica já não é o único fator de decisão. A confiança, a perceção de higiene, a tecnologia e o conforto são comunicados antes de o paciente se sentar na cadeira. A sua marca é o primeiro diagnóstico.',
                  cta=('/contacto', 'Fale connosco →'), cta2=('#intervencao', 'A nossa intervenção')),
        blocks=[
            ('texto', dict(eyebrow='Excelência clínica', title='Elevamos a identidade do seu espaço.', paras=[
                'Elevamos a identidade do seu espaço para refletir a excelência clínica, atraindo pacientes que valorizam a qualidade. Design que transmite tranquilidade e rigor.'])),
            ('lista', dict(eyebrow='Porquê', title='Porque é que o branding é crítico?', bg='#f6f7f8', items=[
                ('Diferenciação num mercado saturado', 'Deixe de competir pelo preço e passe a competir pelo valor percebido e exclusividade da sua clínica.'),
                ('Confiança imediata', 'Uma identidade visual coerente reduz a ansiedade do paciente, transmitindo profissionalismo desde o primeiro contacto.'),
                ('Atração de talento', 'Clínicas com uma marca forte e posicionamento claro atraem e retêm os melhores médicos e profissionais de saúde do mercado.'),
            ])),
            ('lista', dict(id='intervencao', eyebrow='A nossa intervenção', title='Da fundação estratégica ao espaço clínico.', text='Uma abordagem holística, desde a fundação estratégica até à presença física no seu espaço clínico.', numbered=False, items=[
                ('Identidade visual', 'Logótipo, paleta cromática e tipografia desenvolvidas para transmitir calma, precisão e autoridade médica.'),
                ('Aplicação no espaço', 'Sinalética, fardamento, decoração de vidros e estacionário. Garantimos que a marca vive coerentemente no espaço físico.'),
                ('Comunicação digital', 'Websites institucionais orientados à conversão e templates de redes sociais para uma comunicação consistente.'),
                ('Posicionamento', 'Definição do tom de voz, manifesto da marca, fotografia e vídeo, e estratégia para clínicas que pretendem liderar no seu segmento.'),
            ], cta=('/servicos/branding', 'Branding e identidade →'))),
            ('frase', dict(eyebrow='Qualidade', title='A estética não é um luxo. É um compasso de qualidade.', text='Os pacientes assumem subconscientemente que o nível de design da sua marca dita o nível de higiene e tecnologia dos seus tratamentos.')),
            ('imagens', dict(id='imagens', eyebrow='Imagens', title='Design que transmite tranquilidade', items=[
                dict(img=LI(s, 'dental_clinic_premium.webp'), alt='Branding e design para clínica dentária premium', cap='Identidade e espaço clínico'),
                dict(img=LI(s, 'dental_clinic_details.webp'), alt='Identidade visual e logótipo para clínica dentária', cap='Detalhes da identidade'),
            ])),
            ('chips', dict(eyebrow='Para quem', title='Para quem desenhamos?', items=['Clínicas de Reabilitação Oral e Implantologia', 'Clínicas de Estética Dentária Avançada', 'Consultórios Boutique e Exclusivos', 'Grupos de Saúde a preparar expansão'])),
            ('lista', dict(eyebrow='Método', title='Método', bg='#f6f7f8', items=[
                ('Imersão', 'Compreendemos a visão do Diretor Clínico e o paciente-alvo.'),
                ('Estratégia', 'Definimos o posicionamento, a diferenciação e a narrativa.'),
                ('Design', 'Criamos a identidade visual e exploramos o universo da marca.'),
                ('Implementação', 'Desdobramos a marca para suportes físicos e digitais.'),
            ])),
            ('texto', dict(eyebrow='Hortelã Magenta', title='A escolha natural', paras=[
                'Na Hortelã Magenta, não seguimos modelos pré-fabricados. Não utilizamos dentes ou sorrisos genéricos nos seus logótipos. Criamos marcas intemporais e sofisticadas, alinhadas com a arquitetura contemporânea e a excelência que pretende entregar aos seus pacientes.',
                'Projetos de branding para saúde exigem sensibilidade e rigor.'])),
            ('links', others('/branding-clinicas-dentarias/')),
        ],
        contact=('Vamos construir a sua marca?', 'Projetos de branding para saúde exigem sensibilidade e rigor. Conte-nos em que momento está a sua clínica e o que quer comunicar.', 'Entrar em contacto'),
    )

    # ===================================================================== Administração pública
    s = 'design-administracao-publica'
    L['lp-administracao-publica'] = dict(
        path='/design-administracao-publica/', name='Design para Administração Pública', current='Gráfico + Editorial',
        title='Design para Administração Pública | Hortelã Magenta',
        desc='Design de comunicação para entidades públicas: relatórios, publicações institucionais, infografia, fotografia e vídeo. Projetos para IMT, Câmara Municipal de Almada e Hospital Garcia de Orta.',
        og=LI(s, 'hortelamagenta_portfolio_marca_imt_fasciaculo_livro_01-1900x2850-q90.webp'),
        hero=dict(crumbs=[('Início', '/'), ('Serviços', '/servicos'), ('Administração pública', None)],
                  h1='Design de Comunicação para Administração Pública em Portugal', display=['Informação complexa', 'em comunicação clara,', 'acessível e relevante.'],
                  intro='Na administração pública, comunicar não é apenas informar: é garantir clareza, transparência e confiança. Projetos institucionais exigem rigor, estrutura e capacidade de transformar informação complexa em comunicação acessível.',
                  cta=('/contacto', 'Fale connosco →'), cta2=('#portfolio', 'Projetos desenvolvidos')),
        blocks=[
            ('texto', dict(eyebrow='Comunicação institucional', title='Comunicar bem é servir melhor.', paras=[
                'Na Hortelã Magenta, desenvolvemos soluções de comunicação completas para entidades públicas, com foco na eficácia, consistência e impacto.',
                'A comunicação institucional enfrenta desafios específicos: grande volume de informação técnica, necessidade de clareza e acessibilidade, comunicação com públicos diversos e responsabilidade na transmissão de dados.',
                'Um bom design permite simplificar conteúdos complexos, melhorar a compreensão da informação, reforçar a confiança nas instituições e aproximar a comunicação dos cidadãos.'])),
            ('imagens', dict(items=[
                foto(I('documentos-normativos-imt', 'imt_fasciaculo_livro_02'), 'Os quatro documentos normativos do IMT', 'IMT · Documentos normativos', 'documentos-normativos-imt'),
                foto(I('camara-municipal-de-almada-roteiro', 'roteiro_mapa_02'), 'Desdobrável de bolso do roteiro de Almada', 'Câmara Municipal de Almada · Roteiro', 'camara-municipal-de-almada-roteiro'),
                foto(I('hospital-garcia-de-orta', 'hgo_estacionario'), 'Estacionário do Hospital Garcia de Orta', 'Hospital Garcia de Orta · Rebranding', 'hospital-garcia-de-orta'),
            ])),
            ('lista', dict(eyebrow='O que fazemos', title='Projetos integrados, do conceito à implementação.', bg='#f6f7f8', numbered=False, text='Desenvolvemos projetos integrados para entidades públicas.', items=[
                ('Estratégia de comunicação', 'Definição de objetivos, estruturação da mensagem e alinhamento institucional.'),
                ('Conceito criativo', 'Direção visual, narrativa e linguagem, coerência global.'),
                ('Design gráfico e editorial', 'Relatórios e contas, publicações institucionais, livros e materiais informativos.'),
                ('Infografia e visualização de dados', 'Simplificação de informação complexa, leitura clara de indicadores e organização visual de conteúdos.'),
                ('Implementação', 'Preparação para produção, acompanhamento técnico e adaptação a diferentes formatos.'),
                ('Fotografia e vídeo', 'Produção de conteúdos visuais, reforço da narrativa institucional e suporte à comunicação digital.'),
            ], cta=('/servicos/design-grafico-e-editorial', 'Design gráfico e editorial →'))),
            ('marquee', dict(id='portfolio', title='Projetos desenvolvidos', intro='Comunicação territorial e institucional, relatórios técnicos e ambientais, relatórios e contas e publicações editoriais.', items=[
                dict(img=LI(s, 'hortelamagenta_portfolio_marca_imt_fasciaculo_livro_01-1900x2850-q90.webp'), alt='Documentos normativos do IMT'),
                dict(img=LI(s, '03-hortelamagenta_hortela-magenta-design-ambiental-comunicacao-apa-apaambiente-rea-sustentabilidade-portal-estado-ambiente-relatorio-editorial-paginacao-grafico-lisbon-portugal.webp'), alt='Relatório do Estado do Ambiente'),
                dict(img=LI(s, 'CM_Odemira_hortelamagenta_guias_turisticos_design_touristic_guide_portugal_03.webp'), alt='Município de Odemira · Comunicação Institucional'),
                dict(img=LI(s, '07-Vilamoura_livro_outros-olhares-novas-historias-editorial-design-hortelamagenta-inframoura-graphic-design.webp'), alt='Vilamoura · Outros olhares, novas histórias'),
                dict(img=LI(s, 'hortela-magenta-inframoura-relatorio-contas-design-editorial-4.webp'), alt='Inframoura · Relatório e Contas'),
                dict(img=LI(s, 'Hortela-Magenta-Hospital-Garcia-de-Horta_07-1.webp'), alt='Rebranding Hospital Garcia de Orta E.P.E. · Design Editorial e Design Gráfico'),
            ])),
            ('frase', dict(eyebrow='Transparência', title='Informação clara gera confiança. Comunicar melhor é servir melhor. Design é transparência.', text='Uma boa comunicação institucional ajuda a aumentar a transparência, melhorar a compreensão pública, reforçar a credibilidade institucional e valorizar o trabalho desenvolvido. A forma como se comunica influencia diretamente a forma como se é percebido.')),
            ('chips', dict(eyebrow='Para quem', title='Para quem é este serviço', items=['Câmaras municipais', 'Entidades governamentais', 'Organismos públicos', 'Empresas públicas'])),
            ('lista', dict(eyebrow='Processo', title='O nosso processo', bg='#f6f7f8', items=[
                ('Diagnóstico', 'Análise do contexto, objetivos e enquadramento institucional.'),
                ('Estratégia', 'Definição da estrutura de comunicação e abordagem.'),
                ('Desenvolvimento', 'Criação do conceito e execução visual.'),
                ('Implementação', 'Acompanhamento técnico e entrega final.'),
            ])),
            ('imagens', dict(items=[
                foto(I('livro-vilamoura', 'livro-vilamoura-img_02'), 'Leitor a folhear o Livro Vilamoura', 'Livro Vilamoura', 'livro-vilamoura'),
                foto(I('camara-municipal-de-almada-roteiro', 'roteiro_foto_05'), 'Visitante com o desdobrável de Almada', 'Câmara Municipal de Almada · Roteiro', 'camara-municipal-de-almada-roteiro'),
                foto(I('documentos-normativos-imt', 'imt_fasciaculo_livro_04'), 'Documento normativo do IMT aberto', 'IMT · Documentos normativos', 'documentos-normativos-imt'),
            ])),
            ('lista', dict(eyebrow='Hortelã Magenta', title='Porquê escolher a Hortelã Magenta', numbered=False, items=[
                ('Experiência em projetos institucionais e editoriais', ''), ('Capacidade de traduzir informação complexa', ''),
                ('Abordagem estratégica e integrada', ''), ('Atenção ao detalhe e à clareza', ''),
            ], foot='Cada projeto é pensado para garantir clareza, consistência e impacto, respeitando sempre o contexto institucional.')),
            ('mais', dict(items=[tile('documentos-normativos-imt'), tile('camara-municipal-de-almada-roteiro'), tile('hospital-garcia-de-orta'), tile('livro-vilamoura')])),
            ('links', others('/design-administracao-publica/')),
        ],
        contact=('Vamos comunicar melhor o serviço público?', 'Se procura melhorar a forma como comunica com os cidadãos e valorizar os projetos, fale connosco. Desenvolvemos comunicação clara, estruturada e relevante.', 'Entrar em contacto'),
    )

    # ===================================================================== Eventos
    s = 'design-de-eventos'
    L['lp-eventos'] = dict(
        path='/design-de-eventos/', name='Design de Comunicação para Eventos', current='Gráfico + Editorial',
        title='Design de Comunicação para Eventos | Hortelã Magenta',
        desc='Identidade de eventos, convites, sinalética, materiais impressos, ecrãs e redes sociais, pensados para o público e o contexto de cada evento. Projeto CROMA.',
        og=LI(s, 'hortelamagenta_portfolio_marca_croma_foto-1900x4560-q90.webp'),
        hero=dict(crumbs=[('Início', '/'), ('Serviços', '/servicos'), ('Eventos', None)],
                  h1='Design de Comunicação para Eventos', display=['Eventos que', 'começam antes', 'de acontecer.'],
                  intro='Design pensado para o público, para o contexto e para o momento. Não desenhamos apenas para o evento: compreendemos a vivência de quem vai participar e o que espera do momento.',
                  cta=('/contacto', 'Falemos sobre o seu evento →'), cta2=('#desenvolvemos', 'O que desenvolvemos')),
        blocks=[
            ('texto', dict(eyebrow='Intenção', title='Mais do que estética, é intenção.', paras=[
                'Desenhamos a comunicação com um foco analítico: atuar não para o espaço físico, mas para o público que o vai experienciar.',
                'Cada evento tem um público específico e um contexto próprio. Um evento institucional comunica de forma diversa de um corporativo. A nossa disciplina visual responde a cada dinâmica com rigor.',
                'Garantimos que cada peça, física ou digital, contribui ativamente para uma experiência coerente e focada no público que a marca quer atingir.'])),
            ('imagens', dict(items=[
                foto(I('croma', 'croma_banner_04'), 'Identidade do CROMA projetada em palco', 'CROMA · Palco', 'croma'),
                foto(I('alsil', 'alsilgroup_portfolio_marca_stand'), 'Stand do Alsil Group numa exposição internacional', 'Alsil Group · Stand', 'alsil'),
                foto(I('croma', 'croma_banner_03'), 'Mupi do CROMA', 'CROMA · Mupi', 'croma'),
            ])),
            ('lista', dict(eyebrow='O design como sistema', title='Num evento, tudo comunica de forma interligada.', bg='#f6f7f8', numbered=False, text='Desde o primeiro contacto ao fechar das portas.', items=[
                ('Identidade transversal', 'Desenvolvemos o master visual do projeto, aplicando-o de forma natural desde a sinalética aos conteúdos digitais.'),
                ('Organização fluida', 'A identidade visual opera como sistema primário de informação, definindo e gerindo intuitivamente a circulação de pessoas no recinto.'),
                ('Reforço da mensagem', 'Espaços, ecrãs e pontos de contacto materializam o mesmo eixo conceptual, garantindo a integridade e consistência do discurso corporativo.'),
            ])),
            ('panels', dict(id='desenvolvemos', eyebrow='O que desenvolvemos', title='Todas as dimensões da identidade visual de eventos.', text='Cada elemento funciona como um ponto de contacto estrutural com a audiência.', cta=('/projetos/croma', 'Ver o projeto CROMA →'), items=[
                dict(short='Master conceptual', title='Master Conceptual', text='Branding para eventos: criação de identidades únicas temporárias, paleta cromática, manual de normas e tom de voz gráfico.', img=LI(s, 'hortelamagenta_portfolio_marca_croma_foto-1900x4560-q90.webp'), cap='Imagem · Croma', pos='50% 50%'),
                dict(short='Impressos', title='Editorial e Impressos', text='Criação de convites corporativos, bilhética, panfletos, programas gerais, menus, badges e acreditação profissional.', img=I('croma', 'croma_tickets'), cap='Imagem · Croma', pos='50% 50%'),
                dict(short='Sinalética', title='Ambiente e Sinalética', text='Painéis, roll-ups, backdrops institucionais, stands completos e sinalização interior direcional intuitiva de larga escala.', img=LI(s, 'hortelamagenta_ludopolis_espaco_mascotes.webp'), cap='Imagem · Ludopolis', pos='50% 50%'),
                dict(short='Ecrãs e digital', title='Ecrãs e Digital', text='Peças de motion design, vídeos para ledwalls, social media kits antes, durante e depois do evento, e reportagem fotográfica.', img=LI(s, 'hortelamagenta_portfolio_marca_croma_rs_01-1900x3831-q90.webp'), cap='Imagem · Croma', pos='50% 50%'),
            ])),
            ('marquee', dict(id='portfolio', title='Desenhar para o público', intro='Compreender quem vai participar e o que espera da marca, rejeitando tendências efémeras.', items=[
                dict(img=LI(s, 'hortelamagenta_portfolio_marca_croma_rs_01-1900x3831-q90.webp'), alt='Comunicação para eventos – CROMA'),
                dict(img=LI(s, 'hortelamagenta_portfolio_marca_croma_bag-1023x1116-q90.webp'), alt='Tote bag com a identidade do evento'),
                dict(img=LI(s, 'hortelamagenta_ludopolis_espaco_mascotes.webp'), alt='Organização do espaço e sinalética em eventos presenciais – Ludopolis'),
                dict(img=LI(s, 'hortelamagenta_ludopolis_grafico_poster_mupi.webp'), alt='Mupi Ludopolis'),
                dict(img=LI(s, 'hortelamagenta_ludopolis_grafico_pulseiras2.webp'), alt='Acreditação, convites e ferramentas de acesso para eventos'),
                dict(img=LI(s, 'hortelamagenta_portfolio_marca_croma_logo_02.gif'), alt='Identidade visual e animação para palcos e eventos'),
            ])),
            ('frase', dict(eyebrow='Escala', title='O tamanho importa. O objetivo não é decorar. É comunicar com intenção.', text='O design tem um papel fundamental na perceção e credibilidade de um evento: contextualiza e orienta, reforça a mensagem e cria ritmo gráfico, orientando de forma silenciosa toda a audiência.')),
            ('imagens', dict(items=[
                foto(I('croma', 'croma_badge'), 'Credenciais do CROMA', 'CROMA · Credenciais', 'croma'),
                foto(I('alsil', 'alsilgroup_portfolio_marca_display'), 'Ecrã de grande formato do Alsil Group numa exposição', 'Alsil Group · Display', 'alsil'),
                foto(I('croma', 'croma_tickets'), 'Bilhetes do CROMA', 'CROMA · Bilhetes', 'croma'),
            ])),
            ('chips', dict(eyebrow='Contextos', title='Contextos onde atuamos', items=['Eventos institucionais e municipais', 'Eventos corporativos B2B/B2C', 'Apresentações, galas e lançamentos de produtos', 'Iniciativas públicas, encontros setoriais e feiras da indústria'])),
            ('lista', dict(eyebrow='O ciclo contínuo', title='Antes, durante e depois.', bg='#f6f7f8', text='A gestão da presença de marca acompanha o evento integralmente.', items=[
                ('Antes', 'Campanhas de teaser nas redes sociais, design de email marketing e convites formais para suscitar e cimentar a expectativa.'),
                ('Durante', 'Elementos físicos no espaço, ecrãs gigantes, crachás e folhetos de leitura em mão para orientar o público.'),
                ('Depois', 'Vídeos de resumo e reportagem, fotografias e documentação editorial para estender o impacto do evento.'),
            ], foot='A envergadura da ocasião não se afere pela dimensão do palco, mas pela emoção e memória que perduram no final.')),
            ('mais', dict(items=[tile('croma'), tile('alsil'), tile('consulai')])),
            ('links', others('/design-de-eventos/')),
        ],
        contact=('Se está a preparar um novo evento', 'Mapeamos e alinhamos de forma clara os eixos de comunicação com toda a audiência presente na sua iniciativa. Conte-nos o que vai acontecer, para quem e onde.', 'Planear a identidade do evento'),
    )
    return L
