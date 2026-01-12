---
problem_id: geometry_solid_pyramid_1882
title: "Правилна тристрана пирамида: Плоштина и Волумен"
grade: 10
difficulty: 5
type: geometry
tags:
  - solid_geometry
  - pyramid
  - stereometry
  - volume
  - surface_area
primary_skill: stereometric_relations
related_skills:
  - trigonometric_ratios
  - algebraic_equations
source: Zbirka_Geom_1882
---

# Правилна тристрана пирамида: Плоштина и Волумен

# Текст на задачата
Основниот раб на правилна тристрана пирамида е со должина $x$, а бочниот ѕид зафаќа со рамнината на основата агол од $60^\circ$. Определи го $x$ ако плоштината на пирамидата е бројно еднаква со волуменот на пирамидата.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Нацртај го „карактеристичниот триаголник“ на пирамидата. Тоа е правоаголен триаголник формиран од висината на пирамидата ($H$), апотемата (висината на бочниот ѕид $h$) и радиусот на впишаната кружница во основата ($r$).

$$r = \frac{x\sqrt{3}}{6}$$

2. Искористи го дадениот агол од $60^\circ$ во овој правоаголен триаголник за да ги изразиш $H$ и $h$ преку $r$ (а со тоа и преку $x$).

$$\tan 60^\circ = \frac{H}{r}, \quad \cos 60^\circ = \frac{r}{h}$$

3. Запиши ги формулите за плоштина ($P = B + M$) и волумен ($V = \frac{B \cdot H}{3}$) и изедначи ги. Внимавај, $B$ е плоштина на рамностран триаголник.

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Ова е класична стереометриска задача која ги поврзува димензиите на пирамидата со нејзините својства (плоштина и волумен).

Клучот за решавање на секоја правилна пирамида лежи во **пресекот** кој ја содржи висината на пирамидата и висината на бочниот ѕид.
Замислете дека ја сечете пирамидата вертикално низ врвот и низ средината на една од основните страни.
Добиваме правоаголен триаголник $OMV$ каде:
*   $O$ е центарот на основата (тежиштето).
*   $M$ е средината на основниот раб.
*   $V$ е врвот на пирамидата.

Во овој триаголник:
*   Катетата $OM$ е радиусот на впишаната кружница во основата ($r$).
*   Катетата $OV$ е висината на пирамидата ($H$).
*   Хипотенузата $MV$ е висината на бочниот ѕид (апотема, $h$).
*   Аголот $\angle VMO$ е дадениот агол од $60^\circ$.

Нашата стратегија е:
1.  Да ги изразиме сите величини ($r, H, h, B, M$) преку непознатата $x$.
2.  Да ја составиме равенката $P=V$.
3.  Да го најдеме $x$.

*Забелешка:* Физички е невозможно плоштина (мерка во $m^2$) да биде еднаква на волумен (мерка во $m^3$), но математички го решаваме ова како равенка на бројните вредности.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Геометрија на основата</summary>

Основата е рамностран триаголник со страна $x$.
Плоштината на основата е:

$$B = \frac{x^2\sqrt{3}}{4}$$

Радиусот на впишаната кружница во рамностран триаголник е една третина од висината на триаголникот ($h_a = \frac{x\sqrt{3}}{2}$):

$$r = \frac{1}{3} h_a = \frac{1}{3} \cdot \frac{x\sqrt{3}}{2} = \frac{x\sqrt{3}}{6}$$

</details>

<details>
<summary>Чекор 2: Односи во карактеристичниот триаголник</summary>

Го разгледуваме правоаголниот триаголник $OMV$ со агол $\angle M = 60^\circ$.
Од дефиницијата за тригонометриски функции:

1.  За висината на пирамидата ($H$):
    $$\tan 60^\circ = \frac{H}{r} \implies H = r \cdot \sqrt{3}$$
    Заменуваме за $r$:
    $$H = \frac{x\sqrt{3}}{6} \cdot \sqrt{3} = \frac{3x}{6} = \frac{x}{2}$$

