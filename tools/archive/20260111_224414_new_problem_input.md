---
problem_id: sigma139_y1_p3
title: Алгебарски идентитет и Диофантова равенка
grade: 9
difficulty: 5
tags:
  - algebra
  - diophantine_equations
  - fractions
source: Sigma 139, Prva godina, Zadaca 3
type: algebra
---

# Текст на задачата
За целите броеви $a \neq 0$ и $b \neq 0$ важи:
$$ \left( \frac{\frac{1}{a}}{\frac{1}{a} - \frac{1}{b}} - \frac{\frac{1}{b}}{\frac{1}{a} + \frac{1}{b}} \right) \cdot \left( \frac{1}{a} - \frac{1}{b} \right) \cdot \frac{1}{\frac{1}{a^2} + \frac{1}{b^2}} = \frac{2}{3} $$
Пресметај го збирот $a+b$.

# Решение
## Стратегија
Изразот изгледа гломазен поради многуте двојни дропки. Најелегантен начин да се реши ова е преку **смена на променливи**.
1.  Воведуваме смена $x = \frac{1}{a}$ и $y = \frac{1}{b}$.
2.  Го упростуваме алгебарскиот израз додека не добиеме едноставна врска меѓу $x$ и $y$.
3.  Ја враќаме смената и добиваме равенка со цели броеви $a$ и $b$ (Диофантова равенка).
4.  Ја решаваме равенката користејќи факторизација.

## Чекор по чекор

**Чекор 1: Воведување смена**
Нека $x = \frac{1}{a}$ и $y = \frac{1}{b}$. Дадениот израз го запишуваме преку $x$ и $y$:
$$ \left( \frac{x}{x-y} - \frac{y}{x+y} \right) \cdot (x-y) \cdot \frac{1}{x^2+y^2} = \frac{2}{3} $$

**Чекор 2: Упростување на изразот во заградата**
Прво ќе го пресметаме изразот во големата заграда со сведување на заеднички именител:
$$ \frac{x}{x-y} - \frac{y}{x+y} = \frac{x(x+y) - y(x-y)}{(x-y)(x+y)} $$
$$ = \frac{x^2 + xy - (xy - y^2)}{x^2 - y^2} $$
$$ = \frac{x^2 + xy - xy + y^2}{x^2 - y^2} $$
$$ = \frac{x^2 + y^2}{x^2 - y^2} $$

**Чекор 3: Множење на членовите**
Сега го заменуваме упростениот дел назад во главната равенка:
$$ \frac{x^2 + y^2}{(x-y)(x+y)} \cdot (x-y) \cdot \frac{1}{x^2+y^2} = \frac{2}{3} $$
Забележуваме дека можеме да скратиме:
1.  Броителот $(x^2+y^2)$ од првиот дел се крати со именителот $(x^2+y^2)$ од третиот дел.
2.  Именителот $(x-y)$ од првиот дел се крати со множителот $(x-y)$ во средината.

Останува само:
$$ \frac{1}{x+y} = \frac{2}{3} $$

**Чекор 4: Враќање на смената**
Од равенката погоре следи:
$$ x + y = \frac{3}{2} $$
Заменуваме $x = \frac{1}{a}$ и $y = \frac{1}{b}$:
$$ \frac{1}{a} + \frac{1}{b} = \frac{3}{2} $$
Сведуваме на заеднички именител:
$$ \frac{a+b}{ab} = \frac{3}{2} $$
Множиме накрсно:
$$ 2(a+b) = 3ab $$
$$ 2a + 2b - 3ab = 0 $$

**Чекор 5: Решавање на Диофантовата равенка**
За да ја решиме равенката $3ab - 2a - 2b = 0$ во множеството цели броеви, ќе го искористиме трикот на Симон за факторизација (SFFT).
Множиме со 3 за да го комплетираме коефициентот пред $ab$:
$$ 9ab - 6a - 6b = 0 $$
Групираме:
$$ 3a(3b - 2) - 6b = 0 $$
Додаваме 4 на двете страни за да можеме да извадиме заеднички множител:
$$ 3a(3b - 2) - 2(3b - 2) = 4 $$
$$ (3a - 2)(3b - 2) = 4 $$

