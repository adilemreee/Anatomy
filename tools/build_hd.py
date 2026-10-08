"""Builds high-detail versions of Z-Anatomy parts from BodyParts3D.

    Blender -b --python tools/build_hd.py -- <bp3d_obj_dir> <parts_list_e.txt> <out_dir> skeletal [visceral ...]

Z-Anatomy's meshes are reduced BodyParts3D meshes. The BodyParts3D 3.0
"95 %" set (BodyParts3D_3.0_obj_95.zip, CC BY-SA 2.1 JP, DBCLS) has about
five times the triangles. For every part of the shipped packs this script

  1. finds the BodyParts3D mesh by name ("Femur.r" -> "right femur"),
  2. brings it into the app's frame: one similarity transform fitted on all
     matched parts, then rigid ICP onto the Z-Anatomy part,
  3. keeps it only when both surfaces agree closely in both directions,
  4. copies Z-Anatomy's material segments (e.g. articular cartilage) from
     the nearest Z-Anatomy triangle and caps very large meshes,

and writes hd-<system>.bin ("ANT1", see export_zanatomy.py) plus
hd-<system>.json, whose parts carry "lod": the index of the part they
replace. Run tools/bake_ao.swift on the .bin, then tools/pack_hd.py.
"""
import json
import os
import re
import struct
import sys
import zlib

import bpy
import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

ARGS = sys.argv[sys.argv.index("--") + 1:]
OBJ_DIR, PARTS_LIST, OUT = ARGS[0], ARGS[1], ARGS[2]
SYSTEMS = ARGS[3:] or ["skeletal"]
MODELS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Anatomy", "Resources", "Models")
MAX_TRIS = 80000
ORDINALS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
REGIONS = {"C": "cervical", "T": "thoracic", "L": "lumbar"}


# --- the shipped (LOD) packs --------------------------------------------------

