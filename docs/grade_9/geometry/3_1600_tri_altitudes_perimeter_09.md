---
grade: 9
field: geometry
difficulty: 5
source: "<натпревар / списание / година>"
problem_id: tri_altitudes_perimeter_09
language_original: <mk | en | sr | hr | ...>
translated: false

# 
tags:
  - vectors
  - angle_chasing
  - geometry
  - area
  - complex_numbers
  - algebra
  - similarity
related_skills:
  - vectors
  - angle_chasing
  - area
  - complex_numbers
  - similarity--- GEOMETRY SKILLS ---
geometry_style: synthetic # synthetic | analytic | mixed
primary_skill: <main_tool> # e.g., angle_chasing, similarity, cyclic_quads
related_skills:
  - area_method
  - reciprocal_relations

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

# Периметар преку однос на висини

## Текст на задачата
За висините во триаголникот $ABC$ важи $h_c = h_a + h_b$. Ако $a = 4$ dm и $b = 6$ dm, пресметај го периметарот на $ABC$.

## 📐 Скица / Конструкција
<Опис на цртежот. Кои се клучните точки? Дали има помошни линии?>

<div align="center">
  <img src="../../assets/images/tri_altitudes_perimeter_09.png" alt="Визуелизација" width="500"/>
</div>
## 🧠 Анализа
Методологија: Изразете ги сите висини преку плоштината $P$ и страните. Плоштината е 'мостот' помеѓу страните и висините.

## 📝 Решение (СИНТЕТИЧКО)
1. **Висини преку плоштина:** Од $P = \frac{a \cdot h_a}{2}$, имаме $h_a = \frac{2P}{a}$. Слично, $h_b = \frac{2P}{b}$ и $h_c = \frac{2P}{c}$.
2. **Замена во условот:** Условот $h_c = h_a + h_b$ станува $\frac{2P}{c} = \frac{2P}{a} + \frac{2P}{b}$.
3. **Упростување:** По делење со $2P$, ја добиваме релацијата $\frac{1}{c} = \frac{1}{a} + \frac{1}{b}$.
4. **Пресметка на c:** Со замена на $a=4$ и $b=6$, добиваме $\frac{1}{c} = \frac{1}{4} + \frac{1}{6} = \frac{5}{12}$, од каде $c = \frac{12}{5} = 2.4$ dm.
5. **Периметар:** $L = a + b + c = 4 + 6 + 2.4 = 12.4$ dm.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.