---
grade: 8
field: geometry
difficulty: 7
source: "<натпревар / списание / година>"
problem_id: geom_8_2018_para_line
language_original: <mk | en | sr | hr | ...>
translated: false

# 
tags:
  - geometry
  - parallelogram
  - perpendiculars
  - coordinates
related_skills:
  - midpoint_formula
  - coordinate_geometry_proof
---

# Problem
Let parallelogram $ABCD$ and line $p$ have a unique common point $D$. If $M, N, O$ are the feet of the perpendiculars drawn from vertices $A, B, C$ to line $p$, respectively, prove that:
$$AM + OC = BN$$

![Problem Visualization](media/geom_8_2018_para_line.mp4)

# Solution
Let line $p$ be the x-axis. Since $D$ lies on $p$, its y-coordinate is $y_D = 0$.
Let $y_A, y_B, y_C$ be the y-coordinates of vertices $A, B, C$.
The lengths of the perpendiculars are the absolute values of the y-coordinates:
$$AM = |y_A|, \quad BN = |y_B|, \quad OC = |y_C|$$

Since $ABCD$ is a parallelogram, the diagonals $AC$ and $BD$ bisect each other.
Let $S$ be the intersection of the diagonals. The y-coordinate of $S$ is the average of the y-coordinates of the endpoints of each diagonal:
$$y_S = \frac{y_A + y_C}{2} = \frac{y_B + y_D}{2}$$

Since $y_D = 0$, we have:
$$\frac{y_A + y_C}{2} = \frac{y_B}{2} \implies y_A + y_C = y_B$$

Since the parallelogram lies on one side of the line $p$ (except for point $D$), the y-coordinates $y_A, y_B, y_C$ all have the same sign.
Therefore, we can sum their absolute values:
$$|y_A| + |y_C| = |y_B|$$

Substituting the lengths of the perpendiculars:
$$AM + OC = BN$$

This completes the proof.

![Parallelogram Line](images/geom_8_2018_para_line.png)

## 💡 Решение

Нека $S$ е пресекот на дијагоналите $AC$ и $BD$. Бидејќи $ABCD$ е паралелограм, $S$ е средина на $AC$ и $BD$.
Нека $S'$ е подножјето на нормалата од $S$ кон правата $p$.
Бидејќи $S$ е средина на $AC$, отсечката $SS'$ е средна линија во трапезот $AMOC$ (или триаголникот ако $A, C$ се од иста страна).
Всушност, $SS'$ е средна вредност на растојанијата од $A$ и $C$ до правата $p$.
Бидејќи $A$ и $C$ се од иста страна на $p$ (бидејќи $p$ има само една заедничка точка со паралелограмот, $D$), важи:
$$ SS' = \frac{AM + OC}{2} $$
Од друга страна, во $\triangle DBN$, $S$ е средина на $DB$.
Бидејќи $D$ лежи на $p$, растојанието од $D$ до $p$ е 0.
Тогаш $SS'$ е средна линија во $\triangle DBN$ (поточно, $SS'$ е паралелна со $BN$ и $S$ е средина на $DB$).
Затоа:
$$ SS' = \frac{BN}{2} $$
Изедначувајќи ги двата израза за $SS'$:
$$ \frac{AM + OC}{2} = \frac{BN}{2} $$
$$ AM + OC = BN $$
Што требаше да се докаже. 
3. **Триаголник DBN:** Точката $D$ лежи на правата $p$ (висина 0). $S$ е средина на $BD$ и $SS' \parallel BN$. Следува дека $SS'$ е средна линија во $\triangle DBN$. Оттука, $SS' = \frac{BN}{2}$. 
4. **Изедначување:** Од двете релации следува $\frac{AM + OC}{2} = \frac{BN}{2}$, односно $AM + OC = BN$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.