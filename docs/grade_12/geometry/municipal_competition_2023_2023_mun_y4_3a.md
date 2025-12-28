---
grade: 12
field: geometry
difficulty: 4
problem_type: calculation
source: "Municipal_Competition_2023"
problem_id: 2023_mun_y4_3a
language_original: <mk | en | sr | hr | ...>
translated: false

# --- GEOMETRY SKILLS ---
geometry_style: synthetic
primary_skill: algebraic_manipulation
related_skills:
  - logic
prerequisites:
  - sine_rule
  - cosine_rule

# --- VISUALIZATION ---
visual_prompt: "No visual prompt provided."

tags:
  - geometry
  - olympiad
  - trigonometry
  - sine_rule
  - cosine_rule
  - angles
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: algebraic_manipulation](../../skill_guides/algebraic_manipulation.md)

# Агол во триаголник (Синусна теорема)

## 📝 Текст на задачата
Ако за аглите во триаголникот $ABC$ важи $\frac{\sin^2 \gamma + \sin^2 \beta - \sin^2 \alpha}{\sin \beta \cdot \sin \gamma} = \sqrt{3}$, одреди ја вредноста на аголот $\alpha$.

## 📐 Скица

![Визуелизација](../../assets/images/2023_mun_y4_3a.png){ width=500 }
## 🧠 Анализа
**Зошто е оваа задача тешка?**
Заменете $\sin x = \frac{strana}{2R}$. $R$ ќе се скрати и ќе добиете $b^2+c^2-a^2 = \sqrt{3}bc$. Споредете со Косинусна теорема.

**Конструктивен потег:**
Заменете $\sin x = \frac{strana}{2R}$. $R$ ќе се скрати и ќе добиете $b^2+c^2-a^2 = \sqrt{3}bc$. Споредете со Косинусна теорема.

## 💡 Решение

??? tip "Чекор 1: Трансформација"
    $$ \frac{\frac{c^2}{4R^2} + \frac{b^2}{4R^2} - \frac{a^2}{4R^2}}{\frac{b}{2R} \cdot \frac{c}{2R}} = \sqrt{3} $$
    $$ \frac{b^2+c^2-a^2}{bc} = \sqrt{3} \implies b^2+c^2-a^2 = \sqrt{3}bc $$

??? tip "Чекор 2: Косинусна теорема"
    $a^2 = b^2+c^2 - 2bc \cos \alpha \implies b^2+c^2-a^2 = 2bc \cos \alpha$.

??? tip "Чекор 3: Споредба"
    $2bc \cos \alpha = \sqrt{3}bc \implies \cos \alpha = \frac{\sqrt{3}}{2}$.
    $\alpha = 30^\circ$.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Оваа задача е идентична со онаа што ја дискутиравме претходно, но сега е правилно класифицирана во 4-та година.