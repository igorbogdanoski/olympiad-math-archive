---
problem_id: regional_2025_2_3ab
title: Плоштина на триаголници и Чевината теорема
grade: 10
difficulty: 6
type: geometry
tags:
  - plostina
  - slicni_triagolnici
  - cevini_pravi
primary_skill: plostinski_metod
related_skills:
  - slicnost_na_triagolnici
  - algebarski_transformacii
source: Сигма 139 (Регионален натпревар 2025, задача 3АБ)
---

# Плоштина на триаголници и Чевината теорема

# Текст на задачата
Нека $S$ е внатрешна точка во триаголникот $ABC$ и нека правите $AS, BS$ и $CS$ ги сечат страните $BC, CA$ и $AB$ во точките $D, E$ и $F$, соодветно. Нека $AS = a, BS = b, CS = c$ и $SD = SE = SF = d$. Ако $a + b + c = 43$ и $d = 3$, тогаш одреди ја вредноста на изразот $abc$.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Како можеме да го изразиме односот на плоштините на триаголниците $BCS$ и $ABC$ преку должините на отсечките на чевината права $AD$?

$$\frac{P_{BCS}}{P_{ABC}} = \frac{SD}{AD}$$

2. Забележете дека $AD = AS + SD = a + d$. Направете го истото за другите две чевини прави.

3. Колкав е збирот на односите на плоштините на трите внатрешни триаголници $BCS, CAS$ и $ABS$ во однос на вкупната плоштина $ABC$?

$$\frac{P_{BCS}}{P_{ABC}} + \frac{P_{CAS}}{P_{ABC}} + \frac{P_{ABS}}{P_{ABC}} = 1$$

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Оваа задача е класичен пример за моќта на **плоштинскиот метод** во геометријата. Наместо да се обидуваме директно да ги пресметаме аглите или страните на триаголникот, ние ги користиме односите на должините на деловите од чевините прави ($AD, BE, CF$) за да воспоставиме врска со плоштините на под-триаголниците кои ги формира точката $S$.

**Тригерот:** Кога точка во внатрешноста на триаголник ги дели чевините прави на познати делови ($a, b, c$ и $d$), тоа е јасен сигнал за користење на својството дека односот на деловите од висините е еднаков на односот на соодветните плоштини.

Зошто ова функционира? Триаголниците $BCS$ и $ABC$ ја делат истата основа $BC$. Нивните плоштини се однесуваат како нивните висини спуштени кон таа основа. Бидејќи овие висини се паралелни, тие формираат слични триаголници со отсечката $AD$, па односот на висините е еднаков на односот $SD/AD$. Оваа „елегантна синтеза“ ни овозможува да го трансформираме геометрискиот проблем во чиста алгебарска равенка.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Воспоставување на врската помеѓу деловите и плоштината</summary>

Нека $P$ е плоштината на триаголникот $ABC$, а $P_{BCS}, P_{CAS}, P_{ABS}$ се плоштините на триаголниците формирани од точката $S$. Да ги разгледаме триаголниците $BCS$ и $ABC$. Тие имаат заедничка страна $BC$. Ако спуштиме висини од $S$ и од $A$ кон страната $BC$ (нека се $h_S$ и $h_A$), тогаш:

$$\frac{P_{BCS}}{P} = \frac{h_S}{h_A}$$

Од сличноста на триаголниците формирани од овие висини и правата $AD$ (види извор), имаме дека $\frac{h_S}{h_A} = \frac{SD}{AD}$. Бидејќи $AD = AS + SD = a + d$, добиваме:

$$\frac{P_{BCS}}{P} = \frac{d}{a+d}$$

Аналогно, за другите два триаголници важи:

$$\frac{P_{CAS}}{P} = \frac{d}{b+d} \quad \text{и} \quad \frac{P_{ABS}}{P} = \frac{d}{c+d}$$

</details>

<details>
<summary>Чекор 2: Формирање на главната равенка</summary>

Бидејќи триаголниците $BCS, CAS$ и $ABS$ целосно го покриваат триаголникот $ABC$ без преклопување, збирот на нивните плоштини е еднаков на $P$:

$$\frac{P_{BCS}}{P} + \frac{P_{CAS}}{P} + \frac{P_{ABS}}{P} = 1$$

Заменувајќи ги изразите од Чекор 1, ја добиваме клучната равенка:

$$\frac{d}{a+d} + \frac{d}{b+d} + \frac{d}{c+d} = 1$$

Бидејќи е дадено дека $d = 3$, равенката станува:

$$\frac{3}{a+3} + \frac{3}{b+3} + \frac{3}{c+3} = 1$$

</details>

<details>
<summary>Чекор 3: Алгебарска манипулација за наоѓање на abc</summary>

