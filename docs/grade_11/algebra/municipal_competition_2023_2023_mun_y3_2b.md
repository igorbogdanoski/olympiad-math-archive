---
grade: 11
field: algebra
difficulty: 3
problem_type: proof
source: "Municipal_Competition_2023"
problem_id: 2023_mun_y3_2b
language_original: mk
translated: false

# --- SKILL MAPPING ---
primary_skill: algebraic_manipulation
related_skills:
  - logic
prerequisites:
  - logarithm_properties

# --- TOPICS ---
tags:
  - logarithms
  - change_of_base
  - proof
  - olympiad
---

[⬅️ Назад кон Индексот](../../README.md) | [🧰 Skill: algebraic_manipulation](../../../tools/skill_guides/algebraic_manipulation.md)

# Логаритамски идентитет

## 📝 Текст на задачата
Докажи дека ако $\log_b x = \frac{1}{2}(\log_a x + \log_c x)$, тогаш $\log_b \sqrt{ac} = \log_b a \cdot \log_b c$. (Услови: $x, a, b, c > 0, \neq 1$).


## 🧠 Анализа (Клучна идеја)
Претворете ги сите логаритми во условот во основа $x$ користејќи $\log_u v = \frac{1}{\log_v u}$. Потоа средете го изразот и вратете се во основа $b$.

## 💡 Решение

<details>
<summary>👀 Прикажи го решението</summary>

**Чекор 1: Промена на основа во $x$**
Условот е:
$$ \frac{1}{\log_x b} = \frac{1}{2} \left( \frac{1}{\log_x a} + \frac{1}{\log_x c} \right) $$

**Чекор 2: Алгебарско средување**
$$ \frac{2}{\log_x b} = \frac{\log_x c + \log_x a}{\log_x a \cdot \log_x c} $$
$$ 2 \log_x a \cdot \log_x c = \log_x b (\log_x (ac)) $$

Ова изгледа комплицирано. Ајде да пробаме да го докажеме равенството со претворање на целта во основа $x$.
Цел: $\log_b \sqrt{ac} = \log_b a \cdot \log_b c$.
Лева страна: $\frac{1}{2} \log_b (ac) = \frac{1}{2} \frac{\log_x (ac)}{\log_x b}$.
Десна страна: $\frac{\log_x a}{\log_x b} \cdot \frac{\log_x c}{\log_x b}$.

Дали се еднакви?
Од чекор 2 имаме: $\frac{2}{\log_x b} = \frac{\log_x (ac)}{\log_x a \cdot \log_x c}$.
Множиме со $\log_x a \cdot \log_x c$ и делиме со 2:
$$ \frac{\log_x a \cdot \log_x c}{\log_x b} = \frac{1}{2} \log_x (ac) $$

Делиме уште еднаш со $\log_x b$:
$$ \frac{\log_x a}{\log_x b} \cdot \frac{\log_x c}{\log_x b} = \frac{1}{2} \frac{\log_x (ac)}{\log_x b} $$
$$ \log_b a \cdot \log_b c = \log_b \sqrt{ac} $$

Доказот е завршен.

</details>


## 🏁 Заклучок
<Краен резултат.>

## 👩‍🏫 За наставници
Промената на основа е најмоќната алатка кога аргументот ($x$) е ист, а основите се различни.