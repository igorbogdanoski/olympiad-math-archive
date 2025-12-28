---
grade: 9
field: geometry
difficulty: 4
source: "<натпревар / списание / година>"
problem_id: geom_9_right_tri_perimeter
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
  - algebraic_manipulation
  - right_triangles

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

# Хипотенуза преку периметар и впишан радиус

## Текст на задачата
Периметарот на еден правоаголен триаголник е $30$ cm, а радиусот на впишаната кружница е $2$ cm. Пресметај ја должината на хипотенузата.

## 📐 Скица / Конструкција


<div align="center">
  <img src="../../assets/images/geom_9_right_tri_perimeter.png" alt="Визуелизација" width="500"/>
</div>
## 🧠 Анализа
Користи ја специјалната формула за радиус на впишана кружница во правоаголен триаголник: $r = (a+b-c)/2$.

## 📝 Решение (СИНТЕТИЧКО)
1. **Поставка:** Нека $a, b$ се катети, а $c$ е хипотенуза. Дадено е $a+b+c = 30$ и $r=2$.
2. **Замена:** Од периметарот, $a+b = 30 - c$. 
3. **Формула:** За правоаголен триаголник важи $r = \frac{a+b-c}{2}$. Заменуваме: $2 = \frac{(30-c)-c}{2}$.
4. **Решавање:** $4 = 30 - 2c \implies 2c = 26 \implies c = 13$ cm.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.