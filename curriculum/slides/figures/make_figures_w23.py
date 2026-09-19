#!/usr/bin/env python3
"""Week 2–3 lecture figures: textbook line drawings (revised)."""

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


def arrow(ax, origin, vec, label="", loff=(0, 0), *, lw=1.6, ms=14, ha="center", va="center"):
    o = np.asarray(origin, dtype=float)
    end = o + np.asarray(vec, dtype=float)
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
        lp = end + np.asarray(loff, dtype=float)
        ax.text(lp[0], lp[1], label, fontsize=12, ha=ha, va=va, zorder=6)


def cm_marker(ax, x, y, r=0.10):
    ax.add_patch(
        Circle((x, y), r, fill=True, facecolor="white", edgecolor="black", lw=1.2, zorder=8)
    )
    s = r * 0.62
    ax.plot([x - s, x + s], [y, y], color="black", lw=1.1, zorder=9)
    ax.plot([x, x], [y - s, y + s], color="black", lw=1.1, zorder=9)


def simple_car(ax, x0, y_road, scale=1.0):
    """Side-view outline: cabin on a box, wheels on the road. Returns CM."""
    s = scale
    r = 0.22 * s
    hub = y_road + r
    body_y0 = hub + 0.06 * s
    body_h = 0.42 * s
    x_nose = x0 + 0.12 * s
    x_tail = x0 + 2.55 * s
    # chassis box
    ax.plot(
        [x_nose, x_tail, x_tail, x_nose, x_nose],
        [body_y0, body_y0, body_y0 + body_h, body_y0 + body_h, body_y0],
        color="black",
        lw=1.45,
        zorder=2,
    )
    # cabin
    xc0, xc1 = x0 + 0.70 * s, x0 + 1.95 * s
    roof = body_y0 + body_h + 0.38 * s
    ax.plot(
        [x0 + 0.55 * s, xc0, xc1, x0 + 2.15 * s],
        [body_y0 + body_h, roof, roof, body_y0 + body_h],
        color="black",
        lw=1.45,
        zorder=2,
    )
    for wx in (0.55, 2.10):
        ax.add_patch(Circle((x0 + s * wx, hub), r, fill=False, lw=1.35, zorder=2))
        ax.add_patch(Circle((x0 + s * wx, hub), 0.08 * s, fill=False, lw=0.8, zorder=2))
    cm = (0.5 * (x_nose + x_tail), body_y0 + 0.55 * body_h)
    return cm


def fig_pressure_definition():
    fig, ax = new_fig(7.6, 3.7)
    ax.add_patch(Rectangle((1.55, 0.55), 2.5, 1.75, fill=False, lw=1.6, zorder=2))
    for x in np.linspace(1.80, 3.80, 6):
        ax.annotate(
            "",
            xy=(x, 2.30),
            xytext=(x, 3.05),
            arrowprops=dict(arrowstyle="-|>", lw=1.1, mutation_scale=10),
        )
    ax.text(2.80, 3.28, r"uniform pressure $P$", ha="center", fontsize=12)
    ax.text(1.22, 1.42, r"area $A$", ha="right", fontsize=12)
    # resultant from the loaded face into the solid; label outside the box
    arrow(ax, (2.80, 2.30), (0, -1.05), r"$F=PA$", (1.55, 0.15), lw=1.9, ms=16, ha="left")
    ax.text(6.05, 2.55, r"$P=\dfrac{F}{A}$", fontsize=16, ha="center")
    ax.text(6.05, 1.75, r"$1~\mathrm{Pa}=1~\mathrm{N/m^2}$", fontsize=11, ha="center")
    ax.set_xlim(0.35, 7.5)
    ax.set_ylim(0.25, 3.55)
    ax.set_title("Pressure is force per area (resultant into the surface)", fontsize=13, pad=8)
    save(fig, "pressure-definition.png")


