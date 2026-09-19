# Lecture figures

Physics-textbook line drawings for weekly decks.

Regenerate:

```bash
python3 curriculum/slides/figures/make_figures.py
python3 curriculum/slides/figures/make_figures_w23.py
```

**FBD convention (particle model):** every force is drawn from the center of mass (circled cross). Arrow length is qualitative; equal magnitudes are drawn equal. Airflow is omitted on FBDs because it is not a force.

**Flow sketches (not FBDs):** streamlines go *around* solids; they do not wrap through a wing or body. Labels sit in empty space, not on arrows or curves.

## Week 1

| File | Used on |
|------|---------|
| [fbd-rest](fbd-rest.png) | Car at rest: $\|N\|=\|mg\|$ |
| [fbd-cruise](fbd-cruise.png) | Cruise: $N=mg+D_w$, $F_{\mathrm{drive}}=F_D$ |
| [not-lighter](not-lighter.png) | Downforce is not “lighter” |
| [friction-budget](friction-budget.png) | $f_{\max}\sim\mu N$ |
| [modular-parts](modular-parts.png) | Splitter, wing, spoiler, diffuser |
| [test-platform](test-platform.png) | Fan / fixture / sensors (concept) |

## Weeks 2–3

| File | Used on |
|------|---------|
| [pressure-definition](pressure-definition.png) | $P=F/A$ |
| [pressure-difference](pressure-difference.png) | Net force from $\Delta P$ |
| [density-definition](density-definition.png) | $\rho=m/V$, unit $\mathrm{kg/m^3}$ |
| [ke-to-q](ke-to-q.png) | $KE/V=\tfrac12\rho v^2=q$ |
| [dynamic-pressure-scale](dynamic-pressure-scale.png) | Meaning of $q$ |
| [q-vs-speed](q-vs-speed.png) | $q\propto v^2$ |
| [wing-pressure-map](wing-pressure-map.png) | Inverted wing $+/-$ sketch |
| [splitter-pressure-map](splitter-pressure-map.png) | Splitter hypothesis |
| [aero-force-components](aero-force-components.png) | $F_D$, $F_L$ from CM |
| [force-derivation-chain](force-derivation-chain.png) | $\Delta P A\to qCA$ |
| [force-anatomy](force-anatomy.png) | Each factor in $F_D=q C_D A$ |
| [coefficient-definition](coefficient-definition.png) | $F=qCA$ |
| [reference-area-frontal](reference-area-frontal.png) | Frontal $A$ |
| [reference-area-two-defs](reference-area-two-defs.png) | Planform vs frontal |
| [efficiency-ratio](efficiency-ratio.png) | Checkpoint 3 metric |
