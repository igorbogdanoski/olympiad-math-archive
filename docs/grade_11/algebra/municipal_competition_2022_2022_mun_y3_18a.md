---
difficulty: 4
field: algebra
grade: 11
language_original: mk
prerequisites:
- algebraic_manipulation
primary_skill: inequalities_am_gm
problem_id: 2022_mun_y3_18a
problem_type: calculation
related_skills:
- logic
related_theorems:
- am_gm_inequality
- optimization
- symmetry
source: Municipal_Competition_2022
tags:
- inequalities
- am_gm
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: inequalities_am_gm](../../skill_guides/inequalities_am_gm.md)

# Минимум на алгебарски израз

## 📝 Текст на задачата
Нека $x, y, z$ се позитивни реални броеви. Најди ја најмалата вредност за изразот:
$$ \left(\frac{x}{y}+2\right)\left(\frac{y}{z}+2\right)\left(\frac{z}{x}+2\right) $$

## 🧠 Анализа (Клучна идеја)
Изможи ги заградите или користи АМ-ГМ на секоја заграда? Не, подобро е да се измножи. Или, забележи дека ако $x=y=z$, вредноста е $(1+2)^3 = 27$.

## 💡 Решение

??? success "👀 Прикажи го решението"
    Нека изразот е $E$.
    Ако ги измножиме заградите:
    $$ E = \frac{x}{y}\frac{y}{z}\frac{z}{x} + 2(\dots) + 4(\dots) + 8 $$
    $$ E = 1 + 2(\frac{x}{y}\frac{y}{z} + \dots) + 4(\frac{x}{y} + \dots) + 8 $$
    $$ E = 9 + 2(\frac{x}{z} + \frac{y}{x} + \frac{z}{y}) + 4(\frac{x}{y} + \frac{y}{z} + \frac{z}{x}) $$
    
    Според АМ-ГМ неравенството за 3 броја:
    $$ a+b+c \ge 3\sqrt[3]{abc} $$
    
    За првата група:
    $$ \frac{x}{z} + \frac{y}{x} + \frac{z}{y} \ge 3\sqrt[3]{1} = 3 $$
    За втората група:
    $$ \frac{x}{y} + \frac{y}{z} + \frac{z}{x} \ge 3\sqrt[3]{1} = 3 $$
    
    Заменуваме:
    $$ E \ge 9 + 2(3) + 4(3) = 9 + 6 + 12 = 27 $$
    
    Минимумот се достигнува кога $x=y=z$.
    
    **Одговор:** 27.

## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Симетријата сугерира дека екстремот е во $x=y=z$.