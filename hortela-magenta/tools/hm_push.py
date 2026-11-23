"""Genera el `code` de novamira/execute-php que sube la capa de correcciones al sitio.

Uso: python3 -I hortela-magenta/tools/hm_push.py [carpeta_fix]   (por defecto hortela-magenta/fix)
Imprime el PHP (sin <?php): escribe assets/hm-boceto-fix.css y .js en el tema hijo, guarda copia .bak de los
anteriores, comprueba la huella md5 y vacía dist + WP Rocket (hm_dist_reset). Devuelve la versión ?v= que
sirve la portada para confirmar que ya se usa la nueva.
Si el paquete pasa de ~12 KB en base64, conviene partirlo (escribir partes en hm-paginas-bak/ y unirlas).
"""
import base64
import gzip
import hashlib
import json
import os
import sys

d = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', 'fix')
data = {k: open(os.path.join(d, 'hm-boceto-fix.' + k), encoding='utf-8').read() for k in ('css', 'js')}
raw = json.dumps(data, ensure_ascii=False).encode()
b64 = base64.b64encode(gzip.compress(raw, 9, mtime=0)).decode()
sys.stderr.write('base64: %d bytes\n' % len(b64))
print(
    "$raw=gzdecode(base64_decode('" + b64 + "'));"
    "if(md5($raw)!=='" + hashlib.md5(raw).hexdigest() + "') return 'md5 distinto: '.md5($raw);"
    "$d=json_decode($raw,true);$a=get_stylesheet_directory().'/assets/';"
    "foreach(['css','js'] as $k){$f=$a.'hm-boceto-fix.'.$k;if(file_exists($f))copy($f,$f.'.bak-'.date('Ymd-His'));file_put_contents($f,$d[$k]);}"
    "clearstatcache();hm_dist_reset();"
    "$r=wp_remote_get(home_url('/'),['timeout'=>40,'sslverify'=>false]);"
    "preg_match('#hm-boceto-fix\\.js\\?v=(\\d+)#',wp_remote_retrieve_body($r),$m);"
    "return ['http'=>wp_remote_retrieve_response_code($r),'v_servida'=>$m[1]??null,'v_archivo'=>filemtime($a.'hm-boceto-fix.js')];"
)
