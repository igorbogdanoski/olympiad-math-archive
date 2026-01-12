---
difficulty: 3
field: algebra
grade: 10
language_original: mk
prerequisites:
- basic_math
primary_skill: logic
problem_id: 2025_mun_y2_2b
problem_type: calculation
related_skills:
- logic
related_theorems:
- polynomial_expansion
source: Municipal_Competition_2025
tags:
- sequences
- polynomials
- recursion
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: logic](../../skill_guides/logic.md)

# Рекурентна врска

## 📝 Текст на задачата
Нека $x$ е реален број за кој важи $x + \frac{1}{x} = 3$. Нека $S_m = x^m + \frac{1}{x^m}$. Одреди ја вредноста на $S_7$.

## 🧠 Анализа (Клучна идеја)
Не го барајте $x$! Користете ја рекурентната врска: $S_n = S_1 S_{n-1} - S_{n-2}$. Ова доаѓа од множењето $(x^{n-1} + 1/x^{n-1})(x + 1/x) = x^n + 1/x^n + x^{n-2} + 1/x^{n-2}$.

## 💡 Решение

??? tip "Чекор 1: Пресметка на почетните членови"
    $$ S_2 = S_1^2 - 2 = 3^2 - 2 = 7 $$
    
    $$ S_3 = 3S_2 - S_1 = 3(7) - 3 = 18 $$
    
    $$ S_4 = 3S_3 - S_2 = 3(18) - 7 = 54 - 7 = 47 $$

??? tip "Чекор 2: Стратегија за $S_7$"
    Можеме да продолжиме чекор по чекор, или да искористиме $S_7 = S_3 S_4 - S_1$ (бидејќи $3+4=7$).
    
    $$ (x^3 + \frac{1}{x^3})(x^4 + \frac{1}{x^4}) = x^7 + \frac{1}{x^7} + x + \frac{1}{x} = S_7 + S_1 $$

??? tip "Чекор 3: Пресметка"
    $$ S_7 = S_3 \cdot S_4 - S_1 $$
    
    $$ S_7 = 18 \cdot 47 - 3 $$
    
    $$ S_7 = 846 - 3 = 843 $$



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Учениците треба да ја препознаат шемата: $S_n$ секогаш се добива од претходните. Ова е поврзано со Чебишеви полиноми.