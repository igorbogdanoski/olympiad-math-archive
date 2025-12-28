---
grade: 9
field: geometry
difficulty: 4
source: "<натпревар / списание / година>"
problem_id: num_li2_11
language_original: <mk | en | sr | hr | ...>
translated: false

# 
tags:
  - vectors
  - angle_chasing
  - geometry
  - complex_numbers
  - algebra
  - similarity
related_skills:
  - vectors
  - complex_numbers
  - angle_chasing
  - similarity--- GEOMETRY SKILLS ---
geometry_style: synthetic # synthetic | analytic | mixed
primary_skill: <main_tool> # e.g., angle_chasing, similarity, cyclic_quads
related_skills:
  - trapezoid_properties
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

# Тангенцијален трапез

## Текст на задачата
Докажи дека висината на рамнокрак тангенцијален трапез е геометриска средина на неговите основи.

## 📐 Скица / Конструкција


## 🧠 Анализа
Користи Питоова теорема: $a+b = 2c$ (каде $c$ е кракот).

## 📝 Решение (СИНТЕТИЧКО)
Нека основите се $a, b$, кракот е $c$, висината е $h$.
1. **Тангентен услов:** $a+b = 2c \implies c = \frac{a+b}{2}$.
2. **Питагора:**
   Во правоаголниот триаголник формиран од висината:
   $$ h^2 = c^2 - (\frac{a-b}{2})^2 $$
   $$ h^2 = (\frac{a+b}{2})^2 - (\frac{a-b}{2})^2 $$
   $$ h^2 = \frac{(a+b)^2 - (a-b)^2}{4} $$
   $$ h^2 = \frac{4ab}{4} = ab $$
   $$ h = \sqrt{ab} $$

**Резултат:** Висината е геометриска средина.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.