"""Trim a raw spread to the 2:1 print shape with an even, centred crop.

A 16:9 source loses a strip off the top and bottom; a 21:9 source loses a strip off the left and right.

Usage: python crop_to_2x1.py "Spread 01 - raw.png" "Spread 01 - 2x1.png" [top_offset]

top_offset (optional, 16:9 sources only) sets how many pixels to trim from the top instead
of an even split, e.g. 40 keeps more sky above text that sits close to the top edge.
"""
import sys
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src)
w, h = im.size
if w / h > 2:  # wider than 2:1: trim the sides
    new_w, new_h = 2 * h, h
else:  # taller than 2:1: trim the top and bottom
    new_w, new_h = w, w // 2
left, top = (w - new_w) // 2, (h - new_h) // 2
if len(sys.argv) > 3 and new_h < h:
    top = max(0, min(h - new_h, int(sys.argv[3])))
out = im.crop((left, top, left + new_w, top + new_h))
out.save(dst)
print(f"{w}x{h} -> {out.size[0]}x{out.size[1]}")
