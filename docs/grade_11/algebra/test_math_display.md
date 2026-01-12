---
difficulty: 1
grade: 11
problem_id: test_math_display
source: Test
tags:
- test
title: Test Math Display
type: algebra
---

# Текст на задачата
Реши ја равенката: $x^2 + 2x + 1 = 0$

# Решение
## 📐 Детално Решение

<details>
<summary>Чекор 1: Формула за квадратен трином</summary>

$$ x^2 + 2x + 1 = (x + 1)^2 $$

</details>

<details>
<summary>Чекор 2: Решавање</summary>

$$ (x + 1)^2 = 0 \implies x + 1 = 0 \implies x = -1 $$

# Pedagogical Notes
Test math display.

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

</details>

---
### 🎨 Визуелизација
![Илустрација](/assets/images/test_math_display/test_math_display.png)