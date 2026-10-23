//
//  AnatomyShaders.metal
//  Anatomy
//
//  Surface shader for every anatomical part. Per-vertex inputs written by
//  VertexBuilder:
//    color.rgb  linear base colour        color.a  baked ambient occlusion
//    tangent    fibre direction projected onto the surface (normal frame)
//    uv1.x      fibre strength (0 none, 1 muscle belly)
//    uv1.y      wetness (0 dry bone … 1 glossy serosa)
//    uv2.xyz    the part's constant fibre axis (drives the streak pattern)
//    uv2.w      surface code / 127: pattern * 16 + tissue
//               pattern 0 plain, 1 muscle fibres, 2 bone, 3 organ
//               tissue  see `Tissue` in MaterialStyle.swift
//  custom_parameter: x = mode (0 solid, 1 ghost, 2 selected, 3 highlighted,
//                    4 specimen highlight patch: colour = glow, alpha = strength),
//                    y = occlusion strength, z = rim strength (ghost: glass strength).
//  custom texture (DetailTexture.swift), tiling, linear, mipmapped:
//    r  broad mottling (fbm)     g  fine isotropic grain     b  cell borders
//
//  All surface detail comes from that one texture: a triplanar lookup
//  (three samples) for every tissue and two more along the fibres of
//  muscles. Mipmapping keeps distant detail from shimmering.
//

#include <metal_stdlib>
#include <RealityKit/RealityKit.h>

using namespace metal;

namespace {

constexpr sampler detailSampler(filter::linear, mip_filter::linear, address::repeat, max_anisotropy(4));
constexpr sampler skinSampler(filter::linear, mip_filter::linear, address::clamp_to_edge, max_anisotropy(8));

/// Detail tile size: one repeat every 10 cm.
constant float kTileScale = 10.0;

enum Tissue : int {
    generic = 0, liver = 1, lung = 2, kidney = 3, spleen = 4, stomach = 5, intestine = 6,
    gland = 7, heart = 8, vessel = 9, brain = 10, hollow = 11, fat = 12, cartilage = 13, nerve = 14, skin = 15,
};

/// Detail texture sampled on the three axis planes, blended by the normal.
half4 triplanar(texture2d<half> tex, float3 p, float3 n, float scale = 1.0) {
    float3 w = pow(abs(n), 4.0);
    w /= max(w.x + w.y + w.z, 1e-4);
    float3 q = p * kTileScale * scale;
    half4 x = tex.sample(detailSampler, q.zy);
    half4 y = tex.sample(detailSampler, q.xz + 0.37);
    half4 z = tex.sample(detailSampler, q.xy + 0.71);
    return x * half(w.x) + y * half(w.y) + z * half(w.z);
}

/// Surface relief from one channel of the detail texture at `scale`: the
/// tangent-space normal of a height field, by finite differences.
float3 reliefNormal(texture2d<half> tex, float3 p, float3 n, float3 t, float scale, int channel, float strength) {
    float3 b = normalize(cross(n, t));
    float e = 0.0004 / scale;
    float h0 = float(triplanar(tex, p, n, scale)[channel]);
    float h1 = float(triplanar(tex, p + t * e, n, scale)[channel]);
    float h2 = float(triplanar(tex, p + b * e, n, scale)[channel]);
    return normalize(float3(-(h1 - h0) * strength, -(h2 - h0) * strength, 1.0));
}

} // namespace

