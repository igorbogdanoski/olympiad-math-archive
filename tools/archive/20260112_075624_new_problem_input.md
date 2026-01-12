---
problem_id: regional_2025_1_4b_verified
title: Заедничка хипотенуза и плоштина на триаголници (Верификувано)
grade: 9
difficulty: 6
type: geometry
tags:
  - pitagorina_teorema
  - slicnost_na_triagolnici
  - plostina
primary_skill: slicnost_na_triagolnici
related_skills:
  - algebarski_sistemi
  - tektivni_cetiriagolnici
source: Регионален натпревар по математика за средно образование 2025 (Сигма 139, стр. 50-51)
---

# Заедничка хипотенуза и плоштина на триаголници

# Текст на задачата
Дадени се два правоаголни триаголници, $\triangle PST$ и $\triangle RST$ со заедничка хипотенуза $ST$. Катетите $PT$ и $RS$ се сечат во точката $Q$. Ако $PS = 6$, $PT = 17$ и $RT = 1$, пресметај ја плоштината на $\triangle SQT$.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Прво пресметајте ја должината на заедничката хипотенуза $ST$, а потоа и катетата $RS$ користејќи ја Питагоровата теорема. Изворите потврдуваат дека $ST^2 = 325$.

$$ST^2 = PS^2 + PT^2$$

2. Користете ја сличноста помеѓу $\triangle PSQ$ и $\triangle RTQ$. Коефициентот на сличност $k$ е односот на нивните катети.

$$k = \frac{PS}{RT} = 6$$

3. Плоштините на триаголниците се поврзани преку збирови. Ако $P_1$ е плоштината на $\triangle SQT$, тогаш плоштините на $\triangle PST$ и $\triangle RST$ го содржат $P_1$.

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Оваа задача ја користи геометриската конфигурација на два правоаголни триаголници впишани во иста кружница (бидејќи ја делат хипотенузата $ST$ како заеднички дијаметар). **Тригерот** за решението е точката на пресек $Q$ на двете катети, која формира два слични триаголници $\triangle PSQ$ и $\triangle RTQ$. 

Зошто се слични? Бидејќи имаат прави агли кај $P$ и $R$, а аглите кај $Q$ се накрсни. Наместо да бараме поединечни должини на катетите $SQ$ или $TQ$, многу поелегантно е да работиме со **системи од плоштини**. Изворот (Сигма 139) го користи овој пристап, дефинирајќи три под-плоштини кои кога ќе се комбинираат ги даваат плоштините на големите триаголници $\triangle PST$ и $\triangle RST$. Ова го трансформира геометрискиот проблем во едноставен линеарен систем.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Примена на Питагорова теорема</summary>

Според изворот, прво ја наоѓаме хипотенузата $ST$:

$$ST^2 = PS^2 + PT^2 = 6^2 + 17^2 = 36 + 289 = 325$$

Сега, ја наоѓаме катетата $RS$ на вториот правоаголен триаголник:

$$RS^2 = ST^2 - RT^2 = 325 - 1^2 = 324$$

$$RS = \sqrt{324} = 18$$

(Овие пресметки се потврдени во изворот).

</details>

<details>
<summary>Чекор 2: Дефинирање на плоштините и сличноста</summary>

Ги означуваме плоштините како во официјалното решение:
- $P_1 = \text{Area}(\triangle SQT)$
- $P_2 = \text{Area}(\triangle PSQ)$
- $P_3 = \text{Area}(\triangle RTQ)$

Плоштините на правоаголните триаголници се:

$$\text{Area}(\triangle PST) = P_1 + P_2 = \frac{6 \cdot 17}{2} = 51$$

$$\text{Area}(\triangle RST) = P_1 + P_3 = \frac{1 \cdot 18}{2} = 9$$

Од сличноста $\triangle PSQ \sim \triangle RTQ$, коефициентот е $k = \frac{PS}{RT} = 6$. Односот на плоштините е $k^2$:

$$\frac{P_2}{P_3} = 6^2 = 36 \implies P_2 = 36P_3$$

</details>

<details>
<summary>Чекор 3: Решавање на системот равенки</summary>

Го решаваме системот:
1) $P_1 + P_2 = 51$
2) $P_1 + P_3 = 9$
3) $P_2 = 36P_3$

Заменувајќи ја (3) во (1):
$P_1 + 36P_3 = 51$

Одземајќи ја равенката (2) од оваа нова равенка:
$(P_1 + 36P_3) - (P_1 + P_3) = 51 - 9$
$35P_3 = 42$
$P_3 = \frac{42}{35} = \frac{6}{5} = 1.2$