Бидејќи $a$ и $b$ се цели броеви, изразите $(3a-2)$ и $(3b-2)$ мора да бидат целобројни делители на бројот 4.
Делителите на 4 се: $\{1, 2, 4, -1, -2, -4\}$.
Исто така, забележуваме дека $3a-2 \equiv 1 \pmod 3$ (при делење со 3 дава остаток 1, бидејќи $-2 \equiv 1$).
Од делителите на 4, само $1, 4$ и $-2$ даваат остаток 1 при делење со 3.
*   $1 \equiv 1 \pmod 3$ (ОК)
*   $2 \equiv 2 \pmod 3$ (НЕ)
*   $4 \equiv 1 \pmod 3$ (ОК)
*   $-1 \equiv 2 \pmod 3$ (НЕ)
*   $-2 \equiv 1 \pmod 3$ (ОК)
*   $-4 \equiv 2 \pmod 3$ (НЕ)

Ги разгледуваме можните случаи за $X = 3a-2$ и $Y = 3b-2$:

1.  **Случај 1:** $3a-2 = 1$ и $3b-2 = 4$
    $3a = 3 \implies a=1$
    $3b = 6 \implies b=2$
    Решение: $(1, 2)$.

2.  **Случај 2:** $3a-2 = 4$ и $3b-2 = 1$
    $3a = 6 \implies a=2$
    $3b = 3 \implies b=1$
    Решение: $(2, 1)$.

3.  **Случај 3:** $3a-2 = -2$ и $3b-2 = -2$
    $3a = 0 \implies a=0$.
    Но, условот на задачата е $a \neq 0$. Ова решение се отфрла.

**Заклучок:**
Единствените валидни парови се $(1, 2)$ и $(2, 1)$.
Во двата случаја, збирот е ист:
$$ a + b = 1 + 2 = 3 $$

# Pedagogical Notes
1.  **Основна идеја:** Моќта на супституцијата. Наместо да се мачиме со сложени дропки, смената $x=1/a$ го претвора проблемот во елементарна алгебра.
2.  **Совет од Олимпиец:** Кога имате равенка од типот $Axy + Bx + Cy = D$, секогаш обидете се да ја факторизирате во облик $(Ax+C)(Ay+B) = K$. Ова е стандардна техника за решавање равенки во цели броеви.
3.  **Чести грешки:** Заборавање на условот $a \neq 0$. Во оваа задача тоа е клучно за да се елиминира решението $(0,0)$.

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Упростување на изразот", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Substitution
        sub_text = MathTex(r"x = \frac{1}{a}, \quad y = \frac{1}{b}", color=BLUE).shift(UP*2)
        self.play(Write(sub_text))
        
        # Original Expression (Simplified view)
        expr = MathTex(
            r"\left( \frac{x}{x-y} - \frac{y}{x+y} \right) \cdot (x-y) \cdot \frac{1}{x^2+y^2} = \frac{2}{3}",
            color=BLACK
        ).next_to(sub_text, DOWN, buff=0.5)
        self.play(Write(expr))
        
        # Simplification step 1: Bracket
        step1 = MathTex(
            r"\frac{x(x+y) - y(x-y)}{x^2-y^2} = \frac{x^2+y^2}{x^2-y^2}",
            color=RED
        ).next_to(expr, DOWN, buff=0.5)
        self.play(Write(step1))
        
        # Simplification step 2: Cancellation
        step2 = MathTex(
            r"\frac{x^2+y^2}{(x-y)(x+y)} \cdot (x-y) \cdot \frac{1}{x^2+y^2} = \frac{1}{x+y}",
            color=GREEN
        ).next_to(step1, DOWN, buff=0.5)
        self.play(Write(step2))
        
        # Final Equation
        final_eq = MathTex(r"\frac{1}{x+y} = \frac{2}{3} \implies x+y = \frac{3}{2}", color=BLACK).next_to(step2, DOWN, buff=0.5)
        self.play(Write(final_eq))
        
        # Back substitution
        result = MathTex(r"\frac{1}{a} + \frac{1}{b} = \frac{3}{2} \implies a+b=3", color=BLUE).next_to(final_eq, DOWN, buff=0.5)
        self.play(Write(result))
        self.play(Indicate(result))
        
        self.wait(2)