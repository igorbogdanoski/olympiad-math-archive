---
difficulty: 3
field: number_theory
grade: 12
language_original: mk
prerequisites:
- legendre_formula
primary_skill: counting
problem_id: 2024_mun_y4_2b
problem_type: calculation
related_skills:
- logic
related_theorems:
- floor_function
source: Municipal_Competition_2024
tags:
- legendre_formula
- factorials
- divisibility
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: counting](../../skill_guides/counting.md)

# Експоненти во факториел

## 📝 Текст на задачата
Нека $x$ и $y$ се природни броеви така што $\frac{2024!}{7^x \cdot 11^y}$ е цел број. Која е најголемата можна вредност на збирот $x+y$?

## 🧠 Анализа (Клучна идеја)
Користете ја Лежандровата формула за да го најдете најголемиот степен на прост број $p$ што го дели $n!$: $E_p(n!) = \sum_{k=1}^{\infty} \lfloor \frac{n}{p^k} \rfloor$. Пресметајте го ова за $p=7$ и $p=11$.

## 💡 Решение

??? tip "Чекор 1: Експонент на 7 во 2024!"
    $$ E_7(2024!) = \lfloor \frac{2024}{7} \rfloor + \lfloor \frac{2024}{49} \rfloor + \lfloor \frac{2024}{343} \rfloor + \lfloor \frac{2024}{2401} \rfloor $$
    $$ = 289 + 41 + 5 + 0 = 335 $$
    Значи, максималното $x$ е 335.

??? tip "Чекор 2: Експонент на 11 во 2024!"
    $$ E_{11}(2024!) = \lfloor \frac{2024}{11} \rfloor + \lfloor \frac{2024}{121} \rfloor + \lfloor \frac{2024}{1331} \rfloor $$
    $$ = 184 + 16 + 1 = 201 $$
    Значи, максималното $y$ е 201.

??? tip "Чекор 3: Збир"
    $$ x + y = 335 + 201 = 536 $$
    
    Одговор: 536.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Лежандровата формула е стандардна алатка за вакви задачи. Внимавајте на делењето (само цел дел).