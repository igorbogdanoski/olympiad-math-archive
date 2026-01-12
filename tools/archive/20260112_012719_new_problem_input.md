---
problem_id: complete_test
title: Complete Test with All Features
grade: 4
difficulty: 2
tags:
  - complete
  - test
  - manim
source: Complete Test
type: algebra
---

# Текст на задачата
Докажи дека $a^2 + b^2 \ge 2ab$.

# Решение
## Стратегија
Користи $(a-b)^2 \ge 0$.

## Чекор по чекор

**Чекор 1: Разлика на квадрати**
$a^2 + b^2 - 2ab = (a-b)^2$

**Чекор 2: Заклучок**
Бидејќи $(a-b)^2 \ge 0$, тогаш $a^2 + b^2 - 2ab \ge 0$, па $a^2 + b^2 \ge 2ab$.

# Pedagogical Notes
1. **Основна идеја:** $(a-b)^2 = a^2 - 2ab + b^2 \ge 0$ е основна неравенка.
2. **Совет од Олимпиец:** Оваа неравенка се користи во многу проблеми со средни вредности.
3. **Чести грешки:** Не заборавај дека квадрат е секогаш позитивен или нула.

# Manim Code
```python
from manim import *

class CompleteTest(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Title
        title = Text("a² + b² ≥ 2ab", color=BLACK).to_edge(UP)
        self.play(Write(title))

        # Equation
        eq = MathTex(r"a^2 + b^2 \geq 2ab", color=BLACK).next_to(title, DOWN)
        self.play(Write(eq))

        # Proof
        proof = MathTex(r"(a - b)^2 = a^2 - 2ab + b^2 \geq 0", color=GREEN).next_to(eq, DOWN)
        self.play(Write(proof))

        self.wait(2)