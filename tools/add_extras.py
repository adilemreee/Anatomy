"""Adds the structures that Z-Anatomy, BodyParts3D and tools/add_female.py lack.

    Blender -b --python tools/add_extras.py -- <hra_dir> <in_dir> <out_dir>

<in_dir> holds the packs after tools/add_female.py (any of ANT1/2/3). The
cardiovascular, regions, muscular and skeletal packs may come from the app:
parts an earlier run added are dropped. <out_dir> receives "ANT1"
visceral, lymphoid, cardiovascular, regions and nervous packs; run bake_ao
and build_lods on them afterwards.

Cut from existing organs along a plane (exact geometry, capped):
    Caecum (below the ileocaecal junction), Anal canal (below the
    anorectal junction).
From the Human Reference Atlas (Visible Human Female, CC BY 4.0,
https://humanatlas.io), <hra_dir>/mammary-gland-female-left.glb:
    lobes, lactiferous ducts, nipple, areola and fat body of the breast,
    conformed onto the chest wall; the right breast mirrors the left.
Modelled from the surrounding anatomy:
    vagina and female urethra (between the female bladder and cervix from
    tools/add_female.py and the rectum); cisterna chyli,
    thoracic duct, right lymphatic duct, pharyngeal and lingual tonsils;
    fibrous pericardium; phrenic nerves; scrotum.
Penile and testicular vessels are marked "sex": "m".
Wrapping sheets (pericardium, scrotum, breast fat) get "covering": true:
the app hides them by default and bake_ao lets light through them.
"""
import json
import math
import os
import struct
import sys
import zlib

import bmesh
import bpy
import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

ARGS = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
HRA, IN_DIR, OUT_DIR = (ARGS + [None] * 3)[:3]
MODELLED = "Anatomi Atlası, modelled on the surrounding anatomy"
HRA_SOURCE = "Human Reference Atlas (HuBMAP), CC BY 4.0"
FEMALE = ["Visceral systems", "Genital systems", "Female genital system"]
MALE = ["Visceral systems", "Genital systems", "Male genital system"]


# MARK: - Packs

class Pack:
    def __init__(self, system):
        self.system = system
        raw = zlib.decompress(open(os.path.join(IN_DIR, f"mesh-{system}.bin"), "rb").read(), -15)
        self.manifest = json.load(open(os.path.join(IN_DIR, f"mesh-{system}.json")))
        has_ao = raw[3:4] in (b"2", b"3")
        count, = struct.unpack_from("<I", raw, 4)
        self.lo = np.array(struct.unpack_from("<3f", raw, 8))
        self.hi = np.array(struct.unpack_from("<3f", raw, 20))
        sizes = [struct.unpack_from("<II", raw, 32 + 8 * i) for i in range(count)]
        cur = 32 + 8 * count
        self.parts = []
        for (nv, ni), info in zip(sizes, self.manifest["parts"]):
            co = np.frombuffer(raw, "<u2", nv * 3, cur).reshape(-1, 3).astype(np.float64) / 65535 * (self.hi - self.lo) + self.lo
            cur += nv * 6
            n = np.frombuffer(raw, "i1", nv * 3, cur).reshape(-1, 3).astype(np.float64) / 127
            cur += nv * 3
            wide = nv > 65535
            idx = np.frombuffer(raw, "<u4" if wide else "<u2", ni, cur).astype(np.int64).reshape(-1, 3)
            cur += ni * (4 if wide else 2) + (nv if has_ao else 0)
            self.parts.append({"info": info, "co": co, "n": n, "idx": idx})
        # Parts from an earlier run of this stage (packs taken from the app).
        self.parts = [p for p in self.parts if not p["info"].get("extra")]

    def get(self, name):
        found = [p for p in self.parts if p["info"]["name"] == name]
        assert found, f"{self.system}: no part {name!r}"
        return found[0]

    def where(self, test):
        return [p for p in self.parts if test(p["info"])]

    def material(self, name):
        materials = self.manifest.setdefault("materials", [])
        if name not in materials:
            materials.append(name)
        return materials.index(name)

    def add(self, name, path, co, tris, material, base=None, side=None, sex=None, covering=False,
            source=MODELLED, normals=None, runs=None, uvs=None):
        co = np.clip(co, self.lo, self.hi)
        used = np.unique(tris)
        remap = np.full(len(co), -1)
        remap[used] = np.arange(len(used))
        co, tris = co[used], remap[tris]
        n = normals[used] if normals is not None else vertex_normals(co, tris)
        uv = uvs[used] if uvs is not None else None
        if base is None:
            base = name.rsplit(".", 1)[0] if name[-2:] in (".l", ".r") else name
        info = {"name": name, "base": base, "path": path, "tris": int(len(tris)),
                "bounds": [round(float(v), 4) for v in (*co.min(0), *co.max(0))],
                "seg": runs or [[self.material(material) if isinstance(material, str) else material, int(len(tris))]],
                "source": source, "extra": True}
        if side:
            info["side"] = side
        if sex:
            info["sex"] = sex
        if covering:
            info["covering"] = True
        part = {"info": info, "co": co, "n": n, "idx": tris, "uv": uv}
        self.parts.append(part)
        print(f"  + {self.system:<14} {name:<36} {len(tris):>6} tris", flush=True)
        return part

    def write(self):
        lo, hi = self.lo, self.hi
        blob = bytearray(b"ANT1" + struct.pack("<I", len(self.parts)) + struct.pack("<3f", *lo) + struct.pack("<3f", *hi))
        for p in self.parts:
            blob += struct.pack("<II", len(p["co"]), p["idx"].size)
        for p in self.parts:
            blob += np.clip(np.round((p["co"] - lo) / (hi - lo) * 65535), 0, 65535).astype("<u2").tobytes()
            blob += np.clip(np.round(p["n"] * 127), -127, 127).astype("i1").tobytes()
            blob += p["idx"].astype("<u2" if len(p["co"]) <= 65535 else "<u4").tobytes()
        comp = zlib.compressobj(9, zlib.DEFLATED, -15)
        open(os.path.join(OUT_DIR, f"mesh-{self.system}.bin"), "wb").write(comp.compress(bytes(blob)) + comp.flush())
        # Texture coordinates (textured skin) go into a side file, in the same
        # vertex order: "UVS1", u32 parts, per part u32 count (0 = none) and
        # that many u16 (u, v) pairs, v pointing down the image.
        uv_path = os.path.join(OUT_DIR, f"mesh-{self.system}.uv")
        if any(p.get("uv") is not None for p in self.parts):
            uvb = bytearray(b"UVS1" + struct.pack("<I", len(self.parts)))
            for p in self.parts:
                uv = p.get("uv")
                if uv is None:
                    uvb += struct.pack("<I", 0)
                    continue
                assert len(uv) == len(p["co"])
                uvb += struct.pack("<I", len(uv))
                # NaN marks vertices drawn with their material colour.
                q = np.clip(np.round(np.nan_to_num(uv, nan=0.0) * 65535), 1, 65535)
                q[np.isnan(uv).any(1)] = 0
                uvb += q.astype("<u2").tobytes()
            comp = zlib.compressobj(9, zlib.DEFLATED, -15)
            open(uv_path, "wb").write(comp.compress(bytes(uvb)) + comp.flush())
        elif os.path.exists(uv_path):
            os.remove(uv_path)
        for p in self.parts:
            info = p["info"]
            info["tris"] = int(len(p["idx"]))
            # Parts cut in two keep their single material run.
            if sum(n for _, n in info["seg"]) != info["tris"]:
                assert len(info["seg"]) == 1, f"{info['name']}: material runs no longer match"
                info["seg"] = [[info["seg"][0][0], info["tris"]]]
            info["bounds"] = [round(float(v), 4) for v in (*p["co"].min(0), *p["co"].max(0))]
        self.manifest["parts"] = [p["info"] for p in self.parts]
        json.dump(self.manifest, open(os.path.join(OUT_DIR, f"mesh-{self.system}.json"), "w"),
                  ensure_ascii=False, separators=(",", ":"))
        print(f"{self.system}: {len(self.parts)} parts", flush=True)


