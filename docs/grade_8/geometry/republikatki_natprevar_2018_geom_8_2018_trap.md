---
grade: 8
field: geometry
difficulty: 7
source: "<натпревар / списание / година>"
problem_id: geom_8_2018_trap
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
  - parallelograms
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

# Агли на основа во специфичен трапез

## Текст на задачата
Даден е трапез $ABCD$ со основи $AB=a, CD=b, a>b$. Нека $M$ и $N$ се средини на основите $AB$ и $CD$, соодветно, и нека $MN = \frac{a-b}{2}$. Пресметај го збирот на аглите на поголемата основа.

## 📐 Скица / Конструкција

![Trapezoid Midpoints](images/geom_8_2018_trap.png)

## 💡 Решение

Нека повлечеме прави низ точката $N$ (средина на $CD$) кои се паралелни со краците $AD$ и $BC$.
Нека овие прави ја сечат основата $AB$ во точките $P$ и $Q$, така што $NP \parallel AD$ и $NQ \parallel BC$.

1.  **Паралелограми:**
    Четириаголникот $APND$ е паралелограм (бидејќи $AP \parallel DN$ и $NP \parallel AD$).
    Следствено, $AP = DN = \frac{b}{2}$.
    Четириаголникот $NQCD$ е паралелограм (бидејќи $NQ \parallel BC$ и $NC \parallel QB$).
    Следствено, $QB = NC = \frac{b}{2}$.

2.  **Должина на $PQ$:**
    $PQ = AB - AP - QB = a - \frac{b}{2} - \frac{b}{2} = a - b$.

3.  **Положба на $M$:**
    Точката $M$ е средина на $AB$, па $AM = \frac{a}{2}$.
    Растојанието $PM = AM - AP = \frac{a}{2} - \frac{b}{2} = \frac{a-b}{2}$.
    Растојанието $MQ = MB - QB = \frac{a}{2} - \frac{b}{2} = \frac{a-b}{2}$.
    Значи, $M$ е средина на отсечката $PQ$.

4.  **Триаголник $PNQ$:**
    Во $\triangle PNQ$, отсечката $NM$ е тежишна линија (медијана) кон страната $PQ$.
    Дадено е дека $MN = \frac{a-b}{2}$.
    Бидејќи $PQ = a-b$, следува дека $MN = \frac{1}{2} PQ$.
    
    Познато е дека медијаната кон една страна во триаголник е еднаква на половина од таа страна ако и само ако триаголникот е правоаголен (со прав агол во темето од кое поаѓа медијаната).
    Значи, $\angle PNQ = 90^\circ$.

5.  **Збир на агли:**
    Бидејќи $NP \parallel AD$, аголот $\angle NPQ = \angle DAB = \alpha$ (согласни агли).
    Бидејќи $NQ \parallel BC$, аголот $\angle NQP = \angle CBA = \beta$ (согласни агли).
    Во правоаголниот $\triangle PNQ$:
    $$ \angle NPQ + \angle NQP = 90^\circ $$
    $$ \alpha + \beta = 90^\circ $$

Збирот на аглите на поголемата основа е $90^\circ$.