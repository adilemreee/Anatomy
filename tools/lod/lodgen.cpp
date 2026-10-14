// Adds simplified levels of detail to the atlas mesh packs.
//
//   clang++ -std=c++17 -O2 tools/lod/lodgen.cpp <meshoptimizer>/src/*.cpp -I<meshoptimizer>/src -lz -o lodgen
//   ./lodgen mesh-muscular.bin mesh-muscular.seg [more bin/seg pairs ...]
//
// Normally run through tools/build_lods.py, which writes the .seg files
// (one line per part: the triangle count of each material run, from the
// manifest's "seg") and calls this tool on every pack.
//
// Reads an "ANT2" pack (or an "ANT3" one, whose level of detail block is
// dropped and rebuilt), reorders every material run for the post-transform
// vertex cache, and writes "ANT3": the ANT2 layout followed by
//
//     "LODS" u32 levelCount
//     for each level 1...levelCount, for each part: f32 error (metres), u32 indexCount
//     for each level, for each part: indexCount indices (u16, or u32 when the
//         part has more than 65535 vertices), local to the part
//
// The simplified levels reuse the part's own vertices, so the app only
// uploads extra indices. An index count of 0 means "same as the level
// above". Each material run is simplified on its own with its border
// locked, so material seams (tendon / belly, cartilage / bone) stay closed.

#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <zlib.h>

#include "meshoptimizer.h"

