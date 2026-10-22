"""The skin layer from BodyParts3D's own skin (tools/skin/bp3d_skin_prep.py).

The skin of the body the atlas bones come from, so it fits them; this makes
sure nothing shows through it anywhere and splits it into the body regions:

  1. Its outer surface: vertices from which rays escape the body (the skin
     also lines the mouth, nostrils, ear canals and navel).
  2. Every bone, cartilage, muscle, vessel, nerve and organ point closer than
     a margin under that outer surface, or outside it, lifts the skin there:
     smooth bumps a few millimetres wide along the normals.
  3. Each triangle takes the Z-Anatomy region nearest to it (its name, group
     path and material), so the regions can be picked and looked up.
  4. Eyes: the atlas's own sclera, iris and lens in the lid openings.

The female body: the same skin without the penis and scrotum (the hole they
leave closed by a smooth membrane with a shallow pudendal cleft), moved by
the female warp (warp.npz), with her breasts: the part of the MakeHuman
female body's difference to the male one that the warp leaves out, carried
over by nearest MakeHuman vertex (her breast tissue lies there). Then lifted
over her (warped) anatomy the same way. Her parts are marked "frame":
"female" (the app does not warp them again).

    Blender -b --python tools/skin/bp3d_skin.py -- <skin.npz> <z-anatomy regions dir> <skeletal dir> \\
        <soft packs dir> <warp.npz> <MakeHuman male skin.npz> <MakeHuman female skin.npz> <out dir>
"""
import os
import sys

import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree
from mathutils.kdtree import KDTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from packedit import load, save, vertex_normals  # noqa: E402
from warp_eval import Warp  # noqa: E402

args = sys.argv[sys.argv.index('--') + 1:]
SKIN, ZREG, BONES, SOFT, WARP, MH_MALE, MH_FEMALE, OUT = args[:8]
MARGIN_BONE, MARGIN_SOFT, REACH = 0.0015, 0.001, 0.006
BUMP = 0.006
_g = np.array([[x, y, z] for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1) if (x, y, z) != (0, 0, 0)], float)
DIRS = [Vector(v / np.linalg.norm(v)) for v in _g]


def bvh(co, tris):
    return BVHTree.FromPolygons([Vector(v) for v in co], [tuple(map(int, t)) for t in tris])


def edges(T):
    e = np.concatenate([T[:, [0, 1]], T[:, [1, 2]], T[:, [2, 0]]])
    return np.concatenate([e, e[:, ::-1]])


def smooth_normals(C, T, it=4):
    e = edges(T); deg = np.bincount(e[:, 0], minlength=len(C)).clip(1)
    n = vertex_normals(C, T)
    for _ in range(it):
        acc = np.zeros_like(n); np.add.at(acc, e[:, 0], n[e[:, 1]])
        n = 0.5 * n + 0.5 * acc / deg[:, None]
        n /= np.linalg.norm(n, axis=1, keepdims=True).clip(1e-12)
    return n


def exterior(C, T):
    """Vertices on the outside of the body: from just off them, a ray
    escapes (no skin within 3 m)."""
    tree = bvh(C, T)
    N = vertex_normals(C, T)
    out = np.zeros(len(C), bool)
    for k, (v, n) in enumerate(zip(C, N)):
        o = Vector(v + n * 0.0008)
        for d in [Vector(n)] + DIRS:
            if tree.ray_cast(o, d, 3.0)[0] is None:
                out[k] = True
                break
    return out


def lift(C, T, ext, samples):
    """Raises the outer skin over `samples` (points, margins): every point
    closer than its margin under the outer surface, or outside it (up to
    REACH), lifts the skin by what it needs, in smooth bumps."""
    face_ext = ext[T].all(1)
    fidx = np.nonzero(face_ext)[0]
    tree = bvh(C, T[fidx])
    req = np.zeros(len(C))
    count = 0
    for pts, margin in samples:
        for p in pts:
            loc, nrm, fi, dist = tree.find_nearest(Vector(p))
            if loc is None or dist > REACH + margin:
                continue
            s = float(np.dot(p - np.array(loc), np.array(nrm)))
            if -margin < s < REACH:
                count += 1
                for v in T[fidx[fi]]:
                    req[v] = max(req[v], s + margin)
    d = req.copy()
    kd = KDTree(len(C))
    for i, v in enumerate(C):
        kd.insert(Vector(v), i)
    kd.balance()
    for j in np.nonzero(req)[0]:
        for _, i, dist in kd.find_range(Vector(C[j]), BUMP):
            t = dist / BUMP
            d[i] = max(d[i], req[j] * (1 - t * t) ** 2)
    d[~ext] = 0.0
    N = smooth_normals(C, T)
    print(f'  lift: {count} points under the skin too close or outside, {int((req > 0).sum())} vertices, '
          f'max {req.max() * 1000:.1f} mm', flush=True)
    return C + N * d[:, None]


