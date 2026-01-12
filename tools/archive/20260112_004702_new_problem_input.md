---
problem_id: sigma139_y4_p3
title: Итерации на квадратна функција
grade: 12
difficulty: 6
tags:
  - functions
  - quadratic_function
  - proof
  - composition
source: Sigma 139, Cetvrta godina, Zadaca 3
type: algebra
---

# Текст на задачата
Квадратниот трином $f(x) = ax^2 + bx + c$ е таков што равенката $f(x) = x$ нема реални решенија. Докажи дека и равенката $f(f(x)) = x$ нема реални решенија.

# Решение
## Стратегија
Ова е класична задача за фиксни точки на функција.
1.  Условот „$f(x) = x$ нема реални решенија“ значи дека графикот на $f(x)$ не ја сече правата $y=x$.
2.  Бидејќи $f(x)$ е непрекината функција (парабола), ова значи дека целиот график е или строго над правата $y=x$ (т.е. $f(x) > x$ за секое $x$) или строго под неа (т.е. $f(x) < x$ за секое $x$).
3.  Ќе го искористиме ова својство за да покажеме дека истото важи и за $f(f(x))$. Ако $f(x) > x$, тогаш $f(f(x)) > f(x) > x$, па $f(f(x)) \neq x$.

## Чекор по чекор

**Чекор 1: Анализа на условот**
Равенката $f(x) = x$ е еквивалентна на $f(x) - x = 0$.
Бидејќи оваа равенка нема реални решенија, функцијата $g(x) = f(x) - x$ нема нули.
Бидејќи $g(x)$ е квадратна функција (непрекината), таа мора да биде или секогаш позитивна или секогаш негативна.

Имаме два случаи:
1.  $f(x) - x > 0$ за секое $x \in \mathbb{R}$. Односно, $f(x) > x$.
2.  $f(x) - x < 0$ за секое $x \in \mathbb{R}$. Односно, $f(x) < x$.

**Чекор 2: Анализа на првиот случај**
Нека $f(x) > x$ за секое $x \in \mathbb{R}$.
Да го разгледаме изразот $f(f(x))$.
Во неравенството $f(t) > t$, да ставиме $t = f(x)$.
Добиваме:
$$ f(f(x)) > f(x) $$
Но, од почетната претпоставка знаеме дека $f(x) > x$.
Со комбинирање на двете неравенства:
$$ f(f(x)) > f(x) > x $$
Следи дека $f(f(x)) > x$ за секое $x$.
Значи, равенката $f(f(x)) = x$ нема реални решенија (бидејќи левата страна е секогаш строго поголема од десната).

**Чекор 3: Анализа на вториот случај**
Нека $f(x) < x$ за секое $x \in \mathbb{R}$.
Слично како претходно, во неравенството $f(t) < t$ ставаме $t = f(x)$.
Добиваме:
$$ f(f(x)) < f(x) $$
Од почетната претпоставка знаеме дека $f(x) < x$.
Со комбинирање:
$$ f(f(x)) < f(x) < x $$
Следи дека $f(f(x)) < x$ за секое $x$.
Значи, и во овој случај равенката $f(f(x)) = x$ нема реални решенија.

**Заклучок:**
Во двата можни случаи докажавме дека $f(f(x)) \neq x$ за секое реално $x$.

# Pedagogical Notes
1.  **Основна идеја:** Ако функцијата $f$ „го поместува“ $x$ секогаш во иста насока (секогаш нагоре или секогаш надолу), тогаш двојната примена на функцијата ќе го помести $x$ уште подалеку во истата насока. Затоа е невозможно да се вратиме на почетната точка $x$.
2.  **Совет од Олимпиец:** Ова тврдење важи не само за квадратни функции, туку за која било непрекината функција дефинирана на $\mathbb{R}$. Клучното својство е непрекинатоста, која гарантира зачувување на знакот на $f(x)-x$.
3.  **Чести грешки:** Учениците понекогаш се обидуваат да ја решат равенката $f(f(x))=x$ алгебарски. Ова води до равенка од 4-ти степен која е многу тешка за анализа без овој логички пристап.

# Manim Code
```python
from manim import *

class FunctionIteration(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Axes
        axes = Axes(
            x_range=[-2, 4, 1],
            y_range=[-2, 4, 1],
            axis_config={"color": BLACK},
            x_length=6,
            y_length=6
        )
        
        # Line y=x
        line_yx = axes.plot(lambda x: x, color=GRAY, stroke_width=2)
        label_yx = MathTex("y=x", color=GRAY).next_to(line_yx, UR)
        
        # Case 1: f(x) > x
        func1 = axes.plot(lambda x: 0.5*(x-1)**2 + 2, color=BLUE, x_range=[-1, 3])
        label_f1 = MathTex("f(x) > x", color=BLUE).next_to(func1, UP)
        
        # Animation Case 1
        self.play(Create(axes), Create(line_yx), Write(label_yx))
        self.play(Create(func1), Write(label_f1))
        
        # Point movement logic
        x0 = 0.5
        p0 = Dot(axes.c2p(x0, x0), color=RED)
        p1 = Dot(axes.c2p(x0, 0.5*(x0-1)**2 + 2), color=RED) # (x, f(x))
        # f(x0) value
        fx0 = 0.5*(x0-1)**2 + 2
        p2 = Dot(axes.c2p(fx0, fx0), color=RED) # (f(x), f(x)) on y=x line
        p3 = Dot(axes.c2p(fx0, 0.5*(fx0-1)**2 + 2), color=RED) # (f(x), f(f(x)))
        
        # Arrows
        arrow1 = Arrow(p0.get_center(), p1.get_center(), color=GREEN, buff=0)
        arrow2 = Arrow(p1.get_center(), p2.get_center(), color=GREEN, buff=0) # Project to y=x
        arrow3 = Arrow(p2.get_center(), p3.get_center(), color=GREEN, buff=0)
        
        self.play(Create(p0))
        self.play(GrowArrow(arrow1), Create(p1))
        self.play(GrowArrow(arrow2), Create(p2))
        self.play(GrowArrow(arrow3), Create(p3))
        
        # Text explanation
        text = MathTex(
            r"f(x) > x \implies f(f(x)) > f(x) > x",
            color=BLACK
        ).to_corner(UL)
        self.play(Write(text))
        
        self.wait(2)