"""Vulva for the female skin, rebuilt as one clean patch.

The crotch of her skin (make_female2.py opens a 28 mm bed between the thighs)
is cut out around the midline and refilled with a regular 0.35 mm grid in a
chart along the midline, stitched to the rest of the skin by a constrained
Delaunay triangulation. The patch is a height field over the chart
(H along the midline's outward normal), so nothing can fold: a smoothed base
(the bed) plus an anatomical relief - labia majora, the pudendal cleft, the
labia minora with ruffled edges, the clitoral hood and glans, the vestibule
with the urethral orifice and the introitus, the fourchette and the perineal
raphe. The introitus and the urethral orifice lie under the vagina and the
female urethra of the visceral pack.

Chart: S = arc length (mm) along the crotch midline, X = lateral (mm, + left),
H = distance (mm) along the outward normal of the midline.

    Blender -b --python tools/skin/vulva.py -- <female_fin.npz> <labels.npy> <visceral pack dir> <out.npz> <anus x,y,z>
"""
import os, sys, json, math, numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree
from mathutils.geometry import delaunay_2d_cdt

args = sys.argv[sys.argv.index('--') + 1:]
skin_path, lab_path, vis_dir, out_path = args[:4]
ANUS = np.array([float(v) for v in args[4].split(',')])
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from packedit import load  # noqa: E402

s_ = np.load(skin_path); C = s_['co'].copy(); T = s_['idx']
lab = np.load(lab_path); names = json.load(open(lab_path.replace('.npy', '_names.json')))
ts = s_['tri_src'] if 'tri_src' in s_.files else np.arange(len(T))
lab = np.where(ts >= 0, lab[np.clip(ts, 0, None)], -1)
oldlab = np.array([names[l] if l >= 0 else 'Skin' for l in lab], dtype=object)
O = np.array([0.0, 0.835, -0.005])
tree0 = BVHTree.FromPolygons([Vector(v) for v in C], [tuple(map(int, t)) for t in T])

# --- the midline: rays in the median plane ------------------------------------------------------
ths = np.radians(np.arange(-62, 100, 0.25))
pts = []
for th in ths:
    hit = tree0.ray_cast(Vector(O), Vector((0, -math.cos(th), math.sin(th))), 0.3)
    pts.append(hit[0])
mid = np.array([[0.0, p[1], p[2]] for p in pts if p is not None])
k = np.ones(9) / 9
for a in (1, 2):
    mid[:, a] = np.convolve(np.pad(mid[:, a], 4, mode='edge'), k, 'valid')
seg = np.linalg.norm(np.diff(mid, axis=0), axis=1)
arc = np.concatenate([[0], np.cumsum(seg)]) * 1000.0
tan = np.gradient(mid, axis=0); tan /= np.linalg.norm(tan, axis=1, keepdims=True)
nrm = np.stack([np.zeros(len(tan)), -tan[:, 2], tan[:, 1]], 1)
nrm[((mid - O) * nrm).sum(1) < 0] *= -1
low = np.argmin(np.where(np.abs(mid[:, 2] - O[2]) < 0.04, mid[:, 1], 9))
arc -= arc[low]


def frame(S):
    M = np.stack([np.interp(S, arc, mid[:, a]) for a in range(3)], -1)
    N = np.stack([np.interp(S, arc, nrm[:, a]) for a in range(3)], -1)
    return M, N / np.linalg.norm(N, axis=-1, keepdims=True)


def chart(p):
    """X, S, H (mm) of points p: S by projection onto the midline polyline (median plane)."""
    p = np.atleast_2d(p)
    A = mid[:-1, 1:]; B = mid[1:, 1:]; AB = B - A; L2 = (AB ** 2).sum(1)
    X = p[:, 0] * 1000.0
    S = np.zeros(len(p)); H = np.zeros(len(p))
    for c0 in range(0, len(p), 4000):
        q = p[c0:c0 + 4000, 1:]
        t = np.clip(((q[:, None] - A[None]) * AB[None]).sum(2) / L2[None], 0, 1)
        proj = A[None] + t[..., None] * AB[None]
        d = np.linalg.norm(q[:, None] - proj, axis=2)
        j = d.argmin(1); tj = t[np.arange(len(q)), j]
        Sv = arc[j] + tj * (arc[j + 1] - arc[j])
        M, N = frame(Sv)
        S[c0:c0 + 4000] = Sv
        H[c0:c0 + 4000] = ((q - M[:, 1:]) * N[:, 1:]).sum(1) * 1000.0
    return X, S, H


