# Week 6 — Test platform, sensors, calibration, uncertainty

## Learning targets

- Distinguish **resolution**, **accuracy**, and **repeatability**.
- Propagate uncertainty for \(C_D = F_D/(qA)\) at an algebra level (dominant-error thinking).
- Write a repeatable run protocol (warm-up, zeroing, replicates).

## Physics / methods checkpoint

1. If force is measured to \(\pm 0.05\,\mathrm{N}\) and typical \(F_D\sim 1.0\,\mathrm{N}\), what is the relative uncertainty in \(F_D\)?  
2. Speed uncertainty of \(\pm 5\%\) implies about what percent uncertainty in \(q\) (and thus in coefficients), holding other quantities fixed? Hint: \(q\propto v^2\).  
3. Why take ≥3 replicates per configuration?

## Design / build tasks

- Finish mechanical fixture: model alignment, wing AoA stops, safe fan mounting.
- Calibrate force sensors (known masses / hanging weights) and document the curve.
- Measure or estimate airspeed vs. fan setting.

## Deliverables

- [ ] Protocol one-pager (also paste into [labs/README.md](../labs/README.md) checklist)  
- [ ] Calibration table/plot  
- [ ] First “tare + empty tunnel/fan” noise floor measurement

## Safety

Eye protection around fans; secure fixtures; no loose clothing/hair near intake; electrical safety for instrument power.
