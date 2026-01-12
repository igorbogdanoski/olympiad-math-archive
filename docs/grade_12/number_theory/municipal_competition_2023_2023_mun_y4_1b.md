---
difficulty: 3
field: number_theory
grade: 12
language_original: mk
prerequisites:
- legendre_formula
primary_skill: algebraic_manipulation
problem_id: 2023_mun_y4_1b
problem_type: calculation
related_skills:
- logic
related_theorems:
- floor_function
source: Municipal_Competition_2023
tags:
- factorials
- divisibility
- legendre_formula
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: algebraic_manipulation](../../skill_guides/algebraic_manipulation.md)

# Деливост на факториели

## 📝 Текст на задачата
Најди ја најголемата вредност на природниот број $n$ за кој што $25! + 26!$ е делив со $3^n$.

## 🧠 Анализа (Клучна идеја)
Факторизирајте го изразот! $25! + 26! = 25!(1 + 26) = 25! \cdot 27 = 25! \cdot 3^3$. Сега задачата се сведува на наоѓање на експонентот на 3 во $25!$ (Лежандрова формула) и додавање на 3.

## 💡 Решение

??? tip "Чекор 1: Факторизација"
    $$ S = 25! + 26! = 25!(1 + 26) = 25! \cdot 27 = 25! \cdot 3^3 $$

??? tip "Чекор 2: Лежандрова формула за 25!"
    Бараме $E_3(25!) = \lfloor \frac{25}{3} \rfloor + \lfloor \frac{25}{9} \rfloor + \lfloor \frac{25}{27} \rfloor$.
    $$ E_3(25!) = 8 + 2 + 0 = 10 $$

??? tip "Чекор 3: Вкупен експонент"
    Вкупниот степен на 3 во $S$ е:
    $$ n = E_3(25!) + 3 = 10 + 3 = 13 $$
    
    Одговор: $n=13$.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Никогаш не пресметувајте факториели! Секогаш барајте заеднички множител.