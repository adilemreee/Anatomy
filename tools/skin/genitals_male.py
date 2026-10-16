"""Male external genitalia for the skin layer, built on the internal anatomy.

Penis: a smooth tube whose centre line and girth follow the corpora
(cavernosum, spongiosum) and the glans of the visceral pack, slice by slice,
with 2.5 mm of skin around them. The glans (circumcised) has a rounded,
slightly conical tip, a corona standing out most on the dorsal side, the
coronal sulcus behind it, a frenular notch on the ventral side and the
vertical slit of the external urethral orifice. The root runs 1.5 cm into the
body so it meets the pubic skin without a seam.

Scrotum: the scrotal sac of the visceral pack, smoothed and given a median
raphe; it hangs behind the penis around the testes.

    co, tris, glans_mask = penis(visceral_parts)
    co, tris = scrotum(visceral_parts)
    tree = crotch_tree(body_co, body_tris)
    co = attach(co, tris, tree)          # the sac hung from the body skin
    co = sink_root(co, tris, tree)       # the root of the penis in the body
    co = fillet(co, tris, body_bvh)      # and widening into the pubic skin
"""
import numpy as np


def _part(parts, name):
    return next(p for p in parts if p['info']['name'] == name)


def _smooth1d(a, it=3):
    a = a.copy()
    for _ in range(it):
        a[1:-1] = 0.25 * a[:-2] + 0.5 * a[1:-1] + 0.25 * a[2:]
    return a


