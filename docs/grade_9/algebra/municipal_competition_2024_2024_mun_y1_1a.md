---
difficulty: 3
field: algebra
grade: 9
language_original: mk
prerequisites:
- linear_equations
primary_skill: functions
problem_id: 2024_mun_y1_1a
problem_type: calculation
related_skills:
- logic
related_theorems:
- functions
source: Municipal_Competition_2024
tags:
- linear_functions
- functional_equation
- system_of_equations
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: functions](../../skill_guides/functions.md)

# Линеарна функција со параметар

## 📝 Текст на задачата
Дадена е линеарната функција $f(x) = (2a-3b)x + (a-2b)$. Ако важи $f(x-1) + f(2x+1) = 3x+1$, одреди ја вредноста на $a$ и $b$.

## 🧠 Анализа (Клучна идеја)
Заменете го аргументот во функцијата. $f(x-1)$ значи секаде каде што има $x$ да ставите $(x-1)$. Средете го изразот на левата страна до облик $Ax + B$. Потоа изедначете ги коефициентите пред $x$ и слободните членови со десната страна ($3x+1$).

## 💡 Решение

??? tip "Чекор 1: Изразување на $f(x-1)$ и $f(2x+1)$"
    Нека $k = 2a-3b$ и $n = a-2b$. Тогаш $f(x) = kx + n$.
    $$ f(x-1) = k(x-1) + n = kx - k + n $$
    $$ f(2x+1) = k(2x+1) + n = 2kx + k + n $$

??? tip "Чекор 2: Збир на функциите"
    $$ f(x-1) + f(2x+1) = (kx - k + n) + (2kx + k + n) $$
    $$ = 3kx + 2n $$

??? tip "Чекор 3: Изедначување со $3x+1$"
    $$ 3kx + 2n = 3x + 1 $$
    Следи:
    1. $3k = 3 \implies k = 1$
    2. $2n = 1 \implies n = 1/2$

??? tip "Чекор 4: Систем за $a$ и $b$"
    Враќаме во замените:
    1. $2a - 3b = 1$
    2. $a - 2b = 1/2 \implies 2a - 4b = 1$
    
    Одземаме (2) од (1):
    $$ (2a - 3b) - (2a - 4b) = 1 - 1 $$
    $$ b = 0 $$
    
    Заменуваме во (1):
    $$ 2a - 0 = 1 \implies a = 1/2 $$
    
    Одговор: $a=1/2, b=0$.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Замената $k$ и $n$ на почетокот драстично го поедноставува пишувањето и ја намалува шансата за грешка во алгебрата.