def load_glb(path):
    data = open(path, "rb").read()
    off, js, binc = 12, None, None
    while off < len(data):
        clen, ctype = struct.unpack_from("<II", data, off); off += 8
        if ctype == 0x4E4F534A:
            js = json.loads(data[off:off + clen])
        elif ctype == 0x004E4942:
            binc = data[off:off + clen]
        off += clen

    def acc(i):
        a = js["accessors"][i]; bv = js["bufferViews"][a["bufferView"]]
        comp = {5126: np.float32, 5125: np.uint32, 5123: np.uint16, 5121: np.uint8}[a["componentType"]]
        n = {"SCALAR": 1, "VEC2": 2, "VEC3": 3, "VEC4": 4}[a["type"]]
        start = bv.get("byteOffset", 0) + a.get("byteOffset", 0)
        size = np.dtype(comp).itemsize * n
        stride = bv.get("byteStride", 0)
        if stride and stride != size:
            rows = np.frombuffer(binc, np.uint8, a["count"] * stride, start).reshape(a["count"], stride)[:, :size]
            return np.frombuffer(rows.tobytes(), comp).reshape(a["count"], n)
        return np.frombuffer(binc, comp, a["count"] * n, start).reshape(a["count"], n)

    out = {}
    for node in js["nodes"]:
        if "mesh" not in node:
            continue
        assert "matrix" not in node and "translation" not in node and "rotation" not in node, "node transforms not handled"
        cos, tris, base = [], [], 0
        for p in js["meshes"][node["mesh"]]["primitives"]:
            co = acc(p["attributes"]["POSITION"]).astype(np.float64)
            idx = acc(p["indices"]).reshape(-1, 3).astype(np.int64) if "indices" in p else np.arange(len(co)).reshape(-1, 3)
            cos.append(co); tris.append(idx + base); base += len(co)
        out[node["name"].replace("VH_F_", "")] = (np.concatenate(cos), np.concatenate(tris))
    return out


# MARK: - Mesh helpers

def merge(meshes):
    cos, tris, base = [], [], 0
    for co, t in meshes:
        cos.append(co); tris.append(t + base); base += len(co)
    return np.concatenate(cos), np.concatenate(tris)


def mesh(p):
    return p["co"], p["idx"]


def vertex_normals(co, tris):
    n = np.zeros_like(co)
    fn = np.cross(co[tris[:, 1]] - co[tris[:, 0]], co[tris[:, 2]] - co[tris[:, 0]])
    for k in range(3):
        np.add.at(n, tris[:, k], fn)
    ln = np.linalg.norm(n, axis=1, keepdims=True); ln[ln == 0] = 1
    return n / ln


def bvh(meshes):
    co, tris = merge(meshes)
    return BVHTree.FromPolygons([Vector(v) for v in co], [tuple(int(i) for i in t) for t in tris])


def neighbours(n, tris):
    """Vertex adjacency as (rows, cols) for scatter-averaging."""
    e = np.concatenate([tris[:, [0, 1]], tris[:, [1, 2]], tris[:, [2, 0]]])
    e = np.concatenate([e, e[:, ::-1]])
    return e[:, 0], e[:, 1], np.bincount(e[:, 0], minlength=n).clip(1)


def smooth_field(field, adjacency, iterations, keep=0.5):
    rows, cols, deg = adjacency
    for _ in range(iterations):
        acc = np.zeros_like(field)
        np.add.at(acc, rows, field[cols])
        field = keep * field + (1 - keep) * acc / deg[:, None]
    return field


def to_object(co, tris, name="tmp"):
    me = bpy.data.meshes.new(name)
    me.from_pydata(co.tolist(), [], tris.tolist())
    me.validate()
    ob = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(ob)
    return ob


def evaluate(ob):
    dg = bpy.context.evaluated_depsgraph_get()
    ev = ob.evaluated_get(dg)
    m = ev.to_mesh(); m.calc_loop_triangles()
    c = np.empty(len(m.vertices) * 3); m.vertices.foreach_get("co", c)
    t = np.empty(len(m.loop_triangles) * 3, dtype=np.int64); m.loop_triangles.foreach_get("vertices", t)
    ev.to_mesh_clear()
    me = ob.data
    bpy.data.objects.remove(ob); bpy.data.meshes.remove(me)
    return c.reshape(-1, 3), t.reshape(-1, 3)


def decimate(co, tris, target):
    ob = to_object(co, tris)
    weld = ob.modifiers.new("weld", "WELD"); weld.merge_threshold = 1e-6
    if len(tris) > target:
        dec = ob.modifiers.new("dec", "DECIMATE"); dec.ratio = target / len(tris)
    return evaluate(ob)


def remesh(co, tris, voxel, smooth=0, round_off=0):
    """Even voxel remesh; `smooth` shrinks a little, `round_off` rounds
    edges and corners while keeping the volume."""
    ob = to_object(co, tris)
    rm = ob.modifiers.new("remesh", "REMESH"); rm.mode = "VOXEL"; rm.voxel_size = voxel; rm.adaptivity = 0
    if smooth:
        sm = ob.modifiers.new("smooth", "SMOOTH"); sm.factor = 0.8; sm.iterations = smooth
    if round_off:
        ls = ob.modifiers.new("round", "LAPLACIANSMOOTH"); ls.lambda_factor = 1.0; ls.iterations = round_off
        ls.use_volume_preserve = True
    return evaluate(ob)


