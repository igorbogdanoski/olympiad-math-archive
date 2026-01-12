---
problem_id: sigma139_p1891
title: Растојанија во ортодијагонален четириаголник
grade: 10
difficulty: 6
tags:
  - geometry
  - cyclic_quadrilateral
  - metric_relations
  - orthodiagonal
source: Sigma 139, Zadaca 1891
type: geometry
---

# Текст на задачата
Нека $ABCD$ е четириаголник со $AC \perp BD$ и нека $P$ е пресечна точка на $AC$ и $BD$. Ако растојанието од $P$ до $AB$ е еднакво на 99, растојанието од $P$ до $BC$ е еднакво на 63 и растојанието од $P$ до $CD$ е еднакво на 77, пресметај го растојанието од $P$ до $AD$.

# Решение
## Стратегија
Ова е задача за **ортодијагонален четириаголник** (дијагоналите се сечат под прав агол).
Клучната идеја е да се искористи својството на тетивни четириаголници кои се формираат кога ќе се спуштат нормали од пресекот на дијагоналите кон страните.
Постои позната релација за растојанијата од пресекот на дијагоналите до страните во тангентен четириаголник, но овде четириаголникот е ортодијагонален.
Дали постои врска од типот $\frac{1}{h_a^2} + \frac{1}{h_c^2} = \frac{1}{h_b^2} + \frac{1}{h_d^2}$?
Или можеби врска со аглите?
Ако $P$ е пресекот, тогаш $\triangle APB, \triangle BPC, \triangle CPD, \triangle DPA$ се правоаголни триаголници.
Растојанието од $P$ до $AB$ е висината $h_{AB}$ во правоаголниот $\triangle APB$.
Важи $\frac{1}{h_{AB}^2} = \frac{1}{PA^2} + \frac{1}{PB^2}$.
Ова ќе ни даде систем равенки.

## Чекор по чекор

**Чекор 1: Означување и геометриски релации**
Нека $PA=a, PB=b, PC=c, PD=d$.
Бидејќи дијагоналите се нормални, триаголниците $\triangle APB, \triangle BPC, \triangle CPD, \triangle DPA$ се правоаголни во темето $P$.
Нека $h_1, h_2, h_3, h_4$ се растојанијата од $P$ до $AB, BC, CD, DA$ соодветно.
Дадено е:
$h_1 = 99$
$h_2 = 63$
$h_3 = 77$
Бараме $h_4 = x$.

Во правоаголен триаголник со катети $x, y$ и висина кон хипотенузата $h$, важи релацијата:
$$ \frac{1}{h^2} = \frac{1}{x^2} + \frac{1}{y^2} $$

Применувајќи го ова за нашите четири триаголници:
1.  $\triangle APB: \quad \frac{1}{h_1^2} = \frac{1}{a^2} + \frac{1}{b^2}$
2.  $\triangle BPC: \quad \frac{1}{h_2^2} = \frac{1}{b^2} + \frac{1}{c^2}$
3.  $\triangle CPD: \quad \frac{1}{h_3^2} = \frac{1}{c^2} + \frac{1}{d^2}$
4.  $\triangle DPA: \quad \frac{1}{h_4^2} = \frac{1}{d^2} + \frac{1}{a^2}$

**Чекор 2: Комбинирање на равенките**
Забележуваме дека ако ги собереме (1) и (3), и (2) и (4), ќе ги добиеме истите членови на десната страна:
$$ \frac{1}{h_1^2} + \frac{1}{h_3^2} = \left(\frac{1}{a^2} + \frac{1}{b^2}\right) + \left(\frac{1}{c^2} + \frac{1}{d^2}\right) = \frac{1}{a^2} + \frac{1}{b^2} + \frac{1}{c^2} + \frac{1}{d^2} $$
$$ \frac{1}{h_2^2} + \frac{1}{h_4^2} = \left(\frac{1}{b^2} + \frac{1}{c^2}\right) + \left(\frac{1}{d^2} + \frac{1}{a^2}\right) = \frac{1}{a^2} + \frac{1}{b^2} + \frac{1}{c^2} + \frac{1}{d^2} $$

Следи дека:
$$ \frac{1}{h_1^2} + \frac{1}{h_3^2} = \frac{1}{h_2^2} + \frac{1}{h_4^2} $$

**Чекор 3: Пресметка**
Заменуваме со дадените вредности:
$$ \frac{1}{99^2} + \frac{1}{77^2} = \frac{1}{63^2} + \frac{1}{x^2} $$

