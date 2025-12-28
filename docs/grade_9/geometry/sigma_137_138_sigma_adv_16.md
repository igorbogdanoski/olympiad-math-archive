---
grade: 9
field: geometry
difficulty: 5
source: "<натпревар / списание / година>"
problem_id: sigma_adv_16
language_original: <mk | en | sr | hr | ...>
translated: false

# 
tags:
  - trigonometry
  - vectors
  - angle_chasing
  - geometry
  - complex_numbers
  - algebra
  - triangle_geometry
  - similarity
related_skills:
  - trigonometry
  - vectors
  - angle_chasing
  - complex_numbers
  - triangle_geometry
  - similarity--- GEOMETRY SKILLS ---
geometry_style: synthetic # synthetic | analytic | mixed
primary_skill: <main_tool> # e.g., angle_chasing, similarity, cyclic_quads
related_skills:
  - angle_bisector_length
  - trigonometry

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

# Должина на симетрала на агол

## Текст на задачата
Во $\triangle ABC$ дадени се страните $AB=9$, $AC=12$ и аголот $\angle A=120^\circ$. Симетралата на аголот $A$ ја сече страната $BC$ во точката $D$. Одреди ја должината на отсечката $AD$.

## 📐 Скица / Конструкција
<Опис на цртежот. Кои се клучните точки? Дали има помошни линии?>

## 🧠 Анализа
Користи го методот на плоштини: $P_{ABC} = P_{ABD} + P_{ACD}$. Плоштината пресметај ја преку формула со синус: $P = \frac{1}{2}xy \sin \alpha$.

## 📝 Решение (СИНТЕТИЧКО)
Нека $AD = x$. Бидејќи $AD$ е симетрала на $\angle A = 120^\circ$, важи $\angle BAD = \angle CAD = 60^\circ$.

1. **Плоштина на $\triangle ABC$:**
   $$ P = \frac{1}{2} AB \cdot AC \cdot \sin 120^\circ = \frac{1}{2} \cdot 9 \cdot 12 \cdot \frac{\sqrt{3}}{2} = 27\sqrt{3} $$

2. **Збир на плоштини:**
   $$ P_{ABD} = \frac{1}{2} AB \cdot AD \cdot \sin 60^\circ = \frac{1}{2} \cdot 9 \cdot x \cdot \frac{\sqrt{3}}{2} = \frac{9x\sqrt{3}}{4} $$
   $$ P_{ACD} = \frac{1}{2} AC \cdot AD \cdot \sin 60^\circ = \frac{1}{2} \cdot 12 \cdot x \cdot \frac{\sqrt{3}}{2} = \frac{12x\sqrt{3}}{4} = 3x\sqrt{3} $$

3. **Равенка:**
   $$ P = P_{ABD} + P_{ACD} $$
   $$ 27\sqrt{3} = \frac{9x\sqrt{3}}{4} + 3x\sqrt{3} $$
   Делиме со $\sqrt{3}$:
   $$ 27 = \frac{9x}{4} + 3x $$
   Множиме со 4:
   $$ 108 = 9x + 12x $$
   $$ 108 = 21x $$
   $$ x = \frac{108}{21} = \frac{36}{7} $$

**Резултат:** $AD = \frac{36}{7}$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
<Краен резултат.>