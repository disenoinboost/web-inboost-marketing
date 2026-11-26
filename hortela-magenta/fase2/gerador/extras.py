"""Alterações de conteúdo em páginas existentes (fase 2). Cada função recebe o modelo já normalizado (comum.normalizar)
e devolve-o alterado; as substituições verificam que o texto original existe exatamente uma vez."""
import re

from base import esc, att


def _rep(t, a, b, n=1):
    c = t.count(a)
    assert c == n, ('esperado %d, encontrado %d' % (n, c), a[:90])
    return t.replace(a, b)


GONCALO = 'https://hortelamagenta.pt/media/pages/sobre/7f11034ae8-1701343726/hm-equipa-goncalo-700x.jpg'
CTA_STYLE = 'style="font-size:18px; color:#1C1B23; text-decoration:none; border-bottom:1px solid #D82E87; padding-bottom:5px;"'


def servicos(t):
    # a cabeçalho funde-se (véu cinzento) com a primeira secção, como em Branding: «Branding» passa a esse cinzento
    t = t.replace('id="branding" data-screen-label="03 Branding" style="background:#ffffff;', 'id="branding" data-screen-label="03 Branding" style="background:#e8eced;', 1)
    # 1) secções 03–05 e Avenças: «Explorar …» para as páginas novas (como Branding e Design Web)
    for page, label in [('/servicos/design-grafico-e-editorial', 'Explorar Gráfico + Editorial'),
                        ('/servicos/campanhas-e-redes-sociais', 'Explorar Campanhas &amp; Redes Sociais'),
                        ('/servicos/fotografia-e-video', 'Explorar Fotografia &amp; Vídeo')]:
        t = t.replace('<a href="/contacto" ' + CTA_STYLE + '>Pedir orçamento →</a>', '<a href="' + page + '" ' + CTA_STYLE + '>' + label + ' →</a>', 1)
    t = _rep(t, '<a href="/contacto" ' + CTA_STYLE + '>Marcar conversa →</a>',
             '<a href="/servicos/avenca-comunicacao-360" ' + CTA_STYLE + '>Explorar Avenças mensais →</a>')
    # 2) contadores 0N / 06 -> 0N / 07 (entra Coaching de Marcas)
    t = re.sub(r'(\d\d) / 06<', r'\1 / 07<', t)
    # 3) frase da cabeçalho
    t = _rep(t, 'Fotografia &amp; Vídeo e Avenças mensais para dar forma', 'Fotografia &amp; Vídeo, Avenças mensais e Coaching de Marcas para dar forma')
    # 4) acesso rápido: 07 Coaching de Marcas
    li = ('\n    <li style="border-top:1px solid rgba(28,27,35,.16);"><a href="#coaching-de-marcas" style="display:flex; gap:12px; align-items:baseline; padding:18px 0; color:#1C1B23; text-decoration:none;" style-hover="color:#D82E87;">'
          '<span style="font-size:16px; color:#6E6A63; font-variant-numeric:tabular-nums;">07</span><span style="font-size:18px; font-weight:300; letter-spacing:-0.02em; line-height:1.2;">Coaching de Marcas</span></a></li>')
    a = t.index('<a href="#avencas-mensais"')
    b = t.index('</li>', a) + 5
    t = t[:b] + li + t[b:]
    # 5) secção Coaching de Marcas (mesma composição de Avenças, fundo branco e imagem à esquerda)
    sec = f'''

<section data-cursor-bg="light" id="coaching-de-marcas" data-screen-label="07a2 Coaching de Marcas" style="background:#ffffff; padding:var(--sp-block) clamp(16px,4vw,64px) var(--sp-block) clamp(16px,4vw,64px); scroll-margin-top:40px;">
  <div style="display:flex; flex-wrap:wrap; gap:56px clamp(40px,7vw,140px); align-items:flex-start; flex-direction:row-reverse; justify-content:flex-end;">
    <div style="flex:1.3 1 460px; min-width:0; display:flex; flex-direction:column; gap:clamp(20px,3vw,40px);">
      <figure data-rise="" style="margin:0; width:78%; align-self:flex-end;"><div style="aspect-ratio:4/5; overflow:hidden; background:#EEEDEA;"><img src="{GONCALO}" alt="Gonçalo Santos, fundador da Hortelã Magenta" loading="lazy" decoding="async" style="display:block; width:100%; height:100%; object-fit:cover; object-position:50% 20%;"></div><figcaption style="margin-top:10px; font-size:16px; color:rgba(28,27,35,.6); font-weight:400;">Gonçalo Santos · Fundador</figcaption></figure>
    </div>
    <div data-faq-side="" style="flex:1 1 320px; max-width:500px; position:sticky; top:clamp(110px,16vh,150px);">
      <p style="margin:0 0 22px; font-size:16px; color:rgba(28,27,35,.6); font-variant-numeric:tabular-nums; font-weight:400;">07 / 07</p>
      <h2 style="margin:0 0 24px; font-size:clamp(40px,3.68vw,67px); font-weight:100; letter-spacing:-0.05em; line-height:.95; text-wrap:balance;">Coaching de Marcas</h2>
      <p style="margin:0 0 var(--sp-title) 0; font-size:18px; font-weight:300; line-height:1.5; color:#4A4743; text-wrap:pretty;">Às vezes, a sua marca só precisa de ser ouvida. Sessões de coaching de marca para clarificar posicionamento, identidade e comunicação: fazemos perguntas, ouvimos com atenção e ajudamos a marca a encontrar as suas próprias respostas.</p>
      <ul style="list-style:none; margin:0 0 32px; padding:0; border-top:1px solid rgba(28,27,35,.12);"><li style="padding:12px 0; border-bottom:1px solid rgba(28,27,35,.12); font-size:18px; font-weight:300;">Escuta</li><li style="padding:12px 0; border-bottom:1px solid rgba(28,27,35,.12); font-size:18px; font-weight:300;">Diagnóstico</li><li style="padding:12px 0; border-bottom:1px solid rgba(28,27,35,.12); font-size:18px; font-weight:300;">Clarificação</li><li style="padding:12px 0; border-bottom:1px solid rgba(28,27,35,.12); font-size:18px; font-weight:300;">Direção</li></ul>
      <a href="/servicos/coaching-de-marcas" {CTA_STYLE}>Explorar Coaching de Marcas →</a>
    </div>
  </div>
</section>'''
    a = t.index('data-screen-label="07a Avenças mensais"')
    b = t.index('</section>', a) + len('</section>')
    t = t[:b] + sec + t[b:]
    return t


