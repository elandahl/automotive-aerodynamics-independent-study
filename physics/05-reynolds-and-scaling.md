# Reynolds number and scale-model honesty

## Definition

\[
\mathrm{Re} = \frac{\rho v L}{\mu} = \frac{v L}{\nu}
\]

- \(L\): characteristic length (car length, wing chord, …)—**define it**.  
- \(\nu = \mu/\rho\): kinematic viscosity. For air near room temperature, \(\nu \sim 1.5\times 10^{-5}\,\mathrm{m^2/s}\) is a usable start.

Re compares **inertial** effects to **viscous** effects. Large Re: inertia dominates; wakes and turbulence are common. Small Re: viscosity matters more; flow may look “stickier.”

## Why scale models lie a little (sometimes a lot)

A 1:10 model at half the road speed has far smaller \(vL\), hence much smaller Re than the full car. Boundary layers and separation points can differ, so \(C_D\) and \(C_L\) need not match full scale.

### Example numbers

| Case | \(L\) | \(v\) | \(\mathrm{Re}\approx vL/\nu\) |
|------|-------|-------|-------------------------------|
| Full car | 4.5 m | 30 m/s | \(\sim 9\times 10^6\) |
| 1:10 model | 0.45 m | 15 m/s | \(\sim 4.5\times 10^5\) |

Same air, much smaller Re. Matching Re in air would require huge model speeds (often impractical). Water tunnels or pressurized tunnels exist in research labs—not assumed here.

## What you may still conclude

- **Ranking** of configs at fixed model Re (which wing AoA made more downforce *here*).  
- Qualitative lessons: stall onset, diffuser sensitivity to ride height, drag penalties.  
- Process skills: FBDs, coefficients, uncertainty, documentation.

## What to avoid claiming

- “Our model \(C_D=0.42\) means the full car is 0.42.”  
- Absolute top-speed predictions for a real vehicle from uncorrected small-Re data.

Put a short **scaling disclaimer** in every major report section that quotes coefficients.
