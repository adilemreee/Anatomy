"""Keeps the segmental bronchi inside the lungs.

Z-Anatomy's segmental bronchi end a few millimetres beyond the lung surface
in places, so their tips poke out of the lobes. Every bronchus vertex that
lies outside (or within 2 mm of) the lateral, anterior, posterior or basal
surface of the lungs moves 2 mm under it; the hilum (medial surface, where
the bronchi enter) is left alone.

    Blender -b --python tools/skin/fit_bronchi.py -- <models dir> <out dir>
"""
import os
import sys

import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from packedit import load, save, vertex_normals  # noqa: E402

src, dst = sys.argv[sys.argv.index('--') + 1:][:2]
manifest, parts, lo, hi = load(src, 'visceral')
lungs = [p for p in parts if 'Lungs' in p['info']['path'] and 'lobe' in p['info']['name']]
co = np.concatenate([p['co'] for p in lungs])
offs = np.cumsum([0] + [len(p['co']) for p in lungs])
tris = np.concatenate([p['idx'] + offs[k] for k, p in enumerate(lungs)])
tree = BVHTree.FromPolygons([Vector(v) for v in co], [tuple(map(int, t)) for t in tris])
depth = 0.002
moved_total = 0
for p in parts:
    name = p['info']['name']
    if 'segmental bronchus' not in name:
        continue
    c = p['co']
    moved = 0
    hit = np.zeros(len(c), bool)
    for i, v in enumerate(c):
        loc, nrm, _, dist = tree.find_nearest(Vector(v))
        if loc is None or dist > 0.03:
            continue
        q, nq = np.array(loc), np.array(nrm)
        # the medial (hilar) surface faces the midline
        if np.sign(q[0]) * nq[0] < -0.35:
            continue
        if np.dot(v - q, nq) > -depth:
            c[i] = q - nq * depth
            hit[i] = True
            moved += 1
    if moved:
        # smooth the moved region a little so the tips stay round
        t = p['idx']
        e = np.concatenate([t[:, [0, 1]], t[:, [1, 2]], t[:, [2, 0]]]); e = np.concatenate([e, e[:, ::-1]])
        deg = np.bincount(e[:, 0], minlength=len(c)).clip(1)
        near = hit.copy()
        np.logical_or.at(near, e[:, 0], hit[e[:, 1]])
        for _ in range(2):
            acc = np.zeros_like(c); np.add.at(acc, e[:, 0], c[e[:, 1]])
            c[near] = 0.6 * c[near] + 0.4 * (acc / deg[:, None])[near]
        p['co'] = c
        p['n'] = vertex_normals(c, t)
    moved_total += moved
    print(f'  {name:<60} {moved:5d} vertices moved in', flush=True)
save(dst, 'visceral', manifest, parts, lo, hi)
print('bronchi: moved', moved_total, flush=True)