[[visible]]
void anatomySurface(realitykit::surface_parameters params)
{
    auto geometry = params.geometry();
    auto surface = params.surface();
    float4 custom = params.uniforms().custom_parameter();
    int mode = int(custom.x + 0.5);
    float occlusionStrength = custom.y;
    float rimStrength = custom.z;
    // Lighter surface detail for smaller GPUs: the skin's relief comes from the
    // one detail lookup every surface makes instead of three more.
    bool lite = custom.w > 0.5;

    float4 vertexColor = geometry.color();
    float3 base = vertexColor.rgb;
    float occlusion = vertexColor.a;
    float2 extra = geometry.uv1();
    float fibreStrength = extra.x;
    float wetness = extra.y;

    float3 normal = normalize(geometry.normal());
    float3 view = normalize(geometry.view_direction());
    float facing = saturate(dot(normal, view));
    float fresnel = pow(1.0 - facing, 3.0);

    float4 patternData = geometry.uv2();
    int code = int(patternData.w * 127.0 + 0.5);
    int pattern = code / 16;
    int tissue = code % 16;
    float3 p = geometry.model_position();

    // Textured skin (MakeHuman atlas): the texture is the base colour.
    float2 skinUV = geometry.uv0();
    bool textured = skinUV.x + skinUV.y > 0.0;
    if (textured) {
        base = float3(params.textures().base_color().sample(skinSampler, skinUV).rgb);
    }

    float3 tangentNormal = float3(0, 0, 1);
    float roughness = mix(0.82, 0.42, wetness);
    float specular = mix(0.2, 0.45, wetness);
    float clearcoat = 0.0;
    float clearcoatRoughness = 0.3;

    // See-through and selected parts skip the detail work.
    bool detailed = mode == 0;
    if (detailed) {
        texture2d<half> tex = params.textures().custom();
        float4 d = float4(triplanar(tex, p, normal));
        float mottle = d.r;
        float grain = d.g;
        float cells = d.b;

        if (pattern == 2) {
            // Bone: ivory cortex with broad mottling, sparse fine pores and
            // brownish staining in deep recesses, like a dry specimen.
            float pores = smoothstep(0.72, 0.9, grain);
            base *= 0.86 + 0.26 * mottle - 0.14 * pores;
            float stain = saturate((1.0 - occlusion) * 1.4 + (0.5 - mottle) * 0.3);
            base = mix(base, base * float3(0.74, 0.62, 0.46), stain * 0.6);
            roughness = 0.78 - 0.1 * mottle;
        } else if (pattern == 1 && fibreStrength > 0.01) {
            // Muscle: fascicles along the part's axis, sampled in a frame
            // across the axis so the streaks run with the fibres.
            float3 axis = normalize(patternData.xyz);
            float3 b1 = normalize(cross(axis, abs(axis.y) < 0.9 ? float3(0, 1, 0) : float3(1, 0, 0)));
            float3 b2 = cross(axis, b1);
            float along = dot(p, axis);
            float2 uv = float2(dot(p, b1), dot(p, b2)) * kTileScale + float2(along * 0.6, along * 0.25);
            float3 across = normalize(cross(normal, normalize(geometry.tangent())));
            float3 pAcross = p + across * 0.0007;
            float2 uv2 = float2(dot(pAcross, b1), dot(pAcross, b2)) * kTileScale + float2(along * 0.6, along * 0.25);
            float f = float(tex.sample(detailSampler, uv).g);
            float f2 = float(tex.sample(detailSampler, uv2).g);
            float slope = (f2 - f) * 2.2;
            tangentNormal = normalize(float3(0, -slope * fibreStrength, 1));
            // Grooves between bundles are darker, bundle tops slightly lighter.
            base *= mix(1.0, 0.72 + 0.46 * f, fibreStrength) * (0.94 + 0.12 * mottle);
            if (tissue == heart) {
                clearcoat = 0.55;
                clearcoatRoughness = 0.22;
            } else {
                clearcoat = 0.18;
                clearcoatRoughness = 0.38;
            }
        } else {
            switch (tissue) {
            case liver:
                // Smooth capsule over faintly visible lobules.
                base *= (0.9 + 0.16 * mottle) * (1.0 - 0.05 * cells);
                roughness = 0.64; specular = 0.26;
                clearcoat = 0.38; clearcoatRoughness = 0.3;
                break;
            case lung:
                // Pink parenchyma with darker interlobular lines and specks.
                base *= (0.9 + 0.18 * mottle) * (1.0 - 0.1 * cells * (0.4 + mottle));
                base = mix(base, float3(0.2, 0.17, 0.18), smoothstep(0.84, 0.96, grain) * 0.3);
                roughness = 0.66; specular = 0.26;
                clearcoat = 0.45; clearcoatRoughness = 0.26;
                break;
            case kidney:
            case spleen:
                base *= 0.9 + 0.16 * mottle;
                roughness = 0.6; specular = 0.28;
                clearcoat = 0.42; clearcoatRoughness = 0.26;
                break;
            case stomach:
            case intestine:
                // Serosa over muscle: soft mottling and a faint vascular blush.
                base *= 0.88 + 0.2 * mottle;
                base = mix(base, base * float3(1.08, 0.86, 0.86), smoothstep(0.55, 0.8, grain) * 0.25);
                roughness = 0.58; specular = 0.3;
                clearcoat = 0.45; clearcoatRoughness = 0.26;
                break;
            case gland:
                // Lobulated glands: pancreas, salivary, thyroid, adrenal.
                base *= (0.88 + 0.18 * mottle) * (1.0 - 0.2 * cells);
                tangentNormal = normalize(float3((cells - 0.5) * 0.25, (mottle - 0.5) * 0.25, 1));
                roughness = 0.6; specular = 0.3;
                clearcoat = 0.45; clearcoatRoughness = 0.3;
                break;
            case vessel:
                base *= 0.94 + 0.1 * mottle;
                roughness = 0.45; specular = 0.4;
                clearcoat = 0.6; clearcoatRoughness = 0.18;
                break;
            case brain:
                base *= 0.92 + 0.14 * mottle;
                roughness = 0.58; specular = 0.32;
                clearcoat = 0.55; clearcoatRoughness = 0.25;
                break;
            case hollow:
                base *= 0.94 + 0.1 * mottle;
                roughness = 0.52; specular = 0.34;
                clearcoat = 0.55; clearcoatRoughness = 0.2;
                break;
            case fat:
                // Lobules of fat bulging between thin, pale fibrous septa.
                base *= 0.92 + 0.14 * mottle;
                base = mix(base, float3(0.86, 0.83, 0.76), smoothstep(0.55, 0.92, cells) * 0.75);
                tangentNormal = normalize(float3((cells - 0.5) * 0.35, (mottle - 0.5) * 0.2, 1));
                roughness = 0.5; specular = 0.35;
                clearcoat = 0.5; clearcoatRoughness = 0.25;
                break;
            case cartilage:
                base *= 0.96 + 0.08 * mottle;
                roughness = 0.4; specular = 0.45;
                clearcoat = 0.6; clearcoatRoughness = 0.15;
                break;
            case nerve: {
                float3 axis = normalize(patternData.xyz);
                float3 b1 = normalize(cross(axis, abs(axis.y) < 0.9 ? float3(0, 1, 0) : float3(1, 0, 0)));
                float2 uv = float2(dot(p, b1), dot(p, cross(axis, b1))) * kTileScale * 2.0 + dot(p, axis) * 0.4;
                float f = float(tex.sample(detailSampler, uv).g);
                base *= 0.9 + 0.2 * f;
                roughness = 0.55; specular = 0.35;
                clearcoat = 0.35; clearcoatRoughness = 0.3;
                break;
            }
            case skin: {
                // Pores and fine creases as relief, soft colour blotches, a
                // faint oily sheen.
                float3 t = normalize(geometry.tangent());
                base *= 0.96 + 0.07 * mottle;
                base = mix(base, base * float3(1.06, 0.93, 0.92), smoothstep(0.55, 0.85, mottle) * 0.35);
                float3 liteRelief = normalize(float3((grain - 0.5) * 0.12, (mottle - 0.5) * 0.12, 1));
                if (pattern == 4) {
                    // Shaved scalp: a soft grey shadow of fine stubble; the
                    // density (wetness channel) fades it out at the hairline.
                    // The skin texture already carries a light stubble.
                    float density = saturate(wetness * 3.0) * (textured ? 0.35 : 1.0);
                    float stubble = lite ? grain : float(triplanar(tex, p, normal, 14.0).g);
                    float dots = smoothstep(0.62, 0.9, stubble);
                    base = mix(base, base * float3(0.8, 0.76, 0.74), (0.32 + 0.12 * mottle) * density);
                    base = mix(base, float3(0.12, 0.09, 0.075), dots * 0.38 * density);
                    tangentNormal = lite ? liteRelief : reliefNormal(tex, p, normal, t, 14.0, 1, 0.25);
                    roughness = 0.66; specular = 0.26; clearcoat = 0.04;
                } else if (pattern == 5) {
                    // Scrotal skin: fine rugae.
                    tangentNormal = lite ? liteRelief : reliefNormal(tex, p, normal, t, 4.0, 1, 0.5);
                    base *= 0.95 + 0.07 * (lite ? grain : float(triplanar(tex, p, normal, 4.0).g));
                    roughness = 0.55; specular = 0.3; clearcoat = 0.12; clearcoatRoughness = 0.35;
                } else {
                    tangentNormal = lite ? liteRelief : reliefNormal(tex, p, normal, t, 3.5, 1, 0.35);
                    roughness = 0.58 - 0.08 * mottle; specular = 0.32;
                    clearcoat = 0.12; clearcoatRoughness = 0.42;
                }
                break;
            }
            default:
                if (pattern == 3) {
                    base *= 0.9 + 0.16 * mottle;
                    clearcoat = 0.5; clearcoatRoughness = 0.25;
                } else {
                    base *= 0.95 + 0.1 * mottle;
                }
                break;
            }
        }
    }

    // Baked occlusion darkens creases between structures.
    float ao = mix(1.0, occlusion, occlusionStrength);
    base *= mix(0.45, 1.0, ao);

    float3 emissive = float3(0);
    float opacity = 1.0;

    if (mode == 4) {
        // Highlight patch in the specimen viewer: vertex colour is the glow,
        // its alpha fades the patch out towards the edge.
        float pulse = 0.5 + 0.5 * sin(params.uniforms().time() * 3.0);
        float strength = vertexColor.a;
        base = vertexColor.rgb;
        // Lit like a surface so the shape stays readable, with a soft pulse.
        emissive = base * (0.22 + 0.22 * pulse) + base * fresnel * 0.35;
        opacity = strength * (0.72 + 0.16 * pulse);
        roughness = 0.4;
        clearcoat = 0.3;
    } else if (mode == 2 || mode == 3) {
        float pulse = 0.5 + 0.5 * sin(params.uniforms().time() * 3.2);
        float3 glow = mode == 2 ? float3(0.12, 0.66, 1.0) : float3(1.0, 0.70, 0.12);
        base = mix(base, glow, 0.5);
        emissive = glow * (0.16 + 0.18 * pulse) + glow * fresnel * 0.6;
        roughness = 0.4;
        clearcoat = 0.4;
    } else if (mode == 1) {
        // X-ray glass: faint in the middle, brighter towards the silhouette.
        opacity = (0.05 + 0.4 * fresnel) * rimStrength;
        emissive = base * fresnel * 0.25 * rimStrength;
        clearcoat = 0;
    } else {
        // A cool rim light separates the figure from the background.
        // Skin keeps only a trace of it: a blue sheen reads as bruising there
        // (and outlines the untextured genital skin against the body).
        emissive = float3(0.5, 0.66, 0.95) * fresnel * rimStrength * ao * 0.8 * (textured || tissue == skin ? 0.3 : 1.0);
    }

    surface.set_base_color(half3(base));
    surface.set_normal(tangentNormal);
    surface.set_roughness(half(roughness));
    surface.set_metallic(half(0));
    surface.set_specular(half(specular));
    surface.set_clearcoat(half(clearcoat * ao));
    surface.set_clearcoat_roughness(half(clearcoatRoughness));
    surface.set_ambient_occlusion(half(ao));
    surface.set_emissive_color(half3(emissive));
    surface.set_opacity(half(opacity));
}
