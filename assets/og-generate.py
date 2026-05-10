#!/usr/bin/env python3
"""
Generate Open Graph social images for Sagelight Studio.
Outputs 1200x630 PNGs into /assets/og/.

Run:
    python3 assets/og-generate.py
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "og")
FONTS = os.path.join(ROOT, "assets", "fonts")
os.makedirs(OUT, exist_ok=True)

W, H = 1200, 630

# Palette — pure-native direction (Stitch iteration 3)
BG = (13, 21, 13)            # #0d150d forest dark
BG_SURFACE = (22, 30, 21)    # #161e15
GREEN = (85, 238, 113)       # #55ee71
GREEN_BRIGHT = (108, 255, 130)
GREEN_DEEP = (48, 209, 88)
TEXT = (220, 229, 215)       # #dce5d7
SUB = (188, 203, 183)        # #bccbb7
DIM = (134, 149, 131)        # #869583
BORDER = (61, 74, 59)        # #3d4a3b
BORDER_SOFT = (32, 42, 30)

# Fonts (downloaded into assets/fonts/)
F_DISPLAY = os.path.join(FONTS, "HankenGrotesk-Bold.ttf")
F_ITALIC = os.path.join(FONTS, "PlayfairDisplay-Italic.ttf")
F_BODY = os.path.join(FONTS, "Inter-Regular.ttf")
F_MONO = os.path.join(FONTS, "JetBrainsMono-Regular.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def base_canvas():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img, "RGBA")

    # Subtle grid that fades toward the bottom
    grid_color = BORDER_SOFT
    for i in range(0, W, 80):
        d.line([(i, 0), (i, H)], fill=grid_color, width=1)
    for i in range(0, H, 80):
        d.line([(0, i), (W, i)], fill=grid_color, width=1)

    # Soft green glow orbs
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((W - 540, -200, W + 140, 460), fill=(85, 238, 113, 50))
    gd.ellipse((-220, H - 360, 420, H + 220), fill=(85, 238, 113, 26))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=90))
    img.paste(glow, (0, 0), glow)

    d = ImageDraw.Draw(img, "RGBA")

    # Top accent line
    d.rectangle((0, 0, W, 3), fill=GREEN)

    # Logo — leaf glyph + wordmark
    cx, cy = 76, 80
    leaf = []
    # Stylized leaf path drawn via points
    pts = [
        (0, -1.0), (0.55, -0.85), (0.85, -0.4), (0.95, 0.05),
        (0.78, 0.55), (0.4, 0.92), (0, 1.0),
        (-0.35, 0.85), (-0.55, 0.55), (-0.55, 0.18),
        (-0.4, -0.05), (-0.18, -0.25), (0, -0.35),
    ]
    r = 24
    for nx, ny in pts:
        leaf.append((cx + int(nx * r), cy + int(ny * r)))
    d.polygon(leaf, fill=GREEN)
    # Vein
    d.line([(cx, cy - 20), (cx, cy + 20)], fill=BG, width=2)

    logo_font = font(F_DISPLAY, 30)
    d.text((114, 64), "Sagelight Studio", font=logo_font, fill=TEXT)
    domain = font(F_MONO, 16)
    d.text((W - 64 - 240, 76), "sagelight-studio.com", font=domain, fill=DIM)

    return img, d


def draw_pill(d, x, y, text, font_obj):
    bbox = d.textbbox((0, 0), text, font=font_obj)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pw = tw + 32
    ph = th + 18
    # Pulse dot
    dot_r = 4
    d.ellipse(
        (x + 14 - dot_r, y + ph // 2 - dot_r, x + 14 + dot_r, y + ph // 2 + dot_r),
        fill=GREEN,
    )
    d.rounded_rectangle(
        (x, y, x + pw, y + ph),
        radius=ph // 2,
        fill=(85, 238, 113, 28),
        outline=(85, 238, 113, 100),
        width=1,
    )
    d.text((x + 26, y + 8), text, font=font_obj, fill=GREEN)
    return pw


def text_with_em(d, x, y, parts, font_reg, font_em, fill_reg, fill_em):
    cx = x
    for txt, kind in parts:
        f = font_em if kind == "em" else font_reg
        c = fill_em if kind == "em" else fill_reg
        d.text((cx, y), txt, font=f, fill=c)
        bbox = d.textbbox((0, 0), txt, font=f)
        cx += bbox[2] - bbox[0]


def page(out_name, eyebrow, title_lines, subtitle, footer):
    img, d = base_canvas()

    pill_font = font(F_MONO, 16)
    draw_pill(d, 64, 150, eyebrow.upper(), pill_font)

    title_font = font(F_DISPLAY, 92)
    title_em = font(F_ITALIC, 92)
    y = 220
    for line in title_lines:
        text_with_em(d, 64, y, line, title_font, title_em, TEXT, GREEN)
        y += 108

    sub_font = font(F_BODY, 26)
    wrap = wrap_text(d, subtitle, sub_font, W - 128)
    sy = y + 24
    for ln in wrap[:3]:
        d.text((64, sy), ln, font=sub_font, fill=SUB)
        sy += 38

    footer_font = font(F_MONO, 16)
    d.text((64, H - 64), footer.upper(), font=footer_font, fill=DIM)

    out_path = os.path.join(OUT, out_name)
    img.save(out_path, "PNG", optimize=True)
    print(f"wrote {out_path}")


def wrap_text(d, text, fnt, max_w):
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        test = (cur + " " + w).strip()
        bw = d.textbbox((0, 0), test, font=fnt)
        if bw[2] - bw[0] <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


PAGES = [
    {
        "out": "home.png",
        "eyebrow": "Privacy-first · EU-built",
        "title_lines": [
            [("Calm software for the", "reg")],
            [("noisy bits ", "em"), ("of life", "reg")],
        ],
        "subtitle": "SageBills · SageMeet · SageDocs — three privacy-first iOS & macOS apps from an independent studio in Romania, EU.",
        "footer": "iOS · macOS · GDPR Compliant · Zero Tracking",
    },
    {
        "out": "sagebills.png",
        "eyebrow": "SageBills · iOS & macOS · Free",
        "title_lines": [
            [("Every bill.", "reg")],
            [("Every provider. ", "reg"), ("One app.", "em")],
        ],
        "subtitle": "The smart utility tracker built for European households. Track, predict, and save — with zero data leaving your device.",
        "footer": "40+ Categories · OCR Scanning · GDPR Compliant",
    },
    {
        "out": "sagemeet.png",
        "eyebrow": "SageMeet · iOS · BYOK",
        "title_lines": [
            [("Record. Transcribe.", "reg")],
            [("Remember ", "em"), ("everything.", "reg")],
        ],
        "subtitle": "AI meeting recorder for iPhone. Whisper transcripts and GPT-4o summaries with your own OpenAI key. Private Mode disables all external data.",
        "footer": "Whisper · GPT-4o · Bring Your Own Key · Private Mode",
    },
    {
        "out": "sagedocs.png",
        "eyebrow": "SageDocs · iOS & macOS · Free",
        "title_lines": [
            [("Your documents.", "reg")],
            [("Encrypted. ", "em"), ("Yours.", "em")],
        ],
        "subtitle": "AES-256 encrypted vault for IDs, contracts, insurance, and personal documents. Biometric-protected. Encrypted iCloud sync.",
        "footer": "AES-256-GCM · Face ID · Encrypted iCloud · Free",
    },
    {
        "out": "blog.png",
        "eyebrow": "Sagelight Studio · Blog",
        "title_lines": [
            [("Tips, insights,", "reg")],
            [("and ", "reg"), ("smart bills", "em"), (".", "reg")],
        ],
        "subtitle": "Money-saving guides and product updates for European households who want to spend less and know more about their utilities.",
        "footer": "Money Saving · Guides · Market Insights",
    },
    {
        "out": "press.png",
        "eyebrow": "Sagelight Studio · Press Kit",
        "title_lines": [
            [("Press resources", "reg")],
            [("for ", "reg"), ("Sagelight ", "em"), ("Studio", "reg")],
        ],
        "subtitle": "Brand assets, press releases, screenshots, and contact info. Everything journalists and content creators need to cover our apps.",
        "footer": "contact@sagelight-studio.com",
    },
    {
        "out": "legal.png",
        "eyebrow": "Sagelight Studio · Legal",
        "title_lines": [
            [("Privacy. GDPR.", "reg")],
            [("Terms ", "em"), ("of Service.", "reg")],
        ],
        "subtitle": "Local-first apps. Zero tracking. Full GDPR compliance. Read exactly how we handle your data — short version: we don't.",
        "footer": "GDPR · Articles 13 & 14 · ePrivacy",
    },
]


def main():
    for p in PAGES:
        page(p["out"], p["eyebrow"], p["title_lines"], p["subtitle"], p["footer"])
    print(f"\nGenerated {len(PAGES)} OG images in {OUT}")


if __name__ == "__main__":
    main()
