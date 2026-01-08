---
problem_id: sigma_136_school_4
title: Агли во триаголник со продолжена страна
grade: 10
difficulty: 6
type: geometry
tags:
  - synthetic_geometry
  - circumcircle
  - special_triangles
  - trigonometry
primary_skill: synthetic_geometry
related_skills:
  - sine_theorem
  - angle_chasing
source: Сигма 136, Задачи од училницата (Втора година)
---

# Агли во триаголник со продолжена страна

# Текст на задачата
Во $\triangle ABC$, $\angle ABC = 45^\circ$ и $\angle CAB = 15^\circ$. Нека $M$ е точка на полуправата $BC$, таква што $\overline{BM} = 3 \cdot \overline{BC}$. Одреди ги аглите на $\triangle ABM$.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. **Синтетички пристап:** Спушти нормала од $M$ кон правата $AC$. Нека пресекот е $N$. Пресметај ги аглите во $\triangle MNC$.
   $$ \angle NCM = 180^\circ - 120^\circ = 60^\circ $$

2. **Клучен чекор:** Искористи го својството на правоаголен триаголник со агли $30^\circ-60^\circ-90^\circ$ за да воспоставиш врска помеѓу $CN$ и $CM$.
   $$ CN = \frac{1}{2} CM $$

3. **Поврзување:** Бидејќи $BM = 3BC$, изрази го $BC$ преку $CM$.
   $$ CM = 2BC \implies BC = \frac{1}{2} CM = CN $$
   Ова значи дека $\triangle BCN$ е рамнокрак!

4. **Финале:** Докажи дека $N$ е центар на опишаната кружница околу $\triangle ABM$ преку еднаквост на отсечките $NA=NB=NM$.

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Оваа задача е класичен пример каде "груба сила" (тригонометрија) работи, но **синтетичката геометрија** нуди решение со неверојатна елеганција.
Клучот е во "скриената" симетрија.
1.  Аголот $\angle C = 120^\circ$ е многу значаен. Неговиот суплемент е $60^\circ$. Ова веднаш сугерира да се повлече линија што ќе го искористи тој агол од $60^\circ$ за да формира "половина рамностран триаголник" ($30-60-90$).
2.  Условот $BM = 3BC$ е многу специфичен. Тоа значи $BC + CM = 3BC \implies CM = 2BC$. Односот $1:2$ е "заштитен знак" на триаголник со агли $30-60-90$.
3.  Ако успееме да поврземе дека $CN = BC$, тогаш добиваме рамнокрак триаголник $\triangle BCN$ кој ќе ни отвори пат кон центарот на опишана кружница.

Ова решение е супериорно бидејќи не бара калкулатор или паметење на $\tan 75^\circ$, туку само елементарна логика.

## 📐 Детално Решение (Синтетички Пристап)

<details>
<summary>Чекор 1: Конструкција и агли околу C</summary>

Нека $N$ е подножјето на нормалата спуштена од точката $M$ врз правата $AC$. Значи $\angle MNC = 90^\circ$.
Во $\triangle ABC$:
$$ \angle BCA = 180^\circ - (15^\circ + 45^\circ) = 120^\circ $$
Аглите $\angle BCA$ и $\angle NCM$ се напоредни (формираат рамен агол на правата $AC$), па:
$$ \angle NCM = 180^\circ - 120^\circ = 60^\circ $$

Во правоаголниот $\triangle MNC$:
$$ \angle NMC = 90^\circ - 60^\circ = 30^\circ $$
</details>

<details>
<summary>Чекор 2: Искористување на односот 30-60-90</summary>

Во правоаголен триаголник со агли $30^\circ-60^\circ-90^\circ$, катетата спроти аголот од $30^\circ$ е половина од хипотенузата.
Во $\triangle MNC$, страната $CN$ лежи спроти аголот од $30^\circ$ ($\angle NMC$).
$$ CN = \frac{1}{2} CM \quad \dots (1) $$

Дадено е $BM = 3 \cdot BC$. Бидејќи $M$ е на полуправата $BC$, точките се распоредени $B-C-M$.
$$ BM = BC + CM \implies 3BC = BC + CM \implies CM = 2BC $$
$$ BC = \frac{1}{2} CM \quad \dots (2) $$

Од (1) и (2) следи:
$$ CN = BC $$
</details>

<details>
<summary>Чекор 3: Рамнокрак триаголник BCN</summary>

Во $\triangle BCN$, имаме $CN = BC$, што значи триаголникот е рамнокрак.
Надворешниот агол кај темето $C$ е $\angle NCM = 60^\circ$.
Внатрешниот агол $\angle BCN = 120^\circ$.
Бидејќи е рамнокрак, аглите на основата се еднакви:
$$ \angle CBN = \angle CNB = \frac{180^\circ - 120^\circ}{2} = 30^\circ $$