def boundary_loops(T):
    from collections import defaultdict
    count = defaultdict(int)
    for t in T:
        for a, b in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0])):
            count[(a, b)] += 1
    nxt = {a: b for (a, b) in count if (b, a) not in count}
    seen, loops = set(), []
    for s0 in nxt:
        if s0 in seen:
            continue
        L, v = [], s0
        while v not in seen and v in nxt:
            seen.add(v); L.append(v); v = nxt[v]
        loops.append(L)
    return loops


def fill_small_holes(C, T, longest=0.03):
    """Closes the small holes left where the outer surface was cut from the
    solid layer: a fan from the middle of each loop shorter than `longest`."""
    add, extra = [], []
    for L in boundary_loops(T):
        p = C[L]
        per = np.linalg.norm(np.diff(np.vstack([p, p[:1]]), axis=0), axis=1).sum()
        if len(L) < 3 or per > longest:
            continue
        k = len(C) + len(extra)
        extra.append(p.mean(0))
        add += [(L[(i + 1) % len(L)], L[i], k) for i in range(len(L))]
    if add:
        C = np.vstack([C, np.array(extra)])
        T = np.vstack([T, np.array(add)])
    print(f'  holes closed: {len(extra)}', flush=True)
    return C, T


# --- inputs ---------------------------------------------------------------------------------------
sk = np.load(SKIN)
C0, T0 = fill_small_holes(sk['co'], sk['idx'])
zman, zparts, zlo, zhi = load(ZREG, 'regions')
INNER = zman['materials'].index('Skin-in')
warp = Warp(WARP)

# region of every skin triangle: the nearest Z-Anatomy region (outer faces, no hairs or nails)
zl_co, zl_t, zl_owner, base = [], [], [], 0
regions = [p for p in zparts if not p['info']['name'].startswith(('Hairs', 'Pubic', 'Eyelashes', 'Nail', 'Perionyx'))
           and p['info'].get('sex') != 'f']
for k, p in enumerate(regions):
    mats = np.concatenate([np.full(n, m) for m, n in p['info']['seg']])[:len(p['idx'])]
    t = p['idx'][mats != INNER]
    zl_co.append(p['co']); zl_t.append(t + base); zl_owner += [k] * len(t); base += len(p['co'])
ztree = bvh(np.concatenate(zl_co), np.concatenate(zl_t))
zl_owner = np.array(zl_owner)
cent = C0[T0].mean(1)
label = np.array([zl_owner[ztree.find_nearest(Vector(c))[2]] for c in cent])


def smooth_labels(T, lab, rounds=4):
    """Evens the region borders: a triangle takes the region of at least two
    of its three neighbours (no spikes along the borders)."""
    from collections import defaultdict
    owner = defaultdict(list)
    for f, t in enumerate(T):
        for a, b in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0])):
            owner[(min(a, b), max(a, b))].append(f)
    nbr = [[] for _ in range(len(T))]
    for fs in owner.values():
        if len(fs) == 2:
            nbr[fs[0]].append(fs[1]); nbr[fs[1]].append(fs[0])
    lab = lab.copy()
    for _ in range(rounds):
        new = lab.copy()
        for f, ns in enumerate(nbr):
            if len(ns) < 2:
                continue
            ls = [lab[g] for g in ns]
            for l_ in set(ls):
                if l_ != lab[f] and ls.count(l_) >= 2:
                    new[f] = l_
                    break
        lab = new
    return lab


label = smooth_labels(T0, label)
print(f'skin {len(C0)} vertices, {len(T0)} triangles; {len(set(label.tolist()))} regions', flush=True)


def dominant(p):
    runs = [(m, n) for m, n in p['info']['seg'] if m != INNER]
    return max(runs, key=lambda r: r[1])[0] if runs else p['info']['seg'][0][0]


