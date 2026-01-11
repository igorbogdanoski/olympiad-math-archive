---
problem_id: sigma139_y2_p3
title: Неравенство со комплексни броеви
grade: 10
difficulty: 7
tags:
  - complex_numbers
  - inequalities
  - triangle_inequality
  - polynomials
source: Sigma 139, Vtora godina, Zadaca 3
type: algebra
---

## Текст на задачата

Нека $z \in \mathbb{C} \setminus \{0\}$ е комплексен број таков што $\left| z^3 + \frac{1}{z^3} \right| \le 2$. Докажи дека $\left| z + \frac{1}{z} \right| \le 2$.

## Решение

### Стратегија

Ова е класична задача со комплексни броеви која бара поврзување на изразот $z^3 + \frac{1}{z^3}$ со $z + \frac{1}{z}$.

- Ќе воведеме смена $w = z + \frac{1}{z}$.
- Ќе го изразиме $z^3 + \frac{1}{z^3}$ преку $w$.
- Ќе го искористиме даденото неравенство за да добиеме неравенство за $w$.
- Ќе го решиме тоа неравенство за $|w|$ користејќи го неравенството на триаголник.

### Чекор по чекор

**Чекор 1: Воведување смена**
Нека $w = z + \frac{1}{z}$.
Да го пресметаме $w^3$:
$$ w^3 = \left( z + \frac{1}{z} \right)^3 = z^3 + 3z^2 \cdot \frac{1}{z} + 3z \cdot \frac{1}{z^2} + \frac{1}{z^3} $$
$$ w^3 = z^3 + 3z + \frac{3}{z} + \frac{1}{z^3} $$
$$ w^3 = \left( z^3 + \frac{1}{z^3} \right) + 3\left( z + \frac{1}{z} \right) $$
$$ w^3 = \left( z^3 + \frac{1}{z^3} \right) + 3w $$

Од тука можеме да го изразиме членот што ни е даден во условот:
$$ z^3 + \frac{1}{z^3} = w^3 - 3w $$

**Чекор 2: Поставување на неравенството**
Дадено е дека $\left| z^3 + \frac{1}{z^3} \right| \le 2$.
Заменуваме со изразот преку $w$:
$$ |w^3 - 3w| \le 2 $$
$$ |w| \cdot |w^2 - 3| \le 2 $$

**Чекор 3: Доказ со контрадикција**
Треба да докажеме дека $|w| \le 2$.
Да претпоставиме спротивно, т.е. дека $|w| > 2$.
Тогаш $|w| = 2 + \epsilon$ за некое $\epsilon > 0$.

Да го разгледаме изразот $|w^3 - 3w|$.
Според неравенството на триаголник во облик $|a - b| \ge |a| - |b|$ (или $|a - b| \ge ||a| - |b||$), имаме:
$$ |w^3 - 3w| \ge |w^3| - |3w| = |w|^3 - 3|w| $$
$$ |w^3 - 3w| \ge |w|(|w|^2 - 3) $$

Ако $|w| > 2$, тогаш $|w|^2 > 4$, па $|w|^2 - 3 > 1$.
Тогаш:
$$ |w|(|w|^2 - 3) > 2 \cdot (4 - 3) = 2 $$
Чекај, ова не е доволно прецизно.
Ако $|w| > 2$, тогаш функцијата $f(x) = x(x^2 - 3) = x^3 - 3x$ е растечка за $x > 1$ (бидејќи $f'(x) = 3x^2 - 3 > 0$).
Значи, ако $|w| > 2$, тогаш:
$$ |w|^3 - 3|w| > 2^3 - 3(2) = 8 - 6 = 2 $$
Значи, добивме:
$$ |w^3 - 3w| \ge |w|^3 - 3|w| > 2 $$
Ова е во контрадикција со условот $|w^3 - 3w| \le 2$.

**Заклучок:**
Претпоставката дека $|w| > 2$ не доведе до контрадикција.
Затоа мора да важи $|w| \le 2$.
Односно:
$$ \left| z + \frac{1}{z} \right| \le 2 $$

## Pedagogical Notes

- **Основна идеја:** Трансформацијата на Жуковски ($w = z + 1/z$) е стандардна алатка во комплексна анализа и олимписка алгебра. Таа ги поврзува степените суми $z^n + 1/z^n$ со полиноми од $w$ (Чебишеви полиноми).
- **Совет од Олимпиец:** Кога треба да докажете неравенство од типот $|A| \le k$, често е корисно да претпоставите спротивно ($|A| > k$) и да користите неравенство на триаголник за да добиете контрадикција. Функцијата $x^3 - 3x$ е монотоно растечка за $x \ge 2$, што е клучен аргумент овде.
- **Чести грешки:** Внимавајте со неравенството на триаголник. $|a-b| \ge |a| - |b|$ важи секогаш, но корисно е само кога $|a| > |b|$. Во нашиот случај, ако $|w| > 2$, тогаш $|w^3| = |w|^3 > 8$ и $|3w| = 3|w| > 6$, па $|w^3| > |3w|$ е исполнето.

## Manim Code

```python
from manim import *

class ComplexInequality(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Комплексни броеви и неравенства", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Substitution
        sub = MathTex(r"w = z + \frac{1}{z}", color=BLUE).shift(UP)
        self.play(Write(sub))
        
        # Expansion
        exp = MathTex(
            r"w^3 = z^3 + \frac{1}{z^3} + 3\left(z + \frac{1}{z}\right)",
            color=BLACK
        ).next_to(sub, DOWN)
        self.play(Write(exp))
        
        # Relation
        rel = MathTex(
            r"z^3 + \frac{1}{z^3} = w^3 - 3w",
            color=RED
        ).next_to(exp, DOWN)
        self.play(TransformFromCopy(exp, rel))
        
        # Inequality
        ineq = MathTex(r"|w^3 - 3w| \le 2", color=BLACK).next_to(rel, DOWN, buff=0.5)
        self.play(Write(ineq))
        
        # Contradiction logic
        contra = MathTex(
            r"\text{Ако } |w| > 2 \implies |w^3 - 3w| \ge |w|^3 - 3|w| > 2",
            color=BLACK, font_size=36
        ).next_to(ineq, DOWN)
        
        self.play(Write(contra))
        
        # Conclusion
        final = MathTex(r"\therefore |w| \le 2", color=GREEN).next_to(contra, DOWN)
        self.play(Indicate(final))
        
        self.wait(2)
```
