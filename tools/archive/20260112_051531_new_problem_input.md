---
problem_id: geometry_triangle_bisector_1883
title: Должина на бисектриса во триаголник
grade: 10
difficulty: 4
type: geometry
tags:
  - triangle
  - angle_bisector
  - area_method
  - trigonometry
primary_skill: area_method
related_skills:
  - sine_rule
  - similar_triangles
source: Zbirka_Geom_1883
---

# Должина на бисектриса во триаголник

# Текст на задачата
Нека $ABC$ е триаголник кај кој $\overline{AB} = 9$, $\overline{AC} = 12$ и $\angle BAC = 120^\circ$. Нека симетралата на аголот во темето $A$ ја сече страната $BC$ во точка $D$. Одреди ја големината на отсечката $AD$.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Обиди се да ја пресметаш плоштината на триаголникот $ABC$ на два начини. Прво како целина, а потоа како збир на два помали триаголници.

$$P_{ABC} = P_{ABD} + P_{ADC}$$

2. Искористи ја формулата за плоштина на триаголник преку две страни и аголот меѓу нив: $P = \frac{1}{2}ab \sin \gamma$.

3. Забележи дека $\sin 120^\circ = \sin 60^\circ = \frac{\sqrt{3}}{2}$. Ова ќе ти овозможи да ги скратиш синусите од равенката.

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Ова е класична задача која може да се реши на „тежок“ начин (со Косинусна теорема за наоѓање на страната $BC$, па потоа Стјуартова теорема) и на „елегантен“ начин.

Најбрзиот и најелегантен алгебарски пристап е **Методот на плоштини**.
Бидејќи $AD$ е симетрала (бисектриса) на аголот $\alpha = 120^\circ$, таа го дели аголот на два еднакви дела од по $60^\circ$.
Ова е клучен момент! Аголот од $60^\circ$ и аголот од $120^\circ$ имаат иста вредност за синус ($\frac{\sqrt{3}}{2}$).

Ако ја запишеме плоштината на големиот триаголник како сума од плоштините на двата помали триаголници што ги формира бисектрисата, непознатата должина $x = AD$ ќе се појави како единствена променлива во линеарна равенка.

*Забелешка за натпреварувачи:* Постои и чисто геометриско решение (без тригонометрија) со повлекување на паралела, кое ќе го објасниме во „Менторски белешки“.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Поставување на равенството за плоштини</summary>

Нека $x = \overline{AD}$ е должината на бисектрисата.
Плоштината на триаголникот $ABC$ е еднаква на збирот на плоштините на триаголниците $ABD$ и $ADC$:

$$P_{ABC} = P_{ABD} + P_{ADC}$$

</details>

<details>
<summary>Чекор 2: Примена на тригонометриската формула за плоштина</summary>

Ја користиме формулата $P = \frac{1}{2} \cdot a \cdot b \cdot \sin \gamma$.

1. За $\triangle ABC$: страните се $AB=9, AC=12$, аголот е $120^\circ$.
2. За $\triangle ABD$: страните се $AB=9, AD=x$, аголот е $60^\circ$.
3. За $\triangle ADC$: страните се $AC=12, AD=x$, аголот е $60^\circ$.

Заменуваме во равенството од Чекор 1:

$$\frac{1}{2} \cdot 9 \cdot 12 \cdot \sin 120^\circ = \frac{1}{2} \cdot 9 \cdot x \cdot \sin 60^\circ + \frac{1}{2} \cdot 12 \cdot x \cdot \sin 60^\circ$$

</details>

<details>
<summary>Чекор 3: Упростување и решавање</summary>

Знаеме дека $\sin 120^\circ = \sin(180^\circ - 60^\circ) = \sin 60^\circ = \frac{\sqrt{3}}{2}$.
Бидејќи синусите се исти и ненулти, можеме да го поделиме целото равенство со $\frac{1}{2} \sin 60^\circ$.

Равенството се сведува на:

$$9 \cdot 12 = 9 \cdot x + 12 \cdot x$$

$$108 = x(9 + 12)$$

$$108 = 21x$$

$$x = \frac{108}{21}$$

Двата броја се деливи со 3:

$$x = \frac{36}{7}$$

</details>

**Краен одговор:** Должината на бисектрисата е $\boxed{\frac{36}{7}}$.

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет (Синтетичка Геометрија):** Еве како ова се решава **без тригонометрија** за помалку од 30 секунди!
    Продолжи ја страната $AC$ преку темето $A$ до точка $E$ така што $BE \parallel AD$.
    Бидејќи правите се паралелни:
    *   $\angle AEB = \angle CAD = 60^\circ$ (согласни агли).
    *   $\angle ABE = \angle BAD = 60^\circ$ (наизменични агли).
    Значи, $\triangle ABE$ е **рамностран**! Следи $AE = AB = 9$.
    Сега имаме слични триаголници $\triangle CAD \sim \triangle CBE$.
    $$\frac{AD}{BE} = \frac{AC}{CE} \implies \frac{x}{9} = \frac{12}{12+9} \implies x = \frac{9 \cdot 12}{21} = \frac{36}{7}$$
    Ова е убавината на олимписката геометрија!

