---
grade: 8
field: geometry
difficulty: 4
source: "<натпревар / списание / година>"
problem_id: geom_angle_orthocenter_02
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
  - orthocenter
  - cyclic_quadrilaterals

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

# Агол кај ортоцентарот

## Текст на задачата
Нека $H$ е ортоцентарот (пресекот на висините) во триаголникот $ABC$. Докажи дека аголот меѓу висините повлечени од темињата $A$ и $B$ е суплементен на аголот кај темето $C$: $$\angle AHB = 180^\circ - \gamma$$

## 📐 Скица / Конструкција

![Orthocenter Angle](images/geom_angle_orthocenter_02.png)

## 💡 Решение

Нека $AD$ и $BE$ се висините спуштени од темињата $A$ и $B$ кон страните $BC$ и $AC$ соодветно.
Нивниот пресек е ортоцентарот $H$.
Бидејќи $AD \perp BC$ и $BE \perp AC$, аглите $\angle ADC$ и $\angle BEC$ се прави ($90^\circ$).
Да го разгледаме четириаголникот $CDHE$.
Аглите кај темињата $D$ и $E$ се $90^\circ$.
Збирот на аглите во четириаголник е $360^\circ$.
$$ \angle C + \angle CDH + \angle DHE + \angle HEC = 360^\circ $$
$$ \gamma + 90^\circ + \angle DHE + 90^\circ = 360^\circ $$
$$ \gamma + 180^\circ + \angle DHE = 360^\circ $$
$$ \angle DHE = 180^\circ - \gamma $$
Аголот $\angle AHB$ и аголот $\angle DHE$ се накрстни агли, па тие се еднакви.
$$ \angle AHB = \angle DHE $$
Следствено:
$$ \angle AHB = 180^\circ - \gamma $$
Што требаше да се докаже.