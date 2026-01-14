---
problem_id: sigma_133_1809
title: Точката на пресек на дијагоналите и педалната кружница
grade: 10
difficulty: 6
type: geometry
tags:
  - паралелограм
  - циклични_четвртинагоници
  - педална_кружница
  - проекции
primary_skill: циклични_четвртинагоници
related_skills:
  - централен_и_периферен_агол
  - својства_на_паралелограм
source: Сигма 133 / Сигма 134
---

# Точката на пресек на дијагоналите и педалната кружница

# Текст на задачата
Нека $ABCD$ е паралелограм со остар агол во темето $A$. Подножјата на нормалите спуштени од темето $C$ на правите $AB, BD, AD$ се $P, Q, R$, соодветно. Докажи дека пресекот на дијагоналите на тој паралелограм лежи на опишаната кружница околу триаголникот $PQR$.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Најпрво идентификувај ги цикличните четвртинагоници. Погледни ги точките $P$ и $Q$ – тие се проекции на $C$ врз две прави што се сечат во $B$. Што ни кажува тоа за отсечката $BC$?

$$ \angle CPC = \angle CQC = 90^\circ $$

2. Слично, најди ги другите два циклични четвртинагоници поврзани со точките $R$ и $Q$, односно $P$ и $R$.

3. Каде се наоѓа центарот на кружницата опишана околу четвртинаголникот $APCR$? Размисли за својството на дијагоналите на паралелограмот.

$$AO = OC$$

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Оваа задача нè внесува во светот на **педалните кружници**. Кога имаме точка (во овој случај $C$) и нејзини проекции на страните на некој триаголник или многуаголник, секогаш бараме циклични структури.

**Клучниот тригер:** Проекциите $P, Q, R$ веднаш создаваат прави агли. Овие агли се „прозорец“ кон циклични четвртинагоници. На пример, $C$ се проектира на $AB$ во $P$ и на $BD$ во $Q$. Бидејќи $\angle CPC = 90^\circ$ и $\angle CQC = 90^\circ$, точките $C, P, Q, B$ лежат на кружница со дијаметар $BC$.

**Детективска работа:** Зошто точката $O$ (пресекот на дијагоналите) е важна? Кај паралелограмот, $O$ е средина на дијагоналата $AC$. Ако ја погледнеме кружницата опишана околу $APCR$, нејзиниот дијаметар е токму $AC$, што значи $O$ е нејзиниот центар! Сега, целта е да покажеме дека аголот под кој се гледа отсечката $PR$ од точките $Q$ и $O$ е ист.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Идентификување на аглите и цикличните четвртинагоници</summary>

Нека $\angle BAD = \alpha$. Поради својствата на паралелограмот ($AD \parallel BC$ и $AB \parallel CD$), важи:

$$ \angle BAD = \angle PBC = \angle CDR = \alpha $$

Ова е точно бидејќи $\angle PBC$ е агол меѓу правата $AB$ и страната $BC$ (согласност со $\angle BAD$), а $\angle CDR$ е агол меѓу правата $AD$ и страната $CD$.

Да ги разгледаме четвртинаголниците формирани од проекциите:
1. Четвртинаголникот $PCQB$: Бидејќи $\angle CPC = \angle CQC = 90^\circ$, точките $P, C, Q, B$ лежат на кружница со дијаметар $BC$. Од ова следува дека периферните агли над ист лак се еднакви:

$$ \angle PQC = \angle PBC = \alpha $$

2. Четвртинаголникот $CRDQ$: Бидејќи $\angle CQC = \angle CRC = 90^\circ$, точките $C, R, Q, D$ лежат на кружница со дијаметар $CD$. Оттука:

$$ \angle CQR = \angle CDR = \alpha $$

</details>

<details>
<summary>Чекор 2: Пресметување на аголот PQR</summary>

Сега можеме да го најдеме вкупниот агол во темето $Q$:

$$ \angle PQR = \angle PQC + \angle CQR = \alpha + \alpha = 2\alpha $$

Оваа релација (1) е клучна за докажување на концикличноста.

</details>

<details>
<summary>Чекор 3: Анализа на кружницата со центар O</summary>

Да го разгледаме четвртинаголникот $APCR$. Бидејќи $\angle APC = 90^\circ$ и $\angle ARC = 90^\circ$, тој е цикличен со дијаметар $AC$.
Пресекот на дијагоналите на паралелограмот $ABCD$, точката $O$, е средина на отсечката $AC$. Значи, $O$ е центар на кружницата опишана околу $APCR$.

Во оваа кружница:
- $\angle PAR = \angle BAD = \alpha$ е периферен агол над лакот $PR$.
- $\angle POR$ е централен агол над истиот лак $PR$.

