---
difficulty: 5
grade: 9
problem_id: test_sigma_138_1886
source: Sigma 138, Zadaca 1886
tags:
- test
- algebra
title: Test Problem from Sigma 138
type: algebra
---

# Problem

Solve for x: $$ x^2 + 2x + 1 = 0 $$

## Решение

$$ x = -1 $$

```python
from manim import *

class TestScene(Scene):
    def construct(self):
        text = Text("Test Illustration")
        self.play(Write(text))