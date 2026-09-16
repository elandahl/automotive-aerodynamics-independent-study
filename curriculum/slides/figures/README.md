# Week 1 lecture figures

Original teaching diagrams for the Week 1 deck (physics-textbook line drawings).

Regenerate:

```bash
python3 curriculum/slides/figures/make_figures.py
```

**FBD convention (particle model):** every force is drawn from the center of mass (circled cross). Arrow length is qualitative; equal magnitudes are drawn equal. Airflow is omitted on FBDs because it is not a force.

| File | Used on |
|------|---------|
| [fbd-rest](fbd-rest.png) | Car at rest: $\|N\|=\|mg\|$ |
| [fbd-cruise](fbd-cruise.png) | Cruise: $N=mg+D_w$, $F_{\mathrm{drive}}=F_D$ |
| [not-lighter](not-lighter.png) | Downforce is not “lighter” |
| [friction-budget](friction-budget.png) | $f_{\max}\sim\mu N$ |
| [modular-parts](modular-parts.png) | Splitter, wing, spoiler, diffuser |
| [test-platform](test-platform.png) | Fan / fixture / sensors (concept) |

| File | Used on |
|------|---------|
| [fbd-rest.svg](fbd-rest.svg) | Car at rest |
| [fbd-cruise.svg](fbd-cruise.svg) | Steady cruise with aero |
| [not-lighter.svg](not-lighter.svg) | Downforce ≠ lighter |
| [friction-budget.svg](friction-budget.svg) | $f_{\max}\sim\mu N$ |
| [modular-parts.svg](modular-parts.svg) | Splitter, wing, spoiler, diffuser |
| [test-platform.svg](test-platform.svg) | Fan / fixture / sensors (concept) |
