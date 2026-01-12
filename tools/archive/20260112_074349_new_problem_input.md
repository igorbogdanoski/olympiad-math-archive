---
problem_id: regional_2025_1_4a
title: Симетрали на агли и дијаметар на опишана кружница
grade: 9
difficulty: 6
type: geometry
tags:
  - tektivna_geometrija
  - simetrala_na_agol
  - pitagorina_teorema
primary_skill: kruznici_i_teptivni_cetiriagolnici
related_skills:
  - talesova_teorema
  - Talesova_teorema
  - agol_pomegu_simetrali
source: Регионален натпревар по математика за средно образование 2025 (Сигма 139)
---

# Симетрали на агли и дијаметар на опишана кружница

# Текст на задачата
Даден е триаголник $ABC$. Нека точките $L$ и $M$ се пресеци на симетралите на внатрешниот и надворешниот агол при темето $C$ со правата $AB$, соодветно. Ако важи $CL = CM$, докажи дека:

$$AC^2 + BC^2 = 4R^2$$

каде $R$ е радиусот на опишаната кружница на $\triangle ABC$.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Размислете за аголот помеѓу внатрешната и надворешната симетрала на ист агол. Колку изнесува $\angle LCM$?

$$\angle LCM = 90^\circ$$

2. Користете го условот $CL = CM$ за да ги одредите аглите на $\triangle CML$. Што заклучувате за $\angle CLM$?

3. Изразете ги аглите $\alpha$ и $\beta$ преку $\gamma$. Дали може да докажете дека $\beta - \alpha = 90^\circ$?

4. Конструирајте точка $D$ на кружницата таква што $BC = CD$. Што ќе биде отсечката $AD$?

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Оваа задача на прв поглед изгледа како да бара пресметки со должини, но нејзината суштина е во **аголната конфигурација**. 

**Тригерот:** Штом се споменати внатрешна и надворешна симетрала на ист агол, веднаш знаеме дека тие се под агол од $90^\circ$. Зошто? Затоа што тие ги половат двата агли кои заедно чинат $180^\circ$. Дополнителниот услов $CL = CM$ го претвора $\triangle CML$ во рамнокрак правоаголен триаголник. Ова е исклучително силен услов кој ги „заклучува“ аглите на почетниот триаголник $\triangle ABC$.

**Стратегија:** Целта е да стигнеме до изразот $4R^2$, што е всушност $(2R)^2$. Ова не асоцира на Питагорова теорема во триаголник каде хипотенузата е дијаметар на кружницата. Значи, нашата задача е да најдеме или конструираме правоаголен триаголник чија хипотенуза е дијаметарот $2R$, а катетите се еднакви на $AC$ и $BC$. Клучот лежи во докажувањето дека $\beta - \alpha = 90^\circ$.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Анализа на аглите околу темето C (формула за \(\angle LCM\))</summary>

Нека $\alpha, \beta, \gamma$ се внатрешните агли на $\triangle ABC$. Симетралите на внатрешниот и надворешниот агол при темето $C$ се заемно нормални бидејќи:

$$
\angle LCM = \frac{\gamma}{2} + \frac{180^\circ - \gamma}{2} = 90^\circ
$$

Бидејќи е дадено дека $CL = CM$, триаголникот $\triangle CML$ е рамнокрак правоаголен триаголник. Оттука следува:

$$
\angle CLM = \angle CML = 45^\circ
$$

Аголот $\angle CLM$ е надворешен за триаголникот $\triangle BLC$ (ако $B$ е помеѓу $A$ и $L$) или дел од него. Поточно, во $\triangle ALC$ имаме:

$$
\angle ALC = 180^\circ - \angle CLM = 135^\circ
$$

Збирот на аглите во $\triangle ALC$ е:

$$
\alpha + \frac{\gamma}{2} + 135^\circ = 180^\circ \implies \alpha + \frac{\gamma}{2} = 45^\circ
$$

</details>

<details>
<summary>Чекор 2: Врска помеѓу аглите алфа и бета (формула за \(\beta - \alpha\))</summary>

Од претходниот чекор имаме $\frac{\gamma}{2} = 45^\circ - \alpha$. Знаеме дека $\gamma = 180^\circ - (\alpha + \beta)$, па:

$$
\frac{180^\circ - \alpha - \beta}{2} = 45^\circ - \alpha
$$
$$
90^\circ - \frac{\alpha}{2} - \frac{\beta}{2} = 45^\circ - \alpha
$$
$$
45^\circ + \frac{\alpha}{2} = \frac{\beta}{2} \implies \beta - \alpha = 90^\circ
$$

Ова е клучниот резултат. Триаголникот $ABC$ е таков што разликата на аглите кај основата е прав агол.

</details>

<details>
<summary>Чекор 3: Геометриска конструкција и Питагорова теорема (прав агол и дијаметар)</summary>

