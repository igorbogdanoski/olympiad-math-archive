---
difficulty: 5
grade: 10
problem_id: latex_test
source: Test
tags:
- test
title: LaTeX Test Problem
type: algebra
---

## Test Problem

Test mathematical expression: $\left| z^3 + \frac{1}{z^3} \right| \leq 2$

## Solution

This is a test to verify LaTeX rendering works.

#```python
from manim import *

class LaTeXTest(Scene):
    def construct(self):
        title = Text("LaTeX Test", color=BLACK)
        self.play(Write(title))

        eq = MathTex(r"\left| z^3 + \frac{1}{z^3} \right| \leq 2", color=BLACK)
        self.play(Write(eq))

        self.wait(2)

---
### 🎨 Визуелизација
![Илустрација](/assets/images/latex_test/latex_test.png)