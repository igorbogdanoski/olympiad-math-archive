---
difficulty: 3
field: algebra
grade: 10
language_original: mk
prerequisites:
- algebraic_identities
primary_skill: vieta_formulas
problem_id: 2022_mun_y2_7a
problem_type: calculation
related_skills:
- logic
related_theorems:
- vieta_formulas
source: Municipal_Competition_2022
tags:
- quadratic_equation
- vieta_formulas
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: vieta_formulas](../../skill_guides/vieta_formulas.md)

# Збир на кубови на решенија

## 📝 Текст на задачата
Колку е апсолутната вредност на збирот на третите степени на решенијата на равенката $x^2 - 2x + 5 = 0$?

## 🧠 Анализа (Клучна идеја)
Не ги барај решенијата (тие се комплексни). Користи Виетови формули: $x_1+x_2=2, x_1x_2=5$ и идентитетот $x_1^3+x_2^3 = (x_1+x_2)((x_1+x_2)^2 - 3x_1x_2)$.

## 💡 Решение

??? success "👀 Прикажи го решението"
    Равенката е $x^2 - 2x + 5 = 0$.
    Според Виетовите формули:
    - $x_1 + x_2 = -\frac{b}{a} = 2$
    - $x_1 \cdot x_2 = \frac{c}{a} = 5$
    
    Бараме $|x_1^3 + x_2^3|$.
    Користиме алгебарски идентитет:
    $$ x_1^3 + x_2^3 = (x_1 + x_2)^3 - 3x_1x_2(x_1 + x_2) $$
    
    Заменуваме:
    $$ x_1^3 + x_2^3 = (2)^3 - 3(5)(2) $$
    $$ = 8 - 30 $$
    $$ = -22 $$
    
    Апсолутната вредност е:
    $$ |-22| = 22 $$
    
    **Одговор:** 22.

## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Ова е класичен пример каде решенијата не се реални, но симетричните изрази од нив се реални броеви.