2.  За апотемата ($h$):
    $$\cos 60^\circ = \frac{r}{h} \implies h = \frac{r}{\cos 60^\circ} = \frac{r}{1/2} = 2r$$
    Заменуваме за $r$:
    $$h = 2 \cdot \frac{x\sqrt{3}}{6} = \frac{x\sqrt{3}}{3}$$

</details>

<details>
<summary>Чекор 3: Изразување на Плоштината и Волуменот</summary>

**Плоштина на пирамидата ($P$):**
Бочната плоштина ($M_{bochna}$) се состои од три еднакви триаголници со основа $x$ и висина $h$:
$$M_{bochna} = 3 \cdot \frac{x \cdot h}{2} = \frac{3}{2} x \left( \frac{x\sqrt{3}}{3} \right) = \frac{x^2\sqrt{3}}{2}$$

Вкупната плоштина е:
$$P = B + M_{bochna} = \frac{x^2\sqrt{3}}{4} + \frac{x^2\sqrt{3}}{2}$$
Сведуваме на заеднички именител:
$$P = \frac{x^2\sqrt{3}}{4} + \frac{2x^2\sqrt{3}}{4} = \frac{3x^2\sqrt{3}}{4}$$

**Волумен на пирамидата ($V$):**
$$V = \frac{B \cdot H}{3} = \frac{1}{3} \cdot \left( \frac{x^2\sqrt{3}}{4} \right) \cdot \left( \frac{x}{2} \right)$$
$$V = \frac{x^3\sqrt{3}}{24}$$

</details>

<details>
<summary>Чекор 4: Решавање на равенката</summary>

Според условот на задачата $P = V$ (бројно):

$$\frac{3x^2\sqrt{3}}{4} = \frac{x^3\sqrt{3}}{24}$$

Можеме да скратиме со $\sqrt{3}$ и со $x^2$ (бидејќи $x \neq 0$):

$$\frac{3}{4} = \frac{x}{24}$$

Множиме со 24:

$$x = \frac{3 \cdot 24}{4} = 3 \cdot 6 = 18$$

</details>

**Краен одговор:** Должината на основниот раб е $\boxed{x = 18}$.

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Во стереометрија, секогаш обидете се да го сведете 3D проблемот на 2D проблем преку наоѓање на соодветен пресек (триаголник). Во овој случај, триаголникот $OMV$ ги содржи сите клучни информации.
2.  **Чести Грешки:** Учениците често мешаат *висина на пирамидата* ($H$) со *висина на бочниот ѕид* ($h$). Висината на пирамидата паѓа во центарот на основата, додека висината на бочниот ѕид (апотема) паѓа на работ на основата.
3.  **Проверка:** Ако $x=18$, тогаш $H=9$. $B = \frac{324\sqrt{3}}{4} = 81\sqrt{3}$. $V = \frac{81\sqrt{3} \cdot 9}{3} = 243\sqrt{3}$.
    $P = \frac{3 \cdot 324 \sqrt{3}}{4} = 243\sqrt{3}$. Резултатот е точен.

### 🔗 Поврзани вештини
* **Примарна вештина:** Стереометриски односи (Stereometric Relations).
* **Потребни предзнаења:** Питагорова теорема, Тригонометрија на остар агол, Формули за рамностран триаголник.

