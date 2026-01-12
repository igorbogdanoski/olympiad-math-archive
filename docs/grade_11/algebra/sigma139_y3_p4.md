---
difficulty: 7
grade: 11
problem_id: sigma139_y3_p4
related_theorems:
- vectors
- optimization
- cauchy_schwarz_inequality
source: Sigma 139, Treta godina, Zadaca 4
tags:
- trigonometry
- cauchy_schwarz
- inequalities
- optimization
title: Равенка со две променливи и Коши-Шварц
type: algebra
---

# Текст на задачата
Реши ја равенката:
$$ (3\sin x + \sqrt{3}\cos x + 5y)^2 = 37(1 + y^2) $$

# Решение
## Стратегија
Ова е равенка со две променливи ($x$ и $y$). Обично ваквите равенки имаат бесконечно многу решенија, освен ако не се работи за некој граничен случај (екстрем).
Забележуваме дека десната страна е производ на збир на квадрати. Левата страна е квадрат на збир. Ова силно сугерира на **неравенството на Коши-Шварц** (Cauchy-Schwarz).
Неравенството гласи: $(a_1 b_1 + a_2 b_2 + \dots)^2 \le (a_1^2 + a_2^2 + \dots)(b_1^2 + b_2^2 + \dots)$.
Ќе се обидеме да ја запишеме левата страна како скаларен производ на два вектора, така што десната страна да биде производ на нивните норми. Ако успееме, тогаш равенството важи само кога векторите се колинеарни.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Трансформација на левата страна</summary>

Изразот во заградата е $3\sin x + \sqrt{3}\cos x + 5y$.
Можеме да го гледаме како скаларен производ на векторите:
$\vec{u} = (3\sin x + \sqrt{3}\cos x, 5)$ и $\vec{v} = (1, y)$.
Тогаш левата страна е $(\vec{u} \cdot \vec{v})^2$.
Десната страна би требало да биде $|\vec{u}|^2 |\vec{v}|^2$.
$|\vec{v}|^2 = 1^2 + y^2 = 1+y^2$. Ова одговара на едниот множител.
Дали $|\vec{u}|^2$ е еднакво на 37?
$|\vec{u}|^2 = (3\sin x + \sqrt{3}\cos x)^2 + 5^2$.
Ова зависи од $x$, па не е константа. Оваа поделба не е добра.

Ајде да пробаме поинаку.
Нека $A = 3\sin x + \sqrt{3}\cos x$.
Равенката е $(A + 5y)^2 = 37(1 + y^2)$.
Ова личи на Коши-Шварц за векторите $\vec{a} = (A, 5)$ и $\vec{b} = (1, y)$?
$(\vec{a} \cdot \vec{b})^2 = (A + 5y)^2$.
$|\vec{a}|^2 |\vec{b}|^2 = (A^2 + 25)(1 + y^2)$.
За да важи равенството од задачата, треба $A^2 + 25 = 37$, т.е. $A^2 = 12$.
Дали $A$ може да биде $\sqrt{12}$?
$A = 3\sin x + \sqrt{3}\cos x$.
Максималната вредност на $a\sin x + b\cos x$ е $\sqrt{a^2+b^2}$.
$\max(A) = \sqrt{3^2 + (\sqrt{3})^2} = \sqrt{9+3} = \sqrt{12}$.
Значи $A^2 \le 12$.
Тогаш $A^2 + 25 \le 12 + 25 = 37$.

</details>

<details>
<summary>Чекор 2: Примена на Коши-Шварц</summary>

Да ги дефинираме векторите:
$\vec{u} = (A, 5)$
$\vec{v} = (1, y)$
Според Коши-Шварц:
$$ (A \cdot 1 + 5 \cdot y)^2 \le (A^2 + 5^2)(1^2 + y^2) $$
$$ (A + 5y)^2 \le (A^2 + 25)(1 + y^2) $$

Знаеме дека $A = 3\sin x + \sqrt{3}\cos x$.
Максималната вредност на $A^2$ е 12.
Значи $A^2 + 25 \le 12 + 25 = 37$.
Затоа:
$$ (A + 5y)^2 \le 37(1 + y^2) $$

Равенката во задачата бара да важи **равенство**:
$$ (A + 5y)^2 = 37(1 + y^2) $$

Ова е можно само ако се исполнети два услови истовремено:
1.  Мора да важи равенство во неравенството $A^2 \le 12$. Ова значи $A^2 = 12$, т.е. $A = \pm \sqrt{12} = \pm 2\sqrt{3}$.
2.  Мора да важи равенство во Коши-Шварц. Ова значи дека векторите $\vec{u}$ и $\vec{v}$ се колинеарни (пропорционални).
    $$ \frac{A}{1} = \frac{5}{y} \implies y = \frac{5}{A} $$

