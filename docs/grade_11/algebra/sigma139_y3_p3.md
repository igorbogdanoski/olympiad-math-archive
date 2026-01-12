---
difficulty: 5
grade: 11
problem_id: sigma139_y3_p3
source: Sigma 139, Treta godina, Zadaca 3
tags:
- trigonometry
- irrational_equations
- inequalities
- substitution
title: Тригонометриска равенка со корени
type: algebra
---

# Текст на задачата
Реши ја равенката:
$$ \sqrt{\sin^2 x + \frac{1}{2}} + \sqrt{\cos^2 x + \frac{1}{2}} = 2 $$

# Решение
## Стратегија
Равенката содржи збир на два корени. Можеме да ја решиме со квадрирање, но тоа ќе доведе до комплицирани изрази.
Поелегантен пристап е да воведеме смена. Забележуваме дека $\sin^2 x + \cos^2 x = 1$.
Ако ставиме $u = \sin^2 x$, тогаш $\cos^2 x = 1 - u$.
Равенката ќе стане алгебарска равенка по $u$.
Исто така, можеме да користиме неравенства (на пример, неравенство меѓу средините) за да покажеме дека левата страна е секогаш $\ge 2$, па равенство важи само во специфичен случај.

## Чекор по чекор

**Чекор 1: Воведување смена**
Нека $u = \sin^2 x$. Бидејќи $0 \le \sin^2 x \le 1$, важи $u \in [0, 1]$.
Тогаш $\cos^2 x = 1 - u$.
Равенката добива облик:
$$ \sqrt{u + \frac{1}{2}} + \sqrt{1 - u + \frac{1}{2}} = 2 $$
$$ \sqrt{u + \frac{1}{2}} + \sqrt{\frac{3}{2} - u} = 2 $$

**Чекор 2: Квадрирање на равенката**
Бидејќи двете страни се позитивни, можеме да квадрираме:
$$ \left( \sqrt{u + \frac{1}{2}} + \sqrt{\frac{3}{2} - u} \right)^2 = 2^2 $$
$$ \left( u + \frac{1}{2} \right) + 2\sqrt{\left(u + \frac{1}{2}\right)\left(\frac{3}{2} - u\right)} + \left( \frac{3}{2} - u \right) = 4 $$

Ги собираме слободните членови:
$$ u - u + \frac{1}{2} + \frac{3}{2} + 2\sqrt{\dots} = 4 $$
$$ 2 + 2\sqrt{\left(u + \frac{1}{2}\right)\left(\frac{3}{2} - u\right)} = 4 $$

**Чекор 3: Изолирање на коренот**
$$ 2\sqrt{\left(u + \frac{1}{2}\right)\left(\frac{3}{2} - u\right)} = 2 $$
Делиме со 2:
$$ \sqrt{\left(u + \frac{1}{2}\right)\left(\frac{3}{2} - u\right)} = 1 $$

**Чекор 4: Второ квадрирање и решавање**
$$ \left(u + \frac{1}{2}\right)\left(\frac{3}{2} - u\right) = 1 $$
Го развиваме изразот:
$$ \frac{3}{2}u - u^2 + \frac{3}{4} - \frac{1}{2}u = 1 $$
$$ -u^2 + u + \frac{3}{4} = 1 $$
$$ -u^2 + u - \frac{1}{4} = 0 $$
Множиме со -1:
$$ u^2 - u + \frac{1}{4} = 0 $$
Ова е полн квадрат:
$$ \left( u - \frac{1}{2} \right)^2 = 0 $$

Значи, единствено решение за $u$ е:
$$ u = \frac{1}{2} $$

**Чекор 5: Враќање на смената**
Имаме $\sin^2 x = \frac{1}{2}$.
$$ \sin x = \pm \frac{1}{\sqrt{2}} = \pm \frac{\sqrt{2}}{2} $$
Ова одговара на аглите $x = \frac{\pi}{4} + \frac{k\pi}{2}$ (или $45^\circ + 90^\circ k$).

