---
problem_id: sigma139_y1_p4
title: Плоштини на триаголници и линеарна функција
grade: 9
difficulty: 4
tags:
  - analytic_geometry
  - area
  - similar_triangles
  - linear_function
source: Sigma 139, Prva godina, Zadaca 4
type: geometry
---

# Текст на задачата
Во координатниот систем на цртежот е конструирана правата $y = -x + b$, каде што $0 < b < 4$. Притоа важи $P_{\triangle QRS} : P_{\triangle QOP} = 9 : 25$. Најди ја вредноста на $b$.

# Решение
## Стратегија
Задачата поврзува аналитичка геометрија (равенка на права) со геометрија на триаголник (плоштина).
1.  Прво ќе ги определиме координатите на сите клучни точки ($P, Q, R, S$) во зависност од параметарот $b$.
2.  Ќе ги изразиме должините на катетите на правоаголните триаголници $\triangle QOP$ и $\triangle QRS$.
3.  Ќе ги пресметаме нивните плоштини како функција од $b$.
4.  Ќе ја поставиме пропорцијата дадена во условот и ќе ја решиме равенката за $b$.

*Алтернативно:* Може да се забележи дека триаголниците се слични (па дури и рамнокраки правоаголни поради коефициентот на правец $-1$), па односот на плоштините е квадрат од односот на страните.

## Чекор по чекор

**Чекор 1: Определување на координатите на точките**
Правата е дадена со равенката $y = -x + b$.
*   **Точка $P$:** Ова е пресекот со $y$-оската (каде $x=0$).
    $y = -0 + b \Rightarrow y = b$.
    Значи, $P(0, b)$.
*   **Точка $Q$:** Ова е пресекот со $x$-оската (каде $y=0$).
    $0 = -x + b \Rightarrow x = b$.
    Значи, $Q(b, 0)$.
*   **Точка $O$:** Координатниот почеток $O(0, 0)$.
*   **Точка $R$:** Дадена е на цртежот како $R(4, 0)$.
*   **Точка $S$:** Оваа точка лежи на правата $x=4$ (вертикалата спуштена од $R$) и на правата $y = -x + b$.
    Заменуваме $x=4$ во равенката на правата:
    $y = -4 + b = b - 4$.
    Значи, $S(4, b - 4)$.

**Чекор 2: Изразување на должините на страните**
Бидејќи $0 < b < 4$, знаеме дека $Q$ се наоѓа помеѓу $O$ и $R$.
*   **За $\triangle QOP$:**
    *   Катета $OQ = |x_Q - x_O| = |b - 0| = b$.
    *   Катета $OP = |y_P - y_O| = |b - 0| = b$.
    *(Забелешка: Триаголникот е рамнокрак правоаголен).*

*   **За $\triangle QRS$:**
    *   Катета $QR = |x_R - x_Q| = |4 - b| = 4 - b$ (бидејќи $b < 4$).
    *   Катета $RS = |y_S - y_R| = |(b - 4) - 0| = |b - 4|$. Бидејќи $b < 4$, вредноста $b-4$ е негативна, па должината е $-(b-4) = 4 - b$.
    *(Забелешка: И овој триаголник е рамнокрак правоаголен).*

**Чекор 3: Пресметка на плоштините**
Плоштина на правоаголен триаголник е половина од производот на катетите.
$$ P_{\triangle QOP} = \frac{1}{2} \cdot OQ \cdot OP = \frac{1}{2} \cdot b \cdot b = \frac{b^2}{2} $$
$$ P_{\triangle QRS} = \frac{1}{2} \cdot QR \cdot RS = \frac{1}{2} \cdot (4 - b) \cdot (4 - b) = \frac{(4 - b)^2}{2} $$

**Чекор 4: Поставување и решавање на равенката**
Даден е условот:
$$ \frac{P_{\triangle QRS}}{P_{\triangle QOP}} = \frac{9}{25} $$

Заменуваме со изразите што ги добивме:
$$ \frac{\frac{(4 - b)^2}{2}}{\frac{b^2}{2}} = \frac{9}{25} $$

Ги кратиме половините:
$$ \frac{(4 - b)^2}{b^2} = \frac{9}{25} $$

Ова можеме да го запишеме како:
$$ \left( \frac{4 - b}{b} \right)^2 = \left( \frac{3}{5} \right)^2 $$

Коренуваме (бидејќи $b$ и $4-b$ се позитивни должини, го земаме само позитивниот корен):
$$ \frac{4 - b}{b} = \frac{3}{5} $$

