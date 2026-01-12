---
difficulty: 3
field: geometry
geometry_style: synthetic
grade: 9
language_original: <mk | en | sr | hr | ...>
prerequisites:
- pythagorean_theorem
primary_skill: pythagorean_theorem
problem_id: 2022_mun_g9_10
problem_type: calculation
related_skills:
- logic
related_theorems:
- pythagorean_theorem
source: Municipal_Competition_2022
tags:
- geometry
- olympiad
- circle
- chords
- pythagoras
translated: false
visual_prompt: No visual prompt provided.
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: pythagorean_theorem](../../skill_guides/pythagorean_theorem.md)

# Растојание меѓу тетиви

## 📝 Текст на задачата
Во кружница со радиус $r=13$ cm, повлечени се две паралелни тетиви со должини 24 cm и 10 cm, така што центарот НЕ е меѓу нив. Колку изнесува растојанието меѓу тетивите?

## 📐 Скица
![Problem_2022_mun_g9_10](https://raw.githubusercontent.com/pc4all/olympiad-math-archive/main/media/images/manim_2022_mun_g9_10/Problem_2022_mun_g9_10_ManimCE_v0.19.1.png)
## 🧠 Анализа
**Зошто е оваа задача тешка?**
Растојанието од центарот до тетива се наоѓа со Питагорова теорема: $d^2 = r^2 - (c/2)^2$. Пресметајте ги растојанијата $d_1$ и $d_2$. Бидејќи центарот не е меѓу нив (тетивите се од иста страна), вкупното растојание е разликата $|d_1 - d_2|$.

**Конструктивен потег:**
Растојанието од центарот до тетива се наоѓа со Питагорова теорема: $d^2 = r^2 - (c/2)^2$. Пресметајте ги растојанијата $d_1$ и $d_2$. Бидејќи центарот не е меѓу нив (тетивите се од иста страна), вкупното растојание е разликата $|d_1 - d_2|$.

## 💡 Решение

??? tip "Чекор 1: Растојание до првата тетива ($c_1 = 24$)"
    Половина тетива: $12$.
    $$ d_1 = \sqrt{13^2 - 12^2} = \sqrt{169 - 144} = \sqrt{25} = 5 \text{ cm} $$

??? tip "Чекор 2: Растојание до втората тетива ($c_2 = 10$)"
    Половина тетива: $5$.
    $$ d_2 = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12 \text{ cm} $$

??? tip "Чекор 3: Вкупно растојание"
    Бидејќи центарот не е меѓу нив, тетивите се од иста страна на центарот.
    $$ d = |d_2 - d_1| = |12 - 5| = 7 \text{ cm} $$
    
    Одговор: 7 cm.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Ако центарот беше меѓу нив, растојанието ќе беше збир ($12+5=17$). Ова е честа варијација.