def point(X, S, H):
    M, N = frame(S)
    return M + np.stack([X / 1000.0, np.zeros_like(X), np.zeros_like(X)], -1) + N * (H / 1000.0)[:, None]


# --- landmarks from the internal anatomy -----------------------------------------------------------
_, vis, _, _ = load(vis_dir, 'visceral')
def bottom(name):
    c = next(p['co'] for p in vis if p['info']['name'] == name)
    return c[c[:, 1] < c[:, 1].min() + 0.003].mean(0)
VAG, URE = bottom('Vagina'), bottom('Female urethra')
_, S_INTRO, H_VAG = [float(v[0]) for v in chart(VAG[None])]
_, S_URE, H_URE = [float(v[0]) for v in chart(URE[None])]
_, S_ANUS, _ = [float(v[0]) for v in chart(ANUS[None])]
S_FOUR = S_INTRO - 12.0          # posterior commissure (fourchette)
S_GLANS = S_URE + 15.0
S_ANT = S_GLANS + 11.0           # anterior commissure
S_LO, S_HI = max(S_ANUS + 14.0, S_FOUR - 42.0), S_ANT + 14.0
print(f'landmarks S (mm): anus {S_ANUS:.1f}, fourchette {S_FOUR:.1f}, introitus {S_INTRO:.1f} (vagina {H_VAG:.1f} mm in), '
      f'urethra {S_URE:.1f} ({H_URE:.1f} mm in), glans {S_GLANS:.1f}, anterior commissure {S_ANT:.1f}; zone {S_LO:.1f}..{S_HI:.1f}', flush=True)
XW = 10.5


def xw(S):
    # narrower over the perineum
    t = np.clip((S - (S_FOUR - 30.0)) / 24.0, 0, 1)
    return 7.5 + 3.0 * t * t * (3 - 2 * t)

# --- the zone: cut out, find its border loop ----------------------------------------------------------
box = (np.abs(C[:, 0]) < 0.04) & (C[:, 1] < 0.87) & (np.abs(C[:, 2] - O[2]) < 0.11)
VX = np.full(len(C), 1e9); VS = np.full(len(C), 1e9); VH = np.full(len(C), 1e9)
VX[box], VS[box], VH[box] = chart(C[box])
vin = box & (np.abs(VX) < xw(VS)) & (VS > S_LO) & (VS < S_HI) & (VH < 11) & (VH > -15)
tz = vin[T].all(1)
# keep the largest connected piece, then fill the holes in it
from collections import defaultdict
edge_tris = defaultdict(list)
for i, t in enumerate(T):
    for a, b in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0])):
        edge_tris[(min(a, b), max(a, b))].append(i)
nbr = defaultdict(list)
for tl in edge_tris.values():
    if len(tl) == 2:
        nbr[tl[0]].append(tl[1]); nbr[tl[1]].append(tl[0])


def components(mask):
    seen = np.zeros(len(T), bool); comps = []
    for s0 in np.where(mask)[0]:
        if seen[s0]:
            continue
        stack = [s0]; seen[s0] = True; comp = []
        while stack:
            f = stack.pop(); comp.append(f)
            for g in nbr[f]:
                if mask[g] and not seen[g]:
                    seen[g] = True; stack.append(g)
        comps.append(comp)
    return comps


comps = components(tz)
main = max(comps, key=len)
tz = np.zeros(len(T), bool); tz[main] = True
# holes: pieces of the rest near the zone that do not reach far
rest = components(~tz & box[T].all(1))
for comp in rest:
    if len(comp) < 2000:
        tz[comp] = True
print('zone triangles', int(tz.sum()), flush=True)
# border edges: one zone triangle, one outside
bedges = []
for (a, b), tl in edge_tris.items():
    z = [tz[i] for i in tl]
    if len(tl) == 2 and z[0] != z[1]:
        f = tl[0] if z[0] else tl[1]
        t = T[f]
        # keep the zone triangle's winding: (a, b) as it runs in that triangle
        for u, v in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0])):
            if {u, v} == {a, b}:
                bedges.append((u, v))
nxt = {u: v for u, v in bedges}
assert len(nxt) == len(bedges), 'border is not a simple loop'
loop = [bedges[0][0]]
while True:
    v = nxt[loop[-1]]
    if v == loop[0]:
        break
    loop.append(v)
