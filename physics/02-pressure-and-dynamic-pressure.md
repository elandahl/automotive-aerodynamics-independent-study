# Pressure, density, and dynamic pressure

## Pressure

Pressure \(P\) is force per area: \(P = F/A\), unit pascal \(\mathrm{Pa} = \mathrm{N/m^2}\).

Fluids push on surfaces; **net** force comes from **pressure differences** (and shear from viscosity). Absolute atmospheric pressure is large (~101 kPa), but opposite sides of a thin plate often see nearly the same ambient contribution—your aero force is about the imbalance.

## Density

Air density near room conditions is often approximated as

\[
\rho \approx 1.2\,\mathrm{kg/m^3}
\]

Better: measure temperature and use a standard atmosphere table, or weigh/calculate if you have lab support. Humidity and altitude matter for careful work.

## Dynamic pressure

Define

\[
q \equiv \tfrac12 \rho v^2
\]

Unit: pascals (same as pressure). Interpretation: characteristic scale of inertial “ram” pressure in the flow.

**Why \(v^2\)?** Doubling speed roughly **quadruples** \(q\), so aero forces explode with speed—central to both racecar design and to choosing a safe, measurable model test speed.

### Example

\(v = 20\,\mathrm{m/s}\), \(\rho = 1.2\,\mathrm{kg/m^3}\):

\[
q = 0.5 \times 1.2 \times 400 = 240\,\mathrm{Pa}
\]

If an effective \(\Delta P\) of order \(q\) acts on \(A = 0.02\,\mathrm{m^2}\),

\[
F \sim q A = 4.8\,\mathrm{N}
\]

Coefficients \(C_D,C_L\) refine this order-of-magnitude estimate.