# Manim Code
```python
from manim import *
import numpy as np

class SolutionScene(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # --- Parameters ---
        # Let x = 4 for visualization scale
        x_val = 4
        h_base = x_val * np.sqrt(3) / 2
        r_val = h_base / 3  # Inradius
        R_val = 2 * h_base / 3 # Circumradius
        
        # Height calculation based on 60 degrees
        # tan(60) = H / r => H = r * sqrt(3)
        H_val = r_val * np.sqrt(3)
        
        # --- Points ---
        # Base in XY plane. Center at Origin.
        # A, B, C vertices of equilateral triangle
        # A at (0, R, 0) ? No, let's align properly.
        # Angles: 90, 210, 330 degrees
        
        A = np.array([R_val * np.cos(np.radians(90)), R_val * np.sin(np.radians(90)), 0])
        B = np.array([R_val * np.cos(np.radians(210)), R_val * np.sin(np.radians(210)), 0])
        C = np.array([R_val * np.cos(np.radians(330)), R_val * np.sin(np.radians(330)), 0])
        
        # Apex V
        V = np.array([0, 0, H_val])
        
        # Center O
        O = np.array([0, 0, 0])
        
        # Midpoint M of BC
        M = (B + C) / 2
        
        # --- Elements ---
        # Base Triangle
        base_tri = Polygon(A, B, C, color=BLUE, fill_opacity=0.1, stroke_width=2)
        
        # Pyramid Edges
        edge_VA = Line(V, A, color=BLACK, stroke_width=2)
        edge_VB = Line(V, B, color=BLACK, stroke_width=2)
        edge_VC = Line(V, C, color=BLACK, stroke_width=2)
        
        # Internal Lines (The Characteristic Triangle OMV)
        line_OM = Line(O, M, color=RED, stroke_width=3) # r
        line_OV = Line(O, V, color=RED, stroke_width=3) # H
        line_VM = Line(V, M, color=RED, stroke_width=3) # h
        
        # Labels (Using MathTex, need to orient them to camera or just place in 3D)
        # Note: In ThreeDScene, fixed_in_frame_mobjects are better for text, 
        # but here we want them attached to geometry.
        
        # We will rotate labels to face camera roughly
        lbl_x = MathTex("x", color=BLACK).move_to((A+B)/2 + LEFT*0.2)
        lbl_H = MathTex("H", color=RED).next_to(line_OV, LEFT, buff=0.1).rotate(PI/2, axis=RIGHT)
        lbl_h = MathTex("h", color=RED).next_to(line_VM, RIGHT, buff=0.1).rotate(PI/2, axis=RIGHT)
        lbl_r = MathTex("r", color=RED).next_to(line_OM, DOWN, buff=0.1)
        
        # Angle Arc
        # Angle at M is not 60, angle at M in triangle OMV is 60.
        # Wait, problem says "lateral face makes 60 deg with base".
        # This is the angle between plane VBC and plane ABC.
        # This is exactly angle VMO.
        
        # --- Animation Sequence ---
        
        # 1. Draw Base
        self.add(base_tri)
        self.wait(0.5)
        
        # 2. Draw Apex and Edges
        self.play(Create(edge_VA), Create(edge_VB), Create(edge_VC))
        self.wait(0.5)
        
        # 3. Highlight Characteristic Triangle
        self.play(Create(line_OM), Create(line_OV), Create(line_VM))
        
        # 4. Add Labels (Static for the final frame)
        # For 3D text, we often just add them.
        self.add_fixed_in_frame_mobjects(MathTex("60^\\circ", color=RED).move_to(UP*0.5 + RIGHT*2))
        # Actually, let's just place 3D mobjects
        
        # Adjusting labels for 3D view
        lbl_H.rotate(PI/2, axis=UP) 
        
        self.add(lbl_H, lbl_h, lbl_r)
        
        # Indicate the angle
        # Create a small arc at M in the plane OMV
        # Vector MO is (-M)
        # Vector MV is (V-M)
        # This is hard to draw perfectly in 3D generic, but we can approximate with a line
        
        angle_text = MathTex("60^\\circ", color=RED).move_to(M + UP*0.3 + LEFT*0.3).scale(0.7)
        angle_text.rotate(PI/2, axis=RIGHT)
        self.add(angle_text)
        
        # Rotate camera to show the "profile" view
        self.move_camera(phi=80 * DEGREES, theta=0 * DEGREES, run_time=2)
        
        self.wait(2)
```