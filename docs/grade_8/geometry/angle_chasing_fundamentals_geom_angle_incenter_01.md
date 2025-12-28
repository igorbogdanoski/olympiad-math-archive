---
grade: 8
field: geometry
difficulty: 4
source: "<натпревар / списание / година>"
problem_id: geom_angle_incenter_01
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
  - angle_bisectors
  - algebraic_substitution

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

# Агол кај центарот на впишана кружница

## Текст на задачата
Нека $I$ е центарот на впишаната кружница во триаголникот $ABC$. Докажи дека аголот меѓу симетралите на аглите кај темињата $A$ и $B$ изнесува: $$\angle AIB = 90^\circ + \frac{\gamma}{2}$$ каде $\gamma$ е аголот кај темето $C$.

## 📐 Скица / Конструкција
<Опис на цртежот. Кои се клучните точки? Дали има помошни линии?>


![Визуелизација](../../assets/images/geom_angle_incenter_01.png)

## 🧠 Анализа
Клучот не е во наоѓање на поединечните агли $\alpha$ и $\beta$, туку во изразување на нивниот збир преку третиот агол $\gamma$.

## 📝 Решение (СИНТЕТИЧКО)
1. **Дефиниција:** Точката $I$ е пресек на симетралите, па во $\triangle AIB$ аглите се $\frac{\alpha}{2}$ и $\frac{\beta}{2}$. 
2. **Сума во $\triangle AIB$:** $\angle AIB = 180^\circ - (\frac{\alpha}{2} + \frac{\beta}{2}) = 180^\circ - \frac{\alpha + \beta}{2}$. 
3. **Врска со $\triangle ABC$:** Знаеме дека $\alpha + \beta = 180^\circ - \gamma$. 
4. **Замена:** $\angle AIB = 180^\circ - \frac{180^\circ - \gamma}{2} = 180^\circ - (90^\circ - \frac{\gamma}{2})$. 
5. **Резултат:** $\angle AIB = 90^\circ + \frac{\gamma}{2}$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
<Краен резултат.>