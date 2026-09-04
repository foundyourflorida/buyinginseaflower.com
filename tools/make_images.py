"""Generate brand images (Open Graph default, favicon, apple-touch-icon) with Pillow."""
import math, os
from PIL import Image, ImageDraw, ImageFont

CREAM, GREEN, GREEN_DARK, CORAL, SAND, MUTED = (250, 240, 222), (30, 85, 64), (15, 46, 36), (232, 121, 107), (241, 227, 203), (95, 109, 102)
FONT_DIRS = ["/System/Library/Fonts/Supplemental", "/Library/Fonts", "/System/Library/Fonts", os.path.expanduser("~/Library/Fonts")]


def font(names, size):
    for n in names:
        for d in FONT_DIRS:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def petal_points(cx, cy, rx, ry, offset, angle_deg, n=48):
    a = math.radians(angle_deg)
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        x, y = rx * math.cos(t), ry * math.sin(t) - offset
        pts.append((cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a)))
    return pts


def draw_flower(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=CREAM)
    for ang in range(0, 360, 60):
        draw.polygon(petal_points(cx, cy, r * 0.24, r * 0.47, r * 0.44, ang), fill=CORAL)
    c = r * 0.25
    draw.ellipse([cx - c, cy - c, cx + c, cy + c], fill=GREEN)
    c2 = r * 0.1
    draw.ellipse([cx - c2, cy - c2, cx + c2, cy + c2], fill=CREAM)


def og_image(path, title="Buying in SeaFlower", subtitle="The independent buyer's guide to SeaFlower, Bradenton FL", kicker="FROM A FORMER BUILDER INSIDER"):
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(im)
    # soft sand band on the right
    d.rectangle([840, 0, W, H], fill=SAND)
    d.rectangle([0, H - 14, W, H], fill=GREEN)
    d.rectangle([0, H - 14, 300, H], fill=CORAL)
    serif = font(["Georgia Bold.ttf", "Georgia-Bold.ttf", "Times New Roman Bold.ttf", "Baskerville.ttc"], 92)
    serif_sm = font(["Georgia.ttf", "Times New Roman.ttf"], 34)
    sans = font(["HelveticaNeue.ttc", "Helvetica.ttc", "Arial.ttf"], 24)
    sans_b = font(["HelveticaNeue.ttc", "Helvetica.ttc", "Arial Bold.ttf", "Arial.ttf"], 22)
    # kicker
    d.text((80, 96), kicker, font=sans_b, fill=CORAL)
    # title (wrap two lines if needed)
    words, lines, cur = title.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textlength(t, font=serif) > 700 and cur:
            lines.append(cur); cur = wd
        else:
            cur = t
    lines.append(cur)
    y = 140
    for ln in lines[:3]:
        d.text((80, y), ln, font=serif, fill=GREEN_DARK); y += 104
    # subtitle wrapped
    words, cur, y = subtitle.split(), "", y + 14
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textlength(t, font=serif_sm) > 700 and cur:
            d.text((80, y), cur, font=serif_sm, fill=MUTED); y += 44; cur = wd
        else:
            cur = t
    if cur:
        d.text((80, y), cur, font=serif_sm, fill=MUTED)
    d.text((80, H - 70), "buyinginseaflower.com  ·  Found Your Florida  ·  Trenton Miller, LPT Realty", font=sans, fill=GREEN)
    draw_flower(d, 1020, 250, 150)
    im.save(path, "JPEG", quality=88, optimize=True)


def icon_png(path, size):
    im = Image.new("RGBA", (size * 4, size * 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    r = size * 2
    d.rounded_rectangle([0, 0, size * 4 - 1, size * 4 - 1], radius=int(size * 0.9), fill=CREAM)
    draw_flower(d, r, r, int(r * 0.82))
    im = im.resize((size, size), Image.LANCZOS)
    im.save(path, "PNG", optimize=True)


def run(out_dir):
    img_dir = os.path.join(out_dir, "assets", "images")
    os.makedirs(img_dir, exist_ok=True)
    og_image(os.path.join(img_dir, "og-default.jpg"))
    icon_png(os.path.join(out_dir, "apple-touch-icon.png"), 180)
    icon_png(os.path.join(img_dir, "icon-512.png"), 512)
    icon_png(os.path.join(img_dir, "icon-192.png"), 192)
    ico = Image.open(os.path.join(img_dir, "icon-192.png")).convert("RGBA")
    ico.save(os.path.join(out_dir, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])


if __name__ == "__main__":
    import sys
    run(sys.argv[1] if len(sys.argv) > 1 else "docs")
