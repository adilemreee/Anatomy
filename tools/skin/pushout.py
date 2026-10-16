"""Keeps bones and joints under the skin.

Where a bone (or a joint's capsule or ligament) reaches within `margin` of
the skin or through it (the coccyx in the gluteal cleft, the tips of the toes),
the skin rises over it: the needed lift at the nearest skin vertices is spread
smoothly over the surrounding skin and applied along the vertex normals.
"""
import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree


def vertex_normals(co, tris):
    n = np.zeros_like(co)
    fn = np.cross(co[tris[:, 1]] - co[tris[:, 0]], co[tris[:, 2]] - co[tris[:, 0]])
    for k in range(3):
        np.add.at(n, tris[:, k], fn)
    return n / np.linalg.norm(n, axis=1, keepdims=True).clip(1e-12)


DIRS = np.array([[0.0, 1.0, 0.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])


def crossings(tree, p, d, reach=2.0):
    """number of skin surfaces a ray from p crosses (odd: p is inside the body)."""
    n = 0; o = Vector(p); dv = Vector(d); left = reach
    while left > 0:
        hit = tree.ray_cast(o, dv, left)
        if hit[0] is None:
            break
        n += 1; left -= hit[3] + 1e-5; o = hit[0] + dv * 1e-5
        if n > 40:
            break
    return n


def push_out(C, T, points, margin=0.0025, spread=25, trusted=None, radius=None, normal_smooth=8, reach=None,
             direction=None):
    """`trusted` marks points under convex skin (the bridge of the nose) where
    the nearest surface is right and the ray count would mislead (the eye
    openings beside them). With `radius` (one value, or x, y, z) every vertex
    that has to rise lifts the skin around it in a smooth bump that wide (the
    root of the nose rises by several millimetres: a narrow lift would fold
    the skin there, a wide one would reach the eyelids), and
    `normal_smooth` evens the direction of the lift across a crease. Points
    more than `reach` out of the skin are left alone: they lie in a cavity of
    the skin mesh (the nostrils run up inside the nose), not under its surface.
    With `direction` the skin moves that way (forward over the root of the
    nose, where moving along the normals would close the crease between the
    nose and the forehead into a fold), as far as the clearance needs."""
    tree = BVHTree.FromPolygons([Vector(v) for v in C], [tuple(map(int, t)) for t in T])
    e = np.concatenate([T[:, [0, 1]], T[:, [1, 2]], T[:, [2, 0]]]); e = np.concatenate([e, e[:, ::-1]])
    deg = np.bincount(e[:, 0], minlength=len(C)).clip(1)
    # the normals of a smoothed copy: in a crease (between the eyes) the
    # mesh's own normals scatter and the lifted skin would crumple
    S = C.copy()
    for _ in range(normal_smooth):
        acc = np.zeros_like(S); np.add.at(acc, e[:, 0], S[e[:, 1]])
        S = 0.5 * S + 0.5 * acc / deg[:, None]
    N = vertex_normals(S, T)
    req = np.zeros(len(C))
    false_alarm = 0
    for k, b in enumerate(points):
        loc, nrm, fi, dist = tree.find_nearest(Vector(b))
        if loc is None or dist > 0.02:
            continue
        pen = float(np.dot(b - np.array(loc), np.array(nrm))) + margin
        if reach is not None and pen > margin + reach:
            continue
        if pen > 0:
            # in a crease (thumb against the palm, between the toes) the nearest
            # surface can face the point from the wrong side: a point inside the
            # body by the ray count is left alone
            if pen > margin + 0.0005 and not (trusted is not None and trusted[k]):
                inside = sum(crossings(tree, b, d) % 2 for d in DIRS[:3]) >= 2
                if inside:
                    false_alarm += 1
                    continue
            for v in T[fi]:
                req[v] = max(req[v], pen)
    if false_alarm:
        print(f'  push-out: {false_alarm} bone points inside by the ray count (nearest surface misleading)', flush=True)
    if direction is not None:
        # the skin moves forward (along the normals the crease between the
        # nose and the forehead would fold), by what each vertex needs along
        # its normal over how much it faces forward; then one smooth field
        u = np.asarray(direction, float) / np.linalg.norm(direction)
        need = req / np.clip(N @ u, 0.35, None)
    else:
        need = req
    d = need.copy()
    if radius:
        # the envelope of smooth bumps, one per vertex that has to rise
        from mathutils.kdtree import KDTree
        kd = KDTree(len(C))
        for i, v in enumerate(C):
            kd.insert(Vector(v), i)
        kd.balance()
        r = np.broadcast_to(np.asarray(radius, float), (3,))
        for j in np.nonzero(need)[0]:
            for co, i, _ in kd.find_range(Vector(C[j]), float(r.max())):
                t2 = float((((np.array(co) - C[j]) / r) ** 2).sum())
                if t2 < 1:
                    d[i] = max(d[i], need[j] * (1 - t2) ** 2)
    else:
        for _ in range(spread):
            acc = np.zeros(len(C)); np.add.at(acc, e[:, 0], d[e[:, 1]])
            d = np.maximum(need, 0.5 * d + 0.5 * acc / deg)
    if direction is not None:
        disp = u * d[:, None]
    else:
        # the lift itself smoothed (it is set per bone point), never below
        # what each vertex needs
        disp = N * d[:, None]
        for _ in range(spread):
            acc = np.zeros_like(disp); np.add.at(acc, e[:, 0], disp[e[:, 1]])
            disp = 0.5 * disp + 0.5 * acc / deg[:, None]
            along = (disp * N).sum(1)
            low = along < req
            disp[low] += N[low] * (req[low] - along[low])[:, None]
    print(f'  push-out: {int((req > 0).sum())} vertices over bone, max lift {req.max() * 1000:.1f} mm', flush=True)
    return C + disp
