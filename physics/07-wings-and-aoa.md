# Wings, angle of attack, and stall

## Geometric angle

Geometric angle of attack $\alpha$ is the angle between the wing **chord** (leading edge to trailing edge) and the free stream.

$$
\alpha = 0
$$

when the chord is parallel to the free stream. On the inverted modular wing, increasing $\alpha$ drops the leading edge so the wing turns air upward. The reaction is downforce.

If a drawing uses the body reference line instead of the free stream, that choice is written once and kept for every run.

Course sign: $C_L$ is up-positive. Downforce is $C_L<0$. The suction side of this inverted wing is the **lower** surface.

## What the curves do

While the flow stays attached, $|C_L|$ rises with $\alpha$, and drag rises with it. A sketch of that drag, before stall, is

$$
C_D \approx C_{D0} + k C_L^2
$$

Stall is separation on the suction side. Then $|C_L|$ peaks and falls (or stops rising) and $C_D$ jumps. The extra drag is the wake, not the $C_L^2$ term.

A thin two-dimensional idealization is about $0.1$ in $C_L$ per degree. A finite wing at model Re on a body is less steep. The sweep is the measurement.

### Illustrative table (not a measured wing)

| $\alpha$ | $C_L$ | $C_D$ | $\mathcal{E}=\|C_L\|/C_D$ |
|----------|-------|-------|---------------------------|
| $0^\circ$ | $-0.12$ | $0.38$ | $0.32$ |
| $5^\circ$ | $-0.32$ | $0.44$ | $0.73$ |
| $10^\circ$ | $-0.52$ | $0.52$ | $1.00$ |
| $15^\circ$ | $-0.58$ | $0.62$ | $0.94$ |
| $20^\circ$ | $-0.36$ | $0.95$ | $0.38$ |

$|C_L|$ peaks at $15^\circ$. Efficiency peaks at $10^\circ$. At $20^\circ$ the sketch has stalled.

Check of the attached drag sketch at $10^\circ$, with $C_{D0}=0.38$ and $k=0.5$:

$$
0.38 + 0.5(0.52)^2 = 0.52
$$

At $20^\circ$ the same formula gives about $0.44$, but the table has $C_D=0.95$.

With $q=135\,\mathrm{Pa}$ and $A=0.015\,\mathrm{m^2}$, the $15^\circ$ row is $F_L=-1.17\,\mathrm{N}$ and $F_D=1.26\,\mathrm{N}$.

## Efficiency when both forces rise

If downforce rises 40% and drag rises 80%,

$$
\frac{\mathcal{E}_2}{\mathcal{E}_1} = \frac{1.40}{1.80} = 0.78
$$

Efficiency falls to about 78% of its old value. Example: $|F_L|$ from $1.00\,\mathrm{N}$ to $1.40\,\mathrm{N}$, $F_D$ from $0.80\,\mathrm{N}$ to $1.44\,\mathrm{N}$, $\mathcal{E}$ from $1.25$ to $0.97$.

An airliner in cruise wants high lift-to-drag, far from stall. A race wing is often run near peak $|C_L|$ because the job is normal force. Past stall, downforce falls and drag jumps.

## How to run the sweep

One fan setting, so $q$ is common. Detents $0^\circ,5^\circ,10^\circ,15^\circ$ (and $20^\circ$ if you want past the peak). At least three replicates. Plot means and the spread. Call stall only when the change is larger than that spread.

Low model Re can move the peak to a smaller $\alpha$ than a full-scale expectation. That is a Week 5 result, not a bad print.

## Course stance

Record $\alpha=0$ on the part. Keep $C_L$ negative for downforce. Treat peak $|C_L|$ and peak $\mathcal{E}$ as different angles until the data say otherwise. Do not describe stall as separation on the upper surface of an upright airplane wing.
