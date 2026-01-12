---
problem_id: regional_2025_4_2a
title: Растојанија, Сличност и Синусна Теорема
grade: 12
difficulty: 5
type: geometry
tags:
  - kruznica
  - slicnost
  - sinusna_teorema
  - tetiva
primary_skill: slicnost_na_triagolnici
related_skills:
  - trigonometrija_vo_triagolnik
  - sinusna_teorema
source: Сигма 139 (Регионален натпревар 2025)
---

# Растојанија, Сличност и Синусна Теорема

# Текст на задачата
Нека $AB$ и $AC$ се тетиви на кружница со радиус $R$. Точката $M$ припаѓа на правата $AB$, а нејзиното растојание од правата $AC$ е еднакво на должината $AC$. Точката $N$ припаѓа на правата $AC$, а нејзиното растојание од правата $AB$ е еднакво на должината $AB$. Докажи дека $MN = 2R$.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Дефинирајте го аголот $\angle BAC = \alpha$. Како растојанието на точка од права е поврзано со синусот на аголот?

$$dist(M, AC) = AM \sin \alpha$$

2. Изразете ги должините $AM$ и $AN$ преку страните на триаголникот $ABC$ и синусот на аголот $\alpha$.

3. Разгледајте ги триаголниците $ABC$ и $AMN$. Дали тие се слични? Колкав е нивниот коефициент на сличност?

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Оваа задача на прв поглед изгледа како проблем на конструкција, но суштината лежи во пресметување на соодноси. **Тригерот** е дефиницијата за растојание од точка до права. Кога точка $M$ лежи на еден крак од агол, нејзиното растојание до другиот крак е директно пропорционално со нејзината оддалеченост од темето на аголот.

Клучниот увид е дека условите $dist(M, AC) = AC$ и $dist(N, AB) = AB$ всушност ни кажуваат колку пати отсечките $AM$ и $AN$ се "подолги" од соодветните страни на триаголникот $ABC$. Ако го означиме аголот кај темето $A$ со $\alpha$, тогаш тој сооднос секогаш ќе биде $1/\sin \alpha$.

Ова неминовно води кон сличност на триаголниците $ABC$ и $AMN$. Штом ја утврдиме сличноста, должината $MN$ ќе зависи само од $BC$ и истиот тој синус. Последната коцка во мозаикот е Синусната теорема, која го поврзува $BC$ со радиусот на опишаната кружница $R$.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Пресметување на должините AM и AN</summary>

Нека $\angle BAC = \alpha$. Нека $M'$ е проекцијата на точката $M$ врз правата $AC$, а $N'$ е проекцијата на точката $N$ врз правата $AB$. Според условот на задачата:
$$MM' = AC \quad \text{и} \quad NN' = AB$$

Во правоаголниот триаголник $AMM'$, имаме:
$$MM' = AM \sin \alpha \implies AC = AM \sin \alpha \implies AM = \frac{AC}{\sin \alpha}$$

Слично, во правоаголниот триаголник $ANN'$, имаме:
$$NN' = AN \sin \alpha \implies AB = AN \sin \alpha \implies AN = \frac{AB}{\sin \alpha}$$

</details>

<details>
<summary>Чекор 2: Докажување на сличност помеѓу триаголниците ABC и AMN</summary>

Да ги разгледаме триаголниците $ABC$ и $AMN$. Тие имаат заеднички агол кај темето $A$ ($\angle BAC = \angle MAN = \alpha$). Од претходниот чекор, ги имаме соодносите на страните:
$$\frac{AM}{AC} = \frac{1}{\sin \alpha} \quad \text{и} \quad \frac{AN}{AB} = \frac{1}{\sin \alpha}$$

Бидејќи $\frac{AM}{AC} = \frac{AN}{AB}$, заклучуваме дека $\triangle ABC \sim \triangle AMN$ според признакот за сличност на триаголници (две страни пропорционални и аголот меѓу нив еднаков).

Коефициентот на сличност $k$ изнесува:
$$k = \frac{MN}{BC} = \frac{AM}{AC} = \frac{1}{\sin \alpha}$$

</details>

<details>
<summary>Чекор 3: Примена на синусна теорема и заклучок</summary>

Од сличноста имаме:
$$MN = \frac{BC}{\sin \alpha}$$

