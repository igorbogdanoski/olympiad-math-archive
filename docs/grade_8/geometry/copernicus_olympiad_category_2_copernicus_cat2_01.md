---
grade: 8
field: geometry
difficulty: 5
source: "<натпревар / списание / година>"
problem_id: copernicus_cat2_01
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
  - isosceles_triangle
  - square_properties

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

# Рамностран триаголник во квадрат

## Текст на задачата
Даден е квадрат $ABCD$. Во неговата внатрешност е избрана точка $E$ така што $\triangle ABE$ е рамностран. Пресметај ја големината на аголот $\angle DEC$.

## 📐 Скица / Конструкција


<div align="center">
  <img src="../../assets/images/copernicus_cat2_01.png" alt="Визуелизација" width="500"/>
</div>
## 🧠 Анализа
Ова е класична задача. Клучот е да ги искористиш еднаквостите на страните. Бидејќи $ABCD$ е квадрат, $AB=BC=CD=DA$. Бидејќи $\triangle ABE$ е рамностран, $AB=AE=BE$. Заклучокот е дека $AE=AD$ и $BE=BC$. Ова формира два скриени рамнокраки триаголници: $\triangle ADE$ и $\triangle BCE$.

## 📝 Решение (СИНТЕТИЧКО)
### Чекор 1: Анализа на страните
Од својствата на квадратот и рамностраниот триаголник имаме:
1. $AB = BC = CD = DA$ (страни на квадрат).
2. $AB = AE = BE$ (страни на рамностран триаголник).

Од (1) и (2) следи транзитивноста:
$$ AD = AE \quad \text{и} \quad BC = BE $$

### Чекор 2: Ловење агли во $\triangle ADE$
Бидејќи $AD = AE$, триаголникот $\triangle ADE$ е **рамнокрак**.
Аголот при врвот $A$ е:
$$ \angle DAE = \angle DAB - \angle EAB = 90^\circ - 60^\circ = 30^\circ $$
Аглите при основата $DE$ се еднакви:
$$ \angle ADE = \angle AED = \frac{180^\circ - 30^\circ}{2} = 75^\circ $$

### Чекор 3: Ловење агли во $\triangle BCE$
Аналогно, $\triangle BCE$ е рамнокрак ($BC=BE$).
Аголот при врвот $B$ е:
$$ \angle CBE = \angle CBA - \angle EBA = 90^\circ - 60^\circ = 30^\circ $$
Аглите при основата $CE$ се:
$$ \angle BCE = \angle BEC = \frac{180^\circ - 30^\circ}{2} = 75^\circ $$

### Чекор 4: Пресметка на $\angle DEC$
Аголот $\angle DEC$ може да се најде на два начина.
**Начин А (Преку полн агол околу E):**
$$ \angle DEC = 360^\circ - (\angle AEB + \angle AED + \angle BEC) $$
$$ \angle DEC = 360^\circ - (60^\circ + 75^\circ + 75^\circ) = 360^\circ - 210^\circ = 150^\circ $$

**Начин Б (Преку аглите на квадратот):**
Во $\triangle CDE$, аглите при основата $CD$ се:
$\angle EDC = \angle ADC - \angle ADE = 90^\circ - 75^\circ = 15^\circ$.
$\angle ECD = \angle BCD - \angle BCE = 90^\circ - 75^\circ = 15^\circ$.
Тогаш:
$$ \angle DEC = 180^\circ - (15^\circ + 15^\circ) = 180^\circ - 30^\circ = 150^\circ $$

**Резултат:** $\angle DEC = 150^\circ$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.