def convex_hull(points):
    bm = bmesh.new()
    for p in points:
        bm.verts.new(p)
    bmesh.ops.convex_hull(bm, input=bm.verts[:])
    bmesh.ops.triangulate(bm, faces=bm.faces[:])
    bm.verts.index_update()
    co = np.array([v.co[:] for v in bm.verts])
    tris = np.array([[v.index for v in f.verts] for f in bm.faces])
    bm.free()
    return co, tris


def inflate(co, tris, distance):
    return co + vertex_normals(co, tris) * distance


def spline(points, step):
    """Centripetal Catmull-Rom through `points`, resampled every `step` metres."""
    p = np.asarray(points, float)
    p = np.vstack([2 * p[0] - p[1], p, 2 * p[-1] - p[-2]])
    out = []
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        t0 = 0; t1 = t0 + np.linalg.norm(p1 - p0) ** 0.5; t2 = t1 + np.linalg.norm(p2 - p1) ** 0.5; t3 = t2 + np.linalg.norm(p3 - p2) ** 0.5
        for t in np.linspace(t1, t2, 24, endpoint=False):
            a1 = (t1 - t) / (t1 - t0) * p0 + (t - t0) / (t1 - t0) * p1
            a2 = (t2 - t) / (t2 - t1) * p1 + (t - t1) / (t2 - t1) * p2
            a3 = (t3 - t) / (t3 - t2) * p2 + (t - t2) / (t3 - t2) * p3
            b1 = (t2 - t) / (t2 - t0) * a1 + (t - t0) / (t2 - t0) * a2
            b2 = (t3 - t) / (t3 - t1) * a2 + (t - t1) / (t3 - t1) * a3
            out.append((t2 - t) / (t2 - t1) * b1 + (t - t1) / (t2 - t1) * b2)
    out.append(p[-2])
    return resample(np.array(out), step)


def resample(path, step):
    seg = np.linalg.norm(np.diff(path, axis=0), axis=1)
    s = np.concatenate([[0], np.cumsum(seg)])
    n = max(2, int(round(s[-1] / step)) + 1)
    t = np.linspace(0, s[-1], n)
    return np.stack([np.interp(t, s, path[:, k]) for k in range(3)], 1)


def bezier(p0, p1, p2, n):
    t = np.linspace(0, 1, n)[:, None]
    return (1 - t) ** 2 * np.asarray(p0) + 2 * (1 - t) * t * np.asarray(p1) + t ** 2 * np.asarray(p2)


def tube(path, rx, ry=None, sides=20, lateral=None, caps=(True, True)):
    """A closed tube along `path`. `rx`/`ry` are radii per path point; with
    `lateral` the rx axis follows that direction (else parallel transport)."""
    path = np.asarray(path, float)
    n = len(path)
    rx = np.broadcast_to(np.asarray(rx, float), (n,))
    ry = rx if ry is None else np.broadcast_to(np.asarray(ry, float), (n,))
    tan = np.gradient(path, axis=0)
    tan /= np.linalg.norm(tan, axis=1, keepdims=True)
    us = []
    if lateral is not None:
        for t in tan:
            u = np.asarray(lateral, float) - np.dot(lateral, t) * t
            us.append(u / np.linalg.norm(u))
    else:
        ref = np.array([1.0, 0, 0]) if abs(tan[0][0]) < 0.9 else np.array([0, 0, 1.0])
        u = ref - np.dot(ref, tan[0]) * tan[0]; u /= np.linalg.norm(u)
        for t in tan:
            u = u - np.dot(u, t) * t; u /= np.linalg.norm(u)
            us.append(u.copy())
    us = np.array(us)
    vs = np.cross(tan, us)
    ang = np.linspace(0, 2 * np.pi, sides, endpoint=False)
    rings = path[:, None, :] + rx[:, None, None] * np.cos(ang)[None, :, None] * us[:, None, :] \
        + ry[:, None, None] * np.sin(ang)[None, :, None] * vs[:, None, :]
    co = rings.reshape(-1, 3)
    tris = []
    for i in range(n - 1):
        for j in range(sides):
            a, b = i * sides + j, i * sides + (j + 1) % sides
            c, d = a + sides, b + sides
            tris += [(a, b, d), (a, d, c)]
    extra = []
    if caps[0]:
        extra.append(path[0] - tan[0] * min(rx[0], ry[0]) * 0.35)
        pole = len(co)
        tris += [(pole, (j + 1) % sides, j) for j in range(sides)]
    if caps[1]:
        extra.append(path[-1] + tan[-1] * min(rx[-1], ry[-1]) * 0.35)
        pole = len(co) + len(extra) - 1
        base = (n - 1) * sides
        tris += [(pole, base + j, base + (j + 1) % sides) for j in range(sides)]
    if extra:
        co = np.vstack([co, extra])
    co, tris = np.asarray(co), np.asarray(tris, dtype=np.int64)
    return orient(co, tris)


def orient(co, tris):
    """Flips a closed mesh whose triangles face inwards."""
    c = co.mean(0)
    fn = np.cross(co[tris[:, 1]] - co[tris[:, 0]], co[tris[:, 2]] - co[tris[:, 0]])
    if (fn * (co[tris].mean(1) - c)).sum() < 0:
        tris = tris[:, ::-1].copy()
    return co, tris


def outward(co, tris):
    """Consistent, outward-facing triangles for a closed mesh (order kept)."""
    bm = bmesh.new()
    verts = [bm.verts.new(v) for v in co]
    faces = [bm.faces.new([verts[i] for i in t]) for t in tris]
    bmesh.ops.recalc_face_normals(bm, faces=faces)
    bm.verts.index_update()
    out = np.array([[v.index for v in f.verts] for f in faces], dtype=np.int64)
    bm.free()
    return out


def loops(tris):
    """Ordered boundary loops of a triangle mesh."""
    from collections import defaultdict
    edges = defaultdict(int)
    for t in tris:
        for a, b in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0])):
            edges[(a, b)] += 1
    nxt = {}
    for (a, b) in edges:
        if (b, a) not in edges:
            nxt[a] = b
    out, seen = [], set()
    for s in nxt:
        if s in seen:
            continue
        loop, v = [], s
        while v not in seen and v in nxt:
            seen.add(v); loop.append(v); v = nxt[v]
        if len(loop) > 2:
            out.append(loop)
    return out


