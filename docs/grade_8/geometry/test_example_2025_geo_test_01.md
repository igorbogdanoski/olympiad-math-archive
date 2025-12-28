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


![Визуелизација](../../assets/images/geo_test_01.png){ width=500 }
## 🧠 Анализа
Користи ја Евклидовата теорема за висината во правоаголен триаголник: Висината на квадрат е еднаква на производот на проекциите на катетите ($h^2 = p \cdot q$).

## 📝 Решение (СИНТЕТИЧКО)
Дадено е:
- $p = AD = 4$ cm
- $q = BD = 9$ cm

Според метричките релации во правоаголен триаголник, важи:
$$ CD^2 = AD \cdot BD $$

Заменуваме со броевите:
$$ CD^2 = 4 \cdot 9 $$
$$ CD^2 = 36 $$
$$ CD = \sqrt{36} = 6 $$

**Резултат:** Висината е **6 cm**.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.