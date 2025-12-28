---
grade: 9
field: geometry
difficulty: 9
source: "<натпревар / списание / година>"
problem_id: geom_9_2015_iso_angle
language_original: <mk | en | sr | hr | ...>
translated: false

# 
tags:
  - geometry
  - trigonometry
  - isosceles_triangle
  - angle_bisector
related_skills:
  - trigonometric_identities
  - solving_equations
---

# Problem
Determine the angles of an isosceles triangle $ABC$, where the altitude to the base is half the length of the angle bisector of one of the base angles.

![Problem Visualization](media/geom_9_2015_iso_angle.mp4)

# Solution
Let the triangle be $ABC$ with $AC=BC$. Let $\alpha$ be the base angle $\angle A = \angle B$, and $\gamma$ be the vertex angle $\angle C$.
Let $h_c$ be the altitude to the base $AB$, and $l_\alpha$ be the angle bisector of $\angle A$.
We are given $l_\alpha = 2 h_c$.

In the right-angled triangle $ADC$ (where $D$ is the midpoint of $AB$), we have:
$$h_c = AC \sin \alpha$$

The length of the angle bisector $l_\alpha$ is given by the formula:
$$l_\alpha = \frac{2 AC \cdot AB \cos(\alpha/2)}{AC + AB}$$
Since $AB = 2 AC \cos \alpha$, we can substitute:
$$l_\alpha = \frac{2 AC \cdot (2 AC \cos \alpha) \cos(\alpha/2)}{AC + 2 AC \cos \alpha} = \frac{4 AC^2 \cos \alpha \cos(\alpha/2)}{AC(1 + 2 \cos \alpha)} = \frac{4 AC \cos \alpha \cos(\alpha/2)}{1 + 2 \cos \alpha}$$

We are given $l_\alpha = 2 h_c$. Substituting $h_c = AC \sin \alpha$:
$$\frac{4 AC \cos \alpha \cos(\alpha/2)}{1 + 2 \cos \alpha} = 2 AC \sin \alpha$$

Dividing by $2 AC$ (since $AC \neq 0$):
$$\frac{2 \cos \alpha \cos(\alpha/2)}{1 + 2 \cos \alpha} = \sin \alpha$$
$$2 \cos \alpha \cos(\alpha/2) = \sin \alpha (1 + 2 \cos \alpha)$$

Using $\sin \alpha = 2 \sin(\alpha/2) \cos(\alpha/2)$:
$$2 \cos \alpha \cos(\alpha/2) = 2 \sin(\alpha/2) \cos(\alpha/2) (1 + 2 \cos \alpha)$$

Since $\alpha < 90^\circ$, $\cos(\alpha/2) \neq 0$, so we can divide by $2 \cos(\alpha/2)$:
$$\cos \alpha = \sin(\alpha/2) (1 + 2 \cos \alpha)$$
$$\cos \alpha = \sin(\alpha/2) + 2 \sin(\alpha/2) \cos \alpha$$
$$\cos \alpha (1 - 2 \sin(\alpha/2)) = \sin(\alpha/2)$$

Let $x = \sin(\alpha/2)$. Then $\cos \alpha = 1 - 2 \sin^2(\alpha/2) = 1 - 2x^2$.
$$(1 - 2x^2)(1 - 2x) = x$$
$$1 - 2x - 2x^2 + 4x^3 = x$$
$$4x^3 - 2x^2 - 3x + 1 = 0$$

We check for rational roots. $x=1$ is a root since $4-2-3+1=0$.
Dividing by $(x-1)$:
$$(x-1)(4x^2 + 2x - 1) = 0$$

Since $x = \sin(\alpha/2) < 1$ (as $\alpha < 180^\circ$), we solve $4x^2 + 2x - 1 = 0$:
$$x = \frac{-2 \pm \sqrt{4 - 4(4)(-1)}}{8} = \frac{-2 \pm \sqrt{20}}{8} = \frac{-1 \pm \sqrt{5}}{4}$$

Since $x > 0$, we take the positive root:
$$x = \frac{\sqrt{5}-1}{4}$$

This value corresponds to $\sin(18^\circ)$.
So $\alpha/2 = 18^\circ \implies \alpha = 36^\circ$.

The angles of the triangle are:
$$\angle A = \angle B = 36^\circ$$
$$\angle C = 180^\circ - 2(36^\circ) = 108^\circ$$

The angles are $36^\circ, 36^\circ, 108^\circ$.

![Isosceles Angle](images/geom_9_2015_iso_angle.png)

## 💡 Решение

Нека аглите при основата се $\alpha$, а аголот при врвот $\gamma$.
Висината кон основата е $h_c = a \sin \alpha$, каде $a$ е должината на кракот.
Симетралата на аголот $\alpha$ е $l_a$.
Во триаголникот $ABD$ (каде $AD$ е симетрала), аглите се $\alpha/2$, $\beta = \alpha$, и $\angle ADB = 180^\circ - 1.5\alpha$.
Според синусната теорема за $\triangle ABD$:
$$ \frac{l_a}{\sin \beta} = \frac{c}{\sin(180^\circ - 1.5\alpha)} $$
$$ \frac{l_a}{\sin \alpha} = \frac{c}{\sin(1.5\alpha)} \implies l_a = \frac{c \sin \alpha}{\sin(1.5\alpha)} $$
Исто така, во правоаголниот триаголник $AMC$ (каде $M$ е средина на $AB$), имаме:
$$ \tan \alpha = \frac{h_c}{c/2} \implies h_c = \frac{c}{2} \tan \alpha $$
Дадено е дека $h_c = \frac{l_a}{2}$. Заменуваме:
$$ \frac{c}{2} \tan \alpha = \frac{1}{2} \frac{c \sin \alpha}{\sin(1.5\alpha)} $$
$$ \tan \alpha = \frac{\sin \alpha}{\sin(1.5\alpha)} $$
$$ \frac{\sin \alpha}{\cos \alpha} = \frac{\sin \alpha}{\sin(1.5\alpha)} $$
Бидејќи $\alpha$ е агол во триаголник, $\sin \alpha \neq 0$, па можеме да скратиме:
$$ \frac{1}{\cos \alpha} = \frac{1}{\sin(1.5\alpha)} \implies \cos \alpha = \sin(1.5\alpha) $$
Користиме идентитет $\cos \alpha = \sin(90^\circ - \alpha)$:
$$ \sin(90^\circ - \alpha) = \sin(1.5\alpha) $$
Решенијата се:
1. $90^\circ - \alpha = 1.5\alpha \implies 2.5\alpha = 90^\circ \implies \alpha = 36^\circ$.
2. $90^\circ - \alpha = 180^\circ - 1.5\alpha \implies 0.5\alpha = 90^\circ \implies \alpha = 180^\circ$ (невозможно).

Значи, аглите при основата се $\alpha = 36^\circ$.
Аголот при врвот е $\gamma = 180^\circ - 2\alpha = 180^\circ - 72^\circ = 108^\circ$.
Аглите на триаголникот се $36^\circ, 36^\circ, 108^\circ$. 
5. $2\alpha + \frac{\alpha}{2} = 90^\circ \implies 5\alpha = 180^\circ \implies \alpha = 36^\circ$. 
6. Аглите се $36^\circ, 36^\circ, 108^\circ$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.