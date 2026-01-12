---
problem_id: sigma_138_1889
title: Геометриско место на средини меѓу две прави
grade: 11
difficulty: 6
type: geometry
tags:
  - locus
  - analytic_geometry
  - hyperbola
primary_skill: coordinate_geometry
related_skills:
  - parametric_equations
  - elimination_method
source: Sigma 138, Problem 1889
---

# Геометриско место на средини меѓу две прави

# Текст на задачата
Дадени се две заемно нормални прави $p$ и $q$ и една точка $O$ што не лежи на ниедна од правите $p$ и $q$. Една променлива права низ точката $O$ ги сече правите $p$ и $q$ соодветно во точките $A$ и $B$. Да се најде геометриското место на средините $M$ од отсечките $AB$.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Најмоќната алатка за наоѓање на геометриско место на точки (ГМТ) кога имаме фиксни прави и променливи пресеци е **аналитичката геометрија**. Постави го координатниот почеток во точката $O(0,0)$.

$$O(0,0)$$

2. Бидејќи правите $p$ и $q$ се нормални, но не минуваат низ $O$, можеме да ги поставиме паралелно со оските. Нека $p: y = a$ и $q: x = b$.

$$y - kx = 0$$

3. Променливата права низ $O$ има равенка $y = kx$. Изрази ги координатите на пресечните точки $A$ (со $p$) и $B$ (со $q$) во зависност од параметарот $k$.

4. Најди ги координатите на средината $M(x, y)$ преку $k$. Потоа, елиминирај го параметарот $k$ од системот равенки за да добиеш врска само меѓу $x$ и $y$.

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Кога слушаме за „променлива права“ и „геометриско место на точки“, треба да размислуваме за тоа како точката $M$ се движи.
1.  Кога правата низ $O$ ќе се приближи да биде паралелна со правата $p$, пресечната точка $A$ оди во бесконечност. Тоа значи дека и средината $M$ ќе оди во бесконечност.
2.  Истото се случува кога правата се приближува кон паралела со $q$.
3.  Крива која има две асимптоти (оди во бесконечност во два правци) најчесто е **хипербола**.

Затоа, очекуваме равенката што ќе ја добиеме да биде од втор ред и да претставува хипербола. Најелегантен начин да се докаже ова е преку координатен систем, поставувајќи ја точката $O$ во центарот.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Поставување на координатен систем</summary>

Го избираме координатниот систем така што координатниот почеток е во точката $O(0,0)$.
Бидејќи правите $p$ и $q$ се заемно нормални, ги поставуваме координатните оски паралелно со нив.
*   Правата $p$ е паралелна со $x$-оската: нејзината равенка е $y = a$ (каде $a \neq 0$ бидејќи $O \notin p$).
*   Правата $q$ е паралелна со $y$-оската: нејзината равенка е $x = b$ (каде $b \neq 0$ бидејќи $O \notin q$).

</details>

<details>
<summary>Чекор 2: Параметризација на променливата права</summary>

Нека променливата права $l$ што минува низ $O$ има равенка:

$$y = kx$$

каде $k$ е реален параметар (коефициент на правец).

Ги наоѓаме пресечните точки:
1.  **Точка $A$ (пресек на $l$ и $p$):**
    Заменуваме $y=a$ во $y=kx$:
    $$a = kx_A \implies x_A = \frac{a}{k}$$
    Значи, $A\left(\frac{a}{k}, a\right)$.

2.  **Точка $B$ (пресек на $l$ и $q$):**
    Заменуваме $x=b$ во $y=kx$:
    $$y_B = kb$$
    Значи, $B(b, kb)$.

</details>

<details>
<summary>Чекор 3: Координати на средината $M$</summary>

Нека $M(x, y)$ е средина на отсечката $AB$. Според формулите за средина:

$$x = \frac{x_A + x_B}{2} = \frac{\frac{a}{k} + b}{2}$$

$$y = \frac{y_A + y_B}{2} = \frac{a + kb}{2}$$

Ова е параметарски запис на кривата. Наша цел е да го елиминираме $k$.

</details>

<details>
<summary>Чекор 4: Елиминација на параметарот $k$</summary>

Од втората равенка го изразуваме $k$:
$$2y = a + kb \implies kb = 2y - a \implies k = \frac{2y - a}{b}$$

Сега го заменуваме ова $k$ во првата равенка за $x$:
$$2x = \frac{a}{k} + b$$
$$2x - b = \frac{a}{k}$$

Заменуваме за $k$:
$$2x - b = \frac{a}{\frac{2y - a}{b}}$$
$$2x - b = \frac{ab}{2y - a}$$

Множиме накрсно:
$$(2x - b)(2y - a) = ab$$

Ги отвораме заградите:
$$4xy - 2ax - 2by + ab = ab$$

Поништуваме $ab$ од двете страни:
$$4xy - 2ax - 2by = 0$$

Делиме со 2:
$$2xy - ax - by = 0$$

Или запишано како во решението:

$$2xy = ax + by$$

</details>

