"""App Store creative assets: the product page header and the search result.

    blender -b --python tools/screenshots/render_figures.py -- Anatomy/Resources/Models tools/screenshots/out/creative still
    blender -b --python tools/screenshots/render_figures.py -- Anatomy/Resources/Models tools/screenshots/out/creative turntable
    python3 tools/screenshots/compose_creative.py [header] [video] [search [lang ...]]

header  out/creative/header.png   3840 x 1646 (21:9), no text, one for every language
video   out/creative/header.mp4   the same with the figures turning, 12 s loop, 30 fps
search  out/creative/<lang>/search.png  3840 x 2560 (3:2), headline and the app

The figures come from render_figures.py; the first one (skin) becomes a white
silhouette like the launch screen. Key content stays inside the safe areas
measured from Apple's templates: header 1646 x 661 centred, search result
x 836-3004, y 765-1795.
"""
import glob
import html
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageChops, ImageFilter

from compose import CHROME, frame_html, ribbon_svg, sparkles, streaks, title_html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out", "creative")
HW, HH = 3840, 1646
SW, SH = 3840, 2560
# Figure centres in the render (render_figures.py: 0.9 m apart, 2.2 m tall frame).
PX_PER_M = HH / 2.2
CENTRES = [HW / 2 + (-1.5 + i) * 0.9 * PX_PER_M for i in range(4)]
SKIN_EDGE = int((CENTRES[0] + CENTRES[1]) / 2)
GLOWS = ["#a9c2ff", "#ff4d5e", "#ffd9a0", "#5b8bff"]

SEARCH = {
    "tr": ("3D ANATOMİ ATLASI", "Kemik, kas, eklem\nve damarlar *3D*", "Latince adlar · 369 madde · 760 açıklamalı soru"),
    "en": ("3D ANATOMY ATLAS", "Bones, muscles, joints\nand vessels in *3D*", "Latin names · 369 articles · 760 explained questions"),
    "fr": ("ATLAS D'ANATOMIE 3D", "Os, muscles, articulations\net vaisseaux en *3D*", "Noms latins · 369 fiches · 760 questions expliquées"),
    "de": ("3D-ANATOMIEATLAS", "Knochen, Muskeln, Gelenke\nund Gefäße in *3D*", "Lateinische Namen · 369 Artikel · 760 erklärte Fragen"),
    "es": ("ATLAS DE ANATOMÍA 3D", "Huesos, músculos, articulaciones\ny vasos en *3D*", "Nombres latinos · 369 fichas · 760 preguntas explicadas"),
}


def silhouette(figures):
    """Turns the skin figure white and gives it a soft glow, like the launch screen."""
    im = figures.convert("RGBA")
    left = im.crop((0, 0, SKIN_EDGE, im.height))
    alpha = left.getchannel("A")
    white = Image.new("RGBA", left.size, (255, 255, 255, 0))
    white.putalpha(alpha)
    glow = Image.new("RGBA", left.size, (200, 220, 255, 0))
    glow.putalpha(alpha.filter(ImageFilter.GaussianBlur(28)).point(lambda v: int(v * 0.55)))
    left = Image.alpha_composite(glow, white)
    im.paste(left, (0, 0))
    return im


def chrome(page, size, out):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(page)
        path = f.name
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--allow-file-access-from-files", "--virtual-time-budget=3000", f"--window-size={size[0]},{size[1]}",
                    f"--screenshot={out}", f"file://{path}"], capture_output=True, timeout=180)
    os.unlink(path)
    return Image.open(out).convert("RGB")


BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:%(W)dpx;height:%(H)dpx;overflow:hidden}
body{position:relative;background:radial-gradient(90%% 120%% at 50%% 40%%,#142650 0%%,#0a1532 42%%,#050913 100%%);
 font-family:-apple-system,"SF Pro Display",system-ui,sans-serif;color:#fff;-webkit-font-smoothing:antialiased}
.orb{position:absolute;border-radius:50%%;filter:blur(%(blur)dpx)}
.ribbon{position:absolute;top:0}
.spark{position:absolute;border-radius:50%%}
.star4{position:absolute;opacity:.85;filter:drop-shadow(0 0 8px rgba(255,255,255,.6))}
.streak{position:absolute;height:3px;border-radius:9px;transform:rotate(-24deg);opacity:.5}
.grid{position:absolute;left:-10%%;right:-10%%;bottom:0;height:34%%;opacity:.18;
 background-image:linear-gradient(rgba(120,160,255,.4) 1px,transparent 1px),linear-gradient(90deg,rgba(120,160,255,.4) 1px,transparent 1px);
 background-size:%(cell)dpx %(cell)dpx;transform:perspective(%(persp)dpx) rotateX(64deg);transform-origin:50%% 100%%;
 -webkit-mask-image:linear-gradient(transparent,#000 70%%)}
.floor{position:absolute;border-radius:50%%;filter:blur(%(fblur)dpx)}
.beam{position:absolute;top:6%%;bottom:8%%;width:3px;background:linear-gradient(transparent,rgba(170,200,255,.55),transparent);
 box-shadow:0 0 30px 6px rgba(120,160,255,.25)}
.vignette{position:absolute;inset:0;background:radial-gradient(120%% 100%% at 50%% 50%%,transparent 55%%,rgba(0,0,0,.55) 100%%)}
"""


def header_background():
    """Everything of the header except the figures."""
    orbs = "".join(f'<i class="orb" style="left:{c - 520:.0f}px;top:{HH * 0.12:.0f}px;width:1040px;height:1200px;background:{g};opacity:.20"></i>'
                   for c, g in zip(CENTRES, GLOWS))
    floors = "".join(f'<i class="floor" style="left:{c - 330:.0f}px;top:{HH * 0.86:.0f}px;width:660px;height:120px;background:{g};opacity:.35"></i>'
                     for c, g in zip(CENTRES, GLOWS))
    beams = "".join(f'<i class="beam" style="left:{(a + b) / 2:.0f}px"></i>' for a, b in zip(CENTRES, CENTRES[1:]))
    css = BASE_CSS % dict(W=HW, H=HH, blur=140, cell=150, persp=1600, fblur=40)
    page = (f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>'
            f'{orbs}<div class="grid"></div>{ribbon_svg(HW, HH, 0, 1, ("#ff5a6e", "#5ba8ff"))}{streaks(HW, HH, ("#ff5a6e", "#5ba8ff"), 1)}'
            f'{sparkles(HW, HH, 41, ("#ff5a6e", "#5ba8ff"), stars=2, star_size=0.45)}{floors}{beams}<div class="vignette"></div></body></html>')
    return chrome(page, (HW, HH), os.path.join(OUT, "header-bg.png"))


def header():
    bg = header_background().convert("RGBA")
    figures = silhouette(Image.open(os.path.join(OUT, "figures.png")))
    out = Image.alpha_composite(bg, figures).convert("RGB")
    out.save(os.path.join(OUT, "header.png"))
    print("  out/creative/header.png")


def video():
    frames = sorted(glob.glob(os.path.join(OUT, "frames", "*.png")))
    assert frames, "render the turntable first"
    bg = Image.open(os.path.join(OUT, "header-bg.png")).convert("RGBA") if os.path.exists(os.path.join(OUT, "header-bg.png")) \
        else header_background().convert("RGBA")
    done = os.path.join(OUT, "video")
    os.makedirs(done, exist_ok=True)
    for i, path in enumerate(frames):
        Image.alpha_composite(bg, silhouette(Image.open(path))).convert("RGB").save(os.path.join(done, f"{i + 1:04d}.png"))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "30", "-i", os.path.join(done, "%04d.png"),
                    "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    os.path.join(OUT, "header.mp4")], check=True)
    print("  out/creative/header.mp4")


def search(lang):
    kicker, title, sub = SEARCH[lang]
    raw = os.path.join(HERE, "raw", "iphone69", lang, "01-atlas.png")
    rw, rh = Image.open(raw).size
    dw = 470
    device, dh, _ = frame_html("phone", dw, dw * (1 - 0.062), dw * (1 - 0.062) * rh / rw, raw, (0.30, 0.27), ("#ff5a6e", "#5ba8ff"))
    # The skeleton with the heart and vessels, large, beside the phone.
    vessels = os.path.join(OUT, "figure-vessels.png")
    if not os.path.exists(vessels):
        left = int((CENTRES[2] + CENTRES[3]) / 2)
        Image.open(os.path.join(OUT, "figures.png")).crop((left, 0, HW, HH)).save(vessels)
    vw, vh = Image.open(vessels).size
    scale = 2300 / (HH * 0.80)
    fig_w, fig_h = vw * scale, vh * scale
    fig_left = 3330 - (CENTRES[3] - int((CENTRES[2] + CENTRES[3]) / 2)) * scale
    css = BASE_CSS % dict(W=SW, H=SH, blur=170, cell=170, persp=1800, fblur=50) + f"""
.figs{{position:absolute;top:{SH * 0.5 - fig_h * 0.53:.0f}px;left:{fig_left:.0f}px;
 width:{fig_w:.0f}px;height:{fig_h:.0f}px;background:url('file://{vessels}') no-repeat;background-size:100% 100%;opacity:.95}}
.text{{position:absolute;left:880px;top:765px;width:1380px;height:1030px;display:flex;flex-direction:column;justify-content:center;z-index:5}}
.kicker{{align-self:flex-start;display:inline-flex;align-items:center;gap:22px;font-size:46px;font-weight:700;letter-spacing:.16em;
 padding:18px 38px;border-radius:999px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.16);color:#ff6b7d}}
.kicker i{{width:18px;height:18px;border-radius:50%;background:#ff6b7d;box-shadow:0 0 26px #ff6b7d}}
h1{{font-size:150px;line-height:1.02;font-weight:800;letter-spacing:-.03em;margin-top:44px;text-shadow:0 10px 50px rgba(0,0,0,.5)}}
.hl{{background:linear-gradient(100deg,#ff5a6e,#5ba8ff);-webkit-background-clip:text;background-clip:text;color:transparent}}
.sub{{font-size:58px;line-height:1.3;font-weight:500;color:rgba(222,232,255,.75);margin-top:40px}}
.stage{{position:absolute;left:{2400:.0f}px;top:{SH / 2 - dh / 2:.0f}px;width:{dw}px;height:{dh:.0f}px;z-index:4}}
.tilt{{position:absolute;inset:0;transform:perspective(6000px) rotateY(-11deg) rotateX(4deg) rotateZ(1.5deg)}}
.metal{{position:relative;background:linear-gradient(135deg,#6b717d 0%,#2a2d34 22%,#4b505a 48%,#1c1e23 74%,#5d636e 100%);
 box-shadow:0 0 0 1px rgba(255,255,255,.18) inset,0 60px 140px rgba(0,0,0,.7),0 0 220px rgba(255,90,110,.35)}}
.bezel{{background:#050507;width:100%;height:100%}}
.screen{{position:relative;overflow:hidden;background:#000}}
.screen img{{display:block;width:100%;height:100%;object-fit:cover;object-position:top}}
.island{{position:absolute;left:50%;transform:translateX(-50%);background:#000;border-radius:999px}}
.btn{{position:absolute;width:9px;border-radius:6px;background:linear-gradient(90deg,#3b3f47,#6a707b,#3b3f47)}}
.ring{{position:absolute;border-radius:50%;border:5px solid}}
.tap{{position:absolute;border-radius:50%;background:rgba(255,255,255,.85);box-shadow:0 0 30px 8px rgba(255,255,255,.55)}}
"""
    page = (f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>'
            f'<i class="orb" style="left:-400px;top:700px;width:1800px;height:1800px;background:#ff4d5e;opacity:.16"></i>'
            f'<i class="orb" style="left:2300px;top:300px;width:1900px;height:1900px;background:#4f8bff;opacity:.20"></i>'
            f'<div class="grid"></div>{ribbon_svg(SW, SH, 0, 1, ("#ff5a6e", "#5ba8ff"))}{sparkles(SW, SH, 77, ("#ff5a6e", "#5ba8ff"), stars=2, star_size=0.5)}'
            f'<div class="figs"></div><div class="vignette"></div>'
            f'<div class="text"><span class="kicker"><i></i>{html.escape(kicker)}</span><h1>{title_html(title)}</h1>'
            f'<p class="sub">{html.escape(sub)}</p></div>'
            f'<div class="stage"><div class="tilt">{device}</div></div>'
            "<script>const h=document.querySelector('h1');let fs=150;"
            "while(h.getBoundingClientRect().width>1380||h.scrollWidth>1380){fs*=0.97;h.style.fontSize=fs+'px';}"
            "const lines=h.innerHTML.split('<br>').length;"
            "while(h.getBoundingClientRect().height>fs*1.02*lines*1.1&&fs>40){fs*=0.97;h.style.fontSize=fs+'px';}</script>"
            '</body></html>')
    os.makedirs(os.path.join(OUT, lang), exist_ok=True)
    chrome(page, (SW, SH), os.path.join(OUT, lang, "search.png")).save(os.path.join(OUT, lang, "search.png"))
    print(f"  out/creative/{lang}/search.png")


def main():
    argv = sys.argv[1:] or ["header", "search"]
    if "header" in argv:
        header()
    if "video" in argv:
        video()
    if "search" in argv:
        langs = [a for a in argv[argv.index("search") + 1:] if a in SEARCH] or list(SEARCH)
        for lang in langs:
            search(lang)


if __name__ == "__main__":
    main()