# anatomy that must stay under the skin
def soft_samples(sex):
    out = []
    for system, folder, margin in (('skeletal', BONES, MARGIN_BONE), ('muscular', SOFT, MARGIN_SOFT),
                                   ('cardiovascular', SOFT, MARGIN_SOFT), ('nervous', SOFT, MARGIN_SOFT),
                                   ('joints', SOFT, MARGIN_SOFT), ('lymphoid', SOFT, MARGIN_SOFT),
                                   ('visceral', SOFT, MARGIN_SOFT)):
        _, parts, _, _ = load(folder, system)
        pts = []
        for p in parts:
            i = p['info']
            if len(p['co']) == 0 or i.get('sex') not in (None, sex) or i.get('covering') \
                    or 'Eye' in i['path'] or 'Eyeball' in i['path']:
                continue
            if sex == 'm' and i.get('frame') == 'female':
                continue
            c = p['co'][::2]
            if sex == 'f' and i.get('frame') != 'female':
                c = c + warp.disp(c)
            pts.append(c)
        out.append((np.concatenate(pts), margin))
    return out


_, nerv, _, _ = load(SOFT, 'nervous')
EYE = {n: p for p in nerv for n in [p['info']['name']] if n.split('.')[0] in ('Sclera', 'Iris', 'Lens', 'Cornea')}

# the lid openings: the skin also covers the eyes; where it lies on them it
# goes, so the atlas eyes show between the lids
_eye = [EYE[f'{n}.{s_}'] for n in ('Sclera', 'Cornea') for s_ in ('l', 'r')]
_et = bvh(np.concatenate([p['co'] for p in _eye]),
          np.concatenate([p['idx'] + sum(len(q['co']) for q in _eye[:k]) for k, p in enumerate(_eye)]))
_cent = C0[T0].mean(1)
_on_eye = np.array([(abs(c[0]) > 0.012 and 1.57 < c[1] < 1.61 and c[2] > 0.05) and _et.find_nearest(Vector(c))[3] < 0.0016
                    for c in _cent])
T0, label = T0[~_on_eye], label[~_on_eye]
_used = np.unique(T0)
_remap = np.full(len(C0), -1); _remap[_used] = np.arange(len(_used))
C0, T0 = C0[_used], _remap[T0]
print(f'  eye openings: {int(_on_eye.sum())} triangles over the eyes removed', flush=True)


def eyes(sex):
    out = []
    for side in ('l', 'r'):
        co, tris, runs, base = [], [], [], 0
        for name, mat in (('Sclera', 'Sclera'), ('Iris', 'Eye iris'), ('Lens', 'Pupil')):
            p = EYE[f'{name}.{side}']
            c = p['co'] if sex == 'm' else p['co'] + warp.disp(p['co'])
            co.append(c); tris.append(p['idx'] + base); runs.append([mat, len(p['idx'])]); base += len(c)
        out.append((f'Eyeball.{side}', side, np.concatenate(co), np.concatenate(tris), runs))
    return out


manifest = dict(zman)
materials = list(zman['materials'])


def material(name):
    if name not in materials:
        materials.append(name)
    return materials.index(name)


out_parts = []


def add_skin(C, T, lab, sex):
    N = vertex_normals(C, T)
    for k in sorted(set(lab.tolist())):
        info0 = regions[k]['info']
        sel = np.nonzero(lab == k)[0]
        t = T[sel]
        used = np.unique(t)
        remap = np.full(len(C), -1); remap[used] = np.arange(len(used))
        info = {'name': info0['name'], 'base': info0['base'], 'path': info0['path'], 'sex': sex,
                'seg': [[dominant(regions[k]), int(len(t))]], 'source': 'BodyParts3D (FMA7163)'}
        if info0.get('side'):
            info['side'] = info0['side']
        if sex == 'f':
            info['frame'] = 'female'
        out_parts.append({'info': info, 'co': C[used], 'n': N[used], 'idx': remap[t]})


def add_eyes(sex):
    path = ['Regions of human body', 'Regions of head', 'Regions of face', 'Orbital region']
    for name, side, co, tris, runs in eyes(sex):
        info = {'name': name, 'base': 'Eyeball', 'path': path, 'side': side, 'sex': sex,
                'seg': [[material(m), n] for m, n in runs], 'source': 'BodyParts3D via Z-Anatomy'}
        if sex == 'f':
            info['frame'] = 'female'
        out_parts.append({'info': info, 'co': co, 'n': vertex_normals(co, tris), 'idx': tris})


