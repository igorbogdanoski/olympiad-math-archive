---
problem_id: regional_2025_1_4b
title: Заедничка хипотенуза и плоштина на триаголници
grade: 9
difficulty: 6
type: geometry
tags:
  - pitagorina_teorema
  - slicnost_na_triagolnici
  - plostina
primary_skill: slicnost_na_triagolnici
related_skills:
  - talesova_teorema
  - algebarski_sistemi
source: Регионален натпревар по математика за средно образование 2025 (Сигма 139)
---

# Заедничка хипотенуза и плоштина на триаголници

# Текст на задачата
Дадени се два правоаголни триаголници, $\triangle PST$ и $\triangle RST$ со заедничка хипотенуза $ST$. Катетите $PT$ и $RS$ се сечат во точката $Q$. Ако $PS = 6$, $PT = 17$ и $RT = 1$, пресметај ја плоштината на $\triangle SQT$.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Прво пресметајте ја должината на заедничката хипотенуза $ST$, а потоа и катетата $RS$ користејќи ја Питагоровата теорема.

$$ST^2 = PS^2 + PT^2$$

2. Забележете дека триаголниците $\triangle PSQ$ и $\triangle RTQ$ се правоаголни и имаат еднакви агли кај темето $Q$. Што вели тоа за нивната сличност?

$$\triangle PSQ \sim \triangle RTQ$$

3. Како се однесуваат плоштините на сличните триаголници во однос на нивните страни?

$$\frac{P_{PSQ}}{P_{RTQ}} = \left( \frac{PS}{RT} \right)^2$$

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Оваа задача нè соочува со интересна конфигурација: четири точки ($P, S, R, T$) кои лежат на иста кружница (бидејќи аглите кај $P$ и $R$ се прави, тие „гледаат“ во дијаметарот $ST$). Ова е класичен **тригер** за користење својства на тетивни четириаголници или сличност.

**Зошто не одиме со директно пресметување на сите страни?** Иако знаеме многу должини, координатите на $Q$ не се веднаш очигледни. Наместо тоа, размислуваме за **односи на плоштини**. Триаголникот чија плоштина ја бараме, $\triangle SQT$, е дел од двата големи правоаголни триаголници чии плоштини лесно се пресметуваат. 

Клучниот увид лежи во сличноста $\triangle PSQ \sim \triangle RTQ$. Бидејќи ги знаеме соодветните катети $PS$ и $RT$, го знаеме и коефициентот на сличност, а со тоа и односот на нивните плоштини. Со поставување на едноставен систем равенки, лесно ќе го изолираме бараниот дел.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Пресметување на непознатите страни — формула: ST² = PS² + PT²</summary>

Прво, ја користиме Питагоровата теорема за $\triangle PST$ за да ја најдеме хипотенузата $ST$:

$$ST^2 = PS^2 + PT^2 = 6^2 + 17^2 = 36 + 289 = 325$$

Сега, ја користиме истата теорема за $\triangle RST$ за да ја најдеме катетата $RS$:

$$RS^2 = ST^2 - RT^2 = 325 - 1^2 = 324$$

$$RS = \sqrt{324} = 18$$

</details>

<details>
<summary>Чекор 2: Поставување на плоштините — формула: Area(PST) = PS·PT/2</summary>

Да ги означиме плоштините на триаголниците на следниот начин:
- $P_1 = \text{Area}(\triangle SQT)$ (ова е она што го бараме)
- $P_2 = \text{Area}(\triangle PSQ)$
- $P_3 = \text{Area}(\triangle RQT)$

Плоштините на големите правоаголни триаголници се:

$$\text{Area}(\triangle PST) = P_1 + P_2 = \frac{PS \cdot PT}{2} = \frac{6 \cdot 17}{2} = 51$$

$$\text{Area}(\triangle RST) = P_1 + P_3 = \frac{RT \cdot RS}{2} = \frac{1 \cdot 18}{2} = 9$$

</details>

<details>
<summary>Чекор 3: Користење на сличноста — формула: P₂/P₃ = (PS/RT)²</summary>

Разгледај ги $\triangle PSQ$ и $\triangle RTQ$. Имаме:
1. $\angle SPQ = \angle TRQ = 90^\circ$ (по услов)
2. $\angle SQP = \angle TQR$ (накрсни агли)

