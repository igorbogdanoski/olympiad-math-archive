
### 🆔 Задача: Cnt92-1012_Prob12 - Најмала вредност на функција на интервал
**📅 Додадено:** 2025-12-26 19:23
**🐍 Python/Manim Код (Копирај во Geo-Mentor):**
```python
from manim import *

class ProblemScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE
    
    # Axes
    axes = Axes(
        x_range=[-3, 4, 1],
        y_range=[-4, 8, 2],
        axis_config={"color": BLACK, "include_numbers": True},
        tips=True
    ).scale(0.8)
    
    # Function y = -x^2 + 2x + 5
    parabola = axes.plot(lambda x: -x**2 + 2*x + 5, color=BLUE)
    
    # Interval [-2, 2]
    interval_line = Line(
        start=axes.c2p(-2, 0),
        end=axes.c2p(2, 0),
        color=GREEN,
        stroke_width=6
    )
    
    # Points of interest
    # x = -2, y = -3 (Minimum on interval)
    pt_min = axes.c2p(-2, -3)
    dot_min = Dot(pt_min, color=RED, radius=0.12)
    label_min = MathTex("min(-2, -3)", color=RED).next_to(dot_min, DOWN+LEFT)
    
    # x = 1, y = 6 (Vertex - Max)
    pt_vertex = axes.c2p(1, 6)
    dot_vertex = Dot(pt_vertex, color=BLACK, radius=0.08)
    label_vertex = MathTex("V(1, 6)", color=BLACK).next_to(dot_vertex, UP)
    
    # x = 2, y = 5 (Other endpoint)
    pt_end = axes.c2p(2, 5)
    dot_end = Dot(pt_end, color=BLACK, radius=0.08)
    
    # Dashed lines for min
    dash_h = DashedLine(start=axes.c2p(0, -3), end=pt_min, color=GRAY)
    dash_v = DashedLine(start=axes.c2p(-2, 0), end=pt_min, color=GRAY)
    
    self.add(axes, parabola, interval_line, dot_min, label_min, dot_vertex, label_vertex, dot_end, dash_h, dash_v)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: Cnt92-1012_Prob12 - Најмала вредност на функција на интервал
**📅 Додадено:** 2025-12-26 20:41
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_Cnt92_1012_Prob12(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE
    
    # Axes
    axes = Axes(
        x_range=[-3, 4, 1],
        y_range=[-4, 8, 2],
        axis_config={"color": BLACK, "include_numbers": True},
        tips=True
    ).scale(0.8)
    
    # Function y = -x^2 + 2x + 5
    parabola = axes.plot(lambda x: -x**2 + 2*x + 5, color=BLUE)
    
    # Interval [-2, 2]
    interval_line = Line(
        start=axes.c2p(-2, 0),
        end=axes.c2p(2, 0),
        color=GREEN,
        stroke_width=6
    )
    
    # Points of interest
    # x = -2, y = -3 (Minimum on interval)
    pt_min = axes.c2p(-2, -3)
    dot_min = Dot(pt_min, color=RED, radius=0.12)
    label_min = MathTex("min(-2, -3)", color=RED).next_to(dot_min, DOWN+LEFT)
    
    # x = 1, y = 6 (Vertex - Max)
    pt_vertex = axes.c2p(1, 6)
    dot_vertex = Dot(pt_vertex, color=BLACK, radius=0.08)
    label_vertex = MathTex("V(1, 6)", color=BLACK).next_to(dot_vertex, UP)
    
    # x = 2, y = 5 (Other endpoint)
    pt_end = axes.c2p(2, 5)
    dot_end = Dot(pt_end, color=BLACK, radius=0.08)
    
    # Dashed lines for min
    dash_h = DashedLine(start=axes.c2p(0, -3), end=pt_min, color=GRAY)
    dash_v = DashedLine(start=axes.c2p(-2, 0), end=pt_min, color=GRAY)
    
    self.add(axes, parabola, interval_line, dot_min, label_min, dot_vertex, label_vertex, dot_end, dash_h, dash_v)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: Cnt92-1012_Prob12 - Најмала вредност на функција на интервал
**📅 Додадено:** 2025-12-26 20:46
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_Cnt92_1012_Prob12(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE
    
    # Axes
    axes = Axes(
        x_range=[-3, 4, 1],
        y_range=[-4, 8, 2],
        axis_config={"color": BLACK, "include_numbers": True},
        tips=True
    ).scale(0.8)
    
    # Function y = -x^2 + 2x + 5
    parabola = axes.plot(lambda x: -x**2 + 2*x + 5, color=BLUE)
    
    # Interval [-2, 2]
    interval_line = Line(
        start=axes.c2p(-2, 0),
        end=axes.c2p(2, 0),
        color=GREEN,
        stroke_width=6
    )
    
    # Points of interest
    # x = -2, y = -3 (Minimum on interval)
    pt_min = axes.c2p(-2, -3)
    dot_min = Dot(pt_min, color=RED, radius=0.12)
    label_min = MathTex("min(-2, -3)", color=RED).next_to(dot_min, DOWN+LEFT)
    
    # x = 1, y = 6 (Vertex - Max)
    pt_vertex = axes.c2p(1, 6)
    dot_vertex = Dot(pt_vertex, color=BLACK, radius=0.08)
    label_vertex = MathTex("V(1, 6)", color=BLACK).next_to(dot_vertex, UP)
    
    # x = 2, y = 5 (Other endpoint)
    pt_end = axes.c2p(2, 5)
    dot_end = Dot(pt_end, color=BLACK, radius=0.08)
    
    # Dashed lines for min
    dash_h = DashedLine(start=axes.c2p(0, -3), end=pt_min, color=GRAY)
    dash_v = DashedLine(start=axes.c2p(-2, 0), end=pt_min, color=GRAY)
    
    self.add(axes, parabola, interval_line, dot_min, label_min, dot_vertex, label_vertex, dot_end, dash_h, dash_v)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: Cnt92-1012_Prob12 - Најмала вредност на функција на интервал
**📅 Додадено:** 2025-12-26 21:00
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_Cnt92_1012_Prob12(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE
    
    # Axes
    axes = Axes(
        x_range=[-3, 4, 1],
        y_range=[-4, 8, 2],
        axis_config={"color": BLACK, "include_numbers": True},
        tips=True
    ).scale(0.8)
    
    # Function y = -x^2 + 2x + 5
    parabola = axes.plot(lambda x: -x**2 + 2*x + 5, color=BLUE)
    
    # Interval [-2, 2]
    interval_line = Line(
        start=axes.c2p(-2, 0),
        end=axes.c2p(2, 0),
        color=GREEN,
        stroke_width=6
    )
    
    # Points of interest
    # x = -2, y = -3 (Minimum on interval)
    pt_min = axes.c2p(-2, -3)
    dot_min = Dot(pt_min, color=RED, radius=0.12)
    label_min = MathTex("min(-2, -3)", color=RED).next_to(dot_min, DOWN+LEFT)
    
    # x = 1, y = 6 (Vertex - Max)
    pt_vertex = axes.c2p(1, 6)
    dot_vertex = Dot(pt_vertex, color=BLACK, radius=0.08)
    label_vertex = MathTex("V(1, 6)", color=BLACK).next_to(dot_vertex, UP)
    
    # x = 2, y = 5 (Other endpoint)
    pt_end = axes.c2p(2, 5)
    dot_end = Dot(pt_end, color=BLACK, radius=0.08)
    
    # Dashed lines for min
    dash_h = DashedLine(start=axes.c2p(0, -3), end=pt_min, color=GRAY)
    dash_v = DashedLine(start=axes.c2p(-2, 0), end=pt_min, color=GRAY)
    
    self.add(axes, parabola, interval_line, dot_min, label_min, dot_vertex, label_vertex, dot_end, dash_h, dash_v)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 14 - Позиција на точки во однос на права
**📅 Додадено:** 2025-12-26 21:07
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_14(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_14(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Coordinate System
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 7, 1],
            axis_config={"color": BLACK, "include_numbers": True},
            background_line_style={"stroke_color": GRAY, "stroke_width": 1, "stroke_opacity": 0.2}
        )
        
        # The Line y = sqrt(2)x + sqrt(3)
        line_graph = axes.plot(
            lambda x: 1.414 * x + 1.732,
            color=BLUE,
            stroke_width=4
        )
        line_label = MathTex("y = \\sqrt{2}x + \\sqrt{3}", color=BLUE).next_to(line_graph, UP).shift(RIGHT)
        
        # Points
        dot_A = Dot(axes.c2p(1, 3), color=RED, radius=0.1)
        label_A = MathTex("A(1, 3)", color=RED).next_to(dot_A, DOWN)
        
        dot_B = Dot(axes.c2p(2, 5), color=GREEN, radius=0.1)
        label_B = MathTex("B(2, 5)", color=GREEN).next_to(dot_B, UP)
        
        # Dashed lines for comparison
        y_on_line_A = 1.414 * 1 + 1.732
        dot_line_A = Dot(axes.c2p(1, y_on_line_A), color=BLUE, radius=0.05)
        dashed_A = DashedLine(dot_A.get_center(), dot_line_A.get_center(), color=GRAY)
        
        y_on_line_B = 1.414 * 2 + 1.732
        dot_line_B = Dot(axes.c2p(2, y_on_line_B), color=BLUE, radius=0.05)
        dashed_B = DashedLine(dot_B.get_center(), dot_line_B.get_center(), color=GRAY)

        self.add(axes, line_graph, line_label)
        self.add(dot_A, label_A, dashed_A)
        self.add(dot_B, label_B, dashed_B)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 16 - Збир на координати на пресек
**📅 Додадено:** 2025-12-26 21:07
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_16(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_16(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Coefficients
        a_val = 2.236 - 1.732 # sqrt(5) - sqrt(3) approx 0.504
        b_val = -2
        c_val = -(2.236 - 1.732)
        
        # Function
        def func(x):
            return a_val * x**2 + b_val * x + c_val

        axes = Axes(
            x_range=[-2, 5, 1],
            y_range=[-3, 4, 1],
            axis_config={"color": BLACK, "include_numbers": True},
            background_line_style={"stroke_opacity": 0}
        )
        
        graph = axes.plot(func, color=BLUE, stroke_width=3)
        
        root1 = Dot(axes.c2p(-0.24, 0), color=RED)
        root2 = Dot(axes.c2p(4.2, 0), color=RED)
        
        label_x1 = MathTex("x_1", color=RED).next_to(root1, UP)
        label_x2 = MathTex("x_2", color=RED).next_to(root2, UP)
        
        equation = MathTex(
            "x_1 + x_2 = -\\frac{b}{a} = \\sqrt{5} + \\sqrt{3}",
            color=BLACK
        ).to_edge(UP)

        self.add(axes, graph)
        self.add(root1, root2, label_x1, label_x2)
        self.add(equation)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 13 - Економисти и Математичари
**📅 Додадено:** 2025-12-26 21:36
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_13(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_13(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Sets
        c1 = Circle(radius=1.5, color=BLUE, fill_opacity=0.1).shift(LEFT)
        c2 = Circle(radius=1.5, color=RED, fill_opacity=0.1).shift(RIGHT)
        
        # Labels
        t1 = MathTex("M (50)", color=BLUE).next_to(c1, UL)
        t2 = MathTex("E (40)", color=RED).next_to(c2, UR)
        t_inter = MathTex("?", color=BLACK).move_to(ORIGIN)
        
        # Universe box
        rect = Rectangle(width=7, height=5, color=BLACK)
        t_u = MathTex("U = 70", color=BLACK).to_corner(UL)
        t_none = MathTex("None = 10", color=GRAY).to_corner(DR)
        
        self.add(rect, c1, c2, t1, t2, t_inter, t_u, t_none)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 14 - Позиција на точки во однос на права
**📅 Додадено:** 2025-12-26 21:36
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_14(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_14(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-1, 4, 1], y_range=[-1, 6, 1], axis_config={"color": BLACK})
        
        # Line
        line = axes.plot(lambda x: 1.414 * x + 1.732, color=BLUE)
        lbl_line = MathTex("y=\\sqrt{2}x+\\sqrt{3}", color=BLUE).next_to(line, UP)
        
        # Points
        pt_A = Dot(axes.c2p(1, 3), color=RED)
        lbl_A = MathTex("A", color=RED).next_to(pt_A, DOWN)
        
        pt_B = Dot(axes.c2p(2, 5), color=GREEN)
        lbl_B = MathTex("B", color=GREEN).next_to(pt_B, UP)
        
        self.add(axes, line, lbl_line, pt_A, lbl_A, pt_B, lbl_B)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 16 - Збир на координати на пресек
**📅 Додадено:** 2025-12-26 21:36
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_16(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_16(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-2, 6, 1], y_range=[-3, 3, 1], axis_config={"color": BLACK})
        
        # Parabola (approximate coeffs for visual)
        a = 0.5
        b = -2
        c = -0.5
        graph = axes.plot(lambda x: a*x**2 + b*x + c, color=BLUE)
        
        # Roots
        r1 = Dot(axes.c2p(-0.24, 0), color=RED)
        r2 = Dot(axes.c2p(4.2, 0), color=RED)
        
        lbl = MathTex("x_1 + x_2 = -b/a", color=BLACK).to_corner(UR)
        
        self.add(axes, graph, r1, r2, lbl)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 13 - Економисти и Математичари
**📅 Додадено:** 2025-12-26 21:56
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_13(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_13(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Sets
        c1 = Circle(radius=1.5, color=BLUE, fill_opacity=0.1).shift(LEFT)
        c2 = Circle(radius=1.5, color=RED, fill_opacity=0.1).shift(RIGHT)
        
        # Labels
        t1 = MathTex("M (50)", color=BLUE).next_to(c1, UL)
        t2 = MathTex("E (40)", color=RED).next_to(c2, UR)
        t_inter = MathTex("?", color=BLACK).move_to(ORIGIN)
        
        # Universe box
        rect = Rectangle(width=7, height=5, color=BLACK)
        t_u = MathTex("U = 70", color=BLACK).to_corner(UL)
        t_none = MathTex("None = 10", color=GRAY).to_corner(DR)
        
        self.add(rect, c1, c2, t1, t2, t_inter, t_u, t_none)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 14 - Позиција на точки во однос на права
**📅 Додадено:** 2025-12-26 21:56
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_14(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_14(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-1, 4, 1], y_range=[-1, 6, 1], axis_config={"color": BLACK})
        
        # Line
        line = axes.plot(lambda x: 1.414 * x + 1.732, color=BLUE)
        lbl_line = MathTex("y=\\sqrt{2}x+\\sqrt{3}", color=BLUE).next_to(line, UP)
        
        # Points
        pt_A = Dot(axes.c2p(1, 3), color=RED)
        lbl_A = MathTex("A", color=RED).next_to(pt_A, DOWN)
        
        pt_B = Dot(axes.c2p(2, 5), color=GREEN)
        lbl_B = MathTex("B", color=GREEN).next_to(pt_B, UP)
        
        self.add(axes, line, lbl_line, pt_A, lbl_A, pt_B, lbl_B)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 16 - Збир на координати на пресек
**📅 Додадено:** 2025-12-26 21:56
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_16(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_16(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-2, 6, 1], y_range=[-3, 3, 1], axis_config={"color": BLACK})
        
        # Parabola (approximate coeffs for visual)
        a = 0.5
        b = -2
        c = -0.5
        graph = axes.plot(lambda x: a*x**2 + b*x + c, color=BLUE)
        
        # Roots
        r1 = Dot(axes.c2p(-0.24, 0), color=RED)
        r2 = Dot(axes.c2p(4.2, 0), color=RED)
        
        lbl = MathTex("x_1 + x_2 = -b/a", color=BLACK).to_corner(UR)
        
        self.add(axes, graph, r1, r2, lbl)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 20 - Пресек на две прави
**📅 Додадено:** 2025-12-26 21:57
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_20(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_20(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": BLACK, "include_numbers": True}
        )
        
        # Lines
        # y = -7/3 x + 5/6
        line1 = axes.plot(lambda x: -2.33*x + 0.833, color=BLUE)
        # y = -3/7 x + 2.5
        line2 = axes.plot(lambda x: -0.428*x + 2.5, color=GREEN)
        
        # Intersection Point (-0.875, 2.875)
        x_int = -0.875
        y_int = 2.875
        dot = Dot(axes.c2p(x_int, y_int), color=RED)
        
        label = MathTex("P(-\\frac{7}{8}, \\frac{23}{8})", color=RED).next_to(dot, UR)
        sum_label = MathTex("x+y=2", color=BLACK).to_corner(UR)

        self.add(axes, line1, line2, dot, label, sum_label)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 20 - Пресек на две прави
**📅 Додадено:** 2025-12-26 22:08
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_20(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_20(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": BLACK, "include_numbers": True}
        )
        
        # Lines
        # y = -7/3 x + 5/6
        line1 = axes.plot(lambda x: -2.33*x + 0.833, color=BLUE)
        # y = -3/7 x + 2.5
        line2 = axes.plot(lambda x: -0.428*x + 2.5, color=GREEN)
        
        # Intersection Point (-0.875, 2.875)
        x_int = -0.875
        y_int = 2.875
        dot = Dot(axes.c2p(x_int, y_int), color=RED)
        
        label = MathTex("P(-\\frac{7}{8}, \\frac{23}{8})", color=RED).next_to(dot, UR)
        sum_label = MathTex("x+y=2", color=BLACK).to_corner(UR)

        self.add(axes, line1, line2, dot, label, sum_label)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 20 - Пресек на две прави
**📅 Додадено:** 2025-12-26 22:18
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_20(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_20(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": BLACK, "include_numbers": True}
        )
        
        # Lines
        # y = -7/3 x + 5/6
        line1 = axes.plot(lambda x: -2.33*x + 0.833, color=BLUE)
        # y = -3/7 x + 2.5
        line2 = axes.plot(lambda x: -0.428*x + 2.5, color=GREEN)
        
        # Intersection Point (-0.875, 2.875)
        x_int = -0.875
        y_int = 2.875
        dot = Dot(axes.c2p(x_int, y_int), color=RED)
        
        label = MathTex("P(-\\frac{7}{8}, \\frac{23}{8})", color=RED).next_to(dot, UR)
        sum_label = MathTex("x+y=2", color=BLACK).to_corner(UR)

        self.add(axes, line1, line2, dot, label, sum_label)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 24 - Максимална плоштина на паралелограм
**📅 Додадено:** 2025-12-26 22:22
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_24(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_24(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Define points for a rhombus (since max area is when a=b)
        # Side length approx 3 units for visualization
        a = 3
        angle = 30 * DEGREES
        
        p1 = ORIGIN
        p2 = RIGHT * a
        p3 = p2 + np.array([a * np.cos(angle), a * np.sin(angle), 0])
        p4 = p1 + np.array([a * np.cos(angle), a * np.sin(angle), 0])
        
        parallelogram = Polygon(p1, p2, p3, p4, color=BLUE, stroke_width=4)
        
        # Labels
        lbl_a = MathTex("a", color=BLACK).next_to(Line(p1, p2), DOWN)
        lbl_b = MathTex("b", color=BLACK).next_to(Line(p2, p3), RIGHT)
        
        # Angle arc
        arc = Angle(Line(p1, p2), Line(p1, p4), radius=0.5, color=RED)
        lbl_angle = MathTex("30^\circ", color=RED).next_to(arc, RIGHT, buff=0.1).shift(UP*0.1)
        
        # Area formula
        formula = MathTex("S = a \\cdot b \\cdot \\sin(30^\circ)", color=BLACK).to_edge(UP)
        cond = MathTex("a+b=24", color=BLACK).next_to(formula, DOWN)
        
        self.add(parallelogram, lbl_a, lbl_b, arc, lbl_angle, formula, cond)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 25 - Неравенка со апсолутни вредности
**📅 Додадено:** 2025-12-26 22:22
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_25(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_25(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Number line
        number_line = NumberLine(
            x_range=[-15, 0, 1],
            length=10,
            color=BLACK,
            include_numbers=True,
            label_direction=DOWN
        )
        
        # Interval (-inf, -3)
        interval_line = Line(
            start=number_line.n2p(-15), 
            end=number_line.n2p(-3), 
            color=BLUE, 
            stroke_width=6
        )
        label_int = MathTex("x < -3", color=BLUE).next_to(number_line.n2p(-3), UP)
        
        # Solution x <= -12
        sol_line = Line(
            start=number_line.n2p(-15), 
            end=number_line.n2p(-12), 
            color=RED, 
            stroke_width=6
        ).shift(UP*0.1) # Shift slightly to show overlap
        
        label_sol = MathTex("x \\le -12", color=RED).next_to(number_line.n2p(-12), UP).shift(LEFT)
        
        self.add(number_line, interval_line, label_int, sol_line, label_sol)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 26 - Број на решенија на систем равенки
**📅 Додадено:** 2025-12-26 22:22
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_26(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_26(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-4, 4, 1], y_range=[-1, 4, 1], axis_config={"color": BLACK})
        
        # Piecewise function segments
        # x < 0, y = 0
        seg1 = Line(axes.c2p(-4, 0), axes.c2p(0, 0), color=BLUE, stroke_width=4)
        # 0 < x < 2, y = 2
        seg2 = Line(axes.c2p(0, 2), axes.c2p(2, 2), color=BLUE, stroke_width=4)
        # x > 2, y = 0
        seg3 = Line(axes.c2p(2, 0), axes.c2p(4, 0), color=BLUE, stroke_width=4)
        
        # Holes
        h1 = Circle(radius=0.08, color=BLUE, fill_color=WHITE, fill_opacity=1).move_to(axes.c2p(0, 0))
        h2 = Circle(radius=0.08, color=BLUE, fill_color=WHITE, fill_opacity=1).move_to(axes.c2p(0, 2))
        h3 = Circle(radius=0.08, color=BLUE, fill_color=WHITE, fill_opacity=1).move_to(axes.c2p(2, 2))
        h4 = Circle(radius=0.08, color=BLUE, fill_color=WHITE, fill_opacity=1).move_to(axes.c2p(2, 0))
        
        # The Line y = kx + 1 (example k=1)
        line = axes.plot(lambda x: 1*x + 1, color=RED)
        lbl_line = MathTex("y=kx+1", color=RED).next_to(line, UP)
        
        self.add(axes, seg1, seg2, seg3, h1, h2, h3, h4, line, lbl_line)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 27 - Бесконечно многу решенија на ирационална равенка
**📅 Додадено:** 2025-12-26 22:22
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_27(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_27(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        number_line = NumberLine(
            x_range=[0, 4, 1],
            length=8,
            color=BLACK,
            include_numbers=True
        )
        
        # Points A and B
        pt_A = Dot(number_line.n2p(1.414), color=BLUE)
        lbl_A = MathTex("\\sqrt{2}", color=BLUE).next_to(pt_A, DOWN)
        
        pt_B = Dot(number_line.n2p(2.236), color=BLUE)
        lbl_B = MathTex("\\sqrt{5}", color=BLUE).next_to(pt_B, DOWN)
        
        # Segment between them
        segment = Line(pt_A.get_center(), pt_B.get_center(), color=RED, stroke_width=6)
        lbl_seg = MathTex("a = \\sqrt{5}-\\sqrt{2}", color=RED).next_to(segment, UP)
        
        # Point x
        pt_x = Dot(number_line.n2p(1.8), color=GREEN)
        lbl_x = MathTex("x", color=GREEN).next_to(pt_x, UP)
        
        self.add(number_line, pt_A, lbl_A, pt_B, lbl_B, segment, lbl_seg, pt_x, lbl_x)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 24 - Максимална плоштина на паралелограм
**📅 Додадено:** 2025-12-26 23:17
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_24(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_24(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Define points for a rhombus (since max area is when a=b)
        # Side length approx 3 units for visualization
        a = 3
        angle = 30 * DEGREES
        
        p1 = ORIGIN
        p2 = RIGHT * a
        p3 = p2 + np.array([a * np.cos(angle), a * np.sin(angle), 0])
        p4 = p1 + np.array([a * np.cos(angle), a * np.sin(angle), 0])
        
        parallelogram = Polygon(p1, p2, p3, p4, color=BLUE, stroke_width=4)
        
        # Labels
        lbl_a = MathTex("a", color=BLACK).next_to(Line(p1, p2), DOWN)
        lbl_b = MathTex("b", color=BLACK).next_to(Line(p2, p3), RIGHT)
        
        # Angle arc
        arc = Angle(Line(p1, p2), Line(p1, p4), radius=0.5, color=RED)
        lbl_angle = MathTex("30^\circ", color=RED).next_to(arc, RIGHT, buff=0.1).shift(UP*0.1)
        
        # Area formula
        formula = MathTex("S = a \\cdot b \\cdot \\sin(30^\circ)", color=BLACK).to_edge(UP)
        cond = MathTex("a+b=24", color=BLACK).next_to(formula, DOWN)
        
        self.add(parallelogram, lbl_a, lbl_b, arc, lbl_angle, formula, cond)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 25 - Неравенка со апсолутни вредности
**📅 Додадено:** 2025-12-26 23:17
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_25(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_25(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Number line
        number_line = NumberLine(
            x_range=[-15, 0, 1],
            length=10,
            color=BLACK,
            include_numbers=True,
            label_direction=DOWN
        )
        
        # Interval (-inf, -3)
        interval_line = Line(
            start=number_line.n2p(-15), 
            end=number_line.n2p(-3), 
            color=BLUE, 
            stroke_width=6
        )
        label_int = MathTex("x < -3", color=BLUE).next_to(number_line.n2p(-3), UP)
        
        # Solution x <= -12
        sol_line = Line(
            start=number_line.n2p(-15), 
            end=number_line.n2p(-12), 
            color=RED, 
            stroke_width=6
        ).shift(UP*0.1) # Shift slightly to show overlap
        
        label_sol = MathTex("x \\le -12", color=RED).next_to(number_line.n2p(-12), UP).shift(LEFT)
        
        self.add(number_line, interval_line, label_int, sol_line, label_sol)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 26 - Број на решенија на систем равенки
**📅 Додадено:** 2025-12-26 23:17
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_26(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_26(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-4, 4, 1], y_range=[-1, 4, 1], axis_config={"color": BLACK})
        
        # Piecewise function segments
        # x < 0, y = 0
        seg1 = Line(axes.c2p(-4, 0), axes.c2p(0, 0), color=BLUE, stroke_width=4)
        # 0 < x < 2, y = 2
        seg2 = Line(axes.c2p(0, 2), axes.c2p(2, 2), color=BLUE, stroke_width=4)
        # x > 2, y = 0
        seg3 = Line(axes.c2p(2, 0), axes.c2p(4, 0), color=BLUE, stroke_width=4)
        
        # Holes
        h1 = Circle(radius=0.08, color=BLUE, fill_color=WHITE, fill_opacity=1).move_to(axes.c2p(0, 0))
        h2 = Circle(radius=0.08, color=BLUE, fill_color=WHITE, fill_opacity=1).move_to(axes.c2p(0, 2))
        h3 = Circle(radius=0.08, color=BLUE, fill_color=WHITE, fill_opacity=1).move_to(axes.c2p(2, 2))
        h4 = Circle(radius=0.08, color=BLUE, fill_color=WHITE, fill_opacity=1).move_to(axes.c2p(2, 0))
        
        # The Line y = kx + 1 (example k=1)
        line = axes.plot(lambda x: 1*x + 1, color=RED)
        lbl_line = MathTex("y=kx+1", color=RED).next_to(line, UP)
        
        self.add(axes, seg1, seg2, seg3, h1, h2, h3, h4, line, lbl_line)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 27 - Бесконечно многу решенија на ирационална равенка
**📅 Додадено:** 2025-12-26 23:17
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_27(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_27(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        number_line = NumberLine(
            x_range=[0, 4, 1],
            length=8,
            color=BLACK,
            include_numbers=True
        )
        
        # Points A and B
        pt_A = Dot(number_line.n2p(1.414), color=BLUE)
        lbl_A = MathTex("\\sqrt{2}", color=BLUE).next_to(pt_A, DOWN)
        
        pt_B = Dot(number_line.n2p(2.236), color=BLUE)
        lbl_B = MathTex("\\sqrt{5}", color=BLUE).next_to(pt_B, DOWN)
        
        # Segment between them
        segment = Line(pt_A.get_center(), pt_B.get_center(), color=RED, stroke_width=6)
        lbl_seg = MathTex("a = \\sqrt{5}-\\sqrt{2}", color=RED).next_to(segment, UP)
        
        # Point x
        pt_x = Dot(number_line.n2p(1.8), color=GREEN)
        lbl_x = MathTex("x", color=GREEN).next_to(pt_x, UP)
        
        self.add(number_line, pt_A, lbl_A, pt_B, lbl_B, segment, lbl_seg, pt_x, lbl_x)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 29 - Параметар во равенка со signum функција
**📅 Додадено:** 2025-12-26 23:18
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_29(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_29(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        number_line = NumberLine(
            x_range=[-3, 4, 1],
            length=10,
            color=BLACK,
            include_numbers=True
        )
        
        # Forbidden zone [-1, 2]
        forbidden = Line(
            number_line.n2p(-1),
            number_line.n2p(2),
            color=RED,
            stroke_width=8
        )
        lbl_forbid = MathTex("u(x) \\le 0", color=RED).next_to(forbidden, UP)
        
        # Parameter range [0, 1]
        param_range = Line(
            number_line.n2p(0),
            number_line.n2p(1),
            color=GREEN,
            stroke_width=8
        ).shift(DOWN * 0.5)
        lbl_param = MathTex("a \\in [0, 1]", color=GREEN).next_to(param_range, DOWN)
        
        self.add(number_line, forbidden, lbl_forbid, param_range, lbl_param)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_03 - Заемна положба на прави
**📅 Додадено:** 2025-12-26 23:26
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], axis_config={"color": BLACK})
        
        # Case a = 1
        # y = x - 1
        line1 = axes.plot(lambda x: x - 1, color=BLUE)
        lbl1 = MathTex("y = x - 1", color=BLUE).next_to(line1, DR)
        
        # y = x + 1
        line2 = axes.plot(lambda x: x + 1, color=RED)
        lbl2 = MathTex("y = x + 1", color=RED).next_to(line2, UL)
        
        title = MathTex("a=1: \\text{Parallel}", color=BLACK).to_corner(UL)
        
        self.add(axes, line1, lbl1, line2, lbl2, title)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_03 - Заемна положба на прави
**📅 Додадено:** 2025-12-26 23:30
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], axis_config={"color": BLACK})
        
        # Case a = 1
        # y = x - 1
        line1 = axes.plot(lambda x: x - 1, color=BLUE)
        lbl1 = MathTex("y = x - 1", color=BLUE).next_to(line1, DR)
        
        # y = x + 1
        line2 = axes.plot(lambda x: x + 1, color=RED)
        lbl2 = MathTex("y = x + 1", color=RED).next_to(line2, UL)
        
        title = MathTex("a=1: \\text{Parallel}", color=BLACK).to_corner(UL)
        
        self.add(axes, line1, lbl1, line2, lbl2, title)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_05 - Равенка на права низ две точки
**📅 Додадено:** 2025-12-26 23:33
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_05(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_05(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-1, 4, 1], y_range=[-4, 2, 1], axis_config={"color": BLACK})
        
        # Points
        p1 = Dot(axes.c2p(2, 0), color=RED)
        lbl1 = MathTex("(2, 0)", color=RED).next_to(p1, UP)
        
        p2 = Dot(axes.c2p(0, -3), color=RED)
        lbl2 = MathTex("(0, -3)", color=RED).next_to(p2, RIGHT)
        
        # Line
        line = axes.plot(lambda x: 1.5*x - 3, color=BLUE)
        eq = MathTex("y = 1.5x - 3", color=BLUE).to_corner(UL)
        
        self.add(axes, p1, lbl1, p2, lbl2, line, eq)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_08 - Тежишна линија кон хипотенузата
**📅 Додадено:** 2025-12-26 23:33
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_08(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_08(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Triangle vertices (6, 8, 10 scaled down by 2 for view)
        A = ORIGIN
        B = RIGHT * 4  # represents 8
        C = UP * 3     # represents 6
        
        triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
        
        # Midpoint of hypotenuse BC
        M = (B + C) / 2
        median = Line(A, M, color=RED, stroke_width=4)
        
        # Labels
        lbl_a = MathTex("6", color=BLACK).next_to(Line(A, C), LEFT)
        lbl_b = MathTex("8", color=BLACK).next_to(Line(A, B), DOWN)
        lbl_c = MathTex("c=10", color=BLACK).next_to(Line(B, C), UR)
        lbl_m = MathTex("m_c = ?", color=RED).next_to(median, RIGHT, buff=0.1)
        
        # Right angle symbol
        ra = RightAngle(Line(A, B), Line(A, C), length=0.4, color=BLACK)
        
        self.add(triangle, median, lbl_a, lbl_b, lbl_c, lbl_m, ra)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_09 - Квадратна равенка без решенија
**📅 Додадено:** 2025-12-26 23:39
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_09(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_09(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-4, 4, 1], y_range=[-4, 2, 1], axis_config={"color": BLACK})
        
        # Parabola for a=0 (y = -0.5x^2 - 0.5)
        graph = axes.plot(lambda x: -0.5*x**2 - 0.5, color=RED)
        label = MathTex("D < 0", color=RED).next_to(graph, DOWN)
        
        # X-axis highlight
        xaxis = Line(axes.c2p(-4, 0), axes.c2p(4, 0), color=BLUE, stroke_width=4)
        
        title = MathTex("-0.5x^2 + ax - 0.5 = 0", color=BLACK).to_corner(UL)
        
        self.add(axes, graph, label, xaxis, title)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_11 - Дефинициона област на функција
**📅 Додадено:** 2025-12-26 23:39
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_11(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_11(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        number_line = NumberLine(
            x_range=[0, 10, 1],
            length=10,
            color=BLACK,
            include_numbers=True
        )
        
        # Condition x >= 6
        line1 = Line(number_line.n2p(6), number_line.n2p(10), color=BLUE, stroke_width=6).shift(UP*0.2)
        lbl1 = MathTex("x \\ge 6", color=BLUE).next_to(number_line.n2p(6), UP*2)
        
        # Condition x <= 8
        line2 = Line(number_line.n2p(0), number_line.n2p(8), color=RED, stroke_width=6).shift(DOWN*0.2)
        lbl2 = MathTex("x \\le 8", color=RED).next_to(number_line.n2p(8), DOWN*2)
        
        # Intersection
        inter = Line(number_line.n2p(6), number_line.n2p(8), color=GREEN, stroke_width=10)
        
        self.add(number_line, line1, lbl1, line2, lbl2, inter)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_12 - Најмала вредност на функција
**📅 Додадено:** 2025-12-26 23:39
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_12(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_12(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-2, 4, 1], y_range=[-12, 2, 2], axis_config={"color": BLACK})
        
        # Function y = -x^2 + 4x - 5
        graph = axes.plot(lambda x: -x**2 + 4*x - 5, color=BLUE)
        
        # Interval [-1, 3]
        p1 = Dot(axes.c2p(-1, -10), color=RED)
        lbl1 = MathTex("(-1, -10)", color=RED).next_to(p1, LEFT)
        
        p2 = Dot(axes.c2p(3, -2), color=RED)
        lbl2 = MathTex("(3, -2)", color=RED).next_to(p2, RIGHT)
        
        # Vertex
        v = Dot(axes.c2p(2, -1), color=GREEN)
        lbl_v = MathTex("Max", color=GREEN).next_to(v, UP)
        
        self.add(axes, graph, p1, lbl1, p2, lbl2, v, lbl_v)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_13 - Множества (Математика и Економија)
**📅 Додадено:** 2025-12-26 23:41
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_13(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_13(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Sets
        c1 = Circle(radius=1.5, color=BLUE, fill_opacity=0.1).shift(LEFT*0.8)
        c2 = Circle(radius=1.5, color=RED, fill_opacity=0.1).shift(RIGHT*0.8)
        
        # Labels
        t1 = MathTex("M (55)", color=BLUE).next_to(c1, UL)
        t2 = MathTex("E (40)", color=RED).next_to(c2, UR)
        t_inter = MathTex("30", color=BLACK).move_to(ORIGIN)
        
        # Universe box
        rect = Rectangle(width=7, height=5, color=BLACK)
        t_u = MathTex("U = 75", color=BLACK).to_corner(UL)
        t_none = MathTex("None = 10", color=GRAY).to_corner(DR)
        
        self.add(rect, c1, c2, t1, t2, t_inter, t_u, t_none)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_14 - Позиција на точки во однос на права
**📅 Додадено:** 2025-12-26 23:41
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_14(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_14(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-1, 3, 1], y_range=[-2, 5, 1], axis_config={"color": BLACK})
        
        # Line y = 2.82x - 2.23
        line = axes.plot(lambda x: 2.828*x - 2.236, color=BLUE)
        
        # Points
        pt_A = Dot(axes.c2p(1, 0), color=RED)
        lbl_A = MathTex("A", color=RED).next_to(pt_A, DOWN)
        
        pt_B = Dot(axes.c2p(2, 3.5), color=GREEN)
        lbl_B = MathTex("B", color=GREEN).next_to(pt_B, UP)
        
        # Dashed lines
        val_A = 2.828*1 - 2.236
        dash_A = DashedLine(pt_A.get_center(), axes.c2p(1, val_A), color=GRAY)
        
        val_B = 2.828*2 - 2.236
        dash_B = DashedLine(pt_B.get_center(), axes.c2p(2, val_B), color=GRAY)
        
        self.add(axes, line, pt_A, lbl_A, pt_B, lbl_B, dash_A, dash_B)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_16 - Збир на координати на пресек (Виетови формули)
**📅 Додадено:** 2025-12-26 23:41
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_16(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_16(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-6, 2, 1], y_range=[-2, 4, 1], axis_config={"color": BLACK})
        
        # Coefficients
        a = 2.646 - 2.236 # approx 0.41
        b = 2
        c = -a
        
        # Graph
        graph = axes.plot(lambda x: a*x**2 + b*x + c, color=BLUE)
        
        # Roots (approx -5.something and something)
        # Sum is approx -4.88
        
        lbl = MathTex("x_1 + x_2 = -\\sqrt{7} - \\sqrt{5}", color=BLACK).to_corner(UR)
        
        self.add(axes, graph, lbl)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_20 - Пресек на прави со децимални коефициенти
**📅 Додадено:** 2025-12-26 23:47
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_20(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_20(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        axes = Axes(
            x_range=[-5, 2, 1],
            y_range=[-1, 7, 1],
            axis_config={"color": BLACK, "include_numbers": True}
        )
        
        # Lines
        # y = -12/13 x + 29/13 approx -0.92x + 2.23
        line1 = axes.plot(lambda x: -0.923*x + 2.23, color=BLUE)
        
        # y = -13/12 x + 1.75 approx -1.08x + 1.75
        line2 = axes.plot(lambda x: -1.083*x + 1.75, color=GREEN)
        
        # Intersection Point (-3, 5)
        dot = Dot(axes.c2p(-3, 5), color=RED)
        
        label = MathTex("P(-3, 5)", color=RED).next_to(dot, UR)
        sum_label = MathTex("x+y=2", color=BLACK).to_corner(UR)

        self.add(axes, line1, line2, dot, label, sum_label)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_20 - Пресек на прави со децимални коефициенти
**📅 Додадено:** 2025-12-26 23:51
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_20(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_20(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        axes = Axes(
            x_range=[-5, 2, 1],
            y_range=[-1, 7, 1],
            axis_config={"color": BLACK, "include_numbers": True}
        )
        
        # Lines
        # y = -12/13 x + 29/13 approx -0.92x + 2.23
        line1 = axes.plot(lambda x: -0.923*x + 2.23, color=BLUE)
        
        # y = -13/12 x + 1.75 approx -1.08x + 1.75
        line2 = axes.plot(lambda x: -1.083*x + 1.75, color=GREEN)
        
        # Intersection Point (-3, 5)
        dot = Dot(axes.c2p(-3, 5), color=RED)
        
        label = MathTex("P(-3, 5)", color=RED).next_to(dot, UR)
        sum_label = MathTex("x+y=2", color=BLACK).to_corner(UR)

        self.add(axes, line1, line2, dot, label, sum_label)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_05 - Равенка на права низ две точки
**📅 Додадено:** 2025-12-26 23:51
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_05(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_05(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-1, 4, 1], y_range=[-4, 2, 1], axis_config={"color": BLACK})
        
        # Points
        p1 = Dot(axes.c2p(2, 0), color=RED)
        lbl1 = MathTex("(2, 0)", color=RED).next_to(p1, UP)
        
        p2 = Dot(axes.c2p(0, -3), color=RED)
        lbl2 = MathTex("(0, -3)", color=RED).next_to(p2, RIGHT)
        
        # Line
        line = axes.plot(lambda x: 1.5*x - 3, color=BLUE)
        eq = MathTex("y = 1.5x - 3", color=BLUE).to_corner(UL)
        
        self.add(axes, p1, lbl1, p2, lbl2, line, eq)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_08 - Тежишна линија кон хипотенузата
**📅 Додадено:** 2025-12-26 23:51
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_08(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_08(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Triangle vertices (6, 8, 10 scaled down by 2 for view)
        A = ORIGIN
        B = RIGHT * 4  # represents 8
        C = UP * 3     # represents 6
        
        triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
        
        # Midpoint of hypotenuse BC
        M = (B + C) / 2
        median = Line(A, M, color=RED, stroke_width=4)
        
        # Labels
        lbl_a = MathTex("6", color=BLACK).next_to(Line(A, C), LEFT)
        lbl_b = MathTex("8", color=BLACK).next_to(Line(A, B), DOWN)
        lbl_c = MathTex("c=10", color=BLACK).next_to(Line(B, C), UR)
        lbl_m = MathTex("m_c = ?", color=RED).next_to(median, RIGHT, buff=0.1)
        
        # Right angle symbol
        ra = RightAngle(Line(A, B), Line(A, C), length=0.4, color=BLACK)
        
        self.add(triangle, median, lbl_a, lbl_b, lbl_c, lbl_m, ra)
        # --- AI GENERATED CODE END ---

```
---
