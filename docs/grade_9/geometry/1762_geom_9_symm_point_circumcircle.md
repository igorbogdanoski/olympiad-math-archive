---
grade: 9
field: geometry
difficulty: 8
source: "<натпревар / списание / година>"
problem_id: geom_9_symm_point_circumcircle
language_original: <mk | en | sr | hr | ...>
translated: false

# 
tags:
  - circle_geometry
  - vectors
  - angle_chasing
  - geometry
  - complex_numbers
  - algebra
  - triangle_geometry
  - similarity
related_skills:
  - circle_geometry
  - vectors
  - angle_chasing
  - complex_numbers
  - triangle_geometry
  - similarity--- GEOMETRY SKILLS ---
geometry_style: synthetic # synthetic | analytic | mixed
primary_skill: <main_tool> # e.g., angle_chasing, similarity, cyclic_quads
related_skills:
  - cyclic_quadrilaterals
  - similarity

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

# Симетрична точка на опишана кружница

## Текст на задачата
Точката $D$ е во внатрешноста на остроаголниот триаголник $ABC$ за кој важат равенствата $\angle ADB = \angle CDA = 180^\circ - \angle BAC$. Докажи дека симетричната точка $A'$ на точката $A$ во однос на точката $D$ лежи на опишаната кружница околу триаголникот $ABC$.

## 📐 Скица / Конструкција

![Визуелизација](../../assets/images/geom_9_symm_point_circumcircle.png)


![Визуелизација](../../assets/images/geom_9_symm_point_circumcircle.png){ width=500 }
## 🧠 Анализа
Хеуристика: 'Докажи тетивност преку суплементни агли'. Треба да покажеме дека $\angle BA'C + \angle BAC = 180^\circ$. Прво докажете ја сличноста на триаголниците со точката $D$.

## 📝 Решение (СИНТЕТИЧКО)
1. **Сличност:** Нека $\angle BAC = \alpha$. Со 'лов на агли' добиваме дека $\triangle ABD \sim \triangle CAD$ (бидејќи имаат два еднакви агли $\alpha-x$ и $\alpha-y$). Од ова следува $AD^2 = BD \cdot CD$.
2. **Втора сличност:** Бидејќи $A'D = AD$ (симетрија), тогаш $A'D^2 = BD \cdot CD$, односно $\frac{BD}{A'D} = \frac{A'D}{CD}$. Бидејќи $\angle BDA' = \angle CDA' = \alpha$ (суплементни на $180-\alpha$), следува $\triangle BDA' \sim \triangle A'DC$ (признак САС).
3. **Агли на четириаголникот:** Од сличноста во чекор 2, наоѓаме дека $\angle BA'D + \angle DA'C = 180^\circ - \alpha$.
4. **Заклучок:** Во четириаголникот $ABA'C$, $\angle BAC + \angle BA'C = \alpha + (180^\circ - \alpha) = 180^\circ$. Бидејќи збирот на спротивните агли е $180^\circ$, четириаголникот е тетивен, па $A'$ лежи на кружницата.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.