def fig_pressure_difference():
    fig, ax = new_fig(8.8, 4.0)

    def plate(x0, title, p_top, p_bot, net_label, top_len, bot_len):
        ax.text(x0 + 1.45, 3.55, title, ha="center", fontsize=11)
        ax.plot([x0 + 0.15, x0 + 2.75], [1.85, 1.85], color="black", lw=3.2, solid_capstyle="butt")
        for x in np.linspace(x0 + 0.40, x0 + 2.50, 5):
            ax.annotate(
                "",
                xy=(x, 1.93),
                xytext=(x, 1.93 + top_len),
                arrowprops=dict(arrowstyle="-|>", lw=0.95, mutation_scale=9),
            )
            ax.annotate(
                "",
                xy=(x, 1.77),
                xytext=(x, 1.77 - bot_len),
                arrowprops=dict(arrowstyle="-|>", lw=0.95, mutation_scale=9),
            )
        ax.text(x0 + 1.45, 1.93 + top_len + 0.22, p_top, ha="center", fontsize=11)
        ax.text(x0 + 1.45, 1.77 - bot_len - 0.28, p_bot, ha="center", fontsize=11)
        ax.text(x0 + 1.45, 0.05, net_label, ha="center", fontsize=11)

    plate(0.15, "Same $P$ both faces", r"$P_{\mathrm{atm}}$", r"$P_{\mathrm{atm}}$", r"net $F=0$", 0.72, 0.72)
    plate(
        4.55,
        r"Difference $\Delta P$",
        r"$P+\Delta P$",
        r"$P$",
        r"net $F\approx\Delta P\,A$ (down)",
        1.05,
        0.48,
    )
    ax.set_xlim(0.0, 8.0)
    ax.set_ylim(-0.25, 3.85)
    ax.set_title("Aero force comes from pressure differences", fontsize=13, pad=6)
    save(fig, "pressure-difference.png")


def fig_density():
    fig, ax = new_fig(8.2, 3.6)
    ax.add_patch(Rectangle((0.9, 0.55), 1.7, 1.7, fill=False, lw=1.5))
    ax.plot([0.9, 1.25], [2.25, 2.55], color="black", lw=1.0)
    ax.plot([2.60, 2.95], [2.25, 2.55], color="black", lw=1.0)
    ax.plot([2.60, 2.95], [0.55, 0.85], color="black", lw=1.0)
    ax.plot([1.25, 2.95], [2.55, 2.55], color="black", lw=1.0)
    ax.plot([2.95, 2.95], [0.85, 2.55], color="black", lw=1.0)
    ax.text(1.75, 1.40, r"$m$", ha="center", fontsize=16)
    ax.annotate("", xy=(0.9, 0.40), xytext=(2.60, 0.40), arrowprops=dict(arrowstyle="<->", lw=1.1))
    ax.text(1.75, 0.18, r"$L$", ha="center", fontsize=12)
    ax.text(4.7, 2.55, r"density $\rho=\dfrac{m}{V}$", fontsize=16, ha="left")
    ax.text(4.7, 1.85, r"$V=L^{3}$", fontsize=13, ha="left")
    ax.text(4.7, 1.35, r"$[\rho]=\mathrm{kg/m^3}$", fontsize=13, ha="left")
    ax.text(4.7, 0.75, r"air (room): $\rho\approx 1.2~\mathrm{kg/m^3}$", fontsize=12, ha="left")
    ax.set_xlim(0.5, 8.3)
    ax.set_ylim(0.0, 3.1)
    ax.set_title(r"Density is mass per volume — how much air is in a box", fontsize=13, pad=8)
    save(fig, "density-definition.png")


def fig_ke_to_q():
    fig, ax = new_fig(8.6, 4.0)
    lines = [
        (3.2, r"kinetic energy of a blob of air:  $KE=\frac{1}{2}mv^{2}$"),
        (2.45, r"divide by the blob's volume $V$:"),
        (1.70, r"$\dfrac{KE}{V}=\frac{1}{2}\left(\dfrac{m}{V}\right)v^{2}=\frac{1}{2}\rho v^{2}$"),
        (0.85, r"that energy density is dynamic pressure  $q\equiv\frac{1}{2}\rho v^{2}$"),
        (0.20, r"units: $\mathrm{J/m^3}=\mathrm{N\cdot m/m^3}=\mathrm{N/m^2}=\mathrm{Pa}$"),
    ]
    for y, txt in lines:
        ax.text(4.3, y, txt, ha="center", va="center", fontsize=13)
    ax.set_xlim(0.2, 8.4)
    ax.set_ylim(-0.15, 3.7)
    ax.set_title(r"From intro-physics $KE$ to $q$  (why $\rho$ and $v^{2}$ appear)", fontsize=13, pad=8)
    save(fig, "ke-to-q.png")


