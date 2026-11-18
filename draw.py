#!/usr/bin/env python3
"""Draw entry.png for news-image-20261117: Tuesday 17 November 2026.

One 1024x1024 newspaper front page, drawn with Pillow + DejaVu only.
Deterministic: no random, no network, no timestamps in the PNG.
Run: python3 draw.py  -> writes entry.png beside this file.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (17, 17, 17)
NAVY = (18, 38, 74)
RED = (178, 34, 34)
BLUE = (30, 90, 160)
TEAL = (14, 110, 110)
ORANGE = (214, 92, 20)
GREEN = (30, 120, 60)
GREY = (90, 90, 90)
WHITE = (255, 255, 255)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIFB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, color, width, leading=4):
    lines = wrap(draw, text, fnt, width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=color)
        y += fnt.size + leading
    return y


def card(draw, x, y, w, h, accent, kicker, headline, body, head_size=30):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10,
                           fill=WHITE, outline=INK, width=2)
    draw.rounded_rectangle([x, y, x + w, y + 34], radius=10, fill=accent)
    draw.rectangle([x, y + 20, x + w, y + 34], fill=accent)
    draw.text((x + 12, y + 6), kicker, font=font(SANSB, 17), fill=WHITE)
    yy = text_block(draw, x + 12, y + 44, headline, font(SANSB, head_size),
                    INK, w - 24, leading=2)
    text_block(draw, x + 12, yy + 4, body, font(SANS, 19), INK, w - 24, leading=3)
    return yy


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# Masthead
d.rectangle([0, 0, W, 118], fill=NAVY)
d.text((24, 10), "THE WORLD IN ONE DAY", font=font(SANSB, 26), fill=(255, 214, 90))
d.text((24, 38), "TUESDAY 17 NOVEMBER 2026", font=font(SERIFB, 52), fill=WHITE)
d.text((24, 96), "The day's world news  —  in one image",
       font=font(SANS, 20), fill=(200, 210, 230))

# ---- Lead: Crimea Bridge, full width ----
lx, ly, lw, lh = 16, 132, 992, 268
d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=10,
                    fill=WHITE, outline=INK, width=2)
d.rounded_rectangle([lx, ly, lx + lw, ly + 34], radius=10, fill=RED)
d.rectangle([lx, ly + 20, lx + lw, ly + 34], fill=RED)
d.text((lx + 12, ly + 6), "LEAD  •  UKRAINE", font=font(SANSB, 17), fill=WHITE)
d.text((lx + 14, ly + 44), "CRIMEA BRIDGE FALLS",
       font=font(SANSB, 38), fill=INK)
d.text((lx + 14, ly + 88),
       "Ukraine strikes the 19-km Kerch bridge;",
       font=font(SANS, 21), fill=INK)
d.text((lx + 14, ly + 114),
       "its road arch collapses into the sea.",
       font=font(SANS, 21), fill=INK)
d.text((lx + 14, ly + 142),
       "Russia hits Kyiv bridges in reply.",
       font=font(SANSB, 21), fill=RED)
# Bridge drawing, right half: deck with a broken middle, fallen span in water
bx, by = 560, 180
d.rectangle([bx, by + 150, bx + 400, by + 200], fill=(70, 140, 190))
for wx in range(bx + 10, bx + 390, 40):
    d.arc([wx, by + 155, wx + 36, by + 185], 0, 180, fill=WHITE, width=3)
d.rectangle([bx, by + 55, bx + 150, by + 68], fill=NAVY)  # deck, left
d.rectangle([bx + 250, by + 55, bx + 400, by + 68], fill=NAVY)  # deck, right
d.rectangle([bx + 20, by + 10, bx + 32, by + 68], fill=NAVY)  # tower left
d.rectangle([bx + 368, by + 10, bx + 380, by + 68], fill=NAVY)  # tower right
d.arc([bx + 30, by - 5, bx + 150, by + 60], 180, 360, fill=NAVY, width=6)
d.arc([bx + 250, by - 5, bx + 370, by + 60], 180, 360, fill=NAVY, width=6)
d.polygon([(bx + 165, by + 68), (bx + 235, by + 68), (bx + 215, by + 145),
           (bx + 185, by + 145)], fill=(120, 120, 120))  # fallen span

# ---- Row 2: Hormuz (left) and Manila summit (right) ----
y2, h2 = 416, 248
# Hormuz
hx, hw = 16, 488
d.rounded_rectangle([hx, y2, hx + hw, y2 + h2], radius=10,
                    fill=WHITE, outline=INK, width=2)
d.rounded_rectangle([hx, y2, hx + hw, y2 + 34], radius=10, fill=ORANGE)
d.rectangle([hx, y2 + 20, hx + hw, y2 + 34], fill=ORANGE)
d.text((hx + 12, y2 + 6), "MIDDLE EAST", font=font(SANSB, 17), fill=WHITE)
d.text((hx + 12, y2 + 44), "TANKERS ON FIRE", font=font(SANSB, 30), fill=INK)
d.text((hx + 12, y2 + 82), "IN THE STRAIT OF HORMUZ",
       font=font(SANSB, 22), fill=INK)
# tanker + flames
tx, ty = hx + 30, y2 + 150
d.rectangle([tx, ty, tx + 240, ty + 34], fill=INK)
d.rectangle([tx + 180, ty - 28, tx + 220, ty], fill=INK)
for fx, fh in [(tx + 20, 46), (tx + 70, 62), (tx + 130, 50), (tx + 185, 58)]:
    d.polygon([(fx, ty), (fx + 18, ty - fh), (fx + 36, ty)], fill=ORANGE)
d.rectangle([tx - 10, ty + 34, tx + 260, ty + 58], fill=(70, 140, 190))
d.text((hx + 12, y2 + 214),
       "US strikes Qeshm Island after tanker attacks.",
       font=font(SANS, 18), fill=INK)
# Manila
mx, mw = 520, 488
d.rounded_rectangle([mx, y2, mx + mw, y2 + h2], radius=10,
                    fill=WHITE, outline=INK, width=2)
d.rounded_rectangle([mx, y2, mx + mw, y2 + 34], radius=10, fill=BLUE)
d.rectangle([mx, y2 + 20, mx + mw, y2 + 34], fill=BLUE)
d.text((mx + 12, y2 + 6), "ASIA", font=font(SANSB, 17), fill=WHITE)
d.text((mx + 12, y2 + 44), "TRUMP LANDS IN MANILA",
       font=font(SANSB, 29), fill=INK)
d.text((mx + 12, y2 + 82), "SUMMIT WITH XI AND PUTIN NEXT",
       font=font(SANSB, 20), fill=INK)
# three flags: USA stripes + canton, China red + star, Russia white/blue/red
for i, lab in enumerate(["USA", "CHINA", "RUSSIA"]):
    fx = mx + 30 + i * 150
    fy = y2 + 130
    if i == 0:
        for s in range(7):
            d.rectangle([fx, fy + s * 9, fx + 110, fy + s * 9 + 9],
                        fill=RED if s % 2 == 0 else WHITE)
        d.rectangle([fx, fy, fx + 46, fy + 27], fill=NAVY)
    elif i == 1:
        d.rectangle([fx, fy, fx + 110, fy + 62], fill=(200, 20, 20))
        d.text((fx + 38, fy + 14), "*", font=font(SANSB, 30), fill=(255, 220, 0))
    else:
        d.rectangle([fx, fy, fx + 110, fy + 62], fill=WHITE)
        d.rectangle([fx, fy + 21, fx + 110, fy + 41], fill=(30, 90, 200))
        d.rectangle([fx, fy + 41, fx + 110, fy + 62], fill=RED)
    d.rectangle([fx, fy, fx + 110, fy + 62], outline=INK, width=2)
    d.text((fx + 28, fy + 70), lab, font=font(SANSB, 18), fill=INK)
d.text((mx + 12, y2 + 214),
       "ASEAN and Quad talks; trilateral summit Thursday.",
       font=font(SANS, 18), fill=INK)

# ---- Row 3: Measles (left) and Nvidia (right) ----
y3, h3 = 680, 212
# Measles
ax, aw = 16, 488
d.rounded_rectangle([ax, y3, ax + aw, y3 + h3], radius=10,
                    fill=WHITE, outline=INK, width=2)
d.rounded_rectangle([ax, y3, ax + aw, y3 + 34], radius=10, fill=RED)
d.rectangle([ax, y3 + 20, ax + aw, y3 + 34], fill=RED)
d.text((ax + 12, y3 + 6), "HEALTH  •  USA", font=font(SANSB, 17), fill=WHITE)
d.text((ax + 12, y3 + 44), "US LOSES MEASLES-FREE",
       font=font(SANSB, 27), fill=INK)
d.text((ax + 12, y3 + 76), "STATUS",
       font=font(SANSB, 27), fill=INK)
d.text((ax + 12, y3 + 112), "First time in 26 years: 5,400+ cases,",
       font=font(SANS, 18), fill=INK)
d.text((ax + 12, y3 + 134), "10 deaths reported.",
       font=font(SANS, 18), fill=INK)
for cx, cy, r in [(430, y3 + 125, 20), (455, y3 + 165, 13)]:
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED, outline=(120, 0, 0), width=2)
    for dx, dy in [(0, -r), (0, r), (-r, 0), (r, 0)]:
        d.line([cx, cy, cx + dx, cy + dy], fill=(120, 0, 0), width=3)
d.text((ax + 12, y3 + 168), "Elimination status lost after 26 years.",
       font=font(SANSB, 17), fill=RED)
# Nvidia
nx, nw = 520, 488
d.rounded_rectangle([nx, y3, nx + nw, y3 + h3], radius=10,
                    fill=WHITE, outline=INK, width=2)
d.rounded_rectangle([nx, y3, nx + nw, y3 + 34], radius=10, fill=GREEN)
d.rectangle([nx, y3 + 20, nx + nw, y3 + 34], fill=GREEN)
d.text((nx + 12, y3 + 6), "TECH", font=font(SANSB, 17), fill=WHITE)
d.text((nx + 12, y3 + 44), "NVIDIA IN TURMOIL",
       font=font(SANSB, 30), fill=INK)
d.text((nx + 12, y3 + 82), "Chief Jensen Huang resigns amid",
       font=font(SANS, 19), fill=INK)
d.text((nx + 12, y3 + 106), "a scandal; record revenue.",
       font=font(SANS, 19), fill=INK)
# chip, kept clear of the headline and body text (right edge, lower)
cx, cy = nx + 395, y3 + 155
d.rectangle([cx - 48, cy - 48, cx + 48, cy + 48], fill=GREEN, outline=INK, width=3)
d.rectangle([cx - 24, cy - 24, cx + 24, cy + 24], fill=(200, 240, 200), outline=INK, width=2)
d.text((cx - 20, cy - 11), "AI", font=font(SANSB, 24), fill=INK)
for i in range(4):
    d.line([cx - 48 + i * 28, cy - 48, cx - 48 + i * 28, cy - 62], fill=INK, width=3)
    d.line([cx - 48 + i * 28, cy + 48, cx - 48 + i * 28, cy + 62], fill=INK, width=3)
d.text((nx + 12, y3 + 168), "US tightens chip-export rules.",
       font=font(SANSB, 17), fill=GREEN)

# ---- Bottom strip ----
sy, sh = 908, 100
d.rounded_rectangle([16, sy, 1008, sy + sh], radius=10,
                    fill=NAVY, outline=INK, width=2)
d.text((28, sy + 12), "ALSO TODAY:", font=font(SANSB, 18), fill=(255, 214, 90))
d.text((28, sy + 38), "EU states plan a Rwanda return hub  •  Winter rains deepen Gaza's shelter crisis",
       font=font(SANS, 18), fill=WHITE)
d.text((28, sy + 62), "Russian plane crashes in Siberia — all 19 aboard killed",
       font=font(SANS, 18), fill=WHITE)

img.save("entry.png", optimize=True)
print("wrote entry.png", img.size)
