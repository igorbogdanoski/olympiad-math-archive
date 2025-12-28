---
grade: 11
field: algebra
difficulty: 5
problem_type: calculation
source: "Municipal_Competition_2022"
problem_id: 2022_mun_y3_8b
language_original: mk
translated: false

# --- SKILL MAPPING ---
primary_skill: trigonometric_equations
related_skills:
  - logic
prerequisites:
  - sum_to_product_formulas

# --- TOPICS ---
tags:
  - trigonometry
  - inequalities
  - olympiad
---

[⬅️ Назад кон Индексот](../../README.md) | [🧰 Skill: trigonometric_equations](../../../tools/skill_guides/trigonometric_equations.md)

# Тригонометриско неравенство

## 📝 Текст на задачата
За кое од следниве множества важи неравенството $\sin x \le \sin 3x$?

## 🧠 Анализа (Клучна идеја)
Префрли сè на една страна: $\sin 3x - \sin x \ge 0$. Користи формула за разлика на синуси: $2 \sin \frac{A-B}{2} \cos \frac{A+B}{2}$.

## 💡 Решение

??? success "👀 Прикажи го решението"
    Неравенството е $\sin 3x - \sin x \ge 0$.
    Користиме формула: $\sin A - \sin B = 2 \sin \frac{A-B}{2} \cos \frac{A+B}{2}$.
    $$ 2 \sin \frac{3x-x}{2} \cos \frac{3x+x}{2} \ge 0 $$
    $$ 2 \sin x \cos 2x \ge 0 $$
    
    Ова е производ на два члена. Треба да имаат ист знак.
    
    **Случај 1:** $\sin x \ge 0$ И $\cos 2x \ge 0$.
    - $\sin x \ge 0 \implies x \in [0, \pi] \cup [2\pi, 3\pi] \dots$
    - $\cos 2x \ge 0 \implies 2x \in [-\frac{\pi}{2}, \frac{\pi}{2}] \cup [\frac{3\pi}{2}, \frac{5\pi}{2}] \dots$
      Делиме со 2: $x \in [-\frac{\pi}{4}, \frac{\pi}{4}] \cup [\frac{3\pi}{4}, \frac{5\pi}{4}]$.
    
    Пресек во $[0, \pi]$:
    - $[0, \pi] \cap [0, \frac{\pi}{4}] = [0, \frac{\pi}{4}]$.
    - $[0, \pi] \cap [\frac{3\pi}{4}, \pi] = [\frac{3\pi}{4}, \pi]$.
    
    **Случај 2:** $\sin x \le 0$ И $\cos 2x \le 0$.
    - $\sin x \le 0 \implies x \in [\pi, 2\pi]$.
    - $\cos 2x \le 0 \implies 2x \in [\frac{\pi}{2}, \frac{3\pi}{2}] \dots$
      $x \in [\frac{\pi}{4}, \frac{3\pi}{4}] \cup [\frac{5\pi}{4}, \frac{7\pi}{4}]$.
    
    Пресек во $[\pi, 2\pi]$:
    - $[\pi, 2\pi] \cap [\frac{5\pi}{4}, \frac{7\pi}{4}] = [\frac{5\pi}{4}, \frac{7\pi}{4}]$.
    
    **Одговор:** Унијата на интервалите погоре.

## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Решавањето на тригонометриски неравенки бара внимателна работа со единичната кружница.