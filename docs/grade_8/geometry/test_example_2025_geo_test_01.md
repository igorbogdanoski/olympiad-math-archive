---
grade: 8
field: geometry
difficulty: 3
source: "<натпревар / списание / година>"
problem_id: geo_test_01
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
  - similarity
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

# Висина кон хипотенузата

## Текст на задачата
Во правоаголен триаголник $ABC$ ($\angle C = 90^\circ$), висината $CD$ спуштена кон хипотенузата ја дели на отсечки со должини $AD=4$ cm и $BD=9$ cm. Пресметај ја должината на висината $CD$.

## 📐 Скица / Конструкција

![Right Triangle Altitude](images/geo_test_01.png)

## 💡 Решение

Дадено е:
*   Правоаголен триаголник $ABC$ со прав агол во $C$.
*   Висина $CD \perp AB$.
*   Отсечки $AD = 4$ cm и $BD = 9$ cm.

Според Евклидовата теорема за висината во правоаголен триаголник, квадратот на висината е еднаков на производот од отсечките на хипотенузата:
$$ CD^2 = AD \cdot BD $$

Заменуваме со дадените вредности:
$$ CD^2 = 4 \cdot 9 $$
$$ CD^2 = 36 $$

Коренуваме за да ја добиеме должината:
$$ CD = \sqrt{36} $$
$$ CD = 6 \text{ cm} $$

Висината $CD$ изнесува $6$ cm.