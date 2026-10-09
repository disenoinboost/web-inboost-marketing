"""Descomprime la salida de fetch_html.php / bundle_assets.php guardada en tool-results.

Uso: python3 -I tools/unpack.py <archivo-tool-result> <dir>
Escribe <dir>/<nombre>.html y, si vienen recursos, <dir>/site/<ruta>.
"""
import base64
import gzip
import json
import os
import sys

src, out = sys.argv[1], sys.argv[2]
data = json.load(open(src))
data = data.get('data', data)
data = data.get('return_value', data)
os.makedirs(out, exist_ok=True)
for name, b64 in data.get('html', {}).items():
    if b64:
        open(os.path.join(out, name + '.html'), 'wb').write(gzip.decompress(base64.b64decode(b64)))
for path, b64 in data.get('files', {}).items():
    fp = os.path.join(out, 'site', path.lstrip('/'))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, 'wb').write(gzip.decompress(base64.b64decode(b64)))
print('html:', list(data.get('html', {})), '| recursos:', len(data.get('files', {})), '| sin encontrar:', data.get('missing', []))
