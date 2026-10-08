//
//  AnatomyShaders.metal
//  Anatomy
//
//  Surface shader for every anatomical part. Per-vertex inputs written by
//  AnatomyScene:
//    color.rgb  linear base colour        color.a  baked ambient occlusion
//    tangent    fibre direction projected onto the surface (normal frame)
//    uv1.x      fibre strength (0 none, 1 muscle belly)
//    uv1.y      wetness (0 dry bone … 1 glossy tendon)
//    uv2.xyz    the part's constant fibre axis (drives the streak pattern)
//    uv2.w      surface pattern: 0 plain, 1 muscle fibres, 2 bone, 3 organ
//  custom_parameter: x = mode (0 solid, 1 ghost, 2 selected, 3 highlighted),
//                    y = occlusion strength, z = rim strength.
//

#include <metal_stdlib>
#include <RealityKit/RealityKit.h>

using namespace metal;

namespace {

float hash31(float3 p) {
    p = fract(p * 0.1031);
    p += dot(p, p.zyx + 31.32);
    return fract((p.x + p.y) * p.z);
}

float valueNoise(float3 p) {
    float3 i = floor(p);
    float3 f = fract(p);
    float3 u = f * f * (3.0 - 2.0 * f);
    float n000 = hash31(i);
    float n100 = hash31(i + float3(1, 0, 0));
    float n010 = hash31(i + float3(0, 1, 0));
    float n110 = hash31(i + float3(1, 1, 0));
    float n001 = hash31(i + float3(0, 0, 1));
    float n101 = hash31(i + float3(1, 0, 1));
    float n011 = hash31(i + float3(0, 1, 1));
    float n111 = hash31(i + float3(1, 1, 1));
    float x00 = mix(n000, n100, u.x);
    float x10 = mix(n010, n110, u.x);
    float x01 = mix(n001, n101, u.x);
    float x11 = mix(n011, n111, u.x);
    return mix(mix(x00, x10, u.y), mix(x01, x11, u.y), u.z);
}

/// Streaks that run along `axis`: the noise is sampled across the fibre
/// direction at high frequency and along it at low frequency.
float fibres(float3 p, float3 axis) {
    float along = dot(p, axis);
    float3 across = p - axis * along;
    // ~3 mm bundles stretched ~25x along the fibres, with finer strands on top.
    float a = valueNoise(across * 330.0 + axis * along * 12.0);
    float b = valueNoise(across * 760.0 + axis * along * 24.0 + 13.1);
    float c = valueNoise(across * 90.0 + axis * along * 4.0 + 7.7);
    return a * 0.5 + b * 0.3 + c * 0.2;
}

float fbm(float3 p) {
    return valueNoise(p) * 0.55 + valueNoise(p * 2.03 + 5.2) * 0.3 + valueNoise(p * 4.01 + 9.7) * 0.15;
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
    int pattern = int(patternData.w + 0.5);
    float3 p = geometry.model_position();

    // Muscle fibres: colour streaks plus a bump across the fibres.
    float3 tangentNormal = float3(0, 0, 1);
    if (pattern == 2) {
        // Bone: ivory cortex with broad mottling, sparse fine pores and
        // brownish staining in deep recesses, like a dry specimen.
        float m = fbm(p * 28.0);
        float spots = fbm(p * 160.0);
        float pores = smoothstep(0.86, 0.96, valueNoise(p * 1100.0));
        base *= 0.86 + 0.24 * m + 0.06 * spots - 0.16 * pores;
        float stain = saturate((1.0 - occlusion) * 1.4 + (0.5 - m) * 0.25);
        base = mix(base, base * float3(0.74, 0.62, 0.46), stain * 0.6);
        float pn = valueNoise((p + float3(0.0003, 0, 0)) * 1100.0) - valueNoise(p * 1100.0);
        float sn = fbm((p + float3(0, 0.0008, 0)) * 160.0) - spots;
        tangentNormal = normalize(float3(pn * 0.6 + sn * 1.5, sn * 1.5 + pores * 0.15, 1));
    } else if (pattern == 3) {
        // Organs and vessels: soft mottling of a moist surface.
        base *= 0.93 + 0.13 * fbm(p * 140.0);
    }
    if (pattern == 1 && fibreStrength > 0.01) {
        float3 axis = normalize(patternData.xyz);
        float3 surfaceAxis = normalize(geometry.tangent());
        float3 across = normalize(cross(normal, surfaceAxis));
        float f = fibres(p, axis);
        float f2 = fibres(p + across * 0.0006, axis);
        float slope = (f2 - f) * 1.1;
        tangentNormal = normalize(float3(0, -slope * fibreStrength, 1));
        // Grooves between bundles are darker, bundle tops slightly lighter.
        base *= mix(1.0, 0.74 + 0.42 * f, fibreStrength);
    }

    // Baked occlusion darkens creases between structures.
    float ao = mix(1.0, occlusion, occlusionStrength);
    base *= mix(0.42, 1.0, ao);

    float roughness = mix(0.78, 0.36, wetness);
    float3 emissive = float3(0);
    float opacity = 1.0;

    if (mode == 2 || mode == 3) {
        float pulse = 0.5 + 0.5 * sin(params.uniforms().time() * 3.2);
        float3 glow = mode == 2 ? float3(0.10, 0.62, 1.0) : float3(1.0, 0.70, 0.12);
        base = mix(base, glow, 0.55);
        emissive = glow * (0.18 + 0.20 * pulse) + glow * fresnel * 0.6;
        roughness = 0.35;
    } else if (mode == 1) {
        // X-ray glass: faint in the middle, brighter towards the silhouette.
        opacity = 0.06 + 0.42 * fresnel;
        emissive = base * fresnel * 0.25;
    } else {
        // A cool rim light separates the figure from the background.
        emissive = float3(0.55, 0.70, 0.95) * fresnel * rimStrength * ao;
    }

    surface.set_base_color(half3(base));
    surface.set_normal(tangentNormal);
    surface.set_roughness(half(roughness));
    surface.set_metallic(half(0));
    surface.set_specular(half(mix(0.18, 0.42, wetness)));
    surface.set_ambient_occlusion(half(ao));
    surface.set_emissive_color(half3(emissive));
    surface.set_opacity(half(opacity));
}
