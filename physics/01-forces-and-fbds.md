# Forces and free-body diagrams for vehicles

## From intro physics

Newton’s second law: $\sum \mathbf{F} = m\mathbf{a}$.  
At constant velocity, $\sum \mathbf{F} = 0$ in each direction you care about.

## Vertical balance (level road, constant speed)

Without aero:

$$
N_{\text{total}} - mg = 0 \quad \Rightarrow \quad N_{\text{total}} = mg
$$

With downward aero force $D_w$ (downforce):

$$
N_{\text{total}} - mg - D_w = 0 \quad \Rightarrow \quad N_{\text{total}} = mg + D_w
$$

Tire friction available for cornering/braking scales with normal force (approximate Coulomb picture: $f_{\max} \sim \mu N$). Downforce can raise $N$ **without** changing mass $m$.

## Horizontal balance (constant speed)

Drag $F_D$ is opposed by drive force from the tires (powered axle) in steady cruise:

$$
F_{\text{drive}} - F_D = 0
$$

More drag ⇒ more power needed to hold the same speed.

## Design translation

| Design claim | Physics translation |
|--------------|---------------------|
| “More grip” | Larger $N$ and/or better tire $\mu$, enabling larger horizontal tire forces |
| “More stable at speed” | Often: beneficial aero moments / load distribution (advanced); start with net $F_D$ and net $D_w$ |
| “More efficient aero” | Often: high $|F_L|/F_D$ or meeting a downforce target with less drag |

## Checkpoint-style example

A 12.0 kg scale model (weights + ballast) at rest has $N = mg \approx 118\,\mathrm{N}$.  
If aero downforce is $2.5\,\mathrm{N}$ at test speed, normal force becomes $\approx 120.5\,\mathrm{N}$ — a small fractional change. That is why **sensitive force sensing** and **light models or dedicated load cells for aero force** matter on small platforms: aero loads may be only a few percent of weight (or you mount the model so the sensor sees aero force more directly).
