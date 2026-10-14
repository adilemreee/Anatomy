"""Replaces Z-Anatomy's simplified organs with BodyParts3D meshes and adds
the organs Z-Anatomy does not have (ileum, rectum).

    Blender -b --python tools/build_organs.py -- <bp3d_obj_dir> <parts_list_e.txt> <in_dir> <out_dir> [system ...]

<in_dir> holds plain "ANT1" packs (tools/strip_pack.py) with their manifests;
the edited packs are written to <out_dir> as "ANT1". Run tools/bake_ao.swift
and tools/build_lods.py on them afterwards.

Z-Anatomy remodelled several organs (the liver, stomach, intestines) into
smooth, simplified shapes. BodyParts3D 3.0 (DBCLS, CC BY-SA 2.1 JP) keeps the
shapes segmented from a real body. For each organ in ORGANS this script

  1. fits one similarity transform from BodyParts3D into the app's frame on
     the centres of all named parts of the system,
  2. moves each group of organs rigidly (ICP) onto the Z-Anatomy organs it
     replaces, so the new organs sit exactly where the old ones did,
  3. lightly smooths segmentation steps, caps very dense meshes and
     recomputes normals,
  4. replaces the Z-Anatomy part (keeping its name, hierarchy and material)
     or adds a new part.
"""
import json
import os
import struct
import sys
import zlib

import bmesh
import bpy
import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

ARGS = sys.argv[sys.argv.index("--") + 1:]
OBJ_DIR, PARTS_LIST, IN_DIR, OUT_DIR = ARGS[:4]
SYSTEMS = ARGS[4:] or ["visceral", "lymphoid"]
MAX_TRIS = 90000

# Rigid groups: the BodyParts3D meshes in a group move together onto the
# union of the Z-Anatomy targets. Each source either replaces a Z-Anatomy
# part ("replace") or is added as a new part ("add": name, base, path, material of).
GROUPS = {
    "visceral": [
        {"targets": ["Liver"], "replace": {"liver": "Liver"}, "force": True},
        {"targets": ["Stomach"], "replace": {"stomach": "Stomach"}, "force": True},
        {"targets": ["Pancreas"], "replace": {"pancreas, nsn": "Pancreas"}},
        {"targets": ["Gallbladder"], "replace": {"gallbladder": "Gallbladder"}},
        {"targets": ["Duodenum"], "replace": {"duodenum": "Duodenum"}, "force": True},
        {"targets": ["Oesophagus"], "replace": {"esophagus": "Oesophagus"}},
        {"targets": ["Jejunum"], "replace": {"jejunum": "Jejunum"}, "force": True,
         "add": {"ileum": ("Ileum", "Ileum", ["Visceral systems", "Digestive system", "Digestive canal", "Small intestine"], "Jejunum")}},
        {"targets": ["Ascending colon", "Transverse colon", "Descending colon", "Sigmoid colon", "Vermiform appendix"], "fit": ["colon, nsn", "appendix"],
         "add": {"rectum": ("Rectum", "Rectum", ["Visceral systems", "Digestive system", "Digestive canal", "Large intestine"], "Sigmoid colon")}},
        {"targets": ["Kidney.l"], "replace": {"left kidney": "Kidney.l"}},
        {"targets": ["Kidney.r"], "replace": {"right kidney": "Kidney.r"}},
        {"targets": ["Ureter.l"], "replace": {"left ureter": "Ureter.l"}},
        {"targets": ["Ureter.r"], "replace": {"right ureter": "Ureter.r"}},
        {"targets": ["Urinary bladder"], "replace": {"urinary bladder": "Urinary bladder"}},
        {"targets": ["Suprarenal gland.l"], "replace": {"left adrenal gland": "Suprarenal gland.l"}},
        {"targets": ["Suprarenal gland.r"], "replace": {"right adrenal gland": "Suprarenal gland.r"}},
        {"targets": ["Superior lobe of right lung", "Middle lobe of right lung", "Inferior lobe of right lung"], "transfer": True,
         "replace": {"upper lobe of right lung": "Superior lobe of right lung", "middle lobe of lung": "Middle lobe of right lung",
                     "lower lobe of right lung": "Inferior lobe of right lung"}},
        {"targets": ["Superior lobe of left lung", "Inferior lobe of left lung"], "transfer": True,
         "replace": {"upper lobe of left lung": "Superior lobe of left lung", "lower lobe of left lung": "Inferior lobe of left lung"}},
        {"targets": ["Testis.l"], "replace": {"left testis": "Testis.l"}},
        {"targets": ["Testis.r"], "replace": {"right testis": "Testis.r"}},
        {"targets": ["Epididymis.l"], "replace": {"left epididymis": "Epididymis.l"}},
        {"targets": ["Epididymis.r"], "replace": {"right epididymis": "Epididymis.r"}},
        {"targets": ["Seminal gland.l"], "replace": {"left seminal vesicle": "Seminal gland.l"}},
        {"targets": ["Seminal gland.r"], "replace": {"right seminal vesicle": "Seminal gland.r"}},
        {"targets": ["Prostate"], "replace": {"prostate": "Prostate"}},
    ],
    "lymphoid": [
        {"targets": ["Spleen"], "replace": {"spleen": "Spleen"}, "force": True},
        {"targets": ["Left lobe of thymus", "Right lobe of thymus"],
         "replace": {"left lobe of thymus": "Left lobe of thymus", "right lobe of thymus": "Right lobe of thymus"}},
    ],
}