assert len(loop) == len(bedges), f'several border loops ({len(loop)} of {len(bedges)} edges)'
loop = np.array(loop)
# densify the border: points every ~0.45 mm on each border edge; the outside
# triangle along it is refanned around its centroid (no T-junctions)
edge_pts = {}
extra = []
n_old = len(C)
dense = []
for i in range(len(loop)):
    u, v = loop[i], loop[(i + 1) % len(loop)]
    L_ = np.linalg.norm(C[v] - C[u]) * 1000.0
    k_ = max(0, int(math.ceil(L_ / 0.45)) - 1)
    ids = []
    for j in range(1, k_ + 1):
        extra.append(C[u] + (C[v] - C[u]) * (j / (k_ + 1)))
        ids.append(n_old + len(extra) - 1)
    edge_pts[(u, v)] = ids
    dense += [u] + ids
outT, outL = [], []
touched = np.zeros(len(T), bool)
for (u, v), ids in edge_pts.items():
    if not ids:
        continue
    f = next(i for i in edge_tris[(min(u, v), max(u, v))] if not tz[i])
    touched[f] = True
for f in np.where(touched)[0]:
    t = T[f]
    ring = []
    for a, b in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0])):
        ring.append(a)
        if (b, a) in edge_pts:               # the zone runs the edge the other way
            ring += edge_pts[(b, a)][::-1]
    extra.append(C[t].mean(0)); cidx = n_old + len(extra) - 1
    for j in range(len(ring)):
        outT.append((cidx, ring[j], ring[(j + 1) % len(ring)])); outL.append(oldlab[f])
C = np.vstack([C, np.array(extra)]) if extra else C
loop = np.array(dense)
VX = np.concatenate([VX, np.full(len(extra), 1e9)]); VS = np.concatenate([VS, np.full(len(extra), 1e9)]); VH = np.concatenate([VH, np.full(len(extra), 1e9)])
newb = loop >= n_old
VX[loop[newb]], VS[loop[newb]], VH[loop[newb]] = chart(C[loop[newb]])
print('border densified to', len(loop), 'points;', int(touched.sum()), 'outside triangles refanned', flush=True)
LX, LS, LH = VX[loop], VS[loop], VH[loop]
print('border loop', len(loop), 'vertices', flush=True)

# --- the grid -----------------------------------------------------------------------------------------
G_ = 0.3
gx, gs = np.meshgrid(np.arange(-XW, XW + 1e-6, G_), np.arange(S_LO, S_HI + 1e-6, G_))
gx, gs = gx.ravel(), gs.ravel()
poly = np.stack([LX, LS], 1)


def inside_poly(px, py):
    res = np.zeros(len(px), bool)
    x0, y0 = poly[:, 0], poly[:, 1]; x1, y1 = np.roll(x0, -1), np.roll(y0, -1)
    for a in range(len(poly)):
        c = ((y0[a] > py) != (y1[a] > py)) & (px < (x1[a] - x0[a]) * (py - y0[a]) / (y1[a] - y0[a] + 1e-12) + x0[a])
        res ^= c
    return res


def dist_poly(px, py):
    P = np.stack([px, py], 1); A = poly; B = np.roll(poly, -1, 0); AB = B - A; L2 = (AB ** 2).sum(1).clip(1e-12)
    out = np.full(len(P), 1e9)
    for c0 in range(0, len(P), 3000):
        q = P[c0:c0 + 3000]
        t = np.clip(((q[:, None] - A[None]) * AB[None]).sum(2) / L2[None], 0, 1)
        d = np.linalg.norm(q[:, None] - (A[None] + t[..., None] * AB[None]), axis=2)
        out[c0:c0 + 3000] = d.min(1)
    return out


ins = inside_poly(gx, gs)
gx, gs = gx[ins], gs[ins]
dgrid = dist_poly(gx, gs)
keepg = dgrid > 0.6 * G_
gx, gs, dgrid = gx[keepg], gs[keepg], dgrid[keepg]
nb = len(loop)
V2 = np.concatenate([poly, np.stack([gx, gs], 1)])
E2 = [(i, (i + 1) % nb) for i in range(nb)]
out = delaunay_2d_cdt([Vector(v) for v in V2], E2, [], 0, 1e-6, True)
ov, oe, of, orig_v = out[0], out[1], out[2], out[3]
assert len(ov) == len(V2), f'CDT added vertices ({len(ov)} vs {len(V2)}): the border folds in the chart'
omap = np.array([o[0] for o in orig_v])
F2 = np.array([[omap[i] for i in f] for f in of if len(f) == 3])
cen = V2[F2].mean(1)
F2 = F2[inside_poly(cen[:, 0], cen[:, 1])]
print('patch', len(V2), 'vertices', len(F2), 'triangles', flush=True)