# --- male -----------------------------------------------------------------------------------------
ext = exterior(C0, T0)
print(f'outer surface: {int(ext.sum())} of {len(C0)} vertices', flush=True)
Cm = lift(C0, T0, ext, soft_samples('m'))
add_skin(Cm, T0, label, 'm')
add_eyes('m')

# --- female ---------------------------------------------------------------------------------------
BOX = (0.065, 0.695, 0.88, -0.045)        # |x|, y from, y to, z from: the male genitals and around


def in_box(P, shrink=0.0):
    return (np.abs(P[:, 0]) < BOX[0] - shrink) & (P[:, 1] > BOX[1] + shrink) & (P[:, 1] < BOX[2] - shrink) \
        & (P[:, 2] > BOX[3] + shrink)


def components(T, minimum):
    """Triangles of the connected pieces with at least `minimum` triangles."""
    parent = np.arange(T.max() + 1)

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    for a, b, c in T:
        ra, rb, rc = find(a), find(b), find(c)
        parent[rb] = ra; parent[find(rc)] = ra
    root = np.array([find(t[0]) for t in T])
    keep_roots = {r for r, n in zip(*np.unique(root, return_counts=True)) if n >= minimum}
    return np.array([r in keep_roots for r in root])


def zipper(C, A, B):
    """Triangles joining loop A to loop B (vertex lists), by arc length."""
    pa, pb = C[A], C[B]
    centre = pa.mean(0)
    u, sv, vt = np.linalg.svd(pa - centre)
    ax1, ax2 = vt[0], vt[1]

    def area(p):
        x, y = (p - centre) @ ax1, (p - centre) @ ax2
        return 0.5 * np.sum(x * np.roll(y, -1) - np.roll(x, -1) * y)
    if np.sign(area(pa)) != np.sign(area(pb)):
        B = B[::-1]; pb = pb[::-1]
    k = int(np.argmin(np.linalg.norm(pb - pa[0], axis=1)))
    B = np.roll(B, -k); pb = np.roll(pb, -k, axis=0)

    def params(p):
        seg = np.linalg.norm(np.diff(np.vstack([p, p[:1]]), axis=0), axis=1)
        return np.r_[0, np.cumsum(seg)] / seg.sum()
    ta, tb = params(pa), params(pb)
    i = j = 0
    na, nb = len(A), len(B)
    tris = []
    while i < na or j < nb:
        if j >= nb or (i < na and ta[i + 1] <= tb[j + 1]):
            tris.append((A[i % na], A[(i + 1) % na], B[j % nb])); i += 1
        else:
            tris.append((A[i % na], B[(j + 1) % nb], B[j % nb])); j += 1
    return np.array(tris)


def female_body(C, T, lab):
    """Her skin before the breasts: the BodyParts3D skin around the male
    genitals cut out (a box), the MakeHuman female body's crotch in its
    place (her shape there, simple), joined by a strip of triangles that is
    then eased. Returns the male-frame and female-frame positions, the
    triangles and the regions."""
    cut = in_box(C[T].mean(1))
    T1, L1 = T[~cut], lab[~cut]
    keep = components(T1, 2000)
    T1, L1 = T1[keep], L1[keep]
    loops = boundary_loops(T1)
    A = np.array(max(loops, key=lambda L: len(L) if np.linalg.norm(C[L].mean(0) - [0, 0.8, 0.02]) < 0.12 else 0))
    mm = np.load(MH_MALE)['co']
    ff = np.load(MH_FEMALE)
    fco, fidx = ff['co'], ff['idx']
    ok = (fidx < len(mm)).all(1)
    ptris = fidx[ok][in_box(mm[fidx[ok]].mean(1), 0.008)]
    ptris = ptris[components(ptris, 500)]
    used = np.unique(ptris)
    remap = np.full(len(fco), -1); remap[used] = np.arange(len(used)) + len(C)
    ptris = remap[ptris]
    Cm = np.vstack([C, mm[used]])
    Cf = np.vstack([C + warp.disp(C), fco[used]])
    B = np.array(max(boundary_loops(ptris), key=len))
    strip = zipper(Cf, A, B)
    # wound like the skin around it
    ns = np.cross(Cf[strip[0, 1]] - Cf[strip[0, 0]], Cf[strip[0, 2]] - Cf[strip[0, 0]])
    nk = vertex_normals(Cf, T1)[A[0]]
    if np.dot(ns, nk) < 0:
        strip = strip[:, ::-1].copy()
    urog = next(k for k, p in enumerate(regions) if p['info']['name'].startswith('Urogenital region'))
    T2 = np.vstack([T1, ptris, strip])
    L2 = np.concatenate([L1, np.full(len(ptris) + len(strip), urog)])
    # ease the seam: the strip and two rings either side
    e2 = edges(T2); deg2 = np.bincount(e2[:, 0], minlength=len(Cf)).clip(1)
    soft = np.zeros(len(Cf), bool); soft[A] = True; soft[B] = True
    for _ in range(4):
        grow = soft.copy(); grow[e2[soft[e2[:, 0]], 1]] = True; soft = grow
    for _ in range(40):
        acc = np.zeros_like(Cf); np.add.at(acc, e2[:, 0], Cf[e2[:, 1]])
        Cf[soft] = 0.5 * Cf[soft] + 0.5 * (acc / deg2[:, None])[soft]
    used2 = np.unique(T2)
    remap2 = np.full(len(Cf), -1); remap2[used2] = np.arange(len(used2))
    print(f'  female crotch: {int(cut.sum())} triangles cut, {len(ptris)} from her body, a strip of {len(strip)}',
          flush=True)
    return Cm[used2], Cf[used2], remap2[T2], L2


