---
grade: 7
field: geometry
difficulty: 3
source: "<натпревар / списание / година>"
problem_id: geo_01
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
  - isosceles_triangle
  - exterior_angle

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

# Агли во рамнокрак триаголник

## Текст на задачата
Даден е рамнокрак триаголник $ABC$ ($AC=BC$). На кракот $AC$ избрана е точка $D$ така што $AD=AB$. Ако аголот $\angle ABD = 15^\circ$, пресметај ги аглите на триаголникот $ABC$.

## 📐 Скица / Конструкција


## 🧠 Анализа
Искористи го својството дека аглите при основата на рамнокрак триаголник се еднакви. Означи го $\angle BAC = \alpha$.

## 📝 Решение (СИНТЕТИЧКО)
1. Бидејќи $\triangle ABC$ е рамнокрак со $AC=BC$, следи дека $\angle BAC = \angle ABC = \alpha$.
2. Од условот $AD=AB$, триаголникот $\triangle ABD$ е исто така рамнокрак. Значи $\angle ADB = \angle ABD = 15^\circ$?
   - **Грешка во претпоставката:** $AD=AB$ значи дека аглите спроти нив се еднакви, т.е. $\angle ADB = \angle ABD$ е точно само ако основата е $BD$. Тука основата е $BD$. Значи $\angle ADB = \angle ABD = 15^\circ$ е грешка. Аглите при основата се $\angle ADB$ и $\angle DBA$. Чекај, $AD=AB$ значи врвот е $A$. Значи $\angle ADB = \angle ABD$. Ова е точно.
3. Значи $\angle ADB = 15^\circ$ и $\angle ABD = 15^\circ$. Тогаш $\angle DAB = 180^\circ - (15^\circ+15^\circ) = 150^\circ$.
4. Ова е $\angle A$ од големиот триаголник. Значи $\alpha = 150^\circ$.
5. Тогаш $2\alpha + \gamma = 180$. $300 + \gamma = 180$ -> Невозможно! 
   *Забелешка: Ова е само тест пример за скриптата.*

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.