# --- the base: ray-cast heights, low-passed; border exact ---------------------------------------------
PX, PS = V2[:, 0], V2[:, 1]
Hr = np.zeros(len(V2)); Hr[:nb] = LH
# from inside the body outwards: the first hit is her skin (a thin flap of the
# atlas skin hangs below it on the right side of the perineum; it is dropped)
start = point(PX[nb:], PS[nb:], np.full(len(PX) - nb, -14.0))
start_o = point(PX[nb:], PS[nb:], np.full(len(PX) - nb, 25.0))
_, Nd = frame(PS[nb:])
for i in range(len(start)):
    hit = tree0.ray_cast(Vector(start[i]), Vector(Nd[i]), 0.04)
    if hit[0] is not None and abs(np.dot(np.array(hit[1]), Nd[i])) < 0.3:
        Hr[nb + i] = np.nan                  # grazing a steep wall: filled from the neighbours
        continue
    if hit[0] is not None and hit[3] * 1000.0 - 14.0 < 12.0:
        Hr[nb + i] = hit[3] * 1000.0 - 14.0
        continue
    hit = tree0.ray_cast(Vector(start_o[i]), Vector(-Nd[i]), 0.06)
    ok_ = hit[0] is not None and abs(np.dot(np.array(hit[1]), Nd[i])) >= 0.3
    Hr[nb + i] = 25.0 - hit[3] * 1000.0 if ok_ else np.nan
e2 = np.concatenate([F2[:, [0, 1]], F2[:, [1, 2]], F2[:, [2, 0]]]); e2 = np.unique(np.sort(e2, 1), axis=0)
e2 = np.concatenate([e2, e2[:, ::-1]])
deg2 = np.bincount(e2[:, 0], minlength=len(V2)).clip(1)


def lap(a, fixed=None, it=1, w=0.5):
    for _ in range(it):
        acc = np.zeros_like(a); np.add.at(acc, e2[:, 0], a[e2[:, 1]])
        new = a + (acc / deg2 - a) * w
        if fixed is not None:
            new[fixed] = a[fixed]
        a = new
    return a


bad = np.isnan(Hr)
if bad.any():
    Hr[bad] = np.nanmean(Hr)
    for _ in range(600):
        acc = np.zeros(len(V2)); np.add.at(acc, e2[:, 0], Hr[e2[:, 1]])
        Hr[bad] = (acc / deg2)[bad]
print('rays missed', int(bad.sum()), flush=True)
Hs = lap(Hr.copy(), None, 150)
fixed = np.zeros(len(V2), bool); fixed[:nb] = True
R = np.zeros(len(V2)); R[:nb] = Hr[:nb] - Hs[:nb]
R = lap(R, fixed, 900, 0.9)
Hb = Hs + R
dedge = np.concatenate([np.zeros(nb), dist_poly(PX[nb:], PS[nb:])])
beta = np.clip(dedge / 3.0, 0, 1); beta = beta * beta * (3 - 2 * beta)
Hb = Hr * (1 - beta) + Hb * beta

# --- the relief (mm along the normal; + outwards) and the regions ---------------------------------------
def G(x, c, w):
    return np.exp(-((x - c) / w) ** 2)


def win(x, a, b, soft):
    t1 = np.clip((x - (a - soft)) / soft, 0, 1); t2 = np.clip(((b + soft) - x) / soft, 0, 1)
    return (t1 * t1 * (3 - 2 * t1)) * (t2 * t2 * (3 - 2 * t2))


def sig(x):
    return 1.0 / (1.0 + np.exp(-x))