Cc, Cf, Tf, labf = female_body(C0, T0, label)
# her fuller thighs must not cross the midline: they meet, pressed flat
leg = (Cc[:, 1] < 0.80) & (np.abs(Cc[:, 0]) > 0.004)
side = np.sign(Cc[:, 0])
ef = edges(Tf); degf = np.bincount(ef[:, 0], minlength=len(Cf)).clip(1)
for _ in range(6):
    over = leg & (side * Cf[:, 0] < 0.0012)
    if not over.any():
        break
    push = np.zeros_like(Cf)
    push[over, 0] = side[over] * 0.0012 - Cf[over, 0]
    for _ in range(6):
        acc = np.zeros_like(push); np.add.at(acc, ef[:, 0], push[ef[:, 1]])
        push = 0.5 * push + 0.5 * acc / degf[:, None]
    push *= 1.6
    push[over, 0] = side[over] * 0.0012 - Cf[over, 0]
    Cf = Cf + push * leg[:, None]
# her breasts: what the warp leaves of the MakeHuman female body's difference
# to the male one, by nearest MakeHuman male vertex (in the male frame)
mh_m, mh_f = np.load(MH_MALE)['co'], np.load(MH_FEMALE)['co']
chest_box = (np.abs(mh_m[:, 0]) < 0.24) & (mh_m[:, 1] > 1.0) & (mh_m[:, 1] < 1.5) & (mh_m[:, 2] > -0.04)
idx = np.nonzero(chest_box)[0]
resid = mh_f[idx] - (mh_m[idx] + warp.disp(mh_m[idx]))
kd = KDTree(len(idx))
for j, i in enumerate(idx):
    kd.insert(Vector(mh_m[i]), j)
kd.balance()
y, z, ax = Cc[:, 1], Cc[:, 2], np.abs(Cc[:, 0])
mask = np.clip((y - 1.05) / 0.05, 0, 1) * np.clip((1.45 - y) / 0.05, 0, 1) * np.clip((z + 0.02) / 0.04, 0, 1) \
    * np.clip((0.22 - ax) / 0.03, 0, 1)
breast = np.zeros_like(Cc)
for k in np.nonzero(mask > 0)[0]:
    near = kd.find_n(Vector(Cc[k]), 6)
    w = np.array([np.exp(-(d / 0.006) ** 2) + 1e-6 for _, _, d in near])
    breast[k] = (w[:, None] * resid[[j for _, j, _ in near]]).sum(0) / w.sum() * mask[k]
Cf = Cf + breast
print(f'female breasts: up to {np.linalg.norm(breast, axis=1).max() * 1000:.0f} mm', flush=True)
extf = exterior(Cf, Tf)
# her soft parts are moved under her skin by tools/skin/female_fix.py; the
# skin rises over her bones only
Cf = lift(Cf, Tf, extf, soft_samples('f')[:1])
add_skin(Cf, Tf, labf, 'f')
add_eyes('f')
manifest['materials'] = materials
manifest['system'] = 'regions'
os.makedirs(OUT, exist_ok=True)
save(OUT, 'regions', manifest, out_parts, zlo, zhi)
print(f'regions written: {len(out_parts)} parts, {sum(len(p["idx"]) for p in out_parts)} triangles', flush=True)