Нека $k$ е опишаната кружница околу $\triangle ABC$ со радиус $R$. Конструираме точка $D$ на кружницата $k$ таква што тетивите $BC$ и $CD$ се еднакви ($BC = CD$). 

- Аглите над еднакви тетиви се еднакви: $\angle CAD = \angle BAC = \alpha$? Не, аголот над тетивата $CD$ е $\angle CAD$, а над $BC$ е $\angle BAC = \alpha$. Значи $\angle CAD = \alpha$.
- Четириаголникот $ABCD$ е тетивен. Тогаш $\angle ADC = 180^\circ - \beta$ (спротивни агли).
- Во триаголникот $ACD$, збирот на аглите е $180^\circ$:

$$
\angle ACD = 180^\circ - (\angle CAD + \angle ADC) = 180^\circ - (\alpha + 180^\circ - \beta) = \beta - \alpha
$$

Бидејќи докажавме дека $\beta - \alpha = 90^\circ$, следува дека $\angle ACD = 90^\circ$. 
Според Талесовата теорема, ако аголот над тетивата $AD$ е прав, тогаш $AD$ мора да биде дијаметар на кружницата, т.е. $AD = 2R$.

</details>

<details>
<summary>Чекор 4: Финализација (Питагорова теорема и крајна формула)</summary>

Применуваме Питагорова теорема на правоаголниот $\triangle ACD$:

$$
AC^2 + CD^2 = AD^2
$$

Бидејќи $CD = BC$ и $AD = 2R$, со замена добиваме:

$$
AC^2 + BC^2 = (2R)^2 = 4R^2
$$

Со што тврдењето е докажано.

</details>

**Краен одговор:** Тврдењето $AC^2 + BC^2 = 4R^2$ е докажано преку својствата на симетралите и конструкција на дијаметар во опишаната кружница. $\boxed{Q.E.D.}$

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Кога во задача е даден радиус на опишана кружница ($R$) и квадрати на страни, секогаш барајте правоаголен триаголник чија хипотенуза е дијаметарот. Ова е најчестиот начин како $R$ се поврзува со страните во олимписката геометрија.
2.  **Чести Грешки:** Внимавајте на распоредот на точките $A, B, L, M$ на правата. Иако сликата помага, доказот преку агли е поопшт и не зависи од тоа дали $\beta$ е тап или остар агол (иако овде $\beta = 90^\circ + \alpha$ јасно ни кажува дека $\beta$ е тап).
3.  **Зошто ова е важно:** Оваа задача ја комбинира теоријата на симетрали со својствата на тетивните четириаголници, што е темел за потешки задачи на BMO и IMO.

### 🔗 Поврзани вештини
* **Примарна вештина:** Тетивна геометрија (Macedonian: Тетивна геометрија).
* **Потребни предзнаења:** Својства на симетрали, Талесова теорема, Питагорова теорема.

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Coordinates for circumcircle R=3
        R = 3
        circle = Circle(radius=R, color=BLACK, stroke_width=4)
        
        # Vertices based on beta - alpha = 90
        # Let alpha = 20, then beta = 110. gamma = 50.
        A = np.array([-3, 0, 0])
        C = np.array([R*np.cos(np.radians(70)), R*np.sin(np.radians(70)), 0])
        # To make CD = BC, D is reflection of B or calculated
        D = np.array([R*np.cos(np.radians(-110)), R*np.sin(np.radians(-110)), 0])
        B = np.array([R*np.cos(np.radians(-40)), R*np.sin(np.radians(-40)), 0])

        # Triangle ABC
        tri_abc = Polygon(A, B, C, color=BLACK, stroke_width=4)
        
        # Point D and lines for the proof
        line_ad = Line(A, D, color=RED, stroke_width=4)
        line_cd = Line(C, D, color=BLUE, stroke_width=4)
        
        # Dots
        dot_a = Dot(A, color=BLACK)
        dot_b = Dot(B, color=BLACK)
        dot_c = Dot(C, color=BLACK)
        dot_d = Dot(D, color=BLACK)
        
        # Labels
        lbl_a = MathTex("A", color=BLACK).next_to(A, LEFT)
        lbl_b = MathTex("B", color=BLACK).next_to(B, RIGHT)
        lbl_c = MathTex("C", color=BLACK).next_to(C, UP)
        lbl_d = MathTex("D", color=BLACK).next_to(D, DOWN)
        lbl_r = MathTex("2R", color=RED).next_to(line_ad.get_center(), UP+LEFT, buff=0.1)


        # Right angle symbol at C for triangle ACD
        right_angle = RightAngle(Line(C, A), Line(C, D), length=0.3, color=GRAY)

        self.add(circle, tri_abc, line_ad, line_cd, right_angle)
        self.add(dot_a, dot_b, dot_c, dot_d, lbl_a, lbl_b, lbl_c, lbl_d, lbl_r)
```