def shape(X, S):
    """relief h (mm) and the region fields (< 0 inside) at chart points."""
    ax = np.abs(X); side = np.where(X >= 0, 1.0, -1.0)
    # the labia minora outline an almond from the fourchette to the clitoris
    t = np.clip((S - S_FOUR) / (S_GLANS - S_FOUR), 0, 1)
    c_min = 1.0 + 3.3 * np.sin(np.pi * t) ** 0.7 + 0.18 * np.sin(S / 3.7 + 1.7 * side)
    vest = -3.4 * sig((c_min - 0.65 - ax) / 0.45) * win(S, S_FOUR + 0.5, S_GLANS - 1.5, 2.5)
    # their free edges ruffled, a little different on each side
    wav = 0.55 * np.sin(S / 2.2 + 1.3 * side) + 0.35 * np.sin(S / 1.15 + 2.1 * side) + 0.2 * np.sin(S / 0.7 + 0.4 * side)
    min_w = win(S, S_FOUR + 1.0, S_GLANS + 1.0, 3)
    minora = (2.3 + 0.7 * wav) * G(ax, c_min, 0.9) * min_w - 0.4 * G(ax, c_min + 1.4, 0.6) * min_w
    # clitoris: the hood over the glans, the glans peeking out below its edge, the frenula
    hood_f = 2.3 * G(S, S_GLANS + 3.8, 4.2) * G(ax, 0, 2.6) * sig((S - (S_GLANS + 0.9)) / 0.5)
    r_gl = np.hypot(X / 1.7, (S - S_GLANS) / 2.0)
    glans = 2.2 * np.exp(-r_gl ** 2 * 1.4)
    fren = 0.7 * G(ax, 1.6, 0.6) * G(S, S_GLANS - 2.4, 1.6)
    # the urethral orifice: a small slit with soft lips
    r_ure = np.hypot(X / 0.9, (S - S_URE) / 1.4)
    urethra = -1.8 * np.exp(-r_ure ** 2) + 0.55 * G(r_ure, 1.5, 0.5)
    # the introitus, down to the vagina, with a hymenal fringe
    r_in = np.hypot(X / 3.0, (S - S_INTRO) / 5.4)
    th_in = np.arctan2(S - S_INTRO, X)
    introitus = -depth_in * np.exp(-(r_in / 0.78) ** 4)
    hymen = 0.45 * G(r_in, 0.98, 0.12) * (1 + 0.6 * np.sin(5 * th_in + 0.7))
    # fossa navicularis, perineal raphe, the cleft up to the anterior commissure
    fossa = -0.35 * G(S, S_FOUR + 3.2, 1.8) * G(ax, 0, 2.6)
    raphe = 0.35 * G(ax, 0, 0.7) * win(S, S_LO + 4, S_FOUR - 4, 3)
    ant = -1.4 * G(ax, 0, 1.1) * win(S, S_GLANS + 6.5, S_ANT + 1, 2)
    h = vest + minora + hood_f + glans + fren + urethra + introitus + hymen + fossa + raphe + ant
    # the relief stays inside the cleft, clear of the patch border
    sw = win(S, S_LO + 4, S_HI - 4, 3)
    fade = np.clip((6.0 - ax) / 1.6, 0, 1) * sw
    fade = fade * fade * (3 - 2 * fade)
    fade = np.where(ax < 2.0, np.maximum(fade, sw), fade)
    inside = (S > S_FOUR + 0.5) & (S < S_GLANS + 1.5)
    fields = {
        'vest': np.where(inside & (S < S_GLANS - 1.0), ax - (c_min - 0.55), 1.0),
        'minus': np.where(inside, ax - (c_min + 1.0), 1.0),
        'hood': np.where((S >= S_GLANS - 1.0) & (S < S_GLANS + 9.0) & (ax < 3.2), 0.5 - hood_f, 1.0),
        'glans': r_gl - 0.95, 'ure': r_ure - 1.25, 'vag': r_in - 0.80,
    }
    return h * fade, fields


depth_in = max(4.0, -H_VAG - 4.4 + 1.0)
X, S = PX.copy(), PS.copy()
# region borders: vertices between inside and outside move onto the field's zero line
# (a Newton step in the chart, at most half a grid cell), so the borders are smooth curves
tri_of = [[] for _ in range(len(V2))]
for f_i, t in enumerate(F2):
    for v in t:
        tri_of[v].append(f_i)
for key in ('vest', 'minus', 'glans', 'ure', 'vag'):
    cen_x, cen_s = X[F2].mean(1), S[F2].mean(1)
    fv = shape(cen_x, cen_s)[1][key]
    neg = fv < 0
    cand = np.array([v for v in range(nb, len(V2)) if tri_of[v] and neg[tri_of[v]].any() and (~neg[tri_of[v]]).any()], dtype=int)
    if not len(cand):
        continue
    for _ in range(3):
        e_ = 0.02
        f0 = shape(X[cand], S[cand])[1][key]
        gx_ = (shape(X[cand] + e_, S[cand])[1][key] - shape(X[cand] - e_, S[cand])[1][key]) / (2 * e_)
        gs_ = (shape(X[cand], S[cand] + e_)[1][key] - shape(X[cand], S[cand] - e_)[1][key]) / (2 * e_)
        g2 = gx_ ** 2 + gs_ ** 2 + 1e-9
        dX_ = -f0 * gx_ / g2; dS_ = -f0 * gs_ / g2
        n_ = np.hypot(dX_, dS_); k_ = np.minimum(1.0, 0.35 * G_ / np.maximum(n_, 1e-9))
        X[cand] += dX_ * k_; S[cand] += dS_ * k_