Попрецизно:
1.  $\sin x = \frac{\sqrt{2}}{2} \implies x = \frac{\pi}{4} + 2k\pi$ или $x = \frac{3\pi}{4} + 2k\pi$.
2.  $\sin x = -\frac{\sqrt{2}}{2} \implies x = -\frac{\pi}{4} + 2k\pi$ или $x = \frac{5\pi}{4} + 2k\pi$.

Сите овие решенија можат да се запишат со една формула:
$$ x = \frac{\pi}{4} + \frac{k\pi}{2}, \quad k \in \mathbb{Z} $$

**Заклучок:**
Решенијата на равенката се $x = \frac{\pi}{4} + \frac{k\pi}{2}$ за $k \in \mathbb{Z}$.

# Pedagogical Notes
1.  **Основна идеја:** Смената $u = \sin^2 x$ е многу корисна кога во равенката се појавуваат само квадрати на синус и косинус. Таа го намалува степенот на проблемот и го претвора во алгебарски.
2.  **Совет од Олимпиец:** Алтернативен пристап е преку неравенството меѓу квадратна и аритметичка средина (QM-AM).
    Нека $a = \sqrt{\sin^2 x + 1/2}$ и $b = \sqrt{\cos^2 x + 1/2}$.
    Знаеме дека $\frac{a+b}{2} \le \sqrt{\frac{a^2+b^2}{2}}$.
    $a^2+b^2 = \sin^2 x + 1/2 + \cos^2 x + 1/2 = 1 + 1 = 2$.
    Значи $\frac{a+b}{2} \le \sqrt{\frac{2}{2}} = 1 \implies a+b \le 2$.
    Равенката бара $a+b=2$. Равенство во QM-AM важи акко $a=b$.
    $\sin^2 x + 1/2 = \cos^2 x + 1/2 \implies \sin^2 x = \cos^2 x \implies \tan^2 x = 1$.
    Ова води до истото решение многу побрзо!
3.  **Чести грешки:** Заборавање на периодичноста на тригонометриските функции. Решението не е само $45^\circ$, туку бесконечно многу агли.

```python
from manim import *

class TrigEquation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Тригонометриска равенка", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Equation
        eq = MathTex(
            r"\sqrt{\sin^2 x + \frac{1}{2}} + \sqrt{\cos^2 x + \frac{1}{2}} = 2",
            color=BLACK
        ).shift(UP)
        self.play(Write(eq))
        
        # Substitution
        sub = MathTex(r"\text{Смена: } u = \sin^2 x \implies \cos^2 x = 1-u", color=BLUE).next_to(eq, DOWN)
        self.play(Write(sub))
        
        # Algebraic Equation
        alg_eq = MathTex(
            r"\sqrt{u + \frac{1}{2}} + \sqrt{\frac{3}{2} - u} = 2",
            color=BLACK
        ).next_to(sub, DOWN)
        self.play(TransformFromCopy(eq, alg_eq))
        
        # Squaring
        squared = MathTex(
            r"\left(u + \frac{1}{2}\right) + 2\sqrt{\dots} + \left(\frac{3}{2} - u\right) = 4",
            color=BLACK
        ).next_to(alg_eq, DOWN)
        
        simplified = MathTex(
            r"2 + 2\sqrt{\dots} = 4 \implies \sqrt{\dots} = 1",
            color=RED
        ).next_to(squared, DOWN)
        
        self.play(Write(squared))
        self.play(Write(simplified))
        
        # Final Solution
        sol_u = MathTex(r"(u - 1/2)^2 = 0 \implies u = 1/2", color=GREEN).next_to(simplified, DOWN)
        sol_x = MathTex(r"\sin^2 x = 1/2 \implies x = \frac{\pi}{4} + \frac{k\pi}{2}", color=GREEN).next_to(sol_u, DOWN)
        
        self.play(Write(sol_u))
        self.play(Write(sol_x))
        self.play(Indicate(sol_x))
        
        self.wait(2)

---
### 🎨 Визуелизација
![Илустрација](/assets/images/sigma139_y3_p3/sigma139_y3_p3.png)