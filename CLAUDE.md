# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

The student-facing companion repo for a university course on Object-Oriented Programming, SOLID,
Design Patterns, and UML in Python (Especialización en Desarrollo de Software, Universidad del
Magdalena — GitHub: `miguepoloc/especializacion_ds`). Content is almost entirely Jupyter
notebooks; there is no application code, build step, or test suite. Each notebook follows a
consistent didactic structure: introduction/objectives, real-world example, practical exercises,
self-assessment, and references.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate        # venv/Scripts/Activate on Windows
pip install -r requirements.txt # graphviz, pydantic
```

Open notebooks with Jupyter or VS Code. `.vscode/settings.json` formats Python on save with
Black and runs flake8 (120-char line length).

## Directory map

- `python_basico/` — Python fundamentals (syntax, data structures, functions, comprehensions,
  type hints/dataclasses/decorators, Pydantic). `utilidades.py` is shared code imported by these
  notebooks.
- `class_uml/` — UML modeling: class/sequence diagrams generated with Graphviz (`.puml` files +
  notebooks rendering them).
- `class_poo/` — the 4 pillars of OOP, one notebook per pillar (`abstraccion`,
  `encapsulamiento`, `herencia`, `polimorfismo`, plus `intro_python`, `definiendo_clases`,
  `interfaz`). `class_poo/ejercicios/` holds fill-in-the-TODO practice versions — these are
  optional practice, never the graded deliverable.
- `solid/` — one notebook per SOLID principle; `solid/ejercicios/` mirrors the same
  practice/deliverable split as `class_poo`.
- `patrones/` — GoF design pattern notebooks, one per pattern, split into
  `patrones_creacionales/`, `patrones_estructurales/`, `patrones_comportamiento/`.
- `refactoring/` — code smells / refactoring notebook (bonus module).
- `docs/actividades/` and `docs/rubricas/` — graded-activity specs and their grading rubrics
  (see "Activities, rubrics, and submissions" below).
- `entregas/` — where students submit work, one subfolder per student.

## Activities, rubrics, and submissions — how the pieces connect

This is the part that isn't obvious from any single file. The course has 4 graded activities
worth 500 points total, and each activity is defined across **three linked locations** that must
stay consistent when edited:

1. **`docs/actividades/actividad_N_<tema>.md`** — the assignment spec: what to build, minimum
   requirements, submission folder layout, and PR title format. (Activity 4, the 350-point
   capstone, is specified inside `docs/rubricas/proyecto.md` instead of its own actividades file.)
2. **`docs/rubricas/<tema>.md`** — the grading rubric: one dimension per requirement in the
   activity spec, 4 performance levels (Excelente/Bueno/Aceptable/Insuficiente) each with a point
   range and a concrete code-level descriptor. Rubrics are written to be pasted into an LLM
   prompt alongside a student's code for an AI-assisted grading pass (see
   `docs/rubricas/README.md` for the exact prompt template) — the AI proposes a score citing
   file:line evidence, the instructor reviews and confirms before publishing it.
3. **`entregas/<nombre_estudiante>/actividad_N_<tema>/`** — where that student's submission for
   the activity lives, submitted as a PR from a branch named
   `entrega/<nombre>-actividadN-<tema>`.

Activity ↔ rubric correspondence is 1:1 by dimension (e.g. `class_poo`'s 4 pillars map to the 4
scored dimensions in `actividad_1_poo.md` and `docs/rubricas/poo.md`). When adding or changing a
graded requirement, update the activity spec and its rubric together — a rubric dimension with no
corresponding requirement (or vice versa) breaks the AI-assisted grading flow.

**Student submission etiquette**: each student works only inside their own
`entregas/<nombre>/` folder — never edit another student's folder, and don't touch course content
outside `entregas/` when preparing a submission.
