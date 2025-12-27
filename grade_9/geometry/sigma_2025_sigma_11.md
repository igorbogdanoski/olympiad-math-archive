---
grade: 9
field: geometry
difficulty: 6
source: "<натпревар / списание / година>"
problem_id: sigma_11
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
  - rotation
  - pythagorean_theorem

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

# Геометрија на хипотенуза (Ротација)

## Текст на задачата
Во рамнокрак правоаголен $\triangle ABC$ ($\angle C=90^\circ$), $M$ и $N$ се точки на хипотенузата такви што $\angle MCN=45^\circ$. Ако $AM=a, MN=b, NB=c$, докажи дека $a^2 + c^2 = b^2$.

## 📐 Скица / Конструкција
<Опис на цртежот. Кои се клучните точки? Дали има помошни линии?>

## 🧠 Анализа
Ротирај го $\triangle ACM$ околу темето $C$ за $90^\circ$. Точката $A$ ќе отиде во $B$, а $M$ во $M'$. Ќе добиеш правоаголен триаголник со катети $a$ и $c$.

## 📝 Решение (СИНТЕТИЧКО)
Ротираме $\triangle ACM$ околу $C$ за $90^\circ$ (така што $CA$ се поклопува со $CB$).
Нека сликата на $M$ е $M'$.

1. **Својства на ротацијата:**
   - $CM = CM'$.
   - $AM = BM' = a$.
   - $\angle MCM' = 90^\circ$.

2. **Анализа на $\triangle M'CN$:**
   - $\angle M'CB = \angle MCA$ (од ротацијата).
   - $\angle M'CN = \angle M'CB + \angle BCN = \angle MCA + \angle BCN$.
   - Знаеме дека $\angle ACB = 90^\circ$ и $\angle MCN = 45^\circ$.
   - Значи $\angle MCA + \angle BCN = 90 - 45 = 45^\circ$.
   - Заклучок: $\angle M'CN = 45^\circ$.

3. **Складност:**
   Споредуваме $\triangle MCN$ и $\triangle M'CN$:
   - $CM = CM'$.
   - $CN$ е заедничка.
   - $\angle MCN = \angle M'CN = 45^\circ$.
   - Следи $\triangle MCN \cong \triangle M'CN$ (САС).
   - Од складноста: $MN = M'N = b$.

4. **Питагорова теорема:**
   Во $\triangle M'BN$:
   - $\angle M'BN = \angle M'BC + \angle CBN$. Од ротацијата $\angle M'BC = \angle MAC = 45^\circ$.
   - $\angle CBN = 45^\circ$ (агол на основата).
   - Значи $\angle M'BN = 45+45=90^\circ$.
   - Триаголникот е правоаголен со катети $BM'=a$ и $BN=c$, и хипотенуза $M'N=b$.
   - Важи: $a^2 + c^2 = b^2$.

**Заклучок:** Докажано.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
<Краен резултат.>