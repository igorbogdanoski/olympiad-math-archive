---
difficulty: 4
field: number_theory
grade: 12
language_original: mk
prerequisites:
- legendre_formula
primary_skill: prime_factorization
problem_id: 2022_mun_y4_13a
problem_type: calculation
related_skills:
- logic
related_theorems:
- number_theory
source: Municipal_Competition_2022
tags:
- factorials
- divisors
- cubes
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: prime_factorization](../../skill_guides/prime_factorization.md)

# Кубови делители на факториели

## 📝 Текст на задачата
Колку точни кубови на природни броеви се делители на бројот $N = 3! \cdot 5! \cdot 7!$?

## 🧠 Анализа (Клучна идеја)
Најди ја простата факторизација на $N$. За бројот да биде куб, степените на простите множители мора да бидат деливи со 3.

## 💡 Решение

??? tip "Чекор 1: Факторизација"
    $3! = 2 \cdot 3$
    $5! = 2^3 \cdot 3 \cdot 5$
    $7! = 2^4 \cdot 3^2 \cdot 5 \cdot 7$
    
    Множиме сè:
    $N = (2^1 \cdot 3^1) \cdot (2^3 \cdot 3^1 \cdot 5^1) \cdot (2^4 \cdot 3^2 \cdot 5^1 \cdot 7^1)$
    $N = 2^{1+3+4} \cdot 3^{1+1+2} \cdot 5^{1+1} \cdot 7^1$
    $N = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7^1$

??? tip "Чекор 2: Броење кубови"
    Делител $d = 2^a 3^b 5^c 7^d$ е куб ако $a,b,c,d$ се деливи со 3.
    Ограничувања:
    - $0 \le a \le 8$. Деливи со 3: $\{0, 3, 6\}$ (3 опции).
    - $0 \le b \le 4$. Деливи со 3: $\{0, 3\}$ (2 опции).
    - $0 \le c \le 2$. Деливи со 3: $\{0\}$ (1 опција).
    - $0 \le d \le 1$. Деливи со 3: $\{0\}$ (1 опција).

??? tip "Чекор 3: Вкупно комбинации"
    $$ 3 \cdot 2 \cdot 1 \cdot 1 = 6 $$
    
    **Одговор:** 6.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
За да биде $n^k$ полн куб, $k$ мора да е содржател на 3.