"""Adds the female internal genital organs to the visceral pack.

    Blender -b --python tools/add_female.py -- <hra_dir> <in_dir> <out_dir>

Z-Anatomy and BodyParts3D model a male body. The uterus, ovaries and
uterine tubes come from the Human Reference Atlas 3D reference organs
(HuBMAP, Visible Human Female, CC BY 4.0, https://humanatlas.io):

    uterus-female.glb, ovary-female-left/right.glb,
    fallopian-tube-female-left/right.glb, urinary-bladder-female.glb,
    pelvis-female.glb

They share the frame of the female pelvis model, so one transform places
all of them: a similarity ICP of the HRA pelvis onto the atlas pelvis (hip
bones, sacrum, coccyx), refined with a mild per-axis scale because the
atlas pelvis is male and narrower. The organs are appended to <in_dir>'s
"ANT1" visceral pack with "sex": "f"; the male genital parts are marked
"sex": "m" so the app can show one set at a time. The female bladder
replaces the male one (which sits where the cervix is) and the ureters get
female copies whose pelvic part is bent onto its ureteral orifices. Run
bake_ao and build_lods afterwards.
"""
import json
import os
import struct
import sys
import zlib

import bpy
import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

ARGS = sys.argv[sys.argv.index("--") + 1:]
HRA, IN_DIR, OUT_DIR = ARGS[:3]
MODELS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Anatomy", "Resources", "Models")
FEMALE_PATH = ["Visceral systems", "Genital systems", "Female genital system", "Female internal genitalia"]
TUBE = {"ampulla_of_uterine_tube": "Ampulla of uterine tube", "isthmus_of_fallopian_tube": "Isthmus of uterine tube",
        "uterine_tube_infundibulum": "Infundibulum of uterine tube", "fibria_of_uterine_tube": "Fimbriae of uterine tube"}


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


def merge(meshes):
    cos, tris, base = [], [], 0
    for co, t in meshes:
        cos.append(co); tris.append(t + base); base += len(co)
    return np.concatenate(cos), np.concatenate(tris)


def read_pack(path_bin, path_json, names=None):
    raw = zlib.decompress(open(path_bin, "rb").read(), -15)
    manifest = json.load(open(path_json))
    has_ao = raw[3:4] in (b"2", b"3")
    count, = struct.unpack_from("<I", raw, 4)
    lo = np.array(struct.unpack_from("<3f", raw, 8)); hi = np.array(struct.unpack_from("<3f", raw, 20))
    counts = [struct.unpack_from("<II", raw, 32 + 8 * i) for i in range(count)]
    cur = 32 + 8 * count
    parts = []
    for (nv, ni), info in zip(counts, manifest["parts"]):
        co = np.frombuffer(raw, "<u2", nv * 3, cur).reshape(-1, 3).astype(np.float64) / 65535 * (hi - lo) + lo
        cur += nv * 6
        nrm = np.frombuffer(raw, "i1", nv * 3, cur).reshape(-1, 3).astype(np.float64) / 127
        cur += nv * 3
        wide = nv > 65535
        idx = np.frombuffer(raw, "<u4" if wide else "<u2", ni, cur).astype(np.int64).reshape(-1, 3)
        cur += ni * (4 if wide else 2) + (nv if has_ao else 0)
        if names is None or info["base"] in names:
            parts.append({"info": info, "co": co, "n": nrm, "idx": idx})
    return manifest, parts, lo, hi


def similarity(src, dst):
    ms, md = src.mean(0), dst.mean(0)
    a, b = src - ms, dst - md
    u, d, vt = np.linalg.svd(b.T @ a / len(src))
    sgn = np.eye(3)
    if np.linalg.det(u @ vt) < 0:
        sgn[2, 2] = -1
    r = u @ sgn @ vt
    s = np.trace(np.diag(d) @ sgn) / (a ** 2).sum(1).mean()
    return s, r, md - s * r @ ms


def subdivide(co, tris, levels):
    """Catmull-Clark smoothing for the very light HRA meshes (the ovaries)."""
    me = bpy.data.meshes.new("organ")
    me.from_pydata(co.tolist(), [], tris.tolist())
    ob = bpy.data.objects.new("organ", me)
    bpy.context.scene.collection.objects.link(ob)
    weld = ob.modifiers.new("weld", "WELD"); weld.merge_threshold = 0.00002
    sub = ob.modifiers.new("sub", "SUBSURF"); sub.levels = levels; sub.render_levels = levels
    dg = bpy.context.evaluated_depsgraph_get()
    ev = ob.evaluated_get(dg)
    m2 = ev.to_mesh(); m2.calc_loop_triangles()
    c = np.empty(len(m2.vertices) * 3); m2.vertices.foreach_get("co", c)
    t = np.empty(len(m2.loop_triangles) * 3, dtype=np.int64); m2.loop_triangles.foreach_get("vertices", t)
    ev.to_mesh_clear()
    bpy.data.objects.remove(ob); bpy.data.meshes.remove(me)
    return c.reshape(-1, 3), t.reshape(-1, 3)


