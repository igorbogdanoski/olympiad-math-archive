---
difficulty: 3
field: algebra
grade: 9
language_original: mk
prerequisites:
- functions
- sum_formula
primary_skill: pattern_recognition
problem_id: 2022_mun_y1_4b
problem_type: calculation
related_skills:
- logic
related_theorems:
- probability
source: Municipal_Competition_2022
tags:
- functions
- summation
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: pattern_recognition](../../skill_guides/pattern_recognition.md)

# Збир на вредности на функција

## 📝 Текст на задачата
Дадена е функцијата $f(x) = x+1$. Колку изнесува вредноста на изразот $f(0) + f(1) + f(2) + \dots + f(2021)$?

## 🧠 Анализа (Клучна идеја)
Ова е збир на аритметичка прогресија. $f(0)=1, f(1)=2, \dots, f(2021)=2022$.

## 💡 Решение

??? tip "Чекор 1: Пресметка на членовите"
    $f(0) = 1$
    $f(1) = 2$
    ...
    $f(2021) = 2022$

??? tip "Чекор 2: Сумирање"
    Бараме $S = 1 + 2 + \dots + 2022$.
    Бројот на членови е $n=2022$.
    $$ S = \frac{n(n+1)}{2} = \frac{2022 \cdot 2023}{2} = 1011 \cdot 2023 $$

??? tip "Чекор 3: Пресметка"
    $1011 \cdot 2023 = 2045253$.
    (Во понудените одговори во оригиналниот тест веројатно имало печатна грешка или 'Ниеден од понудените', но точната математичка вредност е оваа).
    
    **Одговор:** 2045253.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Внимавајте на бројот на членови (од 0 до 2021 има 2022 члена).