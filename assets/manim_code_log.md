
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

### 🆔 Задача: cnt92_v2_24 - Минимален периметар на паралелограм
**📅 Додадено:** 2025-12-26 23:59
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_24(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_24(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Rhombus a=b=5. Scaled down for view.
        # Area = 25. Side = 5.
        side = 3 # visual scale
        angle = 30 * DEGREES
        
        p1 = ORIGIN
        p2 = RIGHT * side
        p3 = p2 + np.array([side * np.cos(angle), side * np.sin(angle), 0])
        p4 = p1 + np.array([side * np.cos(angle), side * np.sin(angle), 0])
        
        shape = Polygon(p1, p2, p3, p4, color=BLUE, stroke_width=4)
        
        lbl_a = MathTex("a", color=BLACK).next_to(Line(p1, p2), DOWN)
        lbl_b = MathTex("b", color=BLACK).next_to(Line(p2, p3), RIGHT)
        lbl_ang = MathTex("30^\circ", color=RED).next_to(p1, UR, buff=0.1)
        
        txt_area = MathTex("S = ab \\sin 30^\circ = 12.5", color=BLACK).to_corner(UL)
        txt_res = MathTex("ab = 25 \\implies P_{min} = 20", color=RED).next_to(txt_area, DOWN)
        
        self.add(shape, lbl_a, lbl_b, lbl_ang, txt_area, txt_res)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_26 - Систем равенки со параметар
**📅 Додадено:** 2025-12-26 23:59
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_26(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_26(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-4, 4, 1], y_range=[-1, 4, 1], axis_config={"color": BLACK})
        
        # Piecewise function
        # x < -2, y = 0
        seg1 = Line(axes.c2p(-4, 0), axes.c2p(-2, 0), color=BLUE, stroke_width=4)
        # -2 < x < 0, y = 2
        seg2 = Line(axes.c2p(-2, 2), axes.c2p(0, 2), color=BLUE, stroke_width=4)
        # x > 0, y = 0
        seg3 = Line(axes.c2p(0, 0), axes.c2p(4, 0), color=BLUE, stroke_width=4)
        
        # Holes
        holes = VGroup(
            Circle(radius=0.08, color=BLUE, fill_color=WHITE, fill_opacity=1).move_to(axes.c2p(-2, 0)),
            Circle(radius=0.08, color=BLUE, fill_color=WHITE, fill_opacity=1).move_to(axes.c2p(-2, 2)),
            Circle(radius=0.08, color=BLUE, fill_color=WHITE, fill_opacity=1).move_to(axes.c2p(0, 2)),
            Circle(radius=0.08, color=BLUE, fill_color=WHITE, fill_opacity=1).move_to(axes.c2p(0, 0))
        )
        
        # Line y = -1x + 1 (example for k < -0.5)
        line = axes.plot(lambda x: -1*x + 1, color=RED)
        lbl = MathTex("k < -0.5", color=RED).to_corner(UR)
        
        self.add(axes, seg1, seg2, seg3, holes, line, lbl)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_27 - Бесконечно многу решенија (Модули)
**📅 Додадено:** 2025-12-26 23:59
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_27(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_27(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        nl = NumberLine(x_range=[-3, 3, 1], length=8, color=BLACK, include_numbers=True)
        
        p1 = Dot(nl.n2p(-1.732), color=BLUE)
        l1 = MathTex("-\\sqrt{3}", color=BLUE).next_to(p1, DOWN)
        
        p2 = Dot(nl.n2p(1.414), color=BLUE)
        l2 = MathTex("\\sqrt{2}", color=BLUE).next_to(p2, DOWN)
        
        seg = Line(p1.get_center(), p2.get_center(), color=RED, stroke_width=6)
        lbl = MathTex("a = \\sqrt{2}+\\sqrt{3}", color=RED).next_to(seg, UP)
        
        self.add(nl, p1, l1, p2, l2, seg, lbl)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: cnt92_v2_29 - Параметар и Signum функција
**📅 Додадено:** 2025-12-27 00:04
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_cnt92_v2_29(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_29(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        number_line = NumberLine(
            x_range=[-2, 4, 1],
            length=10,
            color=BLACK,
            include_numbers=True
        )
        
        # Active zone (-1, 3)
        zone = Line(
            number_line.n2p(-1),
            number_line.n2p(3),
            color=GREEN,
            stroke_width=8
        )
        lbl_zone = MathTex("u(x) < 0", color=GREEN).next_to(zone, UP)
        
        # Parameter range (0, 2)
        param_range = Line(
            number_line.n2p(0),
            number_line.n2p(2),
            color=BLUE,
            stroke_width=8
        ).shift(DOWN * 0.5)
        lbl_param = MathTex("a \\in (0, 2)", color=BLUE).next_to(param_range, DOWN)
        
        self.add(number_line, zone, lbl_zone, param_range, lbl_param)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_y1_3ab - Однос на плоштини во кружница
**📅 Додадено:** 2025-12-27 00:21
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_y1_3ab(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_y1_3ab(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Setup
        R = 3
        O = ORIGIN
        circle = Circle(radius=R, color=BLACK)
        
        # Points A, B (Diameter)
        A = LEFT * R
        B = RIGHT * R
        
        # Point C (2AC = CB => AC = 2/3 R)
        # A is at -3. C should be at -3 + 2 = -1.
        C = LEFT * 1
        
        # Point D (DC perp AB)
        # x = -1. y = sqrt(9 - 1) = sqrt(8) approx 2.82
        D = np.array([-1, np.sqrt(8), 0])
        
        # Point E (DE is diameter => E is symmetric to D wrt O)
        E = -D
        
        # Drawing
        line_AB = Line(A, B, color=BLACK)
        line_DE = Line(D, E, color=BLACK)
        line_DC = Line(D, C, color=BLACK)
        
        # Triangles
        tri_ABD = Polygon(A, B, D, color=BLUE, fill_opacity=0.1)
        tri_CDE = Polygon(C, D, E, color=RED, fill_opacity=0.1)
        
        # Labels
        lbl_A = MathTex("A", color=BLACK).next_to(A, LEFT)
        lbl_B = MathTex("B", color=BLACK).next_to(B, RIGHT)
        lbl_C = MathTex("C", color=BLACK).next_to(C, DOWN)
        lbl_D = MathTex("D", color=BLACK).next_to(D, UP)
        lbl_E = MathTex("E", color=BLACK).next_to(E, DOWN)
        lbl_O = MathTex("O", color=BLACK).next_to(O, DOWN)
        
        self.add(circle, line_AB, line_DE, line_DC)
        self.add(tri_ABD, tri_CDE)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_E, lbl_O)
        
        # Right angle
        ra = RightAngle(Line(C, B), Line(C, D), length=0.3, color=BLACK)
        self.add(ra)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_y2_3ab - Плоштини во триаголник
**📅 Додадено:** 2025-12-27 00:32
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_y2_3ab(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_y2_3ab(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Triangle vertices
        A = UP * 3 + LEFT * 1
        B = DOWN * 2 + LEFT * 3
        C = DOWN * 2 + RIGHT * 3
        
        # Point D (approximate to satisfy areas)
        # AD:DA1 = 2:1, BD:DB1 = 7:2
        # Let's just place D visually inside
        D = ORIGIN
        
        # Intersections
        # A1 is on BC. Line AD intersects BC.
        # B1 is on AC. Line BD intersects AC.
        
        # Helper to find intersection
        def intersect(p1, p2, p3, p4):
            x1, y1 = p1[:2]
            x2, y2 = p2[:2]
            x3, y3 = p3[:2]
            x4, y4 = p4[:2]
            denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
            ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / denom
            return p1 + ua * (p2-p1)

        A1 = intersect(A, D, B, C)
        B1 = intersect(B, D, A, C)
        
        # Draw
        tri = Polygon(A, B, C, color=BLACK, stroke_width=4)
        line_AA1 = Line(A, A1, color=BLUE)
        line_BB1 = Line(B, B1, color=BLUE)
        
        # Labels
        lbl_A = MathTex("A", color=BLACK).next_to(A, UP)
        lbl_B = MathTex("B", color=BLACK).next_to(B, DL)
        lbl_C = MathTex("C", color=BLACK).next_to(C, DR)
        lbl_D = MathTex("D", color=BLACK).next_to(D, UR)
        lbl_A1 = MathTex("A_1", color=BLACK).next_to(A1, DOWN)
        lbl_B1 = MathTex("B_1", color=BLACK).next_to(B1, RIGHT)
        
        # Areas text
        t1 = MathTex("14", color=RED).move_to((A+B+D)/3)
        t2 = MathTex("4", color=RED).move_to((A+B1+D)/3)
        t3 = MathTex("7", color=RED).move_to((B+A1+D)/3)
        
        self.add(tri, line_AA1, line_BB1)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_A1, lbl_B1)
        self.add(t1, t2, t3)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_y2_4a - Параметарска равенка со модули
**📅 Додадено:** 2025-12-27 00:32
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_y2_4a(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_y2_4a(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-3, 3, 1], y_range=[-1, 5, 1], axis_config={"color": BLACK})
        
        # Example a = 0.5
        a = 0.5
        
        # Function f(x) = 2|x-0.5| + 3|x+0.5|
        def func(x):
            return 2*abs(x-a) + 3*abs(x+a)
            
        graph = axes.plot(func, color=BLUE)
        
        # Minimum point at x = -a = -0.5
        # y = 4a = 2
        min_pt = Dot(axes.c2p(-a, 4*a), color=RED)
        lbl_min = MathTex("Min = 4a", color=RED).next_to(min_pt, DOWN)
        
        # Line y = 1
        line_1 = axes.plot(lambda x: 1, color=GREEN)
        lbl_1 = MathTex("y=1", color=GREEN).next_to(line_1, LEFT)
        
        self.add(axes, graph, min_pt, lbl_min, line_1, lbl_1)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_y3_3a - Екстреми на функција со ограничен домен
**📅 Додадено:** 2025-12-27 00:42
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_y3_3a(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_y3_3a(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-4, 4, 1], y_range=[-2, 15, 2], axis_config={"color": BLACK})
        
        # Function
        func = axes.plot(lambda x: x**2 - 2*x - 1, color=GRAY, stroke_opacity=0.5)
        
        # Domain segments
        seg1 = axes.plot(lambda x: x**2 - 2*x - 1, x_range=[-3, -2], color=BLUE, stroke_width=4)
        seg2 = axes.plot(lambda x: x**2 - 2*x - 1, x_range=[2, 3], color=BLUE, stroke_width=4)
        
        # Points
        p_min = Dot(axes.c2p(2, -1), color=RED)
        lbl_min = MathTex("min(-1)", color=RED).next_to(p_min, DOWN)
        
        p_max = Dot(axes.c2p(-3, 14), color=RED)
        lbl_max = MathTex("MAX(14)", color=RED).next_to(p_max, UP)
        
        # Vertex (not in domain)
        v = Dot(axes.c2p(1, -2), color=BLACK)
        lbl_v = MathTex("V(1, -2)", color=BLACK).next_to(v, DOWN)
        
        self.add(axes, func, seg1, seg2, p_min, lbl_min, p_max, lbl_max, v, lbl_v)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_y3_4a - Конус и впишана топка
**📅 Додадено:** 2025-12-27 00:42
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_y3_4a(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_y3_4a(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Cross section: Isosceles triangle with inscribed circle
        # s = 3r. Let r=2, then s=6. h = sqrt(36-4) = sqrt(32) approx 5.65
        r = 2
        h = np.sqrt(32)
        
        A = LEFT * r + DOWN * 2
        B = RIGHT * r + DOWN * 2
        C = UP * (h - 2)
        
        triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
        
        # Incenter calculation
        # For isosceles, incenter is on y-axis.
        # R = rh / (s+r) = 2*5.65 / 8 = 1.41
        R = r * h / (6 + r)
        incenter = DOWN * (2 - R)
        circle = Circle(radius=R, color=BLUE).move_to(incenter)
        
        # Labels
        lbl_r = MathTex("r", color=BLACK).next_to(Line(incenter + DOWN*R, B), DOWN)
        lbl_s = MathTex("s", color=BLACK).next_to(Line(B, C), RIGHT)
        lbl_h = MathTex("h", color=BLACK).next_to(Line(incenter, C), LEFT)
        
        # Formula
        txt = MathTex("\\frac{M}{B} = \\frac{s}{r} = 3", color=RED).to_corner(UL)
        
        self.add(triangle, circle, lbl_r, lbl_s, lbl_h, txt)
        
        # Height line
        hline = DashedLine(C, DOWN*2, color=GRAY)
        self.add(hline)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_y4_4a - Агол во триаголник
**📅 Додадено:** 2025-12-27 01:18
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_y4_4a(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_y4_4a(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Triangle with beta = 30 deg
        # Sides in AP. Let b=1. Then a+c=2.
        # Cos rule: 1 = a^2 + c^2 - 2ac cos(30)
        # 1 = (a+c)^2 - 2ac - ac sqrt(3)
        # 1 = 4 - ac(2 + sqrt(3))
        # ac = 3 / (2 + sqrt(3)) = 3(2-sqrt(3)) = 6 - 3sqrt(3) approx 0.8
        # a, c are roots of x^2 - 2x + 0.8 = 0
        # D = 4 - 3.2 = 0.8. x = (2 +/- 0.9)/2. a=0.55, c=1.45
        
        A = ORIGIN
        c_len = 1.45
        a_len = 0.55
        b_len = 1
        
        B = RIGHT * c_len
        # C is at distance b from A and a from B
        # Using law of cosines to find coords
        # b^2 = c^2 + a^2 - 2ac cos(beta) -> beta is at B?
        # No, beta is opposite b (at B). Wait, standard notation beta is at B.
        # So angle at B is 30.
        
        C = B + np.array([-a_len * np.cos(30*DEGREES), a_len * np.sin(30*DEGREES), 0])
        
        tri = Polygon(A, B, C, color=BLACK, stroke_width=4)
        
        lbl_B = MathTex("\\beta = 30^\circ", color=RED).next_to(B, DL, buff=0.1)
        arc = Angle(Line(B, C), Line(B, A), radius=0.4, color=RED)
        
        txt = MathTex("a, b, c \\in A.P.", color=BLUE).to_corner(UL)
        txt2 = MathTex("r = R(1 - \\cos \\beta)", color=BLACK).next_to(txt, DOWN)
        
        self.add(tri, lbl_B, arc, txt, txt2)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_g4_1 - Броење правоаголници
**📅 Додадено:** 2025-12-27 01:21
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_g4_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_g4_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Define vertices for the grid
        # Main square 2x2
        A, B, C, D = UL*2, UR*2, DR*2, DL*2
        M_AB, M_BC, M_CD, M_DA = UP*2, RIGHT*2, DOWN*2, LEFT*2
        Center = ORIGIN
        
        # Draw the base figure
        lines = VGroup(
            Line(A, B), Line(B, C), Line(C, D), Line(D, A), # Outer
            Line(M_AB, M_CD), Line(M_DA, M_BC), # Cross
            Line(A, C), Line(B, D), # Diagonals
            Line(M_AB, M_BC), Line(M_BC, M_CD), Line(M_CD, M_DA), Line(M_DA, M_AB) # Inner Diamond
        ).set_color(BLACK).set_stroke(width=2)
        
        self.add(lines)
        
        # Highlight examples
        # 1. Large Vertical Rectangle
        rect1 = Polygon(M_AB+LEFT, M_AB+RIGHT, M_CD+RIGHT, M_CD+LEFT, color=BLUE, fill_opacity=0.3)
        lbl1 = Text("Големи (2)", color=BLUE, font_size=24).next_to(rect1, UP)
        
        self.play(FadeIn(rect1), Write(lbl1))
        self.wait(1)
        self.play(FadeOut(rect1), FadeOut(lbl1))
        
        # 2. Small Rectangle (corner)
        rect2 = Polygon(A, M_AB, Center, M_DA, color=GREEN, fill_opacity=0.3)
        lbl2 = Text("Помали (4)", color=GREEN, font_size=24).next_to(rect2, UL)
        
        self.play(FadeIn(rect2), Write(lbl2))
        self.wait(1)
        self.play(FadeOut(rect2), FadeOut(lbl2))
        
        # 3. Slanted Rectangle
        rect3 = Polygon(M_AB, B, M_BC, Center, color=RED, fill_opacity=0.3)
        lbl3 = Text("Коси (4)", color=RED, font_size=24).next_to(rect3, UR)
        
        self.play(FadeIn(rect3), Write(lbl3))
        self.wait(1)
        self.play(FadeOut(rect3), FadeOut(lbl3))
        
        self.add(lines)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_g5_2 - Коцка и проценти
**📅 Додадено:** 2025-12-27 01:25
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_g5_2(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_g5_2(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Draw a 5x5 grid representing the front face
        grid = VGroup()
        for i in range(5):
            for j in range(5):
                sq = Square(side_length=1, color=BLACK, fill_opacity=0)
                sq.move_to(RIGHT*(i-2) + UP*(j-2))
                grid.add(sq)
        
        # Highlight the removed cubes (assuming full layer for visual simplicity as per count 25)
        # Or just show the calculation
        
        cube_text = Text("Вкупно: 5 x 5 x 5 = 125", color=BLACK).to_edge(UP)
        removed_text = Text("Отстранети: 25", color=RED).next_to(cube_text, DOWN)
        percent_text = MathTex("\\frac{25}{125} = \\frac{1}{5} = 20\\%", color=BLUE).next_to(removed_text, DOWN)
        
        self.add(grid, cube_text)
        self.play(grid.animate.set_fill(RED, opacity=0.5), Write(removed_text))
        self.wait(1)
        self.play(Write(percent_text))
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_g5_4 - Лука и Јован на скали
**📅 Додадено:** 2025-12-27 01:25
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_g5_4(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_g5_4(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Stairs
        step_height = 0.5
        step_width = 0.5
        stairs = VGroup()
        for i in range(10):
            stairs.add(Line(start=RIGHT*i*step_width + UP*i*step_height, end=RIGHT*(i+1)*step_width + UP*i*step_height, color=BLACK))
            stairs.add(Line(start=RIGHT*(i+1)*step_width + UP*i*step_height, end=RIGHT*(i+1)*step_width + UP*(i+1)*step_height, color=BLACK))
        
        # Luka at step 3
        luka_x = 3.5 * step_width
        luka_base_y = 3 * step_height
        luka = Rectangle(height=3, width=0.5, color=BLUE).move_to(RIGHT*luka_x + UP*(luka_base_y + 1.5))
        lbl_luka = Text("Лука", color=BLUE, font_size=20).next_to(luka, UP)
        
        # Jovan at step 9
        jovan_x = 9.5 * step_width
        jovan_base_y = 9 * step_height
        jovan = Rectangle(height=2.5, width=0.5, color=GREEN).move_to(RIGHT*jovan_x + UP*(jovan_base_y + 1.25))
        lbl_jovan = Text("Јован", color=GREEN, font_size=20).next_to(jovan, UP)
        
        self.add(stairs, luka, lbl_luka, jovan, lbl_jovan)
        
        # Height lines
        line1 = DashedLine(start=LEFT, end=RIGHT*10, color=GRAY).shift(UP*(luka_base_y + 3))
        lbl1 = MathTex("200", color=BLACK).next_to(line1, LEFT)
        
        self.add(line1, lbl1)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_g6_3 - Периметар со симетрала
**📅 Додадено:** 2025-12-27 01:29
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_g6_3(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_g6_3(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Coordinates
        A = LEFT * 3 + DOWN * 1
        B = RIGHT * 2 + UP * 2
        C = RIGHT * 3 + DOWN * 1
        
        # Perpendicular bisector of AC
        # Midpoint of AC
        M = (A + C) / 2
        # Bisector is vertical line x=0 (since A and C have same y)
        bisector = Line(M + UP*4, M + DOWN*1, color=GRAY, stroke_width=2)
        
        # Intersection Q with AB
        # Line AB equation... let's just calculate intersection visually or geometrically
        # For visualization, let's place Q on AB such that QA=QC
        # Since bisector is x=0, Q must be at x=0 on line AB.
        # A=(-3, -1), B=(2, 2). Line: y - (-1) = (3/5)(x - (-3)) => y = 0.6x + 1.8 - 1 = 0.6x + 0.8
        # If x=0, y=0.8. So Q=(0, 0.8)
        Q = UP * 0.8
        
        # Draw Triangle ABC
        tri = Polygon(A, B, C, color=BLACK, stroke_width=4)
        
        # Draw segments
        line_QC = Line(Q, C, color=RED, stroke_width=4)
        line_QA = Line(Q, A, color=RED, stroke_width=4)
        
        # Labels
        lbl_A = MathTex("A", color=BLACK).next_to(A, DL)
        lbl_B = MathTex("B", color=BLACK).next_to(B, UP)
        lbl_C = MathTex("C", color=BLACK).next_to(C, DR)
        lbl_Q = MathTex("Q", color=BLACK).next_to(Q, UL)
        
        # Equality marks
        mark1 = DashedLine(Q, A, color=RED)
        mark2 = DashedLine(Q, C, color=RED)
        
        txt = MathTex("QA = QC", color=RED).to_corner(UL)
        
        self.add(tri, bisector, line_QC, lbl_A, lbl_B, lbl_C, lbl_Q, txt)
        self.play(Indicate(line_QA), Indicate(line_QC))
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_g6_4 - Агли во четириаголник
**📅 Додадено:** 2025-12-27 01:29
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_g6_4(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_g6_4(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Arbitrary angles satisfying 2a+2b=80. Let 2a=40, 2b=40 => a=20, b=20.
        # Small triangle angles: 40, 40, 100.
        # Large quad angles: 80, 80, 150, x=50.
        
        # Vertices approximation
        A = DL * 2
        B = DR * 2
        # Inner point P such that PAB is 40, PBA is 40.
        # Intersection of rays.
        P = UP * 0.5 # approx
        
        # Outer points D, C
        # Angle at A is 80. Angle at B is 80.
        D = A + UP * 3 + LEFT * 0.5
        C = B + UP * 3 + RIGHT * 0.5
        
        # Draw shapes
        quad = Polygon(A, B, C, D, color=BLACK, stroke_width=4)
        tri_lines = VGroup(Line(A, P), Line(B, P)).set_color(BLUE)
        
        # Labels
        lbl_100 = MathTex("100^\circ", color=BLUE, font_size=24).next_to(P, UP, buff=0.1)
        lbl_150 = MathTex("150^\circ", color=BLACK, font_size=24).next_to(D, UP)
        lbl_x = MathTex("x", color=RED).next_to(C, UP)
        
        lbl_2a = MathTex("2\\alpha", color=BLUE, font_size=20).move_to(A + UR*0.5)
        lbl_2b = MathTex("2\\beta", color=BLUE, font_size=20).move_to(B + UL*0.5)
        
        lbl_4a = MathTex("4\\alpha", color=BLACK, font_size=24).next_to(A, LEFT)
        lbl_4b = MathTex("4\\beta", color=BLACK, font_size=24).next_to(B, RIGHT)
        
        self.add(quad, tri_lines)
        self.add(lbl_100, lbl_150, lbl_x, lbl_2a, lbl_2b, lbl_4a, lbl_4b)
        
        # Equation
        eq = MathTex("2\\alpha + 2\\beta = 80^\circ \\implies 4\\alpha + 4\\beta = 160^\circ", color=RED).to_edge(UP)
        self.add(eq)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_g6_3 - Периметар со симетрала
**📅 Додадено:** 2025-12-27 01:37
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_g6_3(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_g6_3(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Coordinates
        A = LEFT * 3 + DOWN * 1
        B = RIGHT * 2 + UP * 2
        C = RIGHT * 3 + DOWN * 1
        
        # Perpendicular bisector of AC
        # Midpoint of AC
        M = (A + C) / 2
        # Bisector is vertical line x=0 (since A and C have same y)
        bisector = Line(M + UP*4, M + DOWN*1, color=GRAY, stroke_width=2)
        
        # Intersection Q with AB
        # Line AB equation... let's just calculate intersection visually or geometrically
        # For visualization, let's place Q on AB such that QA=QC
        # Since bisector is x=0, Q must be at x=0 on line AB.
        # A=(-3, -1), B=(2, 2). Line: y - (-1) = (3/5)(x - (-3)) => y = 0.6x + 1.8 - 1 = 0.6x + 0.8
        # If x=0, y=0.8. So Q=(0, 0.8)
        Q = UP * 0.8
        
        # Draw Triangle ABC
        tri = Polygon(A, B, C, color=BLACK, stroke_width=4)
        
        # Draw segments
        line_QC = Line(Q, C, color=RED, stroke_width=4)
        line_QA = Line(Q, A, color=RED, stroke_width=4)
        
        # Labels
        lbl_A = MathTex("A", color=BLACK).next_to(A, DL)
        lbl_B = MathTex("B", color=BLACK).next_to(B, UP)
        lbl_C = MathTex("C", color=BLACK).next_to(C, DR)
        lbl_Q = MathTex("Q", color=BLACK).next_to(Q, UL)
        
        # Equality marks
        mark1 = DashedLine(Q, A, color=RED)
        mark2 = DashedLine(Q, C, color=RED)
        
        txt = MathTex("QA = QC", color=RED).to_corner(UL)
        
        self.add(tri, bisector, line_QC, lbl_A, lbl_B, lbl_C, lbl_Q, txt)
        self.play(Indicate(line_QA), Indicate(line_QC))
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_g6_4 - Агли во четириаголник
**📅 Додадено:** 2025-12-27 01:37
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_g6_4(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_g6_4(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Arbitrary angles satisfying 2a+2b=80. Let 2a=40, 2b=40 => a=20, b=20.
        # Small triangle angles: 40, 40, 100.
        # Large quad angles: 80, 80, 150, x=50.
        
        # Vertices approximation
        A = DL * 2
        B = DR * 2
        # Inner point P such that PAB is 40, PBA is 40.
        # Intersection of rays.
        P = UP * 0.5 # approx
        
        # Outer points D, C
        # Angle at A is 80. Angle at B is 80.
        D = A + UP * 3 + LEFT * 0.5
        C = B + UP * 3 + RIGHT * 0.5
        
        # Draw shapes
        quad = Polygon(A, B, C, D, color=BLACK, stroke_width=4)
        tri_lines = VGroup(Line(A, P), Line(B, P)).set_color(BLUE)
        
        # Labels
        lbl_100 = MathTex("100^\circ", color=BLUE, font_size=24).next_to(P, UP, buff=0.1)
        lbl_150 = MathTex("150^\circ", color=BLACK, font_size=24).next_to(D, UP)
        lbl_x = MathTex("x", color=RED).next_to(C, UP)
        
        lbl_2a = MathTex("2\\alpha", color=BLUE, font_size=20).move_to(A + UR*0.5)
        lbl_2b = MathTex("2\\beta", color=BLUE, font_size=20).move_to(B + UL*0.5)
        
        lbl_4a = MathTex("4\\alpha", color=BLACK, font_size=24).next_to(A, LEFT)
        lbl_4b = MathTex("4\\beta", color=BLACK, font_size=24).next_to(B, RIGHT)
        
        self.add(quad, tri_lines)
        self.add(lbl_100, lbl_150, lbl_x, lbl_2a, lbl_2b, lbl_4a, lbl_4b)
        
        # Equation
        eq = MathTex("2\\alpha + 2\\beta = 80^\circ \\implies 4\\alpha + 4\\beta = 160^\circ", color=RED).to_edge(UP)
        self.add(eq)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_g6_3 - Периметар со симетрала
**📅 Додадено:** 2025-12-27 01:37
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_g6_3(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_g6_3(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Coordinates
        A = LEFT * 3 + DOWN * 1
        B = RIGHT * 2 + UP * 2
        C = RIGHT * 3 + DOWN * 1
        
        # Perpendicular bisector of AC
        # Midpoint of AC
        M = (A + C) / 2
        # Bisector is vertical line x=0 (since A and C have same y)
        bisector = Line(M + UP*4, M + DOWN*1, color=GRAY, stroke_width=2)
        
        # Intersection Q with AB
        # Line AB equation... let's just calculate intersection visually or geometrically
        # For visualization, let's place Q on AB such that QA=QC
        # Since bisector is x=0, Q must be at x=0 on line AB.
        # A=(-3, -1), B=(2, 2). Line: y - (-1) = (3/5)(x - (-3)) => y = 0.6x + 1.8 - 1 = 0.6x + 0.8
        # If x=0, y=0.8. So Q=(0, 0.8)
        Q = UP * 0.8
        
        # Draw Triangle ABC
        tri = Polygon(A, B, C, color=BLACK, stroke_width=4)
        
        # Draw segments
        line_QC = Line(Q, C, color=RED, stroke_width=4)
        line_QA = Line(Q, A, color=RED, stroke_width=4)
        
        # Labels
        lbl_A = MathTex("A", color=BLACK).next_to(A, DL)
        lbl_B = MathTex("B", color=BLACK).next_to(B, UP)
        lbl_C = MathTex("C", color=BLACK).next_to(C, DR)
        lbl_Q = MathTex("Q", color=BLACK).next_to(Q, UL)
        
        # Equality marks
        mark1 = DashedLine(Q, A, color=RED)
        mark2 = DashedLine(Q, C, color=RED)
        
        txt = MathTex("QA = QC", color=RED).to_corner(UL)
        
        self.add(tri, bisector, line_QC, lbl_A, lbl_B, lbl_C, lbl_Q, txt)
        self.play(Indicate(line_QA), Indicate(line_QC))
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2025_mun_g6_4 - Агли во четириаголник
**📅 Додадено:** 2025-12-27 01:37
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2025_mun_g6_4(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_g6_4(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Arbitrary angles satisfying 2a+2b=80. Let 2a=40, 2b=40 => a=20, b=20.
        # Small triangle angles: 40, 40, 100.
        # Large quad angles: 80, 80, 150, x=50.
        
        # Vertices approximation
        A = DL * 2
        B = DR * 2
        # Inner point P such that PAB is 40, PBA is 40.
        # Intersection of rays.
        P = UP * 0.5 # approx
        
        # Outer points D, C
        # Angle at A is 80. Angle at B is 80.
        D = A + UP * 3 + LEFT * 0.5
        C = B + UP * 3 + RIGHT * 0.5
        
        # Draw shapes
        quad = Polygon(A, B, C, D, color=BLACK, stroke_width=4)
        tri_lines = VGroup(Line(A, P), Line(B, P)).set_color(BLUE)
        
        # Labels
        lbl_100 = MathTex("100^\circ", color=BLUE, font_size=24).next_to(P, UP, buff=0.1)
        lbl_150 = MathTex("150^\circ", color=BLACK, font_size=24).next_to(D, UP)
        lbl_x = MathTex("x", color=RED).next_to(C, UP)
        
        lbl_2a = MathTex("2\\alpha", color=BLUE, font_size=20).move_to(A + UR*0.5)
        lbl_2b = MathTex("2\\beta", color=BLUE, font_size=20).move_to(B + UL*0.5)
        
        lbl_4a = MathTex("4\\alpha", color=BLACK, font_size=24).next_to(A, LEFT)
        lbl_4b = MathTex("4\\beta", color=BLACK, font_size=24).next_to(B, RIGHT)
        
        self.add(quad, tri_lines)
        self.add(lbl_100, lbl_150, lbl_x, lbl_2a, lbl_2b, lbl_4a, lbl_4b)
        
        # Equation
        eq = MathTex("2\\alpha + 2\\beta = 80^\circ \\implies 4\\alpha + 4\\beta = 160^\circ", color=RED).to_edge(UP)
        self.add(eq)
        # --- AI GENERATED CODE END ---

```
---