def penis(parts):
    cc = _part(parts, 'Corpus cavernosum of penis')['co']
    cs = _part(parts, 'Corpus spongiosum of penis')['co']
    gl = _part(parts, 'Glans penis')['co']
    body = np.concatenate([cc, cs, gl])
    # the free part only (the crura and the bulb run back into the perineum)
    body = body[(body[:, 2] > 0.06) | (body[:, 1] < 0.79)]
    ys = np.arange(gl[:, 1].min() + 0.002, 0.835, 0.002)[::-1]      # from the root down
    cen, hx, hz = [], [], []
    for y in ys:
        s = body[np.abs(body[:, 1] - y) < 0.002]
        if len(s) < 8:
            continue
        cen.append([0.0, y, (s[:, 2].min() + s[:, 2].max()) / 2])
        hx.append(np.abs(s[:, 0]).max()); hz.append((s[:, 2].max() - s[:, 2].min()) / 2)
    cen = np.array(cen); hx = np.array(hx); hz = np.array(hz)
    cen[:, 2] = _smooth1d(cen[:, 2], 20)
    hx = _smooth1d(hx, 4); hz = _smooth1d(hz, 4)
    skin = 0.0025
    # root: extend 1.5 cm up and back into the body
    d0 = cen[0] - cen[3]; d0 /= np.linalg.norm(d0)
    root = [cen[0] + d0 * t for t in (0.03, 0.022, 0.015, 0.008)]
    tip_y = gl[:, 1].min()
    glans_top = gl[:, 1].max()
    # resample the centre line evenly
    tip = cen[-1].copy(); tip[1] = gl[:, 1].min() - 0.0012
    path = np.vstack([root, cen, tip])
    seg = np.linalg.norm(np.diff(path, axis=0), axis=1)
    sarc = np.r_[0, np.cumsum(seg)]
    L = sarc[-1]
    n = 180
    t = np.linspace(0, L, n)
    P = np.stack([np.interp(t, sarc, path[:, k]) for k in range(3)], 1)
    # girth: an even shaft around the corpora; the glans an elongated dome
    # (circumcised) with the corona standing out a little and the coronal
    # sulcus just behind it
    yy = P[:, 1]
    tip_y = tip_y - 0.0012
    corona_y = glans_top - 0.006
    shaft_x = max(np.percentile(hx, 80) + skin, 0.0145)
    shaft_z = max(np.percentile(hz, 80) + skin, 0.0130)
    gx = max(np.abs(gl[:, 0]).max() + 0.0010, shaft_x * 1.03)
    shaft_x = max(shaft_x, gx / 1.04)
    gz = shaft_z * 1.06
    u = np.clip((corona_y - yy) / (corona_y - tip_y), 0, 1)          # 0 at the corona, 1 at the tip
    # an acorn: full near the corona, narrowing to a rounded point
    dome = np.sqrt(np.clip(1 - u ** 2.2, 0, 1)) * (1 - 0.3 * u ** 1.5)
    on_glans = yy < corona_y
    sul = np.exp(-((yy - (corona_y + 0.0035)) / 0.0022) ** 2)
    hxs = np.where(on_glans, gx * dome, shaft_x * (1 - 0.06 * sul))
    hzs = np.where(on_glans, gz * dome, shaft_z * (1 - 0.06 * sul))
    # the corona's rim: a soft step from the sulcus up to the glans
    rim = np.exp(-((yy - corona_y) / 0.0012) ** 2)
    hxs = hxs + 0.0006 * rim; hzs = hzs + 0.0008 * rim
    # the root widens into the body
    root_w = np.clip((yy - (P[3, 1])) / 0.015, 0, 1)
    hxs = hxs * (1 + 0.25 * root_w); hzs = hzs * (1 + 0.25 * root_w)
    prof = np.ones(n)
    # tangent frames: lateral = x, dorsal = anterior
    T = np.gradient(P, axis=0); T /= np.linalg.norm(T, axis=1, keepdims=True)
    X = np.array([1.0, 0, 0])
    D = np.cross(T, X); D *= np.sign(D[:, 2:3] + 1e-9)
    ring = 64
    ang = np.linspace(0, 2 * np.pi, ring, endpoint=False)
    co = []
    for i in range(n):
        for a in ang:
            ca, sa = np.cos(a), np.sin(a)       # sa > 0: dorsal (front)
            rx = hxs[i] * prof[i]
            rz = hzs[i] * prof[i]
            # the corona stands out more dorsally; frenular notch ventrally
            if yy[i] < corona_y + 0.004:
                rz *= 1 + 0.06 * max(sa, 0) * np.exp(-((yy[i] - corona_y) / 0.003) ** 2)
                notch = np.exp(-(ca / 0.25) ** 2) * (sa < 0) * np.exp(-((yy[i] - (corona_y - 0.007)) / 0.007) ** 2)
                rz *= 1 - 0.14 * notch
            co.append(P[i] + X * rx * ca + D[i] * rz * sa)
    co = np.array(co)
    # apex and the meatus: a short vertical slit at the tip, on the ventral side of the apex
    apex = P[-1] + T[-1] * 0.0015
    tris = []
    for i in range(n - 1):
        for j in range(ring):
            a_, b_ = i * ring + j, i * ring + (j + 1) % ring
            c_, d_ = a_ + ring, b_ + ring
            tris += [(a_, c_, d_), (a_, d_, b_)]
    k = len(co)
    co = np.vstack([co, apex, P[0] - T[0] * 0.002])
    last = (n - 1) * ring
    tris += [(k, last + (j + 1) % ring, last + j) for j in range(ring)]
    tris += [(k + 1, j, (j + 1) % ring) for j in range(ring)]
    tris = np.array(tris)
    # meatus: pull in the vertices near the apex along a vertical slit
    rel = co - apex
    slit = np.exp(-(rel[:, 0] / 0.0007) ** 2) * np.exp(-(np.dot(rel, D[-1]) + 0.0015) ** 2 / 0.0028 ** 2) \
        * np.exp(-(np.linalg.norm(rel, axis=1) / 0.0045) ** 2)
    inward = co - P[-8]
    inward /= np.linalg.norm(inward, axis=1, keepdims=True).clip(1e-9)
    co = co - inward * (0.0016 * slit)[:, None]
    # orientation: outward
    fn = np.cross(co[tris[:, 1]] - co[tris[:, 0]], co[tris[:, 2]] - co[tris[:, 0]])
    cen_t = co[tris].mean(1)
    near = np.array([P[np.argmin(np.linalg.norm(P - c, axis=1))] for c in cen_t])
    if (fn * (cen_t - near)).sum() < 0:
        tris = tris[:, ::-1].copy()
    glans = co[tris].mean(1)[:, 1] < corona_y + 0.0012
    return co, tris, glans