Множиме накрсно:
$$ 5(4 - b) = 3b $$
$$ 20 - 5b = 3b $$
$$ 20 = 8b $$
$$ b = \frac{20}{8} = \frac{5}{2} = 2.5 $$

**Заклучок:**
Вредноста на $b$ е **2.5**.

# Pedagogical Notes
1.  **Основна идеја:** Координатната геометрија ни овозможува геометриските проблеми да ги претвориме во алгебарски равенки. Клучно е правилно да се определат координатите на пресечните точки (со оските и меѓу правите).
2.  **Совет од Олимпиец:** Забележете го коефициентот на правец $k = -1$. Ова значи дека правата зафаќа агол од $135^\circ$ со позитивниот дел на x-оската, односно $45^\circ$ со негативниот. Ова веднаш ни кажува дека сите правоаголни триаголници формирани со оските ќе бидат **рамнокраки** ($45^\circ-45^\circ-90^\circ$). Ова ја поедноставува пресметката бидејќи катетите се еднакви ($a=b$), па плоштината е само $a^2/2$.
3.  **Чести грешки:** Внимавајте на должината на отсечката $RS$. Координатата $y$ на точката $S$ е $b-4$, што е негативен број. Должината мора да биде позитивна, па затоа е $|b-4| = 4-b$. Ако заборавите на ова, може да добиете грешка во знакот, иако квадрирањето во плоштината често ја „крие“ оваа грешка.

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Setup axes
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-3, 5, 1],
            axis_config={"color": BLACK},
            x_length=7,
            y_length=6
        ).shift(UP*0.5)
        
        labels = axes.get_axis_labels(x_label="x", y_label="y").set_color(BLACK)
        
        # Value of b
        b_val = 2.5
        
        # Points
        O = axes.c2p(0, 0)
        P = axes.c2p(0, b_val)
        Q = axes.c2p(b_val, 0)
        R = axes.c2p(4, 0)
        S = axes.c2p(4, b_val - 4)
        
        # Line function
        line = axes.plot(lambda x: -x + b_val, color=BLUE)
        line_label = MathTex("y = -x + b", color=BLUE).next_to(line, UR).shift(LEFT*2)
        
        # Vertical line at R
        vline = Line(axes.c2p(4, 2), axes.c2p(4, -3), color=BLACK)
        
        # Triangles
        tri_QOP = Polygon(O, Q, P, fill_opacity=0.3, fill_color=GREEN, color=GREEN)
        tri_QRS = Polygon(Q, R, S, fill_opacity=0.3, fill_color=RED, color=RED)
        
        # Labels for points
        label_O = MathTex("O", color=BLACK).next_to(O, DL, buff=0.1)
        label_P = MathTex("P(0,b)", color=BLACK).next_to(P, LEFT, buff=0.1)
        label_Q = MathTex("Q(b,0)", color=BLACK).next_to(Q, DL, buff=0.1)
        label_R = MathTex("R(4,0)", color=BLACK).next_to(R, UR, buff=0.1)
        label_S = MathTex("S", color=BLACK).next_to(S, RIGHT, buff=0.1)
        
        # Animation sequence
        self.play(Create(axes), Write(labels))
        self.play(Create(line), Write(line_label))
        self.play(Create(vline))
        
        self.play(FadeIn(label_O), FadeIn(label_P), FadeIn(label_Q), FadeIn(label_R), FadeIn(label_S))
        
        self.play(DrawBorderThenFill(tri_QOP))
        self.play(DrawBorderThenFill(tri_QRS))
        
        # Annotations for lengths
        brace_b = Brace(Line(O, Q), DOWN, color=BLACK)
        text_b = brace_b.get_text("b").set_color(BLACK)
        
        brace_4mb = Brace(Line(Q, R), UP, color=BLACK)
        text_4mb = brace_4mb.get_text("4-b").set_color(BLACK)
        
        self.play(Create(brace_b), Write(text_b))
        self.play(Create(brace_4mb), Write(text_4mb))
        
        # Calculation text
        calc1 = MathTex(r"\frac{P_{\Delta QRS}}{P_{\Delta QOP}} = \frac{9}{25}", color=BLACK).to_corner(UL)
        calc2 = MathTex(r"\left(\frac{4-b}{b}\right)^2 = \frac{9}{25}", color=BLACK).next_to(calc1, DOWN)
        calc3 = MathTex(r"\frac{4-b}{b} = \frac{3}{5} \Rightarrow b = 2.5", color=RED).next_to(calc2, DOWN)
        
        self.play(Write(calc1))
        self.play(Write(calc2))
        self.play(Write(calc3))
        self.play(Indicate(calc3))
        
        self.wait(2)