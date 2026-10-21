"""Compose output/bonsai.gif into the README's bonsai art: output/bonsai-tree.gif.

The README (reference-style layout) floats this image right of its "A little more
about me" code block, and the pot of the tree is level with the connect line
under that block. The tree is composed at the largest whole-number scale that
fits the canvas, then scaled to the height the line leaves, so the pot lands on
the text instead of hanging below it. A tree that composes smaller than that is
never scaled up, so the art never goes soft.

The canvas is transparent rather than sheet-white, so the art reads equally in
GitHub light and dark modes. Transparency is decided by the tree's own alpha
channel, never by colour-keying, so white blossoms or highlights in future
trees can never punch holes. One palette is built from every frame composited
on white (colours cannot shift or flicker between frames), index 255 is
reserved for transparency, and disposal=2 restores the background each frame so
the animation cannot smear.
"""
import pathlib
import sys

from PIL import Image, ImageSequence

SRC = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "output/bonsai.gif")
OUT = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "output/bonsai-tree.gif")

COMPOSE_W = 300        # the widest the tree is composed at, in canvas pixels
TARGET_H = 293         # the height the README gives the art: float top to the line below
SIDE, BOTTOM = 8, 4    # transparent margins around the tree, in canvas pixels
PAPER = (255, 255, 255)
TRANSPARENT_INDEX = 255


def scale_rgba(image, size):
    """Resize an RGBA image without letting its colour bleed into the transparency."""
    r, g, b, a = image.split()
    return Image.merge("RGBA", (r.resize(size, Image.LANCZOS),
                                g.resize(size, Image.LANCZOS),
                                b.resize(size, Image.LANCZOS),
                                a.resize(size, Image.LANCZOS)))


def art_frame(tree, size, canvas):
    """Draw the tree at the top of a transparent canvas, centred, pot on the last row."""
    frame = Image.new("RGBA", canvas, (0, 0, 0, 0))
    x = (canvas[0] - size[0]) // 2
    frame.paste(tree, (x, 0), tree)
    return frame


def main():
    src = Image.open(SRC)
    frames, durations = [], []
    for fr in ImageSequence.Iterator(src):
        frames.append(fr.convert("RGBA"))
        durations.append(fr.info.get("duration", src.info.get("duration", 100)))
    w, h = frames[0].size

    # the whole-number scale keeps every art pixel square, the downscale below
    # then fits the tree to the height the README has for it
    k = max(1, int(COMPOSE_W / w))
    composed = (max(1, round(w * k)), max(1, round(h * k)))
    scale = min(1.0, TARGET_H / composed[1])
    art = (max(1, round(composed[0] * scale)), max(1, round(composed[1] * scale)))
    canvas = (art[0] + 2 * SIDE, art[1] + BOTTOM)

    rgba_frames = []
    for f in frames:
        t = f.resize(composed, Image.NEAREST)
        if scale < 1.0:
            t = scale_rgba(t, art)
        rgba_frames.append(art_frame(t, art, canvas))

    # one palette built from every frame on white, so colours cannot shift
    white = Image.new("RGBA", canvas, PAPER + (255,))
    sheet = Image.new("RGB", (canvas[0], canvas[1] * len(rgba_frames)), PAPER)
    for i, c in enumerate(rgba_frames):
        sheet.paste(Image.alpha_composite(white, c).convert("RGB"), (0, i * canvas[1]))
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
    print(f"{OUT}: {len(out)} frames, tree {w}x{h} -> {art[0]}x{art[1]}, transparent")


if __name__ == "__main__":
    main()
