---
problem_id: test_pedagogical
title: Test Pedagogical Notes Accordion
grade: 8
difficulty: 2
tags:
  - test
  - pedagogy
source: Test Pedagogical
type: algebra
---

# Текст на задачата
Реши $x + 1 = 2$.

# Решение
## Стратегија
Ова е едноставна равенка.

## Чекор по чекор

**Чекор 1: Одземање**
$x + 1 - 1 = 2 - 1$

**Чекор 2: Решение**
$x = 1$

# Pedagogical Notes
1. **Основна идеја:** Решувањето равенки бара примена на обратни операции.
2. **Совет од Олимпиец:** Секогаш проверувај го решението со замена во оригиналната равенка.
3. **Чести грешки:** Не заборавај да примениш истата операција на двете страни.

# Manim Code
```python
from manim import *

class PedagogicalTest(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        eq = MathTex(r"x + 1 = 2", color=BLACK)
        self.play(Write(eq))
        self.wait(1)