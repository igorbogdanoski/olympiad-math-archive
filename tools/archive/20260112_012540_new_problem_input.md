---
problem_id: final_test
title: Final Test for All Fixes
grade: 5
difficulty: 1
tags:
  - final
  - test
source: Final Test
type: algebra
---

# Текст на задачата
Реши $x + 1 = 2$.

# Решение
## Стратегија
Одземи 1 од двете страни.

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

class FinalTest(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        text = Text("x + 1 = 2 ⇒ x = 1", color=BLACK)
        self.play(Write(text))
        self.wait(1)