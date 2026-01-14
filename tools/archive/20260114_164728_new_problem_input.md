---
problem_id: sigma_133_1_2
title: Систем линеарни неравенки со целобројни параметри
grade: 9
difficulty: 4
type: algebra
tags:
  - системи_неравенки
  - целобројни_решенија
  - комбинаторика
  - сигма_задачи
primary_skill: анализа_на_бројна_права
related_skills:
  - линеарни_неравенки
  - пребројување
source: Сигма 133, Рубрика „Задачи од училница“
---

# Систем линеарни неравенки со целобројни параметри

# Текст на задачата
Нека $a$ и $b$ се два цели броја такви што целобројните решенија на системот неравенки:

$$
\begin{cases} 
9x - a \ge 0 \\ 
8x - b < 0 
\end{cases}
$$

се само броевите 1, 2 и 3. Одреди го бројот на целобројни подредени парови $(a, b)$ кои го задоволуваат системот.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Прво, реши ги двете неравенки поединечно по променливата $x$. Изрази го $x$ преку параметрите $a$ и $b$.

$$x \ge \frac{a}{9} \quad \text{и} \quad x < \frac{b}{8}$$

2. Бидејќи решенијата се 1, 2 и 3, бројот 1 мора да биде во интервалот, а бројот 0 не смее. Каде треба да се наоѓа границата $\frac{a}{9}$?

$$0 < \frac{a}{9} \le 1$$

3. Слично, бројот 3 мора да биде внатре, а бројот 4 мора да биде надвор. Каде треба да биде границата $\frac{b}{8}$? Внимавај на строгиот знак кај втората неравенка!

$$3 < \frac{b}{8} \le 4$$

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Оваа задача бара прецизна контрола на интервалите на бројната права. Клучниот **тригер** е условот „целобројните решенија се само 1, 2 и 3“. Ова значи дека интервалот кој го формира системот мора да биде доволно широк за да ги „зароби“ овие три броја, но доволно тесен за да не ги вклучи 0 или 4.

**Зошто е важна природата на знаците?** 
Првата неравенка е нестрога ($\ge$), што значи дека левата граница $\frac{a}{9}$ може да биде точно 1 (тогаш 1 е вклучен), но мора да биде строго поголема од 0 (ако е 0, тогаш и 0 ќе биде решение). 
Втората неравенка е строга ($<$), што значи дека десната граница $\frac{b}{8}$ мора да биде строго поголема од 3 (за да го опфати 3), но може да биде точно 4 (бидејќи $x < 4$ не го вклучува 4).

Детективската работа се сведува на решавање на овие „гранични“ неравенки за $a$ и $b$ и пребројување на можните цели вредности. Олимпискиот стандард бара внимателност со знаците за еднаквост — тука се губат или добиваат поени.

### 🔗 Поврзани вештини
* **Примарна вештина:** Анализа на системи неравенки
* **Потребни предзнаења:** Својства на линеарни неравенки, основни принципи на пребројување.

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 1, 1],
            axis_config={"color": BLACK, "include_tip": True},
            tips=False
        )
        number_line = axes.get_x_axis()
        labels = axes.get_coordinate_labels(range(0, 6))
        dots = VGroup(*[Dot(axes.c2p(i, 0), color=BLUE, radius=0.1) for i in [1, 2, 3]])
        forbidden = VGroup(*[Dot(axes.c2p(i, 0), color=RED, radius=0.1) for i in [0, 4]])
        ineq_a = MathTex("0 < \\frac{a}{9} \\leq 1", color=BLACK).to_edge(UP).shift(LEFT * 3)
        ineq_b = MathTex("3 < \\frac{b}{8} \\leq 4", color=BLACK).to_edge(UP).shift(RIGHT * 3)
        bracket = MathTex("[", color=BLUE).move_to(axes.c2p(0.5, 0))
        parenthesis = MathTex(")", color=BLUE).move_to(axes.c2p(3.5, 0))
        interval_line = Line(axes.c2p(0.5, 0), axes.c2p(3.5, 0), color=BLUE, stroke_width=6)
        calc = VGroup(
            MathTex("a \\in \\{1, 2, \\dots, 9\\} \\rightarrow 9", color=BLACK),
            MathTex("b \\in \\{25, 26, \\dots, 32\\} \\rightarrow 8", color=BLACK),
            MathTex("Total: 9 \\times 8 = 72", color=BLUE)
        ).arrange(DOWN, buff=0.3).to_edge(DOWN)
        self.add(axes, labels, dots, forbidden, ineq_a, ineq_b, bracket, parenthesis, interval_line, calc)
        final_box = SurroundingRectangle(calc, color=RED, buff=0.1)
        self.play(Create(final_box))
        self.wait(2)