def decimate(co, tris, target):
    """Collapse decimation for the dense HRA meshes (the bladder)."""
    me = bpy.data.meshes.new("organ")
    me.from_pydata(co.tolist(), [], tris.tolist())
    ob = bpy.data.objects.new("organ", me)
    bpy.context.scene.collection.objects.link(ob)
    weld = ob.modifiers.new("weld", "WELD"); weld.merge_threshold = 0.00002
    dec = ob.modifiers.new("dec", "DECIMATE"); dec.ratio = min(1, target / len(tris))
    dg = bpy.context.evaluated_depsgraph_get()
    ev = ob.evaluated_get(dg)
    m2 = ev.to_mesh(); m2.calc_loop_triangles()
    c = np.empty(len(m2.vertices) * 3); m2.vertices.foreach_get("co", c)
    t = np.empty(len(m2.loop_triangles) * 3, dtype=np.int64); m2.loop_triangles.foreach_get("vertices", t)
    ev.to_mesh_clear()
    bpy.data.objects.remove(ob); bpy.data.meshes.remove(me)
    return c.reshape(-1, 3), t.reshape(-1, 3)


def vertex_normals(co, tris):
    n = np.zeros_like(co)
    fn = np.cross(co[tris[:, 1]] - co[tris[:, 0]], co[tris[:, 2]] - co[tris[:, 0]])
    for k in range(3):
        np.add.at(n, tris[:, k], fn)
    ln = np.linalg.norm(n, axis=1, keepdims=True); ln[ln == 0] = 1
    return n / ln


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    # Target: the atlas pelvis.
    _, pelvis, _, _ = read_pack(os.path.join(MODELS, "mesh-skeletal.bin"), os.path.join(MODELS, "mesh-skeletal.json"),
                                {"Hip bone", "Sacrum", "Coccyx"})
    tgt_co = np.concatenate([p["co"] for p in pelvis])
    offs = np.cumsum([0] + [len(p["co"]) for p in pelvis])
    tgt_tris = np.concatenate([p["idx"] + offs[k] for k, p in enumerate(pelvis)])
    tree = BVHTree.FromPolygons([Vector(v) for v in tgt_co], [tuple(t) for t in tgt_tris])

    # Source: the HRA female pelvis (outer, compact bone).
    hp = load_glb(os.path.join(HRA, "pelvis-female.glb"))
    src = np.concatenate([co for name, (co, _) in hp.items() if "spongy" not in name])
    rng = np.random.default_rng(7)
    sample = src[rng.choice(len(src), min(len(src), 4000), replace=False)]

    # Start: centroids and spread.
    s0 = np.sqrt(((tgt_co - tgt_co.mean(0)) ** 2).sum(1).mean() / ((sample - sample.mean(0)) ** 2).sum(1).mean())
    M = np.eye(3) * s0
    T = tgt_co.mean(0) - M @ sample.mean(0)

    def apply(p):
        return (M @ p.T).T + T

    def nearest(pts):
        out = np.empty_like(pts); dist = np.empty(len(pts))
        for i, p in enumerate(pts):
            loc, _, _, d = tree.find_nearest(Vector(p))
            out[i] = loc; dist[i] = d
        return out, dist

    for it in range(40):
        cur = apply(sample)
        q, d = nearest(cur)
        ok = d < np.percentile(d, 85) * 1.5 + 1e-6
        s, r, t = similarity(cur[ok], q[ok])
        M = s * r @ M
        T = s * r @ T + t
    # Mild per-axis scale (the atlas pelvis is male and narrower).
    for it in range(10):
        cur = apply(sample)
        q, d = nearest(cur)
        ok = d < np.percentile(d, 85) * 1.5 + 1e-6
        c = cur[ok].mean(0); cq = q[ok].mean(0)
        a = cur[ok] - c; b = q[ok] - cq
        k = np.clip((a * b).sum(0) / np.maximum((a * a).sum(0), 1e-12), 0.85, 1.15)
        D = np.diag(k)
        M = D @ M
        T = D @ (T - c) + cq
    _, d = nearest(apply(sample))
    print(f"pelvis fit: mean {d.mean() * 1000:.1f} mm, 90% {np.percentile(d, 90) * 1000:.1f} mm", flush=True)

    manifest, parts, lo, hi = read_pack(os.path.join(IN_DIR, "mesh-visceral.bin"), os.path.join(IN_DIR, "mesh-visceral.json"))
    materials = manifest.setdefault("materials", [])
    if "Female genitalia" not in materials:
        materials.append("Female genitalia")
    mat = materials.index("Female genitalia")
    for p in parts:
        if "Male genital system" in p["info"]["path"]:
            p["info"]["sex"] = "m"

    def add(name, base, side, meshes, path=FEMALE_PATH, material=None, budget=None):
        co, tris = merge(meshes)
        if len(tris) < 1500:
            co, tris = subdivide(co, tris, 2)
        if budget and len(tris) > budget:
            co, tris = decimate(co, tris, budget)
        co = np.clip(apply(co), lo, hi)
        used = np.unique(tris); remap = np.full(len(co), -1); remap[used] = np.arange(len(used))
        co, tris = co[used], remap[tris]
        info = {"name": name, "base": base, "path": path, "tris": int(len(tris)),
                "bounds": [round(float(v), 4) for v in (*co.min(0), *co.max(0))],
                "seg": [[mat if material is None else material, int(len(tris))]], "sex": "f",
                "source": "Human Reference Atlas (HuBMAP), CC BY 4.0"}
        if side:
            info["side"] = side
        parts.append({"info": info, "co": co, "n": vertex_normals(co, tris), "idx": tris})
        print(f"  + {name:<36} {len(tris):>6} tris", flush=True)
        return co

    ut = load_glb(os.path.join(HRA, "uterus-female.glb"))
    add("Uterus", "Uterus", None, [ut["anterior_wall_of_uterus"], ut["posterior_wall_of_uterus"], ut["cornua"]])
    add("Cervix of uterus", "Cervix of uterus", None, [ut["cervix"], ut["cervicovaginal_junction"]])
    for side, suffix in (("l", "left"), ("r", "right")):
        ov = load_glb(os.path.join(HRA, f"ovary-female-{suffix}.glb"))
        add(f"Ovary.{side}", "Ovary", side, list(ov.values()))
        tube = load_glb(os.path.join(HRA, f"fallopian-tube-female-{suffix}.glb"))
        for key, base in TUBE.items():
            mesh = tube.get(f"{key}_{side.upper()}")
            if mesh is not None:
                add(f"{base}.{side}", base, side, [mesh], FEMALE_PATH + ["Uterine tube"])

    # The bladder: the male one sits where the cervix is.
    male = next(p for p in parts if p["info"]["name"] == "Urinary bladder")
    for p in parts:
        if p["info"]["base"] in ("Urinary bladder", "Urethra", "Ureter"):
            p["info"]["sex"] = "m"
    bl = load_glb(os.path.join(HRA, "urinary-bladder-female.glb"))
    add("Urinary bladder", "Urinary bladder", None,
        [bl["fundus_of_urinary_bladder_dome"], bl["fundus_of_urinary_bladder_base"], bl["urinary_bladder_neck_smooth_muscle"]],
        male["info"]["path"], male["info"]["seg"][0][0], budget=9000)

    # Female ureters: the atlas ureters, their pelvic part bent onto the
    # female bladder's ureteral orifices.
    for side, key in (("l", "L"), ("r", "R")):
        ureter = next(p for p in parts if p["info"]["name"] == f"Ureter.{side}" and p["info"].get("sex") == "m")
        orifice = apply(bl[f"ureteral_orifice_{key}"][0]).mean(0)
        co = ureter["co"]
        end = co[co[:, 1] < co[:, 1].min() + 0.003].mean(0)
        brim = 0.93
        w = np.clip((brim - co[:, 1]) / (brim - end[1]), 0, 1)
        w = w * w * (3 - 2 * w)
        bent = co + w[:, None] * (orifice - end)
        info = dict(ureter["info"], sex="f", bounds=[round(float(v), 4) for v in (*bent.min(0), *bent.max(0))])
        parts.append({"info": info, "co": np.clip(bent, lo, hi), "n": vertex_normals(bent, ureter["idx"]), "idx": ureter["idx"]})
        print(f"  + Ureter.{side} bent {np.linalg.norm(orifice - end) * 1000:.0f} mm onto the female bladder", flush=True)

    blob = bytearray(b"ANT1" + struct.pack("<I", len(parts)) + struct.pack("<3f", *lo) + struct.pack("<3f", *hi))
    for p in parts:
        blob += struct.pack("<II", len(p["co"]), p["idx"].size)
    for p in parts:
        blob += np.clip(np.round((p["co"] - lo) / (hi - lo) * 65535), 0, 65535).astype("<u2").tobytes()
        blob += np.clip(np.round(p["n"] * 127), -127, 127).astype("i1").tobytes()
        blob += p["idx"].astype("<u2" if len(p["co"]) <= 65535 else "<u4").tobytes()
    comp = zlib.compressobj(9, zlib.DEFLATED, -15)
    open(os.path.join(OUT_DIR, "mesh-visceral.bin"), "wb").write(comp.compress(bytes(blob)) + comp.flush())
    manifest["parts"] = [p["info"] for p in parts]
    json.dump(manifest, open(os.path.join(OUT_DIR, "mesh-visceral.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    print(f"visceral: {len(parts)} parts", flush=True)


main()
