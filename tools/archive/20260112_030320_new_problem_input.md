---
problem_id: sigma139_p1905
title: Збир на квадрати во Q(sqrt(5))
grade: 12
difficulty: 7
tags:
  - number_theory
  - field_theory
  - quadratic_residues
  - proof
source: Sigma 139, Zadaca 1905
type: number_theory
---

# Текст на задачата
Нека $\mathbb{Q}(\sqrt{5}) = \{a + b\sqrt{5} \mid a, b \in \mathbb{Q}\}$. Докажи дека бројот $1 + \sqrt{5}$ не може да се запише во облик $x_1^2 + x_2^2 + \dots + x_n^2$, каде што $x_1, x_2, \dots, x_n \in \mathbb{Q}(\sqrt{5})$.

# Решение
## Стратегија
Ова е проблем за претставување на броеви како збир на квадрати во квадратно поле.
1.  Ќе претпоставиме спротивно: дека $1 + \sqrt{5}$ може да се запише како збир на квадрати на елементи од $\mathbb{Q}(\sqrt{5})$.
2.  Ќе ја искористиме нормата на полето $N(z) = a^2 - 5b^2$ за $z = a + b\sqrt{5}$.
3.  Ќе го искористиме својството на „конјугирање“: ако $z = \sum x_i^2$, тогаш и за конјугираните елементи важи $\bar{z} = \sum \bar{x}_i^2$.
4.  Бидејќи $\bar{x}_i^2 = (\bar{x}_i)^2 \ge 0$ во $\mathbb{R}$? Не, $\bar{x}_i$ е реален број, па неговиот квадрат е позитивен.
5.  Ќе видиме дека конјугираниот елемент на $1+\sqrt{5}$ е $1-\sqrt{5}$, кој е негативен број.
6.  Но, збир на квадрати на реални броеви мора да биде ненегативен. Ова ќе доведе до контрадикција.

## Чекор по чекор

**Чекор 1: Дефиниции и својства**
Елементите на $\mathbb{Q}(\sqrt{5})$ се реални броеви од облик $a + b\sqrt{5}$.
За секој елемент $z = a + b\sqrt{5}$, дефинираме негов **конјугиран елемент** $\bar{z} = a - b\sqrt{5}$.
Преслiкувањето $z \mapsto \bar{z}$ е автоморфизам на полето $\mathbb{Q}(\sqrt{5})$. Тоа значи:
*   $\overline{z_1 + z_2} = \bar{z}_1 + \bar{z}_2$
*   $\overline{z_1 \cdot z_2} = \bar{z}_1 \cdot \bar{z}_2$
*   $\overline{z^2} = (\bar{z})^2$

**Чекор 2: Претпоставка на спротивното**
Да претпоставиме дека постојат $x_1, x_2, \dots, x_n \in \mathbb{Q}(\sqrt{5})$ такви што:
$$ 1 + \sqrt{5} = x_1^2 + x_2^2 + \dots + x_n^2 $$

**Чекор 3: Примена на конјугирање**
Да го примениме конјугирањето на двете страни на равенството:
$$ \overline{1 + \sqrt{5}} = \overline{x_1^2 + x_2^2 + \dots + x_n^2} $$
Левата страна е:
$$ \overline{1 + 1\cdot\sqrt{5}} = 1 - 1\cdot\sqrt{5} = 1 - \sqrt{5} $$
Десната страна е:
$$ \overline{x_1^2} + \overline{x_2^2} + \dots + \overline{x_n^2} = (\bar{x}_1)^2 + (\bar{x}_2)^2 + \dots + (\bar{x}_n)^2 $$

Значи, добиваме:
$$ 1 - \sqrt{5} = (\bar{x}_1)^2 + (\bar{x}_2)^2 + \dots + (\bar{x}_n)^2 $$

**Чекор 4: Анализа на знакот**
Елементите $x_i$ се од облик $a_i + b_i\sqrt{5}$, каде $a_i, b_i \in \mathbb{Q}$.
Бидејќи $\sqrt{5}$ е реален број, сите елементи од $\mathbb{Q}(\sqrt{5})$ се **реални броеви**.
Следи дека и нивните конјугирани елементи $\bar{x}_i = a_i - b_i\sqrt{5}$ се исто така реални броеви.

