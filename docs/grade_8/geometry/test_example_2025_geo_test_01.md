---
grade: 8
field: geometry
difficulty: 3
source: "<натпревар / списание / година>"
problem_id: geo_test_01
language_original: <mk | en | sr | hr | ...>
translated: false

# 
tags:
  - geometry
  - right_triangle
  - altitude
  - similarity
related_skills:
  - geometric_mean_theorem
  - euclidean_theorems
---

# Problem
In a right-angled triangle $ABC$ ($\angle C = 90^\circ$), the altitude $CD$ to the hypotenuse divides it into segments of lengths $AD=4$ cm and $BD=9$ cm. Calculate the length of the altitude $CD$.

![Problem Visualization](media/geo_test_01.mp4)

# Solution
In a right-angled triangle, the altitude to the hypotenuse is the geometric mean of the segments into which it divides the hypotenuse.
This is a consequence of the similarity of triangles $\triangle ADC \sim \triangle CDB$.
From the similarity, we have:
$$\frac{AD}{CD} = \frac{CD}{BD}$$
$$CD^2 = AD \cdot BD$$

Substituting the given values:
$$CD^2 = 4 \cdot 9 = 36$$
$$CD = \sqrt{36} = 6$$

The length of the altitude is $h = 6$ cm.

![Right Triangle Altitude](images/geo_test_01.png)

## 💡 Решение

Дадено е:
*   Правоаголен триаголник $ABC$ со прав агол во $C$.
*   Висина $CD \perp AB$.
*   Отсечки $AD = 4$ cm и $BD = 9$ cm.

Според Евклидовата теорема за висината во правоаголен триаголник, квадратот на висината е еднаков на производот од отсечките на хипотенузата:
$$ CD^2 = AD \cdot BD $$

Заменуваме со дадените вредности:
$$ CD^2 = 4 \cdot 9 $$
$$ CD^2 = 36 $$

Коренуваме за да ја добиеме должината:
$$ CD = \sqrt{36} $$
$$ CD = 6 \text{ cm} $$

Висината $CD$ изнесува $6$ cm.