# -*- coding: utf-8 -*-
"""Generate the figures for the Kunguru concept deck as standalone SVG.

Helper block adapted from the cs4250 house style (gpu-slides/figs/makefigs.py),
recolored for the Kunguru palette from kunguru.net:
  #1a1a2e page bg, #16213e / #0f3460 dark blues, #e94560 accent, #ff6b6b light
  accent, #e0e0e0 / #a0a0a0 light grays. Figures are drawn for a dark
  background (transparent SVG over the deck's #1a1a2e slide bg).
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)))
INK, DARK, LIGHT = "#e0e0e0", "#ffffff", "#16213e"
MID, ACCENT, ACCENT2, GRAY = "#0f3460", "#e94560", "#ff6b6b", "#a0a0a0"
FONT = "Lato, 'Helvetica Neue', Helvetica, Arial, sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=15, anchor="start", fill=DARK, bold=False, italic=False, halo=False, op=1.0):
    st = f'font-family="{FONT}" font-size="{size}" fill="{fill}"'
    if op != 1.0:
        st += f' opacity="{op}"'
    if bold:
        st += ' font-weight="700"'
    if italic:
        st += ' font-style="italic"'
    if halo:
        st += ' paint-order="stroke" stroke="#1a1a2e" stroke-width="4.5" stroke-linejoin="round"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" {st}>{esc(s)}</text>'


def line(x1, y1, x2, y2, stroke=INK, w=2, dash=None, op=1.0, arrow=False):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    a = f' marker-end="url(#arw_{stroke[1:]})"' if arrow else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{w}" stroke-linecap="round"{d}{a} opacity="{op}"/>')


def rect(x, y, w, h, fill="none", stroke=INK, sw=2, rx=0, dash=None, op=1.0):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d} opacity="{op}"/>')


def circ(x, y, r, fill=INK, op=1.0):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" opacity="{op}"/>'


def path(d, fill="none", stroke=INK, w=2, dash=None, op=1.0):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{w}"{ds} opacity="{op}"/>'


def svg_doc(w, h, body):
    defs = (
        "<defs>"
        f'<marker id="arw_{ACCENT[1:]}" markerWidth="10" markerHeight="8" refX="8" refY="4" orient="auto">'
        f'<path d="M0,0 L10,4 L0,8 Z" fill="{ACCENT}"/></marker>'
        f'<marker id="arw_{INK[1:]}" markerWidth="10" markerHeight="8" refX="8" refY="4" orient="auto">'
        f'<path d="M0,0 L10,4 L0,8 Z" fill="{INK}"/></marker>'
        f'<marker id="arw_{GRAY[1:]}" markerWidth="10" markerHeight="8" refX="8" refY="4" orient="auto">'
        f'<path d="M0,0 L10,4 L0,8 Z" fill="{GRAY}"/></marker>'
        "</defs>"
    )
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}">{defs}{body}</svg>')


def write(name, doc):
    p = os.path.join(OUT, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote", p)


# ---------------------------------------------------------------- ladder ---

def fig_ladder():
    W, H = 1280, 655
    b = []
    # vertical axis: autonomy rises upward. Maintenance is deliberately NOT
    # on this axis — it is separable at any rung (see bottom annotation).
    b.append(line(55, 585, 55, 75, stroke=GRAY, w=2, arrow=True))
    b.append(f'<text x="22" y="330" font-family="{FONT}" font-size="16" fill="{GRAY}" '
             f'text-anchor="middle" transform="rotate(-90 22 330)">'
             f'autonomy · control</text>')

    rungs = [
        # (cx, platform_y, icon, title, subtitle, examples)
        (175, 490, "dorm", "College Dorm", "big tech product",
         "OneDrive · Gmail · Claude Agent Mode"),
        (405, 425, "board", "Boarded Room", "managed commodity",
         "managed NextCloud · Fastmail"),
        (635, 360, "apt", "Rented Apartment", "unmanaged rental",
         "unmanaged VPS rental"),
        (865, 295, "condo", "Condo", "owned unit, shared building",
         "your container or small VM"),
        (1095, 230, "house", "Owned House", "self-hosted",
         "your hardware, your premises"),
    ]

    def icon_dorm(cx, base):
        s = []
        w, h = 90, 120
        x, y = cx - w / 2, base - h
        s.append(rect(x, y, w, h, fill=LIGHT, stroke=INK, sw=2.5, rx=3))
        for r in range(4):
            for c in range(3):
                s.append(rect(x + 12 + c * 24, y + 10 + r * 22, 14, 12,
                              fill=MID, stroke="none", sw=0))
        s.append(rect(cx - 10, base - 22, 20, 22, fill=ACCENT, stroke="none", sw=0, rx=2))
        return "".join(s)

    def icon_board(cx, base):
        s = []
        w, h = 96, 58
        x, y = cx - w / 2, base - h
        # house body + roof
        s.append(rect(x + 6, y + 24, w - 12, h - 24, fill=LIGHT, stroke=INK, sw=2.5))
        s.append(path(f"M{x},{y + 26} L{cx},{y - 6} L{x + w},{y + 26}",
                      fill=LIGHT, stroke=INK, w=2.5))
        s.append(rect(cx - 8, base - 20, 16, 20, fill=ACCENT, stroke="none", sw=0, rx=2))
        # "room for rent" sign on a post — it's their house, your room
        sx = cx + w / 2 + 14
        s.append(line(sx + 20, base, sx + 20, base - 40, stroke=INK, w=2))
        s.append(rect(sx - 6, base - 62, 52, 22, fill=LIGHT, stroke=ACCENT2, sw=2, rx=3))
        s.append(txt(sx + 20, base - 47, "room", size=11, anchor="middle",
                     fill=ACCENT2, bold=True))
        return "".join(s)

    def icon_apt(cx, base):
        s = []
        w, h = 110, 80
        x, y = cx - w / 2, base - h
        s.append(rect(x, y, w, h, fill=LIGHT, stroke=INK, sw=2.5, rx=3))
        for i in range(2):
            s.append(rect(x + 14 + i * 58, y + 14, 24, 18, fill=MID, stroke="none", sw=0))
        s.append(rect(x + 14, y + 44, 24, 18, fill=MID, stroke="none", sw=0))
        s.append(rect(cx + 2, base - 36, 18, 36, fill=ACCENT, stroke="none", sw=0, rx=2))
        return "".join(s)

    def icon_condo(cx, base):
        s = []
        w, h = 100, 100
        x, y = cx - w / 2, base - h
        s.append(rect(x, y, w, h, fill=LIGHT, stroke=INK, sw=2.5, rx=3))
        # unit grid: divided walls, each unit separately owned
        s.append(line(cx, y + 8, cx, base - 8, stroke=INK, w=1.5, op=0.7))
        s.append(line(x + 8, y + 36, x + w - 8, y + 36, stroke=INK, w=1.5, op=0.7))
        s.append(line(x + 8, y + 64, x + w - 8, y + 64, stroke=INK, w=1.5, op=0.7))
        s.append(rect(cx - 26, y + 16, 18, 12, fill=MID, stroke="none", sw=0))
        s.append(rect(cx + 8, y + 44, 18, 12, fill=MID, stroke="none", sw=0))
        s.append(rect(cx - 26, y + 72, 18, 12, fill=MID, stroke="none", sw=0))
        s.append(rect(cx - 8, base - 26, 16, 26, fill=ACCENT, stroke="none", sw=0, rx=2))
        # the deed: you own the unit
        s.append(rect(cx + 12, y - 16, 44, 24, fill=LIGHT, stroke=ACCENT2, sw=2, rx=3))
        s.append(txt(cx + 34, y + 1, "deed", size=10.5, anchor="middle",
                     fill=ACCENT2, bold=True))
        s.append(circ(cx + 21, y - 4, 2.5, fill=ACCENT))
        return "".join(s)

    def icon_house(cx, base):
        s = []
        w, h = 110, 78
        x, y = cx - w / 2, base - h
        s.append(rect(x + 20, y + 2, 11, 20, fill=MID, stroke=INK, sw=1.5))
        s.append(path(f"M{x},{y + 34} L{cx},{y - 8} L{x + w},{y + 34}",
                      fill=LIGHT, stroke=INK, w=2.5))
        s.append(rect(x + 8, y + 34, w - 16, h - 34, fill=LIGHT, stroke=INK, sw=2.5))
        s.append(rect(x + 45, base - 32, 20, 32, fill=ACCENT, stroke="none", sw=0, rx=2))
        s.append(rect(x + 16, y + 46, 18, 16, fill=MID, stroke="none", sw=0))
        return "".join(s)

    icons = {"dorm": icon_dorm, "board": icon_board, "apt": icon_apt,
             "condo": icon_condo, "house": icon_house}

    prev_top = None
    for cx, py, ic, title, sub, ex in rungs:
        # step platform
        b.append(rect(cx - 100, py, 200, 14, fill=MID, stroke="none", sw=0, rx=3))
        b.append(icons[ic](cx, py - 4))
        b.append(txt(cx, py + 42, title, size=19, anchor="middle", bold=True))
        b.append(txt(cx, py + 64, sub, size=13.5, anchor="middle", fill=ACCENT2))
        b.append(txt(cx, py + 86, ex, size=11, anchor="middle", fill=GRAY))
        if prev_top is not None:
            b.append(line(prev_top[0] + 100, prev_top[1] + 7, cx - 100, py + 7,
                          stroke=GRAY, w=1.5, dash="4 5", op=0.6))
        prev_top = (cx, py)

    # dashed connector from axis to first step
    b.append(line(55, 497, 75, 497, stroke=GRAY, w=1.5, dash="4 5", op=0.6))
    # maintenance is separable — it rides alongside the ladder, not up it
    b.append(txt(W / 2, 630, "the wrench is separable — maintenance can be hired at any rung,",
                 size=14, anchor="middle", fill=GRAY, italic=True))
    b.append(txt(W / 2, 650, "by whoever holds no deed and no keys",
                 size=14, anchor="middle", fill=GRAY, italic=True))
    write("fig-ladder.svg", svg_doc(W, H, "".join(b)))


# ------------------------------------------------------------ architecture ---

def fig_architecture():
    W, H = 1160, 560
    b = []

    def box(x, y, w, h, title, caption_lines, icon_fn):
        s = [rect(x, y, w, h, fill=LIGHT, stroke=ACCENT, sw=2.5, rx=10)]
        s.append(icon_fn(x + w / 2, y + 44))
        s.append(txt(x + w / 2, y + 118, title, size=19, anchor="middle", bold=True))
        for i, ln in enumerate(caption_lines):
            s.append(txt(x + w / 2, y + 146 + i * 22, ln, size=14,
                         anchor="middle", fill=GRAY))
        return "".join(s)

    def icon_devices(cx, cy):
        s = []
        s.append(rect(cx - 42, cy - 28, 26, 48, fill=MID, stroke=INK, sw=2, rx=4))   # phone
        s.append(rect(cx - 34, cy + 14, 10, 3, fill=INK, stroke="none", sw=0))
        s.append(path(f"M{cx - 2},{cy + 26} L{cx + 46},{cy + 26} L{cx + 38},{cy - 22} "
                      f"L{cx - 10},{cy - 22} Z", fill=MID, stroke=INK, w=2))         # laptop
        return "".join(s)

    def icon_cloud(cx, cy):
        s = []
        s.append(path(f"M{cx - 44},{cy + 14} A18,18 0 0,1 {cx - 28},{cy - 16} "
                      f"A22,22 0 0,1 {cx + 14},{cy - 22} A18,18 0 0,1 {cx + 40},{cy - 2} "
                      f"A14,14 0 0,1 {cx + 44},{cy + 14} Z", fill=MID, stroke=INK, w=2))
        return "".join(s)

    def icon_server(cx, cy):
        s = []
        s.append(rect(cx - 34, cy - 26, 68, 54, fill=MID, stroke=INK, sw=2, rx=5))
        for i in range(3):
            s.append(rect(cx - 26, cy - 18 + i * 16, 44, 9, fill=LIGHT, stroke=INK, sw=1.2, rx=2))
            s.append(circ(cx + 24, cy - 13.5 + i * 16, 2.6, fill=ACCENT))
        return "".join(s)

    def icon_chip(cx, cy):
        s = []
        for i in range(5):  # pins
            s.append(line(cx - 30 + i * 15, cy - 32, cx - 30 + i * 15, cy - 22, stroke=INK, w=2))
            s.append(line(cx - 30 + i * 15, cy + 22, cx - 30 + i * 15, cy + 32, stroke=INK, w=2))
        s.append(rect(cx - 34, cy - 22, 68, 44, fill=MID, stroke=INK, sw=2, rx=4))
        s.append(rect(cx - 18, cy - 10, 36, 20, fill=ACCENT, stroke="none", sw=0, rx=2))
        return "".join(s)

    y0, bw, bh, gap = 60, 240, 240, 55
    xs = [40, 40 + bw + gap, 40 + 2 * (bw + gap), 40 + 3 * (bw + gap)]
    b.append(box(xs[0], y0, bw, bh, "Your Devices",
                 ["phone · laptop · anything", "with a browser or client"], icon_devices))
    b.append(box(xs[1], y0, bw, bh, "Gateway",
                 ["public internet address", "cloud VPS — could-snoop or", "can't-snoop setup"],
                 icon_cloud))
    b.append(box(xs[2], y0, bw, bh, "Agent Server",
                 ["persistent user data lives here", "Hermes agent — Linux user", "account or container"],
                 icon_server))
    b.append(box(xs[3], y0, bw, bh, "LLM Provider",
                 ["generates responses", "on-prem · direct API ·", "resold · OpenRouter"], icon_chip))

    def arrow(x1, x2, label, sub=None):
        s = [line(x1, y0 + 100, x2, y0 + 100, stroke=ACCENT, w=2.5, arrow=True)]
        s.append(txt((x1 + x2) / 2, y0 + 86, label, size=13, anchor="middle", fill=ACCENT2, bold=True))
        if sub:
            s.append(txt((x1 + x2) / 2, y0 + 126, sub, size=11.5, anchor="middle", fill=GRAY))
        return "".join(s)

    b.append(arrow(xs[0] + bw, xs[1], "chat · tasks"))
    b.append(arrow(xs[1] + bw, xs[2], "chat · tasks"))
    b.append(arrow(xs[2] + bw, xs[3], "requests", "responses back"))

    # trust emphasis under agent server
    b.append(txt(xs[2] + bw / 2, y0 + bh + 34, "most privacy/autonomy-critical component",
                 size=13.5, anchor="middle", fill=ACCENT, bold=True))
    b.append(txt(W / 2, y0 + bh + 66, "three separable services — each independently placeable on the control spectrum",
                 size=15, anchor="middle", fill=GRAY, italic=True))
    write("fig-architecture.svg", svg_doc(W, H, "".join(b)))


if __name__ == "__main__":
    fig_ladder()
    fig_architecture()
