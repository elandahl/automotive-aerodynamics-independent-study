# Lecture slides

Marp Markdown decks for weekly lectures. They render as readable Markdown on GitHub; present locally with the [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) extension, or export:

```bash
npx @marp-team/marp-cli curriculum/slides/week-01-lecture.md -o curriculum/slides/week-01-lecture.pdf
npx @marp-team/marp-cli curriculum/slides/week-02-lecture.md -o curriculum/slides/week-02-lecture.pdf --allow-local-files
npx @marp-team/marp-cli curriculum/slides/week-03-lecture.md -o curriculum/slides/week-03-lecture.pdf --allow-local-files
```

| Week | Deck | PDF | Figures |
|------|------|-----|---------|
| 1 | [Forces, FBDs, and project goals](week-01-lecture.md) | [week-01-lecture.pdf](week-01-lecture.pdf) | [figures/](figures/) |
| 2 | [Pressure, density, $q$](week-02-lecture.md) | [week-02-lecture.pdf](week-02-lecture.pdf) | [figures/](figures/) |
| 3 | [Drag, lift, coefficients](week-03-lecture.md) | [week-03-lecture.pdf](week-03-lecture.pdf) | [figures/](figures/) |

Equations use `$...$` / `$$...$$` for GitHub and Marp MathJax.
