"""Places the breast (HRA mammary gland, its fat body, ducts, areola and
nipple) inside the female skin's breasts.

The parts are moved straight into the female body's frame and marked
`"frame": "female"`, so the app does not warp them again. Every vertex keeps
its place in the breast: the lateral offset from the nipple is scaled to the
female breast, and its depth is spread between the chest wall (the male skin
carried by the warp's chest field, a little deeper) and 2.5 mm under her
skin, column by column along the breast's axis.

    Blender -b --python tools/skin/fit_breast.py -- <models dir> <out dir> <skin dir>
<skin dir> holds female_fin.npz, male_skin_r.npz and warp.npz (tools/skin).
"""
import json
import os
import sys

import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from packedit import load, save, vertex_normals  # noqa: E402

src, dst, sk = sys.argv[sys.argv.index('--') + 1:][:3]
manifest, parts, lo, hi = load(src, 'visceral')
fem = np.load(os.path.join(sk, 'female_fin.npz'))
FC, FT = fem['co'], fem['idx']
male = np.load(os.path.join(sk, 'male_skin_r.npz'))
core = np.load(os.path.join(sk, 'warp.npz'))['core']
chest = male['co'] + core
skin_tree = BVHTree.FromPolygons([Vector(v) for v in FC], [tuple(map(int, t)) for t in FT])
chest_tree = BVHTree.FromPolygons([Vector(v) for v in chest], [tuple(map(int, t)) for t in male['idx']])
FN = vertex_normals(FC, FT)
rig = json.load(open(os.path.join(sk, '..', 'rigs', 'default.mhskel')))
nip_ids = {'l': rig['joints']['breast.L____tail'][0], 'r': rig['joints']['breast.R____tail'][0]}
NAMES = ('Fat body of breast', 'Lobes of mammary gland', 'Lactiferous ducts', 'Areola', 'Nipple')

for side in ('l', 'r'):
    group = [p for p in parts if p['info']['name'] in [f'{n}.{side}' for n in NAMES]]
    if not group:
        continue
    by = {p['info']['name'].rsplit('.', 1)[0]: p for p in group}
    nf = FC[nip_ids[side]]
    a = FN[nip_ids[side]]
    # the breast axis: the skin normal at the nipple, tipped a little forwards
    a = a + np.array([0, 0, 0.6]); a /= np.linalg.norm(a)
    nh = by['Nipple']['co'].mean(0)
    fat = by['Fat body of breast']['co']
    rel = fat - nh
    t_h = rel @ a
    depth_h = -t_h.min()
    lat_h = rel - np.outer(t_h, a)
    # footprint of the female breast mound: skin around the nipple standing out of the chest
    near = np.linalg.norm(FC - nf, axis=1) < 0.11
    rise = np.zeros(len(FC))
    for i in np.where(near)[0]:
        loc, _, _, dd = chest_tree.find_nearest(Vector(FC[i]))
        rise[i] = dd if loc is not None else 0
    mound = near & (rise > 0.006)
    lat_f = FC[mound] - nf
    lat_f -= np.outer(lat_f @ a, a)
    s_lat = np.percentile(np.linalg.norm(lat_f, axis=1), 92) / np.percentile(np.linalg.norm(lat_h, axis=1), 92)
    print(f'{side}: hra depth {depth_h * 1000:.0f} mm, lateral scale {s_lat:.2f}, mound vertices {int(mound.sum())}', flush=True)
    for p in group:
        c = p['co']
        r = c - nh
        t = r @ a
        lat = (r - np.outer(t, a)) * s_lat
        u = np.clip(t / depth_h, -1.2, 0.1)              # -1 at the chest wall, 0 at the nipple
        out = np.empty_like(c)
        for i in range(len(c)):
            q = nf + lat[i]
            o = Vector(q + a * 0.12); d = Vector(-a)
            hs = skin_tree.ray_cast(o, d, 0.3)
            hc = chest_tree.ray_cast(o, d, 0.3)
            if hs[0] is None or hc[0] is None:
                out[i] = nf + lat[i] + a * (u[i] * depth_h); continue
            front = np.array(hs[0]) - a * 0.0025
            back = np.array(hc[0]) - a * 0.007
            if np.dot(front - back, a) < 0.004:          # outside the mound: a thin layer
                back = front - a * 0.004
            out[i] = back + (front - back) * (1 + u[i])
        # areola and nipple lie just under her skin
        if p['info']['name'].startswith(('Areola', 'Nipple')):
            for i in range(len(out)):
                hs = skin_tree.ray_cast(Vector(out[i] + a * 0.05), Vector(-a), 0.1)
                if hs[0] is not None:
                    out[i] = np.array(hs[0]) - a * 0.0008
        p['co'] = out
        p['n'] = vertex_normals(out, p['idx'])
        p['info']['frame'] = 'female'
        print(f'  {p["info"]["name"]:<28} placed', flush=True)

save(dst, 'visceral', manifest, parts, lo, hi)
