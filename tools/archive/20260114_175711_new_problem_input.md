---
problem_id: sigma_133_1810
title: Карактеризација на триаголник преку тригонометриско равенство
grade: 10
difficulty: 4
type: algebra
tags:
  - тригонометрија
  - триаголник
  - синусна_теорема
  - адициони_теореми
primary_skill: тригонометриски_манипулации
related_skills:
  - својства_на_триаголник
  - решавање_тригонометриски_равенки
source: Сигма 134, задача 1810
---

# Карактеризација на триаголник преку тригонометриско равенство

# Текст на задачата
Ако за страните $a, b$ и соодветните агли $\alpha, \beta$ во триаголникот $ABC$ важи равенството:

$$(a^2 + b^2) \sin(\alpha - \beta) = (a^2 - b^2) \sin(\alpha + \beta)$$

тогаш триаголникот $ABC$ е рамнокрак или правоаголен. Докажи!

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Првиот чекор е секогаш да ги елиминираме заградите кај синусот. Искористи ги адиционите теореми за $\sin(\alpha - \beta)$ и $\sin(\alpha + \beta)$.

$$\sin(\alpha \pm \beta) = \sin \alpha \cos \beta \pm \cos \alpha \sin \beta$$

2. Групни ги членовите со $a^2$ на една страна и со $b^2$ на другата страна.

3. Триаголникот има страни $a$ и $b$ и агли $\alpha$ и $\beta$. Како најлесно да ги поврземе? Секако, преку Синусната теорема.

$$\frac{a}{\sin \alpha} = \frac{b}{\sin \beta}$$

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Кога ќе видиме равенство кое ги меша должините на страните и тригонометриските вредности на аглите, нашиот главен **тригер** е да го претвориме во чисто тригонометриско равенство или чисто алгебарско. Бидејќи аглите се веќе „заробени“ во синусни функции, најелегантно е страните $a$ и $b$ да ги изразиме преку аглите користејќи ја Синусната теорема.

Зошто ова е добар пат? Затоа што изразите $a^2 + b^2$ и $a^2 - b^2$ во комбинација со $\sin(\alpha \pm \beta)$ сугерираат дека по средувањето ќе дојдеме до некоја основна тригонометриска релација како $\sin 2\alpha = \sin 2\beta$.

Прашање за размислување: Ако $\sin 2\alpha = \sin 2\beta$, дали тоа значи само дека $\alpha = \beta$? Што ако аглите се суплементни? Токму тука лежи разликата меѓу рамнокрак и правоаголен триаголник.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Примена на адициони теореми</summary>

Поаѓаме од даденото равенство и ги применуваме адиционите формули за синус:

$$(a^2 + b^2)(\sin \alpha \cos \beta - \cos \alpha \sin \beta) = (a^2 - b^2)(\sin \alpha \cos \beta + \cos \alpha \sin \beta)$$

Сега ги множиме заградите:

$$a^2 \sin \alpha \cos \beta - a^2 \cos \alpha \sin \beta + b^2 \sin \alpha \cos \beta - b^2 \cos \alpha \sin \beta = a^2 \sin \alpha \cos \beta + a^2 \cos \alpha \sin \beta - b^2 \sin \alpha \cos \beta - b^2 \cos \alpha \sin \beta$$

</details>

<details>
<summary>Чекор 2: Средување и групирање на изразот</summary>

Ги кратиме еднаквите членови од двете страни ($a^2 \sin \alpha \cos \beta$ и $-b^2 \cos \alpha \sin \beta$):

$$- a^2 \cos \alpha \sin \beta + b^2 \sin \alpha \cos \beta = a^2 \cos \alpha \sin \beta - b^2 \sin \alpha \cos \beta$$

Ги префрламе членовите со $a^2$ на една, а со $b^2$ на друга страна:

$$2b^2 \sin \alpha \cos \beta = 2a^2 \cos \alpha \sin \beta$$

По делење со 2 добиваме:

$$b^2 \sin \alpha \cos \beta = a^2 \cos \alpha \sin \beta \quad (1)$$

</details>

<details>
<summary>Чекор 3: Користење на Синусната теорема</summary>

Од Синусната теорема знаеме дека $a = 2R \sin \alpha$ и $b = 2R \sin \beta$. Ги заменуваме овие изрази во равенката (1):

$$(2R \sin \beta)^2 \sin \alpha \cos \beta = (2R \sin \alpha)^2 \cos \alpha \sin \beta$$

