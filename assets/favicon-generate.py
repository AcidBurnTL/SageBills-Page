#!/usr/bin/env python3
"""Generate PNG favicon variants from the brand SVG (drawn natively in PIL)."""

import os
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = ROOT

BG = (5, 5, 5)
GREEN = (0, 214, 114)
GREEN_DARK = (5, 150, 82)


def render(size: int, padding_ratio: float = 0.08) -> Image.Image:
    img = Image.new("RGBA", (size, size), BG + (255,))
    d = ImageDraw.Draw(img, "RGBA")

    pad = int(size * padding_ratio)
    inner = size - 2 * pad
    cx, cy = size // 2, size // 2 + int(size * 0.04)

    r = inner // 2
    leaf = []
    pts = [
        (0, -1.0), (0.55, -0.85), (0.85, -0.4), (0.95, 0.05),
        (0.78, 0.55), (0.4, 0.92), (0, 1.0),
        (-0.35, 0.85), (-0.55, 0.55), (-0.55, 0.18),
        (-0.4, -0.05), (-0.18, -0.25), (0, -0.35),
    ]
    for nx, ny in pts:
        leaf.append((cx + int(nx * r), cy + int(ny * r)))
    d.polygon(leaf, fill=GREEN)

    d.line(
        [(cx, cy - int(r * 0.85)), (cx, cy + int(r * 0.85))],
        fill=BG, width=max(1, size // 64),
    )

    return img


SIZES = {
    "favicon-16x16.png": 16,
    "favicon-32x32.png": 32,
    "favicon-48x48.png": 48,
    "apple-touch-icon.png": 180,
    "icon-192.png": 192,
    "icon-512.png": 512,
    "og-favicon.png": 256,
}

for name, sz in SIZES.items():
    img = render(sz)
    img.save(os.path.join(OUT, name), "PNG", optimize=True)
    print(f"wrote {name} ({sz}×{sz})")

print("\nFavicon variants written.")
