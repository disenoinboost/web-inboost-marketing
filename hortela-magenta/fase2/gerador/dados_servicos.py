"""Páginas de serviço.
Fontes: hortelamagenta.pt/servicos (famílias e 16 serviços, textos atuais), documentos S03, S04, S06 e S07 (texto base em
espanhol, adaptado a português de Portugal como já se fez em Branding e Design Web a partir de S01/S02) e os Word de Gonçalo
«Avença Mensal 360°» e «Coaching de Marcas» (texto final para revisão, usado tal qual)."""

GONCALO = 'https://hortelamagenta.pt/media/pages/sobre/7f11034ae8-1701343726/hm-equipa-goncalo-700x.jpg'


def servicos(M):
    I = lambda s, k: M.find(s, k)
    V = lambda s, k: M.find(s, k, 'video')
    S = {}

    # ===================================================================== Gráfico + Editorial
    S['servico-grafico-editorial'] = dict(
        path='/servicos/design-grafico-e-editorial', name='Gráfico + Editorial', current='Gráfico + Editorial', form_servico='Gráfico + Editorial',
        title='Design gráfico e editorial para empresas | Hortelã Magenta',
        desc='Packaging, folhetos, catálogos, publicações e ambientes a partir da identidade da sua empresa. Conheça projetos de design gráfico e editorial da Hortelã Magenta.',
        og=I('documentos-normativos-imt', 'imt_fasciaculo_livro_01'),
        hero=dict(crumbs=[('Início', '/'), ('Serviços', '/servicos'), ('Gráfico + Editorial', None)],
                  h1='Design gráfico e editorial para empresas', display=['Materiais que', 'explicam a', 'sua empresa em'],
                  rot=['cada folheto.', 'cada catálogo.', 'cada embalagem.', 'cada página.'],
                  intro='A comunicação eficaz é a combinação perfeita entre o design apelativo e o conteúdo cativante. Seja qual for o suporte – da embalagem ao folheto – na Hortelã Magenta trabalhamos para posicionar a sua marca ou produto de forma fresca e atraente no mercado e na mente dos seus consumidores.',
                  cta=('/contacto', 'Falar sobre um projeto de design →'), cta2=('#trabalhos', 'Ver trabalhos')),
        blocks=[
            ('texto', dict(eyebrow='Materiais para a sua empresa', title='Cada material organiza a informação à sua maneira.', paras=[
                'Os materiais de uma empresa devem ajudar a perceber a sua atividade e manter uma identidade reconhecível. Aplicamos o design gráfico aos suportes que a sua equipa utiliza para apresentar a empresa, comunicar os seus serviços e mostrar os seus produtos.',
                'Uma apresentação comercial, um cartaz e uma peça de comunicação precisam de organizar a informação de forma diferente. Revemos a quem se dirige cada material, onde vai ser visto e que conteúdo deve destacar. A identidade da empresa serve de base para manter a coerência entre as peças.'],
                cta=('/servicos/branding', 'Criar ou rever a identidade: Branding →'))),
            ('panels', dict(eyebrow='O que fazemos', title='Da embalagem ao catálogo.', text='Podemos partir de uma identidade existente para preparar um suporte ou trabalhar um conjunto de aplicações. Quando o projeto exige criar ou renovar a identidade, definimo-lo dentro do serviço de branding.',
                cta=('/contacto', 'Pedir orçamento →'), items=[
                dict(short='Packaging', title='Packaging Design', text='Damos mais forma à sua marca. O design de embalagem, ou packaging design, é fundamental no sucesso dos seus produtos. Deve ser pensado para cativar o consumidor, destacar-se dos concorrentes, facilitar o armazenamento ou assegurar a conservação de produtos.', img=I('farinhas-firmos', 'farinhafirmos_farinha_sacos_02-1900x'), cap='Imagem · Farinhas Firmos', pos='50% 50%'),
                dict(short='Folhetos', title='Folhetos e Brochuras', text='Levamos mais longe marcas e produtos. Seja para divulgar a sua empresa junto de potenciais clientes, para dar a conhecer a sua marca ou promover os seus produtos, pensamos cada peça de comunicação ao nível do texto e da imagem para alcançar os seus objetivos.', img=I('consulai', 'consulai_folhete'), cap='Imagem · Consulai', pos='50% 50%'),
                dict(short='Catálogos', title='Catálogos e Publicações', text='Apresentamos a sua marca e produtos. Um catálogo é uma ferramenta de trabalho da empresa, que estudamos para que possa evoluir e atualizar-se ao longo do tempo, para informar clientes, estimulando e acompanhando as suas vendas.', img=I('documentos-normativos-imt', 'imt_fasciaculo_livro_01'), cap='Imagem · Documentos Normativos IMT', pos='50% 50%'),
                dict(short='Ambientes', title='Decoração de Ambientes', text='Criamos ambientes para a sua loja ou stand. O ambiente do seu espaço comercial é fundamental para projetar a sua empresa e cativar mais clientes. Deve ser pensado e desenhado para ser funcional em termos de utilização e eficaz a cumprir cada um dos seus objetivos de comunicação.', img=I('alsil', 'alsilgroup_portfolio_marca_stand'), cap='Imagem · Alsil Group', pos='50% 50%'),
            ])),
            ('lista', dict(eyebrow='Design editorial', title='Dar estrutura à informação.', text='Organizamos textos, imagens e outros conteúdos ao longo de uma publicação, para facilitar a leitura e manter uma relação clara entre as suas partes.', items=[
                ('Títulos, secções e percursos', 'Uma publicação precisa de títulos, secções e percursos que permitam encontrar a informação. A extensão, o tipo de leitura e o conteúdo condicionam o design. Revemos como se relacionam texto, imagens, tabelas e ilustrações antes de definir a composição das páginas.'),
                ('Catálogos e publicações', 'Um catálogo organiza referências e ajuda a compará-las. Outras publicações precisam de desenvolver um tema, apresentar uma instituição ou reunir informação técnica. O trabalho editorial adapta a estrutura e a apresentação ao uso de cada documento.'),
                ('Folhetos e brochuras', 'Um folheto concentra a informação num formato mais curto. Convém decidir o que o leitor deve perceber e que ordem facilita essa leitura. Trabalhamos a hierarquia de textos e imagens tendo em conta o formato e a forma como a peça vai ser distribuída.'),
                ('Preparar conteúdos e revisões', 'Antes de paginar, revemos o estado dos textos e das imagens e acordamos quem valida o conteúdo. Durante o projeto organizam-se as revisões para controlar as alterações e manter a coerência entre páginas. Se houver vários idiomas ou versões, convém prevê-los desde o início.'),
                ('Entrega para os usos acordados', 'A publicação pode precisar de ficheiros para impressão, para consulta digital ou para ambos. A proposta define que versões se preparam e que requisitos técnicos devem ter. Quando participa uma gráfica ou outro fornecedor, é necessário ter as suas especificações antes de fechar os ficheiros.'),
            ], cta=('/design-administracao-publica/', 'Design para a administração pública →'))),
        ],
        trabalhos=dict(title='Trabalhos de design gráfico e editorial.', text='Publicações, packaging e materiais de comunicação para empresas e instituições. Em cada caso, o design organiza a informação e mantém a identidade reconhecível.',
                       statement='Cada peça organiza a informação para quem a vai ler.', bg=I('livro-vilamoura', 'livro-vilamoura-img_10'), items=[
            dict(name='Documentos Normativos IMT', href='/projetos/documentos-normativos-imt', img=I('documentos-normativos-imt', 'imt_fasciaculo_livro_02'), alt='Documentos normativos do IMT', tags=['Editorial', 'Ilustração'], desc='Quatro documentos normativos para arruamentos urbanos, cada um com a sua cor, com ilustrações técnicas e tabelas.'),
            dict(name='Livro Vilamoura', href='/projetos/livro-vilamoura', img=I('livro-vilamoura', 'livro-vilamoura-cover'), alt='Livro Vilamoura', tags=['Editorial', 'Produção gráfica'], desc='Cadernos que casam com o desenrolar da ação, diferentes em papel, textura e dimensão.'),
            dict(name='Câmara Municipal de Almada', href='/projetos/camara-municipal-de-almada-roteiro', img=I('camara-municipal-de-almada-roteiro', 'roteiro_livro_02'), alt='Roteiro turístico de Almada', tags=['Editorial', 'Fotografia'], desc='Uma brochura-roteiro e um desdobrável de bolso para redescobrir a cidade.'),
            dict(name='Imperalum', href='/projetos/imperalum', img=V('imperalum', 'imperalum_livro_01')[1], alt='Catálogo da Imperalum', tags=['Editorial', 'Packaging'], desc='A comunicação dos produtos revista com o rebranding, do catálogo às embalagens.'),
            dict(name='Farinhas Firmos', href='/projetos/farinhas-firmos', img=I('farinhas-firmos', 'farinhafirmos_farinha_sacos_02-1900x'), alt='Embalagens da Farinhas Firmos', tags=['Packaging', 'Design Gráfico'], desc='A nova marca aplicada à gama de farinhas, ao estacionário e ao merchandising.'),
        ]),
        testimonial=dict(headline='Muito satisfeitos com a qualidade do produto final.', quote='A Hortelã Magenta trabalhou com o IMT e com o LNEC na reconceção gráfica do «Documento Normativo para Arruamentos Urbanos» e podemos dizer que ficámos muito satisfeitos com a qualidade do produto final e com o profissionalismo da equipa ao longo do trabalho.',
                         name='Rui Velasco', company='IMT', role='Diretor de Serviços de Estudos, Avaliação e Prospetiva', href='/projetos/documentos-normativos-imt',
                         img=I('documentos-normativos-imt', 'imt_fasciaculo_foto_01'), img_alt='Documento normativo do IMT paginado pela Hortelã Magenta', caption='IMT · Documentos normativos'),
        faq=dict(title='Perguntas sobre design gráfico e editorial', text='O que convém saber antes de preparar um material ou uma publicação.', items=[
            ('Podem trabalhar com a nossa marca atual?', 'Sim. O ponto de partida é dispor dos ficheiros e das normas da marca, juntamente com os materiais que a empresa já utiliza.'),
            ('O que devemos preparar?', 'Os conteúdos, os formatos ou usos previstos e qualquer requisito do fornecedor que vai produzir as peças.'),
            ('A impressão está incluída?', 'O orçamento deve distinguir o design e a preparação de ficheiros da produção ou de outros serviços que se acordem.'),
            ('Os textos têm de estar terminados?', 'Convém conhecer o seu estado antes de orçamentar e definir que conteúdo estará aprovado ao iniciar a paginação. As revisões previstas acordam-se no projeto.'),
            ('Quem fornece as imagens e as traduções?', 'A proposta identifica os materiais disponíveis e quem se ocupa dos que faltam. As autorizações de uso devem ficar resolvidas antes de publicar.'),
            ('É possível preparar uma versão digital?', 'Define-se de acordo com o uso e as funções necessárias. Nem todas as versões digitais precisam do mesmo formato.'),
        ]),
        contact=('Diga-nos, onde quer chegar?', 'Indique-nos o que precisa de comunicar, que suporte vai utilizar e que conteúdos tem disponíveis. Com essa base podemos organizar o trabalho.', 'Falar sobre um projeto de design'),
    )

    # ===================================================================== Campanhas & Redes Sociais
    S['servico-campanhas'] = dict(
        path='/servicos/campanhas-e-redes-sociais', name='Campanhas & Redes Sociais', current='Campanhas & Redes Sociais', form_servico='Campanhas & Redes Sociais',
        title='Campanhas digitais e redes sociais | Hortelã Magenta',
        desc='Campanhas digitais e redes sociais integradas na comunicação da sua marca: conteúdos, criatividade e acompanhamento. Conheça projetos da Hortelã Magenta.',
        og=I('farinhas-firmos', 'farinhafirmos_redessociais_02'),
        hero=dict(crumbs=[('Início', '/'), ('Serviços', '/servicos'), ('Campanhas & Redes Sociais', None)],
                  h1='Campanhas digitais e redes sociais', display=['Levamos a sua', 'marca e produtos'], rot=['a mais clientes.', 'a mais pessoas.', 'a todo o mundo.'],
                  intro='A comunicação digital não é uma opção com futuro. É uma necessidade de todas as marcas, hoje mesmo. A digitalização dá-lhe um alcance global 24h por dia, e a automatização dá mais disponibilidade à sua equipa. Na Hortelã Magenta aliamos o design à tecnologia web e mobile, para responder a estes desafios.',
                  cta=('/contacto', 'Falar sobre a comunicação da marca →'), cta2=('#trabalhos', 'Ver trabalhos')),
        blocks=[
            ('panels', dict(eyebrow='O que fazemos', title='Campanhas e comunidade, com a mesma voz.', text='As campanhas e as redes sociais fazem parte da comunicação global da marca: trabalhamo-las com a mesma identidade, o mesmo tom de voz e o mesmo cuidado com a imagem.',
                cta=('/servicos/avenca-comunicacao-360', 'Avença de comunicação 360° →'), items=[
                dict(short='Campanhas', title='Campanhas Digitais', text='Levamos a sua marca e produtos a mais clientes. Num mundo cada vez mais on-line, as campanhas digitais são uma garantia de chegar a mais clientes em todo o mundo, com a vantagem de serem dirigidas a públicos e territórios específicos e permitirem medir e analisar resultados.', img=I('croma', 'croma_banner_02'), cap='Imagem · Croma', pos='50% 50%'),
                dict(short='Redes sociais', title='Redes Sociais', text='Criamos uma comunidade de fãs à volta da sua marca. A sua presença nas redes sociais permite-lhe criar uma relação mais próxima com a comunidade de clientes e utilizadores, em todo o mundo, 24h por dia. Uma forma ímpar para chegar a mais pessoas, divulgar novidades e interagir.', img=I('farinhas-firmos', 'farinhafirmos_redessociais_02'), cap='Imagem · Farinhas Firmos', pos='50% 50%'),
                dict(short='Comunicação global', title='Integradas na estratégia da marca', text='Na avença mensal, a gestão de redes sociais integra-se na estratégia global da marca, com conteúdos, textos, fotografia e vídeo planeados em conjunto, reuniões regulares e ajustes contínuos.', img=I('consulai', 'consulai_redes_sociais_02'), cap='Imagem · Consulai', pos='50% 50%'),
            ])),
            ('frase', dict(eyebrow='Comunicação continuada', title='Uma presença consistente nas redes, que aumenta a notoriedade e a confiança na sua marca.', text='As campanhas e as redes sociais funcionam melhor quando fazem parte de uma comunicação planeada: o mesmo tom de voz, a mesma imagem e os mesmos objetivos em todos os canais.', cta=('/servicos/avenca-comunicacao-360', 'Conhecer a avença mensal 360° →'))),
        ],
        trabalhos=dict(title='Trabalhos de campanhas e redes sociais.', text='Conteúdos para redes sociais, campanhas e materiais promocionais, sempre ligados à identidade de cada marca.',
                       statement='Cada publicação fala com a mesma voz da marca.', bg=I('consulai', 'consulai_banner_02'), items=[
            dict(name='Farinhas Firmos', href='/projetos/farinhas-firmos', img=I('farinhas-firmos', 'farinhafirmos_redessociais_02'), alt='Publicações da Farinhas Firmos nas redes sociais', tags=['Redes sociais', 'Projeto 360º'], desc='Presença digital nas redes sociais e website, no projeto dos 30 anos.'),
            dict(name='Croma', href='/projetos/croma', img=I('croma', 'croma_rs_01'), alt='Publicações do CROMA nas redes sociais', tags=['Campanha', 'Redes sociais'], desc='Cartazes, anúncios e conteúdos para atrair público para o ciclo de música.'),
            dict(name='Consulai', href='/projetos/consulai', img=I('consulai', 'consulai_redes_sociais_02'), alt='Publicações da CONSULAI', tags=['Redes sociais', 'Anúncios'], desc='Uma abordagem renovada para as redes sociais e anúncios publicitários.'),
            dict(name='Queijaria da São', href='/projetos/queijaria-da-sao', img=V('queijaria-da-sao', 'queijariadasao_post')[1], alt='Publicações da Queijaria da São', tags=['Redes sociais', 'Website'], desc='Comunicação nas redes sociais e website de uma queijaria com 50 anos.'),
            dict(name='Alinea', href='/projetos/alinea', img=V('alinea', 'alinea_redes_sociais')[1], alt='Publicações da Alinea', tags=['Redes sociais', 'Digital'], desc='Conteúdos digitais com a mesma simplicidade do rebranding.'),
        ]),
        testimonial=dict(headline='Respeito, Confiança e Profissionalismo.', quote='Encontrámos a Hortelã Magenta, por um acaso, no meio de diversas outras empresas de comunicação, em 2014. Mas desde logo percebemos que queríamos trabalhar com eles. Temos desenvolvido uma relação que assenta em 3 pilares fundamentais: Respeito, Confiança e Profissionalismo.',
                         name='Marta Mendes', company='CONSULAI', role='Consultora Sénior, Inovação e Investigação · Coordenadora de Comunicação Institucional', href='/projetos/consulai',
                         img=I('consulai', 'consulai_bag'), img_alt='Saco com a identidade da CONSULAI', caption='Consulai · Comunicação'),
        contact=('Diga-nos, onde quer chegar?', 'Conte-nos o que faz a sua empresa, a quem quer chegar e que canais utiliza. Ajudamos a definir a comunicação de que a marca precisa.', 'Falar sobre a comunicação da marca'),
    )

    # ===================================================================== Fotografia & Vídeo
    S['servico-fotografia-video'] = dict(
        path='/servicos/fotografia-e-video', name='Fotografia & Vídeo', current='Fotografia & Vídeo', form_servico='Fotografia & Vídeo',
        title='Fotografia e vídeo para empresas | Hortelã Magenta',
        desc='Fotografia institucional e de produto, packshot, vídeo e motion graphics para apresentar a sua empresa, os seus produtos e a sua atividade.',
        og=I('queijaria-da-sao', 'queijariadasao_foto_06'),
        hero=dict(crumbs=[('Início', '/'), ('Serviços', '/servicos'), ('Fotografia & Vídeo', None)],
                  h1='Fotografia e vídeo para empresas', display=['Imagens que', 'contam a', 'sua história'], rot=['em cada produto.', 'em cada espaço.', 'em cada ecrã.'],
                  intro='Mais do que mil palavras, uma boa fotografia ou vídeo envolve o espectador na sua história. É uma ferramenta poderosa para criar experiências de marca envolventes, interativas e memoráveis. E até, através da criação 3D e Motion Graphics, para apresentar a realidade que ainda não existe.',
                  cta=('/contacto', 'Falar sobre fotografia ou vídeo →'), cta2=('#trabalhos', 'Ver trabalhos')),
        blocks=[
            ('panels', dict(eyebrow='O que fazemos', title='Da sessão fotográfica ao filme.', text='Planeamos a fotografia e o vídeo dentro da comunicação da marca, a partir de uma mensagem e dos suportes em que vão ser utilizados.',
                cta=('/contacto', 'Pedir orçamento →'), items=[
                dict(short='Institucional', title='Institucional e Ambiente', text='Fazemos sessões de fotografia e vídeo institucionais da sua empresa. Estes registos são ferramentas poderosas para dar a conhecer a empresa, equipa e produtos. Sejam vinhas a perder de vista, um restaurante apetecível, uma fábrica dinâmica ou um ambiente de equipa descontraída, revelamos a sua melhor faceta.', img=I('farinhas-firmos', 'farinhafirmos_fabrica_11'), cap='Imagem · Farinhas Firmos', pos='50% 40%'),
                dict(short='Produto', title='Produto', text='Porque os olhos também comem, uma boa fotografia é essencial para demarcar o seu produto no mercado. Revelamos a sua faceta mais favorável e atraente, capaz de cativar a atenção e preferência de mais clientes ao longo de anos.', img=I('queijaria-da-sao', 'queijariadasao_foto_06'), cap='Imagem · Queijaria da São', pos='50% 50%'),
                dict(short='Packshot', title='Packshot', text='Fotografamos e filmamos produtos para apresentações em vídeo ou suportes estáticos. Este serviço assegura que os seus produtos têm uma presença profissional e apetecível em todos os meios de comunicação.', img=I('imperalum', 'imperalum_lata_01'), cap='Imagem · Imperalum', pos='50% 50%'),
                dict(short='Motion', title='Motion Graphics', text='Damos vida e animação ao que só viu em sonhos. Seja para dar a conhecer um espaço que ainda não existe, para contar uma história ou ainda para dar instruções sobre a utilização de produtos e serviços, as técnicas de Motion Graphics permitem partilhar a sua visão de uma forma mais dinâmica.', img=V('croma', 'croma-2023')[1], cap='Imagem · Croma', pos='50% 50%'),
            ])),
            ('filme', dict(src=V('farinhas-firmos', '30_anosfirmos')[0], poster=V('farinhas-firmos', '30_anosfirmos')[1], title='Vídeo corporativo', text='O vídeo dos 30 anos da Farinhas Firmos, parte de um projeto que incluiu marca, website e fotografia.', word='Vídeo', label='Farinhas Firmos', aria='Vídeo corporativo dos 30 anos da Farinhas Firmos')),
            ('lista', dict(eyebrow='Como trabalhamos', title='Da mensagem à peça final.', text='Antes de fotografar ou filmar, acordamos o que deve mostrar cada imagem e onde vai ser utilizada.', items=[
                ('Imagens para os suportes que utiliza', 'Uma ficha de produto, um catálogo e uma peça de comunicação têm necessidades diferentes. Antes de preparar a sessão, convém identificar os suportes, os enquadramentos e os formatos.'),
                ('Packshot e fotografia em contexto', 'Uma imagem sobre fundo neutro ajuda a reconhecer o produto e a comparar referências de um catálogo. Uma fotografia em contexto mostra como se utiliza ou como se relaciona com outros elementos. Acordamos o tipo de imagem de acordo com o suporte.'),
                ('Vídeo institucional', 'As instalações, os processos e as pessoas trazem informação que nem sempre é fácil transmitir numa descrição. Um vídeo institucional reúne esses elementos numa peça que apresenta a atividade da empresa.'),
                ('Preparação e produção', 'Antes de produzir, é preciso acordar o que o espectador deve perceber e que materiais ou cenas são necessários. A partir daí definem-se a preparação, a produção e a edição, as revisões e os formatos de entrega.'),
                ('Um âmbito adaptado ao uso', 'O número de produtos ou de referências, a duração, os locais, as pessoas que participam e as versões necessárias influenciam o trabalho. A proposta define que fotografias e vídeos se fazem e em que formatos se entregam.'),
            ])),
        ],
        trabalhos=dict(title='Trabalhos de fotografia e vídeo.', text='Sessões fotográficas, fotografia de produto e vídeos institucionais, sempre dentro do trabalho de marca de cada empresa.',
                       statement='Cada imagem mostra a empresa real.', bg=I('farinhas-firmos', 'firmos_20210825'), items=[
            dict(name='Farinhas Firmos', href='/projetos/farinhas-firmos', img=I('farinhas-firmos', 'farinhafirmos_fabrica-1900x'), alt='Fábrica da Farinhas Firmos', tags=['Fotografia', 'Vídeo'], desc='Sessões fotográficas e um vídeo corporativo para os 30 anos da empresa.'),
            dict(name='Queijaria da São', href='/projetos/queijaria-da-sao', img=I('queijaria-da-sao', 'queijariadasao_foto_02'), alt='Queijos da Queijaria da São', tags=['Fotografia', 'Vídeo'], desc='Fotografia de produto e um vídeo institucional sobre o saber-fazer da marca.'),
            dict(name='Alsilgroup', href='/projetos/alsil', img=I('alsil', 'alsilgroup_fabrica_08'), alt='Equipa do Alsil Group na fábrica', tags=['Fotografia', 'Vídeo'], desc='A fábrica e as pessoas do grupo, fotografadas para a nova comunicação.'),
            dict(name='Alinea', href='/projetos/alinea', img=I('alinea', 'alinea_foto_01'), alt='Clínica Alinea', tags=['Fotografia', 'Vídeo'], desc='Imagem própria dos espaços e da equipa da Alinea.'),
            dict(name='Croma', href='/projetos/croma', img=V('croma', 'croma-2023')[1], alt='Vídeo do CROMA', tags=['Vídeo', 'Motion'], desc='Vídeos institucionais para televisão.'),
        ]),
        testimonial=dict(headline='Sempre disponíveis e com soluções completas.', quote='Sempre disponíveis e com soluções completas, diferenciam-se pela sua imagem única, e o entusiasmo e atenção ao detalhe no trabalho que apresentam fazem com que a sua marca seja sentida em qualquer projeto que lhes seja contratado. Recomendam-se vivamente!',
                         name='Luís Firmo', company='Farinhas Firmos', role='RH e I&D, Gestor Projeto', href='/projetos/farinhas-firmos',
                         img=I('farinhas-firmos', 'farinhafirmos_fabrica_09'), img_alt='Silos da Farinhas Firmos fotografados pela Hortelã Magenta', caption='Farinhas Firmos · Fotografia'),
        faq=dict(title='Perguntas sobre fotografia e vídeo', text='O que convém saber antes de pedir uma sessão ou um vídeo.', items=[
            ('Que informação precisamos para pedir uma proposta?', 'Uma lista de produtos, o seu tamanho aproximado, o número de imagens esperado e os suportes em que vão ser utilizadas. No caso do vídeo, o objetivo, a quem se dirige e onde vai ser utilizado.'),
            ('As mesmas fotografias servem para o site e para o catálogo?', 'Algumas imagens podem ter vários usos, mas convém prevê-los desde o início. O enquadramento e os ficheiros de entrega devem adaptar-se às necessidades de cada suporte.'),
            ('Quanto deve durar um vídeo?', 'A duração depende da mensagem e do contexto de utilização. Acorda-se ao preparar a peça; não tem de ser a mesma para uma apresentação e para outras versões.'),
            ('Podemos utilizar materiais existentes?', 'É preciso rever primeiro a sua qualidade, formato e autorizações. A proposta indicará o que pode ser aproveitado e que material novo o projeto precisa.'),
            ('O que determina o orçamento?', 'O número e as características dos produtos, as imagens necessárias, a preparação, a produção, a edição e as versões acordadas. O âmbito e as condições definem-se antes de começar.'),
        ]),
        contact=('Diga-nos, onde quer chegar?', 'Partilhe o tipo de produto ou o objetivo do vídeo, os suportes previstos e a data em que precisa das imagens. Com essa informação começamos a definir o trabalho.', 'Falar sobre fotografia ou vídeo'),
    )

    # ===================================================================== Avença 360 (Word de Gonçalo)
    S['servico-avenca'] = dict(
        path='/servicos/avenca-comunicacao-360', name='Avenças mensais', current='Avenças mensais', form_servico='Avenças mensais',
        title='Avença de Comunicação 360° | Hortelã Magenta',
        desc='O departamento de comunicação da sua empresa. Conhecemos o seu negócio por dentro para lhe dar uma voz própria, coerente e real. Desde 2007.',
        og='https://hortelamagenta.pt/media/pages/projetos/camolas/34c1b44fdb-1735900095/hortelamagenta_portfolio_marca_camolas_estacionario-1900x.jpg',
        hero=dict(crumbs=[('Início', '/'), ('Serviços', '/servicos'), ('Avença Mensal 360°', None)], display_is_h1=True,
                  eyebrow='Avença Mensal 360°', display=['O departamento de', 'comunicação da sua', 'empresa. Só que do', 'lado de fora.'], display_wide=['O departamento de comunicação', 'da sua empresa.', 'Só que do lado de fora.'],
                  intro='Há empresas que precisam de uma agência. E há empresas que precisam de alguém que conheça o seu negócio tão bem como elas. Na avença mensal 360° somos as duas coisas: a agência e o departamento de comunicação da sua empresa.',
                  cta=('/contacto', 'Marcar conversa →'), cta2=('#inclui', 'O que inclui')),
        blocks=[
            ('texto', dict(eyebrow='Mês após mês', title='Um parceiro que conhece a sua marca.', paras=[
                'Não nos limitamos a executar pedidos. Entramos no dia a dia da empresa, percebemos o que a move e assumimos a responsabilidade de a comunicar com consistência, mês após mês. Tem um parceiro, que conhece a sua marca, o seu mercado e os seus objetivos.'])),
            ('texto', dict(eyebrow='Primeiro ouvimos', title='Primeiro ouvimos. Depois damos voz à sua empresa.', bg='#f6f7f8', paras=[
                'Para comunicar bem uma empresa é preciso conhecê-la por dentro. Queremos saber o que vende e também porque existe: qual é o seu _core business_, o que a distingue, como pensam as pessoas que a gerem e o que os clientes valorizam nela.',
                'Este conhecimento não se força com questionários nem com reuniões de _briefing_. Vai-se construindo com proximidade: no contacto regular, em conversas francas e, muitas vezes, à volta de uma mesa, num almoço com o cliente. É aí que surgem as histórias, as conquistas e os desafios, e que se percebe para onde o negócio está a evoluir.',
                'Depois fazemos o nosso trabalho: **transformamos essas conversas em estratégia.** O que foi partilhado de forma informal ganha forma, direção e uma voz própria. Uma voz positiva, imediata, direta e real, que soa à sua empresa e a mais nenhuma.'])),
            ('lista', dict(id='inclui', eyebrow='Avença mensal', title='O que inclui a avença mensal', text='Marca, imagem gráfica, textos, web, fotografia, vídeo e redes sociais, com reuniões regulares e um valor mensal fixo.', numbered=True, items=[
                ('Reforço de marca', 'Uma presença consistente que aumenta a notoriedade e a confiança na sua marca.'),
                ('Coerência de marca', 'Tudo o que a empresa comunica, em qualquer canal e formato, fala a mesma língua.'),
                ('Tom de voz', 'Definimos e mantemos a forma como a sua marca fala, escreve e se apresenta.'),
                ('Criação de imagem gráfica', 'Identidade, design gráfico e editorial, materiais institucionais e comerciais.'),
                ('Criação de conteúdos e textos', 'Mensagens claras, com propósito e alinhadas com o negócio.'),
                ('Criação digital e web', 'Websites, conteúdos digitais e campanhas online.'),
                ('Fotografia e vídeo', 'Imagem própria, que mostra a empresa real.'),
                ('Gestão de redes sociais', 'Integrada na estratégia global da marca.'),
                ('Acompanhamento próximo', 'Reuniões regulares, planeamento e ajustes contínuos.'),
            ], cta=('/contacto', 'Marcar conversa →'))),
            ('panels', dict(eyebrow='Departamento externo', title='Porquê ter um departamento de comunicação externo?', items=[
                dict(short='Equipa completa', title='Uma equipa completa', text='Estratégia, design, textos e digital, sem ter de construir e gerir uma equipa interna.', img='https://hortelamagenta.pt/media/pages/projetos/camolas/34c1b44fdb-1735900095/hortelamagenta_portfolio_marca_camolas_estacionario-1900x.jpg', cap='Imagem · Adega Camolas', pos='50% 50%'),
                dict(short='Continuidade', title='Continuidade e conhecimento profundo', text='Conhecemos a história da marca, incluindo a que não está escrita em lado nenhum. Muitas vezes é nas conversas informais com os donos e administradores que descobrimos o que a empresa tem de mais verdadeiro. São histórias, valores e decisões que nunca chegaram a ser comunicados.', img=I('consulai', 'consulai_wall_logo'), cap='Imagem · Consulai', pos='50% 50%'),
                dict(short='Visão de fora', title='Visão de fora, com conhecimento de dentro', text='É esse conhecimento informal que nos permite, muitas vezes, reposicionar a marca e levá-la a lugares em que a própria administração ainda não tinha pensado. Vemos a empresa como os clientes a veem, mas sabemos o que está por trás.', img=I('alsil', 'alsilgroup_portfolio_marca_display'), cap='Imagem · Alsil Group', pos='50% 50%'),
                dict(short='Previsibilidade', title='Previsibilidade', text='Um valor mensal fixo e uma comunicação sempre ativa, sem começar do zero em cada projeto.', img=I('farinhas-firmos', 'farinhafirmos_calendario'), cap='Imagem · Farinhas Firmos', pos='50% 50%'),
            ])),
            ('frase', dict(eyebrow='Desde 2007', title='Quase 20 anos a fazer crescer marcas.', text='Desde 2007 que acompanhamos empresas de vários setores. Algumas estão connosco há mais de 15 anos: marcas com responsabilidades nacionais e internacionais que confiam em nós como o seu departamento de comunicação. Uma relação destas não se constrói com campanhas pontuais. Constrói-se com tempo, confiança e com quem conhece a empresa por dentro.', cta=('/contacto', 'Quero um departamento de comunicação →'))),
        ],
        faq=dict(title='Perguntas frequentes', text='Sobre a avença de comunicação mensal 360°.', items=[
            ('O que é uma avença de comunicação?', 'É um acordo mensal em que a Hortelã Magenta funciona como o departamento de comunicação da sua empresa. Em vez de contratar projetos isolados, conta com uma equipa que acompanha a marca de forma contínua: estratégia, imagem gráfica, textos, digital, web, fotografia e vídeo. Tudo é planeado em conjunto e ajustado à realidade do seu negócio, mês após mês.'),
            ('Qual a diferença entre uma avença e projetos pontuais?', 'Num projeto pontual resolvemos uma necessidade específica, como uma identidade, um website ou uma campanha. Na avença acompanhamos a empresa ao longo do tempo. Isso permite-nos conhecer o negócio por dentro, manter a coerência da marca em tudo o que é comunicado e antecipar oportunidades, em vez de apenas responder a pedidos. O resultado é uma comunicação mais consistente, mais eficaz e com custos previsíveis.'),
            ('Trabalham com empresas fora da Moita e de Setúbal?', 'Sim. Estamos sediados na Moita e acompanhamos empresas de todo o país, algumas com atividade internacional. Valorizamos o contacto presencial sempre que possível, porque é nas conversas que melhor conhecemos as marcas. Combinamos esse contacto com reuniões online e um acompanhamento regular, onde quer que a sua empresa esteja.'),
            ('Que tipo de empresas acompanham?', 'Trabalhamos com empresas de vários setores e dimensões, desde PME a marcas com responsabilidades nacionais e internacionais. Algumas estão connosco há mais de 15 anos. O que têm em comum é a vontade de comunicar com coerência e de ter, ao seu lado, um parceiro que conhece o negócio e ajuda a marca a crescer.'),
        ]),
        contact=('Quero um departamento de comunicação.', 'Conte-nos o que faz a sua empresa e o que precisa de comunicar. Marcamos uma conversa para conhecer o seu negócio por dentro.', 'Marcar conversa'),
    )

    # ===================================================================== Coaching de Marcas (Word de Gonçalo)
    S['servico-coaching'] = dict(
        path='/servicos/coaching-de-marcas', name='Coaching de Marcas', current='Coaching de Marcas', form_servico='Coaching de Marcas',
        title='Coaching de Marcas e Mentoria de Branding | Hortelã Magenta',
        desc='Sessões de coaching de marca para clarificar posicionamento, identidade e comunicação. Ouvimos a sua marca para a ajudar a encontrar a sua voz.',
        og=GONCALO,
        hero=dict(crumbs=[('Início', '/'), ('Serviços', '/servicos'), ('Coaching de Marcas', None)], display_is_h1=True,
                  eyebrow='Coaching de Marcas', display=['Coaching de Marcas:', 'às vezes, a sua', 'marca só precisa', 'de ser ouvida.'], display_wide=['Coaching de Marcas:', 'às vezes, a sua marca', 'só precisa de ser ouvida.'],
                  intro='Este serviço não fomos nós que o inventámos. Foram os nossos clientes que lhe deram nome.',
                  cta=('/contacto', 'Marcar uma sessão →'), cta2=('#como-funciona', 'Como funciona')),
        blocks=[
            ('texto', dict(eyebrow='Uma consulta', title='Percebemos que já fazíamos isto há anos. Só faltava dizê-lo.', paras=[
                'Ao longo de quase 20 anos, fomos percebendo que muitas reuniões com clientes não eram sobre logótipos, cores ou campanhas. Eram sobre dúvidas. _Quem somos? Para quem falamos? Porque é que o mercado não nos vê como nós nos vemos?_ Os clientes começaram a dizer que nós fazíamos "coaching" às marcas deles. Um dia, um cliente ligou-nos e pediu, literalmente, **"uma consulta"** sobre branding e posicionamento.',
                'Percebemos então que já fazíamos isto há anos. Só faltava dizê-lo.'])),
            ('citacao', dict(eyebrow='Um psicólogo para a sua marca', headline='Um psicólogo para a sua marca.', quote='Costumo dizer, meio a brincar, que sou quase um psicólogo de marcas. Antes de comunicar uma marca, é preciso deixá-la falar.',
                             name='Gonçalo Santos', company='Hortelã Magenta', role='Fundador da Hortelã Magenta', href='/sobre#equipa', link_label='Conhecer a equipa →',
                             img=GONCALO, img_alt='Gonçalo Santos, fundador da Hortelã Magenta', caption='Gonçalo Santos · Fundador', pos='50% 20%')),
            ('texto', dict(eyebrow='Do mesmo lado da mesa', title='Não trazemos fórmulas feitas. Trazemos clareza.', bg='#f6f7f8', paras=[
                'As marcas, tal como as pessoas, têm uma história, inseguranças, ambições e contradições. Às vezes cresceram depressa demais. Às vezes mudaram de rumo e a imagem ficou para trás. Às vezes sabem muito bem o que fazem, mas não sabem explicar porque é que isso importa.',
                'No Coaching de Marcas sentamo-nos do mesmo lado da mesa. Fazemos perguntas, ouvimos com atenção e ajudamos a marca a encontrar as suas próprias respostas. Não trazemos fórmulas feitas. Trazemos clareza.'])),
            ('lista', dict(id='para-quem', eyebrow='Para quem é', title='Para quem é', numbered=False, items=[
                ('Empresas que sentem que a marca já não as representa', 'Mas não sabem porquê.'),
                ('Fundadores e gestores', 'Que precisam de clarificar o posicionamento antes de investir em comunicação.'),
                ('Marcas em mudança', 'Um novo produto, um novo mercado, uma nova geração na gestão.'),
                ('Negócios que comunicam muito mas não são percebidos', 'Ou que não sabem por onde começar.'),
            ])),
            ('lista', dict(id='como-funciona', eyebrow='Como funciona', title='Como funciona', bg='#f6f7f8', numbered=True, items=[
                ('Escuta', 'Uma conversa profunda sobre o negócio, as pessoas, a história e as ambições.'),
                ('Diagnóstico', 'Analisamos como a marca se vê, como é vista e onde está a diferença.'),
                ('Clarificação', 'Trabalhamos juntos o posicionamento, a proposta de valor, a personalidade e o tom de voz.'),
                ('Direção', 'Recebe um plano claro e prático para comunicar com confiança, connosco ou com a sua equipa.'),
            ], foot='Pode ser uma sessão pontual ou um acompanhamento regular de mentoria de marca.', cta=('/contacto', 'Marcar uma sessão de Coaching de Marca →'))),
            ('frase', dict(eyebrow='Clareza', title='Não é consultoria. É uma conversa que muda a forma como comunica.', text='A consultoria tradicional entrega relatórios. Nós entregamos clareza. Quando uma marca se conhece, tudo o resto fica mais fácil: o design, os textos, as campanhas e até as decisões de negócio.', cta=('/contacto', 'Marcar uma sessão de Coaching de Marca →'))),
        ],
        faq=dict(title='Perguntas frequentes', text='Sobre as sessões de Coaching de Marcas.', items=[
            ('O que é coaching de marcas?', 'É um processo de reflexão guiada sobre a sua marca. Através de conversas estruturadas, ajudamos empresários e gestores a perceber quem a marca é, como é vista e como deve comunicar. O foco está em ouvir: perceber a história, o negócio e as ambições da empresa para chegar a um posicionamento claro e a uma voz própria. É um serviço que nasceu dos nossos clientes, que começaram a dar este nome à forma como trabalhamos com eles.'),
            ('Qual a diferença entre coaching de marca e consultoria de branding?', 'A consultoria de branding parte, muitas vezes, de modelos e análises externas e termina num relatório. No coaching de marca as respostas são construídas em conjunto consigo. Fazemos as perguntas certas, ouvimos e ajudamos a organizar o que a empresa já sabe sobre si mesma, mas ainda não conseguiu traduzir em comunicação. O resultado é mais prático, mais próximo da realidade do negócio e mais fácil de pôr em prática.'),
            ('Preciso de fazer rebranding depois das sessões?', 'Não necessariamente. Muitas vezes a marca não precisa de mudar de imagem. Precisa de clareza sobre o que diz e como o diz. Em alguns casos, as sessões revelam que pequenos ajustes no posicionamento, nas mensagens ou no tom de voz são suficientes. Noutros, mostram que faz sentido evoluir a identidade. Se for esse o caminho, podemos acompanhá-lo, mas a decisão é sempre sua.'),
            ('Quanto tempo dura uma sessão?', 'A primeira sessão pode demorar até 3h. É o tempo necessário para ouvirmos com calma a história da empresa, o negócio, as ambições e as dúvidas sobre a marca. No final, avaliamos em conjunto consigo se são necessárias mais sessões. Essa decisão depende da complexidade do negócio e do que a marca precisa para ganhar clareza.'),
        ]),
        contact=('Marcar uma sessão de Coaching de Marca.', 'Conte-nos em que momento está a sua marca e que dúvidas tem. Marcamos uma primeira sessão para a ouvir com calma.', 'Marcar uma sessão'),
    )
    return S
