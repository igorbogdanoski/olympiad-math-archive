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
  - vectors
  - angle_chasing
  - geometry
  - complex_numbers
  - algebra
  - triangle_geometry
  - similarity
related_skills:
  - vectors
  - angle_chasing
  - complex_numbers
  - triangle_geometry
  - similarity--- GEOMETRY SKILLS ---
geometry_style: synthetic # synthetic | analytic | mixed
primary_skill: <main_tool> # e.g., angle_chasing, similarity, cyclic_quads
related_skills:
  - parallelogram_properties
  - trapezoid_midline

allowed_tools:
  - classical_euclidean
  - similarity
  - symmetry
forbidden_tools:
  - coordinate_geometry
  - vectors
  - complex_numbers
tags:
  - geometry
  - olympiad
---

# Збир на нормали од темиња на паралелограм

## Текст на задачата
Нека паралелограмот $ABCD$ и правата $p$ имаат единствена заедничка точка $D$. Ако $M, N, O$ се подножјата на нормалите повлечени од темињата $A, B, C$ на правата $p$, соодветно, докажи дека: $$AM + OC = BN$$

## 📐 Скица / Конструкција
<Опис на цртежот. Кои се клучните точки? Дали има помошни линии?>


<!-- VISUAL PROMPT: Draw parallelogram ABCD touching line p only at point D. Draw line p at an angle. Drop perpendiculars from A to p (point M), B to p (point N), and C to p (point O). Mark the center of the parallelogram as S and drop perpendicular SS'. -->

## 🧠 Анализа
Користи ја централната симетрија на паралелограмот. Пресекот на дијагоналите е клучната точка која ја поврзува левата и десната страна на равенството преку средни линии.

## 📝 Решение (СИНТЕТИЧКО)
1. **Конструкција:** Нека $S$ е пресекот на дијагоналите $AC$ и $BD$. Спуштаме нормала $SS'$ на правата $p$. 
2. **Трапез AMOC:** Бидејќи $AM \parallel SS' \parallel CO$ и $S$ е средина на $AC$, следува дека $SS'$ е средна линија во трапезот $AMOC$. Оттука, $SS' = \frac{AM + OC}{2}$. 
3. **Триаголник DBN:** Точката $D$ лежи на правата $p$ (висина 0). $S$ е средина на $BD$ и $SS' \parallel BN$. Следува дека $SS'$ е средна линија во $\triangle DBN$. Оттука, $SS' = \frac{BN}{2}$. 
4. **Изедначување:** Од двете релации следува $\frac{AM + OC}{2} = \frac{BN}{2}$, односно $AM + OC = BN$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
<Краен резултат.>