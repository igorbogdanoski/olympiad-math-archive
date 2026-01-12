---
difficulty: 2
field: algebra
grade: 7
language_original: mk
prerequisites:
- fraction_decimal_conversion
primary_skill: calculation
problem_id: 2022_mun_g7_11
problem_type: calculation
related_skills:
- logic
related_theorems:
- number_theory
source: Municipal_Competition_2022
tags:
- decimals
- fractions
- order_of_operations
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: calculation](../../skill_guides/calculation.md)

# Броен израз со децимали

## 📝 Текст на задачата
Колку е вредноста на бројниот израз $0.8 + \left(\frac{1}{2} + 1.25\right) : 1\frac{3}{4} - 1 + 1\frac{1}{5}$?

## 🧠 Анализа (Клучна идеја)
Најлесно е сè да се претвори во децимални броеви, бидејќи именителите се 2, 4, 5 (сите се делители на 10 или 100). $1/2 = 0.5$, $3/4 = 0.75$, $1/5 = 0.2$.

## 💡 Решение

??? tip "Чекор 1: Претворање во децимални броеви"
    $\frac{1}{2} = 0.5$
    $1\frac{3}{4} = 1.75$
    $1\frac{1}{5} = 1.2$

??? tip "Чекор 2: Замена во изразот"
    $$ 0.8 + (0.5 + 1.25) : 1.75 - 1 + 1.2 $$

??? tip "Чекор 3: Заграда и делење"
    Заградата: $0.5 + 1.25 = 1.75$.
    Делењето: $1.75 : 1.75 = 1$.

??? tip "Чекор 4: Собирање и одземање"
    $$ 0.8 + 1 - 1 + 1.2 $$
    $$ 0.8 + 1.2 = 2 $$
    
    Одговор: 2.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Кога имаме мешани броеви и децимали, обично децималите се побрзи ако нема периодични броеви (како 1/3).