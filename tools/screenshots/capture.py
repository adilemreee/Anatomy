"""Captures raw App Store screenshots from a booted simulator.

Each shot launches the app with launch arguments (see AppModel and RootView)
in one language and saves the screen as PNG:

    python3 tools/screenshots/capture.py <udid> <device-name> [lang ...] [--only name ...] [--window 466x678]

--window shrinks the app's window on a full-screen iPad (-WindowSize, Debug
builds) and crops it out; this is how the iPhone Duo displays are captured:
466x678 pt for the outer display, 669x951 pt for the inner one.

Output: tools/screenshots/raw/<device-name>/<lang>/<shot>.png
"""
import os
import subprocess
import sys
import time

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = "adilemre.Anatomy"
LOCALES = {"tr": "tr_TR", "en": "en_US", "fr": "fr_FR", "de": "de_DE", "es": "es_ES"}
COMMON = ["-PremiumUnlocked", "YES", "-SkipOnboarding", "YES", "-SkipSplash", "YES", "-AtlasNoHint", "YES",
          "-AtlasColors", "realistic", "-AtlasSex", "male"]

# name: (launch arguments, seconds to wait before the capture)
SHOTS = {
    "01-atlas": (["-AppTab", "atlas", "-AtlasLayers", "skeletal,muscular", "-atlas.labels", "YES"], 30),
    "02-muscle": (["-AppTab", "atlas", "-AtlasInspect", "Biceps brachii muscle"], 35),
    "03-vessels": (["-AppTab", "atlas", "-AtlasLayers", "skeletal,cardiovascular", "-atlas.labels", "YES"], 30),
    "04-quiz": (["-AppTab", "study", "-StartQuiz", "key:cv-ac08c79d,mu-64e5a84c,ar-d525aa5a", "-QuizReveal", "YES"], 16),
    "05-article": (["-AppTab", "systems", "-OpenEntry", "m-deltoideus"], 10),
    "06-study": (["-AppTab", "study"], 10),
    "07-explore": (["-AppTab", "systems"], 10),
}


def run(cmd, timeout):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout).returncode
    except subprocess.TimeoutExpired:
        return -1


def crop_window(path, size):
    """Crops a window placed at the left edge, just below the status bar."""
    w, h = (int(v) * 2 for v in size.split("x"))
    im = Image.open(path).convert("RGB")
    probe = w - 20
    top = next(y for y in range(40, im.height) if sum(im.getpixel((probe, y))) > 6)
    im.crop((0, top, w, top + h)).save(path)


def capture(udid, device, lang, name, window=None):
    args, wait = SHOTS[name]
    out = os.path.join(HERE, "raw", device, lang)
    os.makedirs(out, exist_ok=True)
    run(["xcrun", "simctl", "terminate", udid, BUNDLE], 15)
    time.sleep(1)
    launch = ["xcrun", "simctl", "launch", udid, BUNDLE, "-AppleLanguages", f"({lang})",
              "-AppleLocale", LOCALES[lang]] + COMMON + args + (["-WindowSize", window] if window else [])
    if run(launch, 40) != 0:
        print(f"  launch failed: {name}")
    time.sleep(wait * float(os.environ.get("WAIT_SCALE", "1")))
    path = os.path.join(out, f"{name}.png")
    run(["xcrun", "simctl", "io", udid, "screenshot", path], 30)
    if window:
        crop_window(path, window)
    print(f"  {device}/{lang}/{name}.png", flush=True)


def main():
    argv = sys.argv[1:]
    only, window = [], None
    if "--window" in argv:
        i = argv.index("--window")
        window = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    if "--only" in argv:
        i = argv.index("--only")
        only = argv[i + 1:]
        argv = argv[:i]
    udid, device = argv[0], argv[1]
    langs = argv[2:] or list(LOCALES)
    for lang in langs:
        for name in SHOTS:
            if not only or name in only:
                capture(udid, device, lang, name, window)
    run(["xcrun", "simctl", "terminate", udid, BUNDLE], 15)


if __name__ == "__main__":
    main()
