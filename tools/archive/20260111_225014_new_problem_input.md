---
problem_id: sigma139_y2_p1
title: Ирационална равенка со смена на променлива
grade: 10
difficulty: 5
tags:
  - algebra
  - irrational_equations
  - substitution
source: Sigma 139, Vtora godina, Zadaca 1
type: algebra
---

# Текст на задачата
Реши ја равенката:
$$ \sqrt{5 + \sqrt[3]{x}} + \sqrt{5 - \sqrt[3]{x}} = \sqrt[3]{x} $$

# Решение
## Стратегија
Равенката содржи ирационални изрази (квадратни и трети корени). Забележуваме дека изразот $\sqrt[3]{x}$ се повторува три пати. Ова е силен сигнал за воведување на **смена**.
1.  Ќе воведеме нова променлива $t = \sqrt[3]{x}$.
2.  Ќе ја анализираме дефиниционата област за $t$ (за кои вредности равенката има смисла).
3.  Ќе ја квадрираме равенката за да се ослободиме од надворешните корени.
4.  Ќе ги провериме добиените решенија во почетната равенка (задолжителен чекор кај ирационални равенки).

## Чекор по чекор

**Чекор 1: Воведување смена и дефинициона област**
Нека $t = \sqrt[3]{x}$. Равенката добива облик:
$$ \sqrt{5 + t} + \sqrt{5 - t} = t $$

За да биде дефинирана оваа равенка во множеството реални броеви, мора да важат следниве услови:
1.  Поткореновите величини да се ненегативни:
    *   $5 + t \ge 0 \implies t \ge -5$
    *   $5 - t \ge 0 \implies t \le 5$
    Значи, $t \in [-5, 5]$.
2.  Левата страна е збир на два квадратни корени (кои се секогаш ненегативни), што значи дека и десната страна мора да биде ненегативна:
    *   $t \ge 0$

**Заклучок за доменот:** Бараме решение за $t$ во интервалот $[0, 5]$.

**Чекор 2: Квадрирање на равенката**
Ја квадрираме равенката $\sqrt{5 + t} + \sqrt{5 - t} = t$:
$$ (\sqrt{5 + t} + \sqrt{5 - t})^2 = t^2 $$
Користиме формула за квадрат на бином $(A+B)^2 = A^2 + 2AB + B^2$:
$$ (5 + t) + 2\sqrt{(5 + t)(5 - t)} + (5 - t) = t^2 $$

Ги средуваме членовите ($t$ и $-t$ се поништуваат):
$$ 10 + 2\sqrt{25 - t^2} = t^2 $$

**Чекор 3: Изолирање на коренот**
Го оставаме коренот на една страна:
$$ 2\sqrt{25 - t^2} = t^2 - 10 $$

Тука можеме да направиме уште една проверка на условите. За да има решение, десната страна мора да биде ненегативна:
$t^2 - 10 \ge 0 \implies t^2 \ge 10 \implies t \ge \sqrt{10}$ (бидејќи $t>0$).
Бидејќи $\sqrt{10} \approx 3.16$, нашето решение мора да биде во интервалот $[\sqrt{10}, 5]$.

**Чекор 4: Второ квадрирање**
Ја квадрираме равенката повторно:
$$ (2\sqrt{25 - t^2})^2 = (t^2 - 10)^2 $$
$$ 4(25 - t^2) = t^4 - 20t^2 + 100 $$
$$ 100 - 4t^2 = t^4 - 20t^2 + 100 $$

Ги префрламе сите членови на десната страна:
$$ t^4 - 20t^2 + 4t^2 + 100 - 100 = 0 $$
$$ t^4 - 16t^2 = 0 $$

**Чекор 5: Решавање на биквадратната равенка**
Факторизираме:
$$ t^2(t^2 - 16) = 0 $$
Можните решенија за $t$ се:
1.  $t^2 = 0 \implies t_1 = 0$
2.  $t^2 - 16 = 0 \implies t^2 = 16 \implies t_{2,3} = \pm 4$

