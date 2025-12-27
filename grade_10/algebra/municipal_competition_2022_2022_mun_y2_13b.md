---
grade: 10
field: algebra
difficulty: 4
problem_type: calculation
source: "Municipal_Competition_2022"
problem_id: 2022_mun_y2_13b
language_original: mk
translated: false

# --- SKILL MAPPING ---
primary_skill: algebraic_substitution
related_skills:
  - logic
prerequisites:
  - trig_identities
  - quadratic_equation

# --- TOPICS ---
tags:
  - trigonometry
  - equation
  - olympiad
---

[⬅️ Назад кон Индексот](../../README.md) | [🧰 Skill: algebraic_substitution](../../../tools/skill_guides/algebraic_substitution.md)

# Хомогена тригонометриска равенка

## 📝 Текст на задачата
Познато е дека важи равенството $2 - \cos^2 \alpha = 3 \sin \alpha \cos \alpha$. Да се најде вредноста $2 \tan \alpha$, ако се знае дека $\sin \alpha \ne \cos \alpha$ и $\cos \alpha \ne 0$.


## 🧠 Анализа (Клучна идеја)
Ова е хомогена равенка. Подели со $\cos^2 \alpha$ за да добиеш квадратна равенка по $\tan \alpha$.

## 💡 Решение

<details>
<summary>👀 Прикажи го решението</summary>

Дадено: $2 - \cos^2 \alpha = 3 \sin \alpha \cos \alpha$.
Делиме со $\cos^2 \alpha$:
$$ \frac{2}{\cos^2 \alpha} - 1 = 3 \tan \alpha $$
$$ 2(1 + \tan^2 \alpha) - 1 = 3 \tan \alpha $$
$$ 2\tan^2 \alpha - 3\tan \alpha + 1 = 0 $$

Смена $t = \tan \alpha$:
$$ 2t^2 - 3t + 1 = 0 $$
$(2t-1)(t-1) = 0$.
$t_1 = 1, t_2 = 1/2$.

Услов: $\sin \alpha \ne \cos \alpha \implies \tan \alpha \ne 1$.
Значи $t=1$ отпаѓа.
Останува $\tan \alpha = 1/2$.

Бараме $2 \tan \alpha = 2(1/2) = 1$.

**Одговор:** 1.

</details>


## 🏁 Заклучок
<Краен резултат.>

## 👩‍🏫 За наставници
Стандардна постапка за хомогени равенки.