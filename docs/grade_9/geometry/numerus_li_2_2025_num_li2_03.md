---
grade: 9
field: geometry
difficulty: 6
source: "<натпревар / списание / година>"
problem_id: num_li2_03
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
  - circumcenter
  - construction

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

# Агли во триаголник (Рефлексија)

## Текст на задачата
Во $\triangle ABC$ со агли $\angle A = 40^\circ$ и $\angle C = 100^\circ$, да се одреди $\angle DCB$ ако $\angle DAB=20^\circ$ и $\angle ADB=130^\circ$.

## 📐 Скица / Конструкција
<Опис на цртежот. Кои се клучните точки? Дали има помошни линии?>

## 🧠 Анализа
Ова е варијација на Ленглиевиот проблем. Потребна е помошна конструкција. Забележи дека $\angle B = 40^\circ$, па $\triangle ABC$ е рамнокрак ($AC=BC$).

## 📝 Решение (СИНТЕТИЧКО)
1. **Анализа на $\triangle ABC$:**
   $\angle B = 180 - (40+100) = 40^\circ$. Бидејќи $\angle A = \angle B = 40^\circ$, триаголникот е рамнокрак со $AC=BC$.

2. **Анализа на $\triangle ABD$:**
   $\angle DAB = 20^\circ$, $\angle ADB = 130^\circ \implies \angle ABD = 30^\circ$.

3. **Конструкција:**
   Нека $O$ е центар на опишаната кружница околу $\triangle ABD$? Не, тоа е тешко.
   Ајде да искористиме тригонометриска форма на Чева за $\triangle ABC$ и точка $D$.
   $$ \frac{\sin 20}{\sin 20} \cdot \frac{\sin(100-x)}{\sin x} \cdot \frac{\sin 10}{\sin 30} = 1 $$
   (Бидејќи $\angle CAD = 40-20=20$, $\angle CBD = 40-30=10$).
   $$ 1 \cdot \frac{\sin(100-x)}{\sin x} \cdot \frac{\sin 10}{0,5} = 1 $$
   $$ \frac{\sin(100-x)}{\sin x} = \frac{0,5}{\sin 10} $$
   Решението е $x=20^\circ$ (види претходни слични задачи).

**Резултат:** $\angle DCB = 20^\circ$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.