def _blog_sem_exemplos(t):
    """NÃO SE APLICA (2026-11-24, pedido de Laura: manter os seis cartões de exemplo para mostrar como fica o blog).
    Se se quiser retirar os cartões quando houver artigos reais, renomear para blog()."""
    m = re.search(r'const PAGE = \{"items":\[.*?\],"chips":\[.*?\],', t, re.S)
    assert m
    t = t[:m.start()] + 'const PAGE = {"items":[],"chips":[],' + t[m.end():]
    # barra flutuante de filtros (sem artigos para filtrar) e grelha «Todos os artigos»
    n = t.index('<nav aria-label="Filtrar artigos por tema"')
    a = t.rfind('<div', 0, n)
    b = t.index('</div>', t.index('</nav>', n)) + 6
    t = t[:a] + t[b:]
    a = t.index('<p data-posts-top=""')
    b = t.index('</sc-for>', a)
    b = t.index('</div>', b) + 6
    t = t[:a] + t[b:]
    t = t.replace('<span aria-hidden="true">·</span><span>6 min de leitura</span>', '', 1)
    return t


def artigo(t):
    """«Continue a ler» mostrava três artigos que não existem (todos ligavam a este). Passa a «Continue a explorar» com páginas reais."""
    a = t.index('data-screen-label="03 Relacionados"')
    a = t.rfind('<section', 0, a)
    b = t.index('</section>', a) + 10
    cards = [
        ('/servicos/design-web', 'https://hortelamagenta.pt/media/pages/projetos/camolas/93fc94cba4-1736267817/hortelamagenta_portfolio_marca_camolas_site_02-1900x.jpg', 'Serviço', 'Criação de sites para empresas', 'Site da Adega Camolas'),
        ('/projetos/knowledgebiz', 'https://hortelamagenta.pt/media/pages/projetos/knowledgebiz/41d543fd60-1711376064/hortelamagenta_portfolio_marca_knowledgebiz_banner-1900x.jpg', 'Projeto', 'Knowledgebiz: rebranding e website', 'Cartazes da Knowledgebiz'),
        ('/projetos/farinhas-firmos', 'https://hortelamagenta.pt/media/pages/projetos/farinhas-firmos/0d8085f2b6-1733915142/hortelamagenta_portfolio_marca_farinhafirmos_farinha_sacos_02-1900x.jpg', 'Projeto', 'Farinhas Firmos: um projeto 360º', 'Embalagens da Farinhas Firmos'),
    ]
    html = ''.join(f'''
    <a href="{h}" data-cursor="Ver" style="display:block; color:#1C1B23; text-decoration:none;"><div style="aspect-ratio:4/3; overflow:hidden; background:#EEEDEA;"><img src="{img}" alt="{att(alt)}" loading="lazy" decoding="async" style="display:block; width:100%; height:100%; object-fit:cover; transition:transform 1.2s cubic-bezier(.2,.7,.2,1);" style-hover="transform:scale(1.04);"></div><p style="margin:18px 0 12px; font-size:18px; color:#6E6A63;"><span style="color:#1C1B23;">{k}</span></p><h3 data-m="card-title" style="margin:0; font-size:clamp(22px,1.6vw,24px); font-weight:200; letter-spacing:-0.02em; line-height:1.2;">{esc(ti)}</h3></a>''' for h, img, k, ti, alt in cards)
    sec = f'''<section data-cursor-bg="light" data-screen-label="03 Relacionados" style="background:#f6f7f8; padding:var(--sp-block) clamp(16px,4vw,64px) var(--sp-block) clamp(16px,4vw,64px);">
  <div style="display:flex; justify-content:space-between; align-items:flex-end; gap:20px; flex-wrap:wrap; margin-bottom:var(--sp-title);"><h2 data-fw="200@1372:100" style="margin:0; font-size:clamp(34px,2.88vw,51px); font-weight:100; letter-spacing:-0.045em; line-height:1;">Continue a explorar</h2><a href="/projetos" style="font-size:18px; color:#1C1B23; text-decoration:none; border-bottom:1px solid #D82E87; padding-bottom:5px;">Ver todos os projetos →</a></div>
  <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(min(100%,300px),1fr)); gap:48px clamp(24px,3vw,48px); align-items:start;">{html}
  </div>
</section>'''
    return t[:a] + sec + t[b:]


