---
grade: 9
field: geometry
difficulty: 8
source: "<натпревар / списание / година>"
problem_id: geom_9_tri_angle_45_60
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
  - trigonometric_ratios
  - angle_chasing

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

# Пресметка на агли преку поделба на страна

## Текст на задачата
Нека $D$ е точка на страната $BC$ од $\triangle ABC$, така што $2\cdot BD = DC$. Определи ги аглите во $\triangle ABC$, ако $\angle ABC=45^\circ$ и $\angle ADC=60^\circ$.

## 📐 Скица / Конструкција
<Опис на цртежот. Кои се клучните точки? Дали има помошни линии?>


<!-- VISUAL PROMPT: Draw triangle ABC. On side BC, mark point D such that the length DC is twice the length of BD. Label angle B as 45 degrees and angle ADC as 60 degrees. Drop altitude AH. -->

## 🧠 Анализа
Спушти висина $AH$ и изрази ги сите делови на основата преку висината $h$. Побарај го аголот чиј тангенс е $2+\sqrt{3}$ или $2-\sqrt{3}$.

## 📝 Решение (СИНТЕТИЧКО)
1. **Конструкција:** Спуштаме висина $AH=h$. Во $\triangle ABH$, $BH=h$ (бидејќи $\angle B=45^\circ$). Во $\triangle ADH$, $DH = h/\sqrt{3}$.
2. **Метрика:** $BD = BH - DH = h(1 - 1/\sqrt{3})$. Од условот $DC = 2BD = 2h(1 - 1/\sqrt{3})$.
3. **Агол C:** $HC = DC - DH = 2h - 2h/\sqrt{3} - h/\sqrt{3} = h(2-\sqrt{3})$. Во $\triangle AHC$, $\tan C = AH/HC = 1/(2-\sqrt{3}) = 2+\sqrt{3}$.
4. **Резултат:** Вредноста $\tan 75^\circ = 2+\sqrt{3}$. Значи $\angle C = 75^\circ$.
5. **Финале:** $\angle A = 180^\circ - (45^\circ + 75^\circ) = 60^\circ$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
<Краен резултат.>