def split(p, plane_co, plane_no):
    """Cuts a part along a plane; returns (below, above) as capped meshes
    with normals."""
    plane_no = np.asarray(plane_no, float) / np.linalg.norm(plane_no)
    bm = bmesh.new()
    verts = [bm.verts.new(v) for v in p["co"]]
    for t in p["idx"]:
        try:
            bm.faces.new([verts[i] for i in t])
        except ValueError:
            pass
    bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=plane_co, plane_no=plane_no, dist=1e-7)
    bmesh.ops.triangulate(bm, faces=bm.faces[:])
    bm.verts.index_update()
    co = np.array([v.co[:] for v in bm.verts])
    tris = np.array([[v.index for v in f.verts] for f in bm.faces])
    bm.free()
    side = ((co[tris].mean(1) - plane_co) @ plane_no) < 0
    out = []
    for keep, outward in ((side, plane_no), (~side, -plane_no)):
        t = tris[keep]
        used = np.unique(t); remap = np.full(len(co), -1); remap[used] = np.arange(len(used))
        c, t = co[used], remap[t]
        n = vertex_normals(c, t)
        caps_co, caps_t = [], []
        k = len(c)
        for loop in loops(t):
            ring = c[loop]
            if np.abs((ring - plane_co) @ plane_no).max() > 1e-4:
                continue
            # A fan of its own vertices, so the wall keeps smooth normals.
            centre = ring.mean(0)
            m = len(ring)
            flip = np.dot(np.cross(ring - centre, np.roll(ring, -1, 0) - centre).sum(0), outward) < 0
            for j in range(m):
                a, b = k + j, k + (j + 1) % m
                caps_t.append((k + m, b, a) if flip else (k + m, a, b))
            caps_co.append(np.vstack([ring, centre]))
            k += m + 1
        if caps_co:
            capc = np.vstack(caps_co)
            n = np.vstack([n, np.tile(outward, (len(capc), 1))])
            c = np.vstack([c, capc])
            t = np.vstack([t, np.array(caps_t)])
        out.append((c, t, n))
    return out


def slice_centre(co, y, band=0.003):
    m = np.abs(co[:, 1] - y) < band
    if not m.any():
        return None, None
    s = co[m]
    c = s.mean(0)
    r = np.linalg.norm((s - c)[:, [0, 2]], axis=1).mean()
    return c, r


def push_out(path, tree, clearance, fixed=(), iterations=10):
    """Moves path points out of obstacles, then smooths, a few times."""
    path = path.copy()
    for it in range(iterations):
        for i, p in enumerate(path):
            if i in fixed:
                continue
            loc, nrm, _, dist = tree.find_nearest(Vector(p))
            if loc is None:
                continue
            q, nv = np.array(loc), np.array(nrm)
            inside = np.dot(p - q, nv) < 0
            if inside or dist < clearance:
                path[i] = q + nv * clearance
        if it < iterations - 1:
            sm = path.copy()
            sm[1:-1] = (path[:-2] + 2 * path[1:-1] + path[2:]) / 4
            for i in fixed:
                sm[i] = path[i]
            path = sm
    return path


def ray_grid(tree, xs, ys, origin, direction):
    """First hit along `direction` from origin(x, y) for every grid cell."""
    out = np.full((len(xs), len(ys)), np.nan)
    d = Vector(direction)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            loc, _, _, _ = tree.ray_cast(Vector(origin(x, y)), d)
            if loc is not None:
                out[i, j] = loc[:][list(np.abs(direction)).index(1)]
    return out


def sample(grid, xs, ys, x, y):
    i = np.clip(np.round((x - xs[0]) / (xs[1] - xs[0])).astype(int), 0, len(xs) - 1)
    j = np.clip(np.round((y - ys[0]) / (ys[1] - ys[0])).astype(int), 0, len(ys) - 1)
    inside = (x >= xs[0]) & (x <= xs[-1]) & (y >= ys[0]) & (y <= ys[-1])
    v = grid[i, j]
    v[~inside] = np.nan
    return v


def pad(tree, origin, axis, lateral, spread, size, thickness, relief, lift=0.0003):
    """A lens-shaped pad lying on the surface `tree` as seen from `origin`
    (inside a cavity): rays fan out around `axis`, the hit points form the
    base and the pad bulges back towards the origin."""
    axis = np.asarray(axis, float) / np.linalg.norm(axis)
    u = np.asarray(lateral, float); u = u - np.dot(u, axis) * axis; u /= np.linalg.norm(u)
    v = np.cross(axis, u)
    nu, nv = size
    au = np.linspace(-1, 1, nu); av = np.linspace(-1, 1, nv)
    base = np.zeros((nu, nv, 3)); dirs = np.zeros((nu, nv, 3)); ok = np.zeros((nu, nv), bool)
    for i, a in enumerate(au):
        for j, b in enumerate(av):
            # Square grid onto a disc, so the pad has a rounded outline.
            da, db = a * math.sqrt(1 - b * b / 2), b * math.sqrt(1 - a * a / 2)
            d = axis + math.tan(spread[0] * da) * u + math.tan(spread[1] * db) * v
            d /= np.linalg.norm(d)
            loc, _, _, _ = tree.ray_cast(Vector(origin), Vector(d), 0.08)
            if loc is not None:
                base[i, j] = np.array(loc) - d * lift; dirs[i, j] = d; ok[i, j] = True
    assert ok.all(), f"pad: {np.count_nonzero(~ok)} rays missed"
    # Round off the facets of coarse surfaces (the tongue).
    for _ in range(8):
        base[1:-1, 1:-1] = 0.5 * base[1:-1, 1:-1] + 0.125 * (base[:-2, 1:-1] + base[2:, 1:-1] + base[1:-1, :-2] + base[1:-1, 2:])
    A, B = np.meshgrid(au, av, indexing="ij")
    t = thickness * np.clip(1 - A ** 2, 0, 1) ** 0.6 * np.clip(1 - B ** 2, 0, 1) ** 0.6 * relief(A, B)
    top = base - dirs * t[..., None]
    co = np.vstack([top.reshape(-1, 3), base.reshape(-1, 3)])
    off = nu * nv
    top_t, base_t = [], []
    for i in range(nu - 1):
        for j in range(nv - 1):
            a, b, c, d = i * nv + j, (i + 1) * nv + j, (i + 1) * nv + j + 1, i * nv + j + 1
            top_t += [(a, b, c), (a, c, d)]
            base_t += [(off + a, off + c, off + b), (off + a, off + d, off + c)]
    top_t = np.array(top_t)
    # The top faces the origin.
    fn = np.cross(co[top_t[:, 1]] - co[top_t[:, 0]], co[top_t[:, 2]] - co[top_t[:, 0]])
    flip = (fn * -dirs.reshape(-1, 3)[top_t[:, 0]]).sum() < 0
    tris = np.vstack([top_t, np.array(base_t)])
    if flip:
        tris = tris[:, ::-1].copy()
    # Weld the rim (zero thickness) so the pad is closed.
    rim = np.zeros((nu, nv), bool); rim[0, :] = rim[-1, :] = rim[:, 0] = rim[:, -1] = True
    remap = np.arange(len(co))
    remap[off:][rim.reshape(-1)] = np.arange(off)[rim.reshape(-1)]
    return co, remap[tris]