```
---
problem_id: sigma_133_1_2
title: Систем линеарни неравенки со целобројни параметри
grade: 9
difficulty: 4
type: algebra
tags:
  - системи_неравенки
  - целобројни_решенија
  - комбинаторика
  - сигма_задачи
primary_skill: анализа_на_бројна_права
related_skills:
  - линеарни_неравенки
  - пребројување
source: Сигма 133, Рубрика „Задачи од училница“
---

# Систем линеарни неравенки со целобројни параметри

# Текст на задачата
Нека $a$ и $b$ се два цели броја такви што целобројните решенија на системот неравенки:

$$
\begin{cases} 
9x - a \ge 0 \\ 
8x - b < 0 
\end{cases}
$$

се само броевите 1, 2 и 3. Одреди го бројот на целобројни подредени парови $(a, b)$ кои го задоволуваат системот.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Прво, реши ги двете неравенки поединечно по променливата $x$. Изрази го $x$ преку параметрите $a$ и $b$.

$$x \ge \frac{a}{9} \quad \text{и} \quad x < \frac{b}{8}$$

2. Бидејќи решенијата се 1, 2 и 3, бројот 1 мора да биде во интервалот, а бројот 0 не смее. Каде треба да се наоѓа границата $\frac{a}{9}$?

$$0 < \frac{a}{9} \le 1$$

3. Слично, бројот 3 мора да биде внатре, а бројот 4 мора да биде надвор. Каде треба да биде границата $\frac{b}{8}$? Внимавај на строгиот знак кај втората неравенка!

$$3 < \frac{b}{8} \le 4$$

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Оваа задача бара прецизна контрола на интервалите на бројната права. Клучниот **тригер** е условот „целобројните решенија се само 1, 2 и 3“. Ова значи дека интервалот кој го формира системот мора да биде доволно широк за да ги „зароби“ овие три броја, но доволно тесен за да не ги вклучи 0 или 4.

**Зошто е важна природата на знаците?** 
Првата неравенка е нестрога ($\ge$), што значи дека левата граница $\frac{a}{9}$ може да биде точно 1 (тогаш 1 е вклучен), но мора да биде строго поголема од 0 (ако е 0, тогаш и 0 ќе биде решение). 
Втората неравенка е строга ($<$), што значи дека десната граница $\frac{b}{8}$ мора да биде строго поголема од 3 (за да го опфати 3), но може да биде точно 4 (бидејќи $x < 4$ не го вклучува 4).

Детективската работа се сведува на решавање на овие „гранични“ неравенки за $a$ и $b$ и пребројување на можните цели вредности. Олимпискиот стандард бара внимателност со знаците за еднаквост — тука се губат или добиваат поени.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Решавање на системот по x</summary>

Го средуваме системот во форма на интервал за $x$:

$$9x \ge a \implies x \ge \frac{a}{9}$$
$$8x < b \implies x < \frac{b}{8}$$

Целобројните решенија за $x$ лежат во интервалот $[\frac{a}{9}, \frac{b}{8})$.

</details>

<details>
<summary>Чекор 2: Определување на опсегот за параметарот a</summary>

Целобројните решенија се 1, 2 и 3. Најмалото решение е 1. Тоа значи:
- $\frac{a}{9} \le 1$ (за да биде 1 вклучено како решение).
- $\frac{a}{9} > 0$ (за да биде 0 исклучено).

Од системот $0 < \frac{a}{9} \le 1$ добиваме:
$$0 < a \le 9$$

Бидејќи $a$ е цел број, можни вредности се $a \in \{1, 2, 3, 4, 5, 6, 7, 8, 9\}$. Ова се вкупно **9 избори** за $a$.

</details>

<details>
<summary>Чекор 3: Определување на опсегот за параметарот b</summary>

Најголемото решение е 3, а следното (исклучено) е 4. Поради строгата неравенка $x < \frac{b}{8}$:
- $\frac{b}{8} > 3$ (за да биде 3 вклучено; ако $\frac{b}{8} = 3$, тогаш $x < 3$ не го вклучува 3).
- $\frac{b}{8} \le 4$ (за да биде 4 исклучено; ако $\frac{b}{8} = 4$, тогаш $x < 4$ не го вклучува 4).

Од системот $3 < \frac{b}{8} \le 4$ добиваме:
$$24 < b \le 32$$

Бидејќи $b$ е цел број, можни вредности се $b \in \{25, 26, 27, 28, 29, 30, 31, 32\}$. Ова се вкупно **8 избори** за $b$.

</details>

<details>
<summary>Чекор 4: Пресметка на вкупниот број на парови</summary>

Бројот на подредени парови $(a, b)$ е производ од бројот на избори за $a$ и бројот на избори за $b$:

$$\text{Вкупно парови} = 9 \times 8 = 72$$

Паровите се од облик $(1, 25), (1, 26), \dots, (9, 32)$.

</details>

**Краен одговор:** Постојат $\boxed{72}$ такви подредени парови.

## 👨‍🏫 Менторски Белешки
1. **Златен Совет:** Кај неравенки со параметри каде се бараат специфични цели решенија, секогаш цртај ја бројната права. „Заглави“ ги посакуваните решенија меѓу нивните најблиски соседи (0 и 4 во овој случај).
2. **Чести Грешки:** Најчеста грешка е кај втората граница: учениците пишуваат $\frac{b}{8} < 4$, заборавајќи дека бидејќи неравенката во системот е строга ($x < \dots$), самата граница може да биде точно 4.
3. **Зошто ова е важно:** Оваа задача го вежба логичкото резонирање и транзицијата од алгебарски изрази кон дискретни пребројувања, што е основа за посериозни задачи од комбинаторика и теорија на броеви.

### 🔗 Поврзани вештини
* **Примарна вештина:** Анализа на системи неравенки
* **Потребни предзнаења:** Својства на линеарни неравенки, основни принципи на пребројување.

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        # Expert Tip 1: Setting background to WHITE for print-ready diagrams
        self.camera.background_color = WHITE
        
        # Expert Tip 7: Using c2p for precise mathematical coordinate positioning
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 1, 1],
            axis_config={"color": BLACK, "include_tip": True},
            tips=False
        )
        
        # Number line with integer markers
        number_line = axes.get_x_axis()
        labels = axes.get_coordinate_labels(range(0, 6), color=BLACK)
        
        # Expert Tip 9: Using always_redraw for structural changes in visual markers
        # Highlighting the allowed integer solutions {1, 2, 3}
        dots = VGroup(*[Dot(axes.c2p(i, 0), color=BLUE, radius=0.1) for i in])
        forbidden = VGroup(*[Dot(axes.c2p(i, 0), color=RED, radius=0.1) for i in])
        
        # Expert Tip 16: Mathematical LaTeX transformations for constraints
        # No Cyrillic characters allowed inside MathTex (Tip 96)
        ineq_a = MathTex("0 < \\frac{a}{9} \\leq 1", color=BLACK).to_edge(UP).shift(LEFT * 3)
        ineq_b = MathTex("3 < \\frac{b}{8} \\leq 4", color=BLACK).to_edge(UP).shift(RIGHT * 3)
        
        # Visualizing the interval [a/9, b/8)
        # We use a bracket and parenthesis
        bracket = MathTex("[", color=BLUE).move_to(axes.c2p(0.5, 0))
        parenthesis = MathTex(")", color=BLUE).move_to(axes.c2p(3.5, 0))
        interval_line = Line(axes.c2p(0.5, 0), axes.c2p(3.5, 0), color=BLUE, stroke_width=6)
        
        # Expert Tip 19 & 23: VGroup for logical alignment
        calc = VGroup(
            MathTex("a \\in \{1, 2, \dots, 9\} \\rightarrow 9", color=BLACK),
            MathTex("b \\in \{25, 26, \dots, 32\} \\rightarrow 8", color=BLACK),
            MathTex("Total: 9 \\times 8 = 72", color=BLUE)
        ).arrange(DOWN, buff=0.3).to_edge(DOWN)
        
        # Adding elements to scene
        self.add(axes, labels, dots, forbidden, ineq_a, ineq_b, bracket, parenthesis, interval_line, calc)
        
        # Expert Tip 15: Natural equation rearrangement with path_arc
        # Simulation of a key transformation step
        final_box = SurroundingRectangle(calc, color=RED, buff=0.1)
        self.play(Create(final_box))
        self.wait(2)
```