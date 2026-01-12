---
problem_id: sigma_138_1886
title: Плоштина на правоаголен триаголник преку хипотенузата
grade: 9
difficulty: 5
type: geometry
tags:
  - right_triangle
  - incircle
  - area_formula
  - tangent_segments
primary_skill: tangent_properties
related_skills:
  - algebraic_manipulation
  - area_calculation
source: Sigma 138, Problem 1886
---

# Плоштина на правоаголен триаголник преку хипотенузата

# Текст на задачата
Впишаната кружница во правоаголен триаголник со допирната точка ја дели хипотенузата на две отсечки со должини $p$ и $q$. Пресметај ја плоштината на триаголникот.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Означи ги темињата на триаголникот со $A, B, C$ (каде $C$ е правиот агол) и допирните точки на впишаната кружница со страните. Искористи го својството на тангентни отсечки: тангентните отсечки повлечени од иста точка до кружница се еднакви.

$$AR = AP = p, \quad BQ = BP = q$$

2. Што се случува кај темето на правиот агол $C$? Ако $r$ е радиусот на впишаната кружница, каков четириаголник формираат темето $C$, центарот $O$ и допирните точки на катетите?

$$CR = CQ = r$$

3. Изрази ја плоштината на триаголникот на два начини:
   а) Преку полупериметарот и радиусот: $P = s \cdot r$
   б) Преку катетите: $P = \frac{1}{2} a \cdot b$
   Израмни ги овие два изрази.

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Ова е една од оние „бисери“ во геометријата каде резултатот е изненадувачки едноставен и елегантен.
Кога имаме впишана кружница во правоаголен триаголник, клучната работа е да се забележи што се случува во аглите.
1.  Кај острите агли ($A$ и $B$), кружницата „отсекува“ еднакви должини на страните (својство на тангентни отсечки). Значи, ако хипотенузата е поделена на $p$ и $q$, тие должини се „пресликуваат“ и на катетите.
2.  Кај правиот агол ($C$), радиусите кон допирните точки се нормални на катетите. Бидејќи и аголот на триаголникот е $90^\circ$, се формира **квадрат** со страна $r$ (радиусот на впишаната кружница).

Значи, катетите се всушност $a = q + r$ и $b = p + r$.
Нашата цел е да најдеме плоштина. Имаме две формули за плоштина. Едната вклучува само множење на катетите, а другата периметар и радиус. Ако ги комбинираме, можеби $r$ ќе се поништи и ќе остане само врската меѓу $p$ и $q$.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Означување и својства на тангентни отсечки</summary>

Нека $ABC$ е правоаголен триаголник со прав агол во темето $C$. Нека $O$ е центарот на впишаната кружница со радиус $r$.
Нека допирните точки на кружницата со страните $AB$ (хипотенуза), $BC$ и $AC$ се $P, Q$ и $R$ соодветно.

Според условот на задачата, точката $P$ ја дели хипотенузата на отсечки:
$$AP = p \quad \text{и} \quad BP = q$$

Според својството на тангентни отсечки повлечени од иста точка:
1.  Од темето $A$: $AR = AP = p$
2.  Од темето $B$: $BQ = BP = q$
3.  Од темето $C$: $CR = CQ = r$ (бидејќи $C R O Q$ е квадрат со страна $r$).

</details>

<details>
<summary>Чекор 2: Изразување на страните и плоштината преку $r$</summary>

Сега можеме да ги изразиме должините на катетите:
$$a = \overline{BC} = BQ + QC = q + r$$
$$b = \overline{AC} = AR + RC = p + r$$

Плоштината на триаголникот $P_{ABC}$ може да се пресмета преку полупериметарот $s$ и радиусот $r$:
$$s = \frac{a+b+c}{2} = \frac{(q+r) + (p+r) + (p+q)}{2} = \frac{2p + 2q + 2r}{2} = p + q + r$$

Значи, плоштината е:
$$P_{ABC} = s \cdot r = (p + q + r) \cdot r = pr + qr + r^2$$

</details>

<details>
<summary>Чекор 3: Изразување на плоштината преку катетите</summary>

Од друга страна, плоштината на правоаголен триаголник е половина од производот на катетите:
$$P_{ABC} = \frac{1}{2} a \cdot b = \frac{1}{2} (q + r)(p + r)$$

Го развиваме овој израз:
$$P_{ABC} = \frac{1}{2} (pq + pr + qr + r^2)$$

</details>

<details>
<summary>Чекор 4: Изедначување и финален резултат</summary>

Ги изедначуваме двата изрази за плоштината што ги добивме во Чекор 2 и Чекор 3:

$$pr + qr + r^2 = \frac{1}{2} (pq + pr + qr + r^2)$$

За да се ослободиме од дропката, множиме со 2:

$$2(pr + qr + r^2) = pq + (pr + qr + r^2)$$

Нека целиот израз $(pr + qr + r^2)$ го означиме со $X$. Тогаш равенката е $2X = pq + X$.
Одземаме $X$ (односно $pr + qr + r^2$) од двете страни:

$$pr + qr + r^2 = pq$$

Но, забележуваме дека левата страна ($pr + qr + r^2$) е точно изразот за плоштината што го добивме во Чекор 2 ($P_{ABC} = s \cdot r$).

Значи:
$$P_{ABC} = pq$$

</details>