# MARK: - Digestive

def digestive(vis):
    colon = vis.get("Ascending colon")
    ileum = vis.get("Ileum")["co"]
    # The ileocaecal junction: where the ileum touches the colon.
    tree = bvh([mesh(colon)])
    near = ileum[np.array([tree.find_nearest(Vector(v))[3] for v in ileum]) < 0.0015]
    junction = near[:, 1].mean() - 0.004
    (lo, lt, ln), (hi_, ht, hn) = split(colon, np.array([0, junction, 0]), [0, 1, 0])
    colon["co"], colon["idx"], colon["n"] = hi_, ht, hn
    info = colon["info"]
    vis.add("Caecum", info["path"][:-1], lo, lt, info["seg"][0][0], normals=ln, source=info.get("source", "Z-Anatomy"))
    print(f"  caecum below y {junction:.3f}", flush=True)

    rectum = vis.get("Rectum")
    co = rectum["co"]
    c_low, _ = slice_centre(co, 0.792)
    c_high, _ = slice_centre(co, 0.822)
    axis = (c_high - c_low) / np.linalg.norm(c_high - c_low)
    (lo, lt, ln), (hi_, ht, hn) = split(rectum, c_high, axis)
    rectum["co"], rectum["idx"], rectum["n"] = hi_, ht, hn
    info = rectum["info"]
    vis.add("Anal canal", info["path"], lo, lt, info["seg"][0][0], normals=ln, source=info.get("source", "Z-Anatomy"))


# MARK: - Female pelvis

def female_pelvis(vis):
    cervix = vis.get("Cervix of uterus")
    bladder = next(p for p in vis.where(lambda i: i["name"] == "Urinary bladder" and i.get("sex") == "f"))
    mat = vis.material("Female genitalia")

    # Vagina: from the vestibule up and back to the vault round the cervix.
    cc = cervix["co"]
    tip = cc[cc[:, 1] < cc[:, 1].min() + 0.006].mean(0)
    vault = tip + [0, 0.008, -0.009]
    introitus = np.array([-0.001, 0.783, -0.007])
    # Steep below, leaning back towards the vault (concave forwards).
    mid = np.array([(vault[0] + introitus[0]) / 2, introitus[1] + 0.6 * (vault[1] - introitus[1]), introitus[2] - 0.002])
    path = resample(bezier(introitus, mid, vault, 200), 0.0012)
    s = np.linspace(0, 1, len(path))
    dome = np.sqrt(np.clip(1 - ((s - 0.86) / 0.14).clip(0) ** 2, 0, 1))
    entry = np.sqrt(np.clip(1 - ((0.06 - s) / 0.06).clip(0) ** 2, 0.08, 1))
    rx = (0.0085 + 0.0075 * s) * dome * entry
    ry = (0.0038 + 0.0072 * s ** 1.4) * dome * entry
    vco, vt = tube(path[1:-1], rx[1:-1].clip(0.0006), ry[1:-1].clip(0.0006), sides=36, lateral=[1, 0, 0])
    vagina = vis.add("Vagina", FEMALE + ["Female internal genitalia"], vco, vt, mat, sex="f")
    length = np.linalg.norm(np.diff(path, axis=0), axis=1).sum()

    # Female urethra: bladder neck to the vestibule, in front of the vagina.
    co = bladder["co"]
    low = co[np.abs(co[:, 0] - np.median(co[:, 0])) < 0.004]
    neck = low[low[:, 1].argmin()] + [0, 0.003, 0]
    meatus = np.array([-0.001, 0.785, 0.0015])
    mid = (neck + meatus) / 2 + [0, 0, -0.0015]
    path = resample(bezier(neck, mid, meatus, 120), 0.001)
    s = np.linspace(0, 1, len(path))
    r = 0.0029 - 0.0008 * s ** 3
    uco, ut = tube(path, r, sides=20)
    urethra = vis.get("Urethra")
    vis.add("Female urethra", urethra["info"]["path"], uco, ut, urethra["info"]["seg"][0][0], sex="f")
    tree = bvh([mesh(vagina)])
    gap = min(tree.find_nearest(Vector(p))[3] for p in path[5:-5]) - 0.0029
    print(f"  urethra–vagina gap {gap * 1000:.1f} mm, urethra {np.linalg.norm(np.diff(path, axis=0), axis=1).sum() * 100:.1f} cm, "
          f"vagina {length * 100:.1f} cm", flush=True)


# MARK: - Breast

