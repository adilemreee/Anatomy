"""Keeps the soft parts under the male skin.

The muscles, vessels, nerves and organs come from Z-Anatomy, the skin from
MakeHuman; where the atlas body is fuller than the skin (forehead, armpits,
perineum) a part reaches through it. Every vertex closer than `margin` to the
skin, or outside it, moves to `margin` under it; the move fades out over the
part's mesh so thin muscles bend instead of folding. Bones stay (the skin is
raised over them in build_skin_pack.py), as do the eyes and the parts drawn
in the female frame.

    Blender -b --python tools/skin/fit_inside.py -- <models dir> <out dir> [system ...]
"""
import os
import sys

import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from packedit import load, save, vertex_normals  # noqa: E402

args = sys.argv[sys.argv.index('--') + 1:]
src, dst = args[:2]
systems = args[2:] or ['muscular', 'cardiovascular', 'nervous', 'joints', 'visceral', 'lymphoid']
MARGIN = 0.0015
EYES = np.array([[0.0305, 1.5907, 0.0632], [-0.0305, 1.5907, 0.0632]])

_, regions, _, _ = load(src, 'regions')
skip_skin = ('Eyeball', 'Eyelashes', 'Eyebrow', 'Oral fissure')
cos, tris, base = [], [], 0
for p in regions:
    i = p['info']
    if i.get('sex') != 'm' or i['name'].startswith(skip_skin):
        continue
    cos.append(p['co']); tris.append(p['idx'] + base); base += len(p['co'])
SC, ST = np.concatenate(cos), np.concatenate(tris)
tree = BVHTree.FromPolygons([Vector(v) for v in SC], [tuple(map(int, t)) for t in ST])
print('male skin', len(SC), 'vertices', flush=True)


def is_eye(info):
    return 'Eye' in info['path'] or 'Eyeball' in info['path'] or info['base'] in ('Cornea', 'Lens', 'Iris', 'Sclera')


for system in systems:
    manifest, parts, lo, hi = load(src, system)
    moved_parts = 0
    for p in parts:
        info = p['info']
        if info.get('frame') == 'female' or info.get('sex') == 'f' or is_eye(info) or len(p['co']) == 0:
            continue
        c = p['co']
        need = np.zeros_like(c)
        hit = np.zeros(len(c), bool)
        for k, v in enumerate(c):
            if np.min(np.linalg.norm(EYES - v, axis=1)) < 0.017:
                continue
            loc, nrm, _, dist = tree.find_nearest(Vector(v))
            if loc is None or dist > 0.02:
                continue
            q, n = np.array(loc), np.array(nrm)
            s = float(np.dot(v - q, n))
            if s > -MARGIN:
                need[k] = -n * (s + MARGIN)
                hit[k] = True
        if not hit.any():
            continue
        t = p['idx']
        e = np.concatenate([t[:, [0, 1]], t[:, [1, 2]], t[:, [2, 0]]]); e = np.concatenate([e, e[:, ::-1]])
        deg = np.bincount(e[:, 0], minlength=len(c)).clip(1)
        d = need.copy()
        mag = np.linalg.norm(need, axis=1)
        for _ in range(8):
            acc = np.zeros_like(d); np.add.at(acc, e[:, 0], d[e[:, 1]])
            spread = acc / deg[:, None] * 0.8
            take = np.linalg.norm(spread, axis=1) > np.linalg.norm(d, axis=1)
            d[take] = spread[take]
            d[hit] = need[hit]
        p['co'] = c + d
        p['n'] = vertex_normals(p['co'], t)
        moved_parts += 1
        if mag.max() > 0.004:
            print(f'  {system:<14} {info["name"]:<52} {int(hit.sum()):5d} vertices, up to {mag.max() * 1000:.1f} mm', flush=True)
    save(dst, system, manifest, parts, lo, hi)
    print(system, 'parts moved under the skin:', moved_parts, flush=True)
