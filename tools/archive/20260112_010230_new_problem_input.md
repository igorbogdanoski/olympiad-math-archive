---
problem_id: sigma139_p1892
title: Логаритамска неравенка со променлива основа
grade: 11
difficulty: 5
tags:
  - logarithms
  - inequalities
  - domain
  - cases
source: Sigma 139, Zadaca 1892
type: algebra
---

# Текст на задачата
Реши ја неравенката:
$$ \log_{x-1}(x^2 + 3x) < 1 $$

# Решение
## Стратегија
Ова е логаритамска неравенка каде што и основата ($x-1$) и аргументот ($x^2+3x$) содржат променлива.
1.  Прво мора да ја определиме **дефиниционата област** (доменот) на неравенката. Основата мора да биде позитивна и различна од 1, а аргументот мора да биде позитивен.
2.  Потоа ќе ја решиме неравенката разгледувајќи два случаи во зависност од основата:
    *   Случај 1: Основата е поголема од 1 ($x-1 > 1$). Тогаш знакот на неравенството се задржува.
    *   Случај 2: Основата е помеѓу 0 и 1 ($0 < x-1 < 1$). Тогаш знакот на неравенството се менува.
3.  На крајот ќе го најдеме пресекот на решенијата со дефиниционата област.

## Чекор по чекор

**Чекор 1: Дефинициона област**
За логаритамот да биде дефиниран, мора да важат следниве услови:
1.  Аргументот $> 0$:
    $$ x^2 + 3x > 0 $$
    $$ x(x+3) > 0 $$
    Решение: $x \in (-\infty, -3) \cup (0, +\infty)$.

2.  Основата $> 0$:
    $$ x - 1 > 0 \implies x > 1 $$

3.  Основата $\neq 1$:
    $$ x - 1 \neq 1 \implies x \neq 2 $$

Пресекот на сите овие услови е:
$$ x \in (1, 2) \cup (2, +\infty) $$
Ова е нашиот домен $D$.

**Чекор 2: Решавање на неравенката**
Неравенката е $\log_{x-1}(x^2 + 3x) < 1$.
Можеме да ја запишеме 1 како $\log_{x-1}(x-1)$.
$$ \log_{x-1}(x^2 + 3x) < \log_{x-1}(x-1) $$

**Случај 1: Основата е поголема од 1**
$$ x - 1 > 1 \implies x > 2 $$
Во овој случај, логаритамската функција е растечка, па знакот на неравенството се задржува:
$$ x^2 + 3x < x - 1 $$
$$ x^2 + 2x + 1 < 0 $$
$$ (x + 1)^2 < 0 $$
Квадрат на реален број никогаш не е строго помал од 0.
Значи, во овој случај **нема решение**.

**Случај 2: Основата е помеѓу 0 и 1**
$$ 0 < x - 1 < 1 \implies 1 < x < 2 $$
Во овој случај, логаритамската функција е опаѓачка, па знакот на неравенството се менува:
$$ x^2 + 3x > x - 1 $$
$$ x^2 + 2x + 1 > 0 $$
$$ (x + 1)^2 > 0 $$
Ова неравенство важи за секој $x \neq -1$.
Бидејќи работиме во интервалот $x \in (1, 2)$, условот $x \neq -1$ е автоматски исполнет.
Значи, решението во овој случај е целиот интервал $(1, 2)$.

**Чекор 3: Конечен пресек**
Ги обединуваме решенијата од двата случаи и правиме пресек со доменот.
*   Случај 1 ($x > 2$): Нема решение.
*   Случај 2 ($1 < x < 2$): Решение е $x \in (1, 2)$.

Доменот беше $(1, 2) \cup (2, +\infty)$.
Пресекот е $(1, 2)$.

**Заклучок:**
Решението на неравенката е $x \in (1, 2)$.

# Pedagogical Notes
1.  **Основна идеја:** Логаритамската функција $f(t) = \log_a t$ е монотона, но насоката на монотоност зависи од основата $a$. Ако $a > 1$, таа расте (знакот се чува). Ако $0 < a < 1$, таа опаѓа (знакот се врти). Ова е најважното правило за логаритамски неравенки.
2.  **Совет од Олимпиец:** Никогаш не заборавајте ја дефиниционата област! Многу ученици веднаш почнуваат со антилогаритмирање и добиваат решенија кои се надвор од доменот. Во оваа задача, условот $x>1$ е клучен.
3.  **Чести грешки:**
    *   Заборавање да се смени знакот кога основата е помала од 1.
    *   Заборавање дека основата не смее да биде 1 ($x \neq 2$).
    *   Грешка при решавање на $(x+1)^2 < 0$ (некои мислат дека има решение).

# Manim Code
```python
from manim import *

class LogInequality(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Логаритамска неравенка", color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Inequality
        ineq = MathTex(r"\log_{x-1}(x^2 + 3x) < 1", color=BLACK).shift(UP)
        self.play(Write(ineq))
        
        # Domain
        domain_text = Text("Домен:", color=BLUE, font_size=24).next_to(ineq, DOWN, buff=0.5).to_edge(LEFT)
        domain_cond = MathTex(
            r"1. \quad x^2+3x > 0 \implies x \in (-\infty, -3) \cup (0, \infty)",
            r"2. \quad x-1 > 0 \implies x > 1",
            r"3. \quad x-1 \neq 1 \implies x \neq 2",
            color=BLUE, font_size=30
        ).arrange(DOWN, aligned_edge=LEFT).next_to(domain_text, DOWN, aligned_edge=LEFT)
        
        final_domain = MathTex(r"D: x \in (1, 2) \cup (2, \infty)", color=RED).next_to(domain_cond, DOWN)
        
        self.play(Write(domain_text))
        self.play(Write(domain_cond))
        self.play(Write(final_domain))
        
        # Cases
        case1 = MathTex(r"\text{Случај 1: } x-1 > 1 \implies x > 2", color=BLACK, font_size=30).next_to(final_domain, DOWN, buff=0.5).to_edge(LEFT)
        sol1 = MathTex(r"x^2+3x < x-1 \implies (x+1)^2 < 0 \implies \emptyset", color=BLACK, font_size=30).next_to(case1, DOWN, aligned_edge=LEFT)
        
        case2 = MathTex(r"\text{Случај 2: } 0 < x-1 < 1 \implies 1 < x < 2", color=BLACK, font_size=30).next_to(sol1, DOWN, buff=0.2).to_edge(LEFT)
        sol2 = MathTex(r"x^2+3x > x-1 \implies (x+1)^2 > 0 \implies \mathbb{R} \setminus \{-1\}", color=BLACK, font_size=30).next_to(case2, DOWN, aligned_edge=LEFT)
        
        self.play(Write(case1))
        self.play(Write(sol1))
        self.play(Write(case2))
        self.play(Write(sol2))
        
        # Final Result
        result = MathTex(r"x \in (1, 2)", color=GREEN).next_to(sol2, DOWN, buff=0.5)
        self.play(Indicate(result))
        
        self.wait(2)