def breasts(vis, muscular, skeletal):
    g = load_glb(os.path.join(HRA, "mammary-gland-female-left.glb"))
    pieces = [  # name, glb nodes, material, triangle budget, covering
        ("Fat body of breast", ["fat_L"], "Breast fat", 9000, True),
        ("Lobes of mammary gland", ["mammary_lobes_L"], "Mammary lobule", 24000, False),
        ("Lactiferous ducts", ["main_lactiferous_ducts_L", "main_lactiferous_sinuses_L"], "Lactiferous duct", 14000, False),
        ("Areola", ["areola_L", "areolar_tubercles_L"], "Female genitalia", 2200, False),
        ("Nipple", ["nipple_L"], "Female genitalia", 1200, False),
    ]
    meshes = []
    for name, nodes, material, budget, covering in pieces:
        co, tris = merge([g[n] for n in nodes])
        co, tris = decimate(co, tris, budget)
        meshes.append([co, tris])

    # Nipple at the fourth intercostal space, a little lateral to the
    # midclavicular line.
    ribs = {k: skeletal.get(f"{k} rib.l")["co"] for k in ("Fourth", "Fifth")}
    x = 0.094
    front = {k: c[(np.abs(c[:, 0] - x) < 0.006)] for k, c in ribs.items()}
    front = {k: c[c[:, 2] > c[:, 2].max() - 0.012] for k, c in front.items()}
    y = (front["Fourth"][:, 1].mean() + front["Fifth"][:, 1].mean()) / 2
    scale = 0.86
    nipple = meshes[4][0].mean(0)
    for m in meshes:
        m[0] = (m[0] - nipple) * scale + [x, y, 0.2]

    # Lay the base onto the chest wall.
    wall_parts = [p for p in muscular.parts if any(k in p["info"]["base"] for k in
                  ("pectoralis major", "Serratus anterior", "External abdominal oblique", "intercostal"))]
    wall_parts += [p for p in skeletal.parts if any(k in p["info"]["base"] for k in ("rib", "sternum", "Costal cartilage", "Sternum"))]
    wall = bvh([mesh(p) for p in wall_parts if p["info"]["bounds"][0] > -0.05])
    fat = meshes[0][0]
    lo, hi = fat.min(0) - 0.01, fat.max(0) + 0.01
    step = 0.002
    xs = np.arange(lo[0], hi[0], step); ys = np.arange(lo[1], hi[1], step)
    wz = ray_grid(wall, xs, ys, lambda x, y: (x, y, 0.5), (0, 0, -1))
    bz = np.full_like(wz, np.nan)
    i = np.clip(((fat[:, 0] - xs[0]) / step).astype(int), 0, len(xs) - 1)
    j = np.clip(((fat[:, 1] - ys[0]) / step).astype(int), 0, len(ys) - 1)
    for a, b, z in zip(i, j, fat[:, 2]):
        if np.isnan(bz[a, b]) or z < bz[a, b]:
            bz[a, b] = z
    d = wz + 0.0025 - bz
    known = ~np.isnan(d)
    # Fill the gaps (outside the footprint) from the nearest known cells.
    while not known.all():
        grown = d.copy()
        for sx, sy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            shifted = np.roll(np.roll(d, sx, 0), sy, 1)
            take = ~known & ~np.isnan(shifted)
            grown[take] = shifted[take]
        d = grown
        known = ~np.isnan(d)
    k = np.exp(-0.5 * (np.arange(-8, 9) / 3.0) ** 2); k /= k.sum()
    for axis in (0, 1):
        d = np.apply_along_axis(lambda r: np.convolve(np.pad(r, 8, mode="edge"), k, "valid"), axis, d)
    for m in meshes:
        m[0][:, 2] += sample(d, xs, ys, m[0][:, 0], m[0][:, 1])

    for (name, _, material, _, covering), (co, tris) in zip(pieces, meshes):
        path = FEMALE + ["Breast"] + ([] if covering else ["Mammary gland"])
        for side, sign in (("l", 1), ("r", -1)):
            c = co * [sign, 1, 1]
            t = tris if sign > 0 else tris[:, ::-1].copy()
            vis.add(f"{name}.{side}", path, c, t, material, side=side, sex="f", covering=covering, source=HRA_SOURCE)


# MARK: - Lymphoid

def lymphoid(lym, vis, cardio, skeletal):
    duct_mat = lym.get("Palatine tonsil.l")["info"]["seg"][0][0]
    vessel = lym.material("Lymph-1")
    aorta_t = cardio.get("Thoracic aorta")["co"]; aorta_a = cardio.get("Abdominal aorta")["co"]
    azygos = cardio.get("Azygos vein")["co"]
    oes = vis.get("Oesophagus")["co"]
    vertebrae = [p for p in skeletal.parts if p["info"]["name"].startswith("Vertebra")]
    spine = np.concatenate([p["co"] for p in vertebrae])
    spine = spine[np.abs(spine[:, 0]) < 0.008]

    def front_of_spine(y):
        s = spine[np.abs(spine[:, 1] - y) < 0.004]
        return s[:, 2].max()

    def venous_angle(side):
        ijv = cardio.get(f"Internal jugular vein.{side}")["co"]
        return ijv[ijv[:, 1] < ijv[:, 1].min() + 0.006].mean(0)

    pts = []
    # Cisterna chyli: right of and behind the abdominal aorta at L1–L2.
    for y in (1.050, 1.075, 1.100):
        c, r = slice_centre(aorta_a, y)
        pts.append([c[0] - r - 0.0055, y, front_of_spine(y) + 0.006])
    cist = np.array(pts)
    # Thoracic duct: between aorta and azygos in front of the spine, then to
    # the left behind the oesophagus at T4–T5, arching into the left venous angle.
    duct = [cist[-1]]
    for y in np.arange(1.13, 1.32, 0.02):
        a, ra = slice_centre(aorta_t if y > 1.21 else aorta_a, y)
        z_az, rz = slice_centre(azygos, y)
        right = z_az[0] + rz if z_az is not None else a[0] - ra - 0.012
        duct.append([(a[0] - ra + right) / 2, y, front_of_spine(y) + 0.004])
    for y in np.arange(1.34, 1.44, 0.02):
        e, re = slice_centre(oes, y)
        duct.append([e[0] + re + 0.003 * (y - 1.32) / 0.12 + 0.002, y, e[2] - re * 0.4])
    angle = venous_angle("l")
    top = duct[-1]
    duct.append([angle[0] - 0.004, angle[1] + 0.032, angle[2] - 0.012])
    duct.append([angle[0] + 0.001, angle[1] + 0.012, angle[2] - 0.006])
    duct.append(angle + [0.001, 0.004, -0.002])
    path = spline(duct, 0.0015)
    obstacles = bvh([(aorta_t, cardio.get("Thoracic aorta")["idx"]), (aorta_a, cardio.get("Abdominal aorta")["idx"]),
                     (azygos, cardio.get("Azygos vein")["idx"]), mesh(vis.get("Oesophagus"))] + [mesh(p) for p in vertebrae])
    n = len(path)
    path = push_out(path, obstacles, 0.0034, fixed={0, n - 1, n - 2, n - 3})
    s = np.arange(n) * 0.0015
    r = 0.0022 * (1 + 0.12 * np.sin(2 * np.pi * s / 0.011)) * np.clip(s / 0.01, 0.8, 1)
    co, t = tube(path, r, sides=14)
    lym.add("Thoracic duct", ["Lymphoid organs", "Lymphatic trunks and ducts"], co, t, vessel)

    cpath = spline(np.vstack([cist[0] + [0, -0.006, 0], cist, duct[1]]), 0.001)
    s = np.linspace(0, 1, len(cpath))
    rx = 0.0023 + 0.0042 * np.sin(np.pi * np.clip(s / 0.8, 0, 1)) ** 0.8
    co, t = tube(cpath, rx, rx * 1.25, sides=20, lateral=[1, 0, 0])
    lym.add("Cisterna chyli", ["Lymphoid organs", "Lymphatic trunks and ducts"], co, t, vessel)

    angle = venous_angle("r")
    rpath = spline([angle + [0.0, 0.002, -0.002], angle + [-0.005, 0.008, -0.005], angle + [-0.011, 0.014, -0.006]], 0.001)
    co, t = tube(rpath, 0.0019, sides=12)
    lym.add("Right lymphatic duct", ["Lymphoid organs", "Lymphatic trunks and ducts"], co, t, vessel)

    # Pharyngeal tonsil on the roof and back wall of the nasopharynx.
    naso = vis.get("Nasopharynx")
    lo, hi = np.array(naso["info"]["bounds"][:3]), np.array(naso["info"]["bounds"][3:])
    origin = (lo + hi) / 2 + [0, -0.004, 0.006]
    co, t = pad(bvh([mesh(naso)]), origin, [0, 0.55, -0.85], [1, 0, 0], (0.75, 0.55), (28, 22), 0.0042,
                lambda a, b: 1 + 0.22 * np.cos(5 * np.pi * a) * (1 - np.abs(b)))
    lym.add("Pharyngeal tonsil", ["Lymphoid organs", "Secondary lymphoid organs", "Pharyngeal lymphoid ring"], co, t, duct_mat)

    # Lingual tonsil on the root of the tongue, behind the sulcus terminalis.
    tongue = vis.get("Tongue")
    lo, hi = np.array(tongue["info"]["bounds"][:3]), np.array(tongue["info"]["bounds"][3:])
    origin = np.array([0, lo[1] + 0.024, lo[2] - 0.008])
    rng = np.random.default_rng(3)
    bumps = rng.uniform(-1, 1, (26, 2))

    def follicles(a, b):
        f = np.zeros_like(a)
        for bx, by in bumps:
            f += np.exp(-((a - bx) ** 2 + (b - by) ** 2) / 0.02)
        return 0.55 + 0.6 * np.clip(f, 0, 1)

    co, t = pad(bvh([mesh(tongue)]), origin, [0, -0.35, 1], [1, 0, 0], (0.6, 0.45), (30, 24), 0.0028, follicles)
    lym.add("Lingual tonsil", ["Lymphoid organs", "Secondary lymphoid organs", "Pharyngeal lymphoid ring"], co, t, duct_mat)


