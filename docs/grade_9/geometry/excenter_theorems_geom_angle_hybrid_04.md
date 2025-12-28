---
grade: 9
field: geometry
difficulty: 6
source: "<натпревар / списание / година>"
problem_id: geom_angle_hybrid_04
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
  - external_bisectors
  - interior_bisectors

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

# Агол меѓу внатрешна и надворешна симетрала

## Текст на задачата
Во триаголникот $ABC$, нека $AY$ е симетрала на внатрешниот агол кај $A$, а $BY$ е симетрала на надворешниот агол кај $B$. Докажи дека тие се сечат под агол: $$\angle AYB = \frac{\gamma}{2}$$

## 📐 Скица / Конструкција
<Опис на цртежот. Кои се клучните точки? Дали има помошни линии?>


![Визуелизација](../../assets/images/geom_angle_hybrid_04.png)

## 🧠 Анализа
Користи ја теоремата за надворешен агол во $\triangle ABY$.

## 📝 Решение (СИНТЕТИЧКО)
1. **Агли во $\triangle ABY$:** $\angle YAB = \frac{\alpha}{2}$. 
2. **Агол кај $B$:** Надворешниот агол кај $B$ во $\triangle ABC$ е $\alpha + \gamma$. Неговата половина е $\angle YBC = \frac{\alpha + \gamma}{2}$. 
3. **Надворешен агол во $\triangle ABY$:** Аголот $\angle YBC$ е надворешен за $\triangle ABY$, па $\angle YBC = \angle YAB + \angle AYB$. 
4. **Замена:** $\frac{\alpha + \gamma}{2} = \frac{\alpha}{2} + \angle AYB$. 
5. **Резултат:** $\angle AYB = \frac{\gamma}{2}$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
<Краен резултат.>