Сега можеме да заклучиме нешто важно за $\triangle BMN$:
Аголот $\angle M = 30^\circ$ (од Чекор 1).
Аголот $\angle NBM = \angle CBN = 30^\circ$.
Значи $\triangle BMN$ е рамнокрак со основа $BM$.
$$ NB = NM \quad \dots (3) $$
</details>

<details>
<summary>Чекор 4: Центар на опишана кружница</summary>

Да го пресметаме аголот $\angle ABN$:
$$ \angle ABN = \angle ABC - \angle NBC = 45^\circ - 30^\circ = 15^\circ $$
Дадено е дека $\angle BAN = \angle BAC = 15^\circ$.
Значи, во $\triangle ABN$, имаме $\angle BAN = \angle ABN = 15^\circ$.
Следи дека $\triangle ABN$ е рамнокрак:
$$ NA = NB \quad \dots (4) $$

Од (3) и (4) добиваме клучно равенство:
$$ NA = NB = NM $$
Ова значи дека точката $N$ е **центар на опишаната кружница** околу $\triangle ABM$.
</details>

<details>
<summary>Чекор 5: Пресметка на аглите преку централен и периферен агол</summary>

Бидејќи $N$ е центар, аглите кај центарот се двојно поголеми од периферните агли над истиот лак.

1.  **Агол $\angle BAM$:**
    Централниот агол над тетивата $BM$ е $\angle BNM$.
    $\angle BNM = \angle BNC + \angle CNM = 30^\circ + 90^\circ = 120^\circ$.
    Периферниот агол е $\angle BAM = \frac{1}{2} \angle BNM = \frac{120^\circ}{2} = 60^\circ$.

2.  **Агол $\angle BMA$:**
    Централниот агол над тетивата $AB$ е $\angle ANB$.
    Во $\triangle ABN$, аглите се $15^\circ, 15^\circ$, па $\angle ANB = 180^\circ - 30^\circ = 150^\circ$.
    Периферниот агол е $\angle BMA = \frac{1}{2} \angle ANB = \frac{150^\circ}{2} = 75^\circ$.

3.  **Агол $\angle ABM$:**
    Веќе е даден како $45^\circ$. (Проверка: $60^\circ + 75^\circ + 45^\circ = 180^\circ$).
</details>

**Краен одговор:** Аглите на $\triangle ABM$ се $\boxed{45^\circ, 60^\circ, 75^\circ}$.

---

### 🧠 Алтернативен Пристап (Тригонометрија)
За оние кои претпочитаат аналитички метод, еве краток преглед на тригонометриското решение (како "план Б").

<details>
<summary>Тригонометриско Решение</summary>

1.  Во $\triangle ABC$, со Синусна теорема наоѓаме:
    $$ \frac{AB}{\sin 120^\circ} = \frac{BC}{\sin 15^\circ} \implies AB = BC \frac{\sin 60^\circ}{\sin 15^\circ} $$
2.  Во $\triangle ABM$, имаме $BM = 3BC$ и $\angle B = 45^\circ$.
    Со Синусна теорема за $\triangle ABM$:
    $$ \frac{AB}{\sin \angle M} = \frac{BM}{\sin(135^\circ - \angle M)} $$
3.  Заменуваме $AB$ и $BM$:
    $$ \frac{BC \sin 60^\circ}{\sin 15^\circ \sin \angle M} = \frac{3BC}{\sin(135^\circ - \angle M)} $$
4.  Се добива равенка за $\tan(\angle M)$. По средување (користејќи $\sin 15^\circ = \frac{\sqrt{6}-\sqrt{2}}{4}$), се добива:
    $$ \tan(\angle M) = 2 + \sqrt{3} $$
    Што одговара на $\angle M = 75^\circ$.
</details>

## 👨‍🏫 Менторски Белешки
1.  **Зошто Синтетичкото е подобро?** Забележете дека во синтетичкото решение не пресметавме ниту еден корен ($\sqrt{3}, \sqrt{2}$). Сè се базираше на својства на триаголници ($30-60-90$, рамнокрак). Ова ја намалува можноста за грешка во пресметки.
2.  **Препознавање на шаблони:** Кога ќе видите агол од $120^\circ$ и однос на страни $1:2$ (или $1:3$ што се сведува на $1:2$), веднаш барајте го "половина рамностран триаголник".
3.  **Центар на кружница:** Докажувањето дека $NA=NB=NM$ е многу моќна техника. Тоа веднаш ги дава сите агли преку врската централен-периферен агол.

