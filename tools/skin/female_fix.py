"""Per-vertex corrections for the female body.

The warp (warp-female.bin) moves the atlas into the female skin; a few
thousand vertices still end up outside it or just under it (her narrower
crotch and armpits, fingers, toes, face). For each of them this computes the
extra move that puts it `margin` under her skin, spread over its part like
tools/skin/fit_inside.py (bones move as a whole); the breast, modelled in her
shape and not warped, is checked the same way. The moves are written sparsely:

    "FFX1", system count; per system: name (u8 length + utf-8), count u32,
    then count × (u32 vertex index in the pack, f16 xyz)
raw deflate. The app adds them after the warp (WarpField.swift).

    Blender -b --python tools/skin/female_fix.py -- <warp.npz> <models dir> <out female-fix.bin>

Of the bones only the nose is moved (see `nose_part`).
"""
import os
import struct
import sys
import zlib

import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from packedit import load  # noqa: E402
from pushout import crossings, DIRS  # noqa: E402

wpath, models, out = sys.argv[sys.argv.index('--') + 1:][:3]
MARGIN = 0.0015
EYES = np.array([[0.0305, 1.5907, 0.0632], [-0.0305, 1.5907, 0.0632]])
from warp_eval import Warp  # noqa: E402
disp = Warp(wpath).disp


_, regions, _, _ = load(models, 'regions')
cos, tris, base = [], [], 0
for p in regions:
    i = p['info']
    if i.get('sex') != 'f' or i['name'].startswith(('Eyeball', 'Eyelashes', 'Eyebrow', 'Oral fissure')):
        continue
    cos.append(p['co']); tris.append(p['idx'] + base); base += len(p['co'])
SC, ST = np.concatenate(cos), np.concatenate(tris)
tree = BVHTree.FromPolygons([Vector(v) for v in SC], [tuple(map(int, t)) for t in ST])

blob = bytearray(b'FFX1')
# bones (and the attachment patches on them) stay, the skin is raised over
# them instead; except the nose: her nose is much smaller than the atlas
# skull's nasal bones and cartilages (they would stand up to a centimetre out
# of it), so they go under her skin
systems = ['joints', 'muscular', 'cardiovascular', 'nervous', 'visceral', 'lymphoid', 'skeletal', 'insertions']


def nose_part(info):
    name = info['name']
    return name.startswith(('Nasal bone', 'Nasal septal', 'Lateral process of nasal septal', 'Major alar', 'Maxilla',
                            'Lacrimal bone')) \
        or 'Nasal bone' in info['path'] or 'Nasal cartilages' in info['path']


def nose_box(c):
    """The root and bridge of the nose (atlas frame): of the maxilla only its
    frontal process beside the nasal bones."""
    return (np.abs(c[:, 0]) < 0.035) & (c[:, 1] > 1.555) & (c[:, 1] < 1.64) & (c[:, 2] > 0.055)
blob += struct.pack('<I', len(systems))
for system in systems:
    _, parts, _, _ = load(models, system)
    entries = []
    offset = 0
    rigid = False
    for p in parts:
        i = p['info']
        c = p['co']; n_ = len(c)
        start = offset; offset += n_
        if n_ == 0 or i.get('sex') == 'm' or 'Eye' in i['path'] or 'Eyeball' in i['path']:
            continue
        if system in ('skeletal', 'insertions') and not nose_part(i):
            continue
        # parts modelled in her shape (the breast) are not warped, but they
        # must stay under her skin too (the nipple and ducts reached through it)
        wv = c if i.get('frame') == 'female' else c + disp(c)
        need = np.zeros_like(c); hit = np.zeros(n_, bool)
        allowed = nose_box(c) if system in ('skeletal', 'insertions') else np.ones(n_, bool)
        for k, v in enumerate(wv):
            if not allowed[k] or np.min(np.linalg.norm(EYES - v, axis=1)) < 0.017:
                continue
            loc, nrm, _, dist = tree.find_nearest(Vector(v))
            if loc is None or dist > 0.08:
                continue
            q, nn = np.array(loc), np.array(nrm)
            s = float(np.dot(v - q, nn))
            if s > -MARGIN:
                # in a deep crease (her gluteal cleft, between the thighs) the nearest
                # surface can face the point from the wrong side: whether it is really
                # outside goes by the ray count
                if (s > 0.002 or dist > 0.04) and sum(crossings(tree, v, d) % 2 for d in DIRS[:3]) >= 2:
                    continue
                need[k] = -nn * (s + MARGIN); hit[k] = True
        if not hit.any():
            continue
        if rigid:
            m = np.linalg.norm(need, axis=1)
            d = np.tile(need[m.argmax()], (n_, 1))
        else:
            t = p['idx']
            e = np.concatenate([t[:, [0, 1]], t[:, [1, 2]], t[:, [2, 0]]]); e = np.concatenate([e, e[:, ::-1]])
            deg = np.bincount(e[:, 0], minlength=n_).clip(1)
            d = need.copy()
            for _ in range(8):
                acc = np.zeros_like(d); np.add.at(acc, e[:, 0], d[e[:, 1]])
                spread = acc / deg[:, None] * 0.8
                take = np.linalg.norm(spread, axis=1) > np.linalg.norm(d, axis=1)
                d[take] = spread[take]
                d[hit] = need[hit]
        moved = np.where(np.linalg.norm(d, axis=1) > 1e-5)[0]
        entries += [(start + int(k), d[k]) for k in moved]
    name = system.encode()
    blob += struct.pack('<B', len(name)) + name + struct.pack('<I', len(entries))
    for k, d in entries:
        blob += struct.pack('<I', k) + np.asarray(d, '<f2').tobytes()
    print(f'{system:<14} {len(entries):7d} vertices corrected', flush=True)
comp = zlib.compressobj(9, zlib.DEFLATED, -15)
data = comp.compress(bytes(blob)) + comp.flush()
open(out, 'wb').write(data)
print(f'female fix {len(data) / 1e6:.2f} MB', flush=True)
