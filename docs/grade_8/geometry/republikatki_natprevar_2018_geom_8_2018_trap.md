---
grade: 8
field: geometry
difficulty: 7
source: "<натпревар / списание / година>"
problem_id: geom_8_2018_trap
language_original: <mk | en | sr | hr | ...>
translated: false

# 
tags:
  - geometry
  - trapezoid
  - midpoints
  - angles
related_skills:
  - parallel_translation
  - right_triangle_median
---

# Problem
Given a trapezoid $ABCD$ with bases $AB=a, CD=b, a>b$. Let $M$ and $N$ be the midpoints of the bases $AB$ and $CD$, respectively, and let $MN = \frac{a-b}{2}$. Calculate the sum of the angles at the larger base.

![Problem Visualization](media/geom_8_2018_trap.mp4)

# Solution
Let's translate the legs $AD$ and $BC$ parallel to themselves so that they pass through $N$.
Let $P$ be a point on $AB$ such that $NP \parallel AD$. Then $ANPD$ is a parallelogram, so $AP = DN = b/2$.
Let $Q$ be a point on $AB$ such that $NQ \parallel BC$. Then $NBCQ$ is a parallelogram, so $QB = NC = b/2$.

The length of the segment $PQ$ is:
$$PQ = AB - AP - QB = a - \frac{b}{2} - \frac{b}{2} = a - b$$

We are given that $MN = \frac{a-b}{2}$.
In $\triangle NPQ$, $M$ is the midpoint of $PQ$ because $M$ is the midpoint of $AB$ and $P, Q$ are symmetric with respect to $M$ (since $AP=QB$).
Wait, let's verify $M$ is the midpoint of $PQ$.
$AM = a/2$.
$PM = AM - AP = a/2 - b/2 = (a-b)/2$.
$MQ = MB - QB = a/2 - b/2 = (a-b)/2$.
So $M$ is indeed the midpoint of $PQ$.

In $\triangle NPQ$, the median $NM$ has length $\frac{a-b}{2}$, which is exactly half the length of the side $PQ$ ($PQ = a-b$).
A triangle where the median to a side is half the length of that side is a right-angled triangle.
Therefore, $\angle PNQ = 90^\circ$.

Since $NP \parallel AD$, $\angle APN = \angle A$ (corresponding angles? No, $NP \parallel AD$, so $\angle A + \angle APN = 180^\circ$ if consecutive interior, or $\angle NPQ = \angle A$ if we extend... wait).
Actually, $NP \parallel AD \implies \angle NPQ = \angle DAB = \alpha$ (corresponding angles).
And $NQ \parallel BC \implies \angle NQP = \angle CBA = \beta$ (corresponding angles).

In the right-angled triangle $NPQ$ (right angle at $N$), the sum of the acute angles is $90^\circ$.
$$\angle NPQ + \angle NQP = 90^\circ$$
$$\alpha + \beta = 90^\circ$$

So the sum of the angles at the larger base is $90^\circ$.

![Trapezoid Midpoints](images/geom_8_2018_trap.png)

## 💡 Решение

Нека повлечеме прави низ точката $N$ (средина на $CD$) кои се паралелни со краците $AD$ и $BC$.
Нека овие прави ја сечат основата $AB$ во точките $P$ и $Q$, така што $NP \parallel AD$ и $NQ \parallel BC$.

1.  **Паралелограми:**
    Четириаголникот $APND$ е паралелограм (бидејќи $AP \parallel DN$ и $NP \parallel AD$).
    Следствено, $AP = DN = \frac{b}{2}$.
    Четириаголникот $NQCD$ е паралелограм (бидејќи $NQ \parallel BC$ и $NC \parallel QB$).
    Следствено, $QB = NC = \frac{b}{2}$.

2.  **Должина на $PQ$:**
    $PQ = AB - AP - QB = a - \frac{b}{2} - \frac{b}{2} = a - b$.

3.  **Положба на $M$:**
    Точката $M$ е средина на $AB$, па $AM = \frac{a}{2}$.
    Растојанието $PM = AM - AP = \frac{a}{2} - \frac{b}{2} = \frac{a-b}{2}$.
    Растојанието $MQ = MB - QB = \frac{a}{2} - \frac{b}{2} = \frac{a-b}{2}$.
    Значи, $M$ е средина на отсечката $PQ$.

4.  **Триаголник $PNQ$:**
    Во $\triangle PNQ$, отсечката $NM$ е тежишна линија (медијана) кон страната $PQ$.
    Дадено е дека $MN = \frac{a-b}{2}$.
    Бидејќи $PQ = a-b$, следува дека $MN = \frac{1}{2} PQ$.
    
    Познато е дека медијаната кон една страна во триаголник е еднаква на половина од таа страна ако и само ако триаголникот е правоаголен (со прав агол во темето од кое поаѓа медијаната).
    Значи, $\angle PNQ = 90^\circ$.

5.  **Збир на агли:**
    Бидејќи $NP \parallel AD$, аголот $\angle NPQ = \angle DAB = \alpha$ (согласни агли).
    Бидејќи $NQ \parallel BC$, аголот $\angle NQP = \angle CBA = \beta$ (согласни агли).
    Во правоаголниот $\triangle PNQ$:
    $$ \angle NPQ + \angle NQP = 90^\circ $$
    $$ \alpha + \beta = 90^\circ $$

Збирот на аглите на поголемата основа е $90^\circ$.