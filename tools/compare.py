"""Monta comparativas lado a lado (actual | propuesta) a partir de las capturas de render.js.

Uso: python3 -I tools/compare.py <dir> <salida> [orig] [prop]
Genera: hero de escritorio y de móvil, cada sección con el mismo índice en ambas páginas y las
páginas completas reducidas. Revisa el índice de secciones en report.json si la propuesta añade secciones.
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = None
d, out = sys.argv[1], sys.argv[2]
a, b = sys.argv[3:5] if len(sys.argv) > 4 else ('orig', 'prop')
os.makedirs(out, exist_ok=True)
rep = json.load(open(os.path.join(d, 'report.json')))


def font(size):
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf'):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def side(left, right, labels, dest, scale):
    imgs = [Image.open(x).convert('RGB') for x in (left, right)]
    imgs = [i.resize((int(i.width * scale), int(i.height * scale))) for i in imgs]
    gap = 24
    canvas = Image.new('RGB', (imgs[0].width + imgs[1].width + gap * 3, max(i.height for i in imgs) + 56), (245, 245, 240))
    draw = ImageDraw.Draw(canvas)
    x = gap
    for img, label in zip(imgs, labels):
        canvas.paste(img, (x, 48))
        draw.text((x, 12), label, fill=(20, 20, 20), font=font(22))
        x += img.width + gap
    canvas.save(dest, optimize=True)


def section(name, vp, idx, dest):
    s = rep[f'{name}-{vp}']['sections'][idx]
    full = Image.open(os.path.join(d, 'shots', f'{name}-{vp}-full.png'))
    full.crop((0, s['top'], full.width, s['top'] + s['h'])).save(dest)


shots = os.path.join(d, 'shots')
side(f'{shots}/{a}-desktop-hero.png', f'{shots}/{b}-desktop-hero.png', ('ACTUAL · 1440 px', 'PROPUESTA · 1440 px'), f'{out}/hero-escritorio.png', 0.5)
side(f'{shots}/{a}-mobile-hero.png', f'{shots}/{b}-mobile-hero.png', ('ACTUAL · 390 px', 'PROPUESTA · 390 px'), f'{out}/hero-movil.png', 1.0)
n = min(len(rep[f'{a}-desktop']['sections']), len(rep[f'{b}-desktop']['sections']))
for i in range(n):
    section(a, 'desktop', i, f'{shots}/_a{i}.png')
    section(b, 'desktop', i, f'{shots}/_b{i}.png')
    side(f'{shots}/_a{i}.png', f'{shots}/_b{i}.png', (f'ACTUAL · sección {i}', f'PROPUESTA · sección {i}'), f'{out}/seccion-{i:02d}-escritorio.png', 0.5)
for name in (a, b):
    for vp, w in (('desktop', 480), ('mobile', 390)):
        im = Image.open(f'{shots}/{name}-{vp}-full.png').convert('RGB')
        im.resize((w, int(im.height * w / im.width))).save(f'{out}/completa-{name}-{vp}.jpg', quality=82)
print(sorted(os.listdir(out)))
