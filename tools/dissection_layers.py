"""Sorts the muscles into dissection layers, from the surface inwards.

    blender -b --python tools/dissection_layers.py -- <models dir> [out.json]

Rays are cast at the body from 16 directions around it and from above and
below at an angle, in parallel grids 4 mm apart. The muscles the rays hit
first make the outermost layer; they are then taken away and the rays cast
again, so the next layer is what lay under them, and so on. A muscle counts
as uncovered when enough rays reach it for its size. Whatever is left after
the last pass joins the deepest layer.

A muscle counts as uncovered when the rays reaching it would cover about a
third of its surface: seen from all around, a fully exposed surface of area A
takes about 32 · A / 4 rays per spacing² (the mean projected area of a convex
body is a quarter of its surface).

Writes <models dir>/muscle-layers.json: {"layers": n, "depth": {part name: layer}}
with layer 0 the most superficial. The app's dissection slider hides the
layers above the one chosen (AnatomyScene.dissection).
"""
import json
import math
import os
import sys

import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'skin'))
from packedit import load  # noqa: E402

args = sys.argv[sys.argv.index('--') + 1:]
MODELS = args[0]
OUT = args[1] if len(args) > 1 else os.path.join(MODELS, 'muscle-layers.json')
MAX_LAYERS = 6
SPACING = 0.004
# Share of a muscle's surface that must be reached to call it uncovered.
EXPOSED = 0.3
MIN_HITS = 4

manifest, parts, lo, hi = load(MODELS, 'muscular')
names = [p['info']['name'] for p in parts]


def area(part):
    co, idx = part['co'], part['idx']
    return float(np.linalg.norm(np.cross(co[idx[:, 1]] - co[idx[:, 0]], co[idx[:, 2]] - co[idx[:, 0]]), axis=1).sum() / 2)



print(f'{len(parts)} muscle parts')


def build(remaining):
    verts, polys, owner = [], [], []
    base = 0
    for i in remaining:
        co, idx = parts[i]['co'], parts[i]['idx']
        verts.extend(map(tuple, co))
        polys.extend(map(tuple, idx + base))
        owner.extend([i] * len(idx))
        base += len(co)
    return BVHTree.FromPolygons(verts, polys, all_triangles=True), owner


def directions():
    out = []
    for k in range(16):
        a = 2 * math.pi * k / 16
        out.append(Vector((math.sin(a), 0, math.cos(a))))
    for pitch in (-0.8, 0.8):
        for k in range(8):
            a = 2 * math.pi * k / 8
            out.append(Vector((math.sin(a) * math.cos(pitch), math.sin(pitch), math.cos(a) * math.cos(pitch))))
    return out


areas = [area(p) for p in parts]
center = Vector(((lo + hi) / 2).tolist())
radius = float(np.linalg.norm(hi - lo)) / 2 + 0.05
sample = np.concatenate([p['co'][::25] for p in parts]) - np.array(center)

depth = {}
remaining = list(range(len(parts)))
for layer in range(MAX_LAYERS):
    if not remaining:
        break
    tree, owner = build(remaining)
    hits = {}
    for d in directions():
        # A grid of rays across the body, perpendicular to `d`, cast towards -d.
        up = Vector((0, 1, 0)) if abs(d.y) < 0.9 else Vector((1, 0, 0))
        u = d.cross(up).normalized()
        v = d.cross(u).normalized()
        # Only across the body's outline seen from `d`.
        pu, pv = sample @ np.array(u), sample @ np.array(v)
        u0, v0 = pu.min() - 0.01, pv.min() - 0.01
        for a in range(int((pu.max() - u0 + 0.01) / SPACING) + 1):
            for b in range(int((pv.max() - v0 + 0.01) / SPACING) + 1):
                origin = center + d * radius + u * (u0 + a * SPACING) + v * (v0 + b * SPACING)
                location, normal, index, distance = tree.ray_cast(origin, -d)
                if index is not None:
                    part = owner[index]
                    hits[part] = hits.get(part, 0) + 1
    rays = len(directions())
    uncovered = [i for i in remaining
                 if hits.get(i, 0) >= max(MIN_HITS, EXPOSED * rays * areas[i] / 4 / SPACING ** 2)]
    if layer == MAX_LAYERS - 1:
        uncovered = remaining
    for i in uncovered:
        depth[names[i]] = layer
    remaining = [i for i in remaining if i not in set(uncovered)]
    print(f'layer {layer}: {len(uncovered)} parts, {len(remaining)} left')

layers = max(depth.values()) + 1
json.dump({'layers': layers, 'depth': depth}, open(OUT, 'w'), ensure_ascii=False, separators=(',', ':'))
print(f'wrote {OUT}: {layers} layers')