Квадратот на кој било реален број е ненегативен:
$$ (\bar{x}_i)^2 \ge 0 \quad \text{за секое } i $$
Затоа, нивниот збир мора да биде ненегативен:
$$ \sum_{i=1}^n (\bar{x}_i)^2 \ge 0 $$

Од друга страна, левата страна на равенството од Чекор 3 е:
$$ 1 - \sqrt{5} $$
Бидејќи $\sqrt{4} < \sqrt{5} < \sqrt{9}$, имаме $2 < \sqrt{5} < 3$.
Значи:
$$ 1 - \sqrt{5} < 1 - 2 = -1 < 0 $$

**Чекор 5: Контрадикција**
Добивме дека негативен број ($1-\sqrt{5}$) е еднаков на збир на квадрати на реални броеви (што е $\ge 0$).
$$ 1 - \sqrt{5} < 0 \le \sum (\bar{x}_i)^2 $$
Ова е контрадикција.

**Заклучок:**
Претпоставката е погрешна. Бројот $1 + \sqrt{5}$ не може да се запише како збир на квадрати во $\mathbb{Q}(\sqrt{5})$.

# Pedagogical Notes
1.  **Основна идеја:** Клучот е во тоа што $\mathbb{Q}(\sqrt{5})$ е подполе на $\mathbb{R}$. Во реалните броеви, збир на квадрати е секогаш позитивен. „Трикот“ е да се префрлиме на конјугираниот елемент, кој мора да го задоволува истото алгебарско својство (да биде збир на квадрати), но нумерички е негативен.
2.  **Совет од Олимпиец:** Кога работите со полиња од облик $\mathbb{Q}(\sqrt{d})$, секогаш размислувајте за конјугирањето $a+b\sqrt{d} \to a-b\sqrt{d}$. Тоа е најмоќната алатка за докажување на алгебарски својства.
3.  **Генерализација:** Ова важи за секој елемент $\alpha \in \mathbb{Q}(\sqrt{d})$ (каде $d>0$) чиј конјугат $\bar{\alpha}$ е негативен. Таквите елементи се нарекуваат „тотално позитивни“ ако и $\alpha > 0$ и $\bar{\alpha} > 0$. Само тотално позитивните елементи можат да бидат збир на квадрати.

# Manim Code
```python
from manim import *

class SumOfSquaresProof(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Збир на квадрати во Q(√5)", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Assumption
        assumption = MathTex(
            r"1 + \sqrt{5} = \sum_{i=1}^n x_i^2, \quad x_i \in \mathbb{Q}(\sqrt{5})",
            color=BLACK
        ).shift(UP)
        self.play(Write(assumption))
        
        # Conjugation
        conjugate_text = Text("Применуваме конјугирање:", color=BLUE, font_size=24).next_to(assumption, DOWN, buff=0.5).to_edge(LEFT)
        conjugate_eq = MathTex(
            r"\overline{1 + \sqrt{5}} = \overline{\sum x_i^2} = \sum (\bar{x}_i)^2",
            color=BLUE
        ).next_to(conjugate_text, DOWN)
        
        self.play(Write(conjugate_text))
        self.play(Write(conjugate_eq))
        
        # Calculation
        calc = MathTex(
            r"1 - \sqrt{5} = \sum (\bar{x}_i)^2",
            color=RED
        ).next_to(conjugate_eq, DOWN)
        self.play(Write(calc))
        
        # Contradiction
        contra_text = Text("Анализа на знакот:", color=BLACK, font_size=24).next_to(calc, DOWN, buff=0.5).to_edge(LEFT)
        
        lhs = MathTex(r"LHS: 1 - \sqrt{5} < 0", color=RED).next_to(contra_text, DOWN)
        rhs = MathTex(r"RHS: \sum (\bar{x}_i)^2 \ge 0", color=GREEN).next_to(lhs, DOWN)
        
        self.play(Write(contra_text))
        self.play(Write(lhs))
        self.play(Write(rhs))
        
        # Conclusion
        final = Text("Контрадикција!", color=RED).next_to(rhs, DOWN, buff=0.5)
        self.play(Write(final))
        
        self.wait(2)