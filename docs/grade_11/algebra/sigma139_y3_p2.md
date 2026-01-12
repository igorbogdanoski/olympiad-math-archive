---
difficulty: 6
grade: 11
problem_id: sigma139_y3_p2
source: Sigma 139, Treta godina, Zadaca 2
tags:
- trigonometry
- inequalities
- polynomials
- substitution
title: Тригонометриско неравенство
type: algebra
---

# Текст на задачата
Докажи дека за секој реален број $x$ важи:
$$ 5 + 8\cos x + 4\cos 2x + \cos 3x \ge 0 $$

# Решение
## Стратегија
Изразот содржи косинуси од повеќекратни агли ($x, 2x, 3x$). Најдобра стратегија е да ги изразиме сите членови преку $\cos x$ користејќи ги формулите за двоен и троен агол.
Ова ќе го трансформира тригонометриското неравенство во алгебарско неравенство за променливата $t = \cos x$, каде $t \in [-1, 1]$.
Потоа ќе треба да докажеме дека добиениот полином $P(t)$ е ненегативен на интервалот $[-1, 1]$.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Изразување преку $\cos x$</summary>

Ги користиме познатите идентитети:
1.  $\cos 2x = 2\cos^2 x - 1$
2.  $\cos 3x = 4\cos^3 x - 3\cos x$

Нека $t = \cos x$. Тогаш $\cos 2x = 2t^2 - 1$ и $\cos 3x = 4t^3 - 3t$.

</details>

<details>
<summary>Чекор 2: Замена во неравенството</summary>

Го заменуваме секој член во дадениот израз:
$ E = 5 + 8t + 4(2t^2 - 1) + (4t^3 - 3t) $
$ E = 5 + 8t + 8t^2 - 4 + 4t^3 - 3t $

Ги групираме членовите по степени:
$ E = 4t^3 + 8t^2 + 5t + 1 $

</details>

<details>
<summary>Чекор 3: Факторизација на полиномот</summary>

Треба да докажеме дека $P(t) = 4t^3 + 8t^2 + 5t + 1 \ge 0$ за секое $t \in [-1, 1]$.
Да пробаме да најдеме нули на полиномот.
Проверуваме за $t = -1$:
$ P(-1) = 4(-1)^3 + 8(-1)^2 + 5(-1) + 1 = -4 + 8 - 5 + 1 = 0 $

Бидејќи $P(-1) = 0$, значи $(t+1)$ е фактор на полиномот.

Го делиме полиномот со $(t+1)$ (на пример, со Хорнерова шема или полиномно делење):
$ 4t^3 + 8t^2 + 5t + 1 = (t+1)(4t^2 + 4t + 1) $

</details>

<details>
<summary>Чекор 4: Анализа на квадратниот трином</summary>

Вториот множител е $4t^2 + 4t + 1$.
Забележуваме дека ова е полн квадрат:
$ 4t^2 + 4t + 1 = (2t + 1)^2 $

Значи, целиот израз можеме да го запишеме како:
$ E = (t+1)(2t+1)^2 $

</details>

<details>
<summary>Чекор 5: Доказ на неравенството</summary>

Враќаме $t = \cos x$.
$ E = (\cos x + 1)(2\cos x + 1)^2 $

Треба да докажеме дека $E \ge 0$.
1.  Знаеме дека $-1 \le \cos x \le 1$, па $\cos x + 1 \ge 0$ за секој реален број $x$.
2.  Квадратот на кој било реален број е ненегативен, па $(2\cos x + 1)^2 \ge 0$.

Производ на два ненегативни броја е ненегативен број.
$ (\cos x + 1) \cdot (2\cos x + 1)^2 \ge 0 $

Со ова неравенството е докажано.

</details>

**Заклучок:**
Даденото неравенство важи за секој реален број $x$. Еднаквост се достигнува кога $\cos x = -1$ (т.е. $x = \pi + 2k\pi$) или кога $\cos x = -1/2$ (т.е. $x = \pm 2\pi/3 + 2k\pi$).

# Pedagogical Notes
1.  **Основна идеја:** Трансформацијата на тригонометриски полином во алгебарски полином е стандардна техника. Клучно е да се запамети дека новата променлива $t$ е ограничена во $[-1, 1]$.
2.  **Совет од Олимпиец:** Кога факторизирате полином и добиете полн квадрат (како $(2t+1)^2$), тоа е сигурен знак дека сте на прав пат, бидејќи квадратите се секогаш позитивни, што е идеално за докажување неравенства.
3.  **Чести грешки:** Заборавање на формулата за $\cos 3x$. Ако не ја знаете напамет, можете да ја изведете како $\cos(2x+x) = \cos 2x \cos x - \sin 2x \sin x$.

```python
from manim import *

class TrigInequality(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Тригонометриско неравенство", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Original Inequality
        ineq = MathTex(
            r"5 + 8\cos x + 4\cos 2x + \cos 3x \ge 0",
            color=BLACK
        ).shift(UP)
        self.play(Write(ineq))
        
        # Substitution
        sub_text = MathTex(r"\text{Смена: } t = \cos x", color=BLUE).next_to(ineq, DOWN)
        formulas = MathTex(
            r"\cos 2x = 2t^2 - 1, \quad \cos 3x = 4t^3 - 3t",
            color=BLUE, font_size=36
        ).next_to(sub_text, DOWN)
        
        self.play(Write(sub_text))
        self.play(Write(formulas))
        
        # Polynomial
        poly = MathTex(
            r"P(t) &= 5 + 8t + 4(2t^2 - 1) + (4t^3 - 3t) \\ &= 4t^3 + 8t^2 + 5t + 1",
            color=BLACK
        ).next_to(formulas, DOWN)
        
        self.play(Write(poly))
        
        # Factorization
        factored = MathTex(
            r"P(t) = (t+1)(2t+1)^2",
            color=RED
        ).next_to(poly, DOWN)
        
        self.play(Transform(poly.copy(), factored))
        
        # Final Argument
        argument = MathTex(
            r"t \ge -1 \implies t+1 \ge 0",
            r"\quad (2t+1)^2 \ge 0",
            color=GREEN
        ).next_to(factored, DOWN)
        
        self.play(Write(argument))
        
        self.wait(2)