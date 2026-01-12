---
difficulty: 1
grade: 5
problem_id: final_test
source: Final Test
tags:
- final
- test
title: Final Test for All Fixes
type: algebra
---

# Текст на задачата
Реши $x + 1 = 2$.

# Решение
## Стратегија
Одземи 1 од двете страни.

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

class FinalTest(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        text = Text("x + 1 = 2 ⇒ x = 1", color=BLACK)
        self.play(Write(text))
        self.wait(1)

</details>