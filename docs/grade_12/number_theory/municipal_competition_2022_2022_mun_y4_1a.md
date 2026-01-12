---
difficulty: 3
field: number_theory
grade: 12
language_original: mk
prerequisites:
- arithmetic_progression_sum
primary_skill: algebraic_modeling
problem_id: 2022_mun_y4_1a
problem_type: calculation
related_skills:
- logic
related_theorems:
- number_theory
source: Municipal_Competition_2022
tags:
- arithmetic_progression
- sum
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: algebraic_modeling](../../skill_guides/algebraic_modeling.md)

# Збир на последователни броеви

## 📝 Текст на задачата
Ако збирот на $k$ последователни природни броеви е 45, која е најголемата можна вредност на $k$?

## 🧠 Анализа (Клучна идеја)
Збирот на аритметичка прогресија е $S = \frac{k}{2}(2a + k - 1)$. Замени $S=45$ и анализирај ги делителите на 90.

## 💡 Решение

??? success "👀 Прикажи го решението"
    Нека првиот број во низата е $a$ ($a \ge 1$).
    Збирот на $k$ последователни броеви е:
    $$ S = a + (a+1) + \dots + (a+k-1) = ka + \frac{k(k-1)}{2} $$
    Дадено е $S = 45$:
    $$ ka + \frac{k(k-1)}{2} = 45 $$
    Множиме со 2:
    $$ 2ka + k(k-1) = 90 $$
    $$ k(2a + k - 1) = 90 $$
    
    Бидејќи $a \ge 1$, тогаш $2a + k - 1 > k$. (Вториот множител е поголем од првиот).
    Бараме делители на 90: $1, 2, 3, 5, 6, 9, 10, 15, \dots$
    
    Проверуваме за најголемите можни вредности на $k$ (каде $k < \sqrt{90} \approx 9.4$ не мора да важи, но $k$ мора да е помалиот множител).
    
    1.  Ако $k=9$: $9(2a + 8) = 90 \implies 2a + 8 = 10 \implies 2a = 2 \implies a = 1$.
        Низата е $1, 2, 3, 4, 5, 6, 7, 8, 9$. Збир 45. Ова е валидно.
    2.  Ако $k=10$: $10(2a + 9) = 90 \implies 2a + 9 = 9 \implies 2a = 0$. Не е природен број.
    3.  За $k > 10$, $k$ би бил поголемиот множител, што е невозможно бидејќи $2a+k-1 > k$.
    
    **Одговор:** Најголемата вредност е $k=9$.

## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Клучот е факторизацијата на равенката $k(2a+k-1)=2S$.