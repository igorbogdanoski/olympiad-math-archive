---
difficulty: 5
grade: 12
problem_id: sigma139_y4_p1
related_theorems:
- polynomial_expansion
- quadratic_equations
- number_theory
source: Sigma 139, Cetvrta godina, Zadaca 1
tags:
- polynomials
- factorization
- complex_roots
- quadratic_substitution
title: Равенка од четврти степен
type: algebra
---

# Текст на задачата
Реши ја равенката:
$$ x^4 + 26x^2 - x + 182 = 0 $$

# Решение
## Стратегија
Ова е полиномна равенка од четврти степен. Нема очигледни целобројни корени (делителите на 182 се $\pm 1, \pm 2, \pm 7, \pm 13, \dots$, но ниту еден не одговара).
Бидејќи коефициентите се реални, ако има комплексни корени, тие доаѓаат во конјугирани парови.
Стратегијата е да се обидеме да го разложиме полиномот на два квадратни триноми со целобројни коефициенти:
$$ (x^2 + ax + b)(x^2 + cx + d) = x^4 + 26x^2 - x + 182 $$
Бидејќи коефициентот пред $x^3$ е 0, мора $a+c=0$, т.е. $c=-a$.
Значи бараме разложување од облик:
$$ (x^2 + ax + b)(x^2 - ax + d) = 0 $$

## 📐 Детално Решение

<details>
<summary>Чекор 1: Поставување на системот равенки</summary>

Го множиме претпоставениот облик:
$$ (x^2 + ax + b)(x^2 - ax + d) = x^4 - ax^3 + dx^2 + ax^3 - a^2x^2 + adx + bx^2 - abx + bd $$
$$ = x^4 + (d - a^2 + b)x^2 + (ad - ab)x + bd $$

Ги изедначуваме коефициентите со дадената равенка $x^4 + 26x^2 - x + 182$:
1.  $d - a^2 + b = 26$
2.  $a(d - b) = -1$
3.  $bd = 182$

</details>

<details>
<summary>Чекор 2: Решавање на системот во цели броеви</summary>

Од равенката (2) $a(d-b) = -1$, бидејќи бараме целобројни коефициенти, $a$ мора да биде делител на -1.
Значи $a = 1$ или $a = -1$.
Без губење на општоста, нека $a = 1$.
Тогаш $d - b = -1$, односно $b = d + 1$.

Заменуваме во равенката (3):
$$ (d+1)d = 182 $$
$$ d^2 + d - 182 = 0 $$
Бараме два последователни цели броја чиј производ е 182.
$13 \times 14 = 182$.
Значи $d = 13$ (бидејќи $13 \times 14 = 182$) или $d = -14$ (бидејќи $-14 \times -13 = 182$).
Ако $d=13$, тогаш $b=14$.
Ако $d=-14$, тогаш $b=-13$.

Да провериме која комбинација ја задоволува равенката (1):
$d - a^2 + b = 26$
За $a=1$:
*   Случај 1 ($d=13, b=14$): $13 - 1^2 + 14 = 13 - 1 + 14 = 26$. Ова одговара!
*   Случај 2 ($d=-14, b=-13$): $-14 - 1 - 13 = -28 \neq 26$.

Значи, разложувањето е:
$$ (x^2 + x + 14)(x^2 - x + 13) = 0 $$

</details>

<details>
<summary>Чекор 3: Решавање на квадратните равенки</summary>

Равенката се распаѓа на две квадратни равенки:
1.  $x^2 + x + 14 = 0$
    $$ x_{1,2} = \frac{-1 \pm \sqrt{1^2 - 4(14)}}{2} = \frac{-1 \pm \sqrt{1 - 56}}{2} = \frac{-1 \pm \sqrt{-55}}{2} = \frac{-1 \pm i\sqrt{55}}{2} $$

2.  $x^2 - x + 13 = 0$
    $$ x_{3,4} = \frac{1 \pm \sqrt{(-1)^2 - 4(13)}}{2} = \frac{1 \pm \sqrt{1 - 52}}{2} = \frac{1 \pm \sqrt{-51}}{2} = \frac{1 \pm i\sqrt{51}}{2} $$

**Заклучок:**
Равенката има четири комплексни решенија:
$$ x \in \left\{ \frac{-1 \pm i\sqrt{55}}{2}, \frac{1 \pm i\sqrt{51}}{2} \right\} $$

# Pedagogical Notes
1.  **Основна идеја:** Методот на неопределени коефициенти (Ferrari-ев метод во поедноставена форма) е најмоќната алатка за полиноми од 4-ти степен кога нема рационални корени. Клучот е да се претпостави формата $(x^2+ax+b)(x^2-ax+d)$ поради отсуството на $x^3$.
2.  **Совет од Олимпиец:** Кога ќе добиете систем како $bd=182$ и $a(d-b)=-1$, секогаш прво барајте целобројни решенија. Бројот 182 изгледа голем, но брзо се факторизира ($2 \cdot 7 \cdot 13$). Фактот што $a$ мора да биде $\pm 1$ драстично го стеснува пребарувањето.
3.  **Чести грешки:** Грешка во знакот при формирање на системот (на пр. $d+b$ наместо $d-b$). Исто така, заборавање на имагинарната единица $i$ кога дискриминантата е негативна.

```python
from manim import *

class QuarticEquation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Равенка од 4-ти степен", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Equation
        eq = MathTex(r"x^4 + 26x^2 - x + 182 = 0", color=BLACK).shift(UP)
        self.play(Write(eq))
        
        # Factorization Strategy
        strategy = MathTex(
            r"(x^2 + ax + b)(x^2 - ax + d) = 0",
            color=BLUE
        ).next_to(eq, DOWN)
        self.play(Write(strategy))
        
        # System of equations
        system = MathTex(
            r"\begin{cases} d - a^2 + b = 26 \\ a(d - b) = -1 \\ bd = 182 \end{cases}",
            color=BLACK
        ).next_to(strategy, DOWN)
        self.play(Write(system))
        
        # Integer solution logic
        logic = MathTex(
            r"a=1 \implies d-b=-1, \quad bd=182",
            r"\implies d=13, b=14",
            color=RED
        ).next_to(system, DOWN)
        self.play(Write(logic))
        
        # Factored form
        factored = MathTex(
            r"(x^2 + x + 14)(x^2 - x + 13) = 0",
            color=GREEN
        ).next_to(logic, DOWN)
        self.play(Write(factored))
        
        # Roots
        roots = MathTex(
            r"x = \frac{-1 \pm i\sqrt{55}}{2}, \quad x = \frac{1 \pm i\sqrt{51}}{2}",
            color=BLACK
        ).next_to(factored, DOWN)
        self.play(Write(roots))
        
        self.wait(2)

</details>

---
### 🎨 Визуелизација
![Илустрација](/assets/images/sigma139_y4_p1/sigma139_y4_p1.png)