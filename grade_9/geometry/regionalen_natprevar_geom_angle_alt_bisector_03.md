---
grade: 9
field: geometry
difficulty: 5
source: "<натпревар / списание / година>"
problem_id: geom_angle_alt_bisector_03
language_original: <mk | en | sr | hr | ...>
translated: false

# --- GEOMETRY SKILLS ---
geometry_style: synthetic # synthetic | analytic | mixed
primary_skill: <main_tool> # e.g., angle_chasing, similarity, cyclic_quads
related_skills:
  - altitudes
  - angle_bisectors

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

# Агол меѓу висина и симетрала

## Текст на задачата
Во триаголник $ABC$ каде $AB < AC$, нека $AD$ е висината, а $AS$ е симетралата на аголот повлечени од темето $A$. Докажи дека аголот меѓу нив е: $$\angle DAS = \frac{\beta - \gamma}{2}$$

## 📐 Скица / Конструкција
<Опис на цртежот. Кои се клучните точки? Дали има помошни линии?>


<!-- VISUAL PROMPT: Draw triangle ABC with AC significantly longer than AB. Draw altitude AD from A to BC. Draw internal angle bisector AS from A to BC. Label angle B as beta and angle C as gamma. -->

## 🧠 Анализа
Пресметај ги аглите $\angle BAS$ и $\angle BAD$ одделно преку $\alpha, \beta, \gamma$ и најди ја нивната разлика.

## 📝 Решение (СИНТЕТИЧКО)
1. **Симетрала:** $\angle BAS = \frac{\alpha}{2}$. Бидејќи $\alpha = 180 - (\beta + \gamma)$, тогаш $\angle BAS = 90 - \frac{\beta + \gamma}{2}$. 
2. **Висина:** Во правоаголниот $\triangle ABD$, $\angle BAD = 90 - \beta$. 
3. **Одземање:** $\angle DAS = \angle BAS - \angle BAD$. 
4. **Алгебра:** $\angle DAS = (90 - \frac{\beta}{2} - \frac{\gamma}{2}) - (90 - \beta) = \beta - \frac{\beta}{2} - \frac{\gamma}{2}$. 
5. **Финале:** $\angle DAS = \frac{\beta - \gamma}{2}$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
<Краен резултат.>