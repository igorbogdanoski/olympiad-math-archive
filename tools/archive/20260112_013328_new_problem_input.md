---
problem_id: sigma139_p1895
title: Диофантова равенка со степен на 2
grade: 11
difficulty: 5
tags:
  - number_theory
  - diophantine_equations
  - modular_arithmetic
  - squares
source: Sigma 139, Zadaca 1895
type: number_theory
---

# Текст на задачата
Да се најдат сите природни броеви $n$ за кои $2^n + 65$ е точен квадрат.

# Решение
## Стратегија
Имаме равенка од облик $2^n + 65 = k^2$.
Ова е експоненцијална Диофантова равенка.
1.  Ќе ја препишеме равенката како $2^n = k^2 - 65$.
2.  Ќе анализираме по модул 3 или 5 за да ја ограничиме парноста на $n$.
3.  Ако $n$ е парен, $n=2m$, тогаш $2^{2m} = (2^m)^2$, па добиваме разлика на квадрати $k^2 - (2^m)^2 = 65$.
4.  Ќе ги најдеме сите факторизации на 65 и ќе ги решиме системите.
5.  Ако $n$ е непарен, ќе провериме дали има решенија (обично со модуларна аритметика).

## Чекор по чекор

**Чекор 1: Поставување на равенката**
Нека $2^n + 65 = k^2$ за некој природен број $k$.
$$ k^2 - 2^n = 65 $$

**Чекор 2: Анализа на парноста на $n$**
Да ја разгледаме равенката по модул 3.
$2 \equiv -1 \pmod 3$.
$65 \equiv 2 \pmod 3$.
$k^2 \equiv 0$ или $1 \pmod 3$.

Равенката станува: $(-1)^n + 2 \equiv k^2 \pmod 3$.
*   Ако $n$ е непарен, $(-1)^n = -1$. Тогаш $-1 + 2 = 1 \equiv k^2 \pmod 3$. Ова е можно.
*   Ако $n$ е парен, $(-1)^n = 1$. Тогаш $1 + 2 = 3 \equiv 0 \equiv k^2 \pmod 3$. Ова е исто така можно (ако $k$ е делив со 3).

Значи модул 3 не ни дава контрадикција за ниту една парност.
Ајде да пробаме да претпоставиме дека $n$ е парен, бидејќи тоа ни овозможува разлика на квадрати.

**Чекор 3: Случај кога $n$ е парен**
Нека $n = 2m$.
$$ 2^{2m} + 65 = k^2 $$
$$ k^2 - (2^m)^2 = 65 $$
$$ (k - 2^m)(k + 2^m) = 65 $$

Бројот 65 може да се запише како производ на два цели броја на следниве начини (бидејќи $k+2^m > k-2^m$ и $k+2^m > 0$):
1.  $1 \cdot 65$
2.  $5 \cdot 13$

Имаме два системи:
*   **Систем 1:**
    $$ \begin{cases} k - 2^m = 1 \\ k + 2^m = 65 \end{cases} $$
    Одзимаме: $(k+2^m) - (k-2^m) = 65 - 1 \implies 2 \cdot 2^m = 64$.
    $$ 2^{m+1} = 64 = 2^6 $$
    $$ m + 1 = 6 \implies m = 5 $$
    Тогаш $n = 2m = 10$.
    Проверка: $2^{10} + 65 = 1024 + 65 = 1089 = 33^2$. Ова е решение.

*   **Систем 2:**
    $$ \begin{cases} k - 2^m = 5 \\ k + 2^m = 13 \end{cases} $$
    Одзимаме: $2 \cdot 2^m = 13 - 5 = 8$.
    $$ 2^{m+1} = 8 = 2^3 $$
    $$ m + 1 = 3 \implies m = 2 $$
    Тогаш $n = 2m = 4$.
    Проверка: $2^4 + 65 = 16 + 65 = 81 = 9^2$. Ова е решение.

**Чекор 4: Случај кога $n$ е непарен**
Нека $n = 2m + 1$.
Равенката е $2^{2m+1} + 65 = k^2$.
$2 \cdot 4^m + 65 = k^2$.
Да разгледаме по модул 5?
$2^n + 65 \equiv 2^n \pmod 5$.
Квадратни остатоци по модул 5 се $0, 1, 4$.
Степените на 2 по модул 5 се:
$2^1 \equiv 2$
$2^2 \equiv 4$
$2^3 \equiv 3$
$2^4 \equiv 1$
Циклусот е $2, 4, 3, 1$.
За $2^n$ да биде квадрат по модул 5 (т.е. 1 или 4), $n$ мора да биде парен (бидејќи за непарни $n$, остатоците се 2 и 3, кои не се квадрати).
Значи, ако $n$ е непарен, $2^n + 65 \equiv 2$ или $3 \pmod 5$, што не може да биде квадрат.

**Заклучок:**
Единствени решенија се $n = 4$ и $n = 10$.

# Pedagogical Notes
1.  **Основна идеја:** Претворањето на равенката во разлика на квадрати $(k-x)(k+x)=C$ е стандардна техника. За да го направиме тоа, ни треба $n$ да биде парен.
2.  **Модуларна аритметика:** Клучниот момент за елиминирање на непарните $n$ е проверката по модул 5. Учениците треба да знаат да ги проверуваат квадратните остатоци за мали модули (3, 4, 5, 8).
3.  **Чести грешки:** Заборавање да се провери случајот за непарно $n$. Многу ученици наоѓаат $n=4$ и $n=10$ и застануваат, без да докажат дека нема други решенија.

# Manim Code
```python
from manim import *

class DiophantineEq(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Диофантова равенка", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Equation
        eq = MathTex(r"2^n + 65 = k^2", color=BLACK).shift(UP)
        self.play(Write(eq))
        
        # Modulo 5 Analysis
        mod_text = Text("Анализа по модул 5:", color=BLUE, font_size=24).next_to(eq, DOWN, buff=0.5).to_edge(LEFT)
        mod_eq = MathTex(r"2^n \equiv k^2 \pmod 5", color=BLUE).next_to(mod_text, DOWN)
        residues = MathTex(
            r"k^2 \pmod 5 \in \{0, 1, 4\}",
            r"2^n \pmod 5 \in \{2, 4, 3, 1\}",
            color=BLACK
        ).arrange(DOWN).next_to(mod_eq, DOWN)
        
        conclusion_odd = MathTex(
            r"\text{За } n \text{ непарен, } 2^n \in \{2, 3\} \implies \text{Нема решение}",
            color=RED
        ).next_to(residues, DOWN)
        
        self.play(Write(mod_text))
        self.play(Write(mod_eq))
        self.play(Write(residues))
        self.play(Write(conclusion_odd))
        
        # Even case
        even_text = Text("За n парен (n=2m):", color=GREEN, font_size=24).next_to(conclusion_odd, DOWN, buff=0.5).to_edge(LEFT)
        diff_sq = MathTex(
            r"(k - 2^m)(k + 2^m) = 65",
            color=BLACK
        ).next_to(even_text, DOWN)
        
        self.play(Write(even_text))
        self.play(Write(diff_sq))
        
        # Solutions
        sols = MathTex(
            r"1) \ 2 \cdot 2^m = 64 \implies m=5 \implies n=10",
            r"2) \ 2 \cdot 2^m = 8 \implies m=2 \implies n=4",
            color=BLACK
        ).arrange(DOWN).next_to(diff_sq, DOWN)
        
        self.play(Write(sols))
        
        self.wait(2)