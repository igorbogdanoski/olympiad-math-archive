---
problem_id: test_sigma_138_1886
title: Test Problem from Sigma 138
grade: 9
difficulty: 5
type: algebra
tags: [test, algebra]
source: Sigma 138, Zadaca 1886
---

# Problem

Solve for x: $$ x^2 + 2x + 1 = 0 $$

## Решение

$$ x = -1 $$

# Manim Code

```python
from manim import *

class TestScene(Scene):
    def construct(self):
        text = Text("Test Illustration")
        self.play(Write(text))