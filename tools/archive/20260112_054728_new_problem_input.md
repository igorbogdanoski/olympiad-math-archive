---
problem_id: test_fix
title: Test Problem Fix
grade: 9
difficulty: 5
type: algebra
tags: [test, algebra]
source: Sigma 138, Zadaca 1887
---

# Problem

Solve for x: $$ x^2 + 3x + 2 = 0 $$

## Решение

$$ x = -1, -2 $$

# Manim Code

```python
from manim import *

class TestScene(Scene):
    def construct(self):
        text = Text("Fixed Illustration")
        self.play(Write(text))
```