def crotch_tree(body_co, body_tris, penis=None):
    """BVH of the body skin the genitals join: the pubic skin, the root of
    the penis and the perineum, without the inner thighs beside them; with
    `penis` (co, tris) the underside of its root too (the scrotal skin
    continues onto it)."""
    from mathutils import Vector
    from mathutils.bvhtree import BVHTree
    c = body_co[body_tris].mean(1)
    fn = np.cross(body_co[body_tris[:, 1]] - body_co[body_tris[:, 0]], body_co[body_tris[:, 2]] - body_co[body_tris[:, 0]])
    fn /= np.linalg.norm(fn, axis=1, keepdims=True).clip(1e-12)
    keep = (np.abs(c[:, 0]) < 0.05) & (c[:, 1] > 0.70) & (c[:, 1] < 0.90) & (np.abs(fn[:, 0]) < 0.6)
    t = body_tris[keep]
    used = np.unique(t)
    remap = np.full(len(body_co), -1); remap[used] = np.arange(len(used))
    verts = [Vector(v) for v in body_co[used]]
    faces = [tuple(map(int, f)) for f in remap[t]]
    if penis is not None:
        pco, ptris = penis
        # the root half of the shaft, its underside (facing down or back)
        pc = pco[ptris].mean(1)
        pn = np.cross(pco[ptris[:, 1]] - pco[ptris[:, 0]], pco[ptris[:, 2]] - pco[ptris[:, 0]])
        pn /= np.linalg.norm(pn, axis=1, keepdims=True).clip(1e-12)
        top = pco[:, 1].max()
        sel = (pc[:, 1] > top - 0.045) & ((pn[:, 1] < -0.2) | (pn[:, 2] < -0.2))
        base = len(verts)
        verts += [Vector(v) for v in pco]
        faces += [tuple(int(i) + base for i in f) for f in ptris[sel]]
    return BVHTree.FromPolygons(verts, faces)


def _smooth_moves(move, tris, it):
    e = np.concatenate([tris[:, [0, 1]], tris[:, [1, 2]], tris[:, [2, 0]]]); e = np.concatenate([e, e[:, ::-1]])
    deg = np.bincount(e[:, 0], minlength=len(move)).clip(1)
    for _ in range(it):
        acc = np.zeros_like(move); np.add.at(acc, e[:, 0], move[e[:, 1]])
        move = 0.5 * move + 0.5 * acc / deg[:, None]
    return move


def attach(co, tris, tree, depth=0.004, smooth=12, taper=0.45):
    """Hangs the sac from the body: it narrows towards its neck (by `taper`
    at the top, from a third of its height up: no square shoulders beside
    the penis), and its upper half converges into the skin of the crotch
    (`crotch_tree`), the top ring `depth` under it, fading out towards the
    middle of the sac, so no rim of the sac shows against the perineum or
    the thighs."""
    from mathutils import Vector
    y0, y1 = co[:, 1].min(), co[:, 1].max()
    h = (co[:, 1] - y0) / (y1 - y0)
    narrow = np.clip((h - 0.3) / 0.7, 0, 1); narrow = narrow * narrow * (3 - 2 * narrow)
    cx = np.median(co[:, 0])
    co = co.copy()
    co[:, 0] = cx + (co[:, 0] - cx) * (1 - taper * narrow)
    w = np.clip((h - 0.45) / 0.55, 0, 1); w = w * w * (3 - 2 * w)
    move = np.zeros_like(co)
    for i, v in enumerate(co):
        if w[i] <= 0:
            continue
        loc, nrm, _, _ = tree.find_nearest(Vector(v))
        if loc is None:
            continue
        target = np.array(loc) - np.array(nrm) * depth
        move[i] = (target - v) * w[i]
    return co + _smooth_moves(move, tris, smooth)


