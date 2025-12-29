---
grade: 8
field: geometry
difficulty: 5
source: "<натпревар / списание / година>"
problem_id: copernicus_cat2_01
language_original: <mk | en | sr | hr | ...>
translated: false

# 
tags:
  - geometry
  - square
  - equilateral_triangle
  - angle_chasing
related_skills:
  - isosceles_triangle_properties
  - angle_sum_triangle
---

# Problem
Given a square $ABCD$. A point $E$ is chosen inside the square such that $\triangle ABE$ is equilateral. Calculate the size of the angle $\angle DEC$.

![Problem Visualization](media/copernicus_cat2_01.mp4)

# Solution
Since $ABCD$ is a square, $AB = BC = CD = DA$ and all angles are $90^\circ$.
Since $\triangle ABE$ is equilateral, $AB = AE = BE$ and all angles are $60^\circ$.

Consider $\triangle ADE$.
$AD = AB$ (sides of square) and $AE = AB$ (sides of equilateral triangle).
Therefore, $AD = AE$, so $\triangle ADE$ is isosceles.
The angle at the vertex $A$ is:
$$\angle DAE = \angle DAB - \angle EAB = 90^\circ - 60^\circ = 30^\circ$$
Since $\triangle ADE$ is isosceles with $AD=AE$, the base angles are equal:
$$\angle ADE = \angle AED = \frac{180^\circ - 30^\circ}{2} = \frac{150^\circ}{2} = 75^\circ$$

Similarly, consider $\triangle BCE$.
$BC = AB$ and $BE = AB$, so $BC = BE$. $\triangle BCE$ is isosceles.
The angle at vertex $B$ is:
$$\angle CBE = \angle CBA - \angle EBA = 90^\circ - 60^\circ = 30^\circ$$
The base angles are:
$$\angle BCE = \angle BEC = \frac{180^\circ - 30^\circ}{2} = 75^\circ$$

Now consider the angles around point $E$.
Wait, we can find $\angle DEC$ directly from the sum of angles in $\triangle CDE$ or around $E$.
Let's use the angles at $D$ and $C$.
$\angle EDC = \angle ADC - \angle ADE = 90^\circ - 75^\circ = 15^\circ$.
$\angle ECD = \angle BCD - \angle BCE = 90^\circ - 75^\circ = 15^\circ$.

In $\triangle CDE$:
$$\angle DEC = 180^\circ - (\angle EDC + \angle ECD) = 180^\circ - (15^\circ + 15^\circ) = 180^\circ - 30^\circ = 150^\circ$$

Alternatively, calculating angles around $E$:
$\angle AEB = 60^\circ$.
$\angle AED = 75^\circ$.
$\angle BEC = 75^\circ$.
The sum of angles around $E$ is $360^\circ$:
$$\angle DEC = 360^\circ - (60^\circ + 75^\circ + 75^\circ) = 360^\circ - 210^\circ = 150^\circ$$

The angle $\angle DEC$ is $150^\circ$.

![Equilateral Triangle in Square](images/copernicus_cat2_01.png)

## 💡 Решение

### Чекор 1: Анализа на страните
Од својствата на квадратот и рамностраниот триаголник имаме:
1. $AB = BC = CD = DA$ (страни на квадрат).
2. $AB = AE = BE$ (страни на рамностран триаголник).

Од (1) и (2) следи транзитивноста:
$$ AD = AE \quad \text{и} \quad BC = BE $$

### Чекор 2: Ловење агли во $\triangle ADE$
Бидејќи $AD = AE$, триаголникот $\triangle ADE$ е **рамнокрак**.
Аголот при врвот $A$ е:
$$ \angle DAE = \angle DAB - \angle EAB = 90^\circ - 60^\circ = 30^\circ $$
Аглите при основата $DE$ се еднакви:
$$ \angle ADE = \angle AED = \frac{180^\circ - 30^\circ}{2} = 75^\circ $$

### Чекор 3: Ловење агли во $\triangle BCE$
Аналогно, $\triangle BCE$ е рамнокрак ($BC=BE$).
Аголот при врвот $B$ е:
$$ \angle CBE = \angle CBA - \angle EBA = 90^\circ - 60^\circ = 30^\circ $$
Аглите при основата $CE$ се:
$$ \angle BCE = \angle BEC = \frac{180^\circ - 30^\circ}{2} = 75^\circ $$

### Чекор 4: Пресметка на $\angle DEC$
Аголот $\angle DEC$ може да се најде преку полниот агол околу $E$:
$$ \angle DEC = 360^\circ - (\angle AEB + \angle AED + \angle BEC) $$
$$ \angle DEC = 360^\circ - (60^\circ + 75^\circ + 75^\circ) = 360^\circ - 210^\circ = 150^\circ $$

**Резултат:** $\angle DEC = 150^\circ$.