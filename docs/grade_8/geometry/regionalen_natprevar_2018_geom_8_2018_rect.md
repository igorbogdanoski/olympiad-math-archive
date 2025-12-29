---
grade: 8
field: geometry
difficulty: 6
source: "<натпревар / списание / година>"
problem_id: geom_8_2018_rect
language_original: <mk | en | sr | hr | ...>
translated: false

# 
tags:
  - geometry
  - rectangle
  - area
  - subtraction_method
related_skills:
  - area_calculation
  - linear_equations
---

# Problem
In a rectangle $ABCD$ with perimeter $60$ cm, $BC = \frac{2}{3}AB$. On side $AB$, a point $E$ is given such that $AE = \frac{1}{3}AB$, and on side $BC$, a point $F$ is given such that $BF = \frac{2}{3}BC$. If point $G$ is the midpoint of segment $AD$, what is the area of triangle $EFG$?

![Problem Visualization](media/geom_8_2018_rect.mp4)

# Solution
First, let's find the dimensions of the rectangle.
Let $AB = a$ and $BC = b$.
We are given $b = \frac{2}{3}a$.
The perimeter is $2(a+b) = 60 \implies a+b = 30$.
Substitute $b$:
$a + \frac{2}{3}a = 30 \implies \frac{5}{3}a = 30 \implies a = 18$.
Then $b = \frac{2}{3}(18) = 12$.
So $AB = CD = 18$ cm and $BC = AD = 12$ cm.
The area of the rectangle is $S_{ABCD} = 18 \cdot 12 = 216$ cm$^2$.

Now let's find the lengths of the segments:
$AE = \frac{1}{3}AB = \frac{1}{3}(18) = 6$ cm.
$EB = AB - AE = 18 - 6 = 12$ cm.
$BF = \frac{2}{3}BC = \frac{2}{3}(12) = 8$ cm.
$FC = BC - BF = 12 - 8 = 4$ cm.
$G$ is the midpoint of $AD$, so $AG = GD = \frac{1}{2}AD = \frac{1}{2}(12) = 6$ cm.

We calculate the area of $\triangle EFG$ by subtracting the areas of the three corner shapes from the total area of the rectangle.
1. Area of $\triangle AGE$:
   $\triangle AGE$ is a right-angled triangle at $A$.
   $S_{AGE} = \frac{1}{2} \cdot AG \cdot AE = \frac{1}{2} \cdot 6 \cdot 6 = 18$ cm$^2$.

2. Area of $\triangle EBF$:
   $\triangle EBF$ is a right-angled triangle at $B$.
   $S_{EBF} = \frac{1}{2} \cdot EB \cdot BF = \frac{1}{2} \cdot 12 \cdot 8 = 48$ cm$^2$.

3. Area of trapezoid $GDCF$:
   $GD \parallel FC$ (since $AD \parallel BC$).
   Height is $DC = AB = 18$ cm.
   $S_{GDCF} = \frac{GD + FC}{2} \cdot DC = \frac{6 + 4}{2} \cdot 18 = \frac{10}{2} \cdot 18 = 5 \cdot 18 = 90$ cm$^2$.

Total area to subtract:
$S_{sub} = 18 + 48 + 90 = 156$ cm$^2$.

Area of $\triangle EFG$:
$S_{EFG} = S_{ABCD} - S_{sub} = 216 - 156 = 60$ cm$^2$.

The area of triangle $EFG$ is $60$ cm$^2$.

![Rectangle Area](images/geom_8_2018_rect.png)

## 💡 Решение

1.  **Одредување на страните на правоаголникот:**
    Периметарот е $L = 2(AB + BC) = 60$, па $AB + BC = 30$.
    Дадено е $BC = \frac{2}{3}AB$.
    Заменуваме во равенката:
    $$ AB + \frac{2}{3}AB = 30 $$
    $$ \frac{5}{3}AB = 30 \implies AB = 30 \cdot \frac{3}{5} = 18 \text{ cm} $$
    $$ BC = \frac{2}{3} \cdot 18 = 12 \text{ cm} $$
    Плоштината на правоаголникот е $P_{ABCD} = 18 \cdot 12 = 216 \text{ cm}^2$.

2.  **Одредување на положбата на точките:**
    *   $AE = \frac{1}{3}AB = \frac{1}{3} \cdot 18 = 6$. Тогаш $EB = 18 - 6 = 12$.
    *   $BF = \frac{2}{3}BC = \frac{2}{3} \cdot 12 = 8$. Тогаш $FC = 12 - 8 = 4$.
    *   $G$ е средина на $AD$, па $AG = GD = \frac{1}{2}AD = \frac{1}{2} \cdot 12 = 6$.

3.  **Пресметка на плоштината на $\triangle EFG$:**
    Од плоштината на правоаголникот ги одземаме плоштините на фигурите во ќошевите:
    *   $\triangle AGE$ (правоаголен кај $A$):
        $$ P_{AGE} = \frac{1}{2} \cdot AG \cdot AE = \frac{1}{2} \cdot 6 \cdot 6 = 18 $$
    *   $\triangle EBF$ (правоаголен кај $B$):
        $$ P_{EBF} = \frac{1}{2} \cdot EB \cdot BF = \frac{1}{2} \cdot 12 \cdot 8 = 48 $$
    *   Трапез $GDCF$ (прав агол кај $D$ и $C$, висина $DC$):
        Основи се $GD=6$ и $FC=4$. Висината е $DC=AB=18$.
        $$ P_{GDCF} = \frac{GD + FC}{2} \cdot DC = \frac{6 + 4}{2} \cdot 18 = 5 \cdot 18 = 90 $$

    Вкупната плоштина што се одзема е:
    $$ P_{sub} = 18 + 48 + 90 = 156 $$

    Плоштината на $\triangle EFG$ е:
    $$ P_{EFG} = P_{ABCD} - P_{sub} = 216 - 156 = 60 \text{ cm}^2 $$

Конечниот резултат е $60 \text{ cm}^2$.