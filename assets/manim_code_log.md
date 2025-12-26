
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
