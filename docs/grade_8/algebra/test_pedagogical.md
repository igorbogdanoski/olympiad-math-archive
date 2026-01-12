---
difficulty: 2
grade: 8
problem_id: test_pedagogical
source: Test Pedagogical
tags:
- test
- pedagogy
title: Test Pedagogical Notes Accordion
type: algebra
---

# Текст на задачата
Реши $x + 1 = 2$.

# Решение
## Стратегија
Ова е едноставна равенка.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Одземање</summary>

$x + 1 - 1 = 2 - 1$

</details>

<details>
<summary>Чекор 2: Решение</summary>

$x = 1$

# Pedagogical Notes
1. **Основна идеја:** Решувањето равенки бара примена на обратни операции.
2. **Совет од Олимпиец:** Секогаш проверувај го решението со замена во оригиналната равенка.
3. **Чести грешки:** Не заборавај да примениш истата операција на двете страни.

```python
from manim import *

class PedagogicalTest(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        eq = MathTex(r"x + 1 = 2", color=BLACK)
        self.play(Write(eq))
        self.wait(1)

</details>