2.  **Генерализација:** За секој триаголник каде аголот е $120^\circ$, должината на бисектрисата е хармониска средина на страните поделена со 2? Не, формулата е $l_a = \frac{bc}{b+c}$. Ова важи *само* кога аголот е $120^\circ$ (бидејќи $2\cos(60^\circ)=1$).

3.  **Чести Грешки:** Учениците често забораваат дека $\sin 120^\circ$ е позитивен. Исто така, грешат во алгебрата ако веднаш заменат $\frac{\sqrt{3}}{2}$ и почнат да множат децимално. Секогаш кратете прво!

### 🔗 Поврзани вештини
* **Примарна вештина:** Метода на плоштини (Area Method).
* **Потребни предзнаења:** Тригонометриски вредности за $60^\circ$ и $120^\circ$, Сличност на триаголници.

# Manim Code
```python
from manim import *
import numpy as np

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # --- Coordinates ---
        # A at origin (0,0)
        # C on x-axis at (6, 0) (scaled down by factor of 2 for visibility)
        # Real lengths: AB=9, AC=12. Let's scale by 0.5.
        # A = (0,0), C = (6, 0)
        # Angle BAC = 120. B is at (4.5 * cos(120), 4.5 * sin(120))
        # B = (-2.25, 3.897)
        
        scale = 0.6
        A = np.array([0, 0, 0])
        C = np.array([12 * scale, 0, 0])
        
        # B coordinates: Length 9, Angle 120 degrees
        B_x = 9 * scale * np.cos(120 * DEGREES)
        B_y = 9 * scale * np.sin(120 * DEGREES)
        B = np.array([B_x, B_y, 0])
        
        # Shift everything to center
        center_shift = (A + B + C) / 3
        A -= center_shift
        B -= center_shift
        C -= center_shift
        
        # Bisector D calculation
        # D divides BC in ratio c:b = 9:12 = 3:4
        # D = (4*B + 3*C) / 7
        D = (4 * B + 3 * C) / 7
        
        # --- Elements ---
        triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
        bisector = Line(A, D, color=RED, stroke_width=4)
        
        # Labels
        lbl_A = MathTex("A", color=BLACK).next_to(A, DOWN)
        lbl_B = MathTex("B", color=BLACK).next_to(B, UL)
        lbl_C = MathTex("C", color=BLACK).next_to(C, RIGHT)
        lbl_D = MathTex("D", color=BLACK).next_to(D, UP)
        
        lbl_c = MathTex("9", color=BLUE).next_to(Line(A, B).get_center(), LEFT)
        lbl_b = MathTex("12", color=BLUE).next_to(Line(A, C).get_center(), DOWN)
        lbl_x = MathTex("x", color=RED).next_to(Line(A, D).get_center(), RIGHT, buff=0.1)
        
        # Angles
        # Angle BAC is 120. Bisector splits into 60, 60.
        # We need to calculate start angles for Arc
        # Line AC angle is 0 (relative to A before rotation, but here A is rotated)
        # Let's use Angle class
        angle_bad = Angle(Line(A, B), Line(A, D), radius=0.5, color=GREEN)
        angle_dac = Angle(Line(A, D), Line(A, C), radius=0.6, color=GREEN) # slightly larger radius to not overlap
        
        lbl_60_1 = MathTex("60^\\circ", font_size=24, color=GREEN).move_to(
            Angle(Line(A, B), Line(A, D), radius=0.8).point_from_proportion(0.5)
        )
        lbl_60_2 = MathTex("60^\\circ", font_size=24, color=GREEN).move_to(
            Angle(Line(A, D), Line(A, C), radius=0.9).point_from_proportion(0.5)
        )
        
        # --- Animation ---
        self.play(Create(triangle), run_time=1.5)
        self.play(Write(lbl_A), Write(lbl_B), Write(lbl_C))
        self.play(Write(lbl_c), Write(lbl_b))
        
        self.play(Create(bisector))
        self.play(Write(lbl_D), Write(lbl_x))
        
        self.play(Create(angle_bad), Create(angle_dac))
        self.play(Write(lbl_60_1), Write(lbl_60_2))
        
        # Highlight Area Method
        # Fill triangles with different opacity
        tri_abd = Polygon(A, B, D, color=BLACK, fill_opacity=0.2, fill_color=BLUE)
        tri_adc = Polygon(A, D, C, color=BLACK, fill_opacity=0.2, fill_color=YELLOW)
        
        self.play(FadeIn(tri_abd))
        self.play(FadeIn(tri_adc))
        
        equation = MathTex("P_{ABC} = P_{ABD} + P_{ADC}", color=BLACK).to_edge(UP)
        self.play(Write(equation))
        
        self.wait(2)
```