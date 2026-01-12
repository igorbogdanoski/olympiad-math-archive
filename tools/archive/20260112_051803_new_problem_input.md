---
problem_id: algebra_func_sum_1884
title: Сума на функционални вредности со симетрија
grade: 10
difficulty: 5
type: algebra
tags:
  - functional_equation
  - summation
  - symmetry
primary_skill: symmetry_pairing
related_skills:
  - exponents
  - algebraic_manipulation
source: Zbirka_Alg_1884
---

# Сума на функционални вредности со симетрија

# Текст на задачата
Нека функцијата е дефинирана со:

$$f(x) = \frac{a^x}{a^x + \sqrt{a}}$$

каде $a \in \mathbb{R}^+$. Најди ја вредноста на изразот:

$$S = f\left(\frac{1}{101}\right) + f\left(\frac{2}{101}\right) + \dots + f\left(\frac{100}{101}\right)$$

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Пресметување на секој член поединечно е невозможно. Забележи ја симетријата во аргументите: првиот е $\frac{1}{101}$, а последниот е $\frac{100}{101}$. Колку е нивниот збир?

$$x + y = \frac{1}{101} + \frac{100}{101} = 1$$

2. Обиди се да го пресметаш збирот $f(x) + f(1-x)$. Ако овој збир е константа, задачата е речиси решена.

$$f(1-x) = \frac{a^{1-x}}{a^{1-x} + \sqrt{a}}$$

3. Упрости го изразот за $f(1-x)$ така што ќе го прошириш дропката со $a^x$. Потоа собери го со $f(x)$.

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Кога гледаме ваква сума со многу членови (во овој случај 100), веднаш знаеме дека не треба да ги собираме „пеш“. Мора да постои некое својство на функцијата што ги „парира“ членовите.

Гледаме дека аргументите се движат од $\frac{1}{101}$ до $\frac{100}{101}$.
Забележуваме дека првиот и последниот аргумент даваат збир 1:
$$\frac{1}{101} + \frac{100}{101} = 1$$
Истото важи и за вториот и претпоследниот:
$$\frac{2}{101} + \frac{99}{101} = 1$$

Ова ни сугерира да истражиме што се случува со збирот $f(x) + f(1-x)$. Ова е познат „трик“ во олимписката математика за функции од обликот $\frac{b^x}{b^x + \sqrt{b}}$. Ако докажеме дека овој збир е 1, тогаш целата сума се сведува на броење на парови.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Анализа на симетријата $f(x) + f(1-x)$</summary>

Да го пресметаме изразот $f(1-x)$:

$$f(1-x) = \frac{a^{1-x}}{a^{1-x} + \sqrt{a}}$$

Го запишуваме $a^{1-x}$ како $\frac{a}{a^x}$:

$$f(1-x) = \frac{\frac{a}{a^x}}{\frac{a}{a^x} + \sqrt{a}}$$

Ја множиме дропката (и броителот и именителот) со $a^x$ за да се ослободиме од двојната дропка:

$$f(1-x) = \frac{a}{a + a^x\sqrt{a}}$$

Сега, извлекуваме $\sqrt{a}$ пред заграда во именителот (бидејќи $a = (\sqrt{a})^2$):

$$f(1-x) = \frac{(\sqrt{a})^2}{\sqrt{a}(\sqrt{a} + a^x)} = \frac{\sqrt{a}}{a^x + \sqrt{a}}$$

</details>

<details>
<summary>Чекор 2: Пресметка на збирот на парот</summary>

Сега ги собираме $f(x)$ и $f(1-x)$. Забележуваме дека имаат ист именител:

$$f(x) + f(1-x) = \frac{a^x}{a^x + \sqrt{a}} + \frac{\sqrt{a}}{a^x + \sqrt{a}}$$

$$f(x) + f(1-x) = \frac{a^x + \sqrt{a}}{a^x + \sqrt{a}} = 1$$

Ова е клучното откритие: **Збирот на вредностите на функцијата за два аргументи чиј збир е 1, е секогаш 1.**

</details>

<details>
<summary>Чекор 3: Групирање на сумата</summary>

Дадената сума е:

$$S = f\left(\frac{1}{101}\right) + f\left(\frac{2}{101}\right) + \dots + f\left(\frac{50}{101}\right) + f\left(\frac{51}{101}\right) + \dots + f\left(\frac{100}{101}\right)$$

Ги групираме првиот со последниот, вториот со претпоследниот, итн.:

$$S = \left[ f\left(\frac{1}{101}\right) + f\left(\frac{100}{101}\right) \right] + \left[ f\left(\frac{2}{101}\right) + f\left(\frac{99}{101}\right) \right] + \dots + \left[ f\left(\frac{50}{101}\right) + f\left(\frac{51}{101}\right) \right]$$

