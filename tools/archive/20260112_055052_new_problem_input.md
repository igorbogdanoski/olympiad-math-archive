---
problem_id: test_trusted
title: Test Trusted Code
grade: 9
difficulty: 5
type: algebra
tags: [test, algebra]
source: Sigma 138, Zadaca 1888
trusted: true
---

# Problem

Solve for x: $$ x^2 + 4x + 3 = 0 $$

## Решение

$$ x = -1, -3 $$

# Manim Code

```python
import manim as mn

class MyScene(mn.Scene):
    def construct(self):
        txt = mn.Text("Trusted Illustration")
        self.play(mn.Write(txt))
```
