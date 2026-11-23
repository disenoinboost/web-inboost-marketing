"""Aplica uma lista de edições (JSON) às páginas desempacotadas (dist) para as testar em local.
Uso: python3 -I hortela-magenta/paquetes/aplicar.py <edicoes.json> <dir-dist> [<dir-saida>]
As mesmas edições aplicam-se no servidor ao template dos pacotes com aplicar.php (mesma lógica)."""
import json, sys, os, re
edits = json.load(open(sys.argv[1], encoding='utf-8'))
src, out = sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else sys.argv[2])
os.makedirs(out, exist_ok=True)
pages, bad = {}, []
for e in edits:
    p = e['page']
    if p not in pages: pages[p] = open(os.path.join(src, p + '.html'), encoding='utf-8').read()
    s = pages[p]
    if e['op'] == 'replace':
        n = s.count(e['old'])
        if n != e['count']: bad.append((p, e['why'], n)); continue
        pages[p] = s.replace(e['old'], e['new'])
    elif e['op'] == 'regex':
        n = len(re.findall(e['pattern'], s))
        if n != e['count']: bad.append((p, e['why'], n)); continue
        pages[p] = re.sub(e['pattern'], e['new'], s)
    elif e['op'] == 'insert_after':
        a = s.find(e['anchor']); b = s.find(e['marker'], a) if a >= 0 else -1
        if a < 0 or b < 0 or s.count(e['anchor']) != 1: bad.append((p, e['why'], 'insert')); continue
        b += len(e['marker']); pages[p] = s[:b] + e['text'] + s[b:]
    else:
        a = s.find(e['start']); b = s.find(e['end'], a) if a >= 0 else -1
        if a < 0 or b < 0 or s.count(e['start']) != 1: bad.append((p, e['why'], 'cut')); continue
        pages[p] = s[:a] + s[b + len(e['end']):]
for p, s in pages.items(): open(os.path.join(out, p + '.html'), 'w', encoding='utf-8').write(s)
print('ok', len(edits) - len(bad), 'de', len(edits), '| falhas:', bad)
