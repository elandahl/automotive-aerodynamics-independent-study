# Syllabus — Automotive Aerodynamics Independent Study

**Credits / format:** Independent study (Physics)  
**Prerequisites:** Full introductory algebra-based physics sequence  
**Primary deliverable:** Modular scale vehicle + aero test platform + quantitative report connecting design choices to measured forces

## Learning outcomes

| ID | Outcome |
|----|---------|
| LO1 | Apply Newton’s laws and free-body diagrams to vehicles under aerodynamic load |
| LO2 | Use pressure, density, and dynamic pressure $q=\tfrac12\rho v^2$ correctly |
| LO3 | Predict and measure drag and lift/downforce coefficients for modular parts |
| LO4 | Critique Bernoulli-only explanations; identify separation and wake effects qualitatively |
| LO5 | Compute Reynolds number; discuss dynamic similarity for scale models |
| LO6 | Design controlled experiments with uncertainty estimates and clear documentation |
| LO7 | Iterate CAD designs from data (design ↔ physics feedback loop) |

## Assessment spine

| Item | Weight (suggested) | Notes |
|------|-------------------|--------|
| Weekly physics checkpoints | 30% | Short problems + concept checks in each week folder |
| Lab notebook & raw→cleaned data | 25% | Reproducible runs, labeled configs |
| Midterm design review (Week 5) | 15% | CAD + predicted $C_D,C_L$ ranges + test plan |
| Final report & presentation | 30% | Physics, methods, results, design recommendations |

Checkpoints are meant to be **short and frequent**—enough to prove the physics is landing before the next CAD cycle.

## Ten-week overview

| Week | Theme | Physics emphasis | Design / build emphasis |
|------|--------|------------------|-------------------------|
| [1](week-01-forces-and-goals.md) | Goals, FBDs, force language | Force, Newton 2, normal force ↔ downforce | Scope modular parts; define success metrics |
| [2](week-02-pressure-and-dynamic-pressure.md) | Pressure & air as a fluid | $P$, $\rho$, $q=\tfrac12\rho v^2$ | Sketch pressure regions on spoilers/wings |
| [3](week-03-drag-lift-coefficients.md) | Drag & lift models | $F_D,F_L$, $C_D,C_L$, frontal area | First CAD of body + one wing; estimate areas |
| [4](week-04-bernoulli-and-limits.md) | Bernoulli + honesty | Continuity, Bernoulli, when it fails | Diffuser / splitter stories with caveats |
| [5](week-05-reynolds-scaling.md) | Scale models & Re | Reynolds number, similarity | Freeze model scale; midterm review |
| [6](week-06-test-platform.md) | Sensors & experiment design | Uncertainty, calibration | Build/fixture test platform |
| [7](week-07-wings-and-aoa.md) | Wings & angle of attack | AoA, stall (qualitative) | Swap wing angles; measure |
| [8](week-08-underbody-diffuser.md) | Splitters & diffusers | Ground effect ideas; pressure recovery | Underbody configs |
| [9](week-09-full-configs.md) | Combined configs | Superposition myths; interactions | Full modular matrix of tests |
| [10](week-10-synthesis.md) | Synthesis | Communicate physics to designers | Final report & presentation |

## Physics minor pathway note

This course does **not** replace a calculus-based fluids course. It deliberately:

- Strengthens algebra-based mechanics and introduces **engineering aero formulas** with clear assumptions.
- Adds **dimensional analysis / Re** as a bridge toward PHYS minor upper-level work.
- Optional stretch problems (marked *Stretch*) use ratios and slopes that foreshadow derivatives without requiring multivariable calculus.

Recommended next DePaul courses (mentor-advised): calculus sequence if not complete, then intermediate mechanics and any available fluids / computational physics electives.

## Communication norms

- Push weekly reflection (½ page) + checkpoint answers to the repo or shared notes.
- Label every CAD/export and every data file with: date, airspeed (or fan setting), part ID, AoA, replicates.
- Prefer claims like “$C_L$ increased from … to … at this Re” over “this wing is faster.”
