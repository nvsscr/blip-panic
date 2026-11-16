"""Build the upload files from index.html.

    python build.py

dist/blip-panic-itch.zip   -> upload to itch.io (or any HTML5 game site)
dist/blip-panic-play.html  -> the version published as a Claude page
"""
import re
import zipfile
from pathlib import Path

root = Path(__file__).parent
dist = root / "dist"
dist.mkdir(exist_ok=True)
src = (root / "index.html").read_text(encoding="utf-8")

with zipfile.ZipFile(dist / "blip-panic-itch.zip", "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("index.html", src)

# Claude pages add their own <html>/<head>/<body> and viewport, so strip ours.
head = src[src.index("<head>") + 6 : src.index("</head>")]
body = src[src.index("<body>") + 6 : src.index("</body>")]
for pat in (r'<meta charset[^>]*>\s*', r'<meta name="viewport"[^>]*>\s*', r'<meta name="theme-color"[^>]*>\s*'):
    head = re.sub(pat, "", head)
head = head.replace(":root {", ":root { color-scheme: dark;", 1)
(dist / "blip-panic-play.html").write_text(head.strip() + "\n" + body.strip() + "\n", encoding="utf-8")

# CrazyGames: same game plus their SDK (ads, gameplay events). Only this copy loads it,
# because the SDK blocks the game on any site that isn't CrazyGames.
SDK_TAG = '<script src="https://sdk.crazygames.com/crazygames-sdk-v3.js"></script>\n'
cg = src.replace("</head>", SDK_TAG + "</head>", 1)
cg_dir = dist / "crazygames"
cg_dir.mkdir(exist_ok=True)
(cg_dir / "index.html").write_text(cg, encoding="utf-8")
with zipfile.ZipFile(dist / "blip-panic-crazygames.zip", "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("index.html", cg)

print("built", *(p.name for p in dist.iterdir()))
