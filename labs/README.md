# Lab & test-platform guide

This guide supports Weeks 6–9. Adapt to available equipment (classroom fan + load cells is enough to learn the physics).

## Goals of the platform

1. Hold a scale vehicle at a known orientation and ride height.  
2. Provide repeatable airflow (even if not a professional wind tunnel).  
3. Measure forces (at least axial drag and vertical load) or deflections calibrated to force.  
4. Swap modular aero parts without changing anything else.

## Suggested instrumentation

| Need | Options |
|------|---------|
| Airspeed | Handheld anemometer; pitot + differential pressure sensor; calibrated fan RPM curve |
| Force | Load cells / multi-axis sensor; calibrated flexure + dial gauge; Arduino/ESP MCU logging optional |
| Angle | Protractor / 3D-printed AoA detents |
| Ride height | Gauge blocks or digital calipers |

## Run protocol (template)

1. Inspect fixtures; clear the intake/exhaust path.  
2. Power sensors; warm up fan if needed.  
3. **Tare** with model installed, flow off.  
4. Set config ID (part labels).  
5. Set speed / fan level; wait for settle.  
6. Record for fixed duration; repeat 3×.  
7. Flow off; verify tare drift.  
8. Change one variable only; repeat.

## Coefficient calculation

\[
q = \tfrac12 \rho v^2, \quad
C_D = \frac{F_D}{q A}, \quad
C_L = \frac{F_L}{q A}
\]

Use the project’s agreed \(A\) and \(\rho\). Include Re using the agreed \(L\).

## Data files

- Template: [data-template.csv](data-template.csv)  
- Put cleaned CSVs in `data/processed/`  
- Keep messy raw logs local or in `data/raw/` (gitignored)

## Lab notebook format

```
## YYYY-MM-DD — Run series title
Goal:
Config IDs:
Speed / fan:
Ambient:
Notes / anomalies:
Results summary:
Next change:
```

## Safety

- Secure all models and wings (failure at speed is a projectile risk).  
- Eye protection; no loose hair/jewelry near fans.  
- GFCI / safe wiring for powered instruments.
