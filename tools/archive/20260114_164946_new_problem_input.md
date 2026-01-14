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
				dots = VGroup(*[Dot(axes.c2p(i, 0), radius=0.1).set_color(BLUE) for i in [1, 2, 3]])
				forbidden = VGroup(*[Dot(axes.c2p(i, 0), radius=0.1).set_color(RED) for i in [0, 4]])
				ineq_a = MathTex("0 < \\frac{a}{9} \\leq 1").set_color(BLACK).to_edge(UP).shift(LEFT * 3)
				ineq_b = MathTex("3 < \\frac{b}{8} \\leq 4").set_color(BLACK).to_edge(UP).shift(RIGHT * 3)
				bracket = MathTex("[").set_color(BLUE).move_to(axes.c2p(0.5, 0))
				parenthesis = MathTex(")").set_color(BLUE).move_to(axes.c2p(3.5, 0))
				interval_line = Line(axes.c2p(0.5, 0), axes.c2p(3.5, 0)).set_color(BLUE).set_stroke(width=6)
				calc = VGroup(
						MathTex("a \\in \\{1, 2, \\dots, 9\\} \\rightarrow 9").set_color(BLACK),
						MathTex("b \\in \\{25, 26, \\dots, 32\\} \\rightarrow 8").set_color(BLACK),
						MathTex("Total: 9 \\times 8 = 72").set_color(BLUE)
				).arrange(DOWN, buff=0.3).to_edge(DOWN)
				self.add(axes, labels, dots, forbidden, ineq_a, ineq_b, bracket, parenthesis, interval_line, calc)
				final_box = SurroundingRectangle(calc, color=RED, buff=0.1)
				self.play(Create(final_box))
				self.wait(2)
```
