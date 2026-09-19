# Week 3 — Drag, lift, and force coefficients

**Lecture slides:** [slides/week-03-lecture.md](slides/week-03-lecture.md) · [PDF](slides/week-03-lecture.pdf)

## Learning targets

- Derive $F=qCA$ from $F\sim\Delta P A$, and write the drag and lift models with a clearly defined reference area $A$:

$$
F_D = \tfrac12 \rho v^2 C_D A, \qquad
F_L = \tfrac12 \rho v^2 C_L A
$$

- Treat **downforce as negative lift** (or define $F_{\text{down}} = -F_L$ and stick to one convention).
- Estimate order-of-magnitude forces for the scale model.

## Physics checkpoint

1. A model has $A = 0.015\,\mathrm{m^2}$, $v = 15\,\mathrm{m/s}$, $\rho = 1.2\,\mathrm{kg/m^3}$, $C_D = 0.45$. Find $F_D$.  
2. Same conditions with $C_L = -0.30$ (downforce). Find the vertical aero force and state direction.  
3. If you change only the wing and $C_L$ becomes $-0.50$ while $C_D$ rises to $0.55$, compute the **downforce-to-drag** ratio $|F_L|/F_D$ before and after. Which config is “more efficient” by that metric?  
4. *Stretch:* Show that $C_D = F_D / (q A)$ with $q=\tfrac12\rho v^2$. Why do engineers like dimensionless coefficients?

## Design / build tasks

- Measure/estimate frontal area of the body and plan a **consistent** $A$ definition for all configs.
- CAD v1 of body + at least one interchangeable wing; record geometric AoA.

## Deliverables

- [ ] Checkpoint solutions  
- [ ] Written definition of reference area $A$ for this project  
- [ ] CAD screenshots + part IDs

## Mentor notes

Insist on one reference-area convention for the whole term so coefficients are comparable across weeks.
