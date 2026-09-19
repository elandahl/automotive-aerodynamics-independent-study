# Pressure, density, and dynamic pressure

## Pressure

Pressure $P$ is force per area: $P = F/A$, unit pascal $\mathrm{Pa} = \mathrm{N/m^2}$.

Fluids push on surfaces; **net** force comes from **pressure differences** (and shear from viscosity). Absolute atmospheric pressure is large (~101 kPa), but opposite sides of a thin plate often see nearly the same ambient contribution—your aero force is about the imbalance.

## Density $\rho$

Density is **mass per volume**:

$$
\rho \equiv \frac{m}{V}
$$

**Meaning:** how much air (or any material) is packed into a region of space. It is not “thickness,” “heaviness of the car,” or a second name for pressure.

**SI unit:** $\mathrm{kg/m^3}$. A cubic meter of room air has a mass of order one kilogram.

Near room conditions a working value is

$$
\rho \approx 1.2\,\mathrm{kg/m^3}
$$

Better: measure temperature and use a standard atmosphere table, or weigh/calculate if you have lab support. Humidity and altitude matter for careful work. For early calculations in this course, freeze $\rho=1.2\,\mathrm{kg/m^3}$ and note weather if it changes.

Denser air means more mass in the same volume, so the same speed $v$ stores more kinetic energy.

## From kinetic energy to dynamic pressure

Intro physics: a mass $m$ moving at speed $v$ has kinetic energy

$$
KE = \tfrac12 m v^2
$$

Take a **blob** of air with that mass and with volume $V$. Divide by $V$:

$$
\frac{KE}{V} = \tfrac12 \left(\frac{m}{V}\right) v^2 = \tfrac12 \rho v^2
$$

That energy density *is* dynamic pressure. Define

$$
q \equiv \tfrac12 \rho v^2
$$

**Units:** $\mathrm{J/m^3} = \mathrm{N\cdot m/m^3} = \mathrm{N/m^2} = \mathrm{Pa}$. Same unit as pressure, which is why $q$ can sit next to $\Delta P$.

Interpretation: characteristic scale of inertial “ram” pressure in the free stream — the kinetic energy packed into each cubic meter of oncoming air.

**Why $v^2$?** It was already in $KE$. Doubling speed **quadruples** $q$, so aero forces explode with speed—central to both racecar design and to choosing a safe, measurable model test speed.

**Why $\rho$?** It converts “a particle of mass $m$” into “a fluid that fills volume $V$.”

### Example

$v = 20\,\mathrm{m/s}$, $\rho = 1.2\,\mathrm{kg/m^3}$:

$$
q = 0.5 \times 1.2 \times 400 = 240\,\mathrm{Pa}
$$

If an effective $\Delta P$ of order $q$ acts on $A = 0.02\,\mathrm{m^2}$,

$$
F \sim q A = 4.8\,\mathrm{N}
$$

Coefficients $C_D,C_L$ (Week 3) refine this order-of-magnitude estimate.
