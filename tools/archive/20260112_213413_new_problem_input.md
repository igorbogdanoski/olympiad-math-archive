---
problem_id: regional_2025_4_4b
title: Геометриско место на средини на впишани правоаголници
grade: 12
difficulty: 6
type: geometry
tags:
  - analiticka_geometrija
  - geometrijsko_mesto_na_tocki
  - vpisani_mnogougalnici
primary_skill: analiticka_geometrija_presmetki
related_skills:
  - ravenka_na_prava
  - aritmeticka_sredina
source: Сигма 139 (Регионален натпревар 2024/25)
---

# Геометриско место на средини на впишани правоаголници

# Текст на задачата
Во правоаголен координатен систем дадени се точките $A(a, 0)$, $B(b, 0)$ и $C(0, h)$, при што $a, h > 0$ и $b < 0$. Одреди го геометриското место на точките што претставуваат средини (пресек на дијагоналите) на правоаголниците впишани во триаголникот $ABC$, такви што, две од темињата на правоаголникот лежат на страната $AB$, а по едно теме лежи на останатите две страни на триаголникот.

## Решение

Средината на правоаголникот се движи долж отсечката од $R(\frac{a+b}{2}, 0)$ до $S(0, \frac{h}{2})$.

# Manim Code

```python
from manim import *
import numpy as np

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # --- CONFIGURATION ---
        a, b, h = 4, -2, 3
        scale = 1.2
        A_coord = np.array([a, 0, 0]) * scale
        B_coord = np.array([b, 0, 0]) * scale
        C_coord = np.array([0, h, 0]) * scale
        
        # Axes - origin at (0,0), vertices align on axes
        axes = Axes(
            x_range=[-2.5, 5, 1],
            y_range=[0, 4, 1],
            axis_config={"color": BLACK, "stroke_width": 2},
            tips=False
        ).scale(scale)
        
        # Triangle
        tri = Polygon(A_coord, C_coord, B_coord, color=BLACK, stroke_width=4)
        
        # Locus endpoints
        R_coord = np.array([(a+b)/2, 0, 0]) * scale
        S_coord = np.array([0, h/2, 0]) * scale
        locus = Line(R_coord, S_coord, color=RED, stroke_width=6)
        
        # Sample Rectangle at t=1.2
        t = 1.2
        xm = (a/h)*(h-t) * scale
        xn = (b/h)*(h-t) * scale
        M = np.array([xm, t * scale, 0])
        N = np.array([xn, t * scale, 0])
        P = np.array([xn, 0, 0])
        Q = np.array([xm, 0, 0])
        rect = Polygon(P, Q, M, N, color=BLUE, fill_opacity=0.1, stroke_width=2)
        
        # Center of rect
        K = Dot((M + N + P + Q)/4, color=RED)
        
        # Labels
        lbl_a = MathTex("A(a,0)", color=BLACK).next_to(A_coord, DR, buff=0.1)
        lbl_b = MathTex("B(b,0)", color=BLACK).next_to(B_coord, DL, buff=0.1)
        lbl_c = MathTex("C(0,h)", color=BLACK).next_to(C_coord, UP, buff=0.1)
        lbl_r = MathTex("R", color=RED).next_to(R_coord, DOWN)
        lbl_s = MathTex("S", color=RED).next_to(S_coord, LEFT)
        lbl_k = MathTex("K", color=RED).next_to(K, UR, buff=0.1)
        
        # Add everything to scene
        self.add(axes, tri, rect, locus, K)
        self.add(lbl_a, lbl_b, lbl_c, lbl_r, lbl_s, lbl_k)
```

### 🎨 Визуелизација
