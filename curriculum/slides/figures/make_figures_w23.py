#!/usr/bin/env python3
"""Week 2–3 lecture figures: textbook line drawings."""

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
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    fig.savefig(path.with_suffix(".svg"), bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    plt.close(fig)
    print("wrote", path.name)


def arrow(ax, origin, vec, label="", loff=(0, 0), *, lw=1.6, ms=14):
    o = np.array(origin, dtype=float)
    end = o + np.array(vec, dtype=float)
    ax.add_patch(
        FancyArrowPatch(
            o,
            end,
            arrowstyle="-|>",
            mutation_scale=ms,
            lw=lw,
            color="black",
            shrinkA=0,
            shrinkB=0,
            zorder=5,
        )
    )
    if label:
        lp = end + np.array(loff, dtype=float)
        ax.text(lp[0], lp[1], label, fontsize=12, ha="center", va="center", zorder=6)


def fig_pressure_definition():
    fig, ax = new_fig(7.4, 3.6)
    ax.add_patch(Rectangle((1.4, 0.6), 2.4, 1.7, fill=False, lw=1.6))
    # distributed pressure ticks into the top face
    for x in np.linspace(1.6, 3.6, 7):
        ax.annotate(
            "",
            xy=(x, 2.3),
            xytext=(x, 2.95),
            arrowprops=dict(arrowstyle="-|>", lw=1.1, mutation_scale=10),
        )
    ax.text(2.6, 3.18, r"fluid pressure $P$", ha="center", fontsize=12)
    ax.text(2.6, 1.45, "surface, area $A$", ha="center", fontsize=12)
    arrow(ax, (5.15, 1.45), (0, -1.15), r"$F=PA$", (0.55, -0.05), lw=1.8, ms=16)
    ax.text(6.35, 2.55, r"$P=\dfrac{F}{A}$", fontsize=16, ha="center")
    ax.text(6.35, 1.85, r"$1~\mathrm{Pa}=1~\mathrm{N/m^2}$", fontsize=11, ha="center")
    ax.set_xlim(0.8, 7.6)
    ax.set_ylim(0.2, 3.5)
    ax.set_title("Pressure is force per area", fontsize=13, pad=8)
    save(fig, "pressure-definition.png")


def fig_pressure_difference():
    fig, ax = new_fig(8.8, 3.8)

    def plate(x0, title, p_top, p_bot, net_label, top_len=0.67, bot_len=0.67):
        ax.text(x0 + 1.5, 3.35, title, ha="center", fontsize=11)
        ax.plot([x0, x0 + 3.0], [1.7, 1.7], color="black", lw=3.0, solid_capstyle="butt")
        for x in np.linspace(x0 + 0.25, x0 + 2.75, 6):
            ax.annotate(
                "",
                xy=(x, 1.78),
                xytext=(x, 1.78 + top_len),
                arrowprops=dict(arrowstyle="-|>", lw=0.9, mutation_scale=9),
            )
            ax.annotate(
                "",
                xy=(x, 1.62),
                xytext=(x, 1.62 - bot_len),
                arrowprops=dict(arrowstyle="-|>", lw=0.9, mutation_scale=9),
            )
        ax.text(x0 + 1.5, 1.78 + top_len + 0.22, p_top, ha="center", fontsize=11)
        ax.text(x0 + 1.5, 1.62 - bot_len - 0.28, p_bot, ha="center", fontsize=11)
        ax.text(x0 + 1.5, -0.05, net_label, ha="center", fontsize=11)

    plate(0.2, "Same $P$ on both faces", r"$P_{\mathrm{atm}}$", r"$P_{\mathrm{atm}}$", r"net $F=0$")
    plate(
        4.7,
        "Pressure difference",
        r"$P+\Delta P$",
        r"$P$",
        r"net $F\approx\Delta P\,A$  (down)",
        top_len=1.05,
        bot_len=0.50,
    )
    ax.set_xlim(0.0, 8.1)
    ax.set_ylim(-0.35, 3.7)
    ax.set_title("Aero force comes from pressure differences", fontsize=13, pad=6)
    save(fig, "pressure-difference.png")


def fig_q_vs_speed():
    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=DPI)
    fig.patch.set_facecolor(FACE)
    ax.set_facecolor(FACE)
    rho = 1.2
    v = np.linspace(0, 35, 200)
    q = 0.5 * rho * v**2
    ax.plot(v, q, color="black", lw=1.8)
    for vv, dx, dy in ((10, 3.0, 80), (20, 3.5, 70), (30, -8.5, -80)):
        qq = 0.5 * rho * vv**2
        ax.plot([vv], [qq], "o", color="black", ms=6)
        ax.annotate(
            rf"$v={vv}$" + "\n" + rf"$q={qq:.0f}\,\mathrm{{Pa}}$",
            xy=(vv, qq),
            xytext=(vv + dx, qq + dy),
            fontsize=9,
            arrowprops=dict(arrowstyle="-", lw=0.6),
        )
    ax.text(8, 350, r"double $v$ $\Rightarrow$ quadruple $q$", fontsize=11)
    ax.set_xlabel(r"speed $v$ (m/s)", fontsize=11)
    ax.set_ylabel(r"dynamic pressure $q=\frac{1}{2}\rho v^{2}$ (Pa)", fontsize=11)
    ax.set_xlim(0, 38)
    ax.set_ylim(0, 620)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(r"Doubling $v$ quadruples $q$  ($\rho=1.2\,\mathrm{kg/m^3}$)", fontsize=13)
    fig.savefig(OUT / "q-vs-speed.png", dpi=DPI, bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    fig.savefig(OUT / "q-vs-speed.svg", bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    plt.close(fig)
    print("wrote q-vs-speed.png")


def fig_ram_pressure():
    fig, ax = new_fig(7.6, 3.5)
    # flow arrows
    for y in (1.0, 1.5, 2.0):
        arrow(ax, (0.3, y), (1.4, 0), lw=1.2, ms=11)
    ax.text(1.0, 2.45, r"free stream $v$", ha="center", fontsize=11)
    # facing plate
    ax.plot([2.2, 2.2], [0.55, 2.45], color="black", lw=3.0)
    ax.text(2.55, 1.5, "facing\narea $A$", fontsize=10, va="center")
    ax.text(4.7, 2.2, r"$q\equiv\frac{1}{2}\rho v^{2}$", fontsize=15, ha="center")
    ax.text(4.7, 1.55, "characteristic inertial\npressure scale (Pa)", fontsize=10, ha="center")
    ax.text(4.7, 0.75, r"$F\sim q A$  before $C_D,C_L$", fontsize=12, ha="center")
    ax.set_xlim(0.1, 6.5)
    ax.set_ylim(0.3, 3.0)
    ax.set_title("Dynamic pressure is the scale of aero loading", fontsize=13, pad=8)
    save(fig, "dynamic-pressure-scale.png")


def inverted_wing_path():
    """Simple inverted camber (high P on top, suction toward road)."""
    x = np.linspace(0, 2.4, 40)
    y_upper = 0.22 + 0.04 * np.sin(np.pi * x / 2.4)  # flatter upper (sky)
    y_lower = 0.22 - 0.22 * np.sin(np.pi * x / 2.4)  # cambered toward road
    y_lower[-1] = y_upper[-1]
    y_lower[0] = y_upper[0]
    return x, y_upper, y_lower


def fig_wing_pressure():
    fig, ax = new_fig(8.0, 4.2)
    x, yu, yl = inverted_wing_path()
    x = x + 2.0
    ax.plot(x, yu, color="black", lw=1.6)
    ax.plot(x, yl, color="black", lw=1.6)
    # plus / minus marks
    ax.text(3.2, 0.55, r"$+$  higher $P$", fontsize=12, ha="center")
    ax.text(3.2, -0.22, r"$-$  lower $P$", fontsize=12, ha="center")
    # net force from a mid-chord point (not an FBD of a car; pressure resultants)
    mid = (3.15, 0.08)
    arrow(ax, mid, (0.0, -1.05), r"$D_w$", (0.32, -0.08), lw=1.8, ms=15)
    for y in (0.85, 1.05, 1.25):
        arrow(ax, (0.35, y), (1.15, 0), lw=1.0, ms=9)
    ax.text(0.9, 1.48, "airflow", fontsize=10, ha="center")
    ax.plot([1.7, 6.3], [-0.85, -0.85], color="black", lw=1.2)
    ax.text(4.0, -1.08, "road", fontsize=10, ha="center")
    ax.text(
        4.0,
        -1.42,
        "Car wing is inverted relative to an airplane wing:\nnet pressure force is into the road (downforce).",
        ha="center",
        fontsize=9,
    )
    ax.set_xlim(0.1, 7.0)
    ax.set_ylim(-1.6, 1.75)
    ax.set_title("Week 2 sketch: hypothesized pressure on a downforce wing", fontsize=13, pad=6)
    save(fig, "wing-pressure-map.png")


def fig_splitter_pressure():
    fig, ax = new_fig(8.2, 3.8)
    # simple nose + splitter
    ax.plot([1.6, 2.3, 3.6, 4.2], [1.55, 1.55, 1.05, 1.05], color="black", lw=1.5)
    ax.plot([4.2, 4.2, 1.9, 1.6], [1.05, 0.55, 0.55, 1.55], color="black", lw=1.5)
    ax.plot([1.15, 2.15], [0.55, 0.55], color="black", lw=2.4, solid_capstyle="butt")
    ax.plot([0.7, 6.3], [0.15, 0.15], color="black", lw=1.2)
    ax.text(1.15, 0.72, "splitter", fontsize=10, ha="center")
    ax.text(2.9, 1.25, "body", fontsize=10, ha="center")
    ax.text(3.5, 1.85, r"$+$ stagnation / high $P$", fontsize=11)
    ax.text(3.2, 0.32, r"$-$ keep high $P$ from flooding the underbody", fontsize=11)
    for y in (1.7, 1.9):
        arrow(ax, (0.4, y), (0.9, 0), lw=1.0, ms=9)
    ax.text(0.85, 2.15, "airflow", fontsize=10, ha="center")
    ax.text(
        3.5,
        -0.25,
        "Hypothesis only. Week 4: why Bernoulli slogans can fail. Sensors decide.",
        ha="center",
        fontsize=9,
    )
    ax.set_xlim(0.2, 6.6)
    ax.set_ylim(-0.45, 2.4)
    ax.set_title("Week 2 sketch: hypothesized splitter / front underbody", fontsize=13, pad=6)
    save(fig, "splitter-pressure-map.png")


def fig_aero_components():
    fig, ax = new_fig(7.6, 4.4)
    # small car outline
    ax.plot([1.4, 1.7, 2.1, 3.3, 3.9, 4.15, 4.25, 4.25, 4.05, 1.5, 1.4],
            [1.35, 1.35, 1.85, 1.85, 1.40, 1.40, 1.32, 1.05, 1.05, 1.05, 1.35],
            color="black", lw=1.3)
    ax.add_patch(Circle((2.05, 1.05), 0.18, fill=False, lw=1.2))
    ax.add_patch(Circle((3.75, 1.05), 0.18, fill=False, lw=1.2))
    ax.plot([0.6, 5.5], [0.87, 0.87], color="black", lw=1.2)
    cm = (2.85, 1.32)
    ax.add_patch(Circle(cm, 0.09, fill=True, facecolor="white", edgecolor="black", lw=1.1, zorder=7))
    ax.plot([cm[0] - 0.05, cm[0] + 0.05], [cm[1], cm[1]], color="black", lw=1.0, zorder=8)
    ax.plot([cm[0], cm[0]], [cm[1] - 0.05, cm[1] + 0.05], color="black", lw=1.0, zorder=8)
    arrow(ax, cm, (-1.35, 0), r"$F_D$", (-0.15, 0.22))
    arrow(ax, cm, (0, -1.15), "", (0, 0))
    ax.text(cm[0] + 0.40, cm[1] - 0.55, r"$F_L<0$", fontsize=12)
    ax.text(3.55, 1.58, r"$D_w=-F_L$", fontsize=11)
    for y in (2.15, 2.35):
        arrow(ax, (0.5, y), (1.0, 0), lw=1.0, ms=9)
    ax.text(1.0, 2.58, r"relative wind", fontsize=10, ha="center")
    ax.text(
        2.9,
        -0.22,
        r"Same CM rule as Week 1.  $F_D$ aft;  $F_L$ up-positive (downforce is $F_L<0$).",
        ha="center",
        fontsize=10,
    )
    ax.set_xlim(0.2, 5.8)
    ax.set_ylim(-0.50, 2.85)
    ax.set_title("Connect to Week 1: aero force has drag and lift parts", fontsize=13, pad=6)
    save(fig, "aero-force-components.png")


def fig_reference_area():
    fig, ax = new_fig(8.4, 4.0)
    # side view small
    ax.plot([0.5, 0.75, 1.1, 2.2, 2.7, 2.9, 3.0, 3.0, 2.8, 0.6, 0.5],
            [1.7, 1.7, 2.15, 2.15, 1.75, 1.75, 1.68, 1.42, 1.42, 1.42, 1.7],
            color="black", lw=1.2)
    ax.add_patch(Circle((1.05, 1.42), 0.16, fill=False, lw=1.1))
    ax.add_patch(Circle((2.55, 1.42), 0.16, fill=False, lw=1.1))
    ax.plot([0.4, 3.15], [1.26, 1.26], color="black", lw=1.0)
    ax.text(1.75, 1.00, "side view", ha="center", fontsize=10)
    # frontal silhouette
    ax.add_patch(FancyBboxPatch((4.5, 1.25), 2.3, 1.45, boxstyle="round,pad=0.02,rounding_size=0.08",
                                fill=False, lw=1.5))
    ax.add_patch(Circle((5.05, 1.43), 0.18, fill=False, lw=1.1))
    ax.add_patch(Circle((6.25, 1.43), 0.18, fill=False, lw=1.1))
    ax.plot([4.5, 6.8], [1.25, 1.25], color="black", lw=1.0)
    ax.annotate(
        "",
        xy=(4.5, 2.85),
        xytext=(6.8, 2.85),
        arrowprops=dict(arrowstyle="<->", lw=1.2),
    )
    ax.annotate(
        "",
        xy=(7.05, 1.25),
        xytext=(7.05, 2.70),
        arrowprops=dict(arrowstyle="<->", lw=1.2),
    )
    ax.text(5.65, 3.05, r"width", ha="center", fontsize=10)
    ax.text(7.45, 1.9, r"height", ha="center", va="center", fontsize=10)
    ax.text(5.65, 0.75, r"frontal area $A$ (projected)", ha="center", fontsize=11)
    ax.set_xlim(0.2, 8.0)
    ax.set_ylim(0.55, 3.35)
    ax.set_title("Primary $A$ for this course: vehicle frontal (projected) area", fontsize=13, pad=6)
    save(fig, "reference-area-frontal.png")


def fig_planform_vs_frontal():
    fig, ax = new_fig(8.0, 3.6)
    ax.add_patch(Rectangle((0.7, 1.15), 2.6, 0.7, fill=False, lw=1.5, angle=8))
    ax.text(2.0, 2.25, "wing planform $A_{\\mathrm{wing}}$", ha="center", fontsize=11)
    ax.text(2.0, 0.7, "Useful for a wing-only study.\nSay so if you use it.", ha="center", fontsize=9)
    ax.add_patch(FancyBboxPatch((4.7, 0.95), 2.1, 1.45, boxstyle="round,pad=0.02,rounding_size=0.08",
                                fill=False, lw=1.5))
    ax.text(5.75, 2.65, r"vehicle frontal $A$", ha="center", fontsize=11)
    ax.text(5.75, 0.45, "Required for comparing\nfull-car configs this term.", ha="center", fontsize=9)
    ax.set_xlim(0.3, 7.4)
    ax.set_ylim(0.15, 3.05)
    ax.set_title("Do not mix area definitions in one table of $C_D,C_L$", fontsize=13, pad=6)
    save(fig, "reference-area-two-defs.png")


def fig_coefficient_meaning():
    fig, ax = new_fig(8.2, 3.4)
    ax.text(4.1, 2.55, r"$F_D = q\,C_D\,A$", fontsize=18, ha="center")
    ax.text(4.1, 1.85, r"$F_L = q\,C_L\,A$", fontsize=18, ha="center")
    ax.text(4.1, 1.05, r"$C_D=\dfrac{F_D}{qA}\qquad C_L=\dfrac{F_L}{qA}$", fontsize=15, ha="center")
    ax.text(
        4.1,
        0.35,
        r"$C_D,C_L$ package shape, attitude, and (quietly) Reynolds number.",
        ha="center",
        fontsize=10,
    )
    ax.set_xlim(0.3, 7.9)
    ax.set_ylim(0.05, 3.0)
    ax.set_title(r"Coefficients turn a force into a fair number at given $q$ and $A$", fontsize=13, pad=8)
    save(fig, "coefficient-definition.png")


def fig_efficiency():
    fig, ax = plt.subplots(figsize=(7.4, 3.8), dpi=DPI)
    fig.patch.set_facecolor(FACE)
    ax.set_facecolor(FACE)
    configs = ["baseline\n$C_L=-0.30$\n$C_D=0.45$", "new wing\n$C_L=-0.50$\n$C_D=0.55$"]
    e = [0.30 / 0.45, 0.50 / 0.55]
    ax.bar([0, 1], e, color="white", edgecolor="black", lw=1.4, width=0.45)
    for i, val in enumerate(e):
        ax.text(i, val + 0.03, rf"$|C_L|/C_D={val:.2f}$", ha="center", fontsize=11)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(configs, fontsize=10)
    ax.set_ylabel(r"downforce-to-drag  $|C_L|/C_D$")
    ax.set_ylim(0, 1.15)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title("Same $A$: efficiency rose, but drag rose too", fontsize=13)
    fig.savefig(OUT / "efficiency-ratio.png", dpi=DPI, bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    fig.savefig(OUT / "efficiency-ratio.svg", bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    plt.close(fig)
    print("wrote efficiency-ratio.png")


if __name__ == "__main__":
    fig_pressure_definition()
    fig_pressure_difference()
    fig_q_vs_speed()
    fig_ram_pressure()
    fig_wing_pressure()
    fig_splitter_pressure()
    fig_aero_components()
    fig_reference_area()
    fig_planform_vs_frontal()
    fig_coefficient_meaning()
    fig_efficiency()