def fig_q_vs_speed():
    fig, ax = plt.subplots(figsize=(7.4, 4.3), dpi=DPI)
    fig.patch.set_facecolor(FACE)
    ax.set_facecolor(FACE)
    rho = 1.2
    v = np.linspace(0, 35, 250)
    q = 0.5 * rho * v**2
    ax.plot(v, q, color="black", lw=1.8, zorder=2)
    # labels in empty corners; leaders stay off the curve
    specs = [
        (10, 60, 1.2, 210),
        (20, 240, 2.5, 390),
        (30, 540, 16.5, 610),
    ]
    for vv, qq, tx, ty in specs:
        ax.plot(vv, qq, "o", color="black", ms=6, zorder=3)
        ax.annotate(
            rf"$v={vv}$ m/s" + "\n" + rf"$q={qq:.0f}$ Pa",
            xy=(vv, qq),
            xytext=(tx, ty),
            fontsize=9,
            ha="left",
            va="bottom",
            arrowprops=dict(arrowstyle="-", lw=0.7, color="0.35", shrinkA=4, shrinkB=6),
        )
    ax.text(1.5, 560, r"double $v$ $\Rightarrow$ quadruple $q$", fontsize=11, ha="left")
    ax.set_xlabel(r"speed $v$ (m/s)", fontsize=11)
    ax.set_ylabel(r"$q=\frac{1}{2}\rho v^{2}$  (Pa)", fontsize=11)
    ax.set_xlim(0, 38)
    ax.set_ylim(0, 720)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(r"$q(v)$ for $\rho=1.2\,\mathrm{kg/m^3}$", fontsize=13)
    fig.savefig(OUT / "q-vs-speed.png", dpi=DPI, bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    fig.savefig(OUT / "q-vs-speed.svg", bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    plt.close(fig)
    print("wrote q-vs-speed.png")


def fig_ram_pressure():
    fig, ax = new_fig(8.0, 3.6)
    ax.plot([3.15, 3.15], [0.55, 2.55], color="black", lw=3.0, zorder=3)
    ax.text(4.45, 2.88, r"plate, area $A$", fontsize=11, ha="left")
    for y, y_off in ((2.25, 0.28), (1.55, 0.0), (0.85, -0.28)):
        xs = np.linspace(0.35, 2.95, 20)
        ax.plot(xs, np.full_like(xs, y), color="black", lw=1.15)
        ax.annotate(
            "",
            xy=(2.95, y),
            xytext=(2.55, y),
            arrowprops=dict(arrowstyle="-|>", lw=1.15, mutation_scale=10),
        )
        ax.plot([3.15, 3.60, 4.15], [y, y + y_off, y + 1.35 * y_off], color="0.35", lw=0.9, ls="--")
    ax.text(1.5, 2.95, r"free stream $v$  (stops / splits at the solid)", ha="center", fontsize=10)
    ax.text(6.15, 2.35, r"$q=\frac{1}{2}\rho v^{2}$", fontsize=14, ha="center")
    ax.text(6.15, 1.70, "inertial pressure scale\nof the oncoming air (Pa)", fontsize=10, ha="center")
    ax.text(6.15, 0.90, r"$F\sim qA$  before $C_D,C_L$", fontsize=12, ha="center")
    ax.set_xlim(0.15, 7.6)
    ax.set_ylim(0.15, 3.25)
    ax.set_title("Oncoming air carries $q$; the solid turns that into a force", fontsize=13, pad=8)
    save(fig, "dynamic-pressure-scale.png")


def fig_wing_pressure():
    """Streamlines go around the section; $D_w$ starts on the lower surface."""
    fig, ax = new_fig(8.6, 4.6)
    c = np.linspace(0, 1, 90)
    x = 2.35 + 2.45 * c
    y0 = 1.45
    yu = y0 + 0.07 * np.sin(np.pi * c)
    yl = y0 - 0.30 * np.sin(np.pi * c)
    verts = np.column_stack(
        [np.concatenate([x, x[::-1]]), np.concatenate([yu, yl[::-1]])]
    )
    ax.add_patch(Polygon(verts, closed=True, facecolor="white", edgecolor="black", lw=1.7, zorder=4))

    def stream(xs, ys):
        ax.plot(xs, ys, color="0.25", lw=1.05, zorder=1)
        ax.annotate(
            "",
            xy=(xs[-1], ys[-1]),
            xytext=(xs[-5], ys[-5]),
            arrowprops=dict(arrowstyle="-|>", lw=1.05, mutation_scale=9, color="0.25"),
        )

    # upper: follow the upper surface with a gap, never through the solid
    for off in (0.22, 0.42):
        xs_l = np.linspace(0.25, x[0], 20)
        xs_r = np.linspace(x[-1], 7.45, 24)
        ys_l = np.full_like(xs_l, yu[0] + off)
        ys_w = yu + off
        ys_r = np.full_like(xs_r, yu[-1] + off)
        stream(np.concatenate([xs_l, x, xs_r]), np.concatenate([ys_l, ys_w, ys_r]))

    # stagnation: stops at the leading edge
    ax.plot([0.25, x[0] - 0.02], [y0, y0], color="0.25", lw=1.05, zorder=1)
    ax.annotate(
        "",
        xy=(x[0] - 0.02, y0),
        xytext=(x[0] - 0.45, y0),
        arrowprops=dict(arrowstyle="-|>", lw=1.05, mutation_scale=9, color="0.25"),
    )

    # lower: follow the lower surface, with a gap at mid-chord for $D_w$
    off = -0.16
    i_cut, i_rejoin = int(0.26 * len(c)), int(0.74 * len(c))
    xs_l = np.linspace(0.25, x[0], 20)
    xs_r = np.linspace(x[-1], 7.45, 24)
    ax.plot(
        np.concatenate([xs_l, x[:i_cut]]),
        np.concatenate([np.full_like(xs_l, yl[0] + off), (yl + off)[:i_cut]]),
        color="0.25",
        lw=1.05,
        zorder=1,
    )
    stream(
        np.concatenate([x[i_rejoin:], xs_r]),
        np.concatenate([(yl + off)[i_rejoin:], np.full_like(xs_r, yl[-1] + off)]),
    )
    # far lower streamline, gap at mid-chord so the $D_w$ arrow is in open space
    x_mid = 3.575
    y_surf = float(np.min(yl))
    xs_a = np.linspace(0.25, x_mid - 0.38, 18)
    xs_b = np.linspace(x_mid + 0.42, 7.45, 22)
    y_far = 0.22
    ax.plot(xs_a, np.full_like(xs_a, y_far), color="0.25", lw=1.05, zorder=1)
    stream(xs_b, np.full_like(xs_b, y_far))

    ax.text(0.85, 2.28, "oncoming\nair", ha="center", fontsize=9)
    ax.text(3.58, 2.18, r"$+$ higher $P$", ha="center", fontsize=11, zorder=6)
    ax.text(1.85, 0.72, r"$-$ lower $P$", ha="center", fontsize=11)

    arrow(ax, (x_mid, y_surf), (0.0, -0.72), r"$D_w$", (0.32, -0.08), lw=1.8, ms=15, ha="left")

    ax.plot([0.35, 7.55], [-0.62, -0.62], color="black", lw=1.2)
    ax.text(7.05, -0.48, "road", fontsize=10, ha="center")
    ax.text(
        3.95,
        -1.12,
        "Streamlines split around the solid. They do not wrap through it.\n"
        "Net pressure force on this inverted wing is into the road.",
        ha="center",
        fontsize=9,
    )
    ax.set_xlim(0.1, 7.8)
    ax.set_ylim(-1.35, 2.55)
    ax.set_title("Hypothesized pressure on a downforce wing", fontsize=13, pad=6)
    save(fig, "wing-pressure-map.png")


def fig_splitter_pressure():
    fig, ax = new_fig(8.4, 4.2)
    y_road = 0.18
    ax.plot([0.35, 8.05], [y_road, y_road], color="black", lw=1.3)
    # closed nose / cabin outline
    outline_x = [2.40, 2.40, 3.70, 4.85, 5.55, 5.55, 2.40]
    outline_y = [0.52, 1.58, 1.58, 1.12, 1.12, 0.52, 0.52]
    ax.plot(outline_x, outline_y, color="black", lw=1.5, zorder=3)
    ax.plot([1.55, 2.40], [0.52, 0.52], color="black", lw=2.5, solid_capstyle="butt", zorder=3)
    ax.text(1.55, 0.72, "splitter", fontsize=10, ha="left")
    ax.text(3.55, 1.00, "body", fontsize=10, ha="center", zorder=4)

    # over the roof, well above the outline
    t = np.linspace(0, 1, 50)
    xs = 0.30 + 5.5 * t
    ys = 1.95 - 0.18 * np.clip((xs - 2.45) / 2.4, 0, 1)
    ax.plot(xs, ys, color="0.25", lw=1.05)
    ax.annotate(
        "",
        xy=(xs[-1], ys[-1]),
        xytext=(xs[-4], ys[-4]),
        arrowprops=dict(arrowstyle="-|>", lw=1.05, mutation_scale=9, color="0.25"),
    )
    # stagnation at the vertical face
    ax.plot([0.30, 2.32], [1.05, 1.05], color="0.25", lw=1.05)
    ax.annotate(
        "",
        xy=(2.32, 1.05),
        xytext=(1.90, 1.05),
        arrowprops=dict(arrowstyle="-|>", lw=1.05, mutation_scale=9, color="0.25"),
    )
    # underbody slot — below the splitter, not through the body
    ax.plot([0.30, 5.20], [0.35, 0.35], color="0.25", lw=1.05, ls="--")
    ax.annotate(
        "",
        xy=(5.20, 0.35),
        xytext=(4.80, 0.35),
        arrowprops=dict(arrowstyle="-|>", lw=1.0, mutation_scale=8, color="0.25"),
    )

    ax.text(0.85, 2.28, "oncoming air", fontsize=10, ha="center")
    ax.text(2.50, 2.22, r"$+$ high $P$ (stagnation)", fontsize=11, ha="left")
    ax.text(3.15, -0.08, r"$-$ hypothesis: underbody kept lower $P$", fontsize=10, ha="left")
    ax.text(
        4.2,
        -0.38,
        "Hypothesis only. Streamlines do not pass through the body. Week 4: Bernoulli limits.",
        ha="center",
        fontsize=9,
    )
    ax.set_xlim(0.15, 8.2)
    ax.set_ylim(-0.58, 2.55)
    ax.set_title("Hypothesized splitter / front underbody", fontsize=13, pad=6)
    save(fig, "splitter-pressure-map.png")


def fig_aero_components():
    fig, ax = new_fig(8.2, 4.7)
    y_road = 1.05
    ax.plot([0.45, 7.35], [y_road, y_road], color="black", lw=1.25)
    cm = simple_car(ax, 2.35, y_road, scale=1.20)
    cm_marker(ax, *cm, r=0.11)
    ax.text(cm[0] + 0.18, cm[1] + 0.50, "CM", fontsize=9, ha="left")
    # $F_D$ leaves the outline to the left; label in open air, not on the shaft
    arrow(ax, cm, (-2.15, 0), r"$F_D$", (-0.18, 0.22), lw=1.8, ms=15)
    # $F_L$ between the wheels, down; label to the right of the shaft
    arrow(ax, cm, (0.0, -(cm[1] - y_road) - 0.55), r"$F_L<0$", (0.28, 0.18), lw=1.8, ms=15, ha="left")
    ax.text(cm[0] + 1.35, cm[1] + 0.72, r"$D_w=-F_L$", fontsize=12, ha="left")
    ax.text(1.15, y_road - 0.22, "aft", fontsize=9, ha="center")
    ax.text(
        4.0,
        0.12,
        r"Particle FBD (Week 1): tails at CM.  $F_D$ parallel to motion (aft).  $F_L$ up-positive.",
        ha="center",
        fontsize=9,
    )
    ax.set_xlim(0.2, 7.6)
    ax.set_ylim(-0.05, 3.35)
    ax.set_title("Aero force has two components: drag and lift", fontsize=13, pad=6)
    save(fig, "aero-force-components.png")


def fig_reference_area():
    fig, ax = new_fig(8.6, 4.1)
    y_road = 1.15
    ax.plot([0.35, 3.35], [y_road, y_road], color="black", lw=1.1)
    simple_car(ax, 0.45, y_road, scale=0.95)
    ax.text(1.85, 0.72, "side view", ha="center", fontsize=10)
    box = FancyBboxPatch(
        (4.55, 1.15),
        2.35,
        1.55,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        fill=False,
        lw=1.5,
        zorder=3,
    )
    ax.add_patch(box)
    ax.add_patch(Circle((5.15, 1.38), 0.20, fill=False, lw=1.15, zorder=3))
    ax.add_patch(Circle((6.30, 1.38), 0.20, fill=False, lw=1.15, zorder=3))
    for xx in np.linspace(4.70, 6.70, 8):
        ax.plot([xx, xx + 0.18], [1.20, 2.62], color="0.75", lw=0.6, zorder=1)
    ax.annotate("", xy=(4.55, 2.88), xytext=(6.90, 2.88), arrowprops=dict(arrowstyle="<->", lw=1.15))
    ax.annotate("", xy=(7.15, 1.15), xytext=(7.15, 2.70), arrowprops=dict(arrowstyle="<->", lw=1.15))
    ax.text(5.72, 3.08, "width", ha="center", fontsize=10)
    ax.text(7.55, 1.90, "height", ha="center", va="center", fontsize=10)
    ax.text(5.72, 0.72, r"frontal projected area $A$  (hatched)", ha="center", fontsize=11)
    ax.set_xlim(0.2, 8.3)
    ax.set_ylim(0.45, 3.35)
    ax.set_title(r"Course default: one $A$ = vehicle frontal projection", fontsize=13, pad=6)
    save(fig, "reference-area-frontal.png")


def fig_planform_vs_frontal():
    fig, ax = new_fig(8.2, 3.7)
    ax.add_patch(Rectangle((0.85, 1.15), 2.5, 0.85, fill=False, lw=1.5))
    ax.text(2.10, 2.28, r"wing planform $A_{\mathrm{wing}}$", ha="center", fontsize=11)
    ax.text(2.10, 0.70, "Top view of the wing.\nOK for a wing-only study if labeled.", ha="center", fontsize=9)
    ax.add_patch(
        FancyBboxPatch(
            (4.85, 0.95),
            2.15,
            1.50,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            fill=False,
            lw=1.5,
        )
    )
    ax.text(5.92, 2.70, r"vehicle frontal $A$", ha="center", fontsize=11)
    ax.text(5.92, 0.48, "Use this for full-car configs\nall term (this course).", ha="center", fontsize=9)
    ax.set_xlim(0.35, 7.6)
    ax.set_ylim(0.15, 3.15)
    ax.set_title(r"Do not mix $A$ definitions in one $C_D,C_L$ table", fontsize=13, pad=6)
    save(fig, "reference-area-two-defs.png")


def fig_force_anatomy():
    fig, ax = new_fig(8.6, 4.1)
    rows = [
        (3.35, r"$F_D=\frac{1}{2}\,\rho\,v^{2}\,C_D\,A$", "the measured (or predicted) drag force"),
        (2.65, r"$\rho$", r"air density  (kg/m$^3$)  — mass of air per volume"),
        (2.05, r"$v$", r"free-stream speed  (m/s)"),
        (1.45, r"$\frac{1}{2}\rho v^{2}=q$", r"dynamic pressure  (Pa)  — KE per volume of the stream"),
        (0.85, r"$A$", r"agreed reference area  (m$^2$)  — frontal projection here"),
        (0.25, r"$C_D$", r"dimensionless leftover: shape, attitude, Re, ..."),
    ]
    for y, left, right in rows:
        ax.text(0.25, y, left, fontsize=13, ha="left", va="center")
        ax.text(3.55, y, right, fontsize=12, ha="left", va="center")
    ax.set_xlim(0.1, 8.5)
    ax.set_ylim(-0.15, 3.85)
    ax.set_title(r"Anatomy of $F_D=q C_D A$  (same pattern for $F_L$)", fontsize=13, pad=8)
    save(fig, "force-anatomy.png")


def fig_coefficient_definition():
    fig, ax = new_fig(8.2, 3.5)
    ax.text(4.1, 2.55, r"$F_D=q\,C_D\,A$", fontsize=18, ha="center")
    ax.text(4.1, 1.85, r"$F_L=q\,C_L\,A$", fontsize=18, ha="center")
    ax.text(4.1, 1.05, r"$C_D=\dfrac{F_D}{qA}\qquad C_L=\dfrac{F_L}{qA}$", fontsize=16, ha="center")
    ax.text(
        4.1,
        0.25,
        r"$C_D$, $C_L$ package shape, attitude, and (quietly) Reynolds number.",
        fontsize=11,
        ha="center",
    )
    ax.set_xlim(0.2, 8.0)
    ax.set_ylim(-0.1, 3.15)
    ax.set_title(r"Coefficients turn a force into a fair number at given $q$ and $A$", fontsize=13, pad=8)
    save(fig, "coefficient-definition.png")


def fig_derivation_chain():
    fig, ax = new_fig(8.6, 3.6)
    lines = [
        (2.85, r"net aero force from a pressure imbalance:  $F\sim\Delta P\,A$"),
        (2.10, r"scale the imbalance on $q$:  $\Delta P = C\,q$  ( $C$ dimensionless )"),
        (1.35, r"so  $F = C\,q\,A$"),
        (0.55, r"split $F$ into drag and lift:  $F_D=q C_D A$,  $F_L=q C_L A$"),
    ]
    for y, txt in lines:
        ax.text(4.3, y, txt, ha="center", va="center", fontsize=13)
    ax.set_xlim(0.2, 8.4)
    ax.set_ylim(0.05, 3.35)
    ax.set_title(r"From $\Delta P\,A$ to the engineering model $F=qCA$", fontsize=13, pad=8)
    save(fig, "force-derivation-chain.png")


def fig_efficiency():
    fig, ax = plt.subplots(figsize=(7.4, 3.9), dpi=DPI)
    fig.patch.set_facecolor(FACE)
    ax.set_facecolor(FACE)
    configs = ["baseline\n$C_L=-0.30$\n$C_D=0.45$", "new wing\n$C_L=-0.50$\n$C_D=0.55$"]
    e = [0.30 / 0.45, 0.50 / 0.55]
    ax.bar([0, 1], e, color="white", edgecolor="black", lw=1.4, width=0.42)
    for i, val in enumerate(e):
        ax.text(i, val + 0.04, rf"$|C_L|/C_D={val:.2f}$", ha="center", fontsize=11)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(configs, fontsize=10)
    ax.set_ylabel(r"$|C_L|/C_D$")
    ax.set_ylim(0, 1.20)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(r"Same $A$: efficiency rose; $C_D$ also rose (not free)", fontsize=13)
    fig.savefig(OUT / "efficiency-ratio.png", dpi=DPI, bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    fig.savefig(OUT / "efficiency-ratio.svg", bbox_inches="tight", facecolor=FACE, pad_inches=0.15)
    plt.close(fig)
    print("wrote efficiency-ratio.png")


if __name__ == "__main__":
    fig_pressure_definition()
    fig_pressure_difference()
    fig_density()
    fig_ke_to_q()
    fig_q_vs_speed()
    fig_ram_pressure()
    fig_wing_pressure()
    fig_splitter_pressure()
    fig_aero_components()
    fig_reference_area()
    fig_planform_vs_frontal()
    fig_force_anatomy()
    fig_coefficient_definition()
    fig_derivation_chain()
    fig_efficiency()
