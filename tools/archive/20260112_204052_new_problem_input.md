---
problem_id: regional_2025_3_4b
title: Логаритамски страни на триаголник
grade: 11
difficulty: 4
type: algebra
tags:
  - logaritmi
  - neravenstvo_na_triagolnik
  - prirodni_broevi
primary_skill: logaritamski_neravenstva
related_skills:
  - neravenstvo_na_triagolnik
  - osnova_na_logaritam
source: Сигма 139 (Регионален натпревар 2025)
---

# Логаритамски страни на триаголник

# Текст на задачата
Најди ги сите природни броеви $n$ такви што $3$, $\log_2 n$ и $\log_4 n$ се должини на страни на триаголник.

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Кој е основниот услов за три отсечки со должини $a, b, c$ да формираат триаголник?

$$a + b > c, \quad a + c > b, \quad b + c > a$$

2. Изразете ги сите логаритми со иста основа за полесно да ги споредувате должините. Како можеме да го запишеме $\log_4 n$ преку основа 2?

$$\log_4 n = \frac{\log_2 n}{\log_2 4} = \frac{1}{2} \log_2 n$$

3. Решете го системот од три неравенства за променливата $t = \log_2 n$.

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Оваа задача нè потсетува на едно од најоосновните правила во геометријата — неравенството на триаголник. Иако страните се дадени како логаритамски изрази, геометриската суштина останува иста. 

**Тригерот** овде е променливоста на две од страните. Едната страна е фиксна ($3$), додека другите две ($b = \log_2 n$ и $c = \frac{1}{2} \log_2 n$) зависат од $n$. Забележуваме дека бидејќи $n$ е природен број, мора да важи $n \ge 2$ за овие вредности да имаат смисла во контекст на триаголник (страните мора да бидат позитивни). 

Зошто ова не е само обична алгебарска задача? Бидејќи мораме да ги задоволиме сите три услови истовремено. Ако $n$ е премногу мало, збирот на двете логаритамски страни нема да ја надмине фиксната страна $3$. Ако $n$ е премногу големо, најголемата логаритамска страна ќе ги „надвладее“ другите две. Нашата цел е да го најдеме тој „балансиран“ опсег на $n$ каде триаголникот може да постои.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Поедноставување на страните на триаголникот</summary>

Да ги означиме страните на триаголникот со $a, b$ и $c$:

$$a = 3, \quad b = \log_2 n, \quad c = \log_4 n$$

Користејќи го својството за промена на основа кај логаритмите, имаме:

$$\log_4 n = \frac{\log_2 n}{\log_2 4} = \frac{\log_2 n}{2} = \frac{1}{2} \log_2 n$$

За страните да бидат реални и позитивни, мора $n > 1$. Бидејќи $n$ е природен број, следува $n \ge 2$.

</details>

<details>
<summary>Чекор 2: Поставување на неравенствата на триаголник</summary>

За овие три вредности да бидат страни на триаголник, мора да бидат исполнети следните три неравенства:

1. $b + c > a \implies \log_2 n + \frac{1}{2} \log_2 n > 3$
2. $a + c > b \implies 3 + \frac{1}{2} \log_2 n > \log_2 n$
3. $a + b > c \implies 3 + \log_2 n > \frac{1}{2} \log_2 n$

</details>

<details>
<summary>Чекор 3: Решавање на системот неравенства</summary>

Воведуваме смена $t = \log_2 n$. Системот станува:

1. $t + \frac{1}{2}t > 3 \implies \frac{3}{2}t > 3 \implies t > 2$.
2. $3 > t - \frac{1}{2}t \implies \frac{1}{2}t < 3 \implies t < 6$.
3. $3 > \frac{1}{2}t - t \implies -\frac{1}{2}t < 3 \implies t > -6$.

Бидејќи веќе имаме $t > 2$ од првото неравенство, третото неравенство ($t > -6$) е автоматски задоволено. Добиваме дека вредноста на $t$ мора да биде во интервалот:

$$2 < t < 6$$

</details>

<details>
<summary>Чекор 4: Наоѓање на вредностите за n</summary>

Се враќаме од смената $t = \log_2 n$:

$$2 < \log_2 n < 6$$

Бидејќи логаритамската функција со основа 2 е растечка, важи:

$$2^2 < n < 2^6 \implies 4 < n < 64$$

Бидејќи $n$ е природен број, решенијата се сите цели броеви од 5 до 63 вклучително.

</details>

**Краен одговор:** $\boxed{n \in \{5, 6, 7, \dots, 63\}}$

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Кај неравенства на триаголник каде страните зависат од променлива, секогаш е најефикасно да ги сведете на најпростата заедничка форма (во овој случај $\log_2 n$) пред да решавате.
2.  **Чести Грешки:** Често се заборавива дека страните мора да бидат позитивни. Иако овде $n > 4$ автоматски го гарантира тоа, кај посложени задачи тоа може да биде клучен филтер. Исто така, внимавајте на границите — неравенствата на триаголник се строги ($>$), па $n=4$ и $n=64$ не се решенија.
3.  **Зошто ова е важно:** Оваа задача ги спојува геометриските концепти со својствата на логаритмите, што е честа појава на регионалните натпревари за 11-та (трета) година.

### 🔗 Поврзани вештини
* **Примарна вештина:** Решавање логаритамски неравенства
* **Потребни предзнаења:** Неравенство на триаголник, својства на логаритми ($\log_{a^k} x = \frac{1}{k} \log_a x$).

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # --- TITLE ---
        eqn = MathTex(r"3, \log_2 n, \log_4 n \text{ are sides of a triangle}", color=BLACK).to_edge(UP)
        
        # --- NUMBER LINE ---
        # We want to visualize 4 < n < 64
        axes = NumberLine(
          x_range=[0, 70, 10],  # from 0 to 70, ticks every 10
            length=10,
            color=BLACK,
            include_numbers=True,
            label_direction=DOWN,
            font_size=24
        ).shift(DOWN * 1)
        
        # Highlight the interval (4, 64)
        interval = Line(
            axes.n2p(4), axes.n2p(64), 
            color=RED, 
            stroke_width=8
        )
        
        # Labels for boundaries
        dot_left = Dot(axes.n2p(4), color=RED)
        dot_right = Dot(axes.n2p(64), color=RED)
        
        lbl_left = MathTex("4", color=RED).next_to(dot_left, UP)
        lbl_right = MathTex("64", color=RED).next_to(dot_right, UP)
        
        # System of inequalities
        system = VGroup(
            MathTex(r"\log_2 n + \frac{1}{2}\log_2 n > 3 \implies n > 4", color=BLACK),
            MathTex(r"3 + \frac{1}{2}\log_2 n > \log_2 n \implies n < 64", color=BLACK)
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).next_to(eqn, DOWN, buff=0.5)

        # Final result box
        final = MathTex(r"n \in \{5, 6, \dots, 63\}", color=BLACK).to_edge(DOWN, buff=0.8)
        rect = SurroundingRectangle(final, color=RED)

        self.add(eqn, system, axes, interval, dot_left, dot_right, lbl_left, lbl_right, final, rect)
```