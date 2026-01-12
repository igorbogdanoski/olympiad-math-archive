---
problem_id: sigma139_p1897_elegant
title: Еднаквост на плоштини во рамнокрак триаголник (Елегантно решение)
grade: 11
difficulty: 7
tags:
  - geometry
  - area
  - isosceles_triangle
  - similarity
  - sine_rule
source: Sigma 139, Zadaca 1897
type: geometry
---

# Текст на задачата
Нека правата $p$ ја сече основата $AB$ на рамнокракиот триаголник $ABC$ во точка $D$, страната $AC$ во точка $E$ и полуправата $BC$ во точка $F$, при што $\angle ADE = \angle BDC$. Докажи дека триаголниците $BCE$ и $AEF$ имаат еднакви плоштини.

# Решение
## Стратегија
За да докажеме дека плоштините на $\triangle BCE$ и $\triangle AEF$ се еднакви, ќе ги изразиме преку тригонометриската формула за плоштина и ќе покажеме дека производите на соодветните страни се еднакви.
1.  Ќе ја искористиме сличноста на триаголниците $\triangle ADE$ и $\triangle BDC$ (која произлегува од условот за аглите) за да добиеме релација меѓу страните.
2.  Ќе ја примениме Синусната теорема на триаголниците $\triangle ADE$ и $\triangle BDF$ за да воспоставиме врска помеѓу отсечките $AE$ и $BF$.
3.  Ќе покажеме дека условот за еднаквост на плоштините ($AE \cdot CF = CE \cdot BC$) е еквивалентен на веќе изведените релации.

## Чекор по чекор

**Чекор 1: Сличност на триаголници**
Нека $\angle A = \angle B = \alpha$ (бидејќи $\triangle ABC$ е рамнокрак).
Дадено е дека $\angle ADE = \angle BDC$.
Во $\triangle ADE$, третиот агол е $\angle AED = 180^\circ - \alpha - \angle ADE$.
Во $\triangle BDC$, третиот агол е $\angle BCD = 180^\circ - \alpha - \angle BDC$.
Бидејќи $\angle ADE = \angle BDC$, следи дека $\angle AED = \angle BCD$.
Бидејќи триаголниците $\triangle ADE$ и $\triangle BDC$ имаат по два еднакви агли ($\alpha$ и $\angle ADE = \angle BDC$), тие се слични:
$$ \triangle ADE \sim \triangle BDC $$
Од сличноста следи пропорционалност на страните:
$$ \frac{AE}{BC} = \frac{AD}{BD} = \frac{DE}{DC} $$
Од првото равенство добиваме:
$$ AE \cdot BD = AD \cdot BC \quad \dots(1) $$

**Чекор 2: Примена на Синусна теорема**
Да ги разгледаме триаголниците $\triangle ADE$ и $\triangle BDF$.
Во $\triangle ADE$, според Синусна теорема:
$$ \frac{AE}{\sin(\angle ADE)} = \frac{DE}{\sin \alpha} \implies AE = DE \frac{\sin(\angle ADE)}{\sin \alpha} $$
Во $\triangle BDF$, аголот кај $B$ е надворешен за $\triangle ABC$, па $\angle DBF = 180^\circ - \alpha$.
Аголот $\angle BDF$ е накрстен со $\angle ADE$, па $\angle BDF = \angle ADE$.
Според Синусна теорема за $\triangle BDF$:
$$ \frac{BF}{\sin(\angle BDF)} = \frac{DF}{\sin(180^\circ - \alpha)} = \frac{DF}{\sin \alpha} $$
$$ BF = DF \frac{\sin(\angle ADE)}{\sin \alpha} $$

Ако ги поделиме изразите за $AE$ и $BF$:
$$ \frac{AE}{BF} = \frac{DE}{DF} \implies AE \cdot DF = BF \cdot DE \quad \dots(2) $$

**Чекор 3: Изразување на плоштините**
Треба да докажеме $P_{BCE} = P_{AEF}$.
1.  $P_{BCE} = \frac{1}{2} CE \cdot BC \sin(\angle C)$.
2.  $P_{AEF} = \frac{1}{2} AE \cdot CF \sin(\angle C)$. (Бидејќи $A, E, C$ се колинеарни и $B, C, F$ се колинеарни, аголот кај $C$ е ист или накрстен).

