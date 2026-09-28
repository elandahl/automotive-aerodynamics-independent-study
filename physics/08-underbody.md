# Splitters, diffusers, and ride height

## The path, not one station

An attached diffuser slows the underbody stream as the area grows, so pressure **rises** toward the exit (Week 4 recovery). Downforce still comes from **low** pressure, because that low pressure is at the throat ahead of the ramp, not inside the recovery.

Stations, front to back:

1. Inlet under the nose, height set in part by the splitter.  
2. Throat under the flat floor: smaller area, higher speed, lower $P$, if this air feeds a larger exit and stays attached.  
3. Diffuser ramp: area up, speed down, $P$ recovers toward the exit.

Low $P$ and rising $P$ are two stations. A separated ramp is a wake, and the recovery number is then unearned.

## Worked estimate

Width $b=0.12\,\mathrm{m}$, throat $h_1=15\,\mathrm{mm}$, exit $h_2=30\,\mathrm{mm}$.

$$
A_1 = 0.0018\,\mathrm{m^2}, \qquad A_2 = 0.0036\,\mathrm{m^2}
$$

Choose an exit speed of $10\,\mathrm{m/s}$ (a teaching assumption, not a measurement). Then $v_1=20\,\mathrm{m/s}$ and

$$
P_1 - P_2 = \tfrac12\rho(v_2^2 - v_1^2) = 0.6(100-400) = -180\,\mathrm{Pa}
$$

The floor is $180\,\mathrm{Pa}$ below the exit. Assumptions: attached channel, no side leakage, exit speed held fixed, incompressible continuity.

Raise the throat to $20\,\mathrm{mm}$ and keep the exit at $30\,\mathrm{mm}$: $v_1'=15\,\mathrm{m/s}$ and $P_1'-P_2=-75\,\mathrm{Pa}$. Five millimeters removed more than half the suction estimate, because $A=bh$.

$180\,\mathrm{Pa}$ on $0.010\,\mathrm{m^2}$ is $1.8\,\mathrm{N}$. That shows why a real $\Delta P$ can reach the sensor. It is not a predicted $C_L$.

## Splitter

Two separate hypotheses:

- The lip sets inlet height $h$.  
- Stagnation on the upper face of the lip is a high-$P$ patch that pushes down on the splitter itself.

Neither replaces the throat-and-recovery path. Test splitter on and off at fixed ride height and fixed wing angle.

## Ride height and a block-off

Clearance matters three ways: area $A\propto h$; too much gap and the road is not a channel wall; too little gap or too steep a ramp and the diffuser separates.

“Ground effect” in this course means that proximity is what makes the underbody a channel. There is no extra multiplier to memorize. Measure two or three values of $h$.

A block-off plate closes the inlet with everything else fixed. If downforce drops, the open channel was doing work. If it does not, the signal was elsewhere.

## What to report

At one fan setting, report $C_L$, $C_D$, and $\mathcal{E}=|C_L|/C_D$. Photograph $h$. Keep the Week 7 wing angle fixed. BOTH is a measured cell, not the sum of the solos (Week 9).

## Course stance

Say where the low pressure is (the floor) and where the pressure rises (the ramp, if attached). Do not conclude “the diffuser lowers the pressure” without naming the station.
