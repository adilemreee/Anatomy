"""Composes the App Store screenshots from the raw captures.

Every slide is an HTML page (device frame, captions, glow, a light ribbon
that flows on from one slide to the next) rendered by headless Chrome at
the exact App Store Connect size:

    python3 tools/screenshots/compose.py [lang ...] [--device iphone69 ...] [--slide 01-atlas ...]

Input:  tools/screenshots/raw/<device>/<lang>/<slide>.png (capture.py)
Output: tools/screenshots/out/<lang>/<device>/<slide>.png
"""
import html
import math
import os
import random
import re
import subprocess
import sys
import tempfile

from PIL import Image

from captions import COPY, LANGS

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Canvas, frame and type sizes per App Store display.
DEVICES = {
    "iphone69": dict(size=(1320, 2868), frame="phone", width=0.80, top=640, text_top=150,
                     kicker=34, title=104, sub=40, chip=36),
    "ipad13": dict(size=(2064, 2752), frame="tablet", width=0.80, top=720, text_top=170,
                   kicker=42, title=128, sub=50, chip=46),
    "duo-outer": dict(size=(1398, 2034), frame="duo-closed", width=0.76, top=560, text_top=120,
                      kicker=32, title=94, sub=38, chip=36),
    "duo-inner": dict(size=(2007, 2853), frame="duo-open", width=0.80, top=690, text_top=170,
                      kicker=42, title=124, sub=48, chip=44),
}
# Smaller iPhone displays are scaled from the 6.9" composition.
DERIVED = {"iphone63": ("iphone69", (1206, 2622))}

# accent colours, tilt direction (-1, 0, 1), where the chips sit (fractions of
# the device box) and a tap ripple on the screen (fractions of the screen).
SLIDES = {
    "01-atlas": dict(accent=("#ff5a6e", "#ffb36b"), tilt=-1, chips=[("l", 0.255), ("r", 0.60)], ripple=(0.30, 0.27)),
    "02-muscle": dict(accent=("#ff6b7d", "#5b9dff"), tilt=1, chips=[("l", 0.30), ("r", 0.72)], ripple=None),
    "03-vessels": dict(accent=("#ff4060", "#4f8bff"), tilt=-1, chips=[("l", 0.17), ("r", 0.80)], ripple=(0.58, 0.36)),
    "04-quiz": dict(accent=("#3ee08f", "#8b6cff"), tilt=0, chips=[("r", 0.47), ("r", 0.137)], ripple=(0.80, 0.405)),
    "05-article": dict(accent=("#ffc857", "#5ba8ff"), tilt=1, chips=[("r", 0.262), ("l", 0.03)], ripple=None),
    "06-study": dict(accent=("#8f6bff", "#ff8a4c"), tilt=-1, chips=[("r", 0.255), ("l", 0.36)], ripple=None),
    "07-explore": dict(accent=("#5ba8ff", "#ff5a6e"), tilt=1, chips=[("r", 0.405), ("l", 0.66)], ripple=None),
}
ORDER = list(SLIDES)