Ја средуваме равенката со доведување на заеднички именител:

$$3[(b+3)(c+3) + (a+3)(c+3) + (a+3)(b+3)] = (a+3)(b+3)(c+3)$$

Левата страна (LHS):
$$3[bc + 3b + 3c + 9 + ac + 3a + 3c + 9 + ab + 3a + 3b + 9]$$
$$3[ab + bc + ca + 6(a+b+c) + 27] = 3(ab+bc+ca) + 18(a+b+c) + 81$$

Десната страна (RHS):
$$(a+3)(bc + 3b + 3c + 9) = abc + 3ab + 3ac + 9a + 3bc + 9b + 9c + 27$$
$$abc + 3(ab+bc+ca) + 9(a+b+c) + 27$$

Изедначувајќи ги LHS и RHS:
$$3(ab+bc+ca) + 18(a+b+c) + 81 = abc + 3(ab+bc+ca) + 9(a+b+c) + 27$$

Членовите $3(ab+bc+ca)$ се кратат:
$$18(a+b+c) + 81 = abc + 9(a+b+c) + 27$$
$$abc = 9(a+b+c) + 54$$

Заменуваме $a+b+c = 43$:
$$abc = 9(43) + 54 = 387 + 54 = 441$$

</details>

**Краен одговор:** $\boxed{441}$

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Овој идентитет $\sum \frac{SD}{AD} = 1$ е фундаментален. Тој е директно поврзан со Чевината теорема. Запомнете: ако точката е внатрешна, збирот на односите на „малите“ делови ($d$) кон целите чевини е секогаш 1.
2.  **Чести Грешки:** Најчеста грешка е обидот да се решат $a, b, c$ поединечно. Задачата не дава доволно информации за тоа, но нивната симетрија во равенката овозможува директно пресметување на производот $abc$.
3.  **Зошто ова е важно:** Оваа техника се користи за докажување на многу познати олимписки теореми, како што е теоремата на Ван Шутен или Лајбницовата формула за растојанија во триаголник.

### 🔗 Поврзани вештини
* **Примарна вештина:** Плоштински метод (Macedonian: Плоштински метод)
* **Потребни предзнаења:** Сличност на триаголници, алгебарско средување на изрази со три променливи.

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Define vertices of triangle ABC
        A = np.array()
        B = np.array([-4, -2, 0])
        C = np.array([4, -2, 0])
        
        # Interior point S
        S = np.array([0, -0.2, 0])
        
        # Ceveian points D, E, F (Approximated for visual clarity)
        # AD passes through S. Let's find D on BC.
        D = np.array([0, -2, 0]) 
        # BE passes through S. E on AC.
        E = np.array([2, 0.5, 0])
        # CF passes through S. F on AB.
        F = np.array([-2, 0.5, 0])
        
        # Drawing elements
        tri = Polygon(A, B, C, color=BLACK, stroke_width=4)
        line_ad = Line(A, D, color=BLACK, stroke_width=2)
        line_be = Line(B, E, color=BLACK, stroke_width=2)
        line_cf = Line(C, F, color=BLACK, stroke_width=2)
        
        # Highlights
        dot_s = Dot(S, color=RED)
        lbl_s = MathTex("S", color=RED).next_to(S, DOWN, buff=0.1)
        
        # Vertex Labels
        lbl_a = MathTex("A", color=BLACK).next_to(A, UP)
        lbl_b = MathTex("B", color=BLACK).next_to(B, DL)
        lbl_c = MathTex("C", color=BLACK).next_to(C, DR)
        lbl_d = MathTex("D", color=BLACK).next_to(D, DOWN)
        lbl_e = MathTex("E", color=BLACK).next_to(E, UR)
        lbl_f = MathTex("F", color=BLACK).next_to(F, UL)
        
        # Segment length indicators (Abstract)
        lbl_a_val = MathTex("a", color=BLUE).move_to((A + S)/2 + LEFT*0.3)
        lbl_d_val = MathTex("d", color=BLUE).move_to((S + D)/2 + LEFT*0.3)

        self.add(tri, line_ad, line_be, line_cf, dot_s, lbl_s)
        self.add(lbl_a, lbl_b, lbl_c, lbl_d, lbl_e, lbl_f)
        self.add(lbl_a_val, lbl_d_val)
        
        # Equation display
        eq = MathTex(r"\frac{d}{a+d} + \frac{d}{b+d} + \frac{d}{c+d} = 1", color=BLACK).to_edge(RIGHT).shift(UP*1)
        res = MathTex("abc = 441", color=BLACK).next_to(eq, DOWN, buff=0.5)
        rect = SurroundingRectangle(res, color=RED)
        
        self.add(eq, res, rect)
```