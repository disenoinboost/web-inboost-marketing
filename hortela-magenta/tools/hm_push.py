"""Genera el `code` de novamira/execute-php que sube la capa de correcciones al sitio.

Uso: python3 -I hortela-magenta/tools/hm_push.py [carpeta_fix]   (por defecto hortela-magenta/capa-fix)
Imprime el PHP (sin <?php): escribe assets/hm-boceto-fix.css y .js en el tema hijo, guarda copia .bak de los
anteriores, comprueba la huella md5 y vacía dist + WP Rocket (hm_dist_reset). Devuelve la versión ?v= que
sirve la portada para confirmar que ya se usa la nueva.

PROTECCIÓN CONTRA PISAR CAMBIOS (2026-11-27): el 24-nov dos sesiones subieron la capa sobre el mismo archivo y la
segunda borró correcciones de la primera (visor de fotos al tocar, filtros de Projetos). Ahora el PHP solo escribe
si el archivo del servidor es exactamente la versión del último commit (git HEAD) de la que parte esta copia, o ya
es la nueva. Si no, NO escribe y devuelve las huellas: hay que traer la versión del servidor, fusionarla y volver
a intentarlo. Saltarse la comprobación solo con --forzar y sabiendo qué se pisa.
"""
import base64
import gzip
import hashlib
import json
import os
import subprocess
import sys

args = [a for a in sys.argv[1:] if not a.startswith('--')]
forzar = '--forzar' in sys.argv
d = args[0] if args else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'capa-fix')
data, base = {}, {}
for k in ('css', 'js'):
    f = os.path.join(d, 'hm-boceto-fix.' + k)
    data[k] = open(f, encoding='utf-8').read()
    rel = os.path.relpath(os.path.abspath(f), subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=d, text=True).strip())
    prev = subprocess.run(['git', 'show', 'HEAD:' + rel], cwd=d, capture_output=True).stdout
    base[k] = hashlib.md5(prev).hexdigest() if prev else ''
new = {k: hashlib.md5(v.encode()).hexdigest() for k, v in data.items()}
raw = json.dumps(data, ensure_ascii=False).encode()
b64 = base64.b64encode(gzip.compress(raw, 9, mtime=0)).decode()
sys.stderr.write('base64: %d bytes · base %s · nueva %s\n' % (len(b64), base, new))
print(
    "$raw=gzdecode(base64_decode('" + b64 + "'));"
    "if(md5($raw)!=='" + hashlib.md5(raw).hexdigest() + "') return 'md5 distinto: '.md5($raw);"
    "$d=json_decode($raw,true);$a=get_stylesheet_directory().'/assets/';"
    "$base=" + json.dumps(base) + ";$new=" + json.dumps(new) + ";$forzar=" + ('true' if forzar else 'false') + ";"
    "foreach(['css','js'] as $k){$f=$a.'hm-boceto-fix.'.$k;$m=file_exists($f)?md5_file($f):'';"
    "if(!$forzar&&$m!==$base[$k]&&$m!==$new[$k]) return ['NO SUBIDO'=>'el servidor tiene otra version de hm-boceto-fix.'.$k.' (otra sesion la cambio): traerla, fusionar y repetir','servidor'=>$m,'esperado'=>$base[$k]];}"
    "foreach(['css','js'] as $k){$f=$a.'hm-boceto-fix.'.$k;if(file_exists($f))copy($f,$f.'.bak-'.date('Ymd-His'));file_put_contents($f,$d[$k]);}"
    "clearstatcache();hm_dist_reset();"
    "$r=wp_remote_get(home_url('/'),['timeout'=>40,'sslverify'=>false]);"
    "preg_match('#hm-boceto-fix\\.js\\?v=(\\d+)#',wp_remote_retrieve_body($r),$m);"
    "return ['http'=>wp_remote_retrieve_response_code($r),'v_servida'=>$m[1]??null,'v_archivo'=>filemtime($a.'hm-boceto-fix.js'),'md5'=>['css'=>md5_file($a.'hm-boceto-fix.css'),'js'=>md5_file($a.'hm-boceto-fix.js')]];"
)
