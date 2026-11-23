#!/usr/bin/env python3
"""Draw the news23 v2 front page: 1 headline + 13 small panels, 8 regions.

All panel text comes from ~/workspace/makefun/news23-facts.json (44 verified
stories, 23 November 2026). Nothing is invented: every number and name below
is copied from that file. Output is a deterministic 1024x1024 PNG.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (22, 22, 22)
MUTED = (85, 85, 85)
CARD = (255, 255, 255)
BORDER = (216, 210, 196)
NAVY = (22, 35, 63)
GOLD = (232, 182, 76)
DECK = (207, 216, 230)

REGION_COLORS = {
    "Europe": (31, 78, 156),
    "Asia": (179, 32, 46),
    "Middle East": (178, 106, 0),
    "Americas": (30, 125, 79),
    "Economy": (106, 63, 160),
    "Africa": (15, 118, 110),
    "Sport": (194, 65, 12),
    "Space/Tech": (71, 85, 105),
}

F_SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
F_SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def chip(d, x, y, text, color, f):
    tw = d.textlength(text, font=f)
    pad_x, pad_y = 8, 4
    d.rounded_rectangle([x, y, x + tw + 2 * pad_x, y + f.size + 2 * pad_y],
                        radius=3, fill=color)
    d.text((x + pad_x, y + pad_y), text, font=f, fill=(255, 255, 255))


def main(out_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.rectangle([0, 0, W, 92], fill=(17, 17, 17))
    f_title = font(F_SERIF_B, 38)
    d.text((24, 26), "THE WORLD IN ONE DAY", font=f_title, fill=(255, 255, 255))
    f_date = font(F_SANS_B, 23)
    date = "MONDAY · 23 NOVEMBER 2026"
    d.text((W - 24 - d.textlength(date, font=f_date), 24), date,
           font=f_date, fill=GOLD)
    f_sub = font(F_SANS, 15)
    sub = "14 STORIES · 8 REGIONS"
    d.text((W - 24 - d.textlength(sub, font=f_sub), 56), sub,
           font=f_sub, fill=(204, 204, 204))

    # ---- Hero: headline panel (left) + COP31 side panel (right) --------
    # Headline panel
    d.rounded_rectangle([16, 104, 664, 396], radius=6, fill=NAVY)
    f_tag = font(F_SANS_B, 14)
    chip(d, 44, 122, "EUROPE", REGION_COLORS["Europe"], f_tag)
    f_head = font(F_SANS_B, 42)
    head_lines = wrap(d, "Russian overnight strike on Dymer kills up to 15 in Kyiv region",
                      f_head, 592)
    y = 156
    for ln in head_lines:
        d.text((44, y), ln, font=f_head, fill=(255, 255, 255))
        y += 50
    f_deck = font(F_SANS, 19)
    deck = ("11 dead in one apartment block in Dymer; a boy aged 7 and a woman "
            "aged 79 rescued after 22 hours.")
    y += 8
    for ln in wrap(d, deck, f_deck, 592):
        d.text((44, y), ln, font=f_deck, fill=DECK)
        y += 25
    f_stamp = font(F_SANS_B, 13)
    d.text((44, 372), "23 NOV 2026 · KYIV REGION, UKRAINE", font=f_stamp, fill=GOLD)

    # Side panel: COP31
    d.rounded_rectangle([676, 104, 1008, 396], radius=6, fill=CARD,
                        outline=BORDER, width=1)
    d.rectangle([676, 104, 1008, 110], fill=REGION_COLORS["Europe"])
    chip(d, 692, 122, "EUROPE", REGION_COLORS["Europe"], f_tag)
    f_side = font(F_SANS_B, 27)
    y = 154
    for ln in wrap(d, "COP31 ends with no climate deal", f_side, 300):
        d.text((692, y), ln, font=f_side, fill=INK)
        y += 33
    f_sdet = font(F_SANS, 15)
    y += 6
    for ln in wrap(d, "$120bn-a-year adaptation target scrapped; 90+ nations back "
                      "electrification.", f_sdet, 300):
        d.text((692, y), ln, font=f_sdet, fill=MUTED)
        y += 20
    d.text((692, 372), "23 NOV 2026 · ANTALYA", font=f_stamp, fill=MUTED)

    # ---- Grid: 12 tiles, 3 cols x 4 rows -------------------------------
    tiles = [
        ("Europe", "Ukraine sinks Russian corvette Merkury off Libya",
         "7 naval drones; Ka-27 destroyed"),
        ("Europe", "3 Russian missiles fall in Poland; NATO meets",
         "Rutte: pre-1997 demands 'unacceptable'"),
        ("Asia", "China cuts stock margin floor to 80%",
         "Frees 400bn yuan ($55bn+) from Nov 30"),
        ("Asia", "Tata Steel buys 26.4% of APL Apollo for $1.67bn",
         "26.38% stake; open offer for 26% more"),
        ("Middle East", "Iran vows 'every means' to break Hormuz blockade",
         "Trump threatens new strikes"),
        ("Middle East", "Report blames Israel for toxic pollution in 99% of Gaza",
         "War turned Gaza into 'a toxic wasteland'"),
        ("Americas", "Record FAA ground stop: 4–5 hours, longest in 25 years",
         "Only the 2nd nationwide stop since 9/11"),
        ("Americas", "Senate GOP open to cutting Iran war funds",
         "Dec 11 shutdown deadline looms"),
        ("Economy", "AI stock rout: Nikkei -4.8%, KOSPI -4.7%",
         "Anthropic IPO $81.3bn, opened $111.50"),
        ("Africa", "WHO urges calm as Ebola-hit DR Congo fighting grows",
         "Fighting in Ituri endangers vaccine teams"),
        ("Sport", "India 720-9 declared; Test vs NZ ends in draw",
         "Pant's record 9th Test century"),
        ("Space/Tech", "OpenAI chief proposes 'perplexity' limits on frontier AI",
         "Pachocki plan; Altman endorses it"),
    ]
    f_tile_tag = font(F_SANS_B, 14)
    f_tile = font(F_SANS_B, 22)
    f_tile_det = font(F_SANS, 14)
    f_tile_date = font(F_SANS_B, 11)
    xs = [16, 350, 684]
    ys = [408, 560, 712, 864]
    for i, (region, head, det) in enumerate(tiles):
        x = xs[i % 3]
        y = ys[i // 3]
        color = REGION_COLORS[region]
        d.rounded_rectangle([x, y, x + 324, y + 142], radius=5, fill=CARD,
                            outline=BORDER, width=1)
        d.rectangle([x, y, x + 324, y + 5], fill=color)
        chip(d, x + 12, y + 13, region.upper(), color, f_tile_tag)
        d.text((x + 324 - 12 - d.textlength("23 NOV", font=f_tile_date), y + 16),
               "23 NOV", font=f_tile_date, fill=MUTED)
        hy = y + 42
        for ln in wrap(d, head, f_tile, 300)[:3]:
            d.text((x + 12, hy), ln, font=f_tile, fill=INK)
            hy += 26
        det_trunc = det
        while d.textlength(det_trunc, font=f_tile_det) > 296 and " " in det_trunc:
            det_trunc = det_trunc.rsplit(" ", 1)[0] + "…"
        d.text((x + 12, y + 120), det_trunc, font=f_tile_det, fill=MUTED)

    img.save(out_path, format="PNG")
    print("saved", out_path)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "entry.png")
