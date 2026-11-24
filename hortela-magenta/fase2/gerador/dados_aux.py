"""Páginas legais e auxiliares.
- Política de Privacidade: texto atual de hortelamagenta.pt/politica-de-privacidade (íntegro).
- Política de Cookies: textos da política atual («Uso de Cookies») e do painel de preferências de cookies da web atual,
  mais a descrição técnica do que o site novo guarda no navegador (verificada no código). A validar juridicamente.
- Mapa do site, Obrigado e 404: páginas novas do site."""
from dados_projetos import ORDER, NAMES, CARD
from dados_landings import LANDS

PRIVACIDADE = dict(
    path='/politica-de-privacidade', title='Política de Privacidade | Hortelã Magenta', h1='Política de Privacidade',
    desc='Como a Hortelã Magenta – Design de Comunicação, Lda. recolhe, utiliza e protege os dados pessoais dos utilizadores do seu site.',
    lead='A Hortelã Magenta respeita a privacidade dos seus utilizadores e compromete-se a proteger os seus dados pessoais, de acordo com a legislação em vigor.',
    sections=[
        ('ambito', 'Âmbito da nossa Política de Privacidade', [
            ('p', 'A Hortelã Magenta – Design de Comunicação, Lda., com sede na R. Dr. Miguel Bombarda nº 88, 2860-461 Moita, Portugal, e contactos pelo telefone 211 806 292 e e-mail <a href="mailto:info@hortelamagenta.com">info@hortelamagenta.com</a>, respeita a privacidade dos seus utilizadores e compromete-se a proteger os seus dados pessoais, de acordo com a legislação em vigor.'),
            ('p', 'Esta Política de Privacidade aplica-se ao site www.hortelamagenta.pt e www.hortelamagenta.com, e descreve a forma como recolhemos, utilizamos e protegemos as informações que nos são fornecidas.')]),
        ('finalidade', 'Finalidade da Recolha de Dados Pessoais', [
            ('p', 'Os dados pessoais recolhidos através dos formulários presentes no nosso website são exclusivamente utilizados para processar os pedidos dos utilizadores. Não serão usados para outros fins sem o seu consentimento expresso.')]),
        ('marketing', 'Uso de Dados Pessoais para Marketing Direto', [
            ('p', 'A Hortelã Magenta não utilizará os seus dados pessoais para enviar comunicações não solicitadas. Não vendemos nem negociamos os dados dos nossos utilizadores com terceiros.')]),
        ('acesso', 'Acesso aos Dados Pessoais', [
            ('p', 'A Hortelã Magenta compromete-se a não divulgar os dados pessoais dos seus utilizadores a terceiros, exceto quando requerido por lei ou com o seu consentimento.')]),
        ('direitos', 'Direitos do Utilizador sobre os Seus Dados Pessoais', [
            ('p', 'Em conformidade com a legislação aplicável, a Hortelã Magenta garante os seguintes direitos aos utilizadores:'),
            ('ul', [
                '<strong>Direito à Informação:</strong> o utilizador tem direito a informações claras e acessíveis sobre como os seus dados pessoais são tratados.',
                '<strong>Direito de Acesso:</strong> o utilizador pode aceder aos dados pessoais que processamos e solicitar uma cópia.',
                '<strong>Direito de Retificação:</strong> o utilizador pode corrigir ou atualizar os seus dados pessoais, caso estejam incorretos ou desatualizados.',
                '<strong>Direito de Apagamento («Direito a Ser Esquecido»):</strong> o utilizador pode solicitar a eliminação dos seus dados pessoais, salvo em casos em que a retenção seja necessária por motivos legais.',
                '<strong>Direito de Oposição:</strong> o utilizador pode optar por não receber comunicações de marketing direto a qualquer momento, através da funcionalidade «remover» nas mensagens enviadas ou por contacto direto.',
                '<strong>Retirada de Consentimento:</strong> o utilizador pode retirar o seu consentimento para o tratamento dos seus dados pessoais a qualquer momento, sem que isso afete a legalidade do tratamento anterior à retirada.',
                '<strong>Direito de Apresentar Queixa:</strong> o utilizador tem o direito de apresentar uma queixa à Comissão Nacional de Proteção de Dados (CNPD), caso considere que o tratamento dos seus dados viola as leis de proteção de dados.',
                '<strong>Direito à Portabilidade:</strong> o utilizador pode solicitar a transferência dos seus dados pessoais para outro responsável pelo tratamento.',
                '<strong>Direito à Limitação do Tratamento:</strong> o utilizador pode solicitar a limitação do tratamento dos seus dados nas seguintes situações: contestação da exatidão dos dados, oposição ao tratamento, entre outras.']),
            ('p', 'Para exercer qualquer um destes direitos, o utilizador pode contactar-nos através dos meios indicados acima.')]),
        ('armazenamento', 'Armazenamento dos Dados', [
            ('p', 'Os dados pessoais dos utilizadores são armazenados nos nossos servidores localizados na União Europeia, protegidos por medidas de segurança adequadas para garantir a conformidade com a legislação de proteção de dados.')]),
        ('cookies', 'Uso de Cookies', [
            ('p', 'O website da Hortelã Magenta utiliza cookies para melhorar a experiência do utilizador. Os cookies são pequenos ficheiros armazenados no seu dispositivo que permitem ao site recordar as suas preferências e atividades. O utilizador pode configurar o seu navegador para recusar cookies, embora isso possa afetar a funcionalidade de algumas áreas do site.'),
            ('p', 'Os cookies utilizados não recolhem dados que identifiquem o utilizador diretamente, mas sim informações anónimas sobre a navegação, como a área geográfica de acesso e as páginas visitadas.'),
            ('p', 'Saiba mais na nossa <a href="/politica-de-cookies">Política de Cookies</a>.')]),
        ('atualizacoes', 'Atualizações da Política de Privacidade', [
            ('p', 'A Hortelã Magenta reserva-se o direito de atualizar ou modificar esta Política de Privacidade a qualquer momento, adaptando-a às alterações legislativas ou às nossas práticas. Recomendamos que consulte periodicamente esta página para estar informado sobre como protegemos os seus dados pessoais.')]),
    ])

