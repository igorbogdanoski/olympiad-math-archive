---
grade: 9
field: geometry
difficulty: 8
source: "<натпревар / списание / година>"
problem_id: geom_9_2018_cm
language_original: <mk | en | sr | hr | ...>
translated: false

# --- GEOMETRY SKILLS ---
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
<Опис на цртежот. Кои се клучните точки? Дали има помошни линии?>


<!-- VISUAL PROMPT: Draw triangle ABC with angle A=40 and B=20. Draw bisector CM. Mark point D on AB such that BD=BC. -->

## 🧠 Анализа
Условот $AB-BC$ сугерира конструкција на точка $D$ на $AB$ таква што $BD=BC$.

## 📝 Решение (СИНТЕТИЧКО)
1. $\angle ACB = 180 - (40+20) = 120^\circ$. Симетралата $CM$ ги дели на $60^\circ$. 
2. Доцртај $D$ на $AB$ со $BD=BC$. Тогаш $AD = AB-BC = 5$. 
3. $\triangle BCD$ е рамнокрак со агли $80, 80, 20$. Тогаш $\angle ADC = 100^\circ$. 
4. Во $\triangle ADC$, аглите се $40, 100, 40$, па $CD=AD=5$. 
5. Во $\triangle CDM$, $\angle CDM=80^\circ$ и $\angle CMD=80^\circ$, па $CM=CD=5$ cm.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
<Краен резултат.>