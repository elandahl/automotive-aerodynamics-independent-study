# Interactions and the decision rule

## The 2×2

The smallest package test is four cells at the same $q$, the same frozen $A$, and the same ride height:

| | no diffuser | diffuser |
|--|-------------|----------|
| baseline wing | BASE | DIFF |
| wing at frozen $\alpha$ | WING | BOTH |

Three replicates, then BASE once more. If the closing baseline has moved by more than the spread, the matrix is not one experiment.

A third on/off factor doubles the matrix. Finish the 2×2 first.

## Worked residual

Up-positive vertical force. Checkpoint deltas from baseline:

$$
\Delta F_z^{\mathrm{wing}}=-1.2\,\mathrm{N},\quad
\Delta F_z^{\mathrm{diff}}=-0.8\,\mathrm{N},\quad
\Delta F_z^{\mathrm{both}}=-1.5\,\mathrm{N}
$$

The sum of the solos is $-2.0\,\mathrm{N}$. The residual is

$$
-1.5-(-2.0)=+0.5\,\mathrm{N}
$$

Positive in this sign means **$0.5\,\mathrm{N}$ less downforce** than additivity. Each solo was measured in an inflow the other part will change.

Lecture drag numbers on a baseline $F_z=-0.30\,\mathrm{N}$, $F_D=0.90\,\mathrm{N}$:

| Config | $F_z$ (N) | $F_D$ (N) | $\mathcal{E}$ |
|--------|-----------|-----------|----------------|
| BASE | $-0.30$ | $0.90$ | $0.33$ |
| WING | $-1.50$ | $1.25$ | $1.20$ |
| DIFF | $-1.10$ | $1.05$ | $1.05$ |
| BOTH | $-1.80$ | $1.50$ | $1.20$ |

Drag residual: solos sum to $+0.50\,\mathrm{N}$, the pair is $+0.60\,\mathrm{N}$, so $0.10\,\mathrm{N}$ more drag than additivity.

At $q=135\,\mathrm{Pa}$ and $A=0.015\,\mathrm{m^2}$, $qA=2.03\,\mathrm{N}$, and the $0.50\,\mathrm{N}$ downforce residual is about $0.25$ in $C_L$. That conversion is valid only when every cell used the same $q$ and $A$.

## Noise and fakes

A 5% uncertainty on a $1.5\,\mathrm{N}$ force is about $0.08\,\mathrm{N}$. The $0.50\,\mathrm{N}$ example clears that bar. A residual inside the replicate spread does not. Say “consistent with additivity.”

Systematic errors that imitate an interaction: ride height changed with the package; angle or airspeed changed and raw forces were compared; tare drifted and no closing baseline caught it.

## The rule, then the champion

Write the Week 1 metric before looking at BOTH.

In the lecture table:

- Maximum downforce, drag uncapped: BOTH.  
- Maximum $\mathcal{E}$: WING and BOTH tie at $1.20$. A tie is not a decision.  
- Maximum downforce with $F_D\le 1.30\,\mathrm{N}$: WING. BOTH is over the cap.

The winner is a ranking at model Re (Week 5), not a full-scale specification.

## Course stance

Do not add solo deltas and skip BOTH. Do not name an interaction the noise does not support. Do not choose the metric after the winner is obvious.
