---
problem_id: sigma139_p1893
title: Алгебарски идентитет со кубни корени
grade: 11
difficulty: 6
tags:
  - algebra
  - identities
  - substitution
  - radicals
source: Sigma 139, Zadaca 1893
type: algebra
---

# Текст на задачата
Ако $vw + wu + uv = uvw$ и $xu^3 = yv^3 = zw^3$, каде $u \neq 0, v \neq 0, w \neq 0$, докажи дека
$$ \sqrt[3]{x} + \sqrt[3]{y} + \sqrt[3]{z} = \sqrt[3]{xu^2 + yv^2 + zw^2} $$

# Решение
## Стратегија
Имаме два услови. Првиот услов $vw + wu + uv = uvw$ може да се трансформира со делење со $uvw$ во попознат облик: $\frac{1}{u} + \frac{1}{v} + \frac{1}{w} = 1$.
Вториот услов $xu^3 = yv^3 = zw^3$ сугерира воведување на параметар $k$. Нека $xu^3 = yv^3 = zw^3 = k^3$. Ова ќе ни овозможи да ги изразиме $x, y, z$ преку $u, v, w$ и $k$.
Потоа ќе ги замениме овие изрази во равенството што треба да се докаже и ќе видиме дали се добива идентитет.

## Чекор по чекор

**Чекор 1: Трансформација на првиот услов**
Дадено е $vw + wu + uv = uvw$.
Бидејќи $u, v, w \neq 0$, можеме да поделиме со $uvw$:
$$ \frac{vw}{uvw} + \frac{wu}{uvw} + \frac{uv}{uvw} = 1 $$
$$ \frac{1}{u} + \frac{1}{v} + \frac{1}{w} = 1 $$

**Чекор 2: Параметризација на вториот услов**
Дадено е $xu^3 = yv^3 = zw^3$.
Нека оваа заедничка вредност е $k^3$ (за полесно коренување подоцна).
$$ xu^3 = k^3 \implies x = \frac{k^3}{u^3} $$
$$ yv^3 = k^3 \implies y = \frac{k^3}{v^3} $$
$$ zw^3 = k^3 \implies z = \frac{k^3}{w^3} $$

**Чекор 3: Пресметка на левата страна (LHS)**
$$ LHS = \sqrt[3]{x} + \sqrt[3]{y} + \sqrt[3]{z} $$
Заменуваме со изразите од Чекор 2:
$$ LHS = \sqrt[3]{\frac{k^3}{u^3}} + \sqrt[3]{\frac{k^3}{v^3}} + \sqrt[3]{\frac{k^3}{w^3}} $$
$$ LHS = \frac{k}{u} + \frac{k}{v} + \frac{k}{w} $$
$$ LHS = k \left( \frac{1}{u} + \frac{1}{v} + \frac{1}{w} \right) $$
Од Чекор 1 знаеме дека изразот во заградата е 1.
$$ LHS = k \cdot 1 = k $$

**Чекор 4: Пресметка на десната страна (RHS)**
$$ RHS = \sqrt[3]{xu^2 + yv^2 + zw^2} $$
Заменуваме за $x, y, z$:
$$ xu^2 = \frac{k^3}{u^3} \cdot u^2 = \frac{k^3}{u} $$
$$ yv^2 = \frac{k^3}{v^3} \cdot v^2 = \frac{k^3}{v} $$
$$ zw^2 = \frac{k^3}{w^3} \cdot w^2 = \frac{k^3}{w} $$

Сега го формираме збирот под коренот:
$$ xu^2 + yv^2 + zw^2 = \frac{k^3}{u} + \frac{k^3}{v} + \frac{k^3}{w} $$
$$ = k^3 \left( \frac{1}{u} + \frac{1}{v} + \frac{1}{w} \right) $$
Повторно го користиме условот од Чекор 1:
$$ = k^3 \cdot 1 = k^3 $$

Значи:
$$ RHS = \sqrt[3]{k^3} = k $$

**Заклучок:**
Добивме $LHS = k$ и $RHS = k$.
Следи дека $LHS = RHS$, со што равенството е докажано.

# Pedagogical Notes
1.  **Основна идеја:** Оваа задача е одличен пример за моќта на **параметризацијата** ($=k^3$). Кога имате верижно равенство ($A=B=C$), секогаш е добра идеја да го изедначите со нова променлива. Ова ги „разврзува“ променливите и овозможува да се изразат една преку друга.
2.  **Совет од Олимпиец:** Кога гледате симетричен израз како $vw+wu+uv=uvw$, веднаш помислете на делење со производот $uvw$. Реципрочните вредности често се клучот за поедноставување.
3.  **Чести грешки:** Учениците често се обидуваат да изразат една променлива (на пр. $x$) преку другите ($y, z$) и да заменуваат, што води до многу посложена алгебра отколку воведувањето на помошна променлива $k$.

# Manim Code
```python
from manim import *

class AlgebraicIdentity(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Алгебарски идентитет", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Condition 1
        cond1 = MathTex(r"vw + wu + uv = uvw", color=BLACK).shift(UP*2)
        cond1_trans = MathTex(r"\frac{1}{u} + \frac{1}{v} + \frac{1}{w} = 1", color=BLUE).next_to(cond1, DOWN)
        
        self.play(Write(cond1))
        self.play(TransformFromCopy(cond1, cond1_trans))
        
        # Condition 2
        cond2 = MathTex(r"xu^3 = yv^3 = zw^3 = k^3", color=BLACK).next_to(cond1_trans, DOWN, buff=0.5)
        self.play(Write(cond2))
        
        # Substitution
        sub = MathTex(
            r"x = \frac{k^3}{u^3}, \quad y = \frac{k^3}{v^3}, \quad z = \frac{k^3}{w^3}",
            color=BLACK
        ).next_to(cond2, DOWN)
        self.play(Write(sub))
        
        # LHS Calculation
        lhs = MathTex(
            r"LHS = \frac{k}{u} + \frac{k}{v} + \frac{k}{w} = k\left(\frac{1}{u} + \frac{1}{v} + \frac{1}{w}\right) = k",
            color=RED
        ).next_to(sub, DOWN, buff=0.5)
        self.play(Write(lhs))
        
        # RHS Calculation
        rhs = MathTex(
            r"RHS = \sqrt[3]{k^3\left(\frac{1}{u} + \frac{1}{v} + \frac{1}{w}\right)} = \sqrt[3]{k^3} = k",
            color=GREEN
        ).next_to(lhs, DOWN)
        self.play(Write(rhs))
        
        # Conclusion
        final = MathTex(r"LHS = RHS", color=BLACK).next_to(rhs, DOWN)
        self.play(Indicate(final))
        
        self.wait(2)