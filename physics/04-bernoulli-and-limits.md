# Bernoulli’s equation and its limits

## Continuity (incompressible sketch)

Along a streamline tube, if density is roughly constant:

\[
A_1 v_1 \approx A_2 v_2
\]

Narrower ⇒ faster.

## Bernoulli (idealized)

For steady, inviscid, incompressible flow along a streamline (same height for a quick estimate):

\[
P + \tfrac12 \rho v^2 \approx \text{constant}
\]

So if speed rises, pressure falls **along that streamline**, under those assumptions.

### Worked estimate

Speed increases from 10 to 20 m/s:

\[
\Delta P \approx \tfrac12\rho(v_1^2 - v_2^2) = 0.6\,(100 - 400) = -180\,\mathrm{Pa}
\]

(pressure lower in the faster region in this idealization).

## Where students get misled

1. **“Path length” wing myths:** equal-time path arguments are not a solid foundation for lift. Pressure distributions and turning of the flow (momentum change) are safer mental models.  
2. **Separated flow:** behind a bluff body or stalled wing, flow does not follow the surface; large wakes form; Bernoulli along a tidy surface streamline is the wrong story.  
3. **Viscosity and boundary layers:** real air sticks to surfaces; shear and separation depend on Reynolds number.  
4. **Cars are packages:** front splitter, underbody, wheels, and wing interact; local Bernoulli slogans do not predict the system.

## Diffusers (honest cartoon)

A diffuser increases area so underbody flow can decelerate and **recover pressure** toward the rear. The performance still depends on sealing, ride height, vortices, and separation—empiricism + coefficients beat slogans.

## Course stance

Use Bernoulli to build intuition for **attached** accelerating/decelerating streams. Always ask: *Is the flow attached? Is this along a streamline? Are we ignoring the wake?* Then measure \(C_L\) and \(C_D\).