# --- packs ----------------------------------------------------------------------

def read_pack(system):
    raw = zlib.decompress(open(os.path.join(IN_DIR, f"mesh-{system}.bin"), "rb").read(), -15)
    manifest = json.load(open(os.path.join(IN_DIR, f"mesh-{system}.json")))
    assert raw[:4] == b"ANT1", "strip the pack first (tools/strip_pack.py)"
    count, = struct.unpack_from("<I", raw, 4)
    lo = np.array(struct.unpack_from("<3f", raw, 8)); hi = np.array(struct.unpack_from("<3f", raw, 20))
    cur = 32
    counts = [struct.unpack_from("<II", raw, cur + 8 * i) for i in range(count)]
    cur += 8 * count
    parts = []
    for (nv, ni), info in zip(counts, manifest["parts"]):
        co = np.frombuffer(raw, "<u2", nv * 3, cur).reshape(-1, 3).astype(np.float64) / 65535 * (hi - lo) + lo
        cur += nv * 6
        nrm = np.frombuffer(raw, "i1", nv * 3, cur).reshape(-1, 3).astype(np.float64) / 127
        cur += nv * 3
        wide = nv > 65535
        idx = np.frombuffer(raw, "<u4" if wide else "<u2", ni, cur).astype(np.int64)
        cur += ni * (4 if wide else 2)
        parts.append({"info": info, "co": co, "n": nrm, "idx": idx.reshape(-1, 3)})
    return manifest, parts, lo, hi


def write_pack(system, manifest, parts, lo, hi):
    blob = bytearray(b"ANT1" + struct.pack("<I", len(parts)) + struct.pack("<3f", *lo) + struct.pack("<3f", *hi))
    for p in parts:
        blob += struct.pack("<II", len(p["co"]), p["idx"].size)
    for p in parts:
        blob += np.clip(np.round((p["co"] - lo) / (hi - lo) * 65535), 0, 65535).astype("<u2").tobytes()
        n = p["n"]; ln = np.linalg.norm(n, axis=1, keepdims=True); ln[ln == 0] = 1
        blob += np.clip(np.round(n / ln * 127), -127, 127).astype("i1").tobytes()
        blob += p["idx"].astype("<u2" if len(p["co"]) <= 65535 else "<u4").tobytes()
    comp = zlib.compressobj(9, zlib.DEFLATED, -15)
    open(os.path.join(OUT_DIR, f"mesh-{system}.bin"), "wb").write(comp.compress(bytes(blob)) + comp.flush())
    manifest["parts"] = [p["info"] for p in parts]
    json.dump(manifest, open(os.path.join(OUT_DIR, f"mesh-{system}.json"), "w"), ensure_ascii=False, separators=(",", ":"))


