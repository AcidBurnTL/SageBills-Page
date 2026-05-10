#!/usr/bin/env python3
"""
Generate Open Graph social images for Sagelight Studio.
Outputs 1200x630 PNGs into /assets/og/.

Run:
    python3 assets/og-generate.py
"""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "og")
os.makedirs(OUT, exist_ok=True)

W, H = 1200, 630

BG = (5, 5, 5)
GREEN = (0, 214, 114)
GREEN_DIM = (0, 214, 114, 60)
TEXT = (232, 232, 237)
SUB = (160, 160, 171)
DIM = (110, 110, 120)
BORDER = (40, 40, 48)

GEORGIA_BOLD = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
GEORGIA_BOLD_ITALIC = "/System/Library/Fonts/Supplemental/Georgia Bold Italic.ttf"
HELVETICA = "/System/Library/Fonts/Helvetica.ttc"
MENLO = "/System/Library/Fonts/Menlo.ttc"


def font(path, size, index=0):
    if path.endswith(".ttc"):
        return ImageFont.truetype(path, size, index=index)
    return ImageFont.truetype(path, size)


def base_canvas():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img, "RGBA")

    for i in range(0, W, 60):
        d.line([(i, 0), (i, H)], fill=BORDER + (), width=1)
    for i in range(0, H, 60):
        d.line([(0, i), (W, i)], fill=BORDER, width=1)

    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((W - 480, -180, W + 120, 420), fill=(0, 214, 114, 40))
    gd.ellipse((-200, H - 320, 400, H + 200), fill=(0, 214, 114, 24))
    glow = glow.filter_nothing() if False else glow
    from PIL import ImageFilter
    glow = glow.filter(ImageFilter.GaussianBlur(radius=80))
    img.paste(glow, (0, 0), glow)

    d = ImageDraw.Draw(img, "RGBA")
    d.rectangle((0, 0, W, 4), fill=GREEN)

    cx, cy = 76, 76
    leaf = [
        (cx, cy - 22),
        (cx + 18, cy - 14),
        (cx + 22, cy + 4),
        (cx + 14, cy + 18),
        (cx, cy + 22),
        (cx - 12, cy + 12),
        (cx - 18, cy - 4),
        (cx - 12, cy - 16),
    ]
    d.polygon(leaf, fill=GREEN)
    d.line([(cx, cy - 18), (cx, cy + 18)], fill=BG, width=2)

    logo_font = font(HELVETICA, 28, index=1)
    d.text((110, 60), "Sagelight Studio", font=logo_font, fill=TEXT)
    domain = font(MENLO, 18, index=0)
    d.text((W - 64 - 280, 70), "sagelight-studio.com", font=domain, fill=DIM)

    return img, d


def draw_pill(d, x, y, text, font_obj):
    bbox = d.textbbox((0, 0), text, font=font_obj)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pw = tw + 28
    ph = th + 16
    d.rounded_rectangle(
        (x, y, x + pw, y + ph),
        radius=ph // 2,
        fill=(0, 214, 114, 26),
        outline=(0, 214, 114, 90),
        width=1,
    )
    d.text((x + 14, y + 6), text, font=font_obj, fill=GREEN)
    return pw


def text_with_em(d, x, y, parts, font_reg, font_em, fill_reg, fill_em, line_h=None):
    cx = x
    for txt, kind in parts:
        f = font_em if kind == "em" else font_reg
        c = fill_em if kind == "em" else fill_reg
        d.text((cx, y), txt, font=f, fill=c)
        bbox = d.textbbox((0, 0), txt, font=f)
        cx += bbox[2] - bbox[0]


def page(out_name, eyebrow, title_lines, subtitle, footer):
    img, d = base_canvas()

    pill_font = font(MENLO, 16, index=0)
    draw_pill(d, 64, 140, eyebrow.upper(), pill_font)

    title_font = font(GEORGIA_BOLD, 86)
    title_em = font(GEORGIA_BOLD_ITALIC, 86)
    y = 210
    for line in title_lines:
        text_with_em(d, 64, y, line, title_font, title_em, TEXT, GREEN)
        y += 102

    sub_font = font(HELVETICA, 26, index=2)
    wrap = wrap_text(d, subtitle, sub_font, W - 128)
    sy = y + 20
    for ln in wrap[:3]:
        d.text((64, sy), ln, font=sub_font, fill=SUB)
        sy += 38

    footer_font = font(MENLO, 16, index=0)
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
        "title_lines": [[("Calm software for the ", "reg")], [("noisy bits ", "em"), ("of life", "reg")]],
        "subtitle": "SageBills · SageMeet · SageDocs — three privacy-first iOS & macOS apps from an independent studio in Romania, EU.",
        "footer": "iOS · macOS · GDPR Compliant · Zero Tracking",
    },
    {
        "out": "sagebills.png",
        "eyebrow": "SageBills · iOS & macOS · Free",
        "title_lines": [[("Every bill.", "reg")], [("Every provider. ", "reg"), ("One app.", "em")]],
        "subtitle": "The smart utility tracker built for European households. Track, predict, and save — with zero data leaving your device.",
        "footer": "40+ Categories · OCR Scanning · GDPR Compliant",
    },
    {
        "out": "sagemeet.png",
        "eyebrow": "SageMeet · iOS · BYOK",
        "title_lines": [[("Record. Transcribe.", "reg")], [("Remember ", "em"), ("everything.", "reg")]],
        "subtitle": "AI meeting recorder for iPhone. Whisper transcripts and GPT-4o summaries with your own OpenAI key. Private Mode disables all external data.",
        "footer": "Whisper · GPT-4o · Bring Your Own Key · Private Mode",
    },
    {
        "out": "sagedocs.png",
        "eyebrow": "SageDocs · iOS & macOS · Free",
        "title_lines": [[("Your documents.", "reg")], [("Encrypted. ", "em"), ("Yours.", "em")]],
        "subtitle": "AES-256 encrypted vault for IDs, contracts, insurance, and personal documents. Biometric-protected. Encrypted iCloud sync.",
        "footer": "AES-256-GCM · Face ID · Encrypted iCloud · Free",
    },
    {
        "out": "blog.png",
        "eyebrow": "Sagelight Studio · Blog",
        "title_lines": [[("Tips, insights,", "reg")], [("and ", "reg"), ("smart bills", "em"), (".", "reg")]],
        "subtitle": "Money-saving guides and product updates for European households who want to spend less and know more about their utilities.",
        "footer": "Money Saving · Guides · Market Insights",
    },
    {
        "out": "press.png",
        "eyebrow": "Sagelight Studio · Press Kit",
        "title_lines": [[("Press resources", "reg")], [("for ", "reg"), ("Sagelight ", "em"), ("Studio", "reg")]],
        "subtitle": "Brand assets, press releases, screenshots, and contact info. Everything journalists and content creators need to cover our apps.",
        "footer": "contact@sagelight-studio.com",
    },
    {
        "out": "legal.png",
        "eyebrow": "Sagelight Studio · Legal",
        "title_lines": [[("Privacy. GDPR.", "reg")], [("Terms ", "em"), ("of Service.", "reg")]],
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