Според признакот АА, следува $\triangle PSQ \sim \triangle RTQ$. Односот на нивните плоштини е еднаков на квадратот на односот на нивните соодветни страни:

$$\frac{P_2}{P_3} = \left( \frac{PS}{RT} \right)^2 = \left( \frac{6}{1} \right)^2 = 36 \implies P_2 = 36P_3$$

</details>

<details>
<summary>Чекор 4: Решавање на системот равенки — формула: P₁ = 9 - P₃</summary>

Ги имаме равенките:
1) $P_1 + P_2 = 51$
2) $P_1 + P_3 = 9$

Ако ги одземеме равенките (1) - (2), добиваме:

$$P_2 - P_3 = 42$$

Заменувајќи $P_2 = 36P_3$:

$$36P_3 - P_3 = 42 \implies 35P_3 = 42$$

$$P_3 = \frac{42}{35} = \frac{6}{5} = 1.2$$

Сега, ја наоѓаме бараната плоштина $P_1$ од втората равенка:

$$P_1 = 9 - P_3 = 9 - 1.2 = 7.8$$

</details>

**Краен одговор:** Плоштината на триаголникот $SQT$ изнесува $\boxed{7.8}$

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Секогаш кога имате два правоаголни триаголници со заедничка хипотенуза, нацртајте ја кружницата околу нив. Ова често открива скриени агли или слични триаголници кои не се очигледни на прв поглед.
2.  **Чести Грешки:** Некои ученици се обидуваат да ги пресметаат должините на $SQ$ или $TQ$ преку сличност пред да работат со плоштините. Иако тоа е точно, пресметките стануваат непотребно гломазни со дропки. Односот на плоштините е секогаш поелегантно решение.
3.  **Зошто ова е важно:** Оваа задача ги спојува Питагоровата теорема, сличноста и системите равенки, што е типичен пример за тоа како геометријата и алгебрата се преплетуваат на олимписко ниво.

### 🔗 Поврзани вештини
* **Примарна вештина:** Сличност на триаголници (Macedonian: Сличност на триаголници)
* **Потребни предзнаења:** Питагорова теорема, Плоштина на триаголник, Решавање линеарни системи.

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Define Points based on the geometry
        # S is at origin, T on x-axis. ST = sqrt(325) approx 18.02
        st_val = 18.027
        S = ORIGIN
        T = RIGHT * 6.5 # Scaled down for fitting the screen
        
        # P and R calculated to match right angles
        # Using a semi-circle logic for visualization
        center = T / 2
        radius = 3.25
        
        # PS=6, PT=17 scaled for display
        P = np.array([0.5, 2.0, 0]) 
        # RT=1, RS=18 scaled
        R = np.array([5.8, 0.4, 0])
        
        # Q is intersection of PT and RS
        # For the diagram we approximate visually for clarity
        Q = np.array([2.5, 0.7, 0])
        
        # Draw Objects
        tri_pst = Polygon(P, S, T, color=BLACK, stroke_width=4)
        tri_rst = Polygon(R, S, T, color=BLACK, stroke_width=4)
        
        # Highlight target triangle SQT
        tri_sqt = Polygon(S, Q, T, color=YELLOW, fill_opacity=0.3, stroke_width=0)
        
        # Points and Labels
        pts = VGroup(
            Dot(S, color=BLACK), Dot(T, color=BLACK), 
            Dot(P, color=BLACK), Dot(R, color=BLACK), Dot(Q, color=RED)
        )
        lbls = VGroup(
            MathTex("S", color=BLACK).next_to(S, LEFT),
            MathTex("T", color=BLACK).next_to(T, RIGHT),
            MathTex("P", color=BLACK).next_to(P, UP),
            MathTex("R", color=BLACK).next_to(R, RIGHT),
            MathTex("Q", color=BLACK).next_to(Q, UP)
        )
        
        # Right Angle marks
        ra1 = RightAngle(Line(P, S), Line(P, T), length=0.2, color=GRAY)
        ra2 = RightAngle(Line(R, T), Line(R, S), length=0.2, color=GRAY)
        
        # Final Layout
        self.add(tri_sqt, tri_pst, tri_rst, ra1, ra2, pts, lbls)
        
        # Area text
        ans = MathTex("Area(SQT) = 7.8", color=BLACK).to_edge(DOWN)
        self.add(ans)
```