FORM_JS = ("submitForm: e => { e.preventDefault(); const f = e.currentTarget || e.target; if (!f || this.__sending) return; this.__sending = 1; "
           "const fd = new FormData(f); fd.append('pagina', location.pathname); fd.append('t0', String(this.__t0 || 0)); "
           "const done = ok => { this.__sending = 0; if (ok) { try { sessionStorage.setItem('hm-form', '1'); } catch (x) {} location.href = '/obrigado'; } else this.setState({ formErr: true }); }; "
           "fetch('/wp-json/hm/v1/contacto', { method: 'POST', body: fd, credentials: 'same-origin' }).then(r => r.json()).then(d => done(d && d.ok)).catch(() => done(false)); }, "
           "errShow: this.state.formErr ? 'block' : 'none', ")


def contacto(t):
    """Formulário: envia de verdade (POST /wp-json/hm/v1/contacto, ver hm-formulario.php) e segue para /obrigado.
    Campo isco invisível, hora de início e pré-seleção do serviço a partir de ?servico= nas ligações das páginas de serviço."""
    t = _rep(t, "submitForm: e => { e.preventDefault(); this.setState({ sent: true }); }, ", FORM_JS)
    # hora de abertura da página (anti-robô simples)
    t = _rep(t, 'componentDidMount() {', 'componentDidMount() { this.__t0 = Math.floor(Date.now() / 1000);')
    # campo isco (escondido) no início do formulário
    t = _rep(t, 'aria-label="Formulário de contacto" style="display:{{ formShow }};',
             'aria-label="Formulário de contacto" style="display:{{ formShow }};')
    a = t.index('<form sc-camel-on-submit="{{ submitForm }}"')
    b = t.index('>', a) + 1
    honey = '<div aria-hidden="true" style="position:absolute; left:-9999px; width:1px; height:1px; overflow:hidden;"><label for="empresa_url">Não preencher</label><input id="empresa_url" name="empresa_url" type="text" tabindex="-1" autocomplete="off"></div>'
    t = t[:b] + honey + t[b:]
    # mensagem de erro (se o envio falhar)
    err = ('<div role="alert" style="display:{{ errShow }}; grid-column:1 / -1; margin:0; padding:16px 0 0; font-size:18px; font-weight:300; line-height:1.5; color:#4A4743;">'
           'Não foi possível enviar a mensagem. Tente de novo ou fale connosco pelo telefone <a href="tel:+351211806292" style="color:#1C1B23;">(+351) 211 806 292</a>.</div>')
    c = t.index('</form>')
    t = t[:c] + err + t[c:]
    # pré-seleção do serviço (?servico=Branding)
    pre = ('<script>(function(){if(window.__hmSv)return;window.__hmSv=1;try{var v=new URLSearchParams(location.search).get("servico");if(!v)return;var n=0;'
           '(function f(){var s=document.getElementById("servico");if(s){for(var i=0;i<s.options.length;i++){if(s.options[i].text===v){s.selectedIndex=i;break}}return}if(n++<80)setTimeout(f,100)})()}catch(e){}})();</script>')
    t = t.replace('</helmet>', pre + '\n</helmet>', 1)
    return t
