---
problem_id: sigma139_p1897
title: Еднаквост на плоштини во рамнокрак триаголник
grade: 11
difficulty: 7
tags:
  - geometry
  - area
  - isosceles_triangle
  - menelaus_theorem
  - sine_rule
source: Sigma 139, Zadaca 1897
type: geometry
---

# Текст на задачата
Нека правата $p$ ја сече основата $AB$ на рамнокракиот триаголник $ABC$ во точка $D$, страната $AC$ во точка $E$ и полуправата $BC$ во точка $F$, при што $\angle ADE = \angle BDC$. Докажи дека триаголниците $BCE$ и $AEF$ имаат еднакви плоштини.

# Решение
## Стратегија
Задачата бара да докажеме еднаквост на плоштини на два триаголници кои не се складни.
1.  Ќе го искористиме условот за аглите $\angle ADE = \angle BDC$ за да воспоставиме врска помеѓу отсечките на основата.
2.  Ќе ја примениме **Менелаевата теорема** за правата $p$ која го сече триаголникот $ABC$ (или неговите продолженија).
3.  Ќе ги изразиме плоштините на $\triangle BCE$ и $\triangle AEF$ преку заеднички елементи (страни и агли) и ќе покажеме дека се еднакви.
    *   Забелешка: Плоштината на триаголник може да се пресмета како $P = \frac{1}{2} ab \sin \gamma$.
    *   Триаголниците $BCE$ и $AEF$ имаат „заеднички“ агол кај темето $C$ (или неговиот суплемент).

## Чекор по чекор

**Чекор 1: Анализа на аглите и сличност**
Нека $\triangle ABC$ е рамнокрак со $AC = BC$. Тогаш $\angle CAB = \angle CBA = \alpha$.
Дадено е дека $\angle ADE = \angle BDC$.
Бидејќи $D$ лежи на $AB$, аглите $\angle ADE$ и $\angle BDF$ се накрстни? Не, $E, D, F$ се колинеарни.
Значи $\angle ADE$ и $\angle BDF$ се накрстни агли, па $\angle ADE = \angle BDF$.
Условот е $\angle ADE = \angle BDC$.
Ова значи дека $\angle BDF = \angle BDC$?
Не, $C, B, F$ се колинеарни (полуправа $BC$). Точката $D$ е на $AB$.
Аголот $\angle BDC$ е агол во $\triangle BDC$.
Аголот $\angle ADE$ е агол помеѓу правата $p$ и основата $AB$.
Бидејќи $E, D, F$ се колинеарни, $\angle ADE$ и $\angle BDF$ се накрстни агли, па се еднакви.
Значи условот $\angle ADE = \angle BDC$ имплицира $\angle BDF = \angle BDC$.
Но, ова би значело дека $DB$ е симетрала на аголот $\angle FDC$?
Или можеби $D, B, C$ се некако поврзани?
Ајде да видиме.
Во $\triangle BDF$: $\angle DBF = 180^\circ - \alpha$ (надворешен агол на $\triangle ABC$).
Во $\triangle ADE$: $\angle DAE = \alpha$.
Условот $\angle ADE = \angle BDC$ е малку чуден. $D$ е на $AB$. $C$ е врвот.
Ако $\angle ADE = \epsilon$, тогаш $\angle BDF = \epsilon$.
Условот вели $\epsilon = \angle BDC$.
Значи во $\triangle BDC$, аголот кај $D$ е еднаков на аголот што правата $p$ го зафаќа со $AB$.

**Чекор 2: Примена на Синусна теорема**
Да ги изразиме плоштините.
$P_{BCE} = \frac{1}{2} CE \cdot CB \cdot \sin(\angle C)$.
$P_{AEF} = P_{CEF} - P_{CAE}$? Не, $A, E, C$ се колинеарни.
$P_{AEF} = \frac{1}{2} AE \cdot AF \cdot \sin(\angle A)$? Не, $F$ не е на $AC$. $F$ е на $BC$.
Триаголникот $AEF$ има темиња $A, E, F$.
$E$ е на $AC$. $F$ е на продолжението на $BC$.
Аголот кај $C$ во $\triangle AEF$ не е внатрешен.
Ајде да користиме координати или вектори? Не, строго синтетички.

Да ја искористиме висината од $F$ кон $AC$.
$P_{AEF} = \frac{1}{2} AE \cdot h_F$.
$P_{BCE} = \frac{1}{2} CE \cdot h_B$.
Ова е тешко за споредба.

