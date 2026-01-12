---
difficulty: 3
field: trigonometry
grade: 11
language_original: mk
prerequisites:
- basic_math
primary_skill: logic
problem_id: 2025_mun_y3_2ab
problem_type: proof
related_skills:
- logic
related_theorems:
- complex_numbers
source: Municipal_Competition_2025
tags:
- trigonometric_identities
- algebraic_manipulation
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: logic](../../skill_guides/logic.md)

# Тригонометриски идентитет

## 📝 Текст на задачата
Докажи дека ако $\sin x + \cos x = \sqrt{3}$, тогаш $\text{tg } x + \text{ctg } x = 1$.

## 🧠 Анализа (Клучна идеја)
Изразете го бараното ($\text{tg } x + \text{ctg } x$) преку синус и косинус. Ќе добиете $\frac{1}{\sin x \cos x}$. Значи, целта е да го најдете производот $\sin x \cos x$. Тоа најлесно се прави со квадрирање на даденото равенство.

## 💡 Решение

??? tip "Чекор 1: Анализа на целта"
    Бараме вредност за:
    
    $$ \text{tg } x + \text{ctg } x = \frac{\sin x}{\cos x} + \frac{\cos x}{\sin x} = \frac{\sin^2 x + \cos^2 x}{\sin x \cos x} = \frac{1}{\sin x \cos x} $$

??? tip "Чекор 2: Квадрирање на условот"
    Дадено е $\sin x + \cos x = \sqrt{3}$. Квадрираме:
    
    $$ (\sin x + \cos x)^2 = (\sqrt{3})^2 $$
    
    $$ \sin^2 x + 2\sin x \cos x + \cos^2 x = 3 $$
    
    Користиме $\sin^2 x + \cos^2 x = 1$:
    
    $$ 1 + 2\sin x \cos x = 3 $$
    
    $$ 2\sin x \cos x = 2 \implies \sin x \cos x = 1 $$

??? tip "Чекор 3: Замена во целта"
    $$ \text{tg } x + \text{ctg } x = \frac{1}{1} = 1 $$
    
    Што и требаше да се докаже.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Важна забелешка за напредни ученици: Равенката $\sin x + \cos x = \sqrt{3}$ нема реални решенија, бидејќи максималната вредност на $\sin x + \cos x$ е $\sqrt{2}$. Сепак, во контекст на алгебарски идентитети (или комплексни броеви), импликацијата е точна.