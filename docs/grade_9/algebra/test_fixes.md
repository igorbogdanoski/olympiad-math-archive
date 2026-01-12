---
difficulty: 3
grade: 9
problem_id: test_fixes
source: Test Problem
tags:
- test
- algebra
title: Test Problem for Fixes
type: algebra
---

# Текст на задачата
Докажи дека $2 + 2 = 4$.

# Решение
## Стратегија
Ова е едноставна аритметичка равенка.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Собирање</summary>

$2 + 2 = 4$

</details>

<details>
<summary>Чекор 2: Проверка</summary>

Да, ова е точно.

# Pedagogical Notes
1. **Основна идеја:** Собирањето е основна математичка операција.
2. **Совет:** Внимавајте со броевите.

```python
from manim import *

class TestScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        text = Text("2 + 2 = 4", color=BLACK)
        self.play(Write(text))
        self.wait(1)

</details>