ICONS = {
    "cube": '<path d="M12 2 3 7v10l9 5 9-5V7z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M3 7l9 5 9-5M12 12v10" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    "heart": '<path d="M12 21s-7.5-4.6-9.5-9.2C1 8.2 3.3 4.5 7 4.5c2 0 3.6 1.1 5 2.8 1.4-1.7 3-2.8 5-2.8 3.7 0 6 3.7 4.5 7.3C19.5 16.4 12 21 12 21z" fill="currentColor"/>',
    "layers": '<path d="M12 3 2 8l10 5 10-5z" fill="currentColor" opacity=".95"/><path d="M2 12l10 5 10-5M2 16l10 5 10-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>',
    "check": '<circle cx="12" cy="12" r="10" fill="currentColor"/><path d="M7 12.5l3.2 3.2L17 9" fill="none" stroke="#06140c" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
    "level": '<rect x="3" y="14" width="4.5" height="7" rx="1.2" fill="currentColor" opacity=".55"/><rect x="9.75" y="9" width="4.5" height="12" rx="1.2" fill="currentColor" opacity=".8"/><rect x="16.5" y="3" width="4.5" height="18" rx="1.2" fill="currentColor"/>',
    "star": '<path d="M12 2.5l2.9 6 6.6.8-4.9 4.6 1.3 6.5L12 17.2l-5.9 3.2 1.3-6.5L2.5 9.3l6.6-.8z" fill="currentColor"/>',
    "book": '<path d="M2 5.5C4.5 4 8.5 4 12 6c3.5-2 7.5-2 10-.5V20c-2.5-1.5-6.5-1.5-10 .5-3.5-2-7.5-2-10-.5z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M12 6v14.5" stroke="currentColor" stroke-width="1.8"/>',
    "flame": '<path d="M12 22c-4.4 0-7.5-3-7.5-7.2 0-3.5 2.3-5.7 4.1-7.8.5 1.8 1.5 3 2.8 3.5-.4-3.4 1.1-6.3 3.6-8.5.4 3.1 2 5 3.4 6.8 1.3 1.6 1.6 3.4 1.6 5.4C20 18.6 16.6 22 12 22z" fill="currentColor"/>',
    "timer": '<circle cx="12" cy="13.5" r="8" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 13.5V9M9.5 2.5h5M19 6l1.5-1.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "globe": '<circle cx="12" cy="12" r="9.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M2.5 12h19M12 2.5c3 3 3 16 0 19M12 2.5c-3 3-3 16 0 19" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    "lock": '<rect x="4.5" y="10.5" width="15" height="11" rx="2.5" fill="currentColor"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3" fill="none" stroke="currentColor" stroke-width="2"/>',
}
DOTS = {"dot": None, "red": "#ff4d5e", "blue": "#4d8dff"}


def ribbon_svg(w, h, index, count, accent):
    """Three glowing strands across the whole carousel; this slide shows its part."""
    total = w * count
    strands = []
    rnd = random.Random(7)
    for k in range(3):
        amp = h * (0.05 + 0.025 * k)
        base = h * (0.60 + 0.07 * k)
        freq = 2 * math.pi / (w * (1.6 + 0.35 * k))
        phase = rnd.uniform(0, math.pi * 2)
        pts = []
        for x in range(-w, total + w, 24):
            y = base + amp * math.sin(x * freq + phase) + h * 0.03 * math.sin(x * freq * 0.37 + k)
            pts.append(f"{x:.0f},{y:.0f}")
        strands.append(" ".join(pts))
    colors = ["#ff5a6e", "#ffb36b", "#5ba8ff", "#8f6bff", "#3ee08f", "#ff4060", "#5ba8ff"]
    stops = "".join(f'<stop offset="{i / (len(colors) - 1):.2f}" stop-color="{c}"/>' for i, c in enumerate(colors))
    lines = []
    for k, pts in enumerate(strands):
        width = [3.2, 2.0, 1.4][k] * w / 1320
        lines.append(f'<polyline points="{pts}" fill="none" stroke="url(#rg)" stroke-width="{width * 9:.1f}" opacity=".10" filter="url(#blur)"/>')
        lines.append(f'<polyline points="{pts}" fill="none" stroke="url(#rg)" stroke-width="{width:.1f}" opacity="{[0.85, 0.55, 0.4][k]}"/>')
    return (f'<svg class="ribbon" width="{total}" height="{h}" viewBox="0 0 {total} {h}" style="left:{-index * w}px">'
            f'<defs><linearGradient id="rg" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{total}" y2="0">{stops}</linearGradient>'
            f'<filter id="blur" x="-5%" y="-50%" width="110%" height="200%"><feGaussianBlur stdDeviation="{w / 120:.1f}"/></filter></defs>'
            + "".join(lines) + "</svg>")


def sparkles(w, h, seed, accent):
    rnd = random.Random(seed)
    out = []
    for _ in range(26):
        x, y = rnd.uniform(0, w), rnd.uniform(0, h * 0.95)
        r = rnd.choice([1, 1, 1.5, 2, 3]) * w / 1320
        c = rnd.choice(["#ffffff", accent[0], accent[1]])
        o = rnd.uniform(0.25, 0.8)
        out.append(f'<i class="spark" style="left:{x:.0f}px;top:{y:.0f}px;width:{r * 2:.1f}px;height:{r * 2:.1f}px;'
                   f'background:{c};opacity:{o:.2f};box-shadow:0 0 {r * 6:.0f}px {r * 2:.0f}px {c}"></i>')
    for _ in range(4):
        x, y = rnd.uniform(0.05, 0.95) * w, rnd.uniform(0.25, 0.9) * h
        s = rnd.uniform(18, 34) * w / 1320
        c = rnd.choice([accent[0], accent[1], "#ffffff"])
        out.append(f'<svg class="star4" style="left:{x - s:.0f}px;top:{y - s:.0f}px;width:{s * 2:.0f}px;height:{s * 2:.0f}px" viewBox="0 0 20 20">'
                   f'<path d="M10 0C10.8 7 13 9.2 20 10 13 10.8 10.8 13 10 20 9.2 13 7 10.8 0 10 7 9.2 9.2 7 10 0z" fill="{c}"/></svg>')
    return "".join(out)


