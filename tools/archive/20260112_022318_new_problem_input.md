---
problem_id: sigma139_p1899
title: Систем равенки со квадрати
grade: 11
difficulty: 6
tags:
  - algebra
  - system_of_equations
  - difference_of_squares
  - substitution
source: Sigma 139, Zadaca 1899
type: algebra
---

# Текст на задачата
Во множеството на реалните броеви реши го системот равенки:
$$
\begin{cases}
(x + y)^2 = z^2 + 1 \\
(y + z)^2 = x^2 + 5 \\
(z + x)^2 = y^2 + 10
\end{cases}
$$

# Решение
## Стратегија
Системот е симетричен по форма, но константите се различни.
Клучната идеја е да се искористи формулата за разлика на квадрати.
Ако го префрлиме членот со квадрат од десната на левата страна, добиваме изрази од типот $(x+y)^2 - z^2 = 1$, што се факторизира како $(x+y-z)(x+y+z) = 1$.
Ова ни овозможува да воведеме нова променлива $S = x+y+z$, што значително ќе го поедностави системот.

## Чекор по чекор

**Чекор 1: Трансформација на равенките**
Ги препишуваме равенките со префрлање на квадратите на левата страна:
1.  $(x + y)^2 - z^2 = 1$
2.  $(y + z)^2 - x^2 = 5$
3.  $(z + x)^2 - y^2 = 10$

**Чекор 2: Факторизација**
Користиме $A^2 - B^2 = (A-B)(A+B)$.
1.  $(x + y - z)(x + y + z) = 1$
2.  $(y + z - x)(y + z + x) = 5$
3.  $(z + x - y)(z + x + y) = 10$

**Чекор 3: Воведување смена**
Нека $S = x + y + z$.
Забележуваме дека:
*   $x + y - z = (x + y + z) - 2z = S - 2z$
*   $y + z - x = (x + y + z) - 2x = S - 2x$
*   $z + x - y = (x + y + z) - 2y = S - 2y$

Системот станува:
1.  $(S - 2z)S = 1 \implies S^2 - 2zS = 1$
2.  $(S - 2x)S = 5 \implies S^2 - 2xS = 5$
3.  $(S - 2y)S = 10 \implies S^2 - 2yS = 10$

**Чекор 4: Наоѓање на $S$**
Ги собираме трите нови равенки:
$$ (S^2 - 2zS) + (S^2 - 2xS) + (S^2 - 2yS) = 1 + 5 + 10 $$
$$ 3S^2 - 2S(x + y + z) = 16 $$
Бидејќи $x + y + z = S$, заменуваме:
$$ 3S^2 - 2S(S) = 16 $$
$$ 3S^2 - 2S^2 = 16 $$
$$ S^2 = 16 $$
Значи, $S = 4$ или $S = -4$.

**Чекор 5: Решавање за $x, y, z$**
Имаме два случаи.

**Случај 1: $S = 4$**
Враќаме во равенките од Чекор 3:
1.  $4(4 - 2z) = 1 \implies 16 - 8z = 1 \implies 8z = 15 \implies z = \frac{15}{8}$
2.  $4(4 - 2x) = 5 \implies 16 - 8x = 5 \implies 8x = 11 \implies x = \frac{11}{8}$
3.  $4(4 - 2y) = 10 \implies 16 - 8y = 10 \implies 8y = 6 \implies y = \frac{6}{8} = \frac{3}{4}$

Проверка за $S$: $x+y+z = \frac{11}{8} + \frac{6}{8} + \frac{15}{8} = \frac{32}{8} = 4$. Точно.

**Случај 2: $S = -4$**
1.  $-4(-4 - 2z) = 1 \implies 16 + 8z = 1 \implies 8z = -15 \implies z = -\frac{15}{8}$
2.  $-4(-4 - 2x) = 5 \implies 16 + 8x = 5 \implies 8x = -11 \implies x = -\frac{11}{8}$
3.  $-4(-4 - 2y) = 10 \implies 16 + 8y = 10 \implies 8y = -6 \implies y = -\frac{6}{8} = -\frac{3}{4}$

Проверка за $S$: $x+y+z = -\frac{11}{8} - \frac{6}{8} - \frac{15}{8} = -\frac{32}{8} = -4$. Точно.

**Заклучок:**
Системот има две решенија:
1.  $(x, y, z) = \left( \frac{11}{8}, \frac{3}{4}, \frac{15}{8} \right)$
2.  $(x, y, z) = \left( -\frac{11}{8}, -\frac{3}{4}, -\frac{15}{8} \right)$

# Pedagogical Notes
1.  **Основна идеја:** Препознавањето на структурата $A^2 - B^2$ е клучно. Кога имате систем каде променливите се „вртат“ циклусно, често е корисно да се воведе збирот $S = x+y+z$ како нова променлива.
2.  **Совет од Олимпиец:** Наместо да изразувате една променлива преку друга (што би довело до комплицирани корени), обидете се да ги соберете равенките. Оваа техника на „сумирање“ често ги поништува поединечните променливи и остава равенка само по $S$.
3.  **Чести грешки:** Заборавање на негативното решение за $S$ ($S = \pm 4$). Квадратната равенка $S^2=16$ секогаш има два корена.

# Manim Code
```python
from manim import *

class SystemOfEquations(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Систем равенки", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Original System
        sys_tex = MathTex(
            r"\begin{cases} (x+y)^2 = z^2 + 1 \\ (y+z)^2 = x^2 + 5 \\ (z+x)^2 = y^2 + 10 \end{cases}",
            color=BLACK
        ).shift(UP)
        self.play(Write(sys_tex))
        
        # Transformation
        trans_tex = MathTex(
            r"\begin{cases} (x+y)^2 - z^2 = 1 \\ (y+z)^2 - x^2 = 5 \\ (z+x)^2 - y^2 = 10 \end{cases}",
            color=BLUE
        ).next_to(sys_tex, DOWN)
        self.play(TransformFromCopy(sys_tex, trans_tex))
        
        # Factorization with S
        s_def = MathTex(r"S = x+y+z", color=RED).next_to(trans_tex, RIGHT, buff=1)
        self.play(Write(s_def))
        
        factored_tex = MathTex(
            r"\begin{cases} (S-2z)S = 1 \\ (S-2x)S = 5 \\ (S-2y)S = 10 \end{cases}",
            color=BLACK
        ).next_to(trans_tex, DOWN)
        self.play(Write(factored_tex))
        
        # Summing up
        sum_step = MathTex(
            r"S(3S - 2(x+y+z)) = 16",
            r"\implies S(3S - 2S) = 16",
            r"\implies S^2 = 16",
            color=GREEN
        ).arrange(DOWN).next_to(factored_tex, DOWN)
        
        self.play(Write(sum_step))
        
        # Final S
        s_val = MathTex(r"S = \pm 4", color=RED).next_to(sum_step, DOWN)
        self.play(Indicate(s_val))
        
        self.wait(2)