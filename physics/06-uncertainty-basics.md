# Uncertainty basics for aero coefficients

## Goal

When you report \(C_D = F_D/(qA)\), you should know whether a change is real or noise.

## Dominant-error thinking (algebra-friendly)

If \(q = \tfrac12\rho v^2\) and \(v\) is uncertain, small speed errors become larger coefficient errors because of the square.

Approximate relative uncertainty (when \(v\) dominates):

\[
\frac{\delta q}{q} \approx 2\frac{\delta v}{v}
\]

Then, schematically,

\[
\frac{\delta C_D}{C_D} \sim \sqrt{ \left(\frac{\delta F_D}{F_D}\right)^2 + \left(\frac{\delta q}{q}\right)^2 + \left(\frac{\delta A}{A}\right)^2 }
\]

(assuming independent contributions; this is a standard lab approximation).

### Example

- \(\delta F_D / F_D = 5\%\)  
- \(\delta v / v = 5\%\) ⇒ \(\delta q/q \approx 10\%\)  
- \(\delta A/A = 2\%\)  

Rough combined relative uncertainty \(\sim \sqrt{5^2+10^2+2^2}\%\approx 11\%\).  
So a 3% change in \(C_D\) between configs is probably **not** meaningful; a 25% change might be.

## Practical rules

1. Calibrate force sensors with known weights.  
2. Measure or carefully estimate \(v\) (anemometer, pitot, or calibrated fan curve).  
3. Take ≥3 replicates; report mean and spread (e.g., standard deviation).  
4. Keep alignment and ride height fixed when claiming a part-only effect.  
5. Record temperature if comparing days (density drift).

## Lab notebook minimum

Date, config ID, fan setting / \(v\), ambient notes, raw forces, tares, replicates, anything that went wrong.