def streaks(w, h, accent, side):
    out = []
    rnd = random.Random(side)
    for i in range(5):
        length = rnd.uniform(0.18, 0.34) * w
        x = (0.62 + rnd.uniform(-0.1, 0.25)) * w if side > 0 else rnd.uniform(-0.1, 0.25) * w
        y = rnd.uniform(0.04, 0.5) * h
        out.append(f'<i class="streak" style="left:{x:.0f}px;top:{y:.0f}px;width:{length:.0f}px;'
                   f'background:linear-gradient(90deg,transparent,{rnd.choice(accent)}88,#ffffffcc);"></i>')
    return "".join(out)


def title_html(text):
    text = html.escape(text)
    text = re.sub(r"\*(.+?)\*", r'<span class="hl">\1</span>', text, flags=re.S)
    return text.replace("\n", "<br>")


def frame_html(kind, dw, sw, sh, img, ripple, accent):
    """Returns (html, device height) for a device of width dw showing img."""
    ripple_html = ""
    if ripple:
        rx, ry = ripple[0] * sw, ripple[1] * sh
        rings = "".join(f'<i class="ring" style="width:{d:.0f}px;height:{d:.0f}px;left:{rx - d / 2:.0f}px;top:{ry - d / 2:.0f}px;'
                        f'border-color:{accent[0]};opacity:{o}"></i>' for d, o in [(sw * 0.07, 0.95), (sw * 0.16, 0.55), (sw * 0.27, 0.25)])
        ripple_html = rings + f'<i class="tap" style="width:{sw * 0.05:.0f}px;height:{sw * 0.05:.0f}px;left:{rx - sw * 0.025:.0f}px;top:{ry - sw * 0.025:.0f}px"></i>'
    screen = f'<div class="screen" style="width:{sw:.0f}px;height:{sh:.0f}px;border-radius:{{sr}}px"><img src="file://{img}">{{extra}}{ripple_html}</div>'
    if kind == "phone":
        metal, bezel = dw * 0.011, dw * 0.020
        r = dw * 0.150
        island = f'<i class="island" style="top:{sw * 0.026:.0f}px;width:{sw * 0.29:.0f}px;height:{sw * 0.085:.0f}px"></i>'
        inner = screen.replace("{sr}", f"{r - metal - bezel:.0f}").replace("{extra}", island)
        buttons = (f'<i class="btn" style="left:{-dw * 0.012:.0f}px;top:{sh * 0.17:.0f}px;height:{sh * 0.035:.0f}px"></i>'
                   f'<i class="btn" style="left:{-dw * 0.012:.0f}px;top:{sh * 0.24:.0f}px;height:{sh * 0.07:.0f}px"></i>'
                   f'<i class="btn" style="left:{-dw * 0.012:.0f}px;top:{sh * 0.33:.0f}px;height:{sh * 0.07:.0f}px"></i>'
                   f'<i class="btn" style="right:{-dw * 0.012:.0f}px;top:{sh * 0.27:.0f}px;height:{sh * 0.10:.0f}px"></i>')
    elif kind == "tablet":
        metal, bezel = dw * 0.007, dw * 0.026
        r = dw * 0.055
        inner = screen.replace("{sr}", f"{r * 0.55:.0f}").replace("{extra}", "")
        buttons = f'<i class="cam" style="top:{-bezel * 0.62:.0f}px;left:{sw / 2 - dw * 0.004:.0f}px;width:{dw * 0.008:.0f}px;height:{dw * 0.008:.0f}px"></i>'
    elif kind == "duo-closed":
        metal, bezel = dw * 0.012, dw * 0.022
        r = dw * 0.115
        cam = f'<i class="punch" style="top:{sw * 0.040:.0f}px;right:{sw * 0.046:.0f}px;width:{sw * 0.042:.0f}px;height:{sw * 0.042:.0f}px"></i>'
        inner = screen.replace("{sr}", f"{r - metal - bezel:.0f}").replace("{extra}", cam)
        buttons = (f'<i class="btn" style="right:{-dw * 0.012:.0f}px;top:{sh * 0.10:.0f}px;height:{sh * 0.09:.0f}px"></i>'
                   f'<i class="btn" style="right:{-dw * 0.012:.0f}px;top:{sh * 0.22:.0f}px;height:{sh * 0.14:.0f}px"></i>')
    else:  # duo-open
        metal, bezel = dw * 0.008, dw * 0.016
        r = dw * 0.062
        hinge = '<i class="hinge"></i><i class="fold-l"></i><i class="fold-r"></i>'
        inner = screen.replace("{sr}", f"{r - metal - bezel:.0f}").replace("{extra}", hinge)
        buttons = (f'<i class="btn" style="right:{-dw * 0.009:.0f}px;top:{sh * 0.08:.0f}px;height:{sh * 0.07:.0f}px"></i>'
                   f'<i class="notch" style="left:{dw / 2 - dw * 0.03:.0f}px;top:{-dw * 0.006:.0f}px;width:{dw * 0.06:.0f}px"></i>'
                   f'<i class="notch" style="left:{dw / 2 - dw * 0.03:.0f}px;bottom:{-dw * 0.006:.0f}px;width:{dw * 0.06:.0f}px"></i>')
    dh = sh + 2 * (metal + bezel)
    device = (f'<div class="metal" style="width:{dw:.0f}px;height:{dh:.0f}px;border-radius:{r:.0f}px;padding:{metal:.0f}px">'
              f'<div class="bezel" style="border-radius:{r - metal:.0f}px;padding:{bezel:.0f}px">{inner}</div>{buttons}</div>')
    return device, dh, r


