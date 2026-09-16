#!/usr/bin/env python3
"""Generate Week 1 lecture figures as physics-textbook line drawings."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import (
    Arc,
    Circle,
    FancyArrowPatch,
    FancyBboxPatch,
    Rectangle,
    Wedge,
)
from matplotlib.lines import Line2D
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
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    fig.savefig(path.with_suffix(".svg"), bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    plt.close(fig)
    print("wrote", path.name)


def arrow(ax, origin, vec, label, loff, *, lw=1.8, ms=16, color="black", tail_shift=(0, 0)):
    """Force arrow. Tail at origin (+ optional shift still on the CM marker)."""
    o = np.array(origin, dtype=float) + np.array(tail_shift, dtype=float)
    v = np.array(vec, dtype=float)
    end = o + v
    patch = FancyArrowPatch(
        o,
        end,
        arrowstyle="-|>",
        mutation_scale=ms,
        lw=lw,
        color=color,
        shrinkA=0,
        shrinkB=0,
        zorder=5,
    )
    ax.add_patch(patch)
    lp = end + np.array(loff, dtype=float)
    ax.text(
        lp[0],
        lp[1],
        label,
        fontsize=13,
        color=color,
        ha="center",
        va="center",
        zorder=6,
        usetex=False,
    )


def cm_marker(ax, x, y, r=0.11):
    """Circled-cross center-of-mass symbol."""
    ax.add_patch(Circle((x, y), r, fill=True, facecolor="white", edgecolor="black", lw=1.2, zorder=7))
    s = r * 0.62
    ax.plot([x - s, x + s], [y, y], color="black", lw=1.1, zorder=8)
    ax.plot([x, x], [y - s, y + s], color="black", lw=1.1, zorder=8)


def car_outline(ax, x0, y0, scale=1.0, wing=False):
    """Side-view line drawing sitting on road y=y0. Returns CM coordinates."""
    s = scale
    r = 0.18 * s
    hub_y = y0 + r
    # body sits on hubs; cabin above
    xb = x0 + s * np.array([0.20, 0.50, 0.82, 1.62, 2.20, 2.48, 2.58, 2.58, 2.40, 0.28, 0.20])
    yb = np.array(
        [
            hub_y + 0.22 * s,
            hub_y + 0.22 * s,
            hub_y + 0.62 * s,
            hub_y + 0.62 * s,
            hub_y + 0.26 * s,
            hub_y + 0.26 * s,
            hub_y + 0.18 * s,
            hub_y,
            hub_y,
            hub_y,
            hub_y + 0.22 * s,
        ]
    )
    ax.plot(xb, yb, color="black", lw=1.35, zorder=2)
    ax.plot(
        x0 + s * np.array([0.80, 1.02, 1.52, 1.52]),
        [hub_y + 0.28 * s, hub_y + 0.54 * s, hub_y + 0.54 * s, hub_y + 0.28 * s],
        color="black",
        lw=0.9,
        zorder=2,
    )
    for wx in (0.68, 2.08):
        ax.add_patch(
            Circle((x0 + s * wx, hub_y), r, fill=False, edgecolor="black", lw=1.3, zorder=2)
        )
        ax.add_patch(
            Circle((x0 + s * wx, hub_y), 0.07 * s, fill=False, edgecolor="black", lw=0.8, zorder=2)
        )
    if wing:
        ax.plot(
            [x0 + s * 2.45, x0 + s * 2.78],
            [hub_y + 0.42 * s, hub_y + 0.42 * s],
            color="black",
            lw=1.5,
            zorder=2,
        )
        ax.plot(
            [x0 + s * 2.68, x0 + s * 2.68],
            [hub_y + 0.26 * s, hub_y + 0.42 * s],
            color="black",
            lw=1.5,
            zorder=2,
        )
    cm = (x0 + s * 1.32, hub_y + 0.20 * s)
    return cm


def road(ax, x1, x2, y):
    ax.plot([x1, x2], [y, y], color="black", lw=1.4, zorder=1)
    ax.plot([x1, x2], [y - 0.04, y - 0.04], color="black", lw=0.5, zorder=1)


def axes_xy(ax, x, y, L=0.45):
    arrow(ax, (x, y), (L, 0), r"$x$", (0.12, -0.12), lw=1.0, ms=10)
    arrow(ax, (x, y), (0, L), r"$y$", (-0.14, 0.10), lw=1.0, ms=10)


def fig_fbd_rest():
    fig, ax = new_fig(7.2, 4.6)
    road(ax, -0.3, 4.6, 0.0)
    cm = car_outline(ax, 0.7, 0.0, scale=1.15, wing=False)
    L = 1.35
    arrow(ax, cm, (0, L), r"$N$", (0.22, 0.08))
    arrow(ax, cm, (0, -L), r"$mg$", (0.28, -0.08))
    cm_marker(ax, *cm)
    ax.text(cm[0] + 0.28, cm[1] + 0.02, "CM", fontsize=8, color="black", va="bottom")
    axes_xy(ax, -0.05, 2.15)
    ax.set_xlim(-0.5, 4.8)
    ax.set_ylim(-1.85, 2.85)
    ax.set_title("Free-body diagram: car at rest", fontsize=13, pad=8)
    ax.text(
        2.15,
        -1.45,
        r"Particle model: every force is drawn from the center of mass." + "\n"
        + r"Level road, $\mathbf{a}=0$.  $|N|=|mg|$.",
        ha="center",
        fontsize=9,
    )
    save(fig, "fbd-rest.png")


def fig_fbd_cruise():
    fig, ax = new_fig(8.2, 5.2)
    road(ax, -0.4, 5.2, 0.0)
    cm = car_outline(ax, 1.05, 0.0, scale=1.15, wing=True)
    mg, dw, fd = 1.20, 0.75, 1.85
    n = mg + dw
    arrow(ax, cm, (0, n), r"$N$", (0.28, 0.10))
    # Parallel downward arrows: both tails remain on the CM marker.
    arrow(ax, cm, (0, -mg), r"$mg$", (-0.32, -0.08), tail_shift=(-0.10, 0))
    arrow(ax, cm, (0, -dw), r"$D_w$", (0.34, -0.06), tail_shift=(0.10, 0))
    arrow(ax, cm, (-fd, 0), r"$F_D$", (-0.22, 0.20))
    arrow(ax, cm, (fd, 0), r"$F_{\mathrm{drive}}$", (0.35, -0.22))
    cm_marker(ax, *cm)
    ax.text(cm[0] + 0.28, cm[1] + 0.14, "CM", fontsize=8)
    axes_xy(ax, -0.15, 2.55)
    ax.set_xlim(-1.6, 5.6)
    ax.set_ylim(-2.05, 3.25)
    ax.set_title("Free-body diagram: steady cruise with aero", fontsize=13, pad=8)
    ax.text(
        2.2,
        -1.65,
        r"$\mathbf{a}=0$:  $N=mg+D_w$  (vertical) and  $F_{\mathrm{drive}}=F_D$  (horizontal)."
        + "\n"
        + r"Arrow length is qualitative. Airflow is not a force and is omitted.",
        ha="center",
        fontsize=9,
    )
    save(fig, "fbd-cruise.png")


def fig_not_lighter():
    fig, ax = new_fig(9.2, 4.4)

    def panel(xoff, title, dw):
        ax.text(xoff + 1.7, 2.55, title, ha="center", fontsize=11)
        ax.add_patch(
            FancyBboxPatch(
                (xoff - 0.15, -1.55),
                3.7,
                4.25,
                boxstyle="round,pad=0.08,rounding_size=0.08",
                fill=False,
                lw=0.8,
                edgecolor="0.55",
            )
        )
        road(ax, xoff + 0.1, xoff + 3.4, 0.0)
        cm = car_outline(ax, xoff + 0.45, 0.0, scale=0.95, wing=(dw > 0))
        mg = 0.95
        n = mg + dw
        arrow(ax, cm, (0, n), r"$N$" if dw == 0 else r"$N$", (0.28 if dw else 0.22, 0.10), lw=1.5, ms=13)
        arrow(ax, cm, (0, -mg), r"$mg$", (-0.28, -0.06), lw=1.5, ms=13, tail_shift=(-0.12 if dw else 0, 0))
        if dw:
            arrow(ax, cm, (0, -dw), r"$D_w$", (0.32, -0.04), lw=1.5, ms=13, tail_shift=(0.12, 0))
        cm_marker(ax, *cm, r=0.09)
        ax.text(
            xoff + 1.7,
            -1.35,
            r"$m$ unchanged" + "\n" + (r"$N=mg$" if dw == 0 else r"$N=mg+D_w$"),
            ha="center",
            fontsize=10,
        )
        return cm

    panel(0.0, "At rest", 0.0)
    panel(4.6, "Steady speed with downforce", 0.55)
    ax.set_xlim(-0.3, 8.4)
    ax.set_ylim(-1.7, 2.8)
    ax.set_title("Downforce does not make the car lighter", fontsize=13, pad=6)
    save(fig, "not-lighter.png")


def fig_friction():
    fig, ax = new_fig(8.6, 4.0)
    ax.plot([-0.35, 2.55], [0, 0], color="black", lw=1.5)
    ax.add_patch(Rectangle((0.45, 0.0), 1.40, 1.05, fill=False, lw=1.4, zorder=2))
    cm = (1.15, 0.52)
    mg = 1.05
    arrow(ax, cm, (0, mg), r"$N$", (0.22, 0.10))
    arrow(ax, cm, (0, -mg), r"$mg$", (-0.38, 0.05))
    arrow(ax, cm, (1.15, 0), r"$f_{\max}$", (0.18, 0.18))
    cm_marker(ax, *cm, r=0.09)
    ax.text(cm[0] + 0.24, cm[1] - 0.02, "CM", fontsize=8, va="center")

    ax.text(4.55, 1.85, r"Available horizontal force (same $\mu$)", fontsize=10, ha="left")
    ax.plot([3.5, 5.55], [1.15, 1.15], color="black", lw=6, solid_capstyle="butt")
    ax.text(5.70, 1.15, r"$\mu\,mg$", va="center", fontsize=11)
    ax.text(3.5, 1.38, "no aero", fontsize=9)
    ax.plot([3.5, 5.55], [0.45, 0.45], color="black", lw=6, solid_capstyle="butt")
    ax.plot([5.55, 6.45], [0.45, 0.45], color="0.35", lw=6, solid_capstyle="butt")
    ax.text(6.60, 0.45, r"$+\ \mu D_w$", va="center", fontsize=11)
    ax.text(3.5, 0.68, "with downforce", fontsize=9)
    ax.text(
        5.1,
        -0.22,
        "Cornering and braking spend this budget.\nAero raises $N$ without changing mass $m$.",
        ha="center",
        fontsize=9,
    )
    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(-1.05, 2.3)
    ax.set_title(r"Friction budget:  $f_{\max}\sim\mu N$", fontsize=13, pad=8)
    save(fig, "friction-budget.png")


def fig_modular():
    fig, ax = new_fig(9.4, 4.3)
    road_y = 0.0
    ax.plot([0.3, 8.7], [road_y, road_y], color="black", lw=1.4)
    x0, s = 1.7, 1.35
    r = 0.18 * s
    hub_y = road_y + r
    xb = x0 + s * np.array([0.20, 0.50, 0.82, 1.70, 2.22, 2.50, 2.58, 2.58, 2.40, 0.28, 0.20])
    yb = np.array(
        [
            hub_y + 0.22 * s,
            hub_y + 0.22 * s,
            hub_y + 0.62 * s,
            hub_y + 0.62 * s,
            hub_y + 0.28 * s,
            hub_y + 0.28 * s,
            hub_y + 0.18 * s,
            hub_y,
            hub_y,
            hub_y,
            hub_y + 0.22 * s,
        ]
    )
    ax.plot(xb, yb, color="black", lw=1.5)
    ax.plot(
        x0 + s * np.array([0.80, 1.05, 1.55, 1.55]),
        [hub_y + 0.28 * s, hub_y + 0.54 * s, hub_y + 0.54 * s, hub_y + 0.28 * s],
        color="black",
        lw=0.9,
    )
    for wx in (0.68, 2.10):
        ax.add_patch(Circle((x0 + s * wx, hub_y), r, fill=False, lw=1.3))
        ax.add_patch(Circle((x0 + s * wx, hub_y), 0.07 * s, fill=False, lw=0.8))
    # splitter attached to front lower lip
    ax.plot([x0 + s * 0.02, x0 + s * 0.28], [hub_y, hub_y], color="black", lw=2.2, solid_capstyle="butt")
    # spoiler on deck
    ax.plot([x0 + s * 2.22, x0 + s * 2.48], [hub_y + 0.30 * s, hub_y + 0.30 * s], color="black", lw=2.0)
    # rear wing
    ax.plot([x0 + s * 2.50, x0 + s * 2.85], [hub_y + 0.52 * s, hub_y + 0.52 * s], color="black", lw=2.0)
    ax.plot([x0 + s * 2.72, x0 + s * 2.72], [hub_y + 0.28 * s, hub_y + 0.52 * s], color="black", lw=1.5)
    # diffuser: expanding underbody behind the rear axle
    ax.plot(
        [x0 + s * 2.22, x0 + s * 2.58, x0 + s * 2.95],
        [hub_y - 0.02 * s, hub_y - 0.02 * s, road_y + 0.06],
        color="black",
        lw=1.6,
    )

    def callout(x1, y1, x2, y2, text, ha="left"):
        ax.annotate(
            text,
            xy=(x1, y1),
            xytext=(x2, y2),
            fontsize=9,
            ha=ha,
            va="center",
            arrowprops=dict(arrowstyle="-", lw=0.8, color="black"),
        )

    callout(x0 + s * 0.02, hub_y, 0.35, 1.55, "splitter")
    callout(x0 + s * 1.25, hub_y + 0.62 * s, x0 + s * 1.05, 2.05, "BODY-01  (held fixed)", ha="center")
    callout(x0 + s * 2.35, hub_y + 0.30 * s, 6.55, 0.85, "spoiler")
    callout(x0 + s * 2.80, hub_y + 0.52 * s, 6.85, 1.85, "wing")
    callout(x0 + s * 2.85, road_y + 0.08, 6.55, 0.22, "diffuser")

    ax.set_xlim(-0.1, 9.3)
    ax.set_ylim(-0.35, 2.35)
    ax.set_title("Modular kit: swap one part at a time", fontsize=13, pad=8)
    ax.text(
        4.6,
        -0.28,
        "Keep the body, ride height, and alignment fixed so a force change can be attributed to one part.",
        ha="center",
        fontsize=9,
    )
    save(fig, "modular-parts.png")


def fig_platform():
    fig, ax = new_fig(9.0, 3.8)
    # fan: circle + 3 blades
    ax.add_patch(Circle((0.85, 1.35), 0.72, fill=False, lw=1.5))
    for ang in (20, 80, 140):
        a = np.deg2rad(ang)
        ax.add_patch(
            Wedge((0.85, 1.35), 0.55, ang - 12, ang + 12, fill=False, lw=0.9)
        )
    ax.add_patch(Circle((0.85, 1.35), 0.10, fill=False, lw=1.1))
    ax.text(0.85, 0.38, "fan", ha="center", fontsize=10)

    # flow arrows (velocity context, not an FBD)
    for y in (1.15, 1.35, 1.55):
        arrow(ax, (1.75, y), (0.85, 0), "", (0, 0), lw=1.1, ms=11)
    ax.text(2.15, 1.82, r"$v$", fontsize=12)

    # table
    ax.plot([3.35, 7.15], [0.85, 0.85], color="black", lw=1.6)
    ax.plot([3.55, 3.55], [0.85, 0.25], color="black", lw=1.4)
    ax.plot([6.95, 6.95], [0.85, 0.25], color="black", lw=1.4)
    ax.plot([3.35, 7.15], [0.22, 0.22], color="black", lw=0.8)

    # load cell
    ax.add_patch(Rectangle((4.85, 0.85), 0.85, 0.22, fill=False, lw=1.2))
    ax.text(5.27, 0.96, "load cell", ha="center", va="center", fontsize=8)

    # model
    car_outline(ax, 4.35, 1.07, scale=0.72, wing=True)
    ax.text(5.27, 1.95, "scale model", ha="center", fontsize=9)

    # anemometer
    ax.plot([7.85, 7.85], [0.35, 1.55], color="black", lw=1.4)
    ax.add_patch(Circle((7.85, 1.70), 0.16, fill=False, lw=1.2))
    ax.text(7.85, 0.18, "speed\nsensor", ha="center", fontsize=9)

    ax.set_xlim(-0.1, 8.6)
    ax.set_ylim(0.0, 2.25)
    ax.set_title("Test-platform schematic (to be instrumented in Week 6)", fontsize=13, pad=8)
    save(fig, "test-platform.png")


if __name__ == "__main__":
    fig_fbd_rest()
    fig_fbd_cruise()
    fig_not_lighter()
    fig_friction()
    fig_modular()
    fig_platform()
