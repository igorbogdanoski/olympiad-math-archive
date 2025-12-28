---
grade: 9
field: geometry
difficulty: 9
source: "<натпревар / списание / година>"
problem_id: geom_9_2015_iso_angle
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
  - angle_chasing
  - isosceles_triangles

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

# Агли кај специфичен рамнокрак триаголник

## Текст на задачата
Одреди ги аглите кај рамнокрак триаголник $ABC$, кај кој висината спуштена кон основата е двапати помала од должината на симетралата на еден од аглите при основата.

## 📐 Скица / Конструкција
<Опис на цртежот. Кои се клучните точки? Дали има помошни линии?>


![Визуелизација](../../assets/images/geom_9_2015_iso_angle.png)

## 🧠 Анализа
Конструирај средна линија која е паралелна со симетралата на аголот.

## 📝 Решение (СИНТЕТИЧКО)
1. Нека $CC_1$ е висина ($h$), $AA_1$ е симетрала ($l$). Дадено $l=2h$. 
2. Нека $D$ е средина на $BA_1$. Тогаш $C_1D$ е средна линија во $\triangle ABA_1$, па $C_1D = \frac{1}{2}l = h$. 
3. Од $C_1D=CC_1$ следува дека $\triangle CC_1D$ е рамнокрак. 
4. Со 'лов на агли': $\angle BC_1D = \frac{\alpha}{2}$. $\angle DC_1C = 2\alpha$. 
5. $2\alpha + \frac{\alpha}{2} = 90^\circ \implies 5\alpha = 180^\circ \implies \alpha = 36^\circ$. 
6. Аглите се $36^\circ, 36^\circ, 108^\circ$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
<Краен резултат.>