---
problem_id: sigma139_p1904
title: Агол во рамнокрак триаголник
grade: 11
difficulty: 6
tags:
  - geometry
  - trigonometry
  - cosine_rule
  - cubic_equation
source: Sigma 139, Zadaca 1904
type: geometry
---

# Текст на задачата
Даден е рамнокрак триаголник $ABC$ со основа $a$ и крак $b$, за кои важи равенството $a^3 - b^3 = 3ab^2$. Пресметај го $\angle BAC$.

# Решение
## Стратегија
Имаме алгебарска врска помеѓу страните на триаголникот.
1.  Ќе ја трансформираме равенката $a^3 - b^3 = 3ab^2$ во хомогена равенка со делење со $b^3$.
2.  Ќе воведеме смена $x = a/b$ и ќе ја решиме кубната равенка за да го најдеме односот на страните.
3.  Ќе ја искористиме Косинусната теорема за да го најдеме аголот $\alpha = \angle BAC$ преку односот $a/b$.
    *   Во рамнокрак триаголник со основа $a$ и крак $b$, $\cos \alpha = \frac{a/2}{b} = \frac{a}{2b}$.

## Чекор по чекор

**Чекор 1: Трансформација на равенката**
Дадено е:
$$ a^3 - b^3 = 3ab^2 $$
Делиме со $b^3$ (бидејќи $b \neq 0$):
$$ \left(\frac{a}{b}\right)^3 - 1 = 3\frac{a}{b} $$
Нека $x = \frac{a}{b}$. Равенката станува:
$$ x^3 - 1 = 3x $$
$$ x^3 - 3x - 1 = 0 $$

**Чекор 2: Решавање на кубната равенка**
Треба да ја решиме равенката $x^3 - 3x - 1 = 0$.
Оваа равенка е поврзана со тригонометрискиот идентитет за троен агол: $\cos 3\theta = 4\cos^3 \theta - 3\cos \theta$.
Ако ставиме $x = 2\cos \theta$:
$$ (2\cos \theta)^3 - 3(2\cos \theta) - 1 = 0 $$
$$ 8\cos^3 \theta - 6\cos \theta = 1 $$
Делиме со 2:
$$ 4\cos^3 \theta - 3\cos \theta = \frac{1}{2} $$
$$ \cos 3\theta = \frac{1}{2} $$

Решенијата за $3\theta$ се $\pm 60^\circ + 360^\circ k$.
Значи $3\theta \in \{60^\circ, 300^\circ, 420^\circ, \dots\}$.
Можните вредности за $\theta$:
1.  $\theta_1 = 20^\circ \implies x_1 = 2\cos 20^\circ$
2.  $\theta_2 = 100^\circ \implies x_2 = 2\cos 100^\circ$ (негативно, не може да биде однос на страни)
3.  $\theta_3 = 140^\circ \implies x_3 = 2\cos 140^\circ$ (негативно)

Значи, единственото позитивно решение е $x = 2\cos 20^\circ$.
(Забелешка: $x^3-3x-1=0$ има три реални корени, но само еден е позитивен бидејќи $f(0)=-1, f(2)=1$, па коренот е меѓу 0 и 2. Другите два се негативни).

Значи, односот на страните е:
$$ \frac{a}{b} = 2\cos 20^\circ $$

**Чекор 3: Пресметка на аголот**
Во рамнокрак триаголник со основа $a$ и крак $b$, аголот при основата $\alpha = \angle BAC$ се пресметува преку:
$$ \cos \alpha = \frac{a/2}{b} = \frac{1}{2} \cdot \frac{a}{b} $$
Заменуваме за $a/b$:
$$ \cos \alpha = \frac{1}{2} \cdot (2\cos 20^\circ) $$
$$ \cos \alpha = \cos 20^\circ $$

Бидејќи $\alpha$ е агол во триаголник, единствено решение е:
$$ \alpha = 20^\circ $$

**Заклучок:**
Аголот $\angle BAC$ изнесува $20^\circ$.

# Pedagogical Notes
1.  **Основна идеја:** Препознавањето на тригонометриската супституција $x=2\cos\theta$ во кубната равенка $x^3-3x-1=0$ е клучен момент. Ова е стандардна техника за решавање на *casus irreducibilis* кај кубни равенки.
2.  **Совет од Олимпиец:** Кога имате хомогена равенка (сите членови имаат ист степен, овде 3), секогаш делете со највисокиот степен на една од променливите за да добиете равенка со една непозната (односот $a/b$).
3.  **Геометриска интерпретација:** Интересно е што добивме $\cos \alpha = \cos 20^\circ$. Ова значи дека триаголникот е многу специфичен (агли $20^\circ, 20^\circ, 140^\circ$).

# Manim Code
```python
from manim import *

class TriangleAngle(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Агол во рамнокрак триаголник", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Equation
        eq = MathTex(r"a^3 - b^3 = 3ab^2", color=BLACK).shift(UP)
        self.play(Write(eq))
        
        # Substitution
        sub = MathTex(r"\text{Делиме со } b^3 \implies x^3 - 1 = 3x, \quad x = a/b", color=BLUE).next_to(eq, DOWN)
        self.play(Write(sub))
        
        # Cubic Equation
        cubic = MathTex(r"x^3 - 3x - 1 = 0", color=BLACK).next_to(sub, DOWN)
        self.play(Write(cubic))
        
        # Trig Substitution
        trig_sub = MathTex(r"\text{Нека } x = 2\cos \theta", color=RED).next_to(cubic, DOWN)
        trig_eq = MathTex(
            r"8\cos^3 \theta - 6\cos \theta = 1 \implies \cos 3\theta = 1/2",
            color=BLACK
        ).next_to(trig_sub, DOWN)
        
        self.play(Write(trig_sub))
        self.play(Write(trig_eq))
        
        # Solution
        theta = MathTex(r"3\theta = 60^\circ \implies \theta = 20^\circ", color=GREEN).next_to(trig_eq, DOWN)
        x_val = MathTex(r"x = 2\cos 20^\circ", color=GREEN).next_to(theta, DOWN)
        
        self.play(Write(theta))
        self.play(Write(x_val))
        
        # Final Angle
        final = MathTex(
            r"\cos \alpha = \frac{a}{2b} = \frac{x}{2} = \cos 20^\circ \implies \alpha = 20^\circ",
            color=BLACK
        ).next_to(x_val, DOWN)
        
        self.play(Write(final))
        self.play(Indicate(final))
        
        self.wait(2)