</details>

<details>
<summary>Чекор 3: Решавање на системот</summary>

Имаме два случаи за $A$:

**Случај 1:** $A = 2\sqrt{3}$.
Тогаш $y = \frac{5}{2\sqrt{3}}$.
Треба да го најдеме $x$ од равенката:
$$ 3\sin x + \sqrt{3}\cos x = 2\sqrt{3} $$
Делиме со $\sqrt{12} = 2\sqrt{3}$:
$$ \frac{3}{2\sqrt{3}}\sin x + \frac{\sqrt{3}}{2\sqrt{3}}\cos x = 1 $$
$$ \frac{\sqrt{3}}{2}\sin x + \frac{1}{2}\cos x = 1 $$
Ова е синус од збир: $\sin x \cos 30^\circ + \cos x \sin 30^\circ = 1$.
$$ \sin(x + 30^\circ) = 1 $$
$$ x + \frac{\pi}{6} = \frac{\pi}{2} + 2k\pi $$
$$ x = \frac{\pi}{3} + 2k\pi $$

**Случај 2:** $A = -2\sqrt{3}$.
Тогаш $y = \frac{5}{-2\sqrt{3}} = -\frac{5}{2\sqrt{3}}$.
Равенката за $x$ е:
$$ 3\sin x + \sqrt{3}\cos x = -2\sqrt{3} $$
Делиме со $2\sqrt{3}$:
$$ \sin(x + 30^\circ) = -1 $$
$$ x + \frac{\pi}{6} = \frac{3\pi}{2} + 2k\pi $$
$$ x = \frac{4\pi}{3} + 2k\pi $$

**Заклучок:**
Решенијата се паровите $(x, y)$:
1.  $x = \frac{\pi}{3} + 2k\pi, \quad y = \frac{5\sqrt{3}}{6}$
2.  $x = \frac{4\pi}{3} + 2k\pi, \quad y = -\frac{5\sqrt{3}}{6}$
(каде $k \in \mathbb{Z}$).

# Pedagogical Notes
1.  **Основна идеја:** Методот на помошен агол ($a\sin x + b\cos x = \sqrt{a^2+b^2}\sin(x+\phi)$) е клучен за да се види дека максималната вредност на изразот е $\sqrt{12}$.
2.  **Совет од Олимпиец:** Кога имате равенка од типот $L(x,y) = R(x,y)$, а знаете дека $L \le M$ и $R \ge M$ (или слично ограничување), тогаш единствено решение е кога двете страни се еднакви на $M$. Овде $M$ беше скриено во Коши-Шварц.
3.  **Чести грешки:** Заборавање на условот за колинеарност кај Коши-Шварц. Не е доволно само $A$ да биде максимум, мора и $y$ да биде соодветно поврзано со $A$.

```python
from manim import *

class CauchyEquation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Равенка и Коши-Шварц", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Equation
        eq = MathTex(
            r"(3\sin x + \sqrt{3}\cos x + 5y)^2 = 37(1 + y^2)",
            color=BLACK
        ).shift(UP)
        self.play(Write(eq))
        
        # Substitution A
        sub_A = MathTex(r"A = 3\sin x + \sqrt{3}\cos x", color=BLUE).next_to(eq, DOWN)
        self.play(Write(sub_A))
        
        # Cauchy-Schwarz Setup
        vectors = MathTex(
            r"\vec{u} = (A, 5), \quad \vec{v} = (1, y)",
            color=BLACK
        ).next_to(sub_A, DOWN)
        
        cs_ineq = MathTex(
            r"(A \cdot 1 + 5 \cdot y)^2 \le (A^2 + 25)(1 + y^2)",
            color=RED
        ).next_to(vectors, DOWN)
        
        self.play(Write(vectors))
        self.play(Write(cs_ineq))
        
        # Max Value Logic
        max_val = MathTex(
            r"A^2 \le 3^2 + (\sqrt{3})^2 = 12 \implies A^2 + 25 \le 37",
            color=GREEN
        ).next_to(cs_ineq, DOWN)
        
        self.play(Write(max_val))
        
        # Conclusion
        conclusion = MathTex(
            r"\text{Равенство } \iff A^2=12 \text{ и } \vec{u} \parallel \vec{v}",
            color=BLACK
        ).next_to(max_val, DOWN)
        
        self.play(Write(conclusion))
        
        self.wait(2)

</details>

---
### 🎨 Визуелизација
![Илустрација](/assets/images/sigma139_y3_p4/sigma139_y3_p4.png)