h, _ = shape(X, S)
h = lap(h, fixed, 3, 0.4)
H = Hb + h
P = point(X, S, H)
BASE = point(X, S, Hb)
# the border keeps its own vertices exactly
P[:nb] = C[loop]; BASE[:nb] = C[loop]

# --- labels ---------------------------------------------------------------------------------------------
fc = lambda a: a[F2].mean(1)
fx, fsv = fc(X), fc(S); fa = np.abs(fx)
fside = np.where(fx >= 0, 'l', 'r')
_, FF = shape(fx, fsv)
# outside the vulva: the region of the old skin there
from mathutils.kdtree import KDTree
zone_ids = np.where(tz)[0]
kd = KDTree(len(zone_ids))
for j, f_i in enumerate(zone_ids):
    kd.insert(Vector(C[T[f_i]].mean(0)), j)
kd.balance()
cb = BASE[F2].mean(1)
labels = np.array([oldlab[zone_ids[kd.find(Vector(c))[1]]] for c in cb], dtype=object)
labels[fsv < S_FOUR - 5] = 'Perineum'
labels[fsv > S_ANT + 3] = 'Mons pubis'
lm = (fsv >= S_FOUR - 5) & (fsv <= S_ANT + 3) & (fa < 8.0)
labels[lm & (fside == 'l')] = 'Labium majus.l'; labels[lm & (fside == 'r')] = 'Labium majus.r'
mins = FF['minus'] < 0
labels[mins & (fside == 'l')] = 'Labium minus.l'; labels[mins & (fside == 'r')] = 'Labium minus.r'
labels[FF['vest'] < 0] = 'Vestibule of vagina'
labels[(FF['hood'] < 0)] = 'Prepuce of clitoris'
labels[FF['glans'] < 0] = 'Glans of clitoris'
labels[FF['ure'] < 0] = 'External urethral orifice'
labels[FF['vag'] < 0] = 'Vaginal orifice'
r_ure = np.hypot(X / 0.9, (S - S_URE) / 1.4); r_in = np.hypot(X / 3.0, (S - S_INTRO) / 5.4)

# --- assemble: old vertices keep their indices, the patch's inner vertices are appended ----------------------
n_old = len(C)
idx_map = np.concatenate([loop, n_old + np.arange(len(V2) - nb)])
CO = np.vstack([C, P[nb:]])
BS = np.vstack([C, BASE[nb:]])
newT = idx_map[F2]
# winding as the old zone triangles
old_t = T[tz][0]
fn_old = np.cross(C[old_t[1]] - C[old_t[0]], C[old_t[2]] - C[old_t[0]])
_, N0 = frame(np.array([VS[old_t].mean()]))
fn_new = np.cross(CO[newT[:, 1]] - CO[newT[:, 0]], CO[newT[:, 2]] - CO[newT[:, 0]])
_, Nn = frame(fc(S))
if (np.sign((fn_new * Nn).sum(1)) != np.sign((fn_old * N0[0]).sum())).mean() > 0.5:
    newT = newT[:, ::-1].copy()
flipped = ((np.cross(CO[newT[:, 1]] - CO[newT[:, 0]], CO[newT[:, 2]] - CO[newT[:, 0]]) * Nn).sum(1) < 0).sum()
print('patch triangles facing inwards (folds):', int(flipped), flush=True)
keepT = ~tz & ~touched
allT = np.vstack([T[keepT], np.array(outT, dtype=T.dtype).reshape(-1, 3), newT])
alllab = np.concatenate([oldlab[keepT], np.array(outL, dtype=object), labels])
ure = point(np.array([0.0]), np.array([S_URE]), np.array([Hb[np.argmin(r_ure)] + h[np.argmin(r_ure)]]))[0]
vag = point(np.array([0.0]), np.array([S_INTRO]), np.array([Hb[np.argmin(r_in)] + h[np.argmin(r_in)]]))[0]
print('orifices urethra', ure.round(4), 'vagina', vag.round(4), flush=True)
np.savez(out_path, co=CO, idx=allT, labels=alllab, urethra=ure, vagina=vag, base=BS)
from collections import Counter
print('labels', Counter(labels.tolist()).most_common(), flush=True)
