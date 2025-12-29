---
grade: 8
field: geometry
difficulty: 5
source: "<натпревар / списание / година>"
problem_id: geom_angle_overlap_05
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
  - right_triangles
  - overlapping_angles

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

# Агол на преклопување на хипотенуза

## Текст на задачата
На хипотенузата $BC$ во правоаголниот триаголник $ABC$ дадени се точките $D$ и $E$ такви што $BE = AB$ и $CD = AC$. Пресметај го аголот $\angle DAE$.

## 📐 Скица / Конструкција

![Визуелизација](../../assets/images/geom_angle_overlap_05.png){ width=500 }


![Визуелизација](../../assets/images/geom_angle_overlap_05.png){ width=500 }
## 🧠 Анализа
Аголот $\angle DAE$ е всушност 'вишокот' што се појавува кога ќе ги собереш аглите на двата рамнокраки триаголници внатре во правиот агол.

## 📝 Решение (СИНТЕТИЧКО)
1. **Рамнокраки триаголници:** $\triangle ABE$ е рамнокрак со врв во $B$, па $\angle BAE = 90 - \frac{\beta}{2}$. 
2. **Втор триаголник:** $\triangle ACD$ е рамнокрак со врв во $C$, па $\angle CAD = 90 - \frac{\gamma}{2}$. 
3. **Преклопување:** $\angle DAE = \angle BAE + \angle CAD - \angle BAC$. 
4. **Замена:** $\angle DAE = (90 - \frac{\beta}{2}) + (90 - \frac{\gamma}{2}) - 90 = 90 - \frac{\beta + \gamma}{2}$. 
5. **Финале:** Бидејќи $\beta + \gamma = 90$ (остри агли), тогаш $\angle DAE = 90 - 45 = 45^\circ$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.