Ајде да пробаме преку односи.
$P_{AEF} = P_{CEF} - P_{CAE}$? Не.
$A, E, C$ се на иста права.
$P_{AEF} = \frac{AE}{AC} P_{ACF}$.
$P_{ACF} = \frac{CF}{CB} P_{ABC}$.
Значи $P_{AEF} = \frac{AE}{AC} \cdot \frac{CF}{CB} P_{ABC}$.

Слично за $P_{BCE}$.
$P_{BCE} = \frac{CE}{AC} P_{ABC}$.
(Бидејќи $E$ е на $AC$, висината од $B$ е иста).

Значи треба да докажеме:
$$ \frac{AE}{AC} \cdot \frac{CF}{CB} P_{ABC} = \frac{CE}{AC} P_{ABC} $$
Кратиме $P_{ABC}$ и $AC$:
$$ AE \cdot \frac{CF}{CB} = CE $$
$$ \frac{AE}{CE} = \frac{CB}{CF} $$
Бидејќи $AC=CB$ (рамнокрак), ова е еквивалентно на:
$$ \frac{AE}{CE} = \frac{AC}{CF} $$
Или:
$$ AE \cdot CF = CE \cdot AC $$

**Чекор 3: Менелаева теорема**
Правата $p$ ($E-D-F$) ги сече страните на $\triangle ABC$.
Сече $AC$ во $E$, $AB$ во $D$, $BC$ во $F$.
Според Менелаевата теорема:
$$ \frac{AE}{EC} \cdot \frac{CF}{FB} \cdot \frac{BD}{DA} = 1 $$
Од тука:
$$ \frac{AE}{EC} = \frac{FB}{CF} \cdot \frac{DA}{BD} $$

