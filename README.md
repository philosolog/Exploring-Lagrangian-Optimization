# Exploring Lagrangian Optimization

This repository contains the final project I completed for a high school multivariable calculus course. The goal was to study constrained optimization through self-directed research, produce a written report, and present the material to the class.

The paper is not intended for formal journal publication, it instead documents our learning and presentation materials.

## Project focus:
- Topic: constrained optimization using Lagrange multipliers
- Approach: derive the theory, work through worked examples, compare methods
- Examples included: Cobb-Douglas optimization (economics), a constrained physics problem, and classroom-friendly demonstrations

## Contents and artifacts
- **Paper:** LaTeX source in `paper/` and compiled PDF at `paper/wrapper.pdf`.
- **Presentation:** slides and web presentation in `presentation/` (HTML + source). The slide sources live in `presentation/` and `presentation/template.html` is the template.
- **References and notes:** `paper/references/` and `paper/sections/` contain supporting material and section files.

## Build & usage notes
- Build the paper (requires a TeX distribution such as TeX Live or MiKTeX):
```sh
latexmk -pdf paper/wrapper.tex
```
or run `pdflatex` / `bibtex` as needed until references compile.
- Serve or build the slides (from [manim-slides](https://manim-slides.eertmans.be/latest/quickstart.html)):
```sh
manim-slides convert Introduction Lagrange_Multipliers Key_Differences Cobb_Douglas_Introduction Cobb_Douglas_Problem Physics_Problem main.html --use-template template.html
```
