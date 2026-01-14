---
problem_id: geometry_circles_midpoint_parallel
title: Средина на тетива и пресек на кружници
grade: 10
difficulty: 6
type: geometry
tags:
  - kruzni_linii
  - sredna_linija
  - simetrala_na_otsecka
  - izometricni_transformacii
primary_skill: simetrala_na_otsecka
related_skills:
  - sredna_linija_vo_triagolnik
  - perpendikularnost
source: Legendary Math Coach
---

# Средина на тетива и пресек на кружници

# Текст на задачата
Дадени се две кружници $k_1$ и $k_2$ со центри $O$ и $O_1$ соодветно, така што центарот $O_1$ лежи на кружницата $k_1$. Нека $A$ е произволна точка од $k_2$, а $M$ е средишна точка на отсечката $AO_1$.
Ако $B$ е точка од $k_2$ ($B \neq A$), таква што тетивата $AB$ е паралелна со правата $MO$, докажи дека средишната точка на отсечката $AB$ лежи на кружницата $k_1$.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Нека $K$ е средината на отсечката $AB$. Што знаеме за правата $O_1K$ во однос на тетивата $AB$?

$$O_1K \perp AB$$

2. Искористете ја средната линија во триаголникот $ABO_1$. Поврзете ги $M$ и $K$. Каква врска има $MK$ со радиусот на $k_2$?

$$MK = \frac{1}{2}R_2$$

3. Анализирајте го триаголникот $MO_1K$. Дали е рамнокрак? Како правата $MO$ се однесува кон основата $O_1K$?

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Ова е класичен проблем кој ја крие својата убавина во симетријата.
**Тригерот** овде е комбинацијата од „средина на тетива“ и „паралелни прави“.
1.  Штом слушнеме „средина на тетива“ ($K$ за $AB$), веднаш помислуваме на перпендикуларност: $O_1K \perp AB$.
2.  Штом имаме „паралелност“ ($AB \parallel MO$) и перпендикуларност, знаеме дека $O_1K \perp MO$. Ова е клучен агол од $90^\circ$.
3.  Следната трага е точката $M$. Таа е средина на $AO_1$. Точката $K$ е средина на $AB$. Ова *вика* да се искористи **Средна линија** во триаголник.

Интуицијата ни вели: Ако докажеме дека триаголникот $MO_1K$ е рамнокрак и дека $MO$ е негова висина (а со тоа и симетрала), тогаш точката $O$ ќе биде подеднакво оддалечена од $K$ и $O_1$. Бидејќи $O_1$ е веќе на $k_1$, и $K$ мора да биде таму. Да го формализираме ова со чиста синтетичка геометрија.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Дефинирање на точките и својство на тетивата</summary>

Нека $K$ е средишната точка на отсечката $AB$. Бидејќи $AB$ е тетива во кружницата $k_2$ со центар $O_1$, правата што ги поврзува центарот и средината на тетивата е нормална на тетивата.

$$O_1K \perp AB$$

Според условот на задачата, имаме $AB \parallel MO$. Бидејќи $O_1K$ е нормална на $AB$, таа мора да биде нормална и на секоја права паралелна со $AB$.

$$O_1K \perp MO$$

Ова значи дека правата $MO$ е висина спуштена од темето $M$ кон страната $O_1K$ во триаголникот $\triangle MO_1K$.

</details>

<details>
<summary>Чекор 2: Примена на средна линија во триаголник</summary>

Да го разгледаме триаголникот $\triangle ABO_1$.
- $K$ е средина на страната $AB$.
- $M$ е средина на страната $AO_1$ (дадено во задачата).

Според својството за средна линија, отсечката $MK$ е паралелна со третата страна $BO_1$ и е еднаква на нејзината половина.

$$MK = \frac{1}{2} O_1B$$

Но, $O_1B$ и $O_1A$ се радиуси на кружницата $k_2$ ($R_2$). Значи $O_1B = O_1A = R_2$.
Исто така, бидејќи $M$ е средина на $AO_1$, важи:

$$MO_1 = \frac{1}{2} AO_1 = \frac{1}{2} R_2$$

Од последните две равенства следува:

$$MK = \frac{1}{2} R_2 = MO_1$$

</details>

<details>
<summary>Чекор 3: Симетрала и завршен доказ</summary>

Во претходниот чекор покажавме дека $MK = MO_1$. Ова значи дека триаголникот $\triangle MO_1K$ е **рамнокрак** со врв во точката $M$ и основа $O_1K$.

Во Чекор 1 докажавме дека $MO \perp O_1K$.
Во рамнокрак триаголник ($\triangle MO_1K$), висината спуштена кон основата се совпаѓа со симетралата на основата.
Значи, правата $MO$ е **симетрала на отсечката** $O_1K$.

Според својството на симетралата, секоја точка што лежи на неа е подеднакво оддалечена од крајните точки на отсечката. Бидејќи центарот $O$ лежи на правата $MO$ (очигледно), важи:

$$OK = OO_1$$

Бидејќи $O_1$ лежи на кружницата $k_1$ со центар $O$, растојанието $OO_1$ е всушност радиусот на $k_1$ ($R_1$).

$$OK = R_1$$

Штом растојанието од центарот $O$ до точката $K$ е еднакво на радиусот на кружницата $k_1$, следува дека точката $K$ лежи на $k_1$.

</details>

