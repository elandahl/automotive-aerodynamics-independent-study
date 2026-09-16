# Automotive Aerodynamics Independent Study

Independent study linking **industrial design** and **physics**: modular car aero parts (spoilers, wings, splitters, diffusers), scale-model testing, and the fluid-force models needed to interpret the data.

**Instructor:** Physics faculty mentor  
**Student path:** Algebra-based intro physics completed; Physics minor (DePaul) in progress  
**Length:** 10 weeks

## Start here

| Document | Purpose |
|----------|---------|
| [Project proposal](docs/proposal.md) | Student’s original plan (web-readable) |
| [Syllabus & outcomes](curriculum/SYLLABUS.md) | Weekly learning goals, physics checkpoints, deliverables |
| [Week 1 lecture slides](curriculum/slides/week-01-lecture.md) | Detailed Marp deck for forces, FBDs, metrics |
| [Physics concept notes](physics/README.md) | Algebra-friendly notes bridging intro physics → aero |
| [Lab & test-platform guide](labs/README.md) | How to measure, log, and analyze forces |
| [Reading & references](resources/reading-list.md) | Curated sources (design + physics) |
| [Mentor guide](docs/mentor-guide.md) | Faculty checklist and misconception watchlist |
| [Coefficient helper](tools/compute_coefficients.py) | CSV → $q$, Re, $C_D$, $C_L$ |

## What success looks like

By the end of the term the student should be able to:

- Draw free-body diagrams for a vehicle under aero loads and relate them to tire normal force / “grip.”
- Use $F_D = \tfrac12\rho v^2 C_D A$ and $F_L = \tfrac12\rho v^2 C_L A$ with correct signs (downforce as negative lift).
- Explain Bernoulli’s equation **and** when it is misleading for bluff-body car flow.
- Estimate Reynolds number for full-scale vs. model-scale tests and state what can / cannot be claimed.
- Run a controlled modular-part experiment, report uncertainties, and redesign a part based on data.

## Repository layout

```
curriculum/     Week-by-week plan and checkpoints
physics/        Concept notes and worked examples
labs/           Test platform, sensors, data templates
docs/           Proposal and course admin notes
resources/      Readings and design case studies
data/           Place for cleaned measurement CSVs (optional)
cad/            Notes / exports from CAD (optional)
```

## How to use this repo (student)

1. Read the [proposal](docs/proposal.md) and [syllabus](curriculum/SYLLABUS.md).
2. Each week: complete the physics checkpoint **before** heavy CAD iteration when possible.
3. Log experiments with the [data template](labs/data-template.csv) and the lab notebook format in [labs/README.md](labs/README.md).
4. Push notes, cleaned data, photos of setups, and short weekly reflections here so mentor feedback can be timely.

## How to use this repo (mentor)

- Weekly checkpoints in the syllabus are the assessment spine.
- Concept notes in `physics/` are pitched at algebra-based physics with optional calculus callouts for minor-track stretch.
- Emphasize **scaling honesty** early (Week 3–4) so model tests do not overclaim full-car performance.

## Math on GitHub

Equations use GitHub’s native MathJax syntax so they render on github.com:

- Inline: `$F_D = q C_D A$`
- Display: `$$` … `$$` on their own lines

Prefer `$...$` / `$$...$$` over `\(...\)` / `\[...\]` when editing.
