---
difficulty: 5
field: algebra
grade: 10
language_original: mk
prerequisites:
- exponent_rules
- trig_identities
primary_skill: algebraic_substitution
problem_id: 2022_mun_y2_12b
problem_type: calculation
related_skills:
- logic
related_theorems:
- number_theory
source: Municipal_Competition_2022
tags:
- exponential_equation
- trigonometry
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: algebraic_substitution](../../skill_guides/algebraic_substitution.md)

# Експоненцијална равенка со тригонометрија

## 📝 Текст на задачата
Ако најголемата вредност на променливата $x \in (0, \pi/2]$ за која важи равенството $6 \cdot 2^{\sin^2 x} - 8 = 2^{2\cos^2 x + 2}$ е $m$, најди ја вредноста на $\frac{4m}{\pi}$.

## 🧠 Анализа (Клучна идеја)
Користи го идентитетот $\cos^2 x = 1 - \sin^2 x$. Воведи смена $y = 2^{\sin^2 x}$. Равенката ќе се сведе на квадратна равенка по $y$.

## 💡 Решение

??? tip "Чекор 1: Трансформација на равенката"
    Дадено: $6 \cdot 2^{\sin^2 x} - 8 = 2^{2\cos^2 x + 2}$.
    Експонентот на десната страна:
    $$ 2\cos^2 x + 2 = 2(1-\sin^2 x) + 2 = 2 - 2\sin^2 x + 2 = 4 - 2\sin^2 x $$
    Равенката станува:
    $$ 6 \cdot 2^{\sin^2 x} - 8 = 2^{4 - 2\sin^2 x} = \frac{2^4}{2^{2\sin^2 x}} = \frac{16}{(2^{\sin^2 x})^2} $$

??? tip "Чекор 2: Смена"
    Нека $y = 2^{\sin^2 x}$. Бидејќи $x \in (0, \pi/2]$, $\sin^2 x \in (0, 1]$, па $y \in (1, 2]$.
    $$ 6y - 8 = \frac{16}{y^2} $$
    $$ 6y^3 - 8y^2 - 16 = 0 $$
    Делиме со 2:
    $$ 3y^3 - 4y^2 - 8 = 0 $$

??? tip "Чекор 3: Решавање на кубната равенка"
    Бараме целобројни решенија (делители на 8). Пробуваме $y=2$:
    $3(2)^3 - 4(2)^2 - 8 = 24 - 16 - 8 = 0$. ✅
    Значи $y=2$ е решение.
    (Другите решенија на $3y^2 + 2y + 4 = 0$ се комплексни).

??? tip "Чекор 4: Наоѓање на $x$"
    $$ 2^{\sin^2 x} = 2^1 \implies \sin^2 x = 1 $$
    Во интервалот $(0, \pi/2]$, ова важи само за $x = \frac{\pi}{2}$.
    Значи $m = \frac{\pi}{2}$.

??? tip "Чекор 5: Пресметка на изразот"
    $$ \frac{4m}{\pi} = \frac{4(\pi/2)}{\pi} = 2 $$
    
    **Одговор:** 2.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Замената на променлива е клучна за решавање на трансцендентни равенки.