Бидејќи $\frac{k}{101} + \frac{101-k}{101} = 1$, секоја заграда има вредност 1.

</details>

<details>
<summary>Чекор 4: Броење на парови</summary>

Вкупно имаме 100 собироци (од 1 до 100).
Кога ги групираме во парови, добиваме точно $\frac{100}{2} = 50$ парови.

$$S = \underbrace{1 + 1 + \dots + 1}_{50 \text{ пати}} = 50$$

</details>

**Краен одговор:** Вредноста на изразот е $\boxed{50}$.

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Кога ќе видите функција со експоненти во дропка од типот $\frac{a^x}{a^x + \sqrt{a}}$ или $\frac{4^x}{4^x+2}$, тоа е скоро секогаш задача со симетрија околу $x=1/2$. Веднаш проверете $f(x) + f(1-x)$.
2.  **Чести Грешки:** Внимавајте на бројот на членови. Ако именителот беше 100 (наместо 101), ќе имавме членови $\frac{1}{100}, \dots, \frac{99}{100}$. Тоа се 99 членови. Ќе имавме 49 парови и еден среден член $f(50/100) = f(1/2)$ кој останува сам. Во нашата задача бројот на членови е парен (100), па нема „осамен“ член во средината.
3.  **Зошто ова е важно:** Оваа задача илустрира како својствата на функциите (симетрија) можат да претворат сложена пресметка во едноставно броење.

### 🔗 Поврзани вештини
* **Примарна вештина:** Симетрично парирање (Symmetry Pairing).
* **Потребни предзнаења:** Степенување, работа со дропки.

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # --- Setup Axes ---
        axes = Axes(
            x_range=[0, 1.2, 0.5],
            y_range=[0, 1.2, 0.5],
            axis_config={"color": BLACK, "include_numbers": True},
            x_length=6,
            y_length=5
        ).shift(DOWN * 0.5)
        
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        # --- Function Definition ---
        # Let a = 4 for visualization, so sqrt(a) = 2
        # f(x) = 4^x / (4^x + 2)
        def func(x):
            return (4**x) / (4**x + 2)
        
        graph = axes.plot(func, x_range=[0, 1], color=BLUE, stroke_width=4)
        
        # --- Visualization of Symmetry ---
        # Pick a point x = 0.2
        x_val = 0.2
        x_sym = 1 - x_val
        
        y_val = func(x_val)
        y_sym = func(x_sym)
        
        # Points
        pt_1 = Dot(axes.c2p(x_val, y_val), color=RED)
        pt_2 = Dot(axes.c2p(x_sym, y_sym), color=RED)
        
        # Lines
        line_1 = axes.get_vertical_line(axes.c2p(x_val, y_val), line_config={"dashed_ratio": 0.5, "color": RED})
        line_2 = axes.get_vertical_line(axes.c2p(x_sym, y_sym), line_config={"dashed_ratio": 0.5, "color": RED})
        
        # Labels
        lbl_x = MathTex("x", color=BLACK).next_to(line_1, DOWN)
        lbl_1_x = MathTex("1-x", color=BLACK).next_to(line_2, DOWN)
        
        # Equation Text
        eq_text = MathTex("f(x) + f(1-x) = 1", color=BLUE).to_edge(UP)
        
        # --- Animation ---
        self.add(axes, labels)
        self.play(Create(graph), run_time=2)
        self.wait(0.5)
        
        self.play(FadeIn(pt_1), Create(line_1), Write(lbl_x))
        self.play(FadeIn(pt_2), Create(line_2), Write(lbl_1_x))
        
        # Show the sum visually
        # We can show that the height of pt_2 plus height of pt_1 equals 1 (top of box)
        
        # Draw line at y=1
        line_top = DashedLine(axes.c2p(0, 1), axes.c2p(1, 1), color=GRAY)
        self.play(Create(line_top))
        
        # Brace for f(x)
        brace_1 = Brace(Line(axes.c2p(x_val, 0), axes.c2p(x_val, y_val)), LEFT, color=RED)
        txt_1 = brace_1.get_text("$f(x)$").set_color(RED).scale(0.7)
        
        # Brace for f(1-x)
        brace_2 = Brace(Line(axes.c2p(x_sym, 0), axes.c2p(x_sym, y_sym)), RIGHT, color=RED)
        txt_2 = brace_2.get_text("$f(1-x)$").set_color(RED).scale(0.7)
        
        self.play(Create(brace_1), Write(txt_1))
        self.play(Create(brace_2), Write(txt_2))
        
        self.play(Write(eq_text))
        
        # Highlight the center point (0.5, 0.5)
        center_pt = Dot(axes.c2p(0.5, 0.5), color=GREEN)
        self.play(Transform(pt_1, center_pt), Transform(pt_2, center_pt), run_time=2)
        
        self.wait(2)
```