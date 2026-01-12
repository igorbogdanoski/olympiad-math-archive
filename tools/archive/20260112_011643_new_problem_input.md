---
problem_id: test_fixes
title: Test Problem for Fixes
grade: 9
difficulty: 3
tags:
  - test
  - algebra
source: Test Problem
type: algebra
---

# Текст на задачата
Докажи дека $2 + 2 = 4$.

# Решение
## Стратегија
Ова е едноставна аритметичка равенка.

## Чекор по чекор

**Чекор 1: Собирање**
$2 + 2 = 4$

**Чекор 2: Проверка**
Да, ова е точно.

# Pedagogical Notes
1. **Основна идеја:** Собирањето е основна математичка операција.
2. **Совет:** Внимавајте со броевите.

# Manim Code
```python
from manim import *

class TestScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        text = Text("2 + 2 = 4", color=BLACK)
        self.play(Write(text))
        self.wait(1)