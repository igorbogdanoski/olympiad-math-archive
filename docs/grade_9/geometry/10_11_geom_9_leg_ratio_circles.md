---
grade: 9
field: geometry
difficulty: 6
source: "<натпревар / списание / година>"
problem_id: geom_9_leg_ratio_circles
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
geometry_style: analytic # synthetic | analytic | mixed
primary_skill: <main_tool> # e.g., angle_chasing, similarity, cyclic_quads
related_skills:
  - quadratic_equations
  - pythagorean_theorem

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

# Однос на катети преку радиуси

## Текст на задачата
Во правоаголен триаголник, односот на радиусите на впишаната и опишаната кружница е $2:5$. Определи го односот на катетите.

## 📐 Скица / Конструкција


<div align="center">
  <img src="../../assets/images/geom_9_leg_ratio_circles.png" alt="Визуелизација" width="500"/>
</div>
## 🧠 Анализа
Изрази ги $r$ и $R$ преку страните ($R=c/2$) и постави хомогена равенка по $k=a/b$.

## 📝 Решение (СИНТЕТИЧКО)
1. **Релации:** $R = c/2$ и $r = (a+b-c)/2$. Односот е $r/R = (a+b-c)/c = 2/5$.
2. **Равенка:** $5a+5b-5c = 2c \implies 5(a+b) = 7c$. Квадрираме: $25(a^2+2ab+b^2) = 49c^2$.
3. **Супституција:** Користиме $a^2+b^2 = c^2$, па $25(c^2+2ab) = 49c^2 \implies 50ab = 24c^2 \implies 50ab = 24(a^2+b^2)$.
4. **Квадратна равенка:** Делиме со $b^2$ и воведуваме $k=a/b$: $12k^2 - 25k + 12 = 0$. Решенијата се $k_1 = 4/3$ и $k_2 = 3/4$.
5. **Заклучок:** Односот на катетите е $3:4$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.