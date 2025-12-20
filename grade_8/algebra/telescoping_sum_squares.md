---
grade: 8
field: algebra
difficulty: 5
source: "Sigma Magazine – Problems Section"
language_original: mk
tags:
  - telescoping_sum
  - fractions
  - algebraic_manipulation
  - olympiad
---

# Телескопска сума со квадрати

## Текст на задачата
Пресметај ја вредноста на бројниот израз
$$
\frac{1^2}{1 \cdot 3} + \frac{2^2}{3 \cdot 5} + \frac{3^2}{5 \cdot 7} + \cdots + \frac{50^2}{99 \cdot 101}.
$$

## Решение

Го разгледуваме општиот член:
$$
\frac{k^2}{(2k-1)(2k+1)} = \frac{k^2}{4k^2 - 1}.
$$

Бараме разложување:
$$
\frac{k^2}{4k^2 - 1}
=
\frac14 + \frac{1}{4(4k^2 - 1)}.
$$

Затоа:
$$
\frac{k^2}{(2k-1)(2k+1)}
=
\frac14 + \frac{1}{4(2k-1)(2k+1)}.
$$

Сумираме од $k=1$ до $k=50$:
$$
\sum_{k=1}^{50} \frac14 = \frac{25}{2},
$$
и
$$
\sum_{k=1}^{50} \frac{1}{(2k-1)(2k+1)}
=
\frac12\left(1 - \frac{1}{101}\right)
=
\frac{50}{101}.
$$

Конечно:
$$
\frac{25}{2} + \frac{25}{202}
=
\frac{1275}{101}.
$$

## Заклучок
Вредноста на дадениот бројниот израз е
$$
\boxed{\frac{1275}{101}}.
$$