Од Синусната теорема за триаголникот $ABC$, знаеме дека односот на една страна и синусот на спротивниот агол е еднаков на дијаметарот на опишаната кружница:
$$\frac{BC}{\sin \alpha} = 2R$$

Со замена на овој израз во равенката за $MN$, добиваме:
$$MN = 2R$$

Со тоа тврдењето е докажано.

</details>

**Краен одговор:** Тврдењето дека $\boxed{MN = 2R}$ е докажано преку сличност на триаголници и примена на Синусната теорема.

## 👨‍🏫 Менторски Белешки
1. **Златен Совет:** Секогаш кога во задача ќе видите растојание од точка до права која формира познат агол, веднаш помислете на тригонометриските функции во правоаголен триаголник. Тоа е најбрзиот начин да се воспостави алгебарска врска.
2. **Чести Грешки:** Студентите често се обидуваат да ја решат задачата со пресметување на координати. Иако е можно, синтетичкиот пристап преку сличност е многу поелегантен и помалку подложен на грешки во пресметките.
3. **Зошто ова е важно:** Оваа задача ја демонстрира убавината на геометриската инваријантност — без разлика каква е формата на триаголникот $ABC$, отсечката $MN$ секогаш ќе зависи само од големината на кружницата.

### 🔗 Поврзани вештини
* **Примарна вештина:** Сличност на триаголници (Macedonian: Сличност на триаголници)
* **Потребни предзнаења:** Синусна теорема, дефиниција за синус во правоаголен триаголник.

# Manim Code
```python
from manim import *
import numpy as np

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parameters
        R = 2.5
        center = ORIGIN
        alpha = 50 * DEGREES
        beta = 70 * DEGREES
        
        # Points on Circle
        phi_A = 110 * DEGREES
        phi_B = phi_A - 2 * alpha
        phi_C = phi_A + 2 * (180*DEGREES - alpha - beta) # Arbitrary C
        
        A = R * np.array([np.cos(phi_A), np.sin(phi_A), 0])
        B = R * np.array([np.cos(phi_B), np.sin(phi_B), 0])
        C = R * np.array([np.cos(10 * DEGREES), np.sin(10 * DEGREES), 0]) # Manual adjustment for visual clarity
        
        # Re-calculating alpha for the current points
        vec_AB = B - A
        vec_AC = C - A
        ang_A = np.arccos(np.dot(vec_AB, vec_AC) / (np.linalg.norm(vec_AB) * np.linalg.norm(vec_AC)))
        
        # Calculate M and N
        # AM = AC / sin(ang_A)
        len_AC = np.linalg.norm(vec_AC)
        len_AB = np.linalg.norm(vec_AB)
        
        M = A + (vec_AB / len_AB) * (len_AC / np.sin(ang_A))
        N = A + (vec_AC / len_AC) * (len_AB / np.sin(ang_A))
        
        # Shapes
        circle = Circle(radius=R, color=BLACK, stroke_width=2)
        tri_abc = Polygon(A, B, C, color=BLACK, stroke_width=4)
        line_mn = Line(M, N, color=RED, stroke_width=4)
        line_am = Line(A, M, color=BLACK, stroke_width=2, stroke_dash_pattern=[0.05, 0.05])
        line_an = Line(A, N, color=BLACK, stroke_width=2, stroke_dash_pattern=[0.05, 0.05])
        
        # Projections for visuals
        M_proj = A + (np.dot(M-A, vec_AC/len_AC)) * (vec_AC/len_AC)
        N_proj = A + (np.dot(N-A, vec_AB/len_AB)) * (vec_AB/len_AB)
        
        dist_m = DashedLine(M, M_proj, color=BLUE)
        dist_n = DashedLine(N, N_proj, color=BLUE)
        
        # Labels
        lbl_a = MathTex("A", color=BLACK).next_to(A, UP)
        lbl_b = MathTex("B", color=BLACK).next_to(B, LEFT)
        lbl_c = MathTex("C", color=BLACK).next_to(C, RIGHT)
        lbl_m = MathTex("M", color=BLACK).next_to(M, DOWN)
        lbl_n = MathTex("N", color=BLACK).next_to(N, RIGHT)
        lbl_mn = MathTex("MN = 2R", color=RED).to_edge(DOWN)

        # Add to scene
        self.add(circle, tri_abc, line_am, line_an, line_mn, dist_m, dist_n)
        self.add(lbl_a, lbl_b, lbl_c, lbl_m, lbl_n, lbl_mn)
```