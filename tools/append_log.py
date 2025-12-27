
import os

log_path = r"c:\Users\pc4all\Documents\matholimpiad\olympiad-math-archive\assets\manim_code_log.md"

new_entries = """
### 🆔 Задача: 4376 - Плоштина на впишан триаголник
**📅 Додадено:** 2025-12-27 01:10
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_4376(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Dimensions
        # a = 27, b = 9. Ratio 3:1.
        # Scale for drawing
        scale = 0.25
        width = 27 * scale
        height = 9 * scale
        
        # Coordinates
        # A = bottom-left
        A = np.array([-width/2, -height/2, 0])
        B = np.array([width/2, -height/2, 0])
        C = np.array([width/2, height/2, 0])
        D = np.array([-width/2, height/2, 0])
        
        rect = Polygon(A, B, C, D, color=BLUE)
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP+RIGHT)
        lbl_D = MathTex("D").next_to(D, UP+LEFT)
        
        # M on AB, AM:MB = 1:2
        # M is at 1/3 of the way from A to B
        M = A + (B - A) * (1/3)
        dot_M = Dot(M, color=RED)
        lbl_M = MathTex("M").next_to(M, DOWN)
        
        # N on BC, BN = NC
        # N is midpoint of BC
        N = (B + C) / 2
        dot_N = Dot(N, color=RED)
        lbl_N = MathTex("N").next_to(N, RIGHT)
        
        # Triangle DMN
        tri_DMN = Polygon(D, M, N, color=RED, fill_opacity=0.2, fill_color=RED)
        
        self.add(rect, lbl_A, lbl_B, lbl_C, lbl_D)
        self.add(dot_M, lbl_M, dot_N, lbl_N)
        self.add(tri_DMN)
        
        # Add some braces
        brace_AB = Brace(Line(A, B), DOWN, buff=0.4)
        lbl_AB = brace_AB.get_text("27")
        
        brace_BC = Brace(Line(B, C), RIGHT, buff=0.4)
        lbl_BC = brace_BC.get_text("9")
        
        self.add(brace_AB, lbl_AB, brace_BC, lbl_BC)
```

### 🆔 Задача: 4411 - Агли во триаголник и симетрала
**📅 Додадено:** 2025-12-27 01:10
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_4411(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # A = 40, B = 60, C = 80
        # Coordinates
        # A at origin
        A = ORIGIN
        # B on x-axis. c = 6 (arbitrary)
        c_len = 6
        B = RIGHT * c_len
        
        # C coordinates
        # b = c * sin(60) / sin(80)
        b_len = c_len * np.sin(60*DEGREES) / np.sin(80*DEGREES)
        C_pt = np.array([b_len * np.cos(40*DEGREES), b_len * np.sin(40*DEGREES), 0])
        
        # Shift to center
        center = (A + B + C_pt) / 3
        A = A - center
        B = B - center
        C_pt = C_pt - center
        
        tri = Polygon(A, B, C_pt, color=BLUE)
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C_pt, UP)
        
        # Bisector of AC
        # Midpoint E
        E = (A + C_pt) / 2
        # Direction AC
        vec_AC = C_pt - A
        # Perpendicular direction
        perp_vec = np.array([-vec_AC[1], vec_AC[0], 0])
        perp_vec = perp_vec / np.linalg.norm(perp_vec)
        
        # Draw bisector line s
        s_start = E + perp_vec * 4
        s_end = E - perp_vec * 4
        bisector = Line(s_start, s_end, color=GREEN)
        lbl_s = MathTex("s", color=GREEN).next_to(s_start, UP)
        
        # Intersection D with AB
        # D is intersection of bisector and AB
        # We can calculate it or use line_intersection
        D = line_intersection(
            [s_start, s_end],
            [A, B]
        )
        dot_D = Dot(D, color=RED)
        lbl_D = MathTex("D").next_to(D, DOWN)
        
        self.add(tri, lbl_A, lbl_B, lbl_C)
        self.add(bisector, lbl_s)
        self.add(dot_D, lbl_D)
        
        # Mark right angle at E
        ra = RightAngle(Line(E, C_pt), Line(E, s_start), length=0.3, quadrant=(-1,1))
        self.add(ra)
```
"""

with open(log_path, "a", encoding="utf-8") as f:
    f.write(new_entries)

print("Successfully appended new entries to log.")
