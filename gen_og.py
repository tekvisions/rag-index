#!/usr/bin/env python3
"""Render og.png (1200x630) for The RAG Index — light vector-field card. Pillow only; graceful fallback."""
from __future__ import annotations

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def _font(paths, size):
    from PIL import ImageFont
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def main() -> int:
    try:
        from PIL import Image, ImageDraw
    except Exception:
        print("Pillow not available — skipping og.png")
        return 0
    try:
        data = json.load(open(os.path.join(HERE, "data.json"), encoding="utf-8"))
        count, cats = data.get("count", 0), len(data.get("categories", []))
    except Exception:
        count, cats = 0, 0

    W, H = 1200, 630
    bg, ink, indigo, magenta, muted = (245, 245, 251), (20, 19, 31), (91, 75, 255), (224, 57, 154), (90, 88, 112)
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    # dotted vector field
    for y in range(40, H, 26):
        for x in range(40, W, 26):
            d.ellipse([x, y, x + 2, y + 2], fill=(215, 212, 232))
    # a few connecting lines (vector edges)
    for (x1, y1, x2, y2) in [(120, 470, 320, 360), (320, 360, 520, 430), (520, 430, 760, 350), (760, 350, 980, 440)]:
        d.line([(x1, y1), (x2, y2)], fill=(205, 198, 235), width=2)

    bold = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/Library/Fonts/Arial Bold.ttf"]
    mono = ["/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
            "/System/Library/Fonts/Menlo.ttc", "/System/Library/Fonts/Monaco.ttf"]
    f_kick = _font(mono, 24)
    f_h1 = _font(bold, 88)
    f_stat = _font(mono, 28)

    d.ellipse([70, 76, 92, 98], fill=indigo)
    d.text((104, 74), "THE RAG INDEX", font=f_kick, fill=indigo)
    d.text((68, 170), "The retrieval", font=f_h1, fill=ink)
    d.text((68, 270), "stack, mapped.", font=f_h1, fill=magenta)
    d.line([70, 460, W - 70, 460], fill=(205, 198, 235), width=2)
    d.text((70, 490), f"{count} tools  ·  {cats} categories  ·  ranked daily by GitHub momentum",
           font=f_stat, fill=muted)
    img.save(os.path.join(HERE, "og.png"))
    print(f"wrote og.png ({count} tools)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
