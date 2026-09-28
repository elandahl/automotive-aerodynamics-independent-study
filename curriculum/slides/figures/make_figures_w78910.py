#!/usr/bin/env python3
"""Week 7–10 lecture figures: textbook line drawings."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyArrowPatch, FancyBboxPatch, Polygon
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


def tip(ax, x, y, dx, dy, *, color="black", lw=1.15, ms=10, zorder=4):
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
            zorder=zorder,
        )
    )


def stream(ax, xs, ys, *, color="0.25", lw=1.05, zorder=1):
    xs = np.asarray(xs, dtype=float)
    ys = np.asarray(ys, dtype=float)
    ax.plot(xs, ys, color=color, lw=lw, zorder=zorder)
    tip(ax, xs[-4], ys[-4], xs[-1] - xs[-4], ys[-1] - ys[-4], color=color, lw=lw, ms=9, zorder=zorder)


def surfaces(alpha_deg, le, chord=3.15, n=90):
    """Inverted airfoil: small pressure side above the chord, camber below."""
    a = np.deg2rad(alpha_deg)
    t = np.linspace(0, 1, n)
    x = t * chord
    yu = 0.04 * np.sin(np.pi * t)
    yl = -0.40 * np.sin(np.pi * t)
    c, s = np.cos(a), np.sin(a)

    def rot(xx, yy):
        return le[0] + xx * c - yy * s, le[1] + xx * s + yy * c

    return rot(x, yu), rot(x, yl), rot(x, np.zeros_like(x))


def draw_airfoil(ax, alpha, le, chord=3.15):
    (xu, yu), (xl, yl), (xc, yc) = surfaces(alpha, le, chord)
    poly_x = np.concatenate([xu, xl[::-1]])
    poly_y = np.concatenate([yu, yl[::-1]])
    ax.add_patch(
        Polygon(
            np.column_stack([poly_x, poly_y]),
            closed=True,
            facecolor="white",
            edgecolor="black",
            lw=1.55,
            zorder=3,
        )
    )
    return (xu, yu), (xl, yl), (xc, yc)


def offset_curve(x, y, gap, side):
    dx = np.gradient(x)
    dy = np.gradient(y)
    nrm = np.hypot(dx, dy)
    nrm = np.maximum(nrm, 1e-9)
    tx, ty = dx / nrm, dy / nrm
    if side == "up":
        nx, ny = -ty, tx
    else:
        nx, ny = ty, -tx
    return x + gap * nx, y + gap * ny


def fig_aoa_definition():
    fig, ax = new_fig(9.0, 4.8)
    alpha = 18.0
    le = (4.15, 1.95)
    chord = 3.35
    (xu, yu), (xl, yl), (xc, yc) = draw_airfoil(ax, alpha, le, chord)
    a = np.deg2rad(alpha)
    vertex = (le[0] - 2.35 * np.cos(a), le[1] - 2.35 * np.sin(a))
    ax.plot([vertex[0], xc[-1]], [vertex[1], yc[-1]], color="black", lw=1.05, ls=(0, (4, 3)), zorder=4)
    ax.plot([vertex[0], vertex[0] + 1.85], [vertex[1], vertex[1]], color="0.15", lw=1.15, zorder=2)
    tip(ax, vertex[0] + 1.45, vertex[1], 0.40, 0, color="0.15", lw=1.15, ms=11, zorder=2)
    ax.add_patch(Arc(vertex, 1.55, 1.55, angle=0, theta1=0, theta2=alpha, lw=1.15, zorder=4))
    # Sit α in the open wedge, clear of both rays.
    mid = np.deg2rad(alpha * 0.42)
    ax.text(
        vertex[0] + 1.05 * np.cos(mid),
        vertex[1] + 1.05 * np.sin(mid),
        r"$\alpha$",
        fontsize=15,
        ha="center",
        va="center",
    )
    ax.text(vertex[0] + 1.05, vertex[1] - 0.32, "free stream", fontsize=11, ha="center")
    i = 48
    ax.annotate(
        "",
        xy=(xl[i] + 0.15, yl[i] - 0.62),
        xytext=(xl[i] + 0.15, yl[i]),
        arrowprops=dict(arrowstyle="-|>", lw=1.45, color="black", shrinkA=0, shrinkB=0),
        zorder=5,
    )
    ax.text(xl[i] + 0.38, yl[i] - 0.28, r"$D_w$", fontsize=13, ha="left", va="center")
    ax.text(4.55, 1.58, "suction side", fontsize=10, ha="center", color="0.2")
    ax.text(float(np.mean(xu)), float(np.max(yu)) + 0.26, "pressure side", fontsize=10, ha="center", color="0.2")
    ax.plot([0.35, 8.75], [0.32, 0.32], color="black", lw=1.3)
    ax.text(8.2, 0.48, "road", fontsize=10, ha="center")
    ax.text(
        4.55,
        -0.02,
        r"$\alpha = 0$ when the chord is parallel to the free stream. Increasing $\alpha$ drops the leading edge.",
        ha="center",
        fontsize=10,
    )
    ax.set_xlim(0.1, 8.95)
    ax.set_ylim(-0.2, 3.65)
    ax.set_title(r"Geometric angle of attack $\alpha$ on the inverted wing", fontsize=13, pad=8)
    save(fig, "aoa-definition.png")


def _gap_ok(xs, ys, xu, yu, xl, yl, gap=0.12):
    """True if every streamline sample stays outside the airfoil by `gap`."""
    px = np.concatenate([xu, xl[::-1]])
    py = np.concatenate([yu, yl[::-1]])
    for x, y in zip(xs, ys):
        d = np.min(np.hypot(px - x, py - y))
        if d < gap:
            return False
    return True


def fig_stall_inverted():
    fig, ax = new_fig(9.4, 4.7)

    def panel(le, alpha, separated):
        (xu, yu), (xl, yl), _ = draw_airfoil(ax, alpha, le, chord=2.55)
        # Upper stream: horizontal, above the highest upper-surface point.
        y_top = float(np.max(yu)) + 0.32
        x0 = le[0] - 1.05
        x1 = float(np.max(xu)) + 0.4
        xs_up = np.linspace(x0, x1, 40)
        stream(ax, xs_up, np.full_like(xs_up, y_top))
        if not _gap_ok(xs_up, np.full_like(xs_up, y_top), xu, yu, xl, yl):
            raise RuntimeError("upper stream too close")
        if not separated:
            # Under the belly, clear of the surface, then a smooth rise after the trailing edge.
            y_under = float(np.min(yl)) - 0.22
            x_te = float(xl[-1])
            x_end = min(x_te + 0.7, 4.35)
            xs = np.linspace(x0, x_end, 48)
            s = np.clip((xs - (x_te - 0.15)) / (x_end - (x_te - 0.15)), 0, 1)
            rise = min(0.48, y_top - y_under - 0.55)
            ys = y_under + rise * s**2
            if not _gap_ok(xs, ys, xu, yu, xl, yl):
                raise RuntimeError("attached lower stream too close")
            stream(ax, xs, ys)
            ax.text(le[0] + 0.85, y_top + 0.28, "attached", ha="center", fontsize=12)
            ax.text(x_end + 0.08, y_under + 0.55 * rise, "turned\nupward", ha="left", va="center", fontsize=10)
        else:
            # Stays below the whole belly and does not turn upward after the trailing edge.
            y_under = float(np.min(yl)) - 0.36
            x_te = float(np.max(xl))
            xs = np.linspace(x0, x_te + 0.95, 36)
            ys = np.full_like(xs, y_under)
            if not _gap_ok(xs, ys, xu, yu, xl, yl):
                raise RuntimeError("stalled lower stream too close")
            stream(ax, xs, ys)
            y_belly = float(np.min(yl))
            x_d0 = float(xl[46])
            x_d1 = x_te - 0.05
            ax.plot([x_d0, x_d1], [y_belly - 0.22, y_belly - 0.22], color="0.45", lw=1.0, ls="--", zorder=1)
            ax.plot([x_d0, x_d1], [y_belly - 0.12, y_belly - 0.12], color="0.45", lw=1.0, ls="--", zorder=1)
            ax.text(x_d1 + 0.12, y_belly - 0.17, "wake", ha="left", va="center", fontsize=11, color="0.35")
            ax.text(le[0] + 0.85, y_top + 0.32, "stalled", ha="center", fontsize=12)
        return y_top

    panel((1.35, 2.05), 6.0, False)
    panel((6.55, 2.15), 16.0, True)
    ax.plot([0.25, 9.9], [0.38, 0.38], color="black", lw=1.2)
    ax.text(2.4, 0.62, "flow stays on the suction side", ha="center", fontsize=10)
    ax.text(7.5, 0.62, "suction side has separated", ha="center", fontsize=10)
    ax.set_xlim(0.1, 10.15)
    ax.set_ylim(0.15, 4.05)
    ax.set_title("Stall is separation on the lower surface of this inverted wing", fontsize=13, pad=8)
    save(fig, "stall-inverted.png")


def fig_cl_cd_aoa():
    alpha = np.array([0, 5, 10, 15, 20], dtype=float)
    cl = np.array([-0.12, -0.32, -0.52, -0.58, -0.36])
    cd = np.array([0.38, 0.44, 0.52, 0.62, 0.95])
    fig, axes = plt.subplots(1, 2, figsize=(9.1, 4.15), dpi=DPI)
    fig.patch.set_facecolor(FACE)
    for ax, y, ylab in (
        (axes[0], cl, r"$C_L$  (up positive)"),
        (axes[1], cd, r"$C_D$"),
    ):
        ax.set_facecolor(FACE)
        ax.axvspan(16.5, 22, color="0.93", zorder=0)
        ax.plot(alpha, y, "-o", color="black", ms=6, lw=1.4, zorder=2)
        ax.set_xlim(-1, 22)
        ax.set_xlabel(r"geometric $\alpha$ (degrees)", fontsize=11)
        ax.set_ylabel(ylab, fontsize=11)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_xticks([0, 5, 10, 15, 20])
    axes[0].set_ylim(-0.85, 0.18)
    axes[0].axhline(0, color="0.6", lw=0.8)
    axes[0].text(19.2, 0.02, "stall", ha="center", fontsize=11, color="0.25")
    axes[1].set_ylim(0, 1.25)
    axes[1].text(19.2, 1.12, "stall", ha="center", fontsize=11, color="0.25")
    fig.suptitle(r"Illustrative sweep only — replace these curves with your means", fontsize=13, y=1.02)
    fig.tight_layout()
    fig.savefig(OUT / "cl-cd-vs-aoa.png", dpi=DPI, bbox_inches="tight", facecolor=FACE, pad_inches=0.16)
    fig.savefig(OUT / "cl-cd-vs-aoa.svg", bbox_inches="tight", facecolor=FACE, pad_inches=0.16)
    plt.close(fig)
    print("wrote cl-cd-vs-aoa.png")


def fig_efficiency_aoa():
    alpha = np.array([0, 5, 10, 15, 20], dtype=float)
    eff = np.array([0.12 / 0.38, 0.32 / 0.44, 0.52 / 0.52, 0.58 / 0.62, 0.36 / 0.95])
    fig, ax = plt.subplots(figsize=(7.6, 4.15), dpi=DPI)
    fig.patch.set_facecolor(FACE)
    ax.set_facecolor(FACE)
    ax.axvspan(16.5, 22, color="0.93", zorder=0)
    ax.plot(alpha, eff, "-o", color="black", ms=6, lw=1.4, zorder=2)
    ax.text(4.0, 1.12, r"$\mathcal{E}$ peaks at $10^\circ$", fontsize=11, ha="center")
    ax.text(18.6, 1.12, r"$|C_L|$ peaks at $15^\circ$", fontsize=11, ha="center")
    ax.set_xlim(-1, 22)
    ax.set_ylim(0, 1.28)
    ax.set_xticks([0, 5, 10, 15, 20])
    ax.set_xlabel(r"geometric $\alpha$ (degrees)", fontsize=11)
    ax.set_ylabel(r"$\mathcal{E}=|C_L|/C_D$", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(r"On this sketch, efficiency peaks before downforce does", fontsize=13)
    fig.savefig(OUT / "efficiency-vs-aoa.png", dpi=DPI, bbox_inches="tight", facecolor=FACE, pad_inches=0.16)
    fig.savefig(OUT / "efficiency-vs-aoa.svg", bbox_inches="tight", facecolor=FACE, pad_inches=0.16)
    plt.close(fig)
    print("wrote efficiency-vs-aoa.png")


def underbody_polygon(x0, floor, ramp0, ramp1, y_exit, y_top):
    xs = [x0, ramp0, ramp1, ramp1, x0]
    ys = [floor, floor, y_exit, y_top, y_top]
    return np.column_stack([xs, ys])


def fig_underbody_path():
    fig, ax = new_fig(9.2, 4.5)
    ax.plot([0.35, 8.9], [0.40, 0.40], color="black", lw=1.4, zorder=2)
    ax.text(8.45, 0.58, "road", fontsize=10, ha="center")
    body = underbody_polygon(1.45, 1.55, 5.15, 8.05, 2.55, 3.05)
    ax.add_patch(Polygon(body, closed=True, facecolor="white", edgecolor="black", lw=1.6, zorder=3))
    # One channel streamline, in the gap, diverging under the ramp but below it.
    xs_flat = np.linspace(0.4, 5.15, 30)
    xs_ramp = np.linspace(5.15, 8.45, 24)
    y_flat = np.full_like(xs_flat, 0.95)
    y_ramp = np.linspace(0.95, 1.55, len(xs_ramp))
    stream(ax, np.concatenate([xs_flat, xs_ramp]), np.concatenate([y_flat, y_ramp]))
    ax.text(3.15, 1.28, "lower $P$", ha="center", fontsize=11)
    ax.text(6.45, 0.68, "$P$ rises", ha="center", fontsize=11)
    ax.text(3.3, 3.28, "flat floor", ha="center", fontsize=11)
    ax.text(6.7, 3.28, "diffuser", ha="center", fontsize=11)
    ax.text(
        4.6,
        0.02,
        "Low pressure is under the floor. The diffuser is the recovery, if the channel stays attached.",
        ha="center",
        fontsize=10,
    )
    ax.set_xlim(0.15, 9.15)
    ax.set_ylim(-0.15, 3.55)
    ax.set_title("Whole underbody path: fast throat, then pressure recovery", fontsize=13, pad=8)
    save(fig, "underbody-path.png")


def fig_splitter_inlet():
    fig, ax = new_fig(9.0, 4.5)
    ax.plot([0.3, 8.7], [0.40, 0.40], color="black", lw=1.4, zorder=2)
    ax.text(8.25, 0.58, "road", fontsize=10)
    # Splitter lip, then body with a flat floor.
    ax.add_patch(
        Polygon(
            [[2.20, 1.35], [2.85, 1.35], [2.85, 1.52], [2.20, 1.52]],
            closed=True,
            facecolor="white",
            edgecolor="black",
            lw=1.5,
            zorder=3,
        )
    )
    body = underbody_polygon(2.85, 1.52, 6.4, 8.15, 2.25, 2.85)
    ax.add_patch(Polygon(body, closed=True, facecolor="white", edgecolor="black", lw=1.6, zorder=3))
    # h is left of every streamline. Upper branch clears the nose; lower branch uses the inlet.
    ax.annotate(
        "",
        xy=(0.72, 0.40),
        xytext=(0.72, 1.35),
        arrowprops=dict(arrowstyle="<->", lw=1.05),
    )
    ax.text(0.42, 0.88, r"$h$", fontsize=13, ha="center", va="center")
    xs_over = np.linspace(1.05, 5.5, 40)
    y_over = np.where(
        xs_over < 1.8,
        2.45,
        2.45 + 0.9 * np.clip((xs_over - 1.8) / 0.6, 0, 1) ** 2,
    )
    y_over = np.minimum(y_over, 3.35)
    stream(ax, xs_over, y_over)
    xs_under = np.linspace(1.2, 5.7, 30)
    stream(ax, xs_under, np.full_like(xs_under, 0.88))
    ax.text(1.45, 1.43, "splitter", fontsize=11, ha="center", va="center")
    ax.text(1.35, 2.05, "higher $P$", fontsize=11, ha="center")
    ax.set_xlim(0.1, 8.9)
    ax.set_ylim(0.05, 3.55)
    ax.set_title("Splitter: stagnation on the lip, inlet height set on purpose", fontsize=13, pad=8)
    save(fig, "splitter-inlet.png")


def fig_ride_height():
    fig, ax = new_fig(9.2, 4.4)

    def one(x_shift, road_y, caption):
        floor = 2.15
        body = underbody_polygon(x_shift + 1.15, floor, x_shift + 2.7, x_shift + 4.15, floor + 0.7, floor + 1.05)
        ax.add_patch(Polygon(body, closed=True, facecolor="white", edgecolor="black", lw=1.5, zorder=3))
        ax.plot([x_shift + 0.2, x_shift + 4.4], [road_y, road_y], color="black", lw=1.3)
        gap_mid = 0.5 * (road_y + floor)
        xs = np.linspace(x_shift + 1.25, x_shift + 4.05, 40)
        s = np.clip((xs - (x_shift + 2.7)) / 1.35, 0, 1)
        ys = gap_mid + 0.16 * (floor - road_y) * s**2
        stream(ax, xs, ys)
        ax.annotate(
            "",
            xy=(x_shift + 0.72, road_y),
            xytext=(x_shift + 0.72, floor),
            arrowprops=dict(arrowstyle="<->", lw=1.05),
        )
        ax.text(x_shift + 0.38, 0.5 * (road_y + floor), r"$h$", fontsize=13, ha="center", va="center")
        ax.text(x_shift + 2.3, 0.28, caption, ha="center", fontsize=11)

    one(0.15, 0.85, "larger clearance")
    one(4.85, 1.45, "tighter channel")
    ax.text(4.6, 3.55, "Same body. Only ride height changes.", ha="center", fontsize=12)
    ax.set_xlim(0.0, 9.5)
    ax.set_ylim(0.05, 3.75)
    ax.set_title(r"Channel area is width times $h$", fontsize=13, pad=8)
    save(fig, "ride-height-pair.png")


def fig_blockoff():
    fig, ax = new_fig(9.0, 4.2)

    def nose(x0, closed):
        ax.plot([x0, x0 + 4.0], [0.4, 0.4], color="black", lw=1.3)
        body = underbody_polygon(x0 + 1.3, 1.5, x0 + 3.1, x0 + 3.9, 2.05, 2.55)
        ax.add_patch(Polygon(body, closed=True, facecolor="white", edgecolor="black", lw=1.5, zorder=3))
        if closed:
            ax.add_patch(
                Polygon(
                    [[x0 + 1.3, 0.4], [x0 + 1.48, 0.4], [x0 + 1.48, 1.5], [x0 + 1.3, 1.5]],
                    closed=True,
                    facecolor="white",
                    edgecolor="black",
                    lw=1.4,
                    zorder=4,
                )
            )
            xs = np.linspace(x0 + 0.2, x0 + 3.5, 36)
            y = 2.45 + 0.7 / (1 + np.exp(-(xs - (x0 + 0.85)) / 0.16))
            y = np.clip(y, 2.45, 3.15)
            stream(ax, xs, y)
            ax.text(x0 + 2.15, 0.12, "block-off control", ha="center", fontsize=11)
        else:
            xs = np.linspace(x0 + 0.2, x0 + 3.3, 26)
            stream(ax, xs, np.full_like(xs, 0.95))
            ax.text(x0 + 2.15, 0.12, "open inlet", ha="center", fontsize=11)

    nose(0.25, False)
    nose(4.7, True)
    ax.set_xlim(0.05, 9.0)
    ax.set_ylim(-0.05, 3.25)
    ax.set_title("A blocked inlet is the control, not another story", fontsize=13, pad=8)
    save(fig, "blockoff-control.png")


def fig_interaction_bars():
    fig, ax = plt.subplots(figsize=(7.8, 4.2), dpi=DPI)
    fig.patch.set_facecolor(FACE)
    ax.set_facecolor(FACE)
    labels = ["wing only\nmeasured", "diffuser only\nmeasured", "sum of solos\nprediction", "both together\nmeasured"]
    vals = [1.2, 0.8, 2.0, 1.5]
    bars = ax.bar(np.arange(4), vals, color="white", edgecolor="black", lw=1.3, width=0.62)
    bars[2].set_hatch("///")
    bars[2].set_facecolor("white")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.06, f"{v:.1f}", ha="center", fontsize=12)
    ax.set_xticks(np.arange(4))
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylabel(r"extra downforce $|\Delta F_z|$ (N)", fontsize=11)
    ax.set_ylim(0, 2.55)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(r"Both together give 1.5 N, not $1.2+0.8=2.0$ N", fontsize=13)
    fig.savefig(OUT / "interaction-bars.png", dpi=DPI, bbox_inches="tight", facecolor=FACE, pad_inches=0.16)
    fig.savefig(OUT / "interaction-bars.svg", bbox_inches="tight", facecolor=FACE, pad_inches=0.16)
    plt.close(fig)
    print("wrote interaction-bars.png")


def fig_story_spine():
    fig, ax = new_fig(10.4, 3.3)
    labels = [
        ("Design\nquestion", "Week 1 metric"),
        ("Physics\nmodel", r"$q$, $C$, Re"),
        ("Measurement", "tare, replicates"),
        ("Result", "what changed"),
        ("Next step", "what to keep"),
    ]
    w, h = 1.48, 1.35
    y = 0.85
    gap = 0.78
    x = 0.15
    for i, (title, sub) in enumerate(labels):
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                w,
                h,
                boxstyle="round,pad=0.04,rounding_size=0.08",
                facecolor="white",
                edgecolor="black",
                lw=1.3,
                zorder=2,
            )
        )
        ax.text(x + w / 2, y + 0.82, title, ha="center", va="center", fontsize=11, zorder=3)
        ax.text(x + w / 2, y + 0.32, sub, ha="center", va="center", fontsize=9, color="0.25", zorder=3)
        if i < len(labels) - 1:
            tip(ax, x + w + 0.12, y + h / 2, gap - 0.42, 0, lw=1.1, ms=8)
        x += w + gap
    ax.set_xlim(0.05, x + 0.05)
    ax.set_ylim(0.35, 2.55)
    ax.set_title("The report is this chain, in this order", fontsize=13, pad=6)
    save(fig, "story-spine.png")


def fig_claim_ladder():
    fig, ax = new_fig(9.0, 4.6)
    rows = [
        ("The force changed", "Calibration in newtons, and a tare"),
        (r"$C_L$ or $C_D$ changed", r"Measured $v$, frozen $A$, same $q$"),
        ("This config ranks higher here", "Replicates, and one variable at a time"),
        ("The road car has this $C_D$", "Matched Re — not a result of this course"),
    ]
    y = 3.55
    for i, (claim, need) in enumerate(rows):
        face = "0.94" if i == 3 else "white"
        ax.add_patch(
            FancyBboxPatch(
                (0.35, y - 0.72),
                8.3,
                0.78,
                boxstyle="round,pad=0.02,rounding_size=0.06",
                facecolor=face,
                edgecolor="black",
                lw=1.2,
            )
        )
        ax.text(0.55, y - 0.33, claim, ha="left", va="center", fontsize=12)
        ax.text(8.4, y - 0.33, need, ha="right", va="center", fontsize=11)
        y -= 0.95
    ax.set_xlim(0.1, 8.9)
    ax.set_ylim(0.15, 4.15)
    ax.set_title("Each stronger sentence needs evidence the weaker one did not", fontsize=13, pad=8)
    save(fig, "claim-ladder.png")


if __name__ == "__main__":
    fig_aoa_definition()
    fig_stall_inverted()
    fig_cl_cd_aoa()
    fig_efficiency_aoa()
    fig_underbody_path()
    fig_splitter_inlet()
    fig_ride_height()
    fig_blockoff()
    fig_interaction_bars()
    fig_story_spine()
    fig_claim_ladder()
