# Drag and lift coefficients

## Definitions

With free-stream speed $v$, density $\rho$, and a chosen reference area $A$:

$$
F_D = q\, C_D\, A, \qquad F_L = q\, C_L\, A, \qquad q=\tfrac12\rho v^2
$$

Equivalently,

$$
C_D = \frac{F_D}{q A}, \qquad C_L = \frac{F_L}{q A}
$$

- **Drag** $F_D$: force component parallel to free stream (resists motion).  
- **Lift** $F_L$: force component perpendicular to free stream (aircraft: up). For cars, useful lift is often **negative** (into the road).

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
