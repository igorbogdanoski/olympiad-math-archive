---
problem_id: latex_test
title: LaTeX Test Problem
grade: 10
difficulty: 5
tags:
  - test
source: Test
type: algebra
---

## Test Problem

Test mathematical expression: $\left| z^3 + \frac{1}{z^3} \right| \leq 2$

## Solution

This is a test to verify LaTeX rendering works.

## Manim Code

```python
from manim import *

class LaTeXTest(Scene):
    def construct(self):
        title = Text("LaTeX Test", color=BLACK)
        self.play(Write(title))

        eq = MathTex(r"\left| z^3 + \frac{1}{z^3} \right| \leq 2", color=BLACK)
        self.play(Write(eq))

        self.wait(2)