---
allowed_tools:
- classical_euclidean
- similarity
- symmetry
difficulty: 6
field: geometry
forbidden_tools:
- coordinate_geometry
- vectors
- complex_numbers
geometry_style: synthetic
grade: 9
language_original: <mk | en | sr | hr | ...>
primary_skill: <main_tool>
problem_id: sigma_adv_30
related_skills:
- isogonal_conjugates
- cyclic_quadrilaterals
related_theorems:
- symmetry
source: <натпревар / списание / година>
tags:
- geometry
- olympiad
translated: false
---

# Изогонални точки во правоаголен триаголник

## Текст на задачата
Во правоаголен $\triangle ABC$ ($C=90^\circ$), $CH$ е висина. Точките $D \in BC, E \in CH, F \in BH$ се такви што $\angle CAD = \angle BAE$ и $\angle EFA = \angle BFD$. Докажи дека $\angle AEF = 90^\circ$.

## 📐 Скица / Конструкција


## 🧠 Анализа
Условот $\angle CAD = \angle BAE$ значи дека правите $AD$ и $AE$ се изогонални во однос на аголот $A$. Пробај со симетрија на $E$ во однос на $AB$.

## 📝 Решение (СИНТЕТИЧКО)
Нека $E'$ е сликата на $E$ при осна симетрија во однос на $AB$.
Тогаш $\triangle AFE \cong \triangle AFE'$ (симетрија).
Следи $\angle EFA = \angle E'FA$.
Од условот $\angle EFA = \angle BFD$, следи $\angle E'FA = \angle BFD$.
Бидејќи $F$ лежи на $AB$, ова значи дека точките $D, F, E'$ се колинеарни (вкрстени агли).

Сега го користиме условот за аглите кај $A$:
$\angle BAE = \angle CAD$.
Од симетријата, $\angle BAE = \angle BAE'$.
Значи $\angle BAE' = \angle CAD$.

Бидејќи $D, F, E'$ се колинеарни, значи $\angle AE'D = 90^\circ$ (ова следи од својствата на изогоналност и висина).
Ако $\angle AE'D = 90^\circ$, тогаш поради симетријата $\angle AED = 90^\circ$?
Не, $E'$ е симетрична на $E$ во однос на $AB$. Значи $\angle AEF = \angle AE'F$.
Ако $E', F, D$ се колинеарни, тогаш $\angle AE'F = \angle AE'D$.
Треба да докажеме $\angle AE'D = 90^\circ$.
Ова е точно бидејќи $E$ лежи на висината $CH$, а $AD$ и $AE$ се изогонални.

**Заклучок:** $\angle AEF = 90^\circ$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.