def read_pack(system):
    raw = zlib.decompress(open(os.path.join(MODELS, f"mesh-{system}.bin"), "rb").read(), -15)
    manifest = json.load(open(os.path.join(MODELS, f"mesh-{system}.json")))
    assert raw[:3] == b"ANT"
    has_ao = raw[3:4] == b"2"
    count, = struct.unpack_from("<I", raw, 4)
    lo = np.array(struct.unpack_from("<3f", raw, 8)); hi = np.array(struct.unpack_from("<3f", raw, 20))
    cur = 32
    counts = [struct.unpack_from("<II", raw, cur + 8 * i) for i in range(count)]
    cur += 8 * count
    parts = []
    for (nv, ni), info in zip(counts, manifest["parts"]):
        co = np.frombuffer(raw, "<u2", nv * 3, cur).reshape(-1, 3).astype(np.float64) / 65535 * (hi - lo) + lo
        cur += nv * 6
        cur += nv * 3  # normals
        wide = nv > 65535
        idx = np.frombuffer(raw, "<u4" if wide else "<u2", ni, cur).astype(np.int64)
        cur += ni * (4 if wide else 2)
        if has_ao:
            cur += nv
        tri_mat = np.concatenate([np.full(n, m) for m, n in info.get("seg") or [[0, ni // 3]]]) if ni else np.zeros(0, int)
        parts.append({"info": info, "co": co, "idx": idx.reshape(-1, 3), "mat": tri_mat})
    return manifest, parts, lo, hi


# --- BodyParts3D --------------------------------------------------------------

def bp3d_names():
    names = {}
    for line in open(PARTS_LIST, encoding="utf-8"):
        cols = line.rstrip("\n").split("\t")
        if len(cols) >= 2 and cols[0].startswith("FMA"):
            names.setdefault(cols[1].strip().lower(), cols[0])
    return names


def obj_files():
    files = {}
    for root, _, fs in os.walk(OBJ_DIR):
        for f in fs:
            if f.lower().endswith(".obj"):
                files[os.path.splitext(f)[0]] = os.path.join(root, f)
    return files


def read_obj(path):
    vs, fs = [], []
    for line in open(path, encoding="utf-8", errors="ignore"):
        if line.startswith("v "):
            vs.append(line.split()[1:4])
        elif line.startswith("f "):
            ids = [int(t.split("/")[0]) for t in line.split()[1:]]
            for k in range(1, len(ids) - 1):
                fs.append((ids[0], ids[k], ids[k + 1]))
    v = np.array(vs, dtype=np.float64)
    f = np.array(fs, dtype=np.int64) - 1
    return v, f


def candidates(info):
    """BodyParts3D names to try for a Z-Anatomy part."""
    base = re.sub(r"^\((.*)\)$", r"\1", info["base"]).strip().lower()
    side = {"r": "right ", "l": "left "}.get(info.get("side"), "")
    out = [side + base, base]
    m = re.match(r"vertebra ([ctl])(\d+)$", base)
    if m:
        out.insert(0, f"{ORDINALS[int(m.group(2)) - 1]} {REGIONS[m.group(1).upper()]} vertebra")
    m = re.match(r"(atlas|axis) \(c\d\)$", base)
    if m:
        out.insert(0, m.group(1))
    if base.endswith(" bone"):
        out += [side + base[:-5], base[:-5]]
    if base.startswith("os "):
        out.append(side + base[3:])
    return out


# --- geometry -----------------------------------------------------------------

def similarity(src, dst):
    """Umeyama: s, R, t minimising |s R src + t - dst|."""
    ms, md = src.mean(0), dst.mean(0)
    a, b = src - ms, dst - md
    u, d, vt = np.linalg.svd(b.T @ a / len(src))
    sgn = np.eye(3)
    if np.linalg.det(u @ vt) < 0:
        sgn[2, 2] = -1
    r = u @ sgn @ vt
    s = np.trace(np.diag(d) @ sgn) / (a ** 2).sum(1).mean()
    return s, r, md - s * r @ ms


def rigid(src, dst):
    """Kabsch: R, t minimising |R src + t - dst|."""
    ms, md = src.mean(0), dst.mean(0)
    a, b = src - ms, dst - md
    u, _, vt = np.linalg.svd(b.T @ a)
    sgn = np.eye(3)
    if np.linalg.det(u @ vt) < 0:
        sgn[2, 2] = -1
    r = u @ sgn @ vt
    return r, md - r @ ms


def bvh(co, tris):
    return BVHTree.FromPolygons([Vector(p) for p in co], [tuple(t) for t in tris])


def nearest(tree, pts):
    out = np.empty_like(pts)
    dist = np.empty(len(pts))
    face = np.empty(len(pts), dtype=np.int64)
    for i, p in enumerate(pts):
        loc, _, f, d = tree.find_nearest(Vector(p))
        if loc is None:
            out[i] = p; dist[i] = 1e9; face[i] = -1
        else:
            out[i] = loc; dist[i] = d; face[i] = f
    return out, dist, face


def vertex_normals(co, tris):
    n = np.zeros_like(co)
    fn = np.cross(co[tris[:, 1]] - co[tris[:, 0]], co[tris[:, 2]] - co[tris[:, 0]])
    for k in range(3):
        np.add.at(n, tris[:, k], fn)
    ln = np.linalg.norm(n, axis=1, keepdims=True); ln[ln == 0] = 1
    return n / ln


def decimate(co, tris, target):
    me = bpy.data.meshes.new("hd")
    me.from_pydata(co.tolist(), [], tris.tolist())
    ob = bpy.data.objects.new("hd", me)
    bpy.context.scene.collection.objects.link(ob)
    mod = ob.modifiers.new("dec", "DECIMATE")
    mod.ratio = target / len(tris)
    mod.use_collapse_triangulate = True
    dg = bpy.context.evaluated_depsgraph_get()
    ev = ob.evaluated_get(dg)
    m2 = ev.to_mesh()
    m2.calc_loop_triangles()
    c = np.empty(len(m2.vertices) * 3); m2.vertices.foreach_get("co", c)
    t = np.empty(len(m2.loop_triangles) * 3, dtype=np.int64); m2.loop_triangles.foreach_get("vertices", t)
    ev.to_mesh_clear()
    bpy.data.objects.remove(ob); bpy.data.meshes.remove(me)
    return c.reshape(-1, 3), t.reshape(-1, 3)


# --- main ---------------------------------------------------------------------

def main():
    names = bp3d_names()
    files = obj_files()
    print(f"BodyParts3D: {len(names)} names, {len(files)} meshes", flush=True)
    os.makedirs(OUT, exist_ok=True)
    for system in SYSTEMS:
        manifest, parts, lo, hi = read_pack(system)
        matched = []
        for i, p in enumerate(parts):
            if len(p["idx"]) == 0:
                continue
            for name in candidates(p["info"]):
                fma = names.get(name)
                if fma and fma in files:
                    matched.append((i, fma, name))
                    break
        print(f"{system}: {len(matched)} of {len(parts)} parts have a BodyParts3D name", flush=True)
        if not matched:
            continue

        meshes = {fma: read_obj(files[fma]) for _, fma, _ in matched}
        # One similarity transform for the whole body from the part centres.
        src = np.array([meshes[f][0].mean(0) for _, f, _ in matched])
        dst = np.array([parts[i]["co"].mean(0) for i, _, _ in matched])
        s, r, t = similarity(src, dst)
        for _ in range(2):  # drop parts Z-Anatomy moved (e.g. the arms) and refit
            err = np.linalg.norm((s * (r @ src.T)).T + t - dst, axis=1)
            keep = err < max(np.median(err) * 3, 0.01)
            s, r, t = similarity(src[keep], dst[keep])
        print(f"  global scale {s:.6f}, median centre error {np.median(err) * 1000:.1f} mm", flush=True)

        out_parts = []
        for i, fma, name in matched:
            lod = parts[i]
            co, tris = meshes[fma]
            if len(tris) == 0:
                continue
            co = (s * (r @ co.T)).T + t
            tree = bvh(lod["co"], lod["idx"])
            rng = np.random.default_rng(i)
            sample = co[rng.choice(len(co), min(len(co), 1500), replace=False)]
            # move the centre onto the Z-Anatomy part first (handles moved limbs)
            shift = lod["co"].mean(0) - co.mean(0)
            co += shift; sample = sample + shift
            for _ in range(25):
                target, dist, _ = nearest(tree, sample)
                ok = dist < np.percentile(dist, 90) * 1.5 + 1e-6
                rr, tt = rigid(sample[ok], target[ok])
                sample = (rr @ sample.T).T + tt
                co = (rr @ co.T).T + tt
            hd_tree = bvh(co, tris)
            _, d_hd, _ = nearest(tree, sample)
            lod_sample = lod["co"][rng.choice(len(lod["co"]), min(len(lod["co"]), 1500), replace=False)]
            _, d_lod, _ = nearest(hd_tree, lod_sample)
            size = np.linalg.norm(lod["co"].max(0) - lod["co"].min(0))
            limit = max(0.0015, size * 0.012)
            good = np.mean(d_hd) < limit and np.mean(d_lod) < limit and np.percentile(d_lod, 95) < limit * 4
            gain = len(tris) / max(len(lod["idx"]), 1)
            print(f"  {lod['info']['name']:<44} {name:<40} {len(lod['idx']):>6} -> {len(tris):>6} tris "
                  f"mean {np.mean(d_hd) * 1000:.2f}/{np.mean(d_lod) * 1000:.2f} mm {'ok' if good else 'REJECT'}", flush=True)
            if not good or gain < 1.3:
                continue
            if len(tris) > MAX_TRIS:
                co, tris = decimate(co, tris, MAX_TRIS)
                hd_tree = bvh(co, tris)
            # weld + drop unused vertices
            used = np.unique(tris)
            remap = np.full(len(co), -1); remap[used] = np.arange(len(used))
            co, tris = co[used], remap[tris]
            nrm = vertex_normals(co, tris)
            # face the same way as Z-Anatomy
            _, _, face = nearest(tree, co[:: max(1, len(co) // 800)])
            lod_n = np.cross(*(lod["co"][lod["idx"][face][:, k]] - lod["co"][lod["idx"][face][:, 0]] for k in (1, 2)))
            if np.mean(np.sum(lod_n * nrm[:: max(1, len(co) // 800)], axis=1)) < 0:
                tris = tris[:, ::-1]; nrm = -nrm
            # materials from the nearest Z-Anatomy triangle
            centres = co[tris].mean(1)
            _, _, face = nearest(tree, centres)
            mat = lod["mat"][np.clip(face, 0, len(lod["mat"]) - 1)]
            order = np.argsort(mat, kind="stable")
            tris, mat = tris[order], mat[order]
            cuts = np.flatnonzero(np.diff(mat)) + 1
            starts = np.concatenate([[0], cuts]); ends = np.concatenate([cuts, [len(mat)]])
            info = dict(lod["info"])
            info["seg"] = [[int(mat[a]), int(b - a)] for a, b in zip(starts, ends)]
            info["tris"] = int(len(tris))
            info["bounds"] = [round(float(v), 4) for v in (*co.min(0), *co.max(0))]
            info["lod"] = i
            info["source"] = fma
            out_parts.append((info, co, nrm, tris))

        blob = bytearray(b"ANT1" + struct.pack("<I", len(out_parts)) + struct.pack("<3f", *lo) + struct.pack("<3f", *hi))
        for _, co, _, tris in out_parts:
            blob += struct.pack("<II", len(co), tris.size)
        for _, co, nrm, tris in out_parts:
            blob += np.clip(np.round((co - lo) / (hi - lo) * 65535), 0, 65535).astype("<u2").tobytes()
            blob += np.clip(np.round(nrm * 127), -127, 127).astype("i1").tobytes()
            blob += tris.astype("<u2" if len(co) <= 65535 else "<u4").tobytes()
        comp = zlib.compressobj(9, zlib.DEFLATED, -15)
        open(os.path.join(OUT, f"hd-{system}.bin"), "wb").write(comp.compress(bytes(blob)) + comp.flush())
        json.dump({"system": system, "materials": manifest.get("materials", []), "parts": [p[0] for p in out_parts]},
                  open(os.path.join(OUT, f"hd-{system}.json"), "w"), ensure_ascii=False, separators=(",", ":"))
        before = sum(len(parts[p[0]["lod"]]["idx"]) for p in out_parts)
        after = sum(len(p[3]) for p in out_parts)
        print(f"{system}: {len(out_parts)} high-detail parts, {before} -> {after} triangles", flush=True)


main()
