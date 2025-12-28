---
grade: 10
field: algebra
difficulty: 5
problem_type: calculation
source: "Municipal_Competition_2022"
problem_id: 2022_mun_y2_15b
language_original: mk
translated: false

# --- SKILL MAPPING ---
primary_skill: algebraic_identities
related_skills:
  - logic
prerequisites:
  - trig_identities

# --- TOPICS ---
tags:
  - trigonometry
  - system_of_equations
  - olympiad
---

[⬅️ Назад кон Индексот](../../README.md) | [🧰 Skill: algebraic_identities](../../../tools/skill_guides/algebraic_identities.md)

# Тригонометриски систем

## 📝 Текст на задачата
Да се определи вредноста на изразот $5\sin\theta - 3\cos\theta$ ако се знае дека $3\sin\theta + 5\cos\theta = 5$ и $0 < \theta < \frac{\pi}{2}$.

## 🧠 Анализа (Клучна идеја)
Нека бараниот израз е $x$. Квадрирај ги двата изрази и собери ги. Ќе добиеш $(3^2+5^2)(\sin^2+\cos^2) = 5^2 + x^2$.

## 💡 Решение

## 💡 Решение

??? success "👀 Прикажи го решението"
    Нека $A = 3\sin\theta + 5\cos\theta = 5$.
    Нека $B = 5\sin\theta - 3\cos\theta = x$.
    
    Квадрираме:
    $$ A^2 = 9\sin^2\theta + 25\cos^2\theta + 30\sin\theta\cos\theta = 25 $$
    $$ B^2 = 25\sin^2\theta + 9\cos^2\theta - 30\sin\theta\cos\theta = x^2 $$
    
    Собираме:
    $$ A^2 + B^2 = (9+25)\sin^2\theta + (25+9)\cos^2\theta $$
    $$ 25 + x^2 = 34(\sin^2\theta + \cos^2\theta) $$
    $$ 25 + x^2 = 34 $$
    $$ x^2 = 9 $$
    $$ x = \pm 3 $$
    
    Треба да го одредиме знакот.
    Од $3\sin\theta + 5\cos\theta = 5$, бидејќи $\theta$ е остар агол ($\sin > 0$), следи $5\cos\theta < 5 \implies \cos\theta < 1$ (што е точно).
    Исто така $3\sin\theta = 5(1-\cos\theta)$.
    Бараме $x = 5\sin\theta - 3\cos\theta$.
    Заменуваме $3\sin\theta$: $x = \frac{5}{3}(3\sin\theta) - 3\cos\theta = \frac{5}{3} \cdot 5(1-\cos\theta) - 3\cos\theta = \frac{25}{3} - \frac{25}{3}\cos\theta - \frac{9}{3}\cos\theta = \frac{25 - 34\cos\theta}{3}$.
    
    Дали ова е позитивно или негативно?
    Од $3\sin\theta = 5(1-\cos\theta)$, квадрираме: $9(1-\cos^2\theta) = 25(1-\cos\theta)^2$.
    $9(1+\cos\theta)(1-\cos\theta) = 25(1-\cos\theta)^2$.
    Бидејќи $\theta \ne 0$, кратиме $(1-\cos\theta)$:
    $9(1+\cos\theta) = 25(1-\cos\theta)$
    $9 + 9\cos\theta = 25 - 25\cos\theta$
    $34\cos\theta = 16 \implies \cos\theta = \frac{16}{34} = \frac{8}{17}$.
    
    Тогаш $x = \frac{25 - 34(8/17)}{3} = \frac{25 - 16}{3} = \frac{9}{3} = 3$.
    
    **Одговор:** 3.

## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Методот со квадрирање и собирање ($a^2+b^2$) е многу елегантен за вакви системи.