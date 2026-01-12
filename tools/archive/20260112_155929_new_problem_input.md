---
problem_id: regional_2025_3_3a
title: Плоштина на триаголник преку збир на квадрати на страни и котангенси
grade: 11
difficulty: 5
type: geometry
tags:
  - trigonometrija
  - plostina_na_triagolnik
  - kosinusna_teorema
  - kotangens
primary_skill: trigonometriska_manipulacija
related_skills:
  - sinusna_formula_za_plostina
  - algebarski_identiteti
source: Регионален натпревар по математика 2025 (Сигма 139, стр. 55-56)
---

# Плоштина на триаголник преку збир на квадрати на страни и котангенси

# Текст на задачата
Збирот на квадратите на страните на даден триаголник е $M$, а збирот на котангенсите на неговите внатрешни агли е $N$. Изрази ја плоштината на триаголникот преку $M$ и $N$.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Поврзете ги страните и аглите на триаголникот користејќи ја косинусната теорема за секоја страна поединечно.

$$a^2 = b^2 + c^2 - 2bc \cos \alpha$$

2. Изразете го производот на две страни (на пр. $bc$) преку плоштината $P$ и синусот на аголот меѓу нив.

$$P = \frac{1}{2}bc \sin \alpha$$

3. Комбинирајте ги овие два изрази за да добиете котангенс. Забележете како $\frac{\cos \alpha}{\sin \alpha}$ природно се појавува во равенката.

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Кога ќе ја видиме задачата, веднаш забележуваме две различни класи на податоци: страни ($a, b, c$) и агли ($\alpha, \beta, \gamma$). Нашата цел е да најдеме мост помеѓу квадратите на страните и котангенсите на аглите.

**Тригерот:** Што е она што ги поврзува две страни и еден агол? Тоа е Косинусната теорема. Но, таа ни дава $\cos \alpha$. Од друга страна, плоштината $P$ најчесто ја изразуваме преку $\sin \alpha$. Бидејќи $\cot \alpha = \frac{\cos \alpha}{\sin \alpha}$, логичниот чекор е да ги „споиме" овие две формули.

Дали е доволно да го направиме тоа само за еден агол? Не, бидејќи $M$ и $N$ се збирови. Искуството ни вели дека ако го примениме овој процес за сите три страни и ги собереме резултатите, линеарните комбинации на квадратите на страните ќе се „исчистат" и ќе ја добиеме бараната врска.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Поврзување на страните и аглите преку косинусна теорема</summary>

Нека $a, b, c$ се страните, а $\alpha, \beta, \gamma$ се соодветните внатрешни агли на триаголникот. Користиме косинусна теорема за страната $a$:

$$a^2 = b^2 + c^2 - 2bc \cos \alpha$$

Од оваа равенка, можеме да го изразиме членот со косинус:

$$2bc \cos \alpha = b^2 + c^2 - a^2$$

</details>

<details>
<summary>Чекор 2: Воведување на плоштината и котангенсот</summary>

Знаеме дека плоштината $P$ на триаголникот може да се запише како:

$$P = \frac{1}{2}bc \sin \alpha \implies bc = \frac{2P}{\sin \alpha}$$

Го заменуваме овој израз за $bc$ во равенката од претходниот чекор:

$$2 \left( \frac{2P}{\sin \alpha} \right) \cos \alpha = b^2 + c^2 - a^2$$

$$4P \frac{\cos \alpha}{\sin \alpha} = b^2 + c^2 - a^2$$

$$4P \cot \alpha = b^2 + c^2 - a^2$$

</details>

<details>
<summary>Чекор 3: Сумирање за сите три агли</summary>

Аналогно на претходниот чекор, ги запишуваме изразите за другите два агли:

$$4P \cot \beta = a^2 + c^2 - b^2$$

$$4P \cot \gamma = a^2 + b^2 - c^2$$

Сега ги собираме трите равенки:

$$4P(\cot \alpha + \cot \beta + \cot \gamma) = (b^2 + c^2 - a^2) + (a^2 + c^2 - b^2) + (a^2 + b^2 - c^2)$$

</details>

<details>
<summary>Чекор 4: Финализирање на изразот</summary>

На левата страна го препознаваме дадениот збир $N = \cot \alpha + \cot \beta + \cot \gamma$. На десната страна, по кратење на членовите, добиваме:

$$4P \cdot N = a^2 + b^2 + c^2$$

Бидејќи по услов $a^2 + b^2 + c^2 = M$, равенката станува:

$$4PN = M$$

Од каде што за плоштината $P$ добиваме:

$$P = \frac{M}{4N}$$

</details>

**Краен одговор:** $\boxed{P = \frac{M}{4N}}$

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Овој идентитет, $a^2 + b^2 + c^2 = 4P \sum \cot \alpha$, е многу корисен во олимписката геометрија и често се нарекува идентитет на котангенси.
2.  **Чести Грешки:** Внимавајте при кратењето на десната страна во Чекор 3. Учениците често грешат во предзнаците.
3.  **Зошто ова е важно:** Оваа задача нè учи како да ги користиме основните тригонометриски теореми.

### 🔗 Поврзани вештини
* **Примарна вештина:** Тригонометриска манипулација
* **Потребни предзнаења:** Косинусна теорема, Синусна формула за плоштина

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # --- CONFIGURATION ---
        # Define a generic triangle
        A = np.array([0, 3, 0])
        B = np.array([-3, -1, 0])
        C = np.array([3, -1, 0])
        
        triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
        
        # Labels for sides
        lbl_c = MathTex("c", color=BLACK).move_to((A + B) / 2 + LEFT * 0.3)
        lbl_b = MathTex("b", color=BLACK).move_to((A + C) / 2 + RIGHT * 0.3)
        lbl_a = MathTex("a", color=BLACK).move_to((B + C) / 2 + DOWN * 0.3)
        
        # Labels for angles
        alpha = MathTex(r"\alpha", color=RED).scale(0.8).next_to(A, DOWN, buff=0.2)
        beta = MathTex(r"\beta", color=RED).scale(0.8).next_to(B, UR, buff=0.2)
        gamma = MathTex(r"\gamma", color=RED).scale(0.8).next_to(C, UL, buff=0.2)
        
        # Identity to display
        identity = MathTex(r"M = a^2 + b^2 + c^2", color=BLUE).to_edge(UP, buff=0.5)
        identity2 = MathTex(r"N = \cot \alpha + \cot \beta + \cot \gamma", color=BLUE).next_to(identity, DOWN)
        
        # Final Result
        result = MathTex(r"P = \frac{M}{4N}", color=BLACK).scale(1.5).to_edge(DOWN, buff=0.5)
        box = SurroundingRectangle(result, color=BLACK, buff=0.2)
        
        # --- ADDING TO SCENE ---
        self.add(triangle, lbl_a, lbl_b, lbl_c, alpha, beta, gamma)
        self.add(identity, identity2, result, box)
```
