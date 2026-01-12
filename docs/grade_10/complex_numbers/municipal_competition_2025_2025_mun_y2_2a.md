---
difficulty: 5
field: complex_numbers
grade: 10
language_original: mk
prerequisites:
- basic_math
primary_skill: logic
problem_id: 2025_mun_y2_2a
problem_type: proof
related_skills:
- logic
related_theorems:
- complex_numbers
source: Municipal_Competition_2025
tags:
- complex_numbers
- conjugate
- modulus
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: logic](../../skill_guides/logic.md)

# Имагинарен број

## 📝 Текст на задачата
Ако $z$ е комплексен број, а $a$ и $b$ се комплексни броеви такви што $|a|=|b|=1$ и $a \neq b$, докажи дека бројот $w = \frac{1}{a-b}(z + ab\overline{z} - a - b)$ е чисто имагинарен.

## 🧠 Анализа (Клучна идеја)
Број $w$ е чисто имагинарен ако и само ако $\overline{w} = -w$ (или $w + \overline{w} = 0$). Користете го својството $|u|=1 \implies \overline{u} = 1/u$. Заменете ги конјугираните вредности за $\overline{a}$ и $\overline{b}$ и обидете се да го добиете изразот за $-w$.

## 💡 Решение

??? tip "Чекор 1: Конјугирање на $w$"
    Користиме $\overline{a} = 1/a$ и $\overline{b} = 1/b$ (бидејќи модулите се 1).
    
    $$ \overline{w} = \frac{\overline{z} + \overline{a}\overline{b}z - \overline{a} - \overline{b}}{\overline{a} - \overline{b}} = \frac{\overline{z} + \frac{1}{ab}z - \frac{1}{a} - \frac{1}{b}}{\frac{1}{a} - \frac{1}{b}} $$

??? tip "Чекор 2: Средување на дропката"
    Множиме горе и долу со $ab$:
    
    $$ \overline{w} = \frac{ab\overline{z} + z - b - a}{b - a} $$

??? tip "Чекор 3: Споредба со $w$"
    Забележуваме дека броителот е ист како кај $w$ ($z + ab\overline{z} - a - b$), но именителот е спротивен ($b-a = -(a-b)$).
    
    $$ \overline{w} = \frac{z + ab\overline{z} - a - b}{-(a-b)} = - \frac{z + ab\overline{z} - a - b}{a-b} = -w $$
    
    Бидејќи $\overline{w} = -w$, бројот е чисто имагинарен.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Оваа задача демонстрира моќта на алгебарските својства на конјугирањето. Замена со $x+iy$ би била пекол.