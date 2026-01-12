---
problem_id: sigma139_p1894_synthetic_final
title: Златен пресек во квадрат (Синтетичко решение)
grade: 11
difficulty: 7
tags:
  - geometry
  - synthetic_geometry
  - similarity
  - golden_ratio
source: Sigma 139, Zadaca 1894
type: geometry
---

# Текст на задачата
Нека $ABCD$ е квадрат. Отсечката $AB$ е поделена внатрешно со точка $H$ така што $\overline{AB} \cdot \overline{BH} = \overline{AH}^2$. Нека $E$ е средишна точка на отсечката $AD$ и $X$ е средишна точка на отсечката $AH$. Нека $Y$ е точка од отсечката $EB$ така што $XY$ е нормална на $EB$. Докажи дека $\overline{XY} = \overline{XH}$.

# Решение
## Стратегија
Ќе користиме **сличност на триаголници** за да ја пресметаме должината на отсечката $XY$.
1.  Ќе ги изразиме сите должини преку страната на квадратот, користејќи го својството на златниот пресек за точката $H$.
2.  Ќе воочиме дека триаголниците $\triangle EAB$ и $\triangle XYB$ се слични (имаат заеднички агол и по еден прав агол).
3.  Преку пропорцијата од сличноста ќе ја пресметаме $XY$ и ќе покажеме дека е еднаква на $XH$.

## Чекор по чекор

**Чекор 1: Анализа на должините**
Нека страната на квадратот е $2a$ (за да избегнеме дропки при делење на половина).
Значи $AB = AD = 2a$.
Точката $E$ е средина на $AD$, па $AE = a$.
Во правоаголниот триаголник $\triangle EAB$, хипотенузата е:
$$ EB = \sqrt{AE^2 + AB^2} = \sqrt{a^2 + (2a)^2} = \sqrt{5a^2} = a\sqrt{5} $$

**Чекор 2: Златен пресек**
Условот $AB \cdot BH = AH^2$ значи дека $H$ ја дели $AB$ во златен пресек.
Нека $AH = x$. Тогаш $BH = 2a - x$.
$$ 2a(2a - x) = x^2 $$
$$ x^2 + 2ax - 4a^2 = 0 $$
Решавајќи ја квадратната равенка по $x$:
$$ x = \frac{-2a + \sqrt{4a^2 + 16a^2}}{2} = \frac{-2a + 2a\sqrt{5}}{2} = a(\sqrt{5} - 1) $$
Значи, $AH = a(\sqrt{5} - 1)$.

Точката $X$ е средина на $AH$, па:
$$ XH = AX = \frac{AH}{2} = \frac{a(\sqrt{5} - 1)}{2} $$
Ова е вредноста што треба да ја добиеме и за $XY$.

**Чекор 3: Сличност на триаголници**
Да ги разгледаме триаголниците $\triangle EAB$ и $\triangle XYB$.
1.  $\angle ABE$ е заеднички агол за двата триаголници (агол кај темето $B$).
2.  $\angle EAB = 90^\circ$ (агол на квадратот).
3.  $\angle XYB = 90^\circ$ (бидејќи $XY \perp EB$).

Бидејќи имаат по два еднакви агли, триаголниците се слични:
$$ \triangle EAB \sim \triangle XYB $$

**Чекор 4: Пресметка на $XY$**
Од сличноста следи пропорцијата на соодветните страни:
$$ \frac{XY}{EA} = \frac{BX}{EB} $$
(Катета спроти агол $B$ во малиот / Катета спроти агол $B$ во големиот = Хипотенуза во малиот / Хипотенуза во големиот? Не, внимателно со страните).
Во $\triangle XYB$: $XY$ е катета спроти агол $B$. Хипотенуза е $XB$.
Во $\triangle EAB$: $EA$ е катета спроти агол $B$. Хипотенуза е $EB$.
Значи пропорцијата е точна:
$$ \frac{XY}{EA} = \frac{XB}{EB} $$

