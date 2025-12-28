---
grade: 8
field: geometry
difficulty: 5
source: "<натпревар / списание / година>"
problem_id: geom_8_viviani_proof
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
  - equilateral_triangle
  - invariants

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

# Теорема на Вивиани

## Текст на задачата
Нека $S$ е произволна точка во внатрешноста на рамностран триаголник $ABC$, а $M, N, P$ се подножјата на нормалите од $S$ кон страните. Докажи дека $SM + SN + SP = h$, каде $h$ е висината на триаголникот.

## 📐 Скица / Конструкција

![Визуелизација](../../../assets/images/geom_8_viviani_proof.png){ width=500 }


![Визуелизација](../../assets/images/geom_8_viviani_proof.png){ width=500 }
## 🧠 Анализа
Ова е специјален случај на идентитетот на нормали. Бидејќи сите страни се еднакви, плоштината се поедноставува драматично.

## 📝 Решение (СИНТЕТИЧКО)
1. **Поделба:** Поврзи ја точката $S$ со темињата $A, B, C$. 
2. **Сума на плоштини:** $P_{ABC} = P_{ABS} + P_{BCS} + P_{CAS}$. 
3. **Алгебарски приказ:** $\frac{ah}{2} = \frac{a \cdot SP}{2} + \frac{a \cdot SM}{2} + \frac{a \cdot SN}{2}$. 
4. **Упростување:** Бидејќи $a \neq 0$ и е исто за сите членови, ја делиме целата равенка со $\frac{a}{2}$. 
5. **Заклучок:** Добиваме $h = SP + SM + SN$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.