**Краен одговор:** Бараното геометриско место на точки е хипербола со равенка $\boxed{2xy - ax - by = 0}$.

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Кога решавате задачи со ГМТ аналитички, секогаш обидете се крајната равенка да ја доведете до препознатлив облик. Равенката $(2x-b)(2y-a) = ab$ јасно покажува дека се работи за хипербола чиј центар е во точката $(b/2, a/2)$ и чии асимптоти се правите $x = b/2$ и $y = a/2$.
2.  **Геометриско значење:** Центарот на оваа хипербола $(b/2, a/2)$ е всушност средината на отсечката што го поврзува координатниот почеток $O$ со пресекот на правите $p$ и $q$ (точката $(b,a)$).
3.  **Чести Грешки:** Внимавајте при делење со $k$. Случаите кога правата е вертикална ($x=0$) или хоризонтална ($y=0$) треба да се разгледаат како гранични случаи, но во општата равенка тие се природно вклучени (освен ако $a$ или $b$ се 0, што е исклучено со условот).

### 🔗 Поврзани вештини
* **Примарна вештина:** Аналитичка геометрија (Coordinate Geometry).
* **Потребни предзнаења:** Равенка на права, Формула за средина на отсечка, Елиминација на параметар.

# Manim Code
```python
from manim import *

class LocusHyperbola(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # --- Setup ---
        # O at origin
        # p: y = 2
        # q: x = 3
        a_val = 2.0
        b_val = 3.0
        
        axes = Axes(
            x_range=[-4, 8, 1],
            y_range=[-4, 6, 1],
            axis_config={"color": BLACK, "stroke_width": 2}
        )
        
        # Points and Lines
        O = axes.c2p(0, 0)
        dot_O = Dot(O, color=BLACK)
        label_O = MathTex("O", color=BLACK).next_to(dot_O, DL, buff=0.1)
        
        line_p = axes.get_horizontal_line(axes.c2p(b_val, a_val), color=BLUE, line_func=Line).set_length(20)
        line_q = axes.get_vertical_line(axes.c2p(b_val, a_val), color=BLUE, line_func=Line).set_length(20)
        
        label_p = MathTex("p: y=a", color=BLUE).next_to(axes.c2p(-2, a_val), UP)
        label_q = MathTex("q: x=b", color=BLUE).next_to(axes.c2p(b_val, -2), RIGHT)
        
        # Variable Line and Points
        # k varies. Let's animate k from 0.2 to 5
        k_tracker = ValueTracker(0.5)
        
        def get_line_points():
            k = k_tracker.get_value()
            # Line y = kx
            # Intersection A with y=a => x = a/k
            pt_A = axes.c2p(a_val/k, a_val)
            # Intersection B with x=b => y = k*b
            pt_B = axes.c2p(b_val, k*b_val)
            return pt_A, pt_B

        line_l = always_redraw(lambda: Line(
            start=axes.c2p(-1, -k_tracker.get_value()), # Just for visual extension
            end=get_line_points()[1], # Extend to B
            color=GRAY, stroke_width=2
        ).set_length(15)) # Make it long enough
        
        dot_A = always_redraw(lambda: Dot(get_line_points()[0], color=RED))
        dot_B = always_redraw(lambda: Dot(get_line_points()[1], color=RED))
        
        label_A = always_redraw(lambda: MathTex("A", color=RED).next_to(dot_A, UP))
        label_B = always_redraw(lambda: MathTex("B", color=RED).next_to(dot_B, RIGHT))
        
        # Midpoint M
        dot_M = always_redraw(lambda: Dot(
            (get_line_points()[0] + get_line_points()[1]) / 2,
            color=GREEN
        ))
        label_M = always_redraw(lambda: MathTex("M", color=GREEN).next_to(dot_M, UL, buff=0.1))
        
        # Trace
        trace = TracedPath(dot_M.get_center, stroke_color=GREEN, stroke_width=4, dissipating_time=None)
        
        # Hyperbola Equation Visualization
        # 2xy - ax - by = 0 => y(2x - b) = ax => y = ax / (2x - b)
        hyperbola_graph = axes.plot(
            lambda x: (a_val * x) / (2 * x - b_val),
            x_range=[b_val/2 + 0.1, 8], # Right branch
            color=GREEN, stroke_opacity=0.5
        )
        hyperbola_graph_left = axes.plot(
            lambda x: (a_val * x) / (2 * x - b_val),
            x_range=[-4, b_val/2 - 0.1], # Left branch
            color=GREEN, stroke_opacity=0.5
        )

        # --- Animation ---
        self.add(axes, dot_O, label_O)
        self.play(Create(line_p), Create(line_q))
        self.play(Write(label_p), Write(label_q))
        
        self.add(line_l, dot_A, dot_B, label_A, label_B, dot_M, label_M, trace)
        
        # Animate k
        self.play(k_tracker.animate.set_value(2.5), run_time=3, rate_func=linear)
        self.play(k_tracker.animate.set_value(0.2), run_time=3, rate_func=linear)
        
        # Show the full locus
        self.play(Create(hyperbola_graph), Create(hyperbola_graph_left))
        
        equation = MathTex("2xy - ax - by = 0", color=GREEN).to_corner(UR)
        box = SurroundingRectangle(equation, color=BLACK, fill_color=WHITE, fill_opacity=0.8)
        self.play(FadeIn(box), Write(equation))
        
        self.wait(2)
```