---
difficulty: 3
field: geometry
geometry_style: synthetic
grade: 9
language_original: <mk | en | sr | hr | ...>
prerequisites:
- basic_math
primary_skill: logic
problem_id: cnt92_v2_24
problem_type: calculation
related_skills:
- logic
related_theorems:
- am_gm_inequality
- optimization
source: Cnt92_Olympiad_Var2
tags:
- geometry
- olympiad
- parallelogram
- area
- optimization
- inequalities
translated: false
visual_prompt: No visual prompt provided.
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: logic](../../skill_guides/logic.md)

# Минимален периметар на паралелограм

## 📝 Текст на задачата
Ако плоштината на паралелограм со агол од $30^\circ$ изнесува 12.5, тогаш најмалата вредност на периметарот е...

## 📐 Скица
![Problem_cnt92_v2_24](https://raw.githubusercontent.com/pc4all/olympiad-math-archive/main/media/images/manim_cnt92_v2_24/Problem_cnt92_v2_24_ManimCE_v0.19.1.png)
## 🧠 Анализа
**Зошто е оваа задача тешка?**
Имаме фиксна плоштина $S = ab \sin \alpha$. Бидејќи аголот е фиксен, производот на страните $ab$ е константен. Бараме минимум на периметарот $P = 2(a+b)$. Кога збирот на два броја е минимален ако нивниот производ е фиксен? (AM-GM неравенство).

**Конструктивен потег:**
Имаме фиксна плоштина $S = ab \sin \alpha$. Бидејќи аголот е фиксен, производот на страните $ab$ е константен. Бараме минимум на периметарот $P = 2(a+b)$. Кога збирот на два броја е минимален ако нивниот производ е фиксен? (AM-GM неравенство).

## 💡 Решение

??? tip "Чекор 1: Врска меѓу страните"
    Плоштината е дадена со:
    
    $$ S = ab \sin 30^\circ = 12.5 $$
    
    $$ ab \cdot 0.5 = 12.5 \implies ab = 25 $$

??? tip "Чекор 2: Минимизација на периметарот"
    Периметарот е $P = 2(a+b)$. Според неравенството меѓу аритметичка и геометриска средина (AM-GM), за позитивни $a, b$ важи:
    
    $$ a + b \ge 2\sqrt{ab} $$
    
    Заменуваме $ab = 25$:
    
    $$ a + b \ge 2\sqrt{25} = 2 \cdot 5 = 10 $$

??? tip "Чекор 3: Пресметка"
    Минималниот периметар е:
    
    $$ P_{min} = 2(a+b)_{min} = 2 \cdot 10 = 20 $$
    
    Ова се постигнува кога $a=b=5$ (ромб).
    Одговор: Опција 4.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Ова е одличен пример за поврзување на геометрија и алгебра. Нагласете дека кај четириаголници со фиксна плоштина, 'најправилната' форма (ромб/квадрат) обично има најмал периметар.