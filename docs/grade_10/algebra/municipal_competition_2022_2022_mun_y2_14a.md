---
difficulty: 3
field: algebra
grade: 10
language_original: mk
prerequisites:
- quadratic_function
primary_skill: functions
problem_id: 2022_mun_y2_14a
problem_type: calculation
related_skills:
- logic
related_theorems:
- vieta_formulas
source: Municipal_Competition_2022
tags:
- quadratic_function
- vertex
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: functions](../../skill_guides/functions.md)

# Теме на парабола

## 📝 Текст на задачата
Нека $f(x) = -x^2 + bx + c$ е квадратна функција со теме во точката $(3, 2)$. Ако $x_1$ и $x_2$ се нулите на функцијата, пресметај ја вредноста на изразот $(x_1 - x_2)^2$.

## 🧠 Анализа (Клучна идеја)
Координатите на темето се $T(-\frac{b}{2a}, f(-\frac{b}{2a}))$. Искористи го ова за да ги најдеш $b$ и $c$. Потоа користи Виетови формули за изразот.

## 💡 Решение

??? success "👀 Прикажи го решението"
    Функцијата е $f(x) = -x^2 + bx + c$. ($a=-1$).
    Темето е $T(3, 2)$.
    
    1. **Наоѓање на $b$:**
       $x_T = -\frac{b}{2a} = -\frac{b}{-2} = \frac{b}{2}$.
       Дадено е $x_T = 3 \implies \frac{b}{2} = 3 \implies b = 6$.
    
    2. **Наоѓање на $c$:**
       $y_T = f(3) = 2$.
       $-3^2 + 6(3) + c = 2$
       $-9 + 18 + c = 2$
       $9 + c = 2 \implies c = -7$.
       Функцијата е $f(x) = -x^2 + 6x - 7$.
    
    3. **Пресметка на изразот:**
       Бараме $(x_1 - x_2)^2$.
       Знаеме $(x_1 - x_2)^2 = (x_1 + x_2)^2 - 4x_1x_2$.
       Од Виетови формули за $-x^2 + 6x - 7 = 0$ (или $x^2 - 6x + 7 = 0$):
       $x_1 + x_2 = 6$
       $x_1 x_2 = 7$
       
       Заменуваме:
       $$ (x_1 - x_2)^2 = 6^2 - 4(7) = 36 - 28 = 8 $$
    
    **Одговор:** 8.

## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Врската меѓу темето и коефициентите е основна за квадратна функција.