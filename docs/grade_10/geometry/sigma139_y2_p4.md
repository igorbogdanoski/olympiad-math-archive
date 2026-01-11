---
difficulty: 6
grade: 10
problem_id: sigma139_y2_p4
source: Sigma 139, Vtora godina, Zadaca 4
tags:
- geometry
- locus
- orthocenter
- coordinates
title: Геометриско место на точки (Ортоцентар)
type: geometry
---

## Текст на задачата

Дадени се точките $A(-3, 0)$ и $B(3, 0)$. Нека $C$ е точка која се движи по правата $y = 3$. Најди го геометриското место на ортоцентрите на триаголниците $ABC$.

## Решение

## Стратегија

Ова е задача за наоѓање на **геометриско место на точки (ГМТ)**.

1. Точките $A$ и $B$ се фиксни на $x$-оската.
2. Точката $C$ има променлива $x$-координата, но фиксна $y$-координата ($y_C = 3$). Нека $C(t, 3)$.
3. Треба да ги најдеме координатите на ортоцентарот $H(x, y)$ во зависност од параметарот $t$.
4. Потоа ќе го елиминираме параметарот $t$ за да добиеме равенка која ги поврзува $x$ и $y$. Оваа равенка ќе го претставува бараното ГМТ.

## Чекор по чекор

<details>
<summary>Чекор 1: Поставување на координатите</summary>

* $A(-3, 0)$
* $B(3, 0)$
* $C(t, 3)$, каде $t \in \mathbb{R}$.

</details>

<details>
<summary>Чекор 2: Наоѓање на висините</summary>

Ортоцентарот $H$ е пресек на висините на триаголникот.

1. **Висина $h_C$ (спуштена од $C$ кон $AB$):**
    Бидејќи $A$ и $B$ лежат на $x$-оската ($y=0$), страната $AB$ е хоризонтална.
    Затоа, висината $h_C$ е вертикална права што минува низ $C(t, 3)$.
    Равенката на $h_C$ е:
    $ x = t $
    Ова значи дека $x$-координатата на ортоцентарот $H$ е иста со $x$-координатата на $C$.
    $ x_H = t $

2. **Висина $h_A$ (спуштена од $A$ кон $BC$):**
    Прво го наоѓаме коефициентот на правец на правата $BC$.
    $B(3, 0)$, $C(t, 3)$.
    $ k_{BC} = \frac{y_C - y_B}{x_C - x_B} = \frac{3 - 0}{t - 3} = \frac{3}{t - 3} $
    Висината $h_A$ е нормална на $BC$, па нејзиниот коефициент на правец е:
    $ k_{h_A} = -\frac{1}{k_{BC}} = -\frac{t - 3}{3} = \frac{3 - t}{3} $
    Равенката на правата $h_A$ која минува низ $A(-3, 0)$ е:
    $ y - y_A = k_{h_A}(x - x_A) $
    $ y - 0 = \frac{3 - t}{3}(x - (-3)) $
    $ y = \frac{3 - t}{3}(x + 3) $

</details>

<details>
<summary>Чекор 3: Наоѓање на координатите на $H$</summary>

Ортоцентарот $H$ е пресек на $h_C$ и $h_A$.
Веќе знаеме дека $x = t$ (од $h_C$).
Заменуваме $x = t$ во равенката за $h_A$ за да го најдеме $y$:
$ y = \frac{3 - t}{3}(t + 3) $
$ y = \frac{3^2 - t^2}{3} $
$ y = \frac{9 - t^2}{3} $
$ y = 3 - \frac{t^2}{3} $

</details>

<details>
<summary>Чекор 4: Елиминација на параметарот $t$</summary>

Имаме систем параметарски равенки за $H(x, y)$:

1. $x = t$
2. $y = 3 - \frac{t^2}{3}$

Заменуваме $t = x$ во втората равенка:
$ y = 3 - \frac{x^2}{3} $
Или запишано во стандардна форма:
$ x^2 = -3(y - 3) $

</details>

<details>
<summary>Чекор 5: Анализа на кривата</summary>

Равенката $y = -\frac{1}{3}x^2 + 3$ претставува **парабола**.

* Темето е во точката $(0, 3)$.
* Отворена е надолу (поради минусот пред $x^2$).
* Минува низ точките $A(-3, 0)$ и $B(3, 0)$? Да провериме:
    За $x=3$, $y = 3 - 9/3 = 0$. Точно.

</details>

