---
grade: 9
field: geometry
difficulty: 7
source: "<натпревар / списание / година>"
problem_id: geom_9_sum_altitudes
language_original: <mk | en | sr | hr | ...>
translated: false

# 
tags:
  - geometry
  - area
  - triangle_decomposition
  - identity
related_skills:
  - area_formula
  - algebraic_manipulation
---

# Problem
From an arbitrary point $M$ inside triangle $ABC$, perpendiculars are drawn to sides $a, b, c$ with lengths $x, y, z$ respectively. Prove the identity:
$$\frac{x}{h_a} + \frac{y}{h_b} + \frac{z}{h_c} = 1$$
where $h_a, h_b, h_c$ are the corresponding altitudes of the triangle.

![Problem Visualization](media/geom_9_sum_altitudes.mp4)

# Solution
Let $P$ be the area of triangle $ABC$.
We can decompose the area of $\triangle ABC$ into the sum of the areas of three smaller triangles: $\triangle MBC$, $\triangle MCA$, and $\triangle MAB$.
$$P = P_{MBC} + P_{MCA} + P_{MAB}$$

The area of each smaller triangle can be calculated using the base (side of $\triangle ABC$) and the corresponding height (perpendicular from $M$):
$$P_{MBC} = \frac{1}{2} a x$$
$$P_{MCA} = \frac{1}{2} b y$$
$$P_{MAB} = \frac{1}{2} c z$$

Substituting these into the area sum:
$$P = \frac{1}{2} a x + \frac{1}{2} b y + \frac{1}{2} c z$$

We also know the area of $\triangle ABC$ can be expressed using its altitudes:
$$P = \frac{1}{2} a h_a \implies a = \frac{2P}{h_a}$$
$$P = \frac{1}{2} b h_b \implies b = \frac{2P}{h_b}$$
$$P = \frac{1}{2} c h_c \implies c = \frac{2P}{h_c}$$

Substitute the expressions for $a, b, c$ into the area equation:
$$P = \frac{1}{2} \left(\frac{2P}{h_a}\right) x + \frac{1}{2} \left(\frac{2P}{h_b}\right) y + \frac{1}{2} \left(\frac{2P}{h_c}\right) z$$

Simplifying:
$$P = P \frac{x}{h_a} + P \frac{y}{h_b} + P \frac{z}{h_c}$$

Since $P \neq 0$, we can divide the entire equation by $P$:
$$1 = \frac{x}{h_a} + \frac{y}{h_b} + \frac{z}{h_c}$$

This proves the identity.

## 💡 Решение

Плоштината на триаголникот $ABC$ може да се претстави како збир од плоштините на трите триаголници формирани од точката $M$ и темињата на триаголникот:
$$ P_{ABC} = P_{MBC} + P_{MCA} + P_{MAB} $$
Плоштината на секој од овие триаголници може да се пресмета користејќи ги страните на $\triangle ABC$ како основи и растојанијата од $M$ до страните како висини:
$$ P_{MBC} = \frac{a \cdot x}{2}, \quad P_{MCA} = \frac{b \cdot y}{2}, \quad P_{MAB} = \frac{c \cdot z}{2} $$
Заменуваме во збирот:
$$ P_{ABC} = \frac{ax}{2} + \frac{by}{2} + \frac{cz}{2} $$
Од друга страна, плоштината на $\triangle ABC$ може да се изрази преку неговите висини:
$$ P_{ABC} = \frac{a \cdot h_a}{2} \implies a = \frac{2P_{ABC}}{h_a} $$
$$ P_{ABC} = \frac{b \cdot h_b}{2} \implies b = \frac{2P_{ABC}}{h_b} $$
$$ P_{ABC} = \frac{c \cdot h_c}{2} \implies c = \frac{2P_{ABC}}{h_c} $$
Заменуваме за $a, b, c$ во равенката за збирот на плоштините:
$$ P_{ABC} = \frac{1}{2} \left( \frac{2P_{ABC}}{h_a} \cdot x + \frac{2P_{ABC}}{h_b} \cdot y + \frac{2P_{ABC}}{h_c} \cdot z \right) $$
$$ P_{ABC} = P_{ABC} \left( \frac{x}{h_a} + \frac{y}{h_b} + \frac{z}{h_c} \right) $$
Бидејќи $P_{ABC} \neq 0$, делиме со $P_{ABC}$:
$$ 1 = \frac{x}{h_a} + \frac{y}{h_b} + \frac{z}{h_c} $$
Што требаше да се докаже.


![Визуелизација](../../assets/images/geom_9_sum_altitudes.png){ width=500 }
## 🧠 Анализа
Клучната хеуристика овде е 'Декомпозиција на целина'. Поврзи ја точката $M$ со темињата за да го поделиш големиот триаголник на три помали, чии висини се токму дадените нормали.

## 📝 Решение (СИНТЕТИЧКО)
1. **Декомпозиција:** Нека $P$ е плоштината на $\triangle ABC$. Го делиме триаголникот на $\triangle MBC$, $\triangle MCA$ и $\triangle MAB$. 
2. **Равенство на плоштини:** $P = P_{MBC} + P_{MCA} + P_{MAB}$. 
3. **Изразување преку нормали:** $P = \frac{ax}{2} + \frac{by}{2} + \frac{cz}{2}$. 
4. **Поврзување со висини:** Знаеме дека $a = \frac{2P}{h_a}$, $b = \frac{2P}{h_b}$ и $c = \frac{2P}{h_c}$. 
5. **Супституција:** Заменуваме во изразот: $P = \frac{x}{2} \cdot \frac{2P}{h_a} + \frac{y}{2} \cdot \frac{2P}{h_b} + \frac{z}{2} \cdot \frac{2P}{h_c}$. 
6. **Финале:** По кратењето со $P$, добиваме $1 = \frac{x}{h_a} + \frac{y}{h_b} + \frac{z}{h_c}$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.