Конечно, ја наоѓаме бараната плоштина $P_1$:
$P_1 = 9 - P_3 = 9 - 1.2 = 7.8$

Изворот го запишува ова како разломка: $P_1 = \frac{39}{5}$.

</details>

**Краен одговор:** $\boxed{7.8}$ (или $\boxed{\frac{39}{5}}$)

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Верификацијата на пресметките покажа дека идентитетот $P_1 + P_3 = 9$ е клучната точка за брзо решение. Секогаш кога имате преклопени триаголници, одземањето на нивните плоштини ја елиминира заедничката површина ($P_1$) и остава чист однос помеѓу преостанатите делови.
2.  **Чести Грешки:** Некои ученици се обидуваат да ја најдат висината на точката $Q$ релативно на $ST$. Иако е можно, тоа бара многу посложена тригонометрија или координатна геометрија, што не е препорачливо според нашиот Кодекс.
3.  **Зошто ова е важно:** Оваа задача е извлечена од официјалниот Регионален натпревар 2025 и служи како совршен пример за поврзување на Питагоровата теорема со напредни својства на сличност.

### 🔗 Поврзани вештини
* **Примарна вештина:** Сличност на триаголници (Macedonian: Сличност на триаголници)
* **Потребни предзнаења:** Питагорова теорема, Системи линеарни равенки.

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # --- CONFIGURATION ---
        # Scaling the diagram to fit the screen based on RS=18, PT=17
        scale_factor = 0.35
        
        # Coordinates (approximated for visual clarity but preserving properties)
        # S is origin, T is on x-axis
        S = ORIGIN
        T = RIGHT * 18.0 * scale_factor
        

        # Calculated to represent PS=6, PT=17 roughly
        P = np.array([2.0, 5.5, 0]) * scale_factor
        # Calculated to represent RT=1, RS=18 roughly
        R = np.array([17.5, 1.0, 0]) * scale_factor

        # Пресметка на Q како пресек на PT и RS
        def line_intersection(A, B, C, D):
          # Наоѓање на пресек на правите AB и CD
          BA = B - A
          DC = D - C
          AC = A - C
          denom = BA[0]*DC[1] - BA[1]*DC[0]
          if abs(denom) < 1e-8:
            return A  # паралелни, врати A
          t = (DC[0]*AC[1] - DC[1]*AC[0]) / denom
          return A + t*BA

        # PT: P->T, RS: R->S
        Q = line_intersection(P, T, R, S)

        # Центрирање на цртежот (поместување лево)
        shift_vec = LEFT * 2.5
        S += shift_vec
        T += shift_vec
        P += shift_vec
        R += shift_vec
        Q += shift_vec
        
        # --- GEOMETRY ---
        tri_pst = Polygon(P, S, T, color=BLACK, stroke_width=4)
        tri_rst = Polygon(R, S, T, color=BLACK, stroke_width=4)
        
        # Target area highlight
        sqt_fill = Polygon(S, Q, T, color=YELLOW, fill_opacity=0.2, stroke_width=0)
        
        # Right angle symbols
        ra_p = RightAngle(Line(P, S), Line(P, T), length=0.2, color=BLACK)
        ra_r = RightAngle(Line(R, T), Line(R, S), length=0.2, color=BLACK)
        
        # Labels
        lbl_p = MathTex("P", color=BLACK).next_to(P, UP)
        lbl_s = MathTex("S", color=BLACK).next_to(S, LEFT)
        lbl_t = MathTex("T", color=BLACK).next_to(T, RIGHT)
        lbl_r = MathTex("R", color=BLACK).next_to(R, RIGHT)
        lbl_q = MathTex("Q", color=BLACK).next_to(Q, UP)
        
        # Annotations (matching Document 51)
        p1 = MathTex("P_1", color=BLACK).move_to(sqt_fill.get_center())
        p2 = MathTex("P_2", color=BLACK).move_to((P+S+Q)/3)
        p3 = MathTex("P_3", color=BLACK).move_to((R+T+Q)/3)

        # Final setup
        self.add(sqt_fill, tri_pst, tri_rst, ra_p, ra_r)
        self.add(lbl_p, lbl_s, lbl_t, lbl_r, lbl_q)
        self.add(p1, p2, p3)
        
        # Boxed answer display
        ans = MathTex("P_1 = 7.8", color=BLACK).to_edge(DOWN).shift(UP*0.5)
        rect = SurroundingRectangle(ans, color=BLACK)
        self.add(ans, rect)
```