---
difficulty: 4
field: algebra
grade: 12
language_original: mk
prerequisites:
- basic_math
primary_skill: logic
problem_id: 2025_mun_y4_2a
problem_type: calculation
related_skills:
- logic
related_theorems:
- trigonometric_identities
source: Municipal_Competition_2025
tags:
- sequences
- trigonometry
- recursion
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: logic](../../skill_guides/logic.md)

# Низа со тригонометриска смена

## 📝 Текст на задачата
Низата $a_n$ е зададена со $a_1 = \frac{1}{2}$ и $a_{n+1} = \sqrt{\frac{1 - \sqrt{1-a_n^2}}{2}}$. Одреди ја формулата за општиот член $a_n$.

## 🧠 Анализа (Клучна идеја)
Изразот $\sqrt{1-a^2}$ вика „синус/косинус“! Ако $a_n = \sin \alpha$, тогаш $\sqrt{1-a_n^2} = \cos \alpha$. Рекурентната врска станува $a_{n+1} = \sqrt{\frac{1-\cos \alpha}{2}} = \sin(\frac{\alpha}{2})$. Ова е формула за половина агол.

## 💡 Решение

??? tip "Чекор 1: Тригонометриска форма на $a_1$"
    Дадено е $a_1 = \frac{1}{2}$. Знаеме дека $\sin(30^\circ) = \sin(\frac{\pi}{6}) = \frac{1}{2}$.
    Нека $a_1 = \sin(\frac{\pi}{6})$.

??? tip "Чекор 2: Анализа на рекурзијата"
    Нека $a_n = \sin(x_n)$ за некој агол $x_n \in (0, \pi/2)$.
    
    $$ a_{n+1} = \sqrt{\frac{1 - \sqrt{1-\sin^2 x_n}}{2}} = \sqrt{\frac{1 - \cos x_n}{2}} $$
    
    Користиме формула за половина агол: $\sin^2(\frac{\alpha}{2}) = \frac{1-\cos \alpha}{2}$.
    
    $$ a_{n+1} = \sqrt{\sin^2(\frac{x_n}{2})} = \sin(\frac{x_n}{2}) $$

??? tip "Чекор 3: Општ член"
    Аголот се преполовува во секој чекор.
    $x_1 = \frac{\pi}{6}$
    $x_2 = \frac{\pi}{12}$
    $x_3 = \frac{\pi}{24}$
    ...
    $x_n = \frac{\pi}{6 \cdot 2^{n-1}} = \frac{\pi}{3 \cdot 2^n}$
    
    Значи, $a_n = \sin \left( \frac{\pi}{3 \cdot 2^n} \right)$.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Ова е стандардна техника за низи кои личат на тригонометриски идентитети. Проверете дали аголот останува во првиот квадрант (за да важи коренувањето).