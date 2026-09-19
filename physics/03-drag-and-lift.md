# Drag and lift coefficients

## From a pressure imbalance to a coefficient

Week 2: the net aero force on a part is about a pressure difference acting on an area,

$$
F \sim \Delta P\, A
$$

Scale that difference on the stream’s kinetic-energy density $q=\tfrac12\rho v^2$:

$$
\Delta P = C\, q
$$

$C$ is dimensionless (a number of pascals of $\Delta P$ per pascal of $q$). Then

$$
F = C\, q\, A
$$

Split $F$ into the two Week 1 components relative to the free stream.

## Definitions

With free-stream speed $v$, density $\rho$ (mass per volume, $\mathrm{kg/m^3}$), and a chosen reference area $A$:

$$
F_D = q\, C_D\, A, \qquad F_L = q\, C_L\, A, \qquad q=\tfrac12\rho v^2
$$

Equivalently,

$$
C_D = \frac{F_D}{q A}, \qquad C_L = \frac{F_L}{q A}
$$

- **Drag** $F_D$: force component parallel to free stream (resists motion; aft on the car).  
- **Lift** $F_L$: force component perpendicular to free stream (aircraft: up). For cars, useful lift is often **negative** (into the road). Downforce $D_w=-F_L$ when $F_L$ is up-positive.

## What each symbol is

| Symbol | Meaning | SI unit |
|--------|---------|---------|
| $\rho$ | mass of air per volume | $\mathrm{kg/m^3}$ |
| $v$ | free-stream speed | $\mathrm{m/s}$ |
| $q=\tfrac12\rho v^2$ | kinetic energy per volume of the stream | $\mathrm{Pa}$ |
| $A$ | agreed reference area | $\mathrm{m^2}$ |
| $C_D$, $C_L$ | leftover factors (shape, attitude, Re, …) | dimensionless |
| $F_D$, $F_L$ | drag and lift forces | $\mathrm{N}$ |

$C_D$ and $C_L$ do **not** hide an extra $v^2$ — that already sits in $q$. If you change only speed and the flow pattern stays similar, the coefficients are roughly constant and the forces scale as $v^2$.

## Reference area $A$

Common choices:

- Vehicle **frontal area** (projected) — good for whole-car $C_D$.  
- Wing **planform area** — good when studying the wing alone.

**Rule for this independent study:** pick one primary $A$ for comparing full-vehicle configs and document it. If you also report wing-only coefficients, say which $A$ you used.

## Order-of-magnitude table (illustrative)

| Object | Typical $C_D$ (ballpark) |
|--------|----------------------------|
| Flat plate facing flow | ~1–2 |
| Streamlined airfoil (section drag) | much smaller; depends on Re |
| Road cars (full vehicle) | often ~0.25–0.35 (modern), higher for boxy shapes |

Your **scale bluff model** may sit higher in $C_D$ than a production car. Relative changes between modular parts still teach design physics.

## Efficiency metric

Downforce-to-drag ratio:

$$
\mathcal{E} = \frac{|F_L|}{F_D} = \frac{|C_L|}{C_D}
$$

(when using the same $A$). Not the only goal—sometimes absolute downforce matters more—but it is a clean starting metric.
