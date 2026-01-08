---
problem_id: sigma137_p1855_algebra_log_inequality
title: Логаритамска Телескопска Неравенка
grade: 11
difficulty: 5
type: algebra
tags:
  - algebra
  - inequalities
  - logarithms
  - telescoping_sum
source: Сигма 137
---

```

# Задача 1855: Логаритамска Телескопска Неравенка

**Текст на задачата:**
Во множеството на реалните броеви реши ја неравенката:


---

### 💡 Помош (Hints)

<details>
<summary>Кликни за мала помош</summary>

1. **Својства на логаритмите:** Искористи го идентитетот . Ова ќе ти овозможи да ги разделиш константите од логаритмите.
2. **Телескопска сума:** Изразот  може да се запише како разлика . Ова овозможува масовно поништување на членовите.
3. **Смена на променлива:** За полесно решавање на крајната неравенка, воведи смена . Внимавај на дефиниционата област ().
</details>

---

### 🧠 Експертска Анализа

Ова е класична задача која комбинира алгебарски манипулации со **логаритамски идентитети** и **телескопски суми**.

Интуицијата оди по следниот тек:

1. **Препознавање на шемата:** Гледаме дека именителот секогаш е производ на два логаритми од облик . Ова сугерира дека  е "заеднички градежен блок".
2. **Трансформација во сума:** Откако ќе го извадиме заедничкиот дел , остануваме со сума од типот . Ова е позната телескопска сума каде сите внатрешни членови се поништуваат ("изедуваат").
3. **Внимателност со неравенството:** Кога множиме или делиме со променливи (во случајов логаритми), мора строго да внимаваме на знакот. Дали изразот е позитивен или негативен?

---

### 📐 Детално Решение



**1. Дефинициона област:**
За логаритмите да бидат дефинирани и именителите да не се нула:
 и  (бидејќи  е во именител,  не смее да биде 1).

**2. Упростување на општиот член:**
Нека го разгледаме -тиот член од левата страна (LHS). Именителот е:



Користејќи го својството :



Значи, општиот член е:


**3. Пресметување на сумата:**
Левата страна е:



Користејќи го разложувањето  (Телескопска сума):



Сите членови се поништуваат освен првиот и последниот:



Сега неравенката гласи:


**4. Решавање на неравенката:**
Кратиме со 2024 (позитивен број):



Користиме врска помеѓу основите: .
Тогаш .
Заменуваме во неравенката:


**5. Воведување смена:**
Нека . Бидејќи , .


Нулите на квадратната функција се  и .
Параболата е отворена нагоре, па таа е помала или еднаква на нула помеѓу нулите:



Но, поради условот , го исклучуваме 0:


**6. Враќање на смената:**



Основата е , па знакот на неравенството се задржува при антилогаритмирање:


Краен одговор: 

---

### 👨‍🏫 Менторски Белешки

Клучно за оваа задача е да не се изгуби условот .
Ако механички го решевте  како , ќе го вклучевте решението . Но, ако , логаритмите во именителот на почетната задача стануваат  што е недефинирано (или именителот станува 0). Затоа  мора да се отфрли.

# Manim Code

```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # --- TITLE ---
        title = Text("Logarithmic Telescoping Sum", color=BLACK).scale(0.8).to_edge(UP)
        self.play(Write(title))
        
        # --- PART 1: The General Term ---
        # Show transformation of log_x(2^k)
        
        eq1 = MathTex(
            r"\log_x(2^k) = k \cdot \log_x 2",
            color=BLACK
        ).shift(UP * 1.5)
        
        self.play(Write(eq1))
        self.wait(1)
        
        # Show general term simplification
        term_original = MathTex(
            r"a_k = \frac{1}{\log_x 2^k \cdot \log_x 2^{k+1}}",
            color=BLACK
        ).scale(0.9)
        
        term_final = MathTex(
            r"a_k = \frac{1}{(\log_x 2)^2} \cdot \frac{1}{k(k+1)}",
            color=BLUE
        ).scale(0.9)
        
        self.play(Write(term_original))
        self.wait(1)
        self.play(Transform(term_original, term_final))
        self.wait(1)
        
        # Move simplified term up
        self.play(FadeOut(eq1), term_original.animate.to_edge(UP).shift(DOWN*0.5))
        
        # --- PART 2: Telescoping Sum Visual ---
        
        # Show partial fractions
        partial_frac = MathTex(
            r"\sum \frac{1}{k(k+1)} = \sum \left( \frac{1}{k} - \frac{1}{k+1} \right)",
            color=BLACK
        ).scale(0.8).shift(UP * 0.5)
        self.play(Write(partial_frac))
        
        # Generate the expansion
        t1 = MathTex(r"(1 - \frac{1}{2})", color=BLACK).shift(LEFT * 2.5, DOWN * 0.5)
        t2 = MathTex(r"+ (\frac{1}{2} - \frac{1}{3})", color=BLACK).next_to(t1, RIGHT)
        t3 = MathTex(r"+ \dots", color=BLACK).next_to(t2, RIGHT)
        tn = MathTex(r"+ (\frac{1}{2024} - \frac{1}{2025})", color=BLACK).next_to(t3, RIGHT)
        
        expansion_group = VGroup(t1, t2, t3, tn).center()
        self.play(Write(expansion_group))
        self.wait(1)
        
        # Animate Cancellation (Slash lines)
        # Cancel 1/2s
        slash1 = Line(t1.get_center() + RIGHT*0.3 + DOWN*0.2, t1.get_center() + RIGHT*0.3 + UP*0.2, color=RED).rotate(PI/4)
        slash2 = Line(t2.get_center() + LEFT*0.3 + DOWN*0.2, t2.get_center() + LEFT*0.3 + UP*0.2, color=RED).rotate(PI/4)
        
        self.play(Create(slash1), Create(slash2))
        self.play(FadeOut(t1[0][2:]), FadeOut(t2[0][1:4]), FadeOut(slash1), FadeOut(slash2)) # Hide canceled parts
        
        # Final Sum Result
        result_text = MathTex(
            r"Sum = 1 - \frac{1}{2025}",
            color=GREEN
        ).next_to(expansion_group, DOWN, buff=0.5)
        
        self.play(Write(result_text))
        self.wait(2)
        
        # --- PART 3: Solving Inequality ---
        self.clear()
        
        ineq_start = MathTex(
            r"\frac{t^2}{2025} \le t",
            color=BLACK
        ).shift(UP * 1)
        
        ineq_solve = MathTex(
            r"t(t - 2025) \le 0",
            color=BLACK
        ).next_to(ineq_start, DOWN)
        
        # Number line visual
        number_line = NumberLine(
            x_range=[-500, 2500, 500],
            length=8,
            color=GRAY,
            include_numbers=True,
            numbers_to_include=[0, 2025]
        ).shift(DOWN * 1.5)
        
        interval = Line(
            number_line.n2p(0),
            number_line.n2p(2025),
            color=GREEN,
            stroke_width=6
        )
        
        dot_0 = Dot(number_line.n2p(0), color=WHITE, stroke_color=RED, stroke_width=2) # Open circle (x != 1)
        dot_2025 = Dot(number_line.n2p(2025), color=GREEN) # Closed circle
        
        label_t = MathTex("t = \log_2 x", color=BLUE).next_to(number_line, UP)
        
        self.play(Write(ineq_start))
        self.play(TransformFromCopy(ineq_start, ineq_solve))
        self.play(Create(number_line), Write(label_t))
        self.play(Create(interval))
        self.play(Create(dot_0), Create(dot_2025))
        
        final_ans = MathTex(
            r"x \in (1, 2^{2025}]",
            color=BLACK
        ).scale(1.2).to_edge(DOWN, buff=1)
        
        self.play(Write(final_ans))
        self.play(Indicate(final_ans, color=GREEN))
        
        self.wait(3)

```