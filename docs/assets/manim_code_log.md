### 🆔 Задача: 2022_mun_y4_19b - Ротација и координати
**📅 Додадено:** 2025-12-28 15:21
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2022_mun_y4_19b(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
        axes = Axes(x_range=[0, 7], y_range=[0, 7], x_length=6, y_length=6)
        
        A = axes.c2p(1, 2)
        A1 = axes.c2p(6, 5)
        B = axes.c2p(1, 4)
        B1 = axes.c2p(4, 5)
        M = axes.c2p(2, 6)
        
        dots = VGroup(Dot(A), Dot(A1), Dot(B), Dot(B1), Dot(M, color=RED))
        labels = VGroup(
            MathTex('A').next_to(A, DL),
            MathTex('A_1').next_to(A1, UR),
            MathTex('B').next_to(B, UL),
            MathTex('B_1').next_to(B1, UR),
            MathTex('M').next_to(M, UP)
        ).set_color(BLACK)
        
        lines = VGroup(
            DashedLine(A, A1, color=GREY),
            DashedLine(B, B1, color=GREY),
            Line(M, A, color=BLUE, stroke_opacity=0.5),
            Line(M, A1, color=BLUE, stroke_opacity=0.5)
        )

        self.add(axes, dots, labels, lines)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2022_mun_y4_19b - Ротација и координати
**📅 Додадено:** 2025-12-28 16:40
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2022_mun_y4_19b(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
        axes = Axes(x_range=[0, 7], y_range=[0, 7], x_length=6, y_length=6)
        
        A = axes.c2p(1, 2)
        A1 = axes.c2p(6, 5)
        B = axes.c2p(1, 4)
        B1 = axes.c2p(4, 5)
        M = axes.c2p(2, 6)
        
        dots = VGroup(Dot(A), Dot(A1), Dot(B), Dot(B1), Dot(M, color=RED))
        labels = VGroup(
            MathTex('A').next_to(A, DL),
            MathTex('A_1').next_to(A1, UR),
            MathTex('B').next_to(B, UL),
            MathTex('B_1').next_to(B1, UR),
            MathTex('M').next_to(M, UP)
        ).set_color(BLACK)
        
        lines = VGroup(
            DashedLine(A, A1, color=GREY),
            DashedLine(B, B1, color=GREY),
            Line(M, A, color=BLUE, stroke_opacity=0.5),
            Line(M, A1, color=BLUE, stroke_opacity=0.5)
        )

        self.add(axes, dots, labels, lines)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2022_mun_y4_19b - Ротација и координати
**📅 Додадено:** 2025-12-28 16:40
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2022_mun_y4_19b(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
        axes = Axes(x_range=[0, 7], y_range=[0, 7], x_length=6, y_length=6)
        
        A = axes.c2p(1, 2)
        A1 = axes.c2p(6, 5)
        B = axes.c2p(1, 4)
        B1 = axes.c2p(4, 5)
        M = axes.c2p(2, 6)
        
        dots = VGroup(Dot(A), Dot(A1), Dot(B), Dot(B1), Dot(M, color=RED))
        labels = VGroup(
            MathTex('A').next_to(A, DL),
            MathTex('A_1').next_to(A1, UR),
            MathTex('B').next_to(B, UL),
            MathTex('B_1').next_to(B1, UR),
            MathTex('M').next_to(M, UP)
        ).set_color(BLACK)
        
        lines = VGroup(
            DashedLine(A, A1, color=GREY),
            DashedLine(B, B1, color=GREY),
            Line(M, A, color=BLUE, stroke_opacity=0.5),
            Line(M, A1, color=BLUE, stroke_opacity=0.5)
        )

        self.add(axes, dots, labels, lines)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: test_001 - Тест Задача за Триаголник
**📅 Додадено:** 2025-12-28 16:41
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_test_001(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class TestScene(Scene): def construct(self): self.add(Circle())
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: test_001 - Тест Задача за Триаголник
**📅 Додадено:** 2025-12-28 17:07
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_test_001(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class TestScene(Scene): def construct(self): self.add(Circle())
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: test_001 - Тест Задача за Триаголник
**📅 Додадено:** 2025-12-28 17:07
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_test_001(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class TestScene(Scene): def construct(self): self.add(Circle())
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: test_001 - Тест Задача за Триаголник
**📅 Додадено:** 2025-12-28 17:13
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_test_001(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
        A = [-2, -1, 0]
        B = [2, -1, 0]
        C = [0, 2, 0]
        triangle = Polygon(A, B, C, color=BLUE)
        labels = VGroup(
            Text("A").next_to(A, DL),
            Text("B").next_to(B, DR),
            Text("C").next_to(C, UP)
        )
        self.add(triangle, labels)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: 2022_mun_y4_19b - Ротација и координати
**📅 Додадено:** 2025-12-28 17:17
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_2022_mun_y4_19b(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
        axes = Axes(x_range=[0, 7], y_range=[0, 7], x_length=6, y_length=6)
        
        A = axes.c2p(1, 2)
        A1 = axes.c2p(6, 5)
        B = axes.c2p(1, 4)
        B1 = axes.c2p(4, 5)
        M = axes.c2p(2, 6)
        
        dots = VGroup(Dot(A), Dot(A1), Dot(B), Dot(B1), Dot(M, color=RED))
        labels = VGroup(
            MathTex('A').next_to(A, DL),
            MathTex('A_1').next_to(A1, UR),
            MathTex('B').next_to(B, UL),
            MathTex('B_1').next_to(B1, UR),
            MathTex('M').next_to(M, UP)
        ).set_color(BLACK)
        
        lines = VGroup(
            DashedLine(A, A1, color=GREY),
            DashedLine(B, B1, color=GREY),
            Line(M, A, color=BLUE, stroke_opacity=0.5),
            Line(M, A1, color=BLUE, stroke_opacity=0.5)
        )

        self.add(axes, dots, labels, lines)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: test_002 - Кружници што се допираат
**📅 Додадено:** 2025-12-28 17:23
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_test_002(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
        # Setup
        O1 = LEFT * 1.5
        O2 = RIGHT * 1.0
        r1 = 1.5
        r2 = 1.0
        
        # Circles
        c1 = Circle(radius=r1, color=BLUE).move_to(O1)
        c2 = Circle(radius=r2, color=RED).move_to(O2)
        
        # Common tangent at (0,0) is the y-axis
        tangent = Line(DOWN*3, UP*3, color=GREEN)
        
        # Labels
        lbl_O1 = MathTex("O_1", color=BLUE).next_to(O1, DOWN)
        lbl_O2 = MathTex("O_2", color=RED).next_to(O2, DOWN)
        lbl_t = MathTex("t", color=GREEN).next_to(tangent, UP)
        
        # Add to scene
        self.add(c1, c2, tangent, lbl_O1, lbl_O2, lbl_t)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: test_002 - Кружници што се допираат
**📅 Додадено:** 2025-12-28 17:25
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_test_002(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
        # Setup
        O1 = LEFT * 1.5
        O2 = RIGHT * 1.0
        r1 = 1.5
        r2 = 1.0
        
        # Circles
        c1 = Circle(radius=r1, color=BLUE).move_to(O1)
        c2 = Circle(radius=r2, color=RED).move_to(O2)
        
        # Common tangent at (0,0) is the y-axis
        tangent = Line(DOWN*3, UP*3, color=GREEN)
        
        # Labels
        lbl_O1 = MathTex("O_1", color=BLUE).next_to(O1, DOWN)
        lbl_O2 = MathTex("O_2", color=RED).next_to(O2, DOWN)
        lbl_t = MathTex("t", color=GREEN).next_to(tangent, UP)
        
        # Add to scene
        self.add(c1, c2, tangent, lbl_O1, lbl_O2, lbl_t)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: geo_three_circles_tangent - Третата кружница (Сангаку)
**📅 Додадено:** 2025-12-28 17:30
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geo_three_circles_tangent(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
        # 1. Setup parameters
        R = 3.0
        r = 2.0
        # Calculate x using the formula: 1/sqrt(x) = 1/sqrt(R) + 1/sqrt(r)
        sqrt_x_inv = 1/np.sqrt(R) + 1/np.sqrt(r)
        x = 1 / (sqrt_x_inv ** 2)
        
        # 2. Coordinates
        # Line at y=0
        # Circle 1 at (0, R)
        O1 = [-2, R - 2, 0] # Shifted down/left for centering
        # Circle 2 distance: 2*sqrt(Rr)
        dist_12 = 2 * np.sqrt(R * r)
        O2 = [O1[0] + dist_12, r - 2, 0]
        
        # Circle 3 distance from C1: 2*sqrt(Rx)
        dist_13 = 2 * np.sqrt(R * x)
        O3 = [O1[0] + dist_13, x - 2, 0]

        # 3. Objects
        line = Line(LEFT*4, RIGHT*4, color=BLACK).shift(DOWN*2)
        c1 = Circle(radius=R, color=BLUE).move_to(O1)
        c2 = Circle(radius=r, color=GREEN).move_to(O2)
        c3 = Circle(radius=x, color=RED).move_to(O3)
        
        # Radii lines
        l1 = Line(O1, O1 + DOWN*R, color=BLACK)
        l2 = Line(O2, O2 + DOWN*r, color=BLACK)
        l3 = Line(O3, O3 + DOWN*x, color=BLACK)

        # 4. Labels
        labels = VGroup(
            MathTex('R').next_to(l1, LEFT, buff=0.1),
            MathTex('r').next_to(l2, RIGHT, buff=0.1),
            MathTex('x', color=RED).next_to(c3, UP, buff=0.1)
        ).set_color(BLACK)

        self.add(line, c1, c2, c3, l1, l2, l3, labels)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: geo_three_circles_tangent - Третата кружница (Сангаку)
**📅 Додадено:** 2025-12-28 17:33
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geo_three_circles_tangent(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
        # 1. Setup parameters
        R = 3.0
        r = 2.0
        # Calculate x using the formula: 1/sqrt(x) = 1/sqrt(R) + 1/sqrt(r)
        sqrt_x_inv = 1/np.sqrt(R) + 1/np.sqrt(r)
        x = 1 / (sqrt_x_inv ** 2)
        
        # 2. Coordinates
        # Line at y=0
        # Circle 1 at (0, R)
        O1 = [-2, R - 2, 0] # Shifted down/left for centering
        # Circle 2 distance: 2*sqrt(Rr)
        dist_12 = 2 * np.sqrt(R * r)
        O2 = [O1[0] + dist_12, r - 2, 0]
        
        # Circle 3 distance from C1: 2*sqrt(Rx)
        dist_13 = 2 * np.sqrt(R * x)
        O3 = [O1[0] + dist_13, x - 2, 0]

        # 3. Objects
        line = Line(LEFT*4, RIGHT*4, color=BLACK).shift(DOWN*2)
        c1 = Circle(radius=R, color=BLUE).move_to(O1)
        c2 = Circle(radius=r, color=GREEN).move_to(O2)
        c3 = Circle(radius=x, color=RED).move_to(O3)
        
        # Radii lines
        l1 = Line(O1, O1 + DOWN*R, color=BLACK)
        l2 = Line(O2, O2 + DOWN*r, color=BLACK)
        l3 = Line(O3, O3 + DOWN*x, color=BLACK)

        # 4. Labels
        labels = VGroup(
            MathTex('R').next_to(l1, LEFT, buff=0.1),
            MathTex('r').next_to(l2, RIGHT, buff=0.1),
            MathTex('x', color=RED).next_to(c3, UP, buff=0.1)
        ).set_color(BLACK)

        self.add(line, c1, c2, c3, l1, l2, l3, labels)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: geo_three_circles_tangent - Третата кружница (Сангаку)
**📅 Додадено:** 2025-12-28 17:40
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geo_three_circles_tangent(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
        # 1. Setup parameters
        R = 3.0
        r = 2.0
        # Calculate x using the formula: 1/sqrt(x) = 1/sqrt(R) + 1/sqrt(r)
        sqrt_x_inv = 1/np.sqrt(R) + 1/np.sqrt(r)
        x = 1 / (sqrt_x_inv ** 2)
        
        # 2. Coordinates
        # Line at y=0
        # Circle 1 at (0, R)
        O1 = [-2, R - 2, 0] # Shifted down/left for centering
        # Circle 2 distance: 2*sqrt(Rr)
        dist_12 = 2 * np.sqrt(R * r)
        O2 = [O1[0] + dist_12, r - 2, 0]
        
        # Circle 3 distance from C1: 2*sqrt(Rx)
        dist_13 = 2 * np.sqrt(R * x)
        O3 = [O1[0] + dist_13, x - 2, 0]

        # 3. Objects
        line = Line(LEFT*4, RIGHT*4, color=BLACK).shift(DOWN*2)
        c1 = Circle(radius=R, color=BLUE).move_to(O1)
        c2 = Circle(radius=r, color=GREEN).move_to(O2)
        c3 = Circle(radius=x, color=RED).move_to(O3)
        
        # Radii lines
        l1 = Line(O1, O1 + DOWN*R, color=BLACK)
        l2 = Line(O2, O2 + DOWN*r, color=BLACK)
        l3 = Line(O3, O3 + DOWN*x, color=BLACK)

        # 4. Labels
        labels = VGroup(
            MathTex('R').next_to(l1, LEFT, buff=0.1),
            MathTex('r').next_to(l2, RIGHT, buff=0.1),
            MathTex('x', color=RED).next_to(c3, UP, buff=0.1)
        ).set_color(BLACK)

        self.add(line, c1, c2, c3, l1, l2, l3, labels)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: geo_three_circles_tangent - Третата кружница (Сангаку)
**📅 Додадено:** 2025-12-28 17:42
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geo_three_circles_tangent(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
        # 1. Setup parameters
        R = 3.0
        r = 2.0
        # Calculate x using the formula: 1/sqrt(x) = 1/sqrt(R) + 1/sqrt(r)
        sqrt_x_inv = 1/np.sqrt(R) + 1/np.sqrt(r)
        x = 1 / (sqrt_x_inv ** 2)
        
        # 2. Coordinates
        # Line at y=0
        # Circle 1 at (0, R)
        O1 = [-2, R - 2, 0] # Shifted down/left for centering
        # Circle 2 distance: 2*sqrt(Rr)
        dist_12 = 2 * np.sqrt(R * r)
        O2 = [O1[0] + dist_12, r - 2, 0]
        
        # Circle 3 distance from C1: 2*sqrt(Rx)
        dist_13 = 2 * np.sqrt(R * x)
        O3 = [O1[0] + dist_13, x - 2, 0]

        # 3. Objects
        line = Line(LEFT*4, RIGHT*4, color=BLACK).shift(DOWN*2)
        c1 = Circle(radius=R, color=BLUE).move_to(O1)
        c2 = Circle(radius=r, color=GREEN).move_to(O2)
        c3 = Circle(radius=x, color=RED).move_to(O3)
        
        # Radii lines
        l1 = Line(O1, O1 + DOWN*R, color=BLACK)
        l2 = Line(O2, O2 + DOWN*r, color=BLACK)
        l3 = Line(O3, O3 + DOWN*x, color=BLACK)

        # 4. Labels
        labels = VGroup(
            MathTex('R').next_to(l1, LEFT, buff=0.1),
            MathTex('r').next_to(l2, RIGHT, buff=0.1),
            MathTex('x', color=RED).next_to(c3, UP, buff=0.1)
        ).set_color(BLACK)

        self.add(line, c1, c2, c3, l1, l2, l3, labels)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: geo_three_circles_tangent - Третата кружница (Сангаку)
**📅 Додадено:** 2026-01-07 21:02
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geo_three_circles_tangent(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
        # 1. Setup parameters
        R = 3.0
        r = 2.0
        # Calculate x using the formula: 1/sqrt(x) = 1/sqrt(R) + 1/sqrt(r)
        sqrt_x_inv = 1/np.sqrt(R) + 1/np.sqrt(r)
        x = 1 / (sqrt_x_inv ** 2)
        
        # 2. Coordinates
        # Line at y=0
        # Circle 1 at (0, R)
        O1 = [-2, R - 2, 0] # Shifted down/left for centering
        # Circle 2 distance: 2*sqrt(Rr)
        dist_12 = 2 * np.sqrt(R * r)
        O2 = [O1[0] + dist_12, r - 2, 0]
        
        # Circle 3 distance from C1: 2*sqrt(Rx)
        dist_13 = 2 * np.sqrt(R * x)
        O3 = [O1[0] + dist_13, x - 2, 0]

        # 3. Objects
        line = Line(LEFT*4, RIGHT*4, color=BLACK).shift(DOWN*2)
        c1 = Circle(radius=R, color=BLUE).move_to(O1)
        c2 = Circle(radius=r, color=GREEN).move_to(O2)
        c3 = Circle(radius=x, color=RED).move_to(O3)
        
        # Radii lines
        l1 = Line(O1, O1 + DOWN*R, color=BLACK)
        l2 = Line(O2, O2 + DOWN*r, color=BLACK)
        l3 = Line(O3, O3 + DOWN*x, color=BLACK)

        # 4. Labels
        labels = VGroup(
            MathTex('R').next_to(l1, LEFT, buff=0.1),
            MathTex('r').next_to(l2, RIGHT, buff=0.1),
            MathTex('x', color=RED).next_to(c3, UP, buff=0.1)
        ).set_color(BLACK)

        self.add(line, c1, c2, c3, l1, l2, l3, labels)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: sigma137_y1_p2 - Аголот во триаголникот и впишаната кружница
**📅 Додадено:** 2026-01-07 21:26
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_sigma137_y1_p2(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE

    # Coordinates based on calculated angles: A=96.5, B=48.25, C=35.25
    # Scale factor
    s = 6
    
    # Point C at origin
    C = ORIGIN
    # Point B on x-axis. Length a. Let's normalize.
    # Sine rule: a/sin(A) = b/sin(B). Let a = 6.
    # b = 6 * sin(48.25) / sin(96.5) approx 6 * 0.746 / 0.993 = 4.5
    
    B = RIGHT * 6
    # A is at angle 35.25 from C, length b
    # 35.25 degrees in radians is 0.615
    A = np.array([4.5 * np.cos(35.25 * DEGREES), 4.5 * np.sin(35.25 * DEGREES), 0])

    # Incenter O
    # Bisector of C is simply line at 35.25/2 degrees
    # Bisector of B is line from B at 180 - 48.25/2 degrees
    # Intersection calculation (simplified for visual)
    # Incenter coordinates formula: (aA + bB + cC) / (a+b+c)
    c_len = np.linalg.norm(A - B)
    b_len = np.linalg.norm(A - C)
    a_len = np.linalg.norm(B - C)
    O = (a_len * A + b_len * B + c_len * C) / (a_len + b_len + c_len)

    # Point K on BC such that CK = AC = b_len
    K = C + (B - C) * (b_len / a_len)

    # Create Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    labels = VGroup(
        MathTex("A").next_to(A, UP),
        MathTex("B").next_to(B, RIGHT),
        MathTex("C").next_to(C, LEFT),
        MathTex("O").next_to(O, UP, buff=0.1),
        MathTex("K").next_to(K, DOWN)
    ).set_color(BLACK)

    # Segments
    seg_AO = Line(A, O, color=BLUE, stroke_width=3)
    seg_KO = Line(K, O, color=BLUE, stroke_width=3)
    seg_BK = Line(B, K, color=RED, stroke_width=4)
    seg_CK = Line(C, K, color=GREEN, stroke_width=4)
    seg_AC = Line(A, C, color=GREEN, stroke_width=4)

    # Markings
    # AC = CK
    mark_AC = DashedLine(A, C, color=GREEN)
    
    # BK = AO = KO
    # Just highlight them

    self.add(triangle)
    self.add(seg_AO, seg_KO, seg_BK, seg_CK, seg_AC)
    self.add(labels)

    # Add angle labels
    angle_A = Angle(Line(A, B), Line(A, C), radius=0.4, other_angle=True)
    label_A = MathTex(r"\alpha").next_to(angle_A, UP)
    
    self.add(angle_A, label_A)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: sigma137_y1_p2 - Аголот во триаголникот и впишаната кружница
**📅 Додадено:** 2026-01-07 21:38
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_sigma137_y1_p2(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE

    # Coordinates based on calculated angles: A=96.5, B=48.25, C=35.25
    # Scale factor
    s = 6
    
    # Point C at origin
    C = ORIGIN
    # Point B on x-axis. Length a. Let's normalize.
    # Sine rule: a/sin(A) = b/sin(B). Let a = 6.
    # b = 6 * sin(48.25) / sin(96.5) approx 6 * 0.746 / 0.993 = 4.5
    
    B = RIGHT * 6
    # A is at angle 35.25 from C, length b
    # 35.25 degrees in radians is 0.615
    A = np.array([4.5 * np.cos(35.25 * DEGREES), 4.5 * np.sin(35.25 * DEGREES), 0])

    # Incenter O
    # Bisector of C is simply line at 35.25/2 degrees
    # Bisector of B is line from B at 180 - 48.25/2 degrees
    # Intersection calculation (simplified for visual)
    # Incenter coordinates formula: (aA + bB + cC) / (a+b+c)
    c_len = np.linalg.norm(A - B)
    b_len = np.linalg.norm(A - C)
    a_len = np.linalg.norm(B - C)
    O = (a_len * A + b_len * B + c_len * C) / (a_len + b_len + c_len)

    # Point K on BC such that CK = AC = b_len
    K = C + (B - C) * (b_len / a_len)

    # Create Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    labels = VGroup(
        MathTex("A").next_to(A, UP),
        MathTex("B").next_to(B, RIGHT),
        MathTex("C").next_to(C, LEFT),
        MathTex("O").next_to(O, UP, buff=0.1),
        MathTex("K").next_to(K, DOWN)
    ).set_color(BLACK)

    # Segments
    seg_AO = Line(A, O, color=BLUE, stroke_width=3)
    seg_KO = Line(K, O, color=BLUE, stroke_width=3)
    seg_BK = Line(B, K, color=RED, stroke_width=4)
    seg_CK = Line(C, K, color=GREEN, stroke_width=4)
    seg_AC = Line(A, C, color=GREEN, stroke_width=4)

    # Markings
    # AC = CK
    mark_AC = DashedLine(A, C, color=GREEN)
    
    # BK = AO = KO
    # Just highlight them

    self.add(triangle)
    self.add(seg_AO, seg_KO, seg_BK, seg_CK, seg_AC)
    self.add(labels)

    # Add angle labels
    angle_A = Angle(Line(A, B), Line(A, C), radius=0.4, other_angle=True)
    label_A = MathTex(r"\alpha").next_to(angle_A, UP)
    
    self.add(angle_A, label_A)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: sigma137_y1_p2 - Аголот во триаголникот и впишаната кружница
**📅 Додадено:** 2026-01-07 21:46
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_sigma137_y1_p2(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE

    # Coordinates based on calculated angles: A=96.5, B=48.25, C=35.25
    # Scale factor
    s = 6
    
    # Point C at origin
    C = ORIGIN
    # Point B on x-axis. Length a. Let's normalize.
    # Sine rule: a/sin(A) = b/sin(B). Let a = 6.
    # b = 6 * sin(48.25) / sin(96.5) approx 6 * 0.746 / 0.993 = 4.5
    
    B = RIGHT * 6
    # A is at angle 35.25 from C, length b
    # 35.25 degrees in radians is 0.615
    A = np.array([4.5 * np.cos(35.25 * DEGREES), 4.5 * np.sin(35.25 * DEGREES), 0])

    # Incenter O
    # Bisector of C is simply line at 35.25/2 degrees
    # Bisector of B is line from B at 180 - 48.25/2 degrees
    # Intersection calculation (simplified for visual)
    # Incenter coordinates formula: (aA + bB + cC) / (a+b+c)
    c_len = np.linalg.norm(A - B)
    b_len = np.linalg.norm(A - C)
    a_len = np.linalg.norm(B - C)
    O = (a_len * A + b_len * B + c_len * C) / (a_len + b_len + c_len)

    # Point K on BC such that CK = AC = b_len
    K = C + (B - C) * (b_len / a_len)

    # Create Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    labels = VGroup(
        MathTex("A").next_to(A, UP),
        MathTex("B").next_to(B, RIGHT),
        MathTex("C").next_to(C, LEFT),
        MathTex("O").next_to(O, UP, buff=0.1),
        MathTex("K").next_to(K, DOWN)
    ).set_color(BLACK)

    # Segments
    seg_AO = Line(A, O, color=BLUE, stroke_width=3)
    seg_KO = Line(K, O, color=BLUE, stroke_width=3)
    seg_BK = Line(B, K, color=RED, stroke_width=4)
    seg_CK = Line(C, K, color=GREEN, stroke_width=4)
    seg_AC = Line(A, C, color=GREEN, stroke_width=4)

    # Markings
    # AC = CK
    mark_AC = DashedLine(A, C, color=GREEN)
    
    # BK = AO = KO
    # Just highlight them

    self.add(triangle)
    self.add(seg_AO, seg_KO, seg_BK, seg_CK, seg_AC)
    self.add(labels)

    # Add angle labels
    angle_A = Angle(Line(A, B), Line(A, C), radius=0.4, other_angle=True)
    label_A = MathTex(r"\alpha").next_to(angle_A, UP)
    
    self.add(angle_A, label_A)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: sigma137_y1_p2 - Аголот во триаголникот и впишаната кружница
**📅 Додадено:** 2026-01-07 21:50
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_sigma137_y1_p2(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE

    # Coordinates based on calculated angles: A=96.5, B=48.25, C=35.25
    # Scale factor
    s = 6
    
    # Point C at origin
    C = ORIGIN
    # Point B on x-axis. Length a. Let's normalize.
    # Sine rule: a/sin(A) = b/sin(B). Let a = 6.
    # b = 6 * sin(48.25) / sin(96.5) approx 6 * 0.746 / 0.993 = 4.5
    
    B = RIGHT * 6
    # A is at angle 35.25 from C, length b
    # 35.25 degrees in radians is 0.615
    A = np.array([4.5 * np.cos(35.25 * DEGREES), 4.5 * np.sin(35.25 * DEGREES), 0])

    # Incenter O
    # Bisector of C is simply line at 35.25/2 degrees
    # Bisector of B is line from B at 180 - 48.25/2 degrees
    # Intersection calculation (simplified for visual)
    # Incenter coordinates formula: (aA + bB + cC) / (a+b+c)
    c_len = np.linalg.norm(A - B)
    b_len = np.linalg.norm(A - C)
    a_len = np.linalg.norm(B - C)
    O = (a_len * A + b_len * B + c_len * C) / (a_len + b_len + c_len)

    # Point K on BC such that CK = AC = b_len
    K = C + (B - C) * (b_len / a_len)

    # Create Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    labels = VGroup(
        MathTex("A").next_to(A, UP),
        MathTex("B").next_to(B, RIGHT),
        MathTex("C").next_to(C, LEFT),
        MathTex("O").next_to(O, UP, buff=0.1),
        MathTex("K").next_to(K, DOWN)
    ).set_color(BLACK)

    # Segments
    seg_AO = Line(A, O, color=BLUE, stroke_width=3)
    seg_KO = Line(K, O, color=BLUE, stroke_width=3)
    seg_BK = Line(B, K, color=RED, stroke_width=4)
    seg_CK = Line(C, K, color=GREEN, stroke_width=4)
    seg_AC = Line(A, C, color=GREEN, stroke_width=4)

    # Markings
    # AC = CK
    mark_AC = DashedLine(A, C, color=GREEN)
    
    # BK = AO = KO
    # Just highlight them

    self.add(triangle)
    self.add(seg_AO, seg_KO, seg_BK, seg_CK, seg_AC)
    self.add(labels)

    # Add angle labels
    angle_A = Angle(Line(A, B), Line(A, C), radius=0.4, other_angle=True)
    label_A = MathTex(r"\alpha").next_to(angle_A, UP)
    
    self.add(angle_A, label_A)
        # --- AI GENERATED CODE END ---

```
---

### 🆔 Задача: sigma137_y1_p2 - Аголот во триаголникот и впишаната кружница
**📅 Додадено:** 2026-01-07 21:56
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_sigma137_y1_p2(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE

    # Coordinates based on calculated angles: A=96.5, B=48.25, C=35.25
    # Scale factor
    s = 6
    
    # Point C at origin
    C = ORIGIN
    # Point B on x-axis. Length a. Let's normalize.
    # Sine rule: a/sin(A) = b/sin(B). Let a = 6.
    # b = 6 * sin(48.25) / sin(96.5) approx 6 * 0.746 / 0.993 = 4.5
    
    B = RIGHT * 6
    # A is at angle 35.25 from C, length b
    # 35.25 degrees in radians is 0.615
    A = np.array([4.5 * np.cos(35.25 * DEGREES), 4.5 * np.sin(35.25 * DEGREES), 0])

    # Incenter O
    # Bisector of C is simply line at 35.25/2 degrees
    # Bisector of B is line from B at 180 - 48.25/2 degrees
    # Intersection calculation (simplified for visual)
    # Incenter coordinates formula: (aA + bB + cC) / (a+b+c)
    c_len = np.linalg.norm(A - B)
    b_len = np.linalg.norm(A - C)
    a_len = np.linalg.norm(B - C)
    O = (a_len * A + b_len * B + c_len * C) / (a_len + b_len + c_len)

    # Point K on BC such that CK = AC = b_len
    K = C + (B - C) * (b_len / a_len)

    # Create Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    labels = VGroup(
        MathTex("A").next_to(A, UP),
        MathTex("B").next_to(B, RIGHT),
        MathTex("C").next_to(C, LEFT),
        MathTex("O").next_to(O, UP, buff=0.1),
        MathTex("K").next_to(K, DOWN)
    ).set_color(BLACK)

    # Segments
    seg_AO = Line(A, O, color=BLUE, stroke_width=3)
    seg_KO = Line(K, O, color=BLUE, stroke_width=3)
    seg_BK = Line(B, K, color=RED, stroke_width=4)
    seg_CK = Line(C, K, color=GREEN, stroke_width=4)
    seg_AC = Line(A, C, color=GREEN, stroke_width=4)

    # Markings
    # AC = CK
    mark_AC = DashedLine(A, C, color=GREEN)
    
    # BK = AO = KO
    # Just highlight them

    self.add(triangle)
    self.add(seg_AO, seg_KO, seg_BK, seg_CK, seg_AC)
    self.add(labels)

    # Add angle labels
    angle_A = Angle(Line(A, B), Line(A, C), radius=0.4, other_angle=True)
    label_A = MathTex(r"\alpha").next_to(angle_A, UP)
    
    self.add(angle_A, label_A)
        # --- AI GENERATED CODE END ---

```
---

### ID Задача: sigma137_p1864 - Неравенство со растојанија во триаголник
**Date Додадено:** 2026-01-07 22:15
**Python Python/Manim Код:**
```python
from manim import *

class Task_sigma137_p1864(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE
    
    # Triangle vertices
    A = UP * 3
    B = LEFT * 3 + DOWN * 2
    C = RIGHT * 3 + DOWN * 2
    
    # Point P inside
    P = DOWN * 0.5 + RIGHT * 0.2
    
    # Projections
    # Function to find projection of P onto line XY
    def get_projection(P, X, Y):
        # Vector XY
        XY = Y - X
        # Vector XP
        XP = P - X
        # Projection scalar
        t = np.dot(XP, XY) / np.dot(XY, XY)
        return X + t * XY
        
    A1 = get_projection(P, B, C)
    B1 = get_projection(P, C, A)
    C1 = get_projection(P, A, B)
    
    # Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    
    # Perpendiculars from P
    line_PA1 = DashedLine(P, A1, color=BLUE)
    line_PB1 = DashedLine(P, B1, color=BLUE)
    line_PC1 = DashedLine(P, C1, color=BLUE)
    
    # Segments PA, PB, PC
    seg_PA = Line(P, A, color=RED, stroke_width=3)
    seg_PB = Line(P, B, color=RED, stroke_width=3)
    seg_PC = Line(P, C, color=RED, stroke_width=3)
    
    # Labels
    lbl_A = MathTex("A").next_to(A, UP)
    lbl_B = MathTex("B").next_to(B, DL)
    lbl_C = MathTex("C").next_to(C, DR)
    lbl_P = MathTex("P").next_to(P, UP, buff=0.1)
    lbl_A1 = MathTex("A_1").next_to(A1, DOWN)
    lbl_B1 = MathTex("B_1").next_to(B1, UR, buff=0.1)
    lbl_C1 = MathTex("C_1").next_to(C1, UL, buff=0.1)
    
    # Right angle markers
    ra_A1 = RightAngle(Line(P, A1), Line(B, C), length=0.3)
    ra_B1 = RightAngle(Line(P, B1), Line(C, A), length=0.3)
    ra_C1 = RightAngle(Line(P, C1), Line(A, B), length=0.3)

    self.add(triangle)
    self.add(line_PA1, line_PB1, line_PC1)
    self.add(seg_PA, seg_PB, seg_PC)
    self.add(lbl_A, lbl_B, lbl_C, lbl_P, lbl_A1, lbl_B1, lbl_C1)
    self.add(ra_A1, ra_B1, ra_C1)
        # --- AI GENERATED CODE END ---

```
---

### ID Задача: sigma137_p1864 - Неравенство со растојанија во триаголник
**Date Додадено:** 2026-01-07 22:15
**Python Python/Manim Код:**
```python
from manim import *

class Task_sigma137_p1864(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE
    
    # Triangle vertices
    A = UP * 3
    B = LEFT * 3 + DOWN * 2
    C = RIGHT * 3 + DOWN * 2
    
    # Point P inside
    P = DOWN * 0.5 + RIGHT * 0.2
    
    # Projections
    # Function to find projection of P onto line XY
    def get_projection(P, X, Y):
        # Vector XY
        XY = Y - X
        # Vector XP
        XP = P - X
        # Projection scalar
        t = np.dot(XP, XY) / np.dot(XY, XY)
        return X + t * XY
        
    A1 = get_projection(P, B, C)
    B1 = get_projection(P, C, A)
    C1 = get_projection(P, A, B)
    
    # Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    
    # Perpendiculars from P
    line_PA1 = DashedLine(P, A1, color=BLUE)
    line_PB1 = DashedLine(P, B1, color=BLUE)
    line_PC1 = DashedLine(P, C1, color=BLUE)
    
    # Segments PA, PB, PC
    seg_PA = Line(P, A, color=RED, stroke_width=3)
    seg_PB = Line(P, B, color=RED, stroke_width=3)
    seg_PC = Line(P, C, color=RED, stroke_width=3)
    
    # Labels
    lbl_A = MathTex("A").next_to(A, UP)
    lbl_B = MathTex("B").next_to(B, DL)
    lbl_C = MathTex("C").next_to(C, DR)
    lbl_P = MathTex("P").next_to(P, UP, buff=0.1)
    lbl_A1 = MathTex("A_1").next_to(A1, DOWN)
    lbl_B1 = MathTex("B_1").next_to(B1, UR, buff=0.1)
    lbl_C1 = MathTex("C_1").next_to(C1, UL, buff=0.1)
    
    # Right angle markers
    ra_A1 = RightAngle(Line(P, A1), Line(B, C), length=0.3)
    ra_B1 = RightAngle(Line(P, B1), Line(C, A), length=0.3)
    ra_C1 = RightAngle(Line(P, C1), Line(A, B), length=0.3)

    self.add(triangle)
    self.add(line_PA1, line_PB1, line_PC1)
    self.add(seg_PA, seg_PB, seg_PC)
    self.add(lbl_A, lbl_B, lbl_C, lbl_P, lbl_A1, lbl_B1, lbl_C1)
    self.add(ra_A1, ra_B1, ra_C1)
        # --- AI GENERATED CODE END ---

```
---

### ID Zadacha: sigma137_p1864 - Неравенство со растојанија во триаголник
**Date Dodadeno:** 2026-01-07 22:16
**Python/Manim Kod:**
```python
from manim import *

class Task_sigma137_p1864(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE
    
    # Triangle vertices
    A = UP * 3
    B = LEFT * 3 + DOWN * 2
    C = RIGHT * 3 + DOWN * 2
    
    # Point P inside
    P = DOWN * 0.5 + RIGHT * 0.2
    
    # Projections
    # Function to find projection of P onto line XY
    def get_projection(P, X, Y):
        # Vector XY
        XY = Y - X
        # Vector XP
        XP = P - X
        # Projection scalar
        t = np.dot(XP, XY) / np.dot(XY, XY)
        return X + t * XY
        
    A1 = get_projection(P, B, C)
    B1 = get_projection(P, C, A)
    C1 = get_projection(P, A, B)
    
    # Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    
    # Perpendiculars from P
    line_PA1 = DashedLine(P, A1, color=BLUE)
    line_PB1 = DashedLine(P, B1, color=BLUE)
    line_PC1 = DashedLine(P, C1, color=BLUE)
    
    # Segments PA, PB, PC
    seg_PA = Line(P, A, color=RED, stroke_width=3)
    seg_PB = Line(P, B, color=RED, stroke_width=3)
    seg_PC = Line(P, C, color=RED, stroke_width=3)
    
    # Labels
    lbl_A = MathTex("A").next_to(A, UP)
    lbl_B = MathTex("B").next_to(B, DL)
    lbl_C = MathTex("C").next_to(C, DR)
    lbl_P = MathTex("P").next_to(P, UP, buff=0.1)
    lbl_A1 = MathTex("A_1").next_to(A1, DOWN)
    lbl_B1 = MathTex("B_1").next_to(B1, UR, buff=0.1)
    lbl_C1 = MathTex("C_1").next_to(C1, UL, buff=0.1)
    
    # Right angle markers
    ra_A1 = RightAngle(Line(P, A1), Line(B, C), length=0.3)
    ra_B1 = RightAngle(Line(P, B1), Line(C, A), length=0.3)
    ra_C1 = RightAngle(Line(P, C1), Line(A, B), length=0.3)

    self.add(triangle)
    self.add(line_PA1, line_PB1, line_PC1)
    self.add(seg_PA, seg_PB, seg_PC)
    self.add(lbl_A, lbl_B, lbl_C, lbl_P, lbl_A1, lbl_B1, lbl_C1)
    self.add(ra_A1, ra_B1, ra_C1)
        # --- AI GENERATED CODE END ---

```
---

### ID Zadacha: sigma137_p1864 - Неравенство со растојанија во триаголник
**Date Dodadeno:** 2026-01-07 22:17
**Python/Manim Kod:**
```python
from manim import *

class Task_sigma137_p1864(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE
    
    # Triangle vertices
    A = UP * 3
    B = LEFT * 3 + DOWN * 2
    C = RIGHT * 3 + DOWN * 2
    
    # Point P inside
    P = DOWN * 0.5 + RIGHT * 0.2
    
    # Projections
    # Function to find projection of P onto line XY
    def get_projection(P, X, Y):
        # Vector XY
        XY = Y - X
        # Vector XP
        XP = P - X
        # Projection scalar
        t = np.dot(XP, XY) / np.dot(XY, XY)
        return X + t * XY
        
    A1 = get_projection(P, B, C)
    B1 = get_projection(P, C, A)
    C1 = get_projection(P, A, B)
    
    # Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    
    # Perpendiculars from P
    line_PA1 = DashedLine(P, A1, color=BLUE)
    line_PB1 = DashedLine(P, B1, color=BLUE)
    line_PC1 = DashedLine(P, C1, color=BLUE)
    
    # Segments PA, PB, PC
    seg_PA = Line(P, A, color=RED, stroke_width=3)
    seg_PB = Line(P, B, color=RED, stroke_width=3)
    seg_PC = Line(P, C, color=RED, stroke_width=3)
    
    # Labels
    lbl_A = MathTex("A").next_to(A, UP)
    lbl_B = MathTex("B").next_to(B, DL)
    lbl_C = MathTex("C").next_to(C, DR)
    lbl_P = MathTex("P").next_to(P, UP, buff=0.1)
    lbl_A1 = MathTex("A_1").next_to(A1, DOWN)
    lbl_B1 = MathTex("B_1").next_to(B1, UR, buff=0.1)
    lbl_C1 = MathTex("C_1").next_to(C1, UL, buff=0.1)
    
    # Right angle markers
    ra_A1 = RightAngle(Line(P, A1), Line(B, C), length=0.3)
    ra_B1 = RightAngle(Line(P, B1), Line(C, A), length=0.3)
    ra_C1 = RightAngle(Line(P, C1), Line(A, B), length=0.3)

    self.add(triangle)
    self.add(line_PA1, line_PB1, line_PC1)
    self.add(seg_PA, seg_PB, seg_PC)
    self.add(lbl_A, lbl_B, lbl_C, lbl_P, lbl_A1, lbl_B1, lbl_C1)
    self.add(ra_A1, ra_B1, ra_C1)
        # --- AI GENERATED CODE END ---

```
---

### ID Zadacha: sigma137_p1864 - Неравенство со растојанија во триаголник
**Date Dodadeno:** 2026-01-07 22:26
**Python/Manim Kod:**
```python
from manim import *

class Task_sigma137_p1864(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE
    
    # Triangle vertices
    A = UP * 3
    B = LEFT * 3 + DOWN * 2
    C = RIGHT * 3 + DOWN * 2
    
    # Point P inside
    P = DOWN * 0.5 + RIGHT * 0.2
    
    # Projections
    # Function to find projection of P onto line XY
    def get_projection(P, X, Y):
        # Vector XY
        XY = Y - X
        # Vector XP
        XP = P - X
        # Projection scalar
        t = np.dot(XP, XY) / np.dot(XY, XY)
        return X + t * XY
        
    A1 = get_projection(P, B, C)
    B1 = get_projection(P, C, A)
    C1 = get_projection(P, A, B)
    
    # Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    
    # Perpendiculars from P
    line_PA1 = DashedLine(P, A1, color=BLUE)
    line_PB1 = DashedLine(P, B1, color=BLUE)
    line_PC1 = DashedLine(P, C1, color=BLUE)
    
    # Segments PA, PB, PC
    seg_PA = Line(P, A, color=RED, stroke_width=3)
    seg_PB = Line(P, B, color=RED, stroke_width=3)
    seg_PC = Line(P, C, color=RED, stroke_width=3)
    
    # Labels
    lbl_A = MathTex("A").next_to(A, UP)
    lbl_B = MathTex("B").next_to(B, DL)
    lbl_C = MathTex("C").next_to(C, DR)
    lbl_P = MathTex("P").next_to(P, UP, buff=0.1)
    lbl_A1 = MathTex("A_1").next_to(A1, DOWN)
    lbl_B1 = MathTex("B_1").next_to(B1, UR, buff=0.1)
    lbl_C1 = MathTex("C_1").next_to(C1, UL, buff=0.1)
    
    # Right angle markers
    ra_A1 = RightAngle(Line(P, A1), Line(B, C), length=0.3)
    ra_B1 = RightAngle(Line(P, B1), Line(C, A), length=0.3)
    ra_C1 = RightAngle(Line(P, C1), Line(A, B), length=0.3)

    self.add(triangle)
    self.add(line_PA1, line_PB1, line_PC1)
    self.add(seg_PA, seg_PB, seg_PC)
    self.add(lbl_A, lbl_B, lbl_C, lbl_P, lbl_A1, lbl_B1, lbl_C1)
    self.add(ra_A1, ra_B1, ra_C1)
        # --- AI GENERATED CODE END ---

```
---

### ID Zadacha: sigma137_p1864 - Неравенство со растојанија во триаголник
**Date Dodadeno:** 2026-01-07 22:27
**Python/Manim Kod:**
```python
from manim import *

class Task_sigma137_p1864(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE
    
    # Triangle vertices
    A = UP * 3
    B = LEFT * 3 + DOWN * 2
    C = RIGHT * 3 + DOWN * 2
    
    # Point P inside
    P = DOWN * 0.5 + RIGHT * 0.2
    
    # Projections
    # Function to find projection of P onto line XY
    def get_projection(P, X, Y):
        # Vector XY
        XY = Y - X
        # Vector XP
        XP = P - X
        # Projection scalar
        t = np.dot(XP, XY) / np.dot(XY, XY)
        return X + t * XY
        
    A1 = get_projection(P, B, C)
    B1 = get_projection(P, C, A)
    C1 = get_projection(P, A, B)
    
    # Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    
    # Perpendiculars from P
    line_PA1 = DashedLine(P, A1, color=BLUE)
    line_PB1 = DashedLine(P, B1, color=BLUE)
    line_PC1 = DashedLine(P, C1, color=BLUE)
    
    # Segments PA, PB, PC
    seg_PA = Line(P, A, color=RED, stroke_width=3)
    seg_PB = Line(P, B, color=RED, stroke_width=3)
    seg_PC = Line(P, C, color=RED, stroke_width=3)
    
    # Labels
    lbl_A = MathTex("A").next_to(A, UP)
    lbl_B = MathTex("B").next_to(B, DL)
    lbl_C = MathTex("C").next_to(C, DR)
    lbl_P = MathTex("P").next_to(P, UP, buff=0.1)
    lbl_A1 = MathTex("A_1").next_to(A1, DOWN)
    lbl_B1 = MathTex("B_1").next_to(B1, UR, buff=0.1)
    lbl_C1 = MathTex("C_1").next_to(C1, UL, buff=0.1)
    
    # Right angle markers
    ra_A1 = RightAngle(Line(P, A1), Line(B, C), length=0.3)
    ra_B1 = RightAngle(Line(P, B1), Line(C, A), length=0.3)
    ra_C1 = RightAngle(Line(P, C1), Line(A, B), length=0.3)

    self.add(triangle)
    self.add(line_PA1, line_PB1, line_PC1)
    self.add(seg_PA, seg_PB, seg_PC)
    self.add(lbl_A, lbl_B, lbl_C, lbl_P, lbl_A1, lbl_B1, lbl_C1)
    self.add(ra_A1, ra_B1, ra_C1)
        # --- AI GENERATED CODE END ---

```
---

### ID Zadacha: sigma137_p1864 - Неравенство со растојанија во триаголник
**Date Dodadeno:** 2026-01-07 22:28
**Python/Manim Kod:**
```python
from manim import *

class Task_sigma137_p1864(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE
    
    # Triangle vertices
    A = UP * 3
    B = LEFT * 3 + DOWN * 2
    C = RIGHT * 3 + DOWN * 2
    
    # Point P inside
    P = DOWN * 0.5 + RIGHT * 0.2
    
    # Projections
    # Function to find projection of P onto line XY
    def get_projection(P, X, Y):
        # Vector XY
        XY = Y - X
        # Vector XP
        XP = P - X
        # Projection scalar
        t = np.dot(XP, XY) / np.dot(XY, XY)
        return X + t * XY
        
    A1 = get_projection(P, B, C)
    B1 = get_projection(P, C, A)
    C1 = get_projection(P, A, B)
    
    # Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    
    # Perpendiculars from P
    line_PA1 = DashedLine(P, A1, color=BLUE)
    line_PB1 = DashedLine(P, B1, color=BLUE)
    line_PC1 = DashedLine(P, C1, color=BLUE)
    
    # Segments PA, PB, PC
    seg_PA = Line(P, A, color=RED, stroke_width=3)
    seg_PB = Line(P, B, color=RED, stroke_width=3)
    seg_PC = Line(P, C, color=RED, stroke_width=3)
    
    # Labels
    lbl_A = MathTex("A").next_to(A, UP)
    lbl_B = MathTex("B").next_to(B, DL)
    lbl_C = MathTex("C").next_to(C, DR)
    lbl_P = MathTex("P").next_to(P, UP, buff=0.1)
    lbl_A1 = MathTex("A_1").next_to(A1, DOWN)
    lbl_B1 = MathTex("B_1").next_to(B1, UR, buff=0.1)
    lbl_C1 = MathTex("C_1").next_to(C1, UL, buff=0.1)
    
    # Right angle markers
    ra_A1 = RightAngle(Line(P, A1), Line(B, C), length=0.3)
    ra_B1 = RightAngle(Line(P, B1), Line(C, A), length=0.3)
    ra_C1 = RightAngle(Line(P, C1), Line(A, B), length=0.3)

    self.add(triangle)
    self.add(line_PA1, line_PB1, line_PC1)
    self.add(seg_PA, seg_PB, seg_PC)
    self.add(lbl_A, lbl_B, lbl_C, lbl_P, lbl_A1, lbl_B1, lbl_C1)
    self.add(ra_A1, ra_B1, ra_C1)
        # --- AI GENERATED CODE END ---

```
---

### ID Zadacha: sigma137_p1864 - Неравенство со растојанија во триаголник
**Date Dodadeno:** 2026-01-07 22:28
**Python/Manim Kod:**
```python
from manim import *

class Task_sigma137_p1864(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE
    
    # Triangle vertices
    A = UP * 3
    B = LEFT * 3 + DOWN * 2
    C = RIGHT * 3 + DOWN * 2
    
    # Point P inside
    P = DOWN * 0.5 + RIGHT * 0.2
    
    # Projections
    # Function to find projection of P onto line XY
    def get_projection(P, X, Y):
        # Vector XY
        XY = Y - X
        # Vector XP
        XP = P - X
        # Projection scalar
        t = np.dot(XP, XY) / np.dot(XY, XY)
        return X + t * XY
        
    A1 = get_projection(P, B, C)
    B1 = get_projection(P, C, A)
    C1 = get_projection(P, A, B)
    
    # Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    
    # Perpendiculars from P
    line_PA1 = DashedLine(P, A1, color=BLUE)
    line_PB1 = DashedLine(P, B1, color=BLUE)
    line_PC1 = DashedLine(P, C1, color=BLUE)
    
    # Segments PA, PB, PC
    seg_PA = Line(P, A, color=RED, stroke_width=3)
    seg_PB = Line(P, B, color=RED, stroke_width=3)
    seg_PC = Line(P, C, color=RED, stroke_width=3)
    
    # Labels
    lbl_A = MathTex("A").next_to(A, UP)
    lbl_B = MathTex("B").next_to(B, DL)
    lbl_C = MathTex("C").next_to(C, DR)
    lbl_P = MathTex("P").next_to(P, UP, buff=0.1)
    lbl_A1 = MathTex("A_1").next_to(A1, DOWN)
    lbl_B1 = MathTex("B_1").next_to(B1, UR, buff=0.1)
    lbl_C1 = MathTex("C_1").next_to(C1, UL, buff=0.1)
    
    # Right angle markers
    ra_A1 = RightAngle(Line(P, A1), Line(B, C), length=0.3)
    ra_B1 = RightAngle(Line(P, B1), Line(C, A), length=0.3)
    ra_C1 = RightAngle(Line(P, C1), Line(A, B), length=0.3)

    self.add(triangle)
    self.add(line_PA1, line_PB1, line_PC1)
    self.add(seg_PA, seg_PB, seg_PC)
    self.add(lbl_A, lbl_B, lbl_C, lbl_P, lbl_A1, lbl_B1, lbl_C1)
    self.add(ra_A1, ra_B1, ra_C1)
        # --- AI GENERATED CODE END ---

```
---

### ID Zadacha: sigma137_p1867 - Аголот $\angle AEF$ преку симетрија
**Date Dodadeno:** 2026-01-07 22:58
**Python/Manim Kod:**
```python
from manim import *

class Task_sigma137_p1867(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
def construct(self):
    self.camera.background_color = WHITE
    
    # Coordinates
    # Let C be origin for calculation, then rotate
    # Easier: Let H be origin (0,0). AB is on x-axis.
    H = ORIGIN
    # Let CH = h = 3
    C = UP * 3
    # Let AH = 2, HB = 4.5 (arbitrary for right triangle)
    # Actually, h^2 = p*q. 3^2 = 2 * 4.5. Correct.
    A = LEFT * 2
    B = RIGHT * 4.5
    
    # E is on CH. Let E be (0, 1.5)
    E = UP * 1.5
    
    # F is on BH (positive x-axis). Let F be (2.5, 0)
    F = RIGHT * 2.5
    
    # D is on BC. We need to find D such that angle conditions hold.
    # This is hard to construct directly from angles without solving.
    # Let's just place D on BC visually.
    # Line BC equation: y - 0 = (3-0)/(0-4.5) * (x - 4.5) => y = -2/3 (x - 4.5)
    # Let x_D = 3. y_D = -2/3 * (3 - 4.5) = -2/3 * (-1.5) = 1.
    D = np.array([3, 1, 0])
    
    # E_prime (symmetric to E wrt AB)
    E_prime = DOWN * 1.5
    
    # Mobjects
    triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
    altitude = Line(C, H, color=BLACK, stroke_width=2)
    
    # Points
    pts = VGroup(Dot(A), Dot(B), Dot(C), Dot(H), Dot(E), Dot(F), Dot(D), Dot(E_prime))
    
    # Segments for the problem
    seg_AE = Line(A, E, color=BLUE)
    seg_EF = Line(E, F, color=BLUE)
    seg_FD = Line(F, D, color=BLUE)
    seg_AE_prime = DashedLine(A, E_prime, color=RED)
    seg_E_prime_F = DashedLine(E_prime, F, color=RED)
    seg_DE_prime = DashedLine(D, E_prime, color=RED)
    
    # Labels
    lbl_A = MathTex("A").next_to(A, DL)
    lbl_B = MathTex("B").next_to(B, DR)
    lbl_C = MathTex("C").next_to(C, UP)
    lbl_H = MathTex("H").next_to(H, DL, buff=0.1)
    lbl_E = MathTex("E").next_to(E, LEFT)
    lbl_F = MathTex("F").next_to(F, DOWN)
    lbl_D = MathTex("D").next_to(D, UR, buff=0.1)
    lbl_Ep = MathTex("E'").next_to(E_prime, DOWN)
    
    self.add(triangle, altitude)
    self.add(seg_AE, seg_EF, seg_FD, seg_AE_prime, seg_E_prime_F, seg_DE_prime)
    self.add(pts)
    self.add(lbl_A, lbl_B, lbl_C, lbl_H, lbl_E, lbl_F, lbl_D, lbl_Ep)
    
    # Right angle at H
    self.add(RightAngle(Line(C, H), Line(H, B), length=0.3))
        # --- AI GENERATED CODE END ---

```
---
