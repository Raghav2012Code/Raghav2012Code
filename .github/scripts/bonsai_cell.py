"""Compose output/bonsai.gif into the README's bonsai art: output/bonsai-hero.gif.

The README (reference-style layout) floats this image right of its "A little
more about me" code block, where it stands in for the pixel-art coder gif of the
layout it follows. It was originally composed as the side-build cell of the
sheet design, which now lives on the old-design branch; the composition is
unchanged.

This image draws no lines of its own, and the canvas is transparent rather than
sheet-white, so the art reads equally in GitHub light and dark modes.
Transparency is decided by the tree's own alpha channel, never by colour-keying,
so white blossoms or highlights in future trees can never punch holes. One
palette is built from every frame composited on white (colours cannot shift or
flicker between frames), index 255 is reserved for transparency, and disposal=2
restores the background each frame so the animation cannot smear.

The tree is scaled by a whole number with nearest-neighbour so every art pixel
stays square, centred horizontally, and bottom-anchored with a transparent
margin below the pot. The canvas is 2x its 140x174 layout size so the art stays
sharp on high-DPI screens.
"""
import pathlib
import sys

from PIL import Image, ImageSequence

SRC = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "output/bonsai.gif")
OUT = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "output/bonsai-hero.gif")

SCALE = 2
W, H = 156 * SCALE, 198 * SCALE     # hero canvas, 2x the 156x198 layout size; fits a 3x tree up to ~98x126
SIDE, BOTTOM = 4 * SCALE, 6 * SCALE # transparent margins; the tree is bottom-anchored on the canvas
BOX_W, BOX_H = W - 2 * SIDE, H - BOTTOM - 3 * SCALE   # 3px of headroom keeps the crown off the top edge
PAPER = (255, 255, 255)
TRANSPARENT_INDEX = 255


def cell_frame_rgba(tree, size):
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    t = tree.resize(size, Image.NEAREST)
    x = (W - size[0]) // 2
    y = H - BOTTOM - size[1]
    canvas.paste(t, (x, y), t)
    return canvas


def main():
    src = Image.open(SRC)
    frames, durations = [], []
    for fr in ImageSequence.Iterator(src):
        frames.append(fr.convert("RGBA"))
        durations.append(fr.info.get("duration", src.info.get("duration", 100)))
    w, h = frames[0].size
    k = min(BOX_W / w, BOX_H / h)
    if k >= 1:
        k = int(k)              # whole-number scale keeps every art pixel square
    size = (max(1, round(w * k)), max(1, round(h * k)))

    rgba_frames = [cell_frame_rgba(f, size) for f in frames]
    # one palette built from every frame on white, so colours cannot shift or
    # flicker between frames; 255 colours leaves index 255 free for transparency
    white = Image.new("RGBA", (W, H), PAPER + (255,))
    sheet = Image.new("RGB", (W, H * len(rgba_frames)), PAPER)
    for i, c in enumerate(rgba_frames):
        sheet.paste(Image.alpha_composite(white, c).convert("RGB"), (0, i * H))
    palette = sheet.quantize(colors=255, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    pal = palette.getpalette() + [0] * (768 - len(palette.getpalette()))
    pal[TRANSPARENT_INDEX * 3:TRANSPARENT_INDEX * 3 + 3] = [255, 0, 255]
    palette.putpalette(pal)

    out = []
    for c in rgba_frames:
        flat = Image.alpha_composite(white, c).convert("RGB")
        q = flat.quantize(palette=palette, dither=Image.Dither.NONE)
        alpha = c.split()[3]
        q.paste(TRANSPARENT_INDEX, mask=alpha.point(lambda a: 0 if a > 128 else 255))
        out.append(q)
    out[0].save(OUT, save_all=True, append_images=out[1:], duration=durations,
                loop=src.info.get("loop", 0), transparency=TRANSPARENT_INDEX,
                disposal=2, optimize=False)
    print(f"{OUT}: {len(out)} frames, tree {w}x{h} -> {size[0]}x{size[1]}, transparent")


if __name__ == "__main__":
    main()
