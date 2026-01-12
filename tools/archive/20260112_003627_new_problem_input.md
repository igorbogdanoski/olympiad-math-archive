---
problem_id: test_math_display
title: Test Math Display
grade: 11
difficulty: 1
tags:
  - test
source: Test
type: algebra
---

# Текст на задачата
Реши ја равенката: $x^2 + 2x + 1 = 0$

# Решение
## Чекор по чекор

**Чекор 1: Формула за квадратен трином**
$$ x^2 + 2x + 1 = (x + 1)^2 $$

**Чекор 2: Решавање**
$$ (x + 1)^2 = 0 \implies x + 1 = 0 \implies x = -1 $$

# Pedagogical Notes
Test math display.

# Manim Code
```python
from manim import *

class TestMath(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Title
        title = Text("Test Math", color=BLACK).to_edge(UP)
        self.play(Write(title))

        # Equation
        eq = MathTex(r"x^2 + 2x + 1 = 0", color=BLACK).shift(UP)
        self.play(Write(eq))

        # Solution
        sol = MathTex(r"(x + 1)^2 = 0 \implies x = -1", color=BLACK).next_to(eq, DOWN)
        self.play(Write(sol))

        self.wait(2)