Според теоремата за централен и периферен агол:

$$ \angle POR = 2 \cdot \angle PAR = 2\alpha $$

Оваа релација (2) ни го дава потребниот доказ.

</details>

<details>
<summary>Чекор 4: Финализација на доказот</summary>

Од равенствата (1) и (2) имаме:

$$ \angle PQR = \angle POR = 2\alpha $$

Бидејќи отсечката $PR$ се гледа под ист агол од точките $Q$ и $O$, и бидејќи двете точки се наоѓаат од иста страна на правата $PR$ (поради остриот агол $\alpha$), заклучуваме дека точките $P, Q, R, O$ лежат на иста кружница. Тоа значи дека $O$ лежи на опишаната кружница околу $\triangle PQR$.

</details>

**Краен одговор:** Докажано е дека точките $P, Q, R$ и $O$ се конциклични, со што точката $O$ лежи на опишаната кружница околу $\triangle PQR$.

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Проекции на точка врз прави секогаш „врескаат“ за Талесови кружници. Дијаметарот секогаш ќе биде отсечката од почетната точка ($C$) до заедничкото теме на правите ($B, D$ или $A$).
2.  **Чести Грешки:** Не мешајте ги дијаметрите. Секој пар проекции припаѓа на своја кружница. Клучот е да се најде врска меѓу нив преку заеднички агли.
3.  **Зошто ова е важно:** Овој проблем е увертира во теоријата на Сипсонова права и педални триаголници. Покажува како внатрешните точки на геометриските фигури се поврзани со нивната надворешна проекција.

### 🔗 Поврзани вештини
* **Примарна вештина:** Користење на својства на циклични четвртинагоници
* **Потребни предзнаења:** Централен и периферен агол, својства на паралелограм, проекција на точка врз права.

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Expert Tip 7: Define mathematical coordinates for a parallelogram
        # Angle A is acute (approx 60 deg)
        A = np.array([-3, -1.5, 0])
        B = np.array([1, -1.5, 0])
        D = np.array([-1, 1.5, 0])
        C = B + (D - A)
        
        # Parallelogram lines
        parallelogram = Polygon(A, B, C, D, color=BLACK, stroke_width=3)
        diag_ac = Line(A, C, color=GRAY, stroke_width=2)
        diag_bd = Line(B, D, color=GRAY, stroke_width=2)
        
        # Intersection point O
        O = (A + C) / 2
        dot_o = Dot(O, color=BLACK)
        
        # Projections from C onto lines AB, BD, AD
        # Projection P on AB (line through A, B)
        # Note: A-B is horizontal, so P has same y as B
        P = np.array([C, B, 0])
        
        # Projection R on AD
        line_ad = Line(A, D)
        R = line_ad.get_projection(C)
        
        # Projection Q on BD
        line_bd = Line(B, D)
        Q = line_bd.get_projection(C)
        
        # Draw projection lines
        cp = DashedLine(C, P, color=BLUE)
        cq = DashedLine(C, Q, color=BLUE)
        cr = DashedLine(C, R, color=BLUE)
        
        # pedal triangle PQR
        pedal_tri = Polygon(P, Q, R, color=RED, stroke_width=4)
        
        # Circumcircle of PQR
        # To show O lies on it, we calculate the circle from P, Q, R
        circle_pqr = Circle.from_three_points(P, Q, R, color=RED, stroke_width=2)
        
        # Labels - ENGLISH ONLY
        lbl_a = MathTex("A", color=BLACK).next_to(A, DL)
        lbl_b = MathTex("B", color=BLACK).next_to(B, DR)
        lbl_c = MathTex("C", color=BLACK).next_to(C, UR)
        lbl_d = MathTex("D", color=BLACK).next_to(D, UL)
        lbl_o = MathTex("O", color=BLACK).next_to(O, DOWN, buff=0.1)
        lbl_p = MathTex("P", color=BLACK).next_to(P, DOWN)
        lbl_q = MathTex("Q", color=BLACK).next_to(Q, UP + RIGHT, buff=0.05)
        lbl_r = MathTex("R", color=BLACK).next_to(R, LEFT)
        
        # Add everything to scene
        self.add(parallelogram, diag_ac, diag_bd, dot_o)
        self.add(cp, cq, cr, pedal_tri, circle_pqr)
        self.add(lbl_a, lbl_b, lbl_c, lbl_d, lbl_o, lbl_p, lbl_q, lbl_r)
        
        # Highlight angle alpha
        angle_alpha = Angle(Line(A, B), Line(A, D), radius=0.4, color=BLACK)
        lbl_alpha = MathTex("\\alpha", color=BLACK).next_to(angle_alpha, RIGHT, buff=0.1)
        self.add(angle_alpha, lbl_alpha)

```