**Дополнителна дискусија:**
Дали сите точки од параболата се можни ортоцентри?
Ако $C$ се совпадне со $A$ или $B$ (т.е. $t = \pm 3$), триаголникот дегенерира? Не, $C$ е на висина $y=3$, а $A, B$ се на $y=0$, па $C$ никогаш не се совпаѓа со $A$ или $B$.
Но, ако $t=3$, тогаш $C(3,3)$. Триаголникот е правоаголен кај $B$. Ортоцентарот е во темето на правиот агол, т.е. $B(3,0)$.
Нашата формула дава $y = 3 - 3^2/3 = 0$, $x=3$. Точно.
Ако $t=-3$, ортоцентарот е $A(-3,0)$.
Ако $t=0$, $C(0,3)$. Триаголникот е рамнокрак. $H$ е на $y$-оската. $y = 3 - 0 = 3$. $H(0,3) = C$. Ова е точно само ако триаголникот е остроаголен? Не, ако $C(0,3)$, тогаш $AC$ и $BC$ имаат наклони $\pm 1$. Аголот кај $C$ е прав?
$k_{AC} = 3/3 = 1$, $k_{BC} = 3/-3 = -1$. Производот е $-1$. Да, аголот кај $C$ е прав. Ортоцентарот е во $C$.
Формулата дава $y=3$. Точно.

**Заклучок:**
Геометриското место на точки е параболата со равенка:
$$ y = 3 - \frac{x^2}{3} $$

## Pedagogical Notes

1. **Основна идеја:** Кога барате ГМТ со подвижна точка, секогаш изразете ги координатите на бараната точка преку параметар (во овој случај $t$), а потоа елиминирајте го параметарот.
2. **Совет од Олимпиец:** Изборот на координатен систем е клучен. Овде тој е веќе даден, но симетријата на точките $A$ и $B$ околу $y$-оската сугерира дека и резултатот ќе биде симетрична крива (парабола со теме на $y$-оската).
3. **Чести грешки:** Внимавајте на делење со нула. Кога пресметувавме $k_{BC} = \frac{3}{t-3}$, ова не е дефинирано за $t=3$. Овој случај (правоаголен триаголник) треба да се провери посебно, иако во овој случај се вклопува во општата формула.

#```python
from manim import *

class LocusScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": BLACK},
            x_length=8,
            y_length=5
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y").set_color(BLACK)

        # Fixed points
        A = axes.c2p(-3, 0)
        B = axes.c2p(3, 0)

        # Locus curve (Parabola)
        parabola = axes.plot(lambda x: 3 - x**2/3, color=RED)

        # Moving point C and Orthocenter H
        t_tracker = ValueTracker(0)

        C = always_redraw(lambda: Dot(axes.c2p(t_tracker.get_value(), 3), color=BLUE))
        H = always_redraw(lambda: Dot(axes.c2p(t_tracker.get_value(), 3 - t_tracker.get_value()**2/3), color=RED))

        # Triangle lines
        lines = always_redraw(lambda: VGroup(
            Line(A, B, color=BLACK),
            Line(B, C.get_center(), color=BLACK),
            Line(C.get_center(), A, color=BLACK)
        ))

        # Altitudes
        altitudes = always_redraw(lambda: VGroup(
            # h_C (vertical)
            Line(C.get_center(), axes.c2p(t_tracker.get_value(), 0), color=GREEN, stroke_opacity=0.5),
            # h_A (perp to BC)
            Line(A, H.get_center(), color=GREEN, stroke_opacity=0.5)
        ))

        # Labels
        lbl_A = MathTex("A", color=BLACK).next_to(A, DL, buff=0.1)
        lbl_B = MathTex("B", color=BLACK).next_to(B, DR, buff=0.1)
        lbl_C = MathTex("C", color=BLUE).next_to(C, UP, buff=0.1)
        lbl_H = MathTex("H", color=RED).next_to(H, RIGHT, buff=0.1)

        # Animation
        self.play(Create(axes), Write(labels))
        self.play(Create(Dot(A)), Create(Dot(B)), Write(lbl_A), Write(lbl_B))
        self.play(Create(C), Write(lbl_C), Create(lines))
        self.play(Create(H), Write(lbl_H), Create(altitudes))

        # Trace
        trace = TracedPath(H.get_center, stroke_color=RED, stroke_width=4)
        self.add(trace)

        # Move C
        self.play(t_tracker.animate.set_value(4), run_time=3)
        self.play(t_tracker.animate.set_value(-4), run_time=6)
        self.play(t_tracker.animate.set_value(0), run_time=3)

        # Show equation
        eq = MathTex(r"y = 3 - \frac{x^2}{3}", color=RED).to_corner(UL)
        self.play(Write(eq))

        self.wait(2)

---
### 🎨 Визуелизација
![Илустрација](/assets/images/sigma139_y2_p4/sigma139_y2_p4.png)