**Краен одговор:** Докажавме дека $\boxed{K \in k_1}$.

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Секогаш кога имате средини на две страни во триаголник, барајте ја „средната линија“. Тоа е еден од најмоќните алатки во геометријата бидејќи пренесува и должина и паралелност.
2.  **Чести Грешки:** Учениците често забораваат дека $MO$ не мора да биде „внатре“ во триаголникот. Перпендикуларноста важи за правите (носителите), без разлика на позицијата на точките. Важно е строго да се дефинира дека $MO$ е симетрала на $O_1K$.
3.  **Зошто ова е важно:** Оваа задача илустрира како основните својства (симетрала на отсечка) се користат за дефинирање на геометриски места на точки (кружница).

### 🔗 Поврзани вештини
* **Примарна вештина:** Симетрала на отсечка (Macedonian: Симетрала на отсечка)
* **Потребни предзнаења:** Својства на тетива, средна линија во триаголник, својства на рамнокрак триаголник.

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # --- DEFINITIONS ---
        # Coordinates setup
        # O at origin
        O = ORIGIN
        R1 = 2.5
        
        # O1 on circle k1 (let's put it at angle 0 for simplicity, then rotate)
        O1 = np.array([R1, 0, 0]) 
        
        # k2 radius R2
        R2 = 1.8
        
        # Point A on k2. Let's pick an angle.
        angle_A = 120 * DEGREES
        A = O1 + np.array([R2 * np.cos(angle_A), R2 * np.sin(angle_A), 0])
        
        # M is midpoint of A O1
        M = (A + O1) / 2
        
        # Calculate vector MO
        vec_MO = O - M
        angle_MO = np.arctan2(vec_MO, vec_MO)
        
        # B is on k2 such that AB || MO.
        # This means vector AB has same direction as MO or -MO.
        # Let's solve geometrically: Intersect line through A parallel to MO with k2.
        # Line equation: P = A + t * vec_MO
        # Circle: |P - O1|^2 = R2^2
        # |A + t*v - O1|^2 = R2^2 => |(A-O1) + t*v|^2 = R2^2
        # Let U = A - O1 (vector from center). |U| = R2.
        # |U + t*v|^2 = |U|^2 + 2t(U.v) + t^2|v|^2 = R2^2
        # R2^2 + 2t(U.v) + t^2|v|^2 = R2^2
        # 2t(U.v) + t^2|v|^2 = 0
        # t(2(U.v) + t|v|^2) = 0
        # Solutions: t=0 (Point A), t = -2(U.v)/|v|^2 (Point B)
        
        U = A - O1
        v = vec_MO
        t_val = -2 * np.dot(U, v) / np.dot(v, v)
        B = A + t_val * v
        
        # K is midpoint of AB
        K = (A + B) / 2
        
        # --- VISUAL ELEMENTS ---
        
        # Circles
        k1 = Circle(radius=R1, color=BLUE, stroke_width=2).move_to(O)
        k2 = Circle(radius=R2, color=GREEN, stroke_width=2).move_to(O1)
        
        # Points
        pt_O = Dot(O, color=BLACK)
        pt_O1 = Dot(O1, color=BLACK)
        pt_A = Dot(A, color=BLACK)
        pt_B = Dot(B, color=BLACK)
        pt_M = Dot(M, color=RED)
        pt_K = Dot(K, color=RED)
        
        # Labels
        lbl_O = MathTex("O", color=BLACK).next_to(pt_O, DOWN)
        lbl_O1 = MathTex("O_1", color=BLACK).next_to(pt_O1, RIGHT)
        lbl_A = MathTex("A", color=BLACK).next_to(pt_A, UP)
        lbl_B = MathTex("B", color=BLACK).next_to(pt_B, LEFT)
        lbl_M = MathTex("M", color=BLACK).next_to(pt_M, UP, buff=0.1)
        lbl_K = MathTex("K", color=BLACK).next_to(pt_K, DL, buff=0.1)
        lbl_k1 = MathTex("k_1", color=BLUE).next_to(k1, UP)
        
        # Lines
        ln_AO1 = Line(A, O1, color=BLACK, stroke_width=2)
        ln_AB = Line(A, B, color=BLACK, stroke_width=3)
        ln_MO = DashedLine(M, O, color=BLACK)
        ln_O1K = Line(O1, K, color=BLACK, stroke_width=2)
        ln_MK = Line(M, K, color=RED, stroke_width=3)
        ln_MO1 = Line(M, O1, color=RED, stroke_width=3)
        
        # Right angle
        right_angle = RightAngle(ln_O1K, Line(O, M, color=BLACK), length=0.3, quadrant=(-1,-1))
        
        # Highlight Isosceles
        # MK = MO1 line highlighting is handled by creating specific red lines above
        
        # --- ANIMATION SCENE ---
        self.add(k1, k2, lbl_k1)
        self.add(pt_O, lbl_O, pt_O1, lbl_O1)
        self.add(pt_A, lbl_A, ln_AO1, pt_M, lbl_M)
        self.add(ln_MO)
        self.add(pt_B, lbl_B, ln_AB, pt_K, lbl_K)
        self.add(ln_O1K, right_angle)
        self.add(ln_MK, ln_MO1) # Highlight the isosceles legs
        
        # Final conclusion text
        conclusion = MathTex(r"OK = R_1 \implies K \in k_1", color=BLUE).to_edge(DOWN)
        self.add(conclusion)
```