def sink_root(co, tris, tree, ring=64, depth=0.003, smooth=6):
    """Sinks the root of the penis into the body ring by ring: every ring of
    the tube that is partly outside the crotch skin, or less than `depth`
    under it, while the rings above it are inside, moves into the body as a
    whole (the tube bends in; a per-vertex move would pinch it), the moves
    eased along the tube."""
    from mathutils import Vector
    n = (len(co) - 2) // ring
    need = np.zeros(n); dirn = np.zeros((n, 3))
    for i in range(n):
        r = co[i * ring:(i + 1) * ring]
        worst, nsum = -1.0, np.zeros(3)
        for v in r:
            loc, nrm, _, _ = tree.find_nearest(Vector(v))
            if loc is None:
                continue
            nn = np.array(nrm)
            worst = max(worst, float(np.dot(v - np.array(loc), nn)) + depth)
            nsum += nn
        need[i] = max(worst, 0.0)
        dirn[i] = nsum / max(np.linalg.norm(nsum), 1e-9)
    # only the root: from the upper end down to the first ring that is
    # entirely outside (the free shaft keeps its place)
    free = np.nonzero(need > 0.012)[0]
    last = free[0] if len(free) else n
    w = np.zeros(n); w[:last] = 1.0
    for _ in range(smooth):
        w[1:-1] = 0.25 * w[:-2] + 0.5 * w[1:-1] + 0.25 * w[2:]
    shift = dirn * (need * w)[:, None]
    for _ in range(smooth):
        shift[1:-1] = 0.25 * shift[:-2] + 0.5 * shift[1:-1] + 0.25 * shift[2:]
    out = co.copy()
    for i in range(n):
        out[i * ring:(i + 1) * ring] -= shift[i]
    out[-1] -= shift[0]          # the cap at the root
    return out


def fillet(co, tris, body_tree, reach=0.016, smooth=6):
    """Blends the penis into the body: the tube's surface near the pubic skin
    (closer than `reach`, outside it) is drawn towards the skin, most where
    it is closest, so the two meet in a soft concave curve instead of a
    sharp edge."""
    from mathutils import Vector
    move = np.zeros_like(co)
    for k, v in enumerate(co):
        loc, nrm, _, _ = body_tree.find_nearest(Vector(v))
        if loc is None:
            continue
        n = np.array(nrm)
        h = float(np.dot(v - np.array(loc), n))
        if h <= 0 or h >= reach:
            continue
        t = 1 - h / reach
        move[k] = -n * h * t * t
    return co + _smooth_moves(move, tris, smooth)


def scrotum(parts, smooth=20):
    sc = _part(parts, 'Scrotum')
    co, tris = sc['co'].copy(), sc['idx']
    e = np.concatenate([tris[:, [0, 1]], tris[:, [1, 2]], tris[:, [2, 0]]]); e = np.concatenate([e, e[:, ::-1]])
    deg = np.bincount(e[:, 0], minlength=len(co)).clip(1)
    for _ in range(smooth):
        acc = np.zeros_like(co); np.add.at(acc, e[:, 0], co[e[:, 1]])
        avg = acc / deg[:, None]
        co = co + (avg - co) * 0.5
        # Taubin step keeps the volume
        acc = np.zeros_like(co); np.add.at(acc, e[:, 0], co[e[:, 1]])
        co = co - (acc / deg[:, None] - co) * 0.53
    n = np.zeros_like(co)
    fn = np.cross(co[tris[:, 1]] - co[tris[:, 0]], co[tris[:, 2]] - co[tris[:, 0]])
    for k in range(3):
        np.add.at(n, tris[:, k], fn)
    n /= np.linalg.norm(n, axis=1, keepdims=True).clip(1e-12)
    co = co + n * 0.0015
    # median raphe: a shallow groove along the midline
    w = np.exp(-(co[:, 0] / 0.0025) ** 2)
    co = co - n * (0.0012 * w)[:, None]
    return co, tris