**Краен одговор:** Плоштината на триаголникот е $\boxed{pq}$.

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Оваа формула $P = pq$ важи **само** за правоаголен триаголник. Тоа е исклучително моќна алатка за натпревари. Ако видите задача каде се дадени отсечките на хипотенузата, веднаш знаете дека нивниот производ е плоштината. Не губете време на Питагорова теорема.
2.  **Геометриска интерпретација:** Ако ги нацртате правоаголниците со страни $p$ и $r$, и $q$ и $r$, и квадратот $r^2$, ќе видите дека тие ја сочинуваат плоштината. Но, уште поинтересно е што производот на проекциите на хипотенузата е директно поврзан со плоштината.
3.  **Чести Грешки:** Учениците често забораваат дека $CR=r$ и се обидуваат да воведат нова променлива, што ја комплицира задачата. Клучно е да се искористи квадратот кај правиот агол.

### 🔗 Поврзани вештини
* **Примарна вештина:** Својства на тангентни отсечки (Tangent Properties).
* **Потребни предзнаења:** Формули за плоштина на триаголник ($P=sr$, $P=\frac{1}{2}ab$).

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # --- Configuration ---
        # Let r = 1.5, p = 2.5, q = 4 (arbitrary values satisfying geometry)
        r_val = 1.5
        p_val = 2.5
        q_val = 4.0
        
        # Coordinates
        # C is at origin (0,0)
        C = np.array([0, 0, 0])
        # A is on y-axis: b = p + r
        A = np.array([0, p_val + r_val, 0])
        # B is on x-axis: a = q + r
        B = np.array([q_val + r_val, 0, 0])
        
        # Incenter O is at (r, r)
        O = np.array([r_val, r_val, 0])
        
        # Tangent points
        R_pt = np.array([0, r_val, 0]) # On AC
        Q_pt = np.array([r_val, 0, 0]) # On BC
        
        # Tangent point P on AB needs calculation
        # Line AB equation: y - 0 = m(x - (q+r)) where m = -(p+r)/(q+r)
        # Or simply, P divides AB in ratio q:p from B? No, BP=q, AP=p.
        # Vector BA = A - B. P = B + (q/(p+q)) * BA
        vec_BA = A - B
        P_pt = B + (q_val / (p_val + q_val)) * vec_BA
        
        # Shift everything to center
        center_shift = (A + B + C) / 3
        A -= center_shift
        B -= center_shift
        C -= center_shift
        O -= center_shift
        R_pt -= center_shift
        Q_pt -= center_shift
        P_pt -= center_shift
        
        # --- Elements ---
        triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
        incircle = Circle(radius=r_val, color=BLUE).move_to(O)
        
        # Points
        dot_O = Dot(O, color=BLUE)
        dot_P = Dot(P_pt, color=RED)
        dot_Q = Dot(Q_pt, color=RED)
        dot_R = Dot(R_pt, color=RED)
        
        # Labels
        lbl_A = MathTex("A", color=BLACK).next_to(A, UP)
        lbl_B = MathTex("B", color=BLACK).next_to(B, RIGHT)
        lbl_C = MathTex("C", color=BLACK).next_to(C, DL)
        lbl_p = MathTex("p", color=RED).move_to((A + P_pt)/2 + RIGHT*0.3)
        lbl_q = MathTex("q", color=RED).move_to((B + P_pt)/2 + UP*0.3)
        
        # Radius lines to show the square
        line_OR = Line(O, R_pt, color=BLUE, stroke_width=2)
        line_OQ = Line(O, Q_pt, color=BLUE, stroke_width=2)
        
        lbl_r1 = MathTex("r", color=BLUE).next_to(line_OR, RIGHT, buff=0.1).scale(0.7)
        lbl_r2 = MathTex("r", color=BLUE).next_to(line_OQ, UP, buff=0.1).scale(0.7)
        
        # Braces for legs
        brace_b = Brace(Line(C, A), LEFT, color=GRAY)
        brace_a = Brace(Line(C, B), DOWN, color=GRAY)
        
        txt_b = brace_b.get_text("$b = p+r$", buff=0.1).set_color(BLACK).scale(0.8)
        txt_a = brace_a.get_text("$a = q+r$", buff=0.1).set_color(BLACK).scale(0.8)
        
        # --- Animation ---
        self.play(Create(triangle), run_time=1.5)
        self.play(Write(lbl_A), Write(lbl_B), Write(lbl_C))
        
        self.play(Create(incircle), FadeIn(dot_O))
        self.play(FadeIn(dot_P), FadeIn(dot_Q), FadeIn(dot_R))
        
        # Highlight segments on hypotenuse
        self.play(Indicate(Line(A, P_pt), color=RED), Write(lbl_p))
        self.play(Indicate(Line(B, P_pt), color=RED), Write(lbl_q))
        
        # Show the square property
        self.play(Create(line_OR), Create(line_OQ))
        self.play(Write(lbl_r1), Write(lbl_r2))
        
        # Show full sides
        self.play(Create(brace_b), Write(txt_b))
        self.play(Create(brace_a), Write(txt_a))
        
        # Final Formula
        formula = MathTex("P = p \cdot q", color=RED).scale(1.5).to_corner(UR)
        box = SurroundingRectangle(formula, color=RED)
        
        self.play(Write(formula))
        self.play(Create(box))
        
        self.wait(2)
```