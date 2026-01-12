---
difficulty: 5
grade: 12
problem_id: sigma139_y4_p2
source: Sigma 139, Cetvrta godina, Zadaca 2
tags:
- inequalities
- means
- optimization
- convex_function
title: Неравенство со услов
type: algebra
---

# Текст на задачата
За произволни броеви $a, b > 0$ важи $a + b = 1$. Докажи дека е исполнето неравенството:
$$ \left( a + \frac{1}{a} \right)^2 + \left( b + \frac{1}{b} \right)^2 \ge \frac{25}{2} $$

# Решение
## Стратегија
Ова е класично неравенство кое може да се реши на повеќе начини:
1.  **Квадратна средина (QM-AM):** Да се искористи неравенството $\sqrt{\frac{x^2+y^2}{2}} \ge \frac{x+y}{2}$.
2.  **Функција:** Да се разгледа функцијата $f(x) = (x + 1/x)^2$ и да се искористи нејзината конвексност (Јенсеново неравенство).
3.  **Алгебарски:** Да се развијат квадратите и да се искористи $a+b=1$ за да се сведе на една променлива или на производ $ab$.

Ќе го користиме методот со средини (QM-AM) бидејќи е најелегантен и најбрз.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Примена на неравенството меѓу средините</summary>

Нека $x = a + \frac{1}{a}$ и $y = b + \frac{1}{b}$.
Според неравенството меѓу квадратна и аритметичка средина (QM $\ge$ AM):
$$ \sqrt{\frac{x^2 + y^2}{2}} \ge \frac{x + y}{2} $$
Квадрираме:
$$ \frac{x^2 + y^2}{2} \ge \left( \frac{x + y}{2} \right)^2 $$
$$ x^2 + y^2 \ge \frac{(x + y)^2}{2} $$

Во нашиот случај:
$$ \left( a + \frac{1}{a} \right)^2 + \left( b + \frac{1}{b} \right)^2 \ge \frac{1}{2} \left( a + \frac{1}{a} + b + \frac{1}{b} \right)^2 $$

</details>

<details>
<summary>Чекор 2: Упростување на десната страна</summary>

Го користиме условот $a + b = 1$.
Изразот во заградата е:
$$ S = a + b + \frac{1}{a} + \frac{1}{b} = 1 + \frac{a+b}{ab} = 1 + \frac{1}{ab} $$

Значи, треба да го минимизираме изразот $1 + \frac{1}{ab}$.
Ова е еквивалентно на максимизирање на производот $ab$.

</details>

<details>
<summary>Чекор 3: Ограничување на производот $ab$</summary>

Знаеме дека за позитивни броеви важи $AM \ge GM$:
$$ \frac{a+b}{2} \ge \sqrt{ab} $$
Бидејќи $a+b=1$:
$$ \frac{1}{2} \ge \sqrt{ab} $$
Квадрираме:
$$ \frac{1}{4} \ge ab $$
Значи, максималната вредност на $ab$ е $1/4$.

</details>

<details>
<summary>Чекор 4: Финална проценка</summary>

Бидејќи $ab \le \frac{1}{4}$, тогаш $\frac{1}{ab} \ge 4$.
Следи:
$$ S = 1 + \frac{1}{ab} \ge 1 + 4 = 5 $$

Сега се враќаме на неравенството од Чекор 1:
$$ \text{Лева страна} \ge \frac{1}{2} S^2 \ge \frac{1}{2} (5)^2 = \frac{25}{2} $$

Со ова неравенството е докажано.

**Заклучок:**
Неравенството важи, а знак за равенство се достигнува кога $a=b=1/2$.

# Pedagogical Notes
1.  **Основна идеја:** Комбинацијата на QM-AM и AM-GM е моќна алатка. Прво го „линеаризираме“ проблемот (од квадрати на збир), а потоа го користиме условот за збирот за да го ограничиме производот.
2.  **Совет од Олимпиец:** Кога имате симетричен израз со $a$ и $b$ и услов $a+b=\text{const}$, екстремната вредност скоро секогаш се постигнува кога $a=b$. Во овој случај $a=b=1/2$. Проверката на овој случај на почетокот ($ (1/2+2)^2 + (1/2+2)^2 = 2(2.5)^2 = 2(6.25) = 12.5 = 25/2 $) ви дава сигурност кон што целите.
3.  **Алтернатива (Јенсен):** Функцијата $f(x) = (x+1/x)^2$ е конвексна за $x \in (0, 1)$.
    $f'(x) = 2(x+1/x)(1-1/x^2)$.
    $f''(x) = \dots > 0$.
    Според Јенсен: $f(a) + f(b) \ge 2 f(\frac{a+b}{2}) = 2 f(1/2) = 2(1/2+2)^2 = 2(2.5)^2 = 12.5$.

```python
from manim import *

class InequalityProof(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Доказ на неравенство", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Inequality
        ineq = MathTex(
            r"\left( a + \frac{1}{a} \right)^2 + \left( b + \frac{1}{b} \right)^2 \ge \frac{25}{2}",
            color=BLACK
        ).shift(UP)
        self.play(Write(ineq))
        
        # QM-AM Step
        qmam = MathTex(
            r"x^2 + y^2 \ge \frac{(x+y)^2}{2}",
            color=BLUE
        ).next_to(ineq, DOWN)
        self.play(Write(qmam))
        
        # Substitution
        sub = MathTex(
            r"\ge \frac{1}{2} \left( a + b + \frac{1}{a} + \frac{1}{b} \right)^2",
            color=BLACK
        ).next_to(qmam, DOWN)
        self.play(Write(sub))
        
        # Using condition a+b=1
        cond = MathTex(
            r"= \frac{1}{2} \left( 1 + \frac{a+b}{ab} \right)^2 = \frac{1}{2} \left( 1 + \frac{1}{ab} \right)^2",
            color=BLACK
        ).next_to(sub, DOWN)
        self.play(Write(cond))
        
        # AM-GM Step
        amgm = MathTex(
            r"ab \le \left(\frac{a+b}{2}\right)^2 = \frac{1}{4} \implies \frac{1}{ab} \ge 4",
            color=RED
        ).next_to(cond, DOWN)
        self.play(Write(amgm))
        
        # Final Result
        final = MathTex(
            r"\ge \frac{1}{2} (1 + 4)^2 = \frac{25}{2}",
            color=GREEN
        ).next_to(amgm, DOWN)
        self.play(Indicate(final))
        
        self.wait(2)

</details>

---
### 🎨 Визуелизација
![Илустрација](/assets/images/sigma139_y4_p2/sigma139_y4_p2.png)