За да ја олесниме пресметката, ќе извадиме заеднички множители.
$99 = 9 \cdot 11$
$77 = 7 \cdot 11$
$63 = 7 \cdot 9$

$$ \frac{1}{(9 \cdot 11)^2} + \frac{1}{(7 \cdot 11)^2} = \frac{1}{(7 \cdot 9)^2} + \frac{1}{x^2} $$
$$ \frac{1}{11^2} \left( \frac{1}{9^2} + \frac{1}{7^2} \right) = \frac{1}{7^2 \cdot 9^2} + \frac{1}{x^2} $$
$$ \frac{1}{121} \left( \frac{49 + 81}{81 \cdot 49} \right) = \frac{1}{3969} + \frac{1}{x^2} $$
$$ \frac{130}{121 \cdot 3969} = \frac{1}{3969} + \frac{1}{x^2} $$

Ова изгледа малку комплицирано за рачна пресметка. Ајде да пробаме поинаку.
$$ \frac{1}{x^2} = \frac{1}{99^2} + \frac{1}{77^2} - \frac{1}{63^2} $$
$$ \frac{1}{x^2} = \frac{1}{11^2 \cdot 9^2} + \frac{1}{11^2 \cdot 7^2} - \frac{1}{7^2 \cdot 9^2} $$
Заеднички именител е $11^2 \cdot 9^2 \cdot 7^2 = (11 \cdot 9 \cdot 7)^2 = 693^2$.
$$ \frac{1}{x^2} = \frac{7^2 + 9^2 - 11^2}{693^2} $$
$$ \frac{1}{x^2} = \frac{49 + 81 - 121}{693^2} $$
$$ \frac{1}{x^2} = \frac{130 - 121}{693^2} $$
$$ \frac{1}{x^2} = \frac{9}{693^2} $$

Коренуваме:
$$ \frac{1}{x} = \frac{3}{693} $$
$$ \frac{1}{x} = \frac{1}{231} $$
$$ x = 231 $$

**Заклучок:**
Растојанието од $P$ до $AD$ е **231**.

# Pedagogical Notes
1.  **Основна идеја:** Во ортодијагонален четириаголник, збирот на реципрочните вредности на квадратите на висините кон спротивните страни е еднаков. Ова е директна последица на Питагоровата теорема (или поточно, релацијата за висина во правоаголен триаголник).
2.  **Совет од Олимпиец:** Кога имате броеви како 99, 63, 77, секогаш барајте ги нивните прости множители ($9 \cdot 11, 7 \cdot 9, 7 \cdot 11$). Тоа драстично ја поедноставува аритметиката и овозможува наоѓање на заеднички именител без огромни броеви.
3.  **Чести грешки:** Директно квадрирање на големите броеви (на пр. $99^2 = 9801$) води до губење време и грешки. Алгебарската манипулација со фактори е многу побезбедна.

# Manim Code
```python
from manim import *

class OrthodiagonalQuad(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Ортодијагонален четириаголник", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Formula
        formula = MathTex(
            r"\frac{1}{h_a^2} + \frac{1}{h_c^2} = \frac{1}{h_b^2} + \frac{1}{h_d^2}",
            color=BLUE
        ).shift(UP)
        self.play(Write(formula))
        
        # Substitution
        sub = MathTex(
            r"\frac{1}{99^2} + \frac{1}{77^2} = \frac{1}{63^2} + \frac{1}{x^2}",
            color=BLACK
        ).next_to(formula, DOWN)
        self.play(Write(sub))
        
        # Factorization
        factors = MathTex(
            r"\frac{1}{(9 \cdot 11)^2} + \frac{1}{(7 \cdot 11)^2} - \frac{1}{(7 \cdot 9)^2} = \frac{1}{x^2}",
            color=BLACK
        ).next_to(sub, DOWN)
        self.play(Write(factors))
        
        # Common Denominator
        common = MathTex(
            r"\frac{7^2 + 9^2 - 11^2}{(7 \cdot 9 \cdot 11)^2} = \frac{1}{x^2}",
            color=RED
        ).next_to(factors, DOWN)
        self.play(Write(common))
        
        # Calculation
        calc = MathTex(
            r"\frac{49 + 81 - 121}{693^2} = \frac{9}{693^2} = \frac{1}{x^2}",
            color=BLACK
        ).next_to(common, DOWN)
        self.play(Write(calc))
        
        # Result
        result = MathTex(
            r"\frac{1}{x} = \frac{3}{693} = \frac{1}{231} \implies x = 231",
            color=GREEN
        ).next_to(calc, DOWN)
        self.play(Indicate(result))
        
        self.wait(2)