**Чекор 6: Селекција на валидни решенија**
Имаме кандидати $t \in \{0, 4, -4\}$.
Ги проверуваме според условите од Чекор 1 и Чекор 3:
*   $t = -4$: Отпаѓа бидејќи $t \ge 0$.
*   $t = 0$: Отпаѓа бидејќи $t \ge \sqrt{10}$ (или со директна проверка: $\sqrt{5}+\sqrt{5} \neq 0$).
*   $t = 4$: Ова е валидно решение бидејќи $4 \in [\sqrt{10}, 5]$.
    *   Проверка: $\sqrt{5+4} + \sqrt{5-4} = \sqrt{9} + \sqrt{1} = 3 + 1 = 4$. Точно.

**Чекор 7: Враќање на смената**
Најдовме $t = 4$.
$$ \sqrt[3]{x} = 4 $$
Го кубираме изразот:
$$ x = 4^3 $$
$$ x = 64 $$

**Заклучок:**
Единственото решение на равенката е $x = 64$.

# Pedagogical Notes
1.  **Основна идеја:** Смената на променлива е моќна алатка за упростување на визуелниот изглед на равенката. Наместо да пишуваме $\sqrt[3]{x}$ постојано, $t$ ни овозможува да се фокусираме на алгебарската структура.
2.  **Совет од Олимпиец:** Кај ирационалните равенки, **проверката е дел од решението**, а не само препорака. Квадрирањето е нееквивалентна трансформација (може да воведе лажни решенија, т.н. "туѓи корени"). На пример, $x=2 \implies x^2=4$, но $x^2=4 \implies x=\pm 2$. Затоа секогаш проверувајте ги крајните кандидати во почетната равенка.
3.  **Чести грешки:** Учениците често забораваат дека $\sqrt{A} + \sqrt{B} = C$ имплицира $C \ge 0$. Во овој случај, тоа веднаш го елиминира решението $t=0$ и $t=-4$ без многу пресметки.

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Ирационална равенка", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Original Equation
        eq_original = MathTex(r"\sqrt{5 + \sqrt[3]{x}} + \sqrt{5 - \sqrt[3]{x}} = \sqrt[3]{x}", color=BLACK).shift(UP)
        self.play(Write(eq_original))
        
        # Substitution
        sub_text = MathTex(r"\text{Смена: } t = \sqrt[3]{x}", color=BLUE).next_to(eq_original, DOWN)
        self.play(Write(sub_text))
        
        # New Equation
        eq_t = MathTex(r"\sqrt{5 + t} + \sqrt{5 - t} = t", color=BLACK).next_to(sub_text, DOWN)
        self.play(TransformFromCopy(eq_original, eq_t))
        
        # Domain constraint
        domain = MathTex(r"t \in [0, 5]", color=RED).next_to(eq_t, RIGHT, buff=1)
        self.play(Write(domain))
        
        # Squaring animation
        square_brace = Brace(eq_t, DOWN)
        square_text = square_brace.get_text("Квадрираме").set_color(BLACK)
        self.play(GrowFromCenter(square_brace), Write(square_text))
        
        eq_squared = MathTex(r"10 + 2\sqrt{25 - t^2} = t^2", color=BLACK).next_to(square_brace, DOWN)
        self.play(Write(eq_squared))
        
        # Isolate root
        eq_iso = MathTex(r"2\sqrt{25 - t^2} = t^2 - 10", color=BLACK).next_to(eq_squared, DOWN)
        self.play(Transform(eq_squared.copy(), eq_iso))
        
        # Final polynomial
        eq_poly = MathTex(r"t^4 - 16t^2 = 0", color=BLACK).next_to(eq_iso, DOWN)
        self.play(Write(eq_poly))
        
        # Solutions
        sols = MathTex(r"t \in \{0, 4, -4\}", color=BLUE).next_to(eq_poly, DOWN)
        self.play(Write(sols))
        
        # Filtering
        valid_sol = MathTex(r"t = 4 \implies x = 64", color=GREEN).next_to(sols, DOWN)
        self.play(Indicate(valid_sol))
        
        self.wait(2)
```