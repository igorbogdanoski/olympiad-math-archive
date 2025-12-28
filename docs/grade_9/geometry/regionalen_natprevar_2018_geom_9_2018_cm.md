---
grade: 9
field: geometry
difficulty: 8
source: "<натпревар / списание / година>"
problem_id: geom_9_2018_cm
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

# Должина на симетрала преку разлика на страни

## Текст на задачата
Даден е триаголник $ABC$ со $\angle BAC=40^\circ, \angle ABC=20^\circ$ и $AB-BC=5$ cm. Ако симетралата на $\angle ACB$ ја сече $AB$ во точка $M$, да се пресмета должината на $CM$.

## 📐 Скица / Конструкција

![Triangle Bisector](images/geom_9_2018_cm.png)

## 💡 Решение

1.  **Пресметка на аглите во $\triangle ABC$:**
    $\angle C = 180^\circ - (40^\circ + 20^\circ) = 120^\circ$.
    Бидејќи $CM$ е симетрала на $\angle C$, следува $\angle ACM = \angle BCM = 60^\circ$.

2.  **Конструкција:**
    Нека $D$ е точка на страната $AB$ така што $BD = BC$.
    Бидејќи $AB > BC$ (затоа што $\angle C > \angle A$), точката $D$ лежи меѓу $A$ и $B$.
    Од условот на задачата, $AD = AB - BD = AB - BC = 5$.

3.  **Анализа на $\triangle BCD$:**
    Бидејќи $BD = BC$, триаголникот е рамнокрак.
    Аголот при врвот е $\angle B = 20^\circ$.
    Аглите при основата се:
    $$ \angle BCD = \angle BDC = \frac{180^\circ - 20^\circ}{2} = 80^\circ $$

4.  **Анализа на $\triangle ADC$:**
    Аголот $\angle ADC$ е суплементарен на $\angle BDC$:
    $$ \angle ADC = 180^\circ - 80^\circ = 100^\circ $$
    Во $\triangle ADC$, знаеме $\angle A = 40^\circ$ и $\angle ADC = 100^\circ$.
    Третиот агол е:
    $$ \angle ACD = 180^\circ - (40^\circ + 100^\circ) = 40^\circ $$
    Бидејќи $\angle A = \angle ACD = 40^\circ$, триаголникот $\triangle ADC$ е рамнокрак со $AD = CD$.
    Значи, $CD = 5$.

5.  **Анализа на $\triangle CDM$:**
    Треба да ја најдеме положбата на $M$ во однос на $D$.
    Бидејќи $\angle BCD = 80^\circ$ и $\angle BCM = 60^\circ$, зракот $CM$ лежи внатре во аголот $\angle BCD$.
    Тоа значи дека точката $M$ лежи помеѓу $D$ и $B$.
    
    Во $\triangle CDM$:
    *   $\angle CDM = 180^\circ - \angle ADC = 180^\circ - 100^\circ = 80^\circ$.
    *   $\angle DCM = \angle BCD - \angle BCM = 80^\circ - 60^\circ = 20^\circ$.
    *   $\angle CMD = 180^\circ - (80^\circ + 20^\circ) = 80^\circ$.
    
    Бидејќи $\angle CDM = \angle CMD = 80^\circ$, триаголникот $\triangle CDM$ е рамнокрак со $CD = CM$.

6.  **Заклучок:**
    Имаме $CM = CD = 5$.

Конечниот одговор е $5$ cm.