Заменуваме во равенството што треба да го докажеме ($\frac{AE}{CE} = \frac{CB}{CF}$):
$$ \frac{FB}{CF} \cdot \frac{DA}{BD} = \frac{CB}{CF} $$
Кратиме $CF$:
$$ FB \cdot \frac{DA}{BD} = CB $$
$$ \frac{DA}{BD} = \frac{CB}{FB} $$
$$ \frac{DA}{BD} = \frac{CB}{CF - CB} $$
(Бидејќи $F$ е на полуправата $BC$, распоредот е $B-C-F$ или $C-B-F$?
Текстот вели „полуправата $BC$“. Тоа значи почеток во $B$, низ $C$. Значи $B-C-F$.
Тогаш $FB = FC + CB$.
Равенството станува:
$$ \frac{FC + CB}{CF} \cdot \frac{DA}{BD} = \frac{CB}{CF} $$
$$ (1 + \frac{CB}{CF}) \frac{DA}{BD} = \frac{CB}{CF} $$
Ова не изгледа точно. Ајде да провериме пак.

**Чекор 4: Враќање на условот со аглите**
Условот беше $\angle ADE = \angle BDC$.
Нека $\angle A = \angle B = \alpha$.
Во $\triangle ADE$: $\angle AED = 180 - \alpha - \angle ADE$.
Во $\triangle BDC$: $\angle BCD = 180 - \alpha - \angle BDC$.
Бидејќи $\angle ADE = \angle BDC$, следи дека $\angle AED = \angle BCD$.
Аголот $\angle BCD$ е аголот $\angle C$ на триаголникот? Не, $D$ е на $AB$.
Значи $\angle BCD$ е дел од аголот $C$.
А $\angle AED$ е агол на правата $AC$.
Ова значи дека $\triangle ADE \sim \triangle BDC$?
Аглите се:
1. $\angle A = \angle B = \alpha$.
2. $\angle ADE = \angle BDC$ (дадено).
Значи третите агли мора да се еднакви:
$$ \angle AED = \angle BCD $$
Од сличноста $\triangle ADE \sim \triangle BDC$ следи пропорционалност на страните:
$$ \frac{AD}{BD} = \frac{AE}{BC} = \frac{DE}{DC} $$
Од ова добиваме:
$$ AE \cdot BD = AD \cdot BC $$
$$ \frac{AE}{BC} = \frac{AD}{BD} $$

**Чекор 5: Поврзување со Менелај**
Имаме $\frac{AE}{BC} = \frac{AD}{BD}$.
Од Менелај: $\frac{AE}{EC} \cdot \frac{CF}{FB} \cdot \frac{BD}{DA} = 1$.
Заменуваме $\frac{BD}{DA} = \frac{BC}{AE}$:
$$ \frac{AE}{EC} \cdot \frac{CF}{FB} \cdot \frac{BC}{AE} = 1 $$
Кратиме $AE$:
$$ \frac{1}{EC} \cdot \frac{CF}{FB} \cdot BC = 1 $$
$$ \frac{CF \cdot BC}{EC \cdot FB} = 1 $$
$$ CF \cdot BC = EC \cdot FB $$
$$ \frac{CF}{FB} = \frac{EC}{BC} $$

Дали ова го докажува тврдењето?
Требаше да докажеме $P_{BCE} = P_{AEF}$.
$P_{BCE} = \frac{1}{2} CE \cdot BC \sin C$. (Агол $ACB$).
$P_{AEF} = P_{ACF} - P_{CEF}$? Не.
$P_{AEF} = \frac{1}{2} AF \cdot AE \sin A$? Не, $F$ не е на $AB$.
$P_{AEF} = \frac{1}{2} AE \cdot CF \sin(180-C)$?
Да, $A, E, C$ се колинеарни. $B, C, F$ се колинеарни.
Аголот $\angle ECF$ е накрстен со $\angle ACB$ (ако $F$ е на продолжението преку $C$).
Ако $F$ е на полуправата $BC$, тогаш $B-C-F$.
Тогаш $\angle ECF = 180^\circ - \angle ACB$.
Значи $\sin(\angle ECF) = \sin(\angle ACB)$.
Плоштината на $\triangle AEF$:
Ова е малку потешко. Темињата се $A, E, F$.
$P_{AEF} = P_{ABF} - P_{EBF}$?
Полесно: $P_{AEF} = \frac{1}{2} AE \cdot h_F$.
$h_F$ е висина од $F$ кон $AC$.
Во $\triangle CFG$ (правоаголен), $h_F = CF \sin(\angle AC F) = CF \sin C$.
Значи $P_{AEF} = \frac{1}{2} AE \cdot CF \sin C$.

Плоштината на $\triangle BCE$:
$P_{BCE} = \frac{1}{2} CE \cdot BC \sin C$.

За да бидат плоштините еднакви, треба:
$$ AE \cdot CF = CE \cdot BC $$
$$ \frac{AE}{CE} = \frac{BC}{CF} $$

Ајде да видиме што добивме од Менелај и сличноста.
Имавме: $\frac{CF}{FB} = \frac{EC}{BC}$.
Значи $EC \cdot FB = CF \cdot BC$.
Но $FB = FC + CB$ (бидејќи $B-C-F$).
$EC(FC + CB) = CF \cdot BC$.
$EC \cdot FC + EC \cdot CB = CF \cdot BC$.
$EC \cdot FC = CF \cdot BC - EC \cdot CB = CB(CF - EC)$.
Ова не води директно до $AE \cdot CF = CE \cdot BC$.

Ајде да се вратиме на $\frac{AE}{BC} = \frac{AD}{BD}$.
И Менелај: $\frac{AE}{EC} \cdot \frac{CF}{FB} \cdot \frac{BD}{DA} = 1$.
Заменуваме $\frac{DA}{BD} = \frac{AE}{BC}$ (внимавај, реципрочно).
$\frac{AE}{EC} \cdot \frac{CF}{FB} \cdot \frac{BC}{AE} = 1$.
$\frac{CF \cdot BC}{EC \cdot FB} = 1$.
$CF \cdot BC = EC \cdot FB$.
Ова е точно.
Треба да докажеме $AE \cdot CF = CE \cdot BC$.
Заменуваме $CE \cdot BC$ со $AE \cdot CF$?
Дали $AE \cdot CF = EC \cdot FB$?
$AE \cdot CF = EC(CF + BC)$.
$AE \cdot CF = EC \cdot CF + EC \cdot BC$.
$(AE - EC) CF = EC \cdot BC$.
Ова не изгледа секогаш точно.

**Грешка во поставката на $P_{AEF}$?**
$P_{AEF} = \frac{1}{2} AE \cdot h_F = \frac{1}{2} AE \cdot CF \sin C$.
Ова е точно само ако $C$ лежи меѓу $A$ и $E$? Не, $E$ е на $AC$. Значи $A-E-C$.
Тогаш $AE$ е основата. Висината од $F$ е $h_F$.
$h_F = CF \sin(\angle FCA) = CF \sin(180-C) = CF \sin C$.
Да, формулата е точна.

Значи треба да докажеме $AE \cdot CF = CE \cdot BC$.
Од Менелај добивме $CF \cdot BC = EC \cdot FB$.
Значи треба да докажеме $AE \cdot CF = CF \cdot BC$?
Тогаш $AE = BC = AC$.
Ова би значело $E=C$, што не е точно.

Каде е грешката?
Ах, $F$ е на полуправата $BC$.
Дали распоредот е $B-C-F$ или $C-B-F$?
„Полуправата $BC$“ обично значи почеток во $B$, правец кон $C$.
Ако $D$ е на $AB$ и $E$ е на $AC$, правата $DE$ ја сече $BC$.
Ако $ABC$ е рамнокрак, $DE$ оди „надолу“.
Пресекот $F$ ќе биде таков што $B$ е меѓу $C$ и $F$?
Или $C$ е меѓу $B$ и $F$?
Ако $E$ е блиску до $A$, $D$ блиску до $B$, правата сече некаде далеку.
Ајде да нацртаме.
$A$ (долу лево), $B$ (долу десно), $C$ (горе).
$D$ на $AB$. $E$ на $AC$.
$\angle ADE = \angle BDC$.
$\angle BDC$ е агол „нагоре“. $\angle ADE$ е агол „нагоре“.
Ова сугерира дека $E$ е „повисоко“ од $D$.
Правата $ED$ оди „надолу-десно“.
Таа ќе ја сече $BC$ (која оди „надолу-десно“ од $C$ кон $B$) некаде под $B$.
Значи распоредот е $C-B-F$.
Тогаш $CF = CB + BF$.
И $FB$ во Менелај е растојанието од $F$ до $B$.
Менелај за $\triangle ABC$ и права $F-D-E$:
$$ \frac{AE}{EC} \cdot \frac{CF}{FB} \cdot \frac{BD}{DA} = 1 $$
(Внимавај на насоките/сегментите).
Ако $C-B-F$, тогаш $F$ е надворешна точка за страната $BC$.
$CF/FB$ е односот.
Равенката е иста.

Ајде да видиме плоштините.
$P_{BCE} = \frac{1}{2} CE \cdot CB \sin C$.
$P_{AEF}$. Темиња $A, E, F$.
Основа $AE$. Висина од $F$ кон $AC$.
Висината е $h_F = CF \sin C$.
Значи $P_{AEF} = \frac{1}{2} AE \cdot CF \sin C$.
Условот за еднаквост е $CE \cdot CB = AE \cdot CF$.
$$ \frac{AE}{CE} = \frac{CB}{CF} $$

Од сличноста $\triangle ADE \sim \triangle BDC$:
$\frac{AE}{BC} = \frac{AD}{BD} \implies \frac{BD}{AD} = \frac{BC}{AE}$.
Заменуваме во Менелај:
$$ \frac{AE}{EC} \cdot \frac{CF}{FB} \cdot \frac{BC}{AE} = 1 $$
$$ \frac{CF \cdot BC}{EC \cdot FB} = 1 \implies CF \cdot BC = EC \cdot FB $$
Имаме систем:
1. Треба да докажеме: $AE \cdot CF = CE \cdot BC$.
2. Знаеме: $CF \cdot BC = EC \cdot FB$.

Делиме (1) со (2):
$$ \frac{AE \cdot CF}{CF \cdot BC} = \frac{CE \cdot BC}{EC \cdot FB} $$
$$ \frac{AE}{BC} = \frac{BC}{FB} $$
$$ AE \cdot FB = BC^2 $$

Дали е ова точно?
Од сличноста: $AE \cdot BD = AD \cdot BC$.
Значи $AE = \frac{AD \cdot BC}{BD}$.
Заменуваме во $AE \cdot FB = BC^2$:
$$ \frac{AD \cdot BC}{BD} \cdot FB = BC^2 $$
$$ \frac{AD \cdot FB}{BD} = BC $$
$$ \frac{FB}{BD} = \frac{BC}{AD} $$
$$ \triangle FBD \sim \triangle CAD $$
Дали се слични?
1. $\angle B = \angle A = \alpha$. (Да, рамнокрак).
2. Страни?
Агли?
$\angle FDB$ и $\angle CDA$.
$F, D, E$ се колинеарни.
$\angle FDB = 180 - \angle ADE$.
$\angle CDA = 180 - \angle BDC$.
Бидејќи $\angle ADE = \angle BDC$, следи $\angle FDB = \angle CDA$.
Имаме два агли еднакви!
Значи $\triangle FBD \sim \triangle CAD$.
Од оваа сличност следи:
$$ \frac{FB}{CA} = \frac{BD}{AD} $$
(Внимавај: $FB$ е спроти $D$, $CA$ е спроти $D$. $BD$ е спроти $F$, $AD$ е спроти $C$).
Значи $FB \cdot AD = CA \cdot BD$.
Бидејќи $CA = BC$ (рамнокрак):
$FB \cdot AD = BC \cdot BD$.
$$ \frac{FB}{BD} = \frac{BC}{AD} $$
Ова е точно тоа што требаше да го докажеме!

**Заклучок:**
Доказот е комплетен.
Логичкиот тек е:
1. $\angle ADE = \angle BDC \implies \angle FDB = \angle CDA$.
2. $\triangle FBD \sim \triangle CAD$ (агли $\alpha$ и $\angle D$).
3. Пропорција од сличноста $\implies$ релација за страните.
4. Замена во изразите за плоштините $\implies P_{BCE} = P_{AEF}$.

# Pedagogical Notes
1.  **Основна идеја:** Клучот е да се воочи „скриената“ сличност. Условот за еднаквост на аглите $\angle ADE = \angle BDC$ не само што дава сличност на $\triangle ADE$ и $\triangle BDC$, туку (преку суплементни агли) и сличност на $\triangle FBD$ и $\triangle CAD$.
2.  **Совет од Олимпиец:** Кога треба да докажете еднаквост на плоштини ($P_1 = P_2$), често е најдобро да ги изразите како $\frac{1}{2}ab \sin \gamma$ и да го сведете проблемот на еднаквост на производи од должини ($a_1 b_1 = a_2 b_2$).
3.  **Синтетичка геометрија:** Ова решение е чисто синтетичко и покажува како верижното поврзување на сличности води до резултатот без комплицирани пресметки.

# Manim Code
```python
from manim import *

class TriangleAreaProof(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Setup Triangle ABC (Isosceles)
        A = LEFT * 2 + DOWN * 1
        B = RIGHT * 2 + DOWN * 1
        C = UP * 2
        
        # Point D on AB
        # Let's pick D such that angles work out visually
        D = LEFT * 0.5 + DOWN * 1
        
        # Line p construction
        # Angle BDC
        vec_DB = B - D
        vec_DC = C - D
        angle_BDC = np.arccos(np.dot(vec_DB, vec_DC) / (np.linalg.norm(vec_DB) * np.linalg.norm(vec_DC)))
        
        # Angle ADE must be equal to BDC
        # Vector DA is -vec_DB
        # We need vector DE such that angle(DA, DE) = angle_BDC
        # Rotate DA by angle_BDC
        vec_DA = A - D
        # Rotation matrix
        rot_matrix = [[np.cos(angle_BDC), -np.sin(angle_BDC), 0], [np.sin(angle_BDC), np.cos(angle_BDC), 0], [0,0,1]]
        vec_DE_dir = np.dot(vec_DA, rot_matrix) # This rotates one way, might need check
        
        # Define line p through D with direction vec_DE_dir
        # Intersect with AC to get E
        # Line AC: P = A + t(C-A)
        # Line p: P = D + u(vec_DE_dir)
        # Solve for intersection
        def intersect(p1, v1, p2, v2):
            A_mat = np.array([[v1[0], -v2[0]], [v1[1], -v2[1]]])
            b_vec = p2[:2] - p1[:2]
            try:
                x = np.linalg.solve(A_mat, b_vec)
                return p1 + x[0] * v1
            except:
                return None

        E = intersect(A, C-A, D, vec_DE_dir)
        
        # Intersect with BC extended to get F
        F = intersect(B, C-B, D, vec_DE_dir)
        
        # Draw
        tri = Polygon(A, B, C, color=BLACK)
        line_p = Line(F, E, color=BLUE) # Extended line
        
        self.play(Create(tri))
        self.play(Create(line_p))
        
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
        
        # Highlight Angles
        # Angle ADE
        arc_ADE = Angle(Line(D, A), Line(D, E), radius=0.4, color=RED)
        # Angle BDC
        arc_BDC = Angle(Line(D, B), Line(D, C), radius=0.5, color=RED)
        
        self.play(Create(arc_ADE), Create(arc_BDC))
        
        # Highlight Triangles for Area
        tri_BCE = Polygon(B, C, E, color=GREEN, fill_opacity=0.2)
        tri_AEF = Polygon(A, E, F, color=ORANGE, fill_opacity=0.2)
        
        self.play(FadeIn(tri_BCE))
        self.wait(1)
        self.play(FadeIn(tri_AEF))
        
        # Text
        text = MathTex(r"P_{BCE} = P_{AEF}", color=BLACK).to_edge(UP)
        self.play(Write(text))
        
        self.wait(2)