# --- BodyParts3D -----------------------------------------------------------------

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
    return np.array(vs, dtype=np.float64), np.array(fs, dtype=np.int64) - 1


# --- geometry -------------------------------------------------------------------

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


def rigid(src, dst):
    ms, md = src.mean(0), dst.mean(0)
    u, _, vt = np.linalg.svd((dst - md).T @ (src - ms))
    sgn = np.eye(3)
    if np.linalg.det(u @ vt) < 0:
        sgn[2, 2] = -1
    r = u @ sgn @ vt
    return r, md - r @ ms


def bvh(co, tris):
    return BVHTree.FromPolygons([Vector(p) for p in co], [tuple(t) for t in tris])


def nearest(tree, pts):
    out = np.empty_like(pts); dist = np.empty(len(pts))
    for i, p in enumerate(pts):
        loc, _, _, d = tree.find_nearest(Vector(p))
        if loc is None:
            out[i] = p; dist[i] = 1e9
        else:
            out[i] = loc; dist[i] = d
    return out, dist


def facing_ratio(co, nrm, tree):
    """Mean agreement between `nrm` and the face normals of `tree` nearby."""
    step = max(1, len(co) // 600)
    total = 0.0
    for p, n in zip(co[::step], nrm[::step]):
        loc, face_normal, _, _ = tree.find_nearest(Vector(p))
        if loc is not None:
            total += float(np.dot(n, np.array(face_normal)))
    return total


def vertex_normals(co, tris):
    n = np.zeros_like(co)
    fn = np.cross(co[tris[:, 1]] - co[tris[:, 0]], co[tris[:, 2]] - co[tris[:, 0]])
    for k in range(3):
        np.add.at(n, tris[:, k], fn)
    ln = np.linalg.norm(n, axis=1, keepdims=True); ln[ln == 0] = 1
    return n / ln


def blender_cleanup(co, tris, target):
    """Welds, lightly smooths (removes CT segmentation steps) and decimates."""
    me = bpy.data.meshes.new("organ")
    me.from_pydata(co.tolist(), [], tris.tolist())
    ob = bpy.data.objects.new("organ", me)
    bpy.context.scene.collection.objects.link(ob)
    bpy.context.view_layer.objects.active = ob
    weld = ob.modifiers.new("weld", "WELD"); weld.merge_threshold = 0.00005
    smooth = ob.modifiers.new("smooth", "LAPLACIANSMOOTH")
    smooth.iterations = 2; smooth.lambda_factor = 0.35; smooth.use_volume_preserve = True
    if len(tris) > target:
        dec = ob.modifiers.new("dec", "DECIMATE"); dec.ratio = target / len(tris); dec.use_collapse_triangulate = True
    dg = bpy.context.evaluated_depsgraph_get()
    ev = ob.evaluated_get(dg)
    m2 = ev.to_mesh()
    # Segmented meshes can have faces wound either way; make them all point out.
    bm = bmesh.new()
    bm.from_mesh(m2)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bmesh.ops.triangulate(bm, faces=bm.faces)
    bm.verts.index_update()
    c = np.array([v.co[:] for v in bm.verts], dtype=np.float64).reshape(-1)
    t = np.array([[v.index for v in f.verts] for f in bm.faces], dtype=np.int64).reshape(-1)
    bm.free()
    ev.to_mesh_clear()
    bpy.data.objects.remove(ob); bpy.data.meshes.remove(me)
    return c.reshape(-1, 3), t.reshape(-1, 3)


# --- main -------------------------------------------------------------------------

def main():
    names = bp3d_names()
    files = obj_files()
    os.makedirs(OUT_DIR, exist_ok=True)
    print(f"BodyParts3D: {len(names)} names, {len(files)} meshes", flush=True)
    for system in SYSTEMS:
        manifest, parts, lo, hi = read_pack(system)
        by_name = {p["info"]["name"]: i for i, p in enumerate(parts)}
        groups = GROUPS.get(system, [])

        def mesh_for(name):
            fma = names.get(name)
            if not fma or fma not in files:
                print(f"  no BodyParts3D mesh for {name!r}", flush=True)
                return None
            return read_obj(files[fma])

        # Global similarity from every organ we know both ways (part centres).
        pairs = []
        for g in groups:
            for src, dst in g.get("replace", {}).items():
                m = mesh_for(src)
                if m is not None and dst in by_name:
                    pairs.append((m[0].mean(0), parts[by_name[dst]]["co"].mean(0)))
        src_c = np.array([p[0] for p in pairs]); dst_c = np.array([p[1] for p in pairs])
        s, r, t = similarity(src_c, dst_c)
        for _ in range(2):
            err = np.linalg.norm((s * (r @ src_c.T)).T + t - dst_c, axis=1)
            keep = err < max(np.median(err) * 3, 0.01)
            s, r, t = similarity(src_c[keep], dst_c[keep])
        print(f"{system}: {len(pairs)} pairs, scale {s:.6f}, median centre error {np.median(err) * 1000:.1f} mm", flush=True)

        replaced, added = 0, []
        for g in groups:
            targets = [by_name[n] for n in g["targets"] if n in by_name]
            if not targets:
                continue
            sources = {}
            for src in list(g.get("replace", {})) + list(g.get("add", {})) + g.get("fit", []):
                if src in sources:
                    continue
                m = mesh_for(src)
                if m is not None and len(m[1]):
                    sources[src] = ((s * (r @ m[0].T)).T + t, m[1])
            if not sources:
                continue
            # ICP of the union of the fitting sources onto the union of the targets.
            fit = g.get("fit") or list(g.get("replace", {}))
            fit_pts = np.concatenate([sources[f][0] for f in fit if f in sources])
            tgt_co = np.concatenate([parts[i]["co"] for i in targets])
            offs = np.cumsum([0] + [len(parts[i]["co"]) for i in targets])
            tgt_tris = np.concatenate([parts[i]["idx"] + offs[k] for k, i in enumerate(targets)])
            tree = bvh(tgt_co, tgt_tris)
            rng = np.random.default_rng(len(fit_pts))
            sample = fit_pts[rng.choice(len(fit_pts), min(len(fit_pts), 2500), replace=False)]
            shift = tgt_co.mean(0) - fit_pts.mean(0)
            R, T = np.eye(3), shift
            sample = sample + shift
            for _ in range(30):
                target_pts, dist = nearest(tree, sample)
                ok = dist < np.percentile(dist, 85) * 1.5 + 1e-6
                rr, tt = rigid(sample[ok], target_pts[ok])
                sample = (rr @ sample.T).T + tt
                R, T = rr @ R, rr @ T + tt
            _, dist = nearest(tree, sample)
            size = np.linalg.norm(tgt_co.max(0) - tgt_co.min(0))
            print(f"  group {g['targets'][0]!r}: mean {np.mean(dist) * 1000:.1f} mm, 90% {np.percentile(dist, 90) * 1000:.1f} mm "
                  f"(size {size * 1000:.0f} mm)", flush=True)
            if np.mean(dist) > max(0.006, min(size * 0.05, 0.012)) and not (g.get("force") and np.mean(dist) < 0.012):
                print("    REJECTED: too far from the Z-Anatomy organ", flush=True)
                continue

            def place(src):
                co, tris = sources[src]
                co = (R @ co.T).T + T
                co, tris = blender_cleanup(co, tris, MAX_TRIS)
                used = np.unique(tris)
                remap = np.full(len(co), -1); remap[used] = np.arange(len(used))
                co, tris = co[used], remap[tris]
                return co, tris

            for src, dst in g.get("replace", {}).items():
                if src not in sources or dst not in by_name:
                    continue
                part = parts[by_name[dst]]
                co, tris = place(src)
                if not g.get("force") and len(tris) < len(part["idx"]) * 1.2:
                    print(f"    {dst:<34} kept (BodyParts3D {len(tris)} vs {len(part['idx'])} tris)", flush=True)
                    continue
                nrm = vertex_normals(co, tris)
                # Keep the outward orientation of the Z-Anatomy part: compare
                # with the face normals of the nearest old triangles.
                if facing_ratio(co, nrm, bvh(part["co"], part["idx"])) < 0:
                    tris = tris[:, ::-1]; nrm = -nrm
                info = dict(part["info"])
                mats = [m for m, _ in (info.get("seg") or [[0, 0]])]
                dominant = max(info.get("seg") or [[0, 1]], key=lambda x: x[1])[0] if info.get("seg") else 0
                if g.get("transfer") and len(mats) > 1:
                    # Material regions (bronchopulmonary segments) from the
                    # nearest Z-Anatomy triangle; triangles sorted by material.
                    old_mat = np.concatenate([np.full(n, m) for m, n in info["seg"]])
                    old_tree = bvh(part["co"], part["idx"])
                    centres = co[tris].mean(1)
                    mat = np.empty(len(tris), dtype=np.int64)
                    for k, c in enumerate(centres):
                        _, _, face, _ = old_tree.find_nearest(Vector(c))
                        mat[k] = old_mat[min(max(face if face is not None else 0, 0), len(old_mat) - 1)]
                    order = np.argsort(mat, kind="stable")
                    tris, mat = tris[order], mat[order]
                    cuts = np.flatnonzero(np.diff(mat)) + 1
                    starts = np.concatenate([[0], cuts]); ends = np.concatenate([cuts, [len(mat)]])
                    info["seg"] = [[int(mat[a]), int(b - a)] for a, b in zip(starts, ends)]
                    nrm = vertex_normals(co, tris)
                    dominant = "transferred"
                else:
                    # The organ keeps its dominant material for the whole surface.
                    info["seg"] = [[int(dominant), int(len(tris))]]
                info["tris"] = int(len(tris))
                info["bounds"] = [round(float(v), 4) for v in (*co.min(0), *co.max(0))]
                info["source"] = "BodyParts3D " + names.get(src, "")
                parts[by_name[dst]] = {"info": info, "co": co, "n": nrm, "idx": tris}
                replaced += 1
                print(f"    {dst:<34} {len(part['idx']):>6} -> {len(tris):>6} tris (materials {mats} -> {dominant})", flush=True)
            for src, (name, base, path, like) in g.get("add", {}).items():
                if src not in sources:
                    continue
                co, tris = place(src)
                nrm = vertex_normals(co, tris)
                ref = parts[by_name[like]]["info"] if like in by_name else {}
                dominant = max(ref.get("seg") or [[0, 1]], key=lambda x: x[1])[0] if ref.get("seg") else 0
                info = {"name": name, "base": base, "path": path, "tris": int(len(tris)),
                        "bounds": [round(float(v), 4) for v in (*co.min(0), *co.max(0))],
                        "seg": [[int(dominant), int(len(tris))]], "source": "BodyParts3D " + names.get(src, "")}
                if ref.get("color"):
                    info["color"] = ref["color"]
                added.append({"info": info, "co": co, "n": nrm, "idx": tris})
                print(f"    + {name:<32} {len(tris):>6} tris", flush=True)
        parts += added
        # Keep everything inside the shared quantisation box.
        for p in parts:
            p["co"] = np.clip(p["co"], lo, hi)
        write_pack(system, manifest, parts, lo, hi)
        print(f"{system}: {replaced} organs replaced, {len(added)} added", flush=True)


main()
