"""Corrects the female warp so nothing reaches through her skin.

The warp (warp_field.py) carries the male body into the female skin from the
skin inwards; near the surface the atlas parts can still end up a little
outside (her narrower crotch, armpits, face). Every part vertex is warped,
tested against her skin, and where it is outside (or within `margin`) the
needed inward move is written into the grids around it and spread a little;
three rounds.

    Blender -b --python tools/skin/warp_fix.py -- <warp.npz> <models dir> <out warp.npz>
<models dir> holds the packs as shipped (the female skin is the regions
pack's "sex": "f" parts).
"""
import os
import sys

import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from packedit import load  # noqa: E402

wpath, models, out = sys.argv[sys.argv.index('--') + 1:][:3]
MARGIN = 0.0015
w = dict(np.load(wpath))
grids = [[w['lo'], float(w['h']), w['D'].astype(np.float64)]]
nsub = len(w['sub_lo']) if 'sub_lo' in w else 0
for k in range(nsub):
    grids.append([w['sub_lo'][k], float(w['hs']), w[f'sub{k}'].astype(np.float64)])


def tri(g, p):
    lo, h, D = g
    dims = np.array(D.shape[:3])
    q = np.clip((p - lo) / h, 0, dims - 1.001)
    i = q.astype(int); f = q - i
    out_ = 0
    for dx in (0, 1):
        for dy in (0, 1):
            for dz in (0, 1):
                wt = (f[:, 0] if dx else 1 - f[:, 0]) * (f[:, 1] if dy else 1 - f[:, 1]) * (f[:, 2] if dz else 1 - f[:, 2])
                out_ = out_ + D[i[:, 0] + dx, i[:, 1] + dy, i[:, 2] + dz] * wt[:, None]
    return out_


def weight(g, p):
    lo, h, D = g
    up = lo + (np.array(D.shape[:3]) - 1) * h
    m = np.minimum((p - lo) / 0.012, (up - p) / 0.012).min(1)
    t = np.clip(m, 0, 1)
    return t * t * (3 - 2 * t)


def disp(p):
    d = tri(grids[0], p)
    for g in grids[1:]:
        t = weight(g, p)
        sel = t > 0
        if sel.any():
            d[sel] += (tri(g, p[sel]) - d[sel]) * t[sel, None]
    return d


# her skin
_, regions, _, _ = load(models, 'regions')
cos, tris, base = [], [], 0
for p in regions:
    i = p['info']
    if i.get('sex') != 'f' or i['name'].startswith(('Eyeball', 'Eyelashes', 'Eyebrow', 'Oral fissure')):
        continue
    cos.append(p['co']); tris.append(p['idx'] + base); base += len(p['co'])
SC, ST = np.concatenate(cos), np.concatenate(tris)
# the lining of the nostrils and the mouth faces into the head: leave it out
full = BVHTree.FromPolygons([Vector(v) for v in SC], [tuple(map(int, t)) for t in ST])
cen = SC[ST].mean(1)
fn = np.cross(SC[ST[:, 1]] - SC[ST[:, 0]], SC[ST[:, 2]] - SC[ST[:, 0]]); fn /= np.linalg.norm(fn, axis=1, keepdims=True).clip(1e-12)
rng = np.random.default_rng(3)
dirs = rng.normal(size=(12, 3)); dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
lining = np.zeros(len(ST), bool)
for k in np.where(cen[:, 1] > 1.45)[0]:
    n = fn[k]
    ds = [n] + [d if np.dot(d, n) > 0 else -d for d in dirs]
    if all(full.ray_cast(Vector(cen[k] + d * 2e-4), Vector(d), 0.08)[0] is not None for d in ds):
        lining[k] = True
print('lining triangles left out', int(lining.sum()), flush=True)
ST = ST[~lining]
tree = BVHTree.FromPolygons([Vector(v) for v in SC], [tuple(map(int, t)) for t in ST])
EYES = np.array([[0.0305, 1.5907, 0.0632], [-0.0305, 1.5907, 0.0632]])

# every part that the app warps
pts = []
for system in ('skeletal', 'muscular', 'cardiovascular', 'nervous', 'joints', 'visceral', 'lymphoid'):
    _, parts, _, _ = load(models, system)
    for p in parts:
        i = p['info']
        if i.get('frame') == 'female' or i.get('sex') == 'm' or 'Eye' in i['path'] or 'Eyeball' in i['path']:
            continue
        pts.append(p['co'][::2])
P = np.concatenate(pts)
P = P[np.min(np.linalg.norm(P[:, None] - EYES[None], axis=2), axis=1) > 0.017]
print('points', len(P), flush=True)

for rnd in range(5):
    W = P + disp(P)
    corr = np.zeros_like(P); bad = np.zeros(len(P), bool)
    for k, v in enumerate(W):
        loc, nrm, _, dist = tree.find_nearest(Vector(v))
        if loc is None or dist > (0.01 if v[1] > 1.45 else 0.04):
            continue
        q, n = np.array(loc), np.array(nrm)
        s = float(np.dot(v - q, n))
        if s > -MARGIN:
            corr[k] = -n * (s + MARGIN * 1.3); bad[k] = True
    print(f'round {rnd}: {int(bad.sum())} points outside or too close, max {np.linalg.norm(corr, axis=1).max() * 1000:.1f} mm', flush=True)
    if bad.sum() == 0:
        break
    Pb, Cb = P[bad], corr[bad]
    for g in grids:
        lo, h, D = g
        dims = np.array(D.shape[:3])
        q = (Pb - lo) / h
        inside = ((q >= 0) & (q <= dims - 1.001)).all(1)
        if not inside.any():
            continue
        q = q[inside]; c = Cb[inside]
        i = q.astype(int); f = q - i
        # every corner of the point's cell gets the full correction (the
        # largest one where several points share a corner)
        C = np.zeros(D.shape); mag = np.zeros(D.shape[:3])
        cm = np.linalg.norm(c, axis=1)
        order = np.argsort(cm)
        for dx in (0, 1):
            for dy in (0, 1):
                for dz in (0, 1):
                    ii = (i[order, 0] + dx, i[order, 1] + dy, i[order, 2] + dz)
                    C[ii] = c[order]          # later (larger) writes win
                    mag[ii] = cm[order]
        # spread a little so the neighbourhood moves along (keep the larger move)
        for _ in range(2 if h > 0.005 else 4):
            S = C.copy()
            S[1:-1, 1:-1, 1:-1] = (C[:-2, 1:-1, 1:-1] + C[2:, 1:-1, 1:-1] + C[1:-1, :-2, 1:-1] + C[1:-1, 2:, 1:-1] + C[1:-1, 1:-1, :-2] + C[1:-1, 1:-1, 2:]) / 6 * 0.9
            take = np.linalg.norm(S, axis=3) > np.linalg.norm(C, axis=3)
            C[take] = S[take]
        g[2] = D + C

w['D'] = grids[0][2].astype(np.float32)
for k in range(nsub):
    w[f'sub{k}'] = grids[k + 1][2].astype(np.float32)
np.savez(out, **w)
print('saved', out, flush=True)