def chip_html(icon, text, size, accent):
    if icon in DOTS:
        color = DOTS[icon] or accent[0]
        glyph = f'<i class="cdot" style="background:{color};box-shadow:0 0 {size * 0.6:.0f}px {color}"></i>'
    else:
        color = "#3ee08f" if icon == "check" else accent[0]
        glyph = f'<svg viewBox="0 0 24 24" style="color:{color}">{ICONS[icon]}</svg>'
    return f'<div class="chip"><span class="cicon">{glyph}</span><span>{html.escape(text)}</span></div>'


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:%(W)dpx;height:%(H)dpx;overflow:hidden}
body{position:relative;background:radial-gradient(120%% 70%% at 50%% 0%%,#13224a 0%%,#0a1430 38%%,#060a16 100%%);
 font-family:-apple-system,"SF Pro Display",system-ui,sans-serif;color:#fff;-webkit-font-smoothing:antialiased}
.orb{position:absolute;border-radius:50%%;filter:blur(%(blur)dpx)}
.grid{position:absolute;left:-10%%;right:-10%%;bottom:0;height:46%%;opacity:.22;
 background-image:linear-gradient(rgba(120,160,255,.35) 1px,transparent 1px),linear-gradient(90deg,rgba(120,160,255,.35) 1px,transparent 1px);
 background-size:%(cell)dpx %(cell)dpx;transform:perspective(%(persp)dpx) rotateX(62deg);transform-origin:50%% 100%%;
 -webkit-mask-image:linear-gradient(transparent,#000 60%%)}
.ribbon{position:absolute;top:0}
.spark{position:absolute;border-radius:50%%}
.star4{position:absolute;opacity:.85;filter:drop-shadow(0 0 8px rgba(255,255,255,.6))}
.streak{position:absolute;height:%(streak)dpx;border-radius:9px;transform:rotate(-24deg);opacity:.55}
.text{position:absolute;left:0;right:0;top:%(text_top)dpx;text-align:center;padding:0 %(pad)dpx;z-index:5}
.kicker{display:inline-flex;align-items:center;gap:%(kgap)dpx;font-size:%(kicker)dpx;font-weight:700;letter-spacing:.16em;
 padding:%(kpy)dpx %(kpx)dpx;border-radius:999px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);color:%(a1)s}
.kicker i{width:%(kdot)dpx;height:%(kdot)dpx;border-radius:50%%;background:%(a1)s;box-shadow:0 0 %(kglow)dpx %(a1)s}
h1{font-size:%(title)dpx;line-height:1.04;font-weight:800;letter-spacing:-.025em;margin-top:%(tgap)dpx;
 text-shadow:0 8px 40px rgba(0,0,0,.45)}
.hl{background:linear-gradient(100deg,%(a1)s,%(a2)s);-webkit-background-clip:text;background-clip:text;color:transparent}
.sub{font-size:%(sub)dpx;line-height:1.3;font-weight:500;color:rgba(222,232,255,.72);margin-top:%(sgap)dpx}
.stage{position:absolute;left:%(dx)dpx;top:%(dy)dpx;width:%(dw)dpx;height:%(dh)dpx;z-index:3}
.tilt{position:absolute;inset:0;transform:%(tilt)s;transform-origin:50%% 40%%;transform-style:preserve-3d}
.ghost{position:absolute;inset:0;border-radius:%(r)dpx;border:%(gb)dpx solid %(a1)s}
.metal{position:relative;background:linear-gradient(135deg,#6b717d 0%%,#2a2d34 22%%,#4b505a 48%%,#1c1e23 74%%,#5d636e 100%%);
 box-shadow:0 0 0 1px rgba(255,255,255,.18) inset,0 %(sh1)dpx %(sh2)dpx rgba(0,0,0,.7),0 0 %(glow)dpx %(glowc)s}
.bezel{background:#050507;width:100%%;height:100%%;box-shadow:0 0 0 1px rgba(255,255,255,.05) inset}
.screen{position:relative;overflow:hidden;background:#000}
.screen img{display:block;width:100%%;height:100%%;object-fit:cover;object-position:top}
.screen:after{content:"";position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.10) 0%%,rgba(255,255,255,0) 32%%);pointer-events:none}
.island{position:absolute;left:50%%;transform:translateX(-50%%);background:#000;border-radius:999px}
.punch{position:absolute;background:#000;border-radius:50%%;box-shadow:0 0 0 3px rgba(255,255,255,.05)}
.btn{position:absolute;width:%(btnw)dpx;border-radius:6px;background:linear-gradient(90deg,#3b3f47,#6a707b,#3b3f47)}
.cam{position:absolute;border-radius:50%%;background:#1b2130;box-shadow:0 0 0 2px #0b0d12}
.notch{position:absolute;height:%(notch)dpx;border-radius:4px;background:#2b2e35}
.hinge{position:absolute;top:0;bottom:0;left:50%%;width:%(hinge)dpx;transform:translateX(-50%%);
 background:linear-gradient(90deg,rgba(0,0,0,0),rgba(0,0,0,.38) 45%%,rgba(255,255,255,.12) 55%%,rgba(0,0,0,0));z-index:2}
.fold-l{position:absolute;top:0;bottom:0;left:0;width:50%%;background:linear-gradient(90deg,rgba(0,0,0,0) 70%%,rgba(0,0,0,.16));z-index:2}
.fold-r{position:absolute;top:0;bottom:0;right:0;width:50%%;background:linear-gradient(270deg,rgba(255,255,255,0) 70%%,rgba(255,255,255,.05));z-index:2}
.ring{position:absolute;border-radius:50%%;border:%(ringb)dpx solid;z-index:3}
.tap{position:absolute;border-radius:50%%;background:rgba(255,255,255,.85);box-shadow:0 0 30px 8px rgba(255,255,255,.55);z-index:3}
.chip{position:absolute;display:flex;align-items:center;gap:%(cgap)dpx;white-space:nowrap;z-index:6;
 font-size:%(chip)dpx;font-weight:650;letter-spacing:-.005em;padding:%(cpy)dpx %(cpx)dpx %(cpy)dpx %(cpy)dpx;border-radius:999px;
 background:linear-gradient(135deg,rgba(255,255,255,.20),rgba(255,255,255,.07));border:1px solid rgba(255,255,255,.28);
 backdrop-filter:blur(%(cblur)dpx) saturate(1.6);-webkit-backdrop-filter:blur(%(cblur)dpx) saturate(1.6);
 box-shadow:0 %(csh)dpx %(csh2)dpx rgba(0,0,0,.45),0 0 0 1px rgba(0,0,0,.2)}
.chip:before{content:"";position:absolute;top:50%%;height:%(trail)dpx;width:%(trailw)dpx;border-radius:9px;transform:translateY(-50%%);z-index:-1}
.chip.l:before{right:96%%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35))}
.chip.r:before{left:96%%;background:linear-gradient(270deg,transparent,rgba(255,255,255,.35))}
.cicon{display:inline-flex;align-items:center;justify-content:center;width:%(ci)dpx;height:%(ci)dpx;border-radius:50%%;
 background:rgba(4,8,20,.55);border:1px solid rgba(255,255,255,.14)}
.cicon svg{width:58%%;height:58%%}
.cdot{width:40%%;height:40%%;border-radius:50%%}
"""


def render_slide(device, lang, slide, out_path):
    spec = DEVICES[device]
    W, H = spec["size"]
    cfg = SLIDES[slide]
    a1, a2 = cfg["accent"]
    kicker, title, sub, chips = COPY[slide][lang]
    raw = os.path.join(HERE, "raw", device, lang, f"{slide}.png")
    if not os.path.exists(raw):
        print(f"  missing raw {device}/{lang}/{slide}")
        return False
    rw, rh = Image.open(raw).size

    dw = W * spec["width"]
    # Screen size from the device width, the frame's bezels and the capture's shape.
    probe = {"phone": 0.062, "tablet": 0.066, "duo-closed": 0.068, "duo-open": 0.048}[spec["frame"]]
    sw = dw * (1 - probe)
    sh = sw * rh / rw
    device_html, dh, r = frame_html(spec["frame"], dw, sw, sh, raw, cfg["ripple"], cfg["accent"])
    dx = (W - dw) / 2 + cfg["tilt"] * W * 0.015
    dy = spec["top"]
    t = cfg["tilt"]
    tilt = "none" if t == 0 else f"perspective({W * 2.6:.0f}px) rotateY({-9 * t}deg) rotateX(5deg) rotateZ({-1.6 * t}deg)"
    if t == 0:
        tilt = f"perspective({W * 2.6:.0f}px) rotateX(4deg)"
    u = W / 1320
    ghosts = "".join(f'<div class="tilt" style="transform:{tilt} translate({-t * k * 34 * u - (k * 10 * u if t == 0 else 0):.0f}px,{k * 26 * u:.0f}px);opacity:{o}">'
                     f'<div class="ghost" style="border-radius:{r:.0f}px"></div></div>'
                     for k, o in [(2, 0.10), (1, 0.22)])
    chips_html = ""
    for (side, cy), (icon, text) in zip(cfg["chips"], chips):
        # Anchored on the device's edge, mostly outside it; the script below
        # keeps every chip inside the canvas.
        x = dx if side == "l" else dx + dw
        shift = -62 if side == "l" else -38
        style = f"top:{dy + cy * dh:.0f}px;left:{x:.0f}px;transform:translate({shift}%,-50%)"
        chips_html += chip_html(icon, text, spec["chip"], cfg["accent"]).replace('<div class="chip">', f'<div class="chip {side}" style="{style}">', 1)

    idx = ORDER.index(slide)
    css = CSS % dict(
        W=W, H=H, blur=W * 0.09, cell=W * 0.07, persp=W * 0.9, streak=max(2, 3 * u), text_top=spec["text_top"],
        pad=W * 0.07, kgap=spec["kicker"] * 0.45, kicker=spec["kicker"], kpy=spec["kicker"] * 0.42, kpx=spec["kicker"] * 0.9,
        a1=a1, a2=a2, kdot=spec["kicker"] * 0.42, kglow=spec["kicker"] * 0.6, title=spec["title"], tgap=spec["title"] * 0.32,
        sub=spec["sub"], sgap=spec["sub"] * 0.55, dx=dx, dy=dy, dw=dw, dh=dh, tilt=tilt, r=r, gb=max(2, 3 * u),
        sh1=60 * u, sh2=140 * u, glow=220 * u, glowc=a1 + "55", btnw=max(5, 9 * u), notch=10 * u, hinge=W * 0.03,
        ringb=max(3, 5 * u), cgap=spec["chip"] * 0.4, chip=spec["chip"], cpy=spec["chip"] * 0.38, cpx=spec["chip"] * 0.75,
        cblur=24 * u, csh=18 * u, csh2=50 * u, trail=max(2, 3 * u), trailw=W * 0.12, ci=spec["chip"] * 1.6)
    orbs = (f'<i class="orb" style="left:{-W * 0.25:.0f}px;top:{H * 0.30:.0f}px;width:{W * 0.85:.0f}px;height:{W * 0.85:.0f}px;background:{a1};opacity:.30"></i>'
            f'<i class="orb" style="left:{W * 0.45:.0f}px;top:{H * 0.52:.0f}px;width:{W * 0.9:.0f}px;height:{W * 0.9:.0f}px;background:{a2};opacity:.24"></i>'
            f'<i class="orb" style="left:{W * 0.15:.0f}px;top:{-W * 0.35:.0f}px;width:{W * 0.7:.0f}px;height:{W * 0.6:.0f}px;background:#3a5bff;opacity:.22"></i>')
    page = f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>
{orbs}<div class="grid"></div>{ribbon_svg(W, H, idx, len(ORDER), cfg["accent"])}{streaks(W, H, cfg["accent"], 1 if idx % 2 else -1)}{sparkles(W, H, idx * 11 + 3, cfg["accent"])}
<div class="text"><span class="kicker"><i></i>{html.escape(kicker)}</span><h1>{title_html(title)}</h1><p class="sub">{html.escape(sub)}</p></div>
<div class="stage">{ghosts}<div class="tilt">{device_html}</div></div>
{chips_html}
<script>
// Long translations: shrink the title until each of its lines fits on one
// line, and the subtitle until it fits on two.
const h1 = document.querySelector('h1');
const lines = h1.innerHTML.split('<br>').length;
let fs = parseFloat(getComputedStyle(h1).fontSize);
while (h1.getBoundingClientRect().height > fs * 1.04 * lines * 1.1 && fs > 20) {{ fs *= 0.97; h1.style.fontSize = fs + 'px'; }}
const sub = document.querySelector('.sub');
let ss = parseFloat(getComputedStyle(sub).fontSize);
while (sub.getBoundingClientRect().height > ss * 1.3 * 2.1 && ss > 14) {{ ss *= 0.97; sub.style.fontSize = ss + 'px'; }}
const m = {W} * 0.03;
for (const c of document.querySelectorAll('.chip')) {{
  const r = c.getBoundingClientRect();
  let dx = 0;
  if (r.left < m) dx = m - r.left;
  if (r.right > {W} - m) dx = {W} - m - r.right;
  if (dx) c.style.marginLeft = dx + 'px';
}}
</script>
</body></html>"""
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(page)
        page_path = f.name
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
           "--allow-file-access-from-files", "--virtual-time-budget=3000", f"--window-size={W},{H}",
           f"--screenshot={out_path}", f"file://{page_path}"]
    subprocess.run(cmd, capture_output=True, timeout=120)
    os.unlink(page_path)
    im = Image.open(out_path)
    if im.size != (W, H) or im.mode != "RGB":
        im.convert("RGB").resize((W, H), Image.LANCZOS).save(out_path)
    return True


def main():
    argv = sys.argv[1:]
    opts = {"--device": [], "--slide": []}
    langs, key = [], None
    for a in argv:
        if a in opts:
            key = a
        elif key:
            opts[key].append(a)
        else:
            langs.append(a)
    langs = langs or LANGS
    # The iPhone Duo sets are made on request (--device duo-outer duo-inner).
    devices = opts["--device"] or ["iphone69", "ipad13"] + list(DERIVED)
    slides = opts["--slide"] or ORDER
    for lang in langs:
        for device in devices:
            if device in DERIVED:
                continue
            for slide in slides:
                out = os.path.join(HERE, "out", lang, device, f"{slide}.png")
                if render_slide(device, lang, slide, out):
                    print(f"  out/{lang}/{device}/{slide}.png")
        for device, (source, size) in DERIVED.items():
            if device not in devices:
                continue
            for slide in slides:
                src = os.path.join(HERE, "out", lang, source, f"{slide}.png")
                if os.path.exists(src):
                    dst = os.path.join(HERE, "out", lang, device, f"{slide}.png")
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    Image.open(src).convert("RGB").resize(size, Image.LANCZOS).save(dst)
                    print(f"  out/{lang}/{device}/{slide}.png")


if __name__ == "__main__":
    main()