Ни треба должината на $XB$.
$XB = AB - AX = 2a - \frac{a(\sqrt{5}-1)}{2} = \frac{4a - a\sqrt{5} + a}{2} = \frac{a(5 - \sqrt{5})}{2}$.

Сега заменуваме во пропорцијата:
$$ XY = EA \cdot \frac{XB}{EB} = a \cdot \frac{\frac{a(5 - \sqrt{5})}{2}}{a\sqrt{5}} $$
$$ XY = \frac{a(5 - \sqrt{5})}{2\sqrt{5}} $$
Рационализираме (множиме и делиме со $\sqrt{5}$):
$$ XY = \frac{a(5\sqrt{5} - 5)}{2 \cdot 5} = \frac{5a(\sqrt{5} - 1)}{10} = \frac{a(\sqrt{5} - 1)}{2} $$

**Чекор 5: Заклучок**
Добивме:
$$ XY = \frac{a(\sqrt{5} - 1)}{2} $$
Од Чекор 2 имаме:
$$ XH = \frac{a(\sqrt{5} - 1)}{2} $$
Следи дека $XY = XH$.

# Pedagogical Notes
1.  **Основна идеја:** Сличноста на триаголници е многу моќна алатка кога имаме прави агли и заеднички темиња. Клучно е правилно да се идентификуваат соодветните страни.
2.  **Совет од Олимпиец:** Кога работите со златен пресек, често се појавуваат изрази од типот $5-\sqrt{5}$. Корисно е да знаете дека $\frac{5-\sqrt{5}}{\sqrt{5}} = \sqrt{5}-1$. Ова алгебарско упростување често е последниот чекор во доказот.
3.  **Избор на променлива:** Користењето на $2a$ за страната на квадратот наместо $a$ значително ја поедностави работата со средишните точки, избегнувајќи двојни дропки во раните фази.

# Manim Code
```python
from manim import *

class SyntheticProof(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Setup
        s = 3
        A = UP * s + LEFT * s
        B = UP * s + RIGHT * s
        D = DOWN * s + LEFT * s
        E = (A + D) / 2
        
        # Golden Ratio
        phi = (np.sqrt(5) - 1) / 2
        H = A + RIGHT * (2 * s * phi)
        X = (A + H) / 2
        
        # Y calculation via projection
        vec_EB = B - E
        vec_XB = B - X
        vec_EX = X - E
        t = np.dot(vec_EX, vec_EB) / np.dot(vec_EB, vec_EB)
        Y = E + t * vec_EB
        
        # Draw
        line_AB = Line(A, B, color=BLACK)
        line_AD = Line(A, D, color=BLACK)
        line_EB = Line(E, B, color=BLUE)
        line_XY = Line(X, Y, color=RED)
        line_XH = Line(X, H, color=GREEN)
        
        self.play(Create(line_AB), Create(line_AD), Create(line_EB))
        
        # Labels
        lbls = VGroup(
            MathTex("A").next_to(A, UL),
            MathTex("B").next_to(B, UR),
            MathTex("E").next_to(E, LEFT),
            MathTex("X").next_to(X, UP),
            MathTex("Y").next_to(Y, DOWN),
            MathTex("H").next_to(H, UP)
        ).set_color(BLACK)
        self.play(Write(lbls))
        
        self.play(Create(line_XY), Create(line_XH))
        
        # Similarity Highlight
        tri_EAB = Polygon(E, A, B, color=BLUE, fill_opacity=0.1)
        tri_XYB = Polygon(X, Y, B, color=RED, fill_opacity=0.1)
        
        self.play(FadeIn(tri_EAB))
        self.wait(0.5)
        self.play(FadeIn(tri_XYB))
        
        # Text
        sim_text = MathTex(r"\triangle EAB \sim \triangle XYB", color=BLACK).to_corner(UL)
        prop_text = MathTex(r"\frac{XY}{EA} = \frac{XB}{EB}", color=BLACK).next_to(sim_text, DOWN)
        res_text = MathTex(r"XY = XH", color=RED).next_to(prop_text, DOWN)
        
        self.play(Write(sim_text))
        self.play(Write(prop_text))
        self.play(Write(res_text))
        
        self.wait(2)