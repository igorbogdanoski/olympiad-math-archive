---
allowed_tools:
- classical_euclidean
- similarity
- symmetry
difficulty: 5
field: geometry
forbidden_tools:
- coordinate_geometry
- vectors
- complex_numbers
geometry_style: synthetic
grade: 9
language_original: <mk | en | sr | hr | ...>
primary_skill: <main_tool>
problem_id: geo_right_triangle_radii
related_skills:
- vieta_formulas
- algebraic_manipulation
related_theorems:
- vieta_formulas
- pythagorean_theorem
source: <натпревар / списание / година>
tags:
- geometry
- olympiad
translated: false
---

# Однос на катети преку радиуси

## Текст на задачата
Во правоаголен триаголник, односот на радиусите на впишаната и опишаната кружница е $2:5$. Определи го односот на катетите.

## 📐 Скица / Конструкција
![Problem_geo_right_triangle_radii](https://raw.githubusercontent.com/pc4all/olympiad-math-archive/main/media/images/manim_geo_right_triangle_radii/Problem_geo_right_triangle_radii_ManimCE_v0.19.1.png)


## 🧠 Анализа
Искористи ги формулите за радиусите во правоаголен триаголник: $r = \frac{a+b-c}{2}$ и $R = \frac{c}{2}$. Ова ќе ти даде врска помеѓу збирот на катетите $a+b$ и хипотенузата $c$. Потоа, искористи ја Питагоровата теорема за да го најдеш производот $ab$ и формирај квадратна равенка.

## 📝 Решение (СИНТЕТИЧКО)
Нека катетите се $a, b$, а хипотенузата е $c$.
Дадено е $\frac{r}{R} = \frac{2}{5}$.

### Чекор 1: Врска помеѓу $a, b, c$
Користиме формули:
$$ r = \frac{a+b-c}{2}, \quad R = \frac{c}{2} $$
Заменуваме во односот:
$$ \frac{\frac{a+b-c}{2}}{\frac{c}{2}} = \frac{2}{5} $$
$$ \frac{a+b-c}{c} = \frac{2}{5} $$
$$ \frac{a+b}{c} - 1 = \frac{2}{5} $$
$$ \frac{a+b}{c} = \frac{7}{5} \implies a+b = \frac{7}{5}c $$

### Чекор 2: Наоѓање на производот $ab$
Го квадрираме изразот за збирот:
$$ (a+b)^2 = \left(\frac{7}{5}c\right)^2 $$
$$ a^2 + 2ab + b^2 = \frac{49}{25}c^2 $$
Бидејќи $a^2 + b^2 = c^2$ (Питагора):
$$ c^2 + 2ab = \frac{49}{25}c^2 $$
$$ 2ab = \frac{49}{25}c^2 - c^2 = \frac{24}{25}c^2 $$
$$ ab = \frac{12}{25}c^2 $$

### Чекор 3: Решавање на системот
Имаме збир $S = a+b = \frac{7}{5}c$ и производ $P = ab = \frac{12}{25}c^2$.
Според Виетовите формули, $a$ и $b$ се решенија на квадратната равенка:
$$ x^2 - Sx + P = 0 $$
$$ x^2 - \frac{7}{5}cx + \frac{12}{25}c^2 = 0 $$
Множиме со 25:
$$ 25x^2 - 35cx + 12c^2 = 0 $$

Решаваме по $x$:
$$ x_{1,2} = \frac{35c \pm \sqrt{(35c)^2 - 4 \cdot 25 \cdot 12c^2}}{50} $$
$$ x_{1,2} = \frac{35c \pm \sqrt{1225c^2 - 1200c^2}}{50} $$
$$ x_{1,2} = \frac{35c \pm \sqrt{25c^2}}{50} = \frac{35c \pm 5c}{50} $$

Двете решенија се:
1. $x_1 = \frac{40c}{50} = \frac{4}{5}c$
2. $x_2 = \frac{30c}{50} = \frac{3}{5}c$

Значи катетите се $a = \frac{3}{5}c$ и $b = \frac{4}{5}c$ (или обратно).

### Чекор 4: Однос
$$ a : b = \frac{3}{5}c : \frac{4}{5}c = 3 : 4 $$

**Резултат:** Односот на катетите е $3:4$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.