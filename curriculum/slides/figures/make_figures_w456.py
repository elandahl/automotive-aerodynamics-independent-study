#!/usr/bin/env python3
"""Week 4–6 lecture figures: textbook line drawings."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle
import numpy as np

OUT = Path(__file__).resolve().parent
DPI = 220
FACE = "white"


def new_fig(w, h):
    fig, ax = plt.subplots(figsize=(w, h), dpi=DPI)
    fig.patch.set_facecolor(FACE)
    ax.set_facecolor(FACE)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def save(fig, name):
    path = OUT / name
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor=FACE, pad_inches=0.18)
    fig.savefig(path.with_suffix(".svg"), bbox_inches="tight", facecolor=FACE, pad_inches=0.18)
    plt.close(fig)
    print("wrote", path.name)


def tip(ax, x, y, dx, dy, *, color="black", lw=1.15, ms=10):
    ax.add_patch(
        FancyArrowPatch(
            (x, y),
            (x + dx, y + dy),
            arrowstyle="-|>",
            mutation_scale=ms,
            lw=lw,
            color=color,
            shrinkA=0,
            shrinkB=0,
            zorder=4,
        )
    )


def stream(ax, xs, ys, *, color="0.25", lw=1.05):
    ax.plot(xs, ys, color=color, lw=lw, zorder=1)
    tip(ax, xs[-5], ys[-5], xs[-1] - xs[-5], ys[-1] - ys[-5], color=color, lw=lw, ms=9)


def fig_continuity():
    fig, ax = new_fig(8.6, 4.0)
    # duct walls: wide, then narrow. Interior stays empty for the arrows.
    upper = [(0.55, 2.55), (2.55, 2.55), (3.35, 1.95), (7.15, 1.95)]
    lower = [(0.55, 0.45), (2.55, 0.45), (3.35, 1.05), (7.15, 1.05)]
    ax.plot(*zip(*upper), color="black", lw=1.6)
    ax.plot(*zip(*lower), color="black", lw=1.6)
    ax.plot([0.55, 0.55], [0.45, 2.55], color="black", lw=1.6)
    for y in (1.05, 1.50, 1.95):
        ax.plot([0.75, 2.15], [y, y], color="0.25", lw=1.05)
        tip(ax, 1.85, y, 0.30, 0, color="0.25", lw=1.05, ms=9)
    ax.plot([3.55, 6.55], [1.50, 1.50], color="0.25", lw=1.05)
    tip(ax, 6.15, 1.50, 0.40, 0, color="0.25", lw=1.05, ms=9)
    ax.annotate("", xy=(0.28, 0.45), xytext=(0.28, 2.55), arrowprops=dict(arrowstyle="<->", lw=1.1))
    ax.text(0.12, 1.50, r"$A_1$", ha="right", va="center", fontsize=13)
    ax.annotate("", xy=(7.45, 1.05), xytext=(7.45, 1.95), arrowprops=dict(arrowstyle="<->", lw=1.1))
    ax.text(7.62, 1.50, r"$A_2$", ha="left", va="center", fontsize=13)
    ax.text(1.55, 2.85, r"slower  $v_1$", ha="center", fontsize=12)
    ax.text(5.15, 2.72, r"faster  $v_2$", ha="center", fontsize=12)
    ax.text(4.0, 0.05, r"incompressible:  $A_1 v_1 = A_2 v_2$", ha="center", fontsize=13)
    ax.set_xlim(0.0, 8.15)
    ax.set_ylim(-0.15, 3.15)
    ax.set_title("Continuity: a narrower tube speeds the same stream up", fontsize=13, pad=8)
    save(fig, "continuity-tube.png")


def fig_bernoulli():
    fig, ax = new_fig(8.6, 4.0)
    upper = [(0.55, 2.55), (2.55, 2.55), (3.35, 1.95), (7.15, 1.95)]
    lower = [(0.55, 0.45), (2.55, 0.45), (3.35, 1.05), (7.15, 1.05)]
    ax.plot(*zip(*upper), color="black", lw=1.6)
    ax.plot(*zip(*lower), color="black", lw=1.6)
    ax.plot([0.55, 0.55], [0.45, 2.55], color="black", lw=1.6)
    ax.plot([0.85, 2.25], [1.50, 1.50], color="0.25", lw=1.15)
    tip(ax, 1.90, 1.50, 0.35, 0, color="0.25", lw=1.15, ms=10)
    ax.plot([3.70, 6.55], [1.50, 1.50], color="0.25", lw=1.15)
    tip(ax, 6.10, 1.50, 0.45, 0, color="0.25", lw=1.15, ms=10)
    ax.text(1.55, 2.90, r"slower, higher $P$", ha="center", fontsize=12)
    ax.text(5.20, 2.72, r"faster, lower $P$", ha="center", fontsize=12)
    ax.text(4.0, 0.08, r"same height, along one streamline:  $P+\frac{1}{2}\rho v^{2}\approx\mathrm{const}$", ha="center", fontsize=12)
    ax.set_xlim(0.05, 7.6)
    ax.set_ylim(-0.2, 3.2)
    ax.set_title("Bernoulli (ideal): speed up along the streamline, pressure falls", fontsize=13, pad=8)
    save(fig, "bernoulli-stations.png")


def fig_attached_separated():
    fig, ax = new_fig(8.8, 4.2)

    def bump(x0, gentle):
        c = np.linspace(0, 1, 80)
        x = x0 + 2.3 * c
        y = 1.15 + (0.55 if gentle else 0.15) * np.sin(np.pi * c) ** (1 if gentle else 8)
        if not gentle:
            # sharp corner: flat then a cliff
            x = np.concatenate([np.linspace(x0, x0 + 1.3, 30), np.linspace(x0 + 1.3, x0 + 2.3, 20)])
            y = np.concatenate([np.full(30, 1.15), np.linspace(1.15, 1.85, 8), np.full(12, 1.85)])
        return x, y

    # left: attached
    xs = np.linspace(0.3, 3.7, 90)
    wall = 1.05 + 0.55 * np.exp(-((xs - 1.9) ** 2) / (2 * 0.45**2))
    ax.plot(xs, wall, color="black", lw=1.6, zorder=3)
    for off in (0.18, 0.40):
        stream(ax, xs, wall + off)
    ax.text(1.9, 2.55, "attached", ha="center", fontsize=12)
    ax.text(1.9, 0.35, "streamlines follow\nthe surface", ha="center", fontsize=10)

    # right: flow follows the top, then leaves at the rear corner
    x0 = 4.85
    ax.plot(
        [x0, x0 + 1.35, x0 + 1.35, x0, x0],
        [1.05, 1.05, 1.72, 1.72, 1.05],
        color="black",
        lw=1.6,
        zorder=3,
    )
    xs_top = np.linspace(x0 - 0.35, x0 + 1.35, 28)
    stream(ax, xs_top, np.full_like(xs_top, 1.95))
    xs_leave = np.linspace(x0 + 1.35, x0 + 3.05, 24)
    ys_leave = 1.95 + 0.28 * (xs_leave - xs_leave[0]) / (xs_leave[-1] - xs_leave[0])
    stream(ax, xs_leave, ys_leave)
    ax.plot([x0 + 1.5, x0 + 2.85], [1.35, 1.15], color="0.45", lw=1.0, ls="--")
    ax.plot([x0 + 1.5, x0 + 2.85], [1.58, 1.72], color="0.45", lw=1.0, ls="--")
    ax.text(x0 + 2.35, 0.85, "wake", ha="center", fontsize=11, color="0.35")
    ax.text(x0 + 1.35, 2.55, "separated", ha="center", fontsize=12)
    ax.text(x0 + 1.45, 0.35, "streamlines leave;\nBernoulli on the wall fails", ha="center", fontsize=10)

    ax.set_xlim(0.1, 8.2)
    ax.set_ylim(0.05, 2.85)
    ax.set_title("Attached flow can follow a gentle surface; a sharp corner sheds a wake", fontsize=13, pad=8)
    save(fig, "attached-vs-separated.png")


def fig_diffuser():
    fig, ax = new_fig(8.6, 4.0)
    ax.plot([0.4, 7.8], [0.35, 0.35], color="black", lw=1.4)
    ax.text(7.35, 0.52, "road", fontsize=10, ha="center")
    # underbody: flat then opening ramp
    ax.plot([0.7, 3.15, 6.6], [1.35, 1.35, 2.35], color="black", lw=1.7, zorder=3)
    ax.plot([0.7, 0.7], [1.35, 2.15], color="black", lw=1.5)
    ax.text(1.7, 1.85, "body", fontsize=11, ha="center")
    # streamlines in the channel, diverging on the ramp, not through the body
    for y0, y1 in ((0.62, 0.85), (0.95, 1.45)):
        xs1 = np.linspace(0.45, 3.15, 24)
        xs2 = np.linspace(3.15, 6.9, 28)
        stream(ax, np.concatenate([xs1, xs2]), np.concatenate([np.full_like(xs1, y0), np.linspace(y0, y1, len(xs2))]))
    ax.plot(3.15, 1.35, "o", color="black", ms=5, zorder=4)
    ax.text(5.15, 2.85, r"if attached: area up, $v$ down, $P$ up", ha="center", fontsize=11)
    ax.text(
        4.1,
        -0.08,
        "A steep kink can separate. Pressure recovery is a hypothesis until the flow stays attached.",
        ha="center",
        fontsize=10,
    )
    ax.set_xlim(0.2, 8.0)
    ax.set_ylim(-0.25, 3.05)
    ax.set_title("Diffuser cartoon: slow the underbody flow and recover pressure", fontsize=13, pad=8)
    save(fig, "diffuser-recovery.png")


def fig_path_myth():
    fig, ax = new_fig(8.8, 4.3)

    def airfoil(x0, y0):
        c = np.linspace(0, 1, 80)
        x = x0 + 2.4 * c
        yu = y0 + 0.08 * np.sin(np.pi * c)
        yl = y0 - 0.32 * np.sin(np.pi * c)
        verts = np.column_stack([np.concatenate([x, x[::-1]]), np.concatenate([yu, yl[::-1]])])
        ax.add_patch(Polygon(verts, closed=True, facecolor="white", edgecolor="black", lw=1.5, zorder=3))
        return x, yu, yl

    x, yu, yl = airfoil(0.7, 1.7)
    for off in (0.22, 0.48):
        xs = np.concatenate([np.linspace(0.25, x[0], 12), x, np.linspace(x[-1], 3.55, 12)])
        ys = np.concatenate([np.full(12, yu[0] + off), yu + off, np.full(12, yu[-1] + off)])
        stream(ax, xs, ys)
    xs = np.concatenate([np.linspace(0.25, x[0], 12), x, np.linspace(x[-1], 3.55, 12)])
    off = -0.18
    ys = np.concatenate([np.full(12, yl[0] + off), yl + off, np.full(12, yl[-1] + off)])
    stream(ax, xs, ys)
    ax.text(1.9, 2.85, "common slogan", ha="center", fontsize=12)
    ax.text(1.9, 0.45, "“longer path, so faster”\nEqual transit time is not required.", ha="center", fontsize=10)

    x, yu, yl = airfoil(5.15, 1.85)
    xs = np.linspace(4.45, x[0] - 0.08, 16)
    stream(ax, xs, np.full_like(xs, yu[0] + 0.28))
    xs = np.concatenate([np.linspace(4.45, x[0], 12), x, np.linspace(x[-1], 8.2, 16)])
    off = -0.16
    ys = np.concatenate(
        [np.full(12, yl[0] + off), yl + off, np.linspace(yl[-1] + off, yl[-1] + off - 0.45, 16)]
    )
    stream(ax, xs, ys)
    ax.text(6.3, 2.85, "safer picture", ha="center", fontsize=12)
    ax.text(6.3, 0.45, "the wing turns the flow;\nnet force is still $\\Delta P$", ha="center", fontsize=10)
    ax.set_xlim(0.1, 8.4)
    ax.set_ylim(0.1, 3.15)
    ax.set_title("Downforce is a pressure force from turning the air, not a path-length race", fontsize=13, pad=8)
    save(fig, "path-length-myth.png")


def fig_reynolds_anatomy():
    fig, ax = new_fig(8.6, 4.2)
    rows = [
        (3.45, r"$\mathrm{Re}=\dfrac{\rho v L}{\mu}=\dfrac{v L}{\nu}$", "inertial effects compared with viscous effects"),
        (2.70, r"$\rho$", r"density  (kg/m$^3$)"),
        (2.10, r"$v$", r"free-stream speed  (m/s)"),
        (1.50, r"$L$", r"one agreed length  (m)  — car length or wing chord, say which"),
        (0.90, r"$\mu$", r"dynamic viscosity  (Pa$\cdot$s)"),
        (0.30, r"$\nu=\mu/\rho$", r"kinematic viscosity  (m$^2$/s); air $\approx 1.5\times 10^{-5}$"),
    ]
    for y, left, right in rows:
        ax.text(0.2, y, left, fontsize=13, ha="left", va="center")
        ax.text(3.7, y, right, fontsize=12, ha="left", va="center")
    ax.set_xlim(0.05, 8.6)
    ax.set_ylim(0.0, 4.0)
    ax.set_title(r"Anatomy of Reynolds number", fontsize=13, pad=8)
    save(fig, "reynolds-anatomy.png")


def fig_inertia_viscosity():
    fig, ax = new_fig(8.6, 4.0)

    def panel(cx, separate):
        cy, radius = 1.45, 0.38
        ax.add_patch(Circle((cx, cy), radius, fill=True, facecolor="white", edgecolor="black", lw=1.5, zorder=4))
        for y in (cy - 1.15, cy + 1.15):
            xs = np.linspace(cx - 1.65, cx + 1.65, 36)
            stream(ax, xs, np.full_like(xs, y))
        xs = np.linspace(cx - 1.65, cx + 1.65, 90)
        for sign in (1.0, -1.0):
            bow = 0.42 * np.exp(-((xs - cx) ** 2) / (2 * 0.32**2))
            ys = cy + sign * (0.62 + bow)
            if separate:
                incoming = xs <= cx + 0.05
                ax.plot(xs[incoming], ys[incoming], color="0.25", lw=1.05, zorder=1)
                x2 = np.linspace(xs[incoming][-1], cx + 1.65, 22)
                y2 = np.full_like(x2, ys[incoming][-1])
                stream(ax, x2, y2)
            else:
                stream(ax, xs, ys)
        if separate:
            ax.plot([cx + 0.55, cx + 1.45], [cy - 0.22, cy - 0.38], color="0.45", ls="--", lw=1.0)
            ax.plot([cx + 0.55, cx + 1.45], [cy + 0.22, cy + 0.38], color="0.45", ls="--", lw=1.0)
            ax.text(cx + 1.15, cy, "wake", fontsize=9, ha="center", color="0.35")

    panel(2.05, separate=True)
    ax.text(2.05, 2.85, "large Re: inertia, wake", ha="center", fontsize=11)
    panel(6.25, separate=False)
    ax.text(6.25, 2.85, "small Re: viscosity matters more", ha="center", fontsize=11)
    ax.set_xlim(0.15, 8.2)
    ax.set_ylim(0.05, 3.15)
    ax.set_title("Same body, different Re: the wake is a viscous story", fontsize=13, pad=8)
    save(fig, "inertia-vs-viscosity.png")


def fig_scale_comparison():
    fig, ax = new_fig(8.4, 3.8)
    ax.text(2.1, 3.15, "full car", ha="center", fontsize=13)
    ax.text(6.2, 3.15, "1:10 model (same air)", ha="center", fontsize=13)
    left = [
        r"$L=4.5\,\mathrm{m}$",
        r"$v=30\,\mathrm{m/s}$",
        r"$\mathrm{Re}\approx 9\times 10^{6}$",
    ]
    right = [
        r"$L=0.45\,\mathrm{m}$",
        r"$v=15\,\mathrm{m/s}$",
        r"$\mathrm{Re}\approx 4.5\times 10^{5}$",
    ]
    for i, (a, b) in enumerate(zip(left, right)):
        y = 2.35 - 0.7 * i
        ax.text(2.1, y, a, ha="center", fontsize=14)
        ax.text(6.2, y, b, ha="center", fontsize=14)
    ax.plot([4.15, 4.15], [0.55, 2.7], color="0.75", lw=1.0)
    ax.text(4.2, 0.15, r"model Re is about $1/20$ of full-scale Re", ha="center", fontsize=12)
    ax.set_xlim(0.3, 8.1)
    ax.set_ylim(-0.1, 3.5)
    ax.set_title(r"Same formula, very different $\mathrm{Re}$", fontsize=13, pad=8)
    save(fig, "scale-re-comparison.png")


def fig_length():
    fig, ax = new_fig(8.4, 3.6)
    ax.plot([0.7, 4.4], [0.55, 0.55], color="black", lw=1.2)
    y_hub = 0.78
    floor = y_hub
    ax.plot([1.2, 4.05, 4.05, 1.2, 1.2], [floor, floor, floor + 0.42, floor + 0.42, floor], color="black", lw=1.4, zorder=2)
    ax.plot([1.8, 2.25, 3.15, 3.55], [floor + 0.42, floor + 0.78, floor + 0.78, floor + 0.42], color="black", lw=1.4, zorder=2)
    ax.add_patch(Circle((1.8, y_hub), 0.22, fill=True, facecolor="white", edgecolor="black", lw=1.2, zorder=3))
    ax.add_patch(Circle((3.55, y_hub), 0.22, fill=True, facecolor="white", edgecolor="black", lw=1.2, zorder=3))
    ax.annotate("", xy=(1.15, 0.22), xytext=(4.05, 0.22), arrowprops=dict(arrowstyle="<->", lw=1.15))
    ax.text(2.6, 0.02, r"car length $L$  (course default for the vehicle)", ha="center", fontsize=11)
    # wing chord above, clear of the roof
    ax.plot([5.3, 7.5], [1.7, 1.55], color="black", lw=1.5)
    ax.plot([5.3, 7.5], [1.7, 1.95], color="black", lw=1.5)
    ax.annotate("", xy=(5.3, 2.35), xytext=(7.5, 2.35), arrowprops=dict(arrowstyle="<->", lw=1.15))
    ax.text(6.4, 2.58, r"wing chord as $L$", ha="center", fontsize=11)
    ax.text(6.4, 0.9, "Use this only in a\nwing-only sentence.", ha="center", fontsize=10)
    ax.set_xlim(0.4, 8.0)
    ax.set_ylim(-0.25, 3.05)
    ax.set_title(r"Name the $L$ inside every $\mathrm{Re}$ you quote", fontsize=13, pad=8)
    save(fig, "length-definition.png")


def fig_re_match():
    fig, ax = new_fig(8.2, 3.4)
    lines = [
        (2.55, r"match $\mathrm{Re}$:  $v_{\mathrm{model}} L_{\mathrm{model}} = v_{\mathrm{full}} L_{\mathrm{full}}$"),
        (1.75, r"$v_{\mathrm{model}} = 30\times 4.5 / 0.45 = 300\,\mathrm{m/s}$"),
        (0.95, r"about $0.9$ times the speed of sound; $q$ is enormous"),
        (0.25, "not a classroom fan, and Bernoulli's incompressible assumption fails"),
    ]
    for y, txt in lines:
        ax.text(4.1, y, txt, ha="center", va="center", fontsize=13)
    ax.set_xlim(0.2, 8.0)
    ax.set_ylim(-0.15, 3.15)
    ax.set_title("Matching full-scale Re in room air is not the plan", fontsize=13, pad=8)
    save(fig, "re-match-impractical.png")


def fig_metrology():
    fig, ax = new_fig(8.8, 3.8)

    def target(cx, title, pts, note):
        ax.add_patch(Circle((cx, 1.55), 0.95, fill=False, lw=1.2, zorder=2))
        ax.add_patch(Circle((cx, 1.55), 0.55, fill=False, lw=1.0, zorder=2))
        ax.add_patch(Circle((cx, 1.55), 0.04, fill=True, facecolor="black", zorder=3))
        for px, py in pts:
            ax.plot(cx + px, 1.55 + py, "o", color="black", ms=5, zorder=4)
        ax.text(cx, 2.75, title, ha="center", fontsize=12)
        ax.text(cx, 0.25, note, ha="center", fontsize=9)

    target(1.5, "repeatable, biased", [(0.28, 0.22), (0.34, 0.30), (0.24, 0.32), (0.32, 0.18)], "tight cluster, off the true value\n(poor accuracy)")
    target(4.4, "scattered about truth", [(0.15, 0.45), (-0.4, 0.1), (0.35, -0.25), (-0.2, -0.4), (0.05, 0.15)], "mean can be fair;\npoor repeatability")
    target(7.3, "coarse resolution", [], "instrument cannot show\na change inside one tick")
    # coarse: two big ticks as a number line under the third target, already noted
    ax.plot([6.7, 7.9], [1.55, 1.55], color="black", lw=1.2)
    for x in (6.85, 7.3, 7.75):
        ax.plot([x, x], [1.42, 1.68], color="black", lw=1.2)
    ax.set_xlim(0.3, 8.5)
    ax.set_ylim(-0.05, 3.15)
    ax.set_title("Three different ways a measurement can be untrustworthy", fontsize=13, pad=8)
    save(fig, "metrology-three.png")


def fig_load_cell():
    fig, ax = new_fig(8.6, 4.0)
    # wall and bar
    ax.plot([0.45, 0.45], [0.7, 2.3], color="black", lw=3.0)
    ax.plot([0.45, 2.7], [1.5, 1.5], color="black", lw=6.0, solid_capstyle="butt", zorder=2)
    ax.text(1.55, 1.15, "bar", ha="center", fontsize=11)
    tip(ax, 2.55, 1.95, -1.15, 0, lw=1.5, ms=12)
    ax.text(1.55, 2.20, "sensing axis", ha="center", fontsize=11)
    tip(ax, 2.70, 1.62, 0, 0.55, lw=1.1, ms=11)
    ax.text(2.85, 2.35, "side load", ha="left", fontsize=10)
    # right: two axes on a fixture, labels in open space
    ax.add_patch(Rectangle((5.3, 1.15), 1.5, 0.7, fill=False, lw=1.4))
    ax.text(6.05, 1.5, "model", ha="center", va="center", fontsize=11)
    tip(ax, 5.3, 1.5, -0.85, 0, lw=1.5, ms=12)
    ax.text(4.15, 1.75, r"$F_D$", ha="center", fontsize=12)
    tip(ax, 6.05, 1.15, 0, -0.7, lw=1.5, ms=12)
    ax.text(6.45, 0.55, r"$F_L$", ha="left", fontsize=12)
    ax.text(6.05, 2.55, "one cell per axis", ha="center", fontsize=11)
    ax.text(
        4.3,
        0.05,
        "Tare with the model on and the fan off. The change is the aero force.",
        ha="center",
        fontsize=10,
    )
    ax.set_xlim(0.15, 8.3)
    ax.set_ylim(-0.25, 2.9)
    ax.set_title("A load cell reports force along one axis, after you calibrate it", fontsize=13, pad=8)
    save(fig, "load-cell-axis.png")


def fig_calibration():
    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=DPI)
    fig.patch.set_facecolor(FACE)
    ax.set_facecolor(FACE)
    reading = np.array([0.0, 120.0, 250.0, 490.0])
    force = np.array([0.0, 0.49, 0.98, 1.96])
    ax.plot(reading, force, "o", color="black", ms=7, zorder=3)
    xs = np.linspace(0, 520, 20)
    ax.plot(xs, xs * (1.96 / 490.0), color="black", lw=1.4, zorder=2)
    ax.text(40, 1.7, r"known weights: $F=mg$", fontsize=11, ha="left")
    ax.set_xlabel("instrument reading (counts)", fontsize=11)
    ax.set_ylabel(r"true force $F$ (N)", fontsize=11)
    ax.set_xlim(-20, 560)
    ax.set_ylim(-0.1, 2.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title("Calibration: hang known masses along the sensing axis", fontsize=13)
    fig.savefig(OUT / "calibration-line.png", dpi=DPI, bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    fig.savefig(OUT / "calibration-line.svg", bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    plt.close(fig)
    print("wrote calibration-line.png")


def fig_error_budget():
    fig, ax = plt.subplots(figsize=(7.4, 4.0), dpi=DPI)
    fig.patch.set_facecolor(FACE)
    ax.set_facecolor(FACE)
    labels = [r"$\delta F_D/F_D$", r"$\delta q/q$", r"$\delta A/A$", "combined"]
    vals = [5, 10, 2, 11.4]
    bars = ax.bar(np.arange(4), vals, color="white", edgecolor="black", lw=1.3, width=0.55)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.4, f"{v:.0f}%" if v > 3 else "2%", ha="center", fontsize=11)
    ax.set_xticks(np.arange(4))
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_ylabel("relative uncertainty (%)", fontsize=11)
    ax.set_ylim(0, 15)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(r"5% in speed is 10% in $q$, and it dominates $C_D$", fontsize=13)
    fig.savefig(OUT / "error-budget.png", dpi=DPI, bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    fig.savefig(OUT / "error-budget.svg", bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    plt.close(fig)
    print("wrote error-budget.png")


if __name__ == "__main__":
    fig_continuity()
    fig_bernoulli()
    fig_attached_separated()
    fig_diffuser()
    fig_path_myth()
    fig_reynolds_anatomy()
    fig_inertia_viscosity()
    fig_scale_comparison()
    fig_length()
    fig_re_match()
    fig_metrology()
    fig_load_cell()
    fig_calibration()
    fig_error_budget()