COOKIES = dict(
    path='/politica-de-cookies', title='Política de Cookies | Hortelã Magenta', h1='Política de Cookies',
    desc='Que cookies e que armazenamento local utiliza o site da Hortelã Magenta, para que servem e como pode gerir as suas preferências.',
    lead='O que são cookies, que informação o site da Hortelã Magenta guarda no seu navegador e como pode gerir as suas preferências.',
    sections=[
        ('o-que-sao', 'O que são cookies', [
            ('p', 'Os cookies são pequenos ficheiros armazenados no seu dispositivo que permitem ao site recordar as suas preferências e atividades. Para o mesmo fim, os sites podem também utilizar o armazenamento local do navegador (sessionStorage e localStorage).')]),
        ('categorias', 'Categorias de cookies', [
            ('p', 'Utilizamos cookies para personalizar o conteúdo e melhorar a sua experiência digital. Alguns cookies são essenciais para o correto funcionamento do site e para fins de segurança. Estes cookies essenciais não podem ser desativados.'),
            ('ul', [
                '<strong>Necessários:</strong> permitem interações e funcionalidades básicas que lhe permitem aceder a funcionalidades selecionadas do nosso serviço e facilitar a sua comunicação connosco.',
                '<strong>Métricas e Analíticas:</strong> ajudam-nos a medir o tráfego e a analisar o seu comportamento para melhorar o nosso serviço.',
                '<strong>Anúncios e Publicidade:</strong> permitem-nos colocar anúncios direcionados noutros sites que visita e medir o seu envolvimento com esses anúncios.']),
            ('p', 'Os cookies de métricas e de publicidade só são utilizados com o seu consentimento. Pode ativar ou desativar essa permissão a qualquer momento; se desativar determinados cookies, a sua experiência de navegação poderá ser afetada.')]),
        ('neste-site', 'O que este site guarda no seu navegador', [
            ('p', 'Ao entrar no site, um painel pede o seu consentimento. As estatísticas e o marketing só são ativados se os aceitar; se recusar, o site funciona na mesma.'),
            ('p', '<strong>Necessários (sempre ativos).</strong> Não identificam o utilizador:'),
            ('ul', [
                '<strong>cmplz_banner-status, cmplz_consented_services, cmplz_policy_id, cmplz_functional, cmplz_preferences, cmplz_statistics e cmplz_marketing:</strong> guardam a escolha feita no painel de consentimento, durante 365 dias.',
                '<strong>hm-pt</strong> e <strong>hm-ptd</strong> (armazenamento de sessão): indicam que vem de outra página do site e o sentido da transição entre páginas.',
                '<strong>hm-theme</strong> (armazenamento de sessão): recorda se escolheu o tema claro ou escuro.',
                '<strong>hm-form</strong> (armazenamento de sessão): confirma, na página de agradecimento, que a mensagem do formulário foi enviada.']),
            ('p', '<strong>Estatísticas (só com consentimento).</strong> Google Analytics 4, carregado através do Google Tag Manager:'),
            ('ul', [
                '<strong>_ga:</strong> distingue visitantes, de forma agregada; dura 2 anos.',
                '<strong>_ga_*:</strong> mantém o estado da sessão; dura 2 anos.']),
            ('p', '<strong>Marketing (só com consentimento).</strong> Píxel da Meta (Facebook e Instagram), carregado através do Google Tag Manager:'),
            ('ul', [
                '<strong>_fbp:</strong> mede a eficácia das campanhas nas plataformas da Meta; dura 3 meses.']),
            ('p', 'Enquanto não houver consentimento, o Google Tag Manager funciona em modo de consentimento (Consent Mode v2) e não ativa cookies de estatística nem de publicidade.'),
            ('p', 'O formulário de contacto envia os dados que preencher apenas para responder ao seu pedido, como descrito na <a href="/politica-de-privacidade">Política de Privacidade</a>.')]),
        ('terceiros', 'Serviços de terceiros', [
            ('p', 'O Google Analytics e o Google Tag Manager são serviços da Google Ireland Limited; o píxel da Meta é um serviço da Meta Platforms Ireland Limited. Estes fornecedores podem tratar dados fora da União Europeia, ao abrigo do Quadro de Privacidade de Dados UE-EUA.'),
            ('links', [
                ('https://policies.google.com/privacy?hl=pt-PT', 'Política de privacidade da Google'),
                ('https://www.facebook.com/privacy/policy/', 'Política de privacidade da Meta')])]),
        ('gerir', 'Como gerir os cookies', [
            ('p', 'Pode mudar ou retirar o seu consentimento a qualquer momento no botão «Preferências de cookies», no rodapé de todas as páginas.'),
            ('p', 'O utilizador pode também configurar o seu navegador para recusar cookies ou apagar os que já existem, embora isso possa afetar a funcionalidade de algumas áreas do site. As opções encontram-se nas definições de privacidade de cada navegador.')]),
        ('contacto-cookies', 'Mais informação', [
            ('p', 'Para qualquer questão sobre esta política, contacte a Hortelã Magenta – Design de Comunicação, Lda. através do telefone 211 806 292 ou do e-mail <a href="mailto:info@hortelamagenta.com">info@hortelamagenta.com</a>.')]),
    ])