### 🔗 Поврзани вештини
*   **Примарна вештина:** Синтетичка геометрија (Synthetic Geometry).
*   **Потребни предзнаења:** Својства на $30-60-90$ триаголник, Централен и периферен агол, Синусна теорема.

# Manim Code
```python
from manim import *

class SyntheticGeometry(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # --- Setup Coordinates ---
        # Let N be the origin (0,0) for easier calculation of circle
        # N is circumcenter. Radius R.
        # Angles at center:
        # ANB = 150 deg
        # BNM = 120 deg
        # MNA = 360 - 270 = 90 deg? Let's check.
        # Angle M = 75. Central angle AOB? No.
        # Angle BAM = 60 => BNM = 120. Correct.
        # Angle BMA = 75 => BNA = 150. Correct.
        # Angle ABM = 45 => ANM = 90. Correct.
        
        R = 2.5
        N = np.array([0, 0, 0])
        
        # Positions based on angles
        # Let M be at 0 deg
        M = np.array([R, 0, 0])
        
        # B is -120 deg from M (clockwise or counter?)
        # Triangle BMN is isosceles (30-30-120).
        # So angle MNB = 120.
        B = np.array([R * np.cos(120*DEGREES), R * np.sin(120*DEGREES), 0])
        
        # A is 150 deg from B
        # 120 + 150 = 270 deg
        A = np.array([R * np.cos(270*DEGREES), R * np.sin(270*DEGREES), 0])
        
        # C is on BM such that N-C is perp to A-C? No.
        # N is perp foot from M to AC.
        # So angle MNC = 90.
        # Line AC is vertical line passing through N? No.
        # Line NM is horizontal. Line AC is vertical x=0?
        # Let's check. N is origin. M is (R, 0).
        # Line AC must be perpendicular to NM at N? No, N is foot from M to AC.
        # So AC is perpendicular to NM. Since NM is horizontal, AC is vertical.
        # Does A lie on the vertical line x=0?
        # A is at (0, -R). Yes! A lies on y-axis.
        # So AC is the y-axis.
        # C is intersection of BM and y-axis.
        
        # Line BM equation:
        # M=(R,0), B=(-R/2, R*sqrt(3)/2)
        # Slope = (R*sqrt(3)/2 - 0) / (-R/2 - R) = (sqrt(3)/2) / (-3/2) = -sqrt(3)/3
        # y - 0 = -1/sqrt(3) * (x - R)
        # x = 0 => y = R/sqrt(3)
        C = np.array([0, R/np.sqrt(3), 0])
        
        # --- Drawing ---
        
        # Circumcircle
        circle = Circle(radius=R, color=LIGHT_GREY)
        
        # Triangle ABM
        tri_ABM = Polygon(A, B, M, color=BLACK, stroke_width=2)
        
        # Auxiliary lines
        line_AC = Line(A, C, color=BLUE) # Extended to C
        line_NM = Line(N, M, color=RED, stroke_width=2) # Radius
        line_NB = Line(N, B, color=RED, stroke_width=2) # Radius
        line_NA = Line(N, A, color=RED, stroke_width=2) # Radius
        line_NC = Line(N, C, color=BLUE)
        
        # Labels
        label_N = MathTex("N", color=RED).next_to(N, DL, buff=0.1)
        label_A = MathTex("A", color=BLACK).next_to(A, DOWN)
        label_B = MathTex("B", color=BLACK).next_to(B, UL)
        label_M = MathTex("M", color=BLACK).next_to(M, RIGHT)
        label_C = MathTex("C", color=BLACK).next_to(C, UP)
        
        # Right angle at N (MNC)
        right_angle = Square(side_length=0.2, color=BLUE).move_to(N).align_to(N, DL)
        # Actually N is origin, M is right, C is up. So square in quadrant 1.
        right_angle = RightAngle(Line(N,M), Line(N,C), length=0.3, quadrant=1)

        # Animation
        self.play(Create(circle), FadeIn(label_N))
        self.play(Create(tri_ABM), Write(label_A), Write(label_B), Write(label_M))
        self.wait(1)
        
        # Construction
        self.play(Create(line_NM), Create(line_NB), Create(line_NA))
        self.play(Create(line_NC), Write(label_C), Create(right_angle))
        
        # Highlight Isosceles BCN
        self.play(Indicate(Polygon(B, C, N, color=ORANGE), color=ORANGE))
        
        # Final Angles Text
        angles_text = VGroup(
            MathTex("\\angle BAM = 60^\\circ", color=BLUE),
            MathTex("\\angle BMA = 75^\\circ", color=BLUE)
        ).arrange(DOWN).to_corner(UL)
        
        self.play(Write(angles_text))
        self.wait(2)
```