namespace {

struct Level {
    float targetRatio;
    float maxError;  // metres
};

// Level 1 for mid-distance views, level 2 for the whole body on a phone.
const Level kLevels[] = {
    {0.30f, 0.0010f},
    {0.08f, 0.0040f},
};

std::vector<uint8_t> readFile(const char* path) {
    std::ifstream in(path, std::ios::binary);
    return std::vector<uint8_t>((std::istreambuf_iterator<char>(in)), std::istreambuf_iterator<char>());
}

std::vector<uint8_t> inflateRaw(const std::vector<uint8_t>& src) {
    z_stream s{};
    inflateInit2(&s, -15);
    s.next_in = const_cast<Bytef*>(src.data());
    s.avail_in = static_cast<uInt>(src.size());
    std::vector<uint8_t> out;
    uint8_t buf[1 << 16];
    int rc;
    do {
        s.next_out = buf;
        s.avail_out = sizeof(buf);
        rc = inflate(&s, Z_NO_FLUSH);
        out.insert(out.end(), buf, buf + (sizeof(buf) - s.avail_out));
    } while (rc == Z_OK);
    inflateEnd(&s);
    if (rc != Z_STREAM_END) {
        fprintf(stderr, "inflate failed (%d)\n", rc);
        exit(1);
    }
    return out;
}

std::vector<uint8_t> deflateRaw(const std::vector<uint8_t>& src) {
    z_stream s{};
    deflateInit2(&s, 9, Z_DEFLATED, -15, 9, Z_DEFAULT_STRATEGY);
    s.next_in = const_cast<Bytef*>(src.data());
    s.avail_in = static_cast<uInt>(src.size());
    std::vector<uint8_t> out(deflateBound(&s, static_cast<uLong>(src.size())));
    s.next_out = out.data();
    s.avail_out = static_cast<uInt>(out.size());
    deflate(&s, Z_FINISH);
    out.resize(out.size() - s.avail_out);
    deflateEnd(&s);
    return out;
}

template <typename T> T load(const std::vector<uint8_t>& d, size_t o) {
    T v;
    memcpy(&v, d.data() + o, sizeof(T));
    return v;
}

template <typename T> void put(std::vector<uint8_t>& d, T v) {
    const uint8_t* p = reinterpret_cast<const uint8_t*>(&v);
    d.insert(d.end(), p, p + sizeof(T));
}

struct Part {
    uint32_t vertexCount = 0, indexCount = 0;
    size_t positionOffset = 0, indexOffset = 0;
    std::vector<uint32_t> indices;           // level 0, rewritten in cache order
    std::vector<float> positions;            // dequantised
    std::vector<std::vector<uint32_t>> lods; // per level
    std::vector<float> errors;
    bool wide() const { return vertexCount > 65535; }
};

std::vector<std::vector<int>> readSegments(const char* path) {
    std::vector<std::vector<int>> out;
    std::ifstream in(path);
    std::string line;
    while (std::getline(in, line)) {
        std::istringstream ss(line);
        std::vector<int> runs;
        int n;
        while (ss >> n) runs.push_back(n);
        out.push_back(runs);
    }
    return out;
}

void process(const char* binPath, const char* segPath) {
    std::vector<uint8_t> raw = inflateRaw(readFile(binPath));
    if (raw.size() < 32 || raw[0] != 'A' || raw[1] != 'N' || raw[2] != 'T' || (raw[3] != '2' && raw[3] != '3')) {
        fprintf(stderr, "%s: expected an ANT2/ANT3 pack (run bake_ao first)\n", binPath);
        exit(1);
    }
    uint32_t count = load<uint32_t>(raw, 4);
    float lo[3], hi[3];
    for (int k = 0; k < 3; k++) {
        lo[k] = load<float>(raw, 8 + 4 * k);
        hi[k] = load<float>(raw, 20 + 4 * k);
    }
    std::vector<std::vector<int>> segments = readSegments(segPath);
    if (segments.size() != count) {
        fprintf(stderr, "%s: %zu segment lines for %u parts\n", segPath, segments.size(), count);
        exit(1);
    }

    std::vector<Part> parts(count);
    size_t cursor = 32;
    for (uint32_t i = 0; i < count; i++) {
        parts[i].vertexCount = load<uint32_t>(raw, cursor);
        parts[i].indexCount = load<uint32_t>(raw, cursor + 4);
        cursor += 8;
    }
    for (auto& p : parts) {
        p.positionOffset = cursor;
        cursor += size_t(p.vertexCount) * 6 + size_t(p.vertexCount) * 3;
        p.indexOffset = cursor;
        cursor += size_t(p.indexCount) * (p.wide() ? 4 : 2);
        cursor += p.vertexCount; // baked occlusion
    }
    const size_t bodyEnd = cursor;

    size_t before = 0, after[2] = {0, 0};
    for (uint32_t pi = 0; pi < count; pi++) {
        Part& p = parts[pi];
        p.positions.resize(size_t(p.vertexCount) * 3);
        for (uint32_t v = 0; v < p.vertexCount; v++)
            for (int k = 0; k < 3; k++) {
                float q = load<uint16_t>(raw, p.positionOffset + (size_t(v) * 3 + k) * 2);
                p.positions[size_t(v) * 3 + k] = lo[k] + q / 65535.0f * (hi[k] - lo[k]);
            }
        p.indices.resize(p.indexCount);
        for (uint32_t i = 0; i < p.indexCount; i++)
            p.indices[i] = p.wide() ? load<uint32_t>(raw, p.indexOffset + size_t(i) * 4)
                                    : load<uint16_t>(raw, p.indexOffset + size_t(i) * 2);
        before += p.indexCount / 3;

        // Material runs, in triangles; fall back to one run for the whole part.
        std::vector<int> runs = segments[pi];
        size_t total = 0;
        for (int r : runs) total += size_t(r);
        if (runs.empty() || total * 3 != p.indexCount) runs = {int(p.indexCount / 3)};

        // Level 0 in vertex cache order, run by run.
        size_t start = 0;
        for (int r : runs) {
            size_t n = size_t(r) * 3;
            if (n > 0) meshopt_optimizeVertexCache(&p.indices[start], &p.indices[start], n, p.vertexCount);
            start += n;
        }

        std::vector<uint32_t> previous = p.indices;
        for (int level = 0; level < 2; level++) {
            std::vector<uint32_t> out;
            float worst = 0;
            size_t runStart = 0;
            for (int r : runs) {
                size_t n = size_t(r) * 3;
                if (n == 0) continue;
                const uint32_t* src = &p.indices[runStart];
                runStart += n;
                if (r < 24) { // too small to be worth it
                    out.insert(out.end(), src, src + n);
                    continue;
                }
                size_t target = std::max<size_t>(3, size_t(double(r) * kLevels[level].targetRatio) * 3);
                std::vector<uint32_t> dst(n);
                float error = 0;
                size_t m = meshopt_simplify(dst.data(), src, n, p.positions.data(), p.vertexCount, 12, target,
                                            kLevels[level].maxError,
                                            meshopt_SimplifyLockBorder | meshopt_SimplifyErrorAbsolute | meshopt_SimplifySparse,
                                            &error);
                if (m == 0) { // keep something on screen
                    out.insert(out.end(), src, src + n);
                    continue;
                }
                dst.resize(m);
                meshopt_optimizeVertexCache(dst.data(), dst.data(), m, p.vertexCount);
                out.insert(out.end(), dst.begin(), dst.end());
                worst = std::max(worst, error);
            }
            // Not worth a separate level: reuse the one above.
            if (out.size() > previous.size() * 85 / 100) {
                p.lods.push_back({});
                p.errors.push_back(level == 0 ? 0.0f : p.errors.back());
                after[level] += previous.size() / 3;
            } else {
                p.lods.push_back(out);
                p.errors.push_back(worst);
                after[level] += out.size() / 3;
                previous = out;
            }
        }
    }

    // Rewrite: ANT3 = ANT2 body with level 0 reordered + LOD block.
    std::vector<uint8_t> outData(raw.begin(), raw.begin() + bodyEnd);
    outData[3] = '3';
    for (const Part& p : parts)
        for (uint32_t i = 0; i < p.indexCount; i++) {
            if (p.wide()) memcpy(&outData[p.indexOffset + size_t(i) * 4], &p.indices[i], 4);
            else {
                uint16_t v = uint16_t(p.indices[i]);
                memcpy(&outData[p.indexOffset + size_t(i) * 2], &v, 2);
            }
        }
    outData.insert(outData.end(), {'L', 'O', 'D', 'S'});
    put<uint32_t>(outData, 2);
    for (int level = 0; level < 2; level++)
        for (const Part& p : parts) {
            put<float>(outData, p.errors[level]);
            put<uint32_t>(outData, uint32_t(p.lods[level].size()));
        }
    for (int level = 0; level < 2; level++)
        for (const Part& p : parts)
            for (uint32_t v : p.lods[level]) {
                if (p.wide()) put<uint32_t>(outData, v);
                else put<uint16_t>(outData, uint16_t(v));
            }

    std::vector<uint8_t> packed = deflateRaw(outData);
    std::ofstream(binPath, std::ios::binary).write(reinterpret_cast<const char*>(packed.data()), std::streamsize(packed.size()));
    printf("%s: %u parts, %zu tris -> LOD1 %zu (%.0f%%), LOD2 %zu (%.0f%%), %.1f MB\n", binPath, count, before,
           after[0], 100.0 * after[0] / std::max<size_t>(before, 1), after[1], 100.0 * after[1] / std::max<size_t>(before, 1),
           packed.size() / 1e6);
}

} // namespace

int main(int argc, char** argv) {
    if (argc < 3 || (argc - 1) % 2 != 0) {
        fprintf(stderr, "usage: lodgen <pack.bin> <pack.seg> [...]\n");
        return 1;
    }
    for (int i = 1; i + 1 < argc; i += 2) process(argv[i], argv[i + 1]);
    return 0;
}
