---
grade: 9
field: geometry
difficulty: 7
source: "<натпревар / списание / година>"
problem_id: geom_9_area_height
language_original: <mk | en | sr | hr | ...>
translated: false

tags:
  - geometry
  - algebra
  - area
  - triangle
related_skills:
  - area_formula
  - algebraic_manipulation

# Problem
Sides of a triangle are $a=4$ and $b=6$. If $h_c = h_a + h_b$, calculate the third side $c$.

![Problem Visualization](media/geom_9_area_height.mp4)

# Solution
Let $P$ be the area of the triangle. We know that:
$$P = \frac{1}{2} a h_a = \frac{1}{2} b h_b = \frac{1}{2} c h_c$$

From this, we can express the altitudes in terms of the area and the sides:
$$h_a = \frac{2P}{a}, \quad h_b = \frac{2P}{b}, \quad h_c = \frac{2P}{c}$$

The problem states that $h_c = h_a + h_b$. Substituting the expressions for the altitudes:
$$\frac{2P}{c} = \frac{2P}{a} + \frac{2P}{b}$$

Dividing by $2P$ (since $P \neq 0$):
$$\frac{1}{c} = \frac{1}{a} + \frac{1}{b}$$

Substitute the given values $a=4$ and $b=6$:
$$\frac{1}{c} = \frac{1}{4} + \frac{1}{6}$$
$$\frac{1}{c} = \frac{3}{12} + \frac{2}{12}$$
$$\frac{1}{c} = \frac{5}{12}$$

Therefore:
$$c = \frac{12}{5} = 2.4$$

The third side is $c = 2.4$.
  - angle_chasing
  - similarity--- GEOMETRY SKILLS ---
geometry_style: synthetic # synthetic | analytic | mixed
primary_skill: <main_tool> # e.g., angle_chasing, similarity, cyclic_quads
related_skills:
  - reciprocal_relations
  - perimeter

allowed_tools:
  - classical_euclidean
  - similarity
  - symmetry
forbidden_tools:
  - coordinate_geometry
  - vectors
  - complex_numbers
tags:
  - geometry
  - olympiad
---

# Периметар преку релација на висини

## Текст на задачата
За висините во триаголникот $ABC$ важи $h_c = h_a + h_b$. Ако $a=4$ dm, $b=6$ dm, пресметај го периметарот на $ABC$.

## 📐 Скица / Конструкција
![Problem_geom_9_area_height](images/geom_9_area_height.png)

## 💡 Решение

Плоштината на триаголникот $P$ може да се изрази преку секоја од страните и соодветната висина:
$$ P = \frac{a \cdot h_a}{2} = \frac{b \cdot h_b}{2} = \frac{c \cdot h_c}{2} $$
Од овие равенства ги изразуваме висините:
$$ h_a = \frac{2P}{a}, \quad h_b = \frac{2P}{b}, \quad h_c = \frac{2P}{c} $$
Дадената релација е $h_c = h_a + h_b$. Заменуваме со изразите погоре:
$$ \frac{2P}{c} = \frac{2P}{a} + \frac{2P}{b} $$
Бидејќи $P \neq 0$, можеме да поделиме со $2P$:
$$ \frac{1}{c} = \frac{1}{a} + \frac{1}{b} $$
Заменуваме со дадените вредности $a=4$ dm и $b=6$ dm:
$$ \frac{1}{c} = \frac{1}{4} + \frac{1}{6} = \frac{3}{12} + \frac{2}{12} = \frac{5}{12} $$
Оттука, $c = \frac{12}{5} = 2.4$ dm.

Периметарот на триаголникот е:
$$ L = a + b + c = 4 + 6 + 2.4 = 12.4 \text{ dm} $$

## 📝 Решение (СИНТЕТИЧКО)
1. Од $h_c = h_a + h_b$ заменуваме $\frac{2P}{c} = \frac{2P}{a} + \frac{2P}{b}$. 
2. Делиме со $2P$ и добиваме: $\frac{1}{c} = \frac{1}{a} + \frac{1}{b}$. 
3. Со замена на $a=4, b=6$: $\frac{1}{c} = \frac{1}{4} + \frac{1}{6} = \frac{5}{12}$. 
4. $c = \frac{12}{5} = 2.4$ dm. 
5. $L = 4 + 6 + 2.4 = 12.4$ dm.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.