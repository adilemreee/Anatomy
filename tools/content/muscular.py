from common import write
import muscular_trunk
import muscular_limbs
import muscular_detail_axial
import muscular_detail_limbs

groups = muscular_trunk.entries + muscular_limbs.entries
parents = {e["id"]: (e["group"], e["region"]) for e in groups}
detail = muscular_detail_axial.build(muscular_detail_axial.specs + muscular_detail_limbs.specs, parents)
# each group entry lists its muscles among the related structures
for e in groups:
    children = [d["id"] for d in detail if e["id"] in d["related"][:1]]
    e["related"] += [c for c in children if c not in e["related"]]
# the most specific entry owns a 3D part (AtlasStore), so the order is free
write("muscular", groups + detail)
