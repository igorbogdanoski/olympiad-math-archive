---
difficulty: 4
field: algebra
grade: 12
language_original: mk
prerequisites:
- functions
primary_skill: substitution
problem_id: 2023_mun_y4_2a
problem_type: proof
related_skills:
- logic
related_theorems:
- functions
source: Municipal_Competition_2023
tags:
- functional_equation
- proof
- contradiction
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: substitution](../../skill_guides/substitution.md)

# Функционална равенка

## 📝 Текст на задачата
Најди ги сите функции $f: \mathbb{R} \to \mathbb{R}$ за кои важи $f(1)=1$ и $f(x+y) = 3y f(x) + 2x f(y)$ за сите реални $x, y$.

## 🧠 Анализа (Клучна идеја)
Обидете се да замените конкретни вредности. На пример $x=0, y=0$ за да најдете $f(0)$. Потоа $x=1, y=0$. Ова ќе ве доведе до контрадикција.

## 💡 Решение

??? tip "Чекор 1: Наоѓање на $f(0)$"
    Ставаме $x=0, y=0$:
    $$ f(0) = 3(0)f(0) + 2(0)f(0) = 0 $$
    Значи $f(0) = 0$.

??? tip "Чекор 2: Контрадикција"
    Ставаме $x=1, y=0$:
    $$ f(1+0) = 3(0)f(1) + 2(1)f(0) $$
    $$ f(1) = 0 + 2(0) = 0 $$
    
    Но, во задачата е дадено $f(1) = 1$.
    Добивме $1 = 0$, што е невозможно.
    
    **Заклучок:**
    Не постои таква функција.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Ова е пример за задача каде што решението е „празно множество“. Учениците често мислат дека мора да најдат формула и се вртат во круг.