$$4R^2 \sin^2 \beta \sin \alpha \cos \beta = 4R^2 \sin^2 \alpha \cos \alpha \sin \beta$$

Бидејќи $R \neq 0$ и $\sin \alpha, \sin \beta \neq 0$ (како агли во триаголник), можеме да ја поделиме целата равенка со $4R^2 \sin \alpha \sin \beta$:

$$\sin \beta \cos \beta = \sin \alpha \cos \alpha$$

</details>

<details>
<summary>Чекор 4: Финална дискусија на решенијата</summary>

Користејќи ја формулата за двоен агол $2 \sin x \cos x = \sin 2x$, добиваме:

$$\sin 2\beta = \sin 2\alpha$$

Ова равенство има две можни решенија во рамките на триаголник ($0 < \alpha, \beta < 180^\circ$):

1. $2\alpha = 2\beta \implies \alpha = \beta$. Во овој случај триаголникот е **рамнокрак**.

2. $2\alpha = 180^\circ - 2\beta \implies 2\alpha + 2\beta = 180^\circ \implies \alpha + \beta = 90^\circ$. Бидејќи збирот на аглите е $180^\circ$, следува дека $\gamma = 90^\circ$. Во овој случај триаголникот е **правоаголен**.

</details>

**Краен одговор:** Докажано е дека $\alpha = \beta$ или $\gamma = 90^\circ$, што значи дека триаголникот е рамнокрак или правоаголен.

## 👨‍🏫 Менторски Белешки
1. **Златен Совет:** Секогаш кога ќе стигнете до $\sin X = \sin Y$, не брзајте само со $X = Y$. Запомнете ја „симетријата“ на синусот кај суплементните агли. Тоа е често клучот во геометриските докази.
2. **Чести Грешки:** Некои ученици се обидуваат да ги заменат синусите преку Косинусната теорема, што ја прави задачата непотребно комплицирана. Синусната теорема е „почист“ инструмент за вакви соодноси.
3. **Зошто ова е важно:** Оваа задача ја демонстрира моќта на тригонометриската форма на геометриските својства. Слични идентитети често се појавуваат на натпревари за карактеризација на специфични фигури.

### 🔗 Поврзани вештини
* **Примарна вештина:** Тригонометриски трансформации
* **Потребни предзнаења:** Адициони формули, Синусна теорема, формули за двоен агол.

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Expert Tip 7: Coordinates to point (c2p)
        # Defining a triangle for visualization
        # Vertices for an isosceles or right-angled triangle candidate
        A_coord = np.array([-2, -1, 0])
        B_coord = np.array([2, -1, 0])
        C_coord = np.array([0, 2, 0])
        
        triangle = Polygon(A_coord, B_coord, C_coord, color=BLACK, stroke_width=4)
        
        # Labels for sides and angles (STRICTLY ENGLISH/MATH)
        lbl_A = MathTex("A", color=BLACK).next_to(A_coord, DL)
        lbl_B = MathTex("B", color=BLACK).next_to(B_coord, DR)
        lbl_C = MathTex("C", color=BLACK).next_to(C_coord, UP)
        
        lbl_alpha = MathTex("\\alpha", color=BLACK).scale(0.8).shift(A_coord + RIGHT*0.5 + UP*0.3)
        lbl_beta = MathTex("\\beta", color=BLACK).scale(0.8).shift(B_coord + LEFT*0.5 + UP*0.3)
        
        lbl_a = MathTex("a", color=BLACK).next_to(Line(B_coord, C_coord).get_center(), UR, buff=0.1)
        lbl_b = MathTex("b", color=BLACK).next_to(Line(A_coord, C_coord).get_center(), UL, buff=0.1)
        
        # Main equation display
        eq = MathTex("(a^2 + b^2) \\sin(\\alpha - \\beta) = (a^2 - b^2) \\sin(\\alpha + \\beta)", color=BLACK).to_edge(UP)
        
        # Final conclusions
        conclusion = VGroup(
            MathTex("\\alpha = \\beta \\implies \\text{Isosceles}", color=RED),
            MathTex("\\alpha + \\beta = 90^\\circ \\implies \\text{Right-angled}", color=BLUE)
        ).arrange(DOWN, buff=0.5).to_edge(RIGHT).scale(0.7)
        
        # Add everything to the frame
        self.add(triangle, lbl_A, lbl_B, lbl_C, lbl_alpha, lbl_beta, lbl_a, lbl_b, eq, conclusion)
```