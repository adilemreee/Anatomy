"""Renders the App Store header figures from the atlas packs.

    blender -b --python tools/screenshots/render_figures.py -- <models dir> <out dir> [still|turntable] [frames]

Four full-body figures side by side, the layers of the app: skin (drawn as
a white silhouette by compose_creative.py), muscles over the skeleton, the
skeleton, and the skeleton with the heart and vessels. The camera frames the 21:9 product page header (3840 x 1646) on a
transparent background; compose_creative.py puts the background behind it.

still      one front view: <out>/figures.png
turntable  every figure turns once around its own axis in [frames] frames
           (default 360, 12 s at 30 fps), a seamless loop: <out>/frames/0001.png …
"""
import math
import os
import sys

import bpy
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'skin'))
from packedit import load  # noqa: E402

args = sys.argv[sys.argv.index('--') + 1:]
MODELS, OUT = args[0], args[1]
MODE = args[2] if len(args) > 2 else 'still'
FRAMES = int(args[3]) if len(args) > 3 else 360
WIDTH, HEIGHT = 3840, 1646
# Figures 0.9 m apart; the middle two stay inside the header's safe area.
SPACING = 0.9
CENTRE_Z = 0.90          # mid-height of the body
ORTHO = 2.2 * WIDTH / HEIGHT   # 2.2 m of height in frame

SKIN = (0.90, 0.88, 0.86)
BONE = (0.93, 0.88, 0.76)
TEETH = (0.97, 0.96, 0.93)
ARTERY = (0.80, 0.10, 0.12)
VEIN = (0.15, 0.30, 0.78)


def conv(p):
    return np.stack([p[:, 0], -p[:, 2], p[:, 1]], 1)


def mesh(name, co, tris):
    me = bpy.data.meshes.new(name)
    me.from_pydata(conv(co).tolist(), [], tris.tolist())
    me.update()
    me.polygons.foreach_set('use_smooth', [True] * len(me.polygons))
    return me


def place(me, color, pivot):
    ob = bpy.data.objects.new(me.name, me)
    ob.color = (*color, 1.0)
    ob.parent = pivot
    bpy.context.scene.collection.objects.link(ob)
    return ob


def pivot(name, x):
    p = bpy.data.objects.new(name, None)
    p.location = (x, 0, 0)
    bpy.context.scene.collection.objects.link(p)
    return p


bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = 'BLENDER_WORKBENCH'
sh = sc.display.shading
sh.light = 'STUDIO'
sh.color_type = 'OBJECT'
sh.show_cavity = True
sh.cavity_type = 'BOTH'
sh.cavity_ridge_factor = 0.6
sh.cavity_valley_factor = 1.4
sh.show_object_outline = True
sh.object_outline_color = (0.12, 0.03, 0.05)
sh.show_specular_highlight = True
sc.display.render_aa = '16' if MODE == 'still' else '8'
sc.render.resolution_x, sc.render.resolution_y = WIDTH, HEIGHT
sc.render.film_transparent = True
sc.view_settings.view_transform = 'Standard'
sc.render.image_settings.file_format = 'PNG'
sc.render.image_settings.color_mode = 'RGBA'
cam = bpy.data.cameras.new('cam')
cam.type = 'ORTHO'
cam.ortho_scale = ORTHO
camera = bpy.data.objects.new('cam', cam)
camera.location = (0, -4.0, CENTRE_Z)
camera.rotation_euler = (math.pi / 2, 0, 0)
sc.collection.objects.link(camera)
sc.camera = camera

xs = [(-1.5 + i) * SPACING for i in range(4)]
pivots = [pivot(f'figure{i}', x) for i, x in enumerate(xs)]

# The bones are shared by three figures.
_, bones, _, _ = load(MODELS, 'skeletal')
bone_meshes = [(mesh(p['info']['name'], p['co'], p['idx']), TEETH if 'Teeth' in p['info']['path'] else BONE) for p in bones]

# 1 skin
_, regions, _, _ = load(MODELS, 'regions')
for p in regions:
    i = p['info']
    # The genital region is left out: store assets must suit a 4+ rating.
    if i.get('sex') == 'f' or i['name'].startswith(('Eyelashes', 'Eyebrow', 'Urogenital region')):
        continue
    place(mesh(i['name'], p['co'], p['idx']), (0.12, 0.12, 0.14) if i['name'].startswith('Eyeball') else SKIN, pivots[0])

# 2 muscles over the skeleton
rng = np.random.default_rng(3)
_, muscles, _, _ = load(MODELS, 'muscular')
for p in muscles:
    i = p['info']
    name = i['name'].lower()
    if i.get('sex') == 'f' or 'fascia' in name or 'sheath' in name or 'bursa' in name or 'retinacul' in name:
        continue
    t = rng.uniform(-1, 1)
    place(mesh(i['name'], p['co'], p['idx']), (0.78 + 0.06 * t, 0.11 + 0.03 * t, 0.13 + 0.02 * t), pivots[1])
for me, color in bone_meshes:
    place(me, color, pivots[1])

# 3 skeleton
for me, color in bone_meshes:
    place(me, color, pivots[2])

# 4 skeleton with the heart and vessels
for me, color in bone_meshes:
    place(me, tuple(c * 0.92 for c in color), pivots[3])
_, vessels, _, _ = load(MODELS, 'cardiovascular')
for p in vessels:
    i = p['info']
    if i.get('sex') == 'f':
        continue
    venous = 'Venous' in ' '.join(i['path']) or ' vein' in i['name'].lower() or 'sinus' in i['name'].lower()
    place(mesh(i['name'], p['co'], p['idx']), VEIN if venous else ARTERY, pivots[3])


def render(path):
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)


if MODE == 'still':
    render(os.path.join(OUT, 'figures.png'))
else:
    os.makedirs(os.path.join(OUT, 'frames'), exist_ok=True)
    for f in range(FRAMES):
        angle = 2 * math.pi * f / FRAMES
        for p in pivots:
            p.rotation_euler = (0, 0, angle)
        render(os.path.join(OUT, 'frames', f'{f + 1:04d}.png'))
print('rendered', MODE, flush=True)
