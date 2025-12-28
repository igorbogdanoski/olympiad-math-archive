---
grade: 11
field: algebra
difficulty: 4
problem_type: calculation
source: "Municipal_Competition_2022"
problem_id: 2022_mun_y3_13a
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
Ова е хомогена равенка од втор степен (секој член е со степен 2, ако 2 го гледаме како $2(\sin^2+\cos^2)$). Подели ја целата равенка со $\cos^2 \alpha$ за да добиеш квадратна равенка по $\tan \alpha$.

## 💡 Решение

<details>
<summary>👀 Прикажи го решението</summary>

Дадено: $2 - \cos^2 \alpha = 3 \sin \alpha \cos \alpha$.
Делиме со $\cos^2 \alpha$ (бидејќи $\cos \alpha \ne 0$):
$$ \frac{2}{\cos^2 \alpha} - 1 = 3 \frac{\sin \alpha}{\cos \alpha} $$
Знаеме дека $\frac{1}{\cos^2 \alpha} = 1 + \tan^2 \alpha$.
$$ 2(1 + \tan^2 \alpha) - 1 = 3 \tan \alpha $$
$$ 2 + 2\tan^2 \alpha - 1 = 3 \tan \alpha $$
$$ 2\tan^2 \alpha - 3\tan \alpha + 1 = 0 $$

Воведуваме смена $t = \tan \alpha$:
$$ 2t^2 - 3t + 1 = 0 $$
Решенија:
$$ t_{1,2} = \frac{3 \pm \sqrt{9 - 8}}{4} = \frac{3 \pm 1}{4} $$
$t_1 = 1, \quad t_2 = \frac{1}{2}$.

Услов: $\sin \alpha \ne \cos \alpha \implies \tan \alpha \ne 1$.
Значи $t=1$ отпаѓа.
Останува $\tan \alpha = \frac{1}{2}$.

Бараме $2 \tan \alpha = 2 \cdot \frac{1}{2} = 1$.

**Одговор:** 1.

</details>


## 🏁 Заклучок
<Краен резултат.>

## 👩‍🏫 За наставници
Трансформацијата во $\tan x$ е стандарден метод за хомогени равенки.