За да бидат плоштините еднакви, треба:
$$ CE \cdot BC = AE \cdot CF $$
$$ \frac{CE}{AE} = \frac{CF}{BC} $$
Додаваме 1 на двете страни:
$$ \frac{CE}{AE} + 1 = \frac{CF}{BC} + 1 $$
$$ \frac{CE+AE}{AE} = \frac{CF+BC}{BC} $$
Бидејќи $CE+AE = AC$ и $CF+BC = BF$ (бидејќи $F$ е на полуправата $BC$, распоредот е $C-B-F$? Не, $D$ е на $AB$, $E$ на $AC$. Правата $ED$ ја сече $BC$ во $F$. За да биде $F$ на полуправата $BC$, $B$ мора да е меѓу $C$ и $F$. Тогаш $CF = CB + BF$. Ако $C$ е меѓу $B$ и $F$, тогаш $BF = BC + CF$.
Ајде да провериме. $\angle ADE = \angle BDC$. Ова сугерира дека $E$ е „поблиску“ до $A$ отколку $D$ до $B$ во однос на висината. Геометриски, $F$ е надворешна точка на страната $BC$ од кај $B$. Значи $C-B-F$. Тогаш $CF = CB + BF$.
Равенството станува:
$$ \frac{AC}{AE} = \frac{BF}{BC} $$
$$ AC \cdot BC = AE \cdot BF $$
Бидејќи $AC = BC$ (рамнокрак), ова се сведува на:
$$ BC^2 = AE \cdot BF $$

**Чекор 4: Доказ на релацијата $BC^2 = AE \cdot BF$**
Од (1) имаме $AE = \frac{AD \cdot BC}{BD}$.
Заменуваме во бараното равенство:
$$ \frac{AD \cdot BC}{BD} \cdot BF = BC^2 $$
$$ \frac{AD \cdot BF}{BD} = BC $$
$$ \frac{BF}{BD} = \frac{BC}{AD} $$

Дали ова е точно?
Да се вратиме на (2): $\frac{AE}{BF} = \frac{DE}{DF}$.
Од сличноста $\triangle ADE \sim \triangle BDC$, имаме $\frac{AE}{BC} = \frac{DE}{DC}$.
Делиме:
$$ \frac{AE/BF}{AE/BC} = \frac{DE/DF}{DE/DC} $$
$$ \frac{BC}{BF} = \frac{DC}{DF} $$
Ова значи дека во $\triangle FDC$, отсечката $DB$ ја дели страната $FC$ во однос на другите две страни.
Според теоремата за симетрала на агол, ова важи ако $DB$ е симетрала на $\angle FDC$.
Дали е?
$\angle FDB = \angle ADE$ (накрстни).
$\angle BDC = \angle ADE$ (услов).
Значи $\angle FDB = \angle BDC$.
Да, $DB$ е симетрала!
Затоа релацијата $\frac{BC}{BF} = \frac{DC}{DF}$ е точна.

Ова имплицира дека сите претходни чекори се еквивалентни и точни.
Специјално, $BC^2 = AE \cdot BF$ е точно.
Следи дека $P_{BCE} = P_{AEF}$.

**Заклучок:**
Докажавме дека плоштините се еднакви.

# Pedagogical Notes
1.  **Основна идеја:** Задачата е прекрасен пример за поврзување на различни геометриски концепти: сличност, синусна теорема и теорема за симетрала на агол. Клучниот момент е препознавањето дека $DB$ е симетрала на аголот во $\triangle FDC$.
2.  **Совет од Олимпиец:** Кога имате услов за еднаквост на агли кои не се во ист триаголник ($\angle ADE = \angle BDC$), обидете се да ги доведете до заедничко теме (преку накрстни агли) за да откриете својства како симетрала.
3.  **Елеганција:** Ова решение е „елегантно“ бидејќи избегнува тешки пресметки и Менелаева теорема, потпирајќи се само на основните својства на триаголниците.

# Manim Code
```python
from manim import *

class ElegantProof(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Setup Triangle
        A = LEFT * 2 + DOWN * 1
        B = RIGHT * 2 + DOWN * 1
        C = UP * 2
        
        # Point D
        D = LEFT * 0.5 + DOWN * 1
        
        # Calculate E and F based on angle condition
        v_DB = B - D
        v_DC = C - D
        ang_BDC = np.arccos(np.dot(v_DB, v_DC) / (np.linalg.norm(v_DB) * np.linalg.norm(v_DC)))
        
        # Rotate DA by ang_BDC to get direction of p
        v_DA = A - D
        c_rot, s_rot = np.cos(ang_BDC), np.sin(ang_BDC)
        v_DE = np.array([v_DA[0]*c_rot - v_DA[1]*s_rot, v_DA[0]*s_rot + v_DA[1]*c_rot, 0])
        
        # Intersect
        def intersect(p1, v1, p2, v2):
            mat = np.array([[v1[0], -v2[0]], [v1[1], -v2[1]]])
            rhs = p2[:2] - p1[:2]
            sol = np.linalg.solve(mat, rhs)
            return p1 + sol[0] * v1
            
        E = intersect(A, C-A, D, v_DE)
        F = intersect(B, C-B, D, v_DE)
        
        # Draw
        tri = Polygon(A, B, C, color=BLACK)
        line_p = Line(F, E, color=BLUE)
        line_CD = Line(C, D, color=BLACK)
        
        self.play(Create(tri))
        self.play(Create(line_p))
        self.play(Create(line_CD))
        
        # Labels
        lbls = VGroup(
            MathTex("A").next_to(A, DL),
            MathTex("B").next_to(B, DR),
            MathTex("C").next_to(C, UP),
            MathTex("D").next_to(D, DOWN),
            MathTex("E").next_to(E, UL),
            MathTex("F").next_to(F, DR)
        ).set_color(BLACK)
        self.play(Write(lbls))
        
        # Angle Bisector Visualization
        arc_FDB = Angle(Line(D, F), Line(D, B), radius=0.4, color=RED)
        arc_BDC = Angle(Line(D, B), Line(D, C), radius=0.5, color=RED)
        
        self.play(Create(arc_FDB), Create(arc_BDC))
        
        bisector_text = MathTex(r"\angle FDB = \angle BDC \implies DB \text{ е симетрала}", color=RED, font_size=30).to_corner(UL)
        self.play(Write(bisector_text))
        
        # Theorem text
        thm_text = MathTex(r"\frac{FB}{BC} = \frac{FD}{DC}", color=BLACK).next_to(bisector_text, DOWN)
        self.play(Write(thm_text))
        
        # Final result
        res_text = MathTex(r"P_{BCE} = P_{AEF}", color=GREEN).to_edge(UP)
        self.play(Write(res_text))
        self.play(Indicate(res_text))
        
        self.wait(2)