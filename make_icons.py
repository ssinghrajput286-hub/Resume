"""Draws the app icon + splash used by @capacitor/assets. Needs: pip install pillow"""
import os
from PIL import Image, ImageDraw

INK = (21, 25, 59, 255)
GOLD = (255, 179, 0, 255)
PINK = (255, 77, 141, 255)
WHITE = (255, 255, 255, 255)

os.makedirs("assets", exist_ok=True)


def paper(draw, cx, cy, w):
    """A resume sheet with a folded corner, a photo dot and text lines."""
    h = int(w * 1.28)
    x0, y0, x1, y1 = cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2
    fold = int(w * 0.28)
    draw.polygon([(x0, y0), (x1 - fold, y0), (x1, y0 + fold), (x1, y1), (x0, y1)], fill=WHITE)
    draw.polygon([(x1 - fold, y0), (x1, y0 + fold), (x1 - fold, y0 + fold)], fill=(220, 224, 245, 255))
    r = int(w * 0.13)
    px, py = x0 + int(w * 0.28), y0 + int(h * 0.27)
    draw.ellipse([px - r, py - r, px + r, py + r], fill=GOLD)
    lx = px + r + int(w * 0.07)
    lh = max(6, int(w * 0.055))
    draw.rounded_rectangle([lx, py - lh - 4, x1 - int(w * 0.12), py - 4], lh // 2, fill=INK)
    draw.rounded_rectangle([lx, py + 6, x1 - int(w * 0.3), py + 6 + lh], lh // 2, fill=PINK)
    y = y0 + int(h * 0.50)
    for i, frac in enumerate([0.78, 0.78, 0.6, 0.78, 0.5]):
        draw.rounded_rectangle([x0 + int(w * 0.12), y, x0 + int(w * 0.12) + int(w * frac * 0.9), y + lh],
                               lh // 2, fill=(200, 205, 235, 255))
        y += int(lh * 2.1)


# full icon (rounded look handled by Android adaptive mask)
icon = Image.new("RGBA", (1024, 1024), INK)
d = ImageDraw.Draw(icon)
d.ellipse([620, -120, 1160, 420], fill=GOLD)
d.ellipse([-140, 700, 300, 1140], fill=(79, 70, 229, 255))
paper(d, 512, 520, 470)
icon.save("assets/icon-only.png")

# adaptive icon layers (keep artwork inside the central safe zone)
fg = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
paper(ImageDraw.Draw(fg), 512, 520, 400)
fg.save("assets/icon-foreground.png")
Image.new("RGBA", (1024, 1024), INK).save("assets/icon-background.png")

# splash
for name in ("splash.png", "splash-dark.png"):
    s = Image.new("RGBA", (2732, 2732), INK)
    paper(ImageDraw.Draw(s), 1366, 1366, 520)
    s.save("assets/" + name)
print("icons ok")
