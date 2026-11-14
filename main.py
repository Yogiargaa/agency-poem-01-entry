import os

# agency-poem-01 entry (Python 3.13, standard library only): writes one fixed
# poem about agency to /output/entry.txt. The judge reads exactly the bytes
# written, line ends included, so the poem is joined with "\n" and no trailing
# line end is added. Outside the grader's container, MAKEFUN_OUTPUT_DIR stands
# in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM_LINES = [
    "Every morning I walked him to the curb",
    "and held his hand across the street.",
    "Each week I let go a little sooner:",
    "halfway, then at the white line, then not at all.",
    "",
    "By autumn he crossed alone.",
    "I stood at the curb, my hand",
    "still shaped around his \u2014",
    "the hand that let go",
    "was the hand that did the work.",
]

POEM = "\n".join(POEM_LINES)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(POEM)
