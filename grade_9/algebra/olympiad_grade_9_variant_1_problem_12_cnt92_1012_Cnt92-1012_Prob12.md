---
grade: 9
field: geometry
difficulty: 3
source: "<натпревар / списание / година>"
problem_id: Cnt92-1012_Prob12
language_original: <mk | en | sr | hr | ...>
translated: false

# --- GEOMETRY SKILLS ---
geometry_style: analytic # synthetic | analytic | mixed
primary_skill: <main_tool> # e.g., angle_chasing, similarity, cyclic_quads
related_skills:
  - quadratic_functions
  - optimization

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

# Најмала вредност на функција на интервал

## Текст на задачата
Најмалата вредност на функцијата $y = -x^2 + 2x + 5$ на интервалот $[-2; 2]$ изнесува:
1) 2
2) 14
3) -3
4) 2
5) -14

## 📐 Скица / Конструкција
<Опис на цртежот. Кои се клучните точки? Дали има помошни линии?>


> **👨‍💻 Manim Code (за Geo-Mentor):**
> ```python
> def construct(self):
    self.camera.background_color = WHITE
    
    # Axes
    axes = Axes(
        x_range=[-3, 4, 1],
        y_range=[-4, 8, 2],
        axis_config={"color": BLACK, "include_numbers": True},
        tips=True
    ).scale(0.8)
    
    # Function y = -x^2 + 2x + 5
    parabola = axes.plot(lambda x: -x**2 + 2*x + 5, color=BLUE)
    
    # Interval [-2, 2]
    interval_line = Line(
        start=axes.c2p(-2, 0),
        end=axes.c2p(2, 0),
        color=GREEN,
        stroke_width=6
    )
    
    # Points of interest
    # x = -2, y = -3 (Minimum on interval)
    pt_min = axes.c2p(-2, -3)
    dot_min = Dot(pt_min, color=RED, radius=0.12)
    label_min = MathTex("min(-2, -3)", color=RED).next_to(dot_min, DOWN+LEFT)
    
    # x = 1, y = 6 (Vertex - Max)
    pt_vertex = axes.c2p(1, 6)
    dot_vertex = Dot(pt_vertex, color=BLACK, radius=0.08)
    label_vertex = MathTex("V(1, 6)", color=BLACK).next_to(dot_vertex, UP)
    
    # x = 2, y = 5 (Other endpoint)
    pt_end = axes.c2p(2, 5)
    dot_end = Dot(pt_end, color=BLACK, radius=0.08)
    
    # Dashed lines for min
    dash_h = DashedLine(start=axes.c2p(0, -3), end=pt_min, color=GRAY)
    dash_v = DashedLine(start=axes.c2p(-2, 0), end=pt_min, color=GRAY)
    
    self.add(axes, parabola, interval_line, dot_min, label_min, dot_vertex, label_vertex, dot_end, dash_h, dash_v)
> ```

## 🧠 Анализа
Графикот е парабола свртена надолу ($a=-1 < 0$). Темето е максимум. Затоа, најмалата вредност на даден интервал мора да се наоѓа во една од крајните точки на интервалот. Провери ги вредностите за $x=-2$ и $x=2$.

## 📝 Решение (СИНТЕТИЧКО)
Функцијата е квадратна: $f(x) = -x^2 + 2x + 5$.

**Чекор 1: Анализа на параболата**
Коефициентот пред $x^2$ е $-1$, што значи параболата е свртена надолу (има облик на $\cap$).
Темето на параболата е во $x_v = -\frac{b}{2a} = -\frac{2}{-2} = 1$.
Бидејќи параболата е свртена надолу, во темето $x=1$ функцијата има **максимум**.

**Чекор 2: Проверка на интервалот**
Интервалот е $[-2; 2]$. Темето $x=1$ припаѓа на интервалот, но бидејќи бараме **најмала** вредност (минимум), а темето е максимум, минимумот мора да биде во една од крајните точки.

**Чекор 3: Пресметка во крајните точки**
*   За $x = -2$:
    $y = -(-2)^2 + 2(-2) + 5 = -4 - 4 + 5 = -3$
*   За $x = 2$:
    $y = -(2)^2 + 2(2) + 5 = -4 + 4 + 5 = 5$

**Заклучок:**
Споредуваме: $-3$ и $5$. Најмалата вредност е $-3$.

Точниот одговор е опцијата **3) -3**.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
<Краен резултат.>