# MARK: - Pericardium, scrotum

def pericardium(cardio):
    pts = []
    for name in ("Right atrium", "Left atrium", "Right ventricle", "Left ventricle"):
        pts.append(cardio.get(name)["co"])
    for name, top in (("Ascending aorta", 1.345), ("Pulmonary trunk", 1.352), ("Superior vena cava", 1.358)):
        c = cardio.get(name)["co"]
        pts.append(c[c[:, 1] < top])
    pts = np.concatenate(pts)
    co, t = convex_hull(pts[::3])
    co, t = remesh(co, t, 0.0028, smooth=6)
    co = inflate(co, t, 0.0028)
    cardio.add("Pericardium", cardio.get("Right atrium")["info"]["path"][:1], co, t, "Pericardium", covering=True)


def phrenic(nerv, muscular, cardio):
    """Phrenic nerves (C3–C5): down the front of scalenus anterior, between
    the subclavian vein and artery into the thorax, past the brachiocephalic
    vein and superior vena cava (right) or the aortic arch (left), then on
    the side of the pericardium in front of the lung root to the diaphragm."""
    peri = cardio.get("Pericardium")["co"]
    vessels = ["Right subclavian artery", "Left subclavian artery", "Right subclavian vein", "Left subclavian vein",
               "Right brachiocephalic vein", "Left brachiocephalic vein", "Superior vena cava", "Thoracic aorta",
               "Ascending aorta", "Brachiocephalic trunk"]
    obstacles = bvh([mesh(cardio.get("Pericardium"))] + [mesh(cardio.get(n)) for n in vessels])
    floor = bvh([mesh(muscular.get("Diaphragm"))])
    path = nerv.get("Accessory nerve (XI).r")["info"]["path"] + ["Cervical plexus"]
    mat = nerv.material("Nerve")
    radius = 0.0011
    for side, sign in (("r", -1), ("l", 1)):
        sc = muscular.get(f"Scalenus anterior muscle.{side}")["co"]
        pts = []
        # On the anterior surface of scalenus anterior, from its lateral to its medial border.
        levels = (1.49, 1.47, 1.45, 1.43, 1.415)
        for k, y in enumerate(levels):
            sl = sc[np.abs(sc[:, 1] - y) < 0.004]
            lateral, medial = (sl[:, 0] * sign).max(), (sl[:, 0] * sign).min()
            t = k / (len(levels) - 1)
            x = (lateral - (0.3 + 0.45 * t) * (lateral - medial)) * sign
            near = sl[np.abs(sl[:, 0] - x) < 0.004]
            pts.append([x, y, near[:, 2].max() + 0.0025])
        if side == "r":
            for name, y in (("Right brachiocephalic vein", 1.392), ("Superior vena cava", 1.36), ("Superior vena cava", 1.345)):
                c, _ = slice_centre(cardio.get(name)["co"], y)
                v = cardio.get(name)["co"]; sl = v[np.abs(v[:, 1] - y) < 0.003]
                pts.append([sl[:, 0].min() - 0.004, y, c[2]])
        else:
            arch = cardio.get("Thoracic aorta")["co"]
            for y in (1.392, 1.37, 1.355):
                sl = arch[np.abs(arch[:, 1] - y) < 0.003]
                if len(sl):
                    pts.append([sl[:, 0].max() + 0.004, y, sl[:, 2].max() - 0.004])
        bottom = peri[:, 1].min()
        for y in np.arange(1.33, bottom + 0.012, -0.012):
            sl = peri[np.abs(peri[:, 1] - y) < 0.003]
            front = sl[sl[:, 2] > sl[:, 2].mean() - 0.004]
            v = front[(front[:, 0] * sign).argmax()]
            pts.append(v + [0.0025 * sign, 0, 0])
        last = np.array(pts[-1])
        loc, _, _, _ = floor.ray_cast(Vector(last), Vector((0, -1, 0)))
        if loc is not None:
            pts.append(np.array(loc) + [0, -0.001, 0])
        line = spline(pts, 0.0015)
        n = len(line)
        line = push_out(line, obstacles, radius + 0.0012, fixed={0, n - 1})
        co, t = tube(line, radius, sides=10)
        nerv.add(f"Phrenic nerve.{side}", path, co, t, mat, side=side)


