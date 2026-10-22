"""Renders the anatomical layers of the app icon from the atlas packs.

    Blender -b --python tools/icon/render_layers.py -- <models dir> <out dir> [frame]

Front views, orthographic, on a transparent background, all with the same
camera (`frame`: "body" for the whole figure, "bust" from the head to the
hips):

    skin.png     the male skin as a flat white silhouette (genitals, hair,
                 eyes and lashes left out)
    anatomy.png  the muscles over the skeleton, softly lit, each muscle a
                 slightly different red, bones ivory, with outlines

tools/icon/make_icon.py splits them down the middle and builds the icon.
"""
import os
import sys

import bpy
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'skin'))
from packedit import load  # noqa: E402

args = sys.argv[sys.argv.index('--') + 1:]
MODELS, OUT = args[0], args[1]
FRAME = args[2] if len(args) > 2 else 'body'
SIZE = 2048
os.makedirs(OUT, exist_ok=True)

# frame: (centre x, centre y, ortho height)
FRAMES = {'body': (0.0, 0.875, 1.86), 'bust': (0.0, 1.265, 1.06)}


def conv(p):
    return np.stack([p[:, 0], -p[:, 2], p[:, 1]], 1)


def add(name, co, tris, color):
    me = bpy.data.meshes.new(name)
    me.from_pydata(conv(co).tolist(), [], tris.tolist())
    me.update()
    me.polygons.foreach_set('use_smooth', [True] * len(me.polygons))
    ob = bpy.data.objects.new(name, me)
    ob.color = (*color, 1.0)
    bpy.context.scene.collection.objects.link(ob)


def scene(flat):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.render.engine = 'BLENDER_WORKBENCH'
    sh = sc.display.shading
    sh.light = 'FLAT' if flat else 'STUDIO'
    sh.color_type = 'OBJECT'
    sh.show_cavity = not flat
    sh.cavity_type = 'BOTH'
    sh.cavity_ridge_factor = 0.6
    sh.cavity_valley_factor = 1.4
    sh.show_object_outline = not flat
    sh.object_outline_color = (0.30, 0.03, 0.06)
    sh.show_specular_highlight = False
    sc.render.resolution_x = sc.render.resolution_y = SIZE
    sc.render.film_transparent = True
    sc.view_settings.view_transform = 'Standard'
    sc.render.image_settings.color_mode = 'RGBA'
    cx, cy, h = FRAMES[FRAME]
    cam = bpy.data.cameras.new('c'); cam.type = 'ORTHO'; cam.ortho_scale = h
    co = bpy.data.objects.new('c', cam); sc.collection.objects.link(co); sc.camera = co
    co.location = (cx, -3.0, cy)
    co.rotation_euler = (np.pi / 2, 0, 0)
    return sc


def render(path):
    bpy.context.scene.render.filepath = path
    bpy.ops.render.render(write_still=True)


# --- skin silhouette ---
scene(flat=True)
_, regions, _, _ = load(MODELS, 'regions')
for p in regions:
    i = p['info']
    if i.get('sex') != 'm' or i['name'].startswith(('Eyeball', 'Eyelashes', 'Eyebrow', 'Penis', 'Scrotum')):
        continue
    add(i['name'], p['co'], p['idx'], (1.0, 1.0, 1.0))
render(os.path.join(OUT, 'skin.png'))

# --- muscles over the skeleton ---
scene(flat=False)
rng = np.random.default_rng(3)
_, muscles, _, _ = load(MODELS, 'muscular')
for p in muscles:
    i = p['info']
    if i.get('sex') == 'f' or i.get('fascia') or 'fascia' in i['name'].lower() or 'sheath' in i['name'].lower() \
            or 'Bursa' in i['name'] or 'bursa' in i['name'] or 'retinacul' in i['name'].lower():
        continue
    t = rng.uniform(-1, 1)
    add(i['name'], p['co'], p['idx'], (0.80 + 0.06 * t, 0.10 + 0.03 * t, 0.12 + 0.02 * t))
_, bones, _, _ = load(MODELS, 'skeletal')
for p in bones:
    i = p['info']
    add(i['name'], p['co'], p['idx'], (0.93, 0.88, 0.76) if 'Teeth' not in i['path'] else (0.97, 0.96, 0.93))
render(os.path.join(OUT, 'anatomy.png'))
print('rendered', FRAME, flush=True)