def mapa():
    proj = [('/projetos/' + s, NAMES[s]) for s in ['camolas'] + [x for x in ORDER if x != 'camolas']]
    return dict(
        path='/mapa-do-site', title='Mapa do site | Hortelã Magenta', h1='Mapa do site',
        desc='Todas as páginas do site da Hortelã Magenta: serviços, especialidades, projetos, blog, contactos e informação legal.',
        lead='Todas as páginas do site da Hortelã Magenta, organizadas por secção.',
        sections=[
            ('principal', 'Páginas principais', [('links', [('/', 'Início'), ('/servicos', 'Serviços'), ('/projetos', 'Projetos'), ('/sobre', 'Sobre'), ('/blog', 'Blog'), ('/contacto', 'Contacto')])]),
            ('servicos', 'Serviços', [('links', [('/servicos/branding', 'Branding'), ('/servicos/design-web', 'Design Web'), ('/servicos/design-grafico-e-editorial', 'Gráfico + Editorial'),
                                                 ('/servicos/campanhas-e-redes-sociais', 'Campanhas & Redes Sociais'), ('/servicos/fotografia-e-video', 'Fotografia & Vídeo'),
                                                 ('/servicos/avenca-comunicacao-360', 'Avença Mensal 360°'), ('/servicos/coaching-de-marcas', 'Coaching de Marcas')])]),
            ('especialidades', 'Especialidades', [('links', list(LANDS))]),
            ('projetos', 'Projetos', [('links', proj)]),
            ('blog', 'Blog', [('links', [('/blog/quanto-custa-um-site', 'Quanto custa um site para empresas?')])]),
            ('legal', 'Informação legal', [('links', [('/politica-de-privacidade', 'Política de Privacidade'), ('/politica-de-cookies', 'Política de Cookies'),
                                                       ('https://www.livroreclamacoes.pt/Inicio/', 'Livro de Reclamações')])]),
        ])