def scrotum(vis):
    pts = [vis.get(n)["co"] for n in ("Testis.l", "Testis.r", "Epididymis.l", "Epididymis.r")]
    dd = [vis.get(f"Ductus deferens.{s}")["co"] for s in "lr"]
    pts += [c[(c[:, 1] < 0.785) & (c[:, 2] > 0.03)] for c in dd]
    co, t = convex_hull(np.concatenate(pts))
    co, t = remesh(co, t, 0.0025, round_off=30)
    co = inflate(co, t, 0.005)
    # Narrow towards the root, above the testes.
    top = max(vis.get(n)["co"][:, 1].max() for n in ("Testis.l", "Testis.r", "Epididymis.l", "Epididymis.r")) + 0.002
    centre = co.mean(0)
    k = np.clip((co[:, 1] - top) / (co[:, 1].max() - top), 0, 1)
    k = k * k * (3 - 2 * k)
    co[:, 0] = centre[0] + (co[:, 0] - centre[0]) * (1 - 0.42 * k)
    co[:, 2] = centre[2] + (co[:, 2] - centre[2]) * (1 - 0.25 * k)
    # The median raphe.
    n = vertex_normals(co, t)
    w = np.clip(1 - np.abs(co[:, 0] - centre[0]) / 0.011, 0, 1)
    w = w * w * (3 - 2 * w)
    co = co - n * (0.0014 * w)[:, None]
    vis.add("Scrotum", MALE, co, t, "Scrotum", sex="m", covering=True)
    tree = bvh([(co, t)])
    testes = np.concatenate([vis.get(n)["co"] for n in ("Testis.l", "Testis.r")])
    inside = np.mean([np.dot(np.array(tree.find_nearest(Vector(v))[0]) - v, tree.find_nearest(Vector(v))[1]) > 0 for v in testes[::5]])
    print(f"  testes inside the scrotum: {inside * 100:.0f}%", flush=True)


# MARK: - Female skin

def female_skin(regions):
    """The urogenital region of the skin for the female body: a smooth
    shell from under the pubic hair to the anal region, tucked under the
    thighs, with the fullness of the labia majora and the pudendal cleft.
    The male region (penis and scrotum) is marked "m"."""
    male = regions.where(lambda i: i["name"].startswith("Urogenital region"))
    for p in male:
        p["info"]["sex"] = "m"
    outer_mat, inner_mat = regions.material("Skin-1"), regions.material("Skin-in")
    midline = spline([(0, 0.852, 0.071), (0, 0.838, 0.066), (0, 0.824, 0.060), (0, 0.808, 0.049), (0, 0.794, 0.031),
                      (0, 0.784, 0.011), (0, 0.777, -0.006), (0, 0.773, -0.019)], 0.001)
    ns, nw = len(midline), 41
    s = np.linspace(0, 1, ns)
    tan = np.gradient(midline, axis=0); tan /= np.linalg.norm(tan, axis=1, keepdims=True)
    # Outward: anterior-inferior, perpendicular to the midline in the sagittal plane.
    out = np.stack([np.zeros(ns), -tan[:, 2], tan[:, 1]], 1)
    out *= np.sign(out[:, 2:3] - out[:, 1:2] + 1e-9)
    half = np.interp(s, [0, 0.12, 0.35, 0.7, 1], [0.05, 0.042, 0.030, 0.024, 0.021])
    w = np.linspace(-1.2, 1.2, nw)
    S, W = np.meshgrid(s, w, indexing="ij")

    def window(x, a, b, soft):
        return np.clip((x - a) / soft, 0, 1) * np.clip((b - x) / soft, 0, 1)

    depth = -0.009 * W ** 2 * (np.abs(W) > 0) - 0.01 * np.clip(np.abs(W) - 1, 0, None)
    labia = 0.0035 * window(S, 0.36, 0.93, 0.18) * np.exp(-((np.abs(W) - 0.42) / 0.3) ** 2)
    cleft = 0.003 * window(S, 0.44, 0.91, 0.08) * np.exp(-(W / 0.1) ** 2)
    mons = 0.003 * np.exp(-((S - 0.2) / 0.14) ** 2) * np.clip(1 - W ** 2, 0, 1) - 0.004 * np.clip(0.08 - S, 0, None) / 0.08
    h = depth + labia - cleft + mons
    outer = midline[:, None, :] + (W * half[:, None])[..., None] * np.array([1.0, 0, 0]) + h[..., None] * out[:, None, :]
    inner = outer - out[:, None, :] * 0.003
    co = np.vstack([outer.reshape(-1, 3), inner.reshape(-1, 3)])
    off = ns * nw

    def quads(base_index, flip):
        t = []
        for i in range(ns - 1):
            for j in range(nw - 1):
                a, b, c, d = i * nw + j, (i + 1) * nw + j, (i + 1) * nw + j + 1, i * nw + j + 1
                t += [(a, b, c), (a, c, d)] if not flip else [(a, c, b), (a, d, c)]
        return np.array(t) + base_index

    top, bottom = quads(0, False), quads(off, True)
    rim = [(0, j) for j in range(nw)] + [(i, nw - 1) for i in range(1, ns)] + \
          [(ns - 1, j) for j in range(nw - 2, -1, -1)] + [(i, 0) for i in range(ns - 2, 0, -1)]
    side = []
    for k in range(len(rim)):
        a = rim[k][0] * nw + rim[k][1]; b = rim[(k + 1) % len(rim)][0] * nw + rim[(k + 1) % len(rim)][1]
        side += [(a, off + a, off + b), (a, off + b, b)]
    side = np.array(side)
    tris = outward(co, np.vstack([top, bottom, side]))
    ref = male[0]["info"]
    regions.add("Urogenital region", ref["path"], co, tris, outer_mat, sex="f", source=MODELLED,
                runs=[[outer_mat, len(top)], [inner_mat, len(bottom) + len(side)]])


# MARK: - Main

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    vis, lym, cardio, regions = Pack("visceral"), Pack("lymphoid"), Pack("cardiovascular"), Pack("regions")
    nerv = Pack("nervous")
    muscular, skeletal = Pack("muscular"), Pack("skeletal")
    assert not any(p["info"]["name"] == "Caecum" for p in vis.parts), \
        "the visceral pack is already cut; start from tools/add_female.py's output"

    digestive(vis)
    female_pelvis(vis)
    breasts(vis, muscular, skeletal)
    scrotum(vis)
    lymphoid(lym, vis, cardio, skeletal)
    pericardium(cardio)
    phrenic(nerv, muscular, cardio)
    female_skin(regions)

    for p in cardio.parts:
        name = p["info"]["name"].lower()
        if "penis" in name or "testicular" in name:
            p["info"]["sex"] = "m"

    for pack in (vis, lym, cardio, regions, nerv):
        pack.write()


if __name__ == "__main__":
    main()