def obrigado(M):
    return dict(
        path='/obrigado', name='Obrigado', current='', crumb='Obrigado',
        title='Obrigado pelo seu contacto | Hortelã Magenta', desc='Recebemos a sua mensagem. A equipa da Hortelã Magenta vai responder em breve.',
        robots='noindex, follow',
        hero=dict(crumbs=[('Início', '/'), ('Contacto', '/contacto'), ('Obrigado', None)], display_is_h1=True, eyebrow='Mensagem enviada',
                  display=['Obrigado.', 'Recebemos a sua'], rot=['mensagem.', 'ideia.', 'história.'],
                  intro='Vamos responder em breve. Se o assunto for urgente, ligue-nos para o (+351) 211 806 292 (chamada para rede fixa nacional). Enquanto isso, conheça alguns dos nossos projetos.',
                  cta=('/projetos', 'Ver projetos →'), cta2=('/', 'Voltar ao início')),
        blocks=[('mais', dict(items=[(NAMES[s], '/projetos/' + s, CARD[s]) for s in ['camolas', 'farinhas-firmos', 'alsil', 'queijaria-da-sao', 'documentos-normativos-imt']]))],
        contact=('Prefere falar já?', 'Estamos na R. Dr. Miguel Bombarda nº 88, na Moita, e ao telefone no (+351) 211 806 292.', 'Ver contactos'),
    )


def erro404(M):
    return dict(
        path='/404', name='Página não encontrada', current='', crumb='Página não encontrada',
        title='Página não encontrada | Hortelã Magenta', desc='A página que procura não existe ou mudou de endereço.',
        robots='noindex, follow', nocanonical=True,
        hero=dict(crumbs=[('Início', '/'), ('Erro 404', None)], display_is_h1=True, eyebrow='Erro 404 · Página não encontrada',
                  display=['Esta página', 'saiu para'], rot=['uma reunião.', 'a gráfica.', 'um café.', 'outro projeto.'],
                  intro='A página que procura não existe ou mudou de endereço. O site da Hortelã Magenta foi renovado: se chegou aqui por uma ligação antiga, comece pela página inicial, pelos serviços ou pelos projetos.',
                  cta=('/', 'Voltar ao início →'), cta2=('/projetos', 'Ver projetos'), veil='#ffffff'),
        blocks=[
            ('links', dict(eyebrow='Talvez procure', title='Por onde quer continuar?', items=[
                ('/servicos', 'Serviços'), ('/projetos', 'Projetos'), ('/sobre', 'Sobre a Hortelã Magenta'), ('/blog', 'Blog'),
                ('/contacto', 'Contacto e pedido de orçamento'), ('/mapa-do-site', 'Mapa do site')])),
            ('mais', dict(items=[(NAMES[s], '/projetos/' + s, CARD[s]) for s in ['camolas', 'consulai', 'alinea', 'croma', 'imperalum']])),
        ],
        contact=('Diga-nos, onde quer chegar?', 'Se não encontrou o que procurava, fale connosco: ajudamos a encontrar a informação ou a definir o seu projeto.', 'Falar connosco'),
    )
