---
problem_id: sigma139_p1898_final
title: Трапез со нормална дијагонала (Синтетичко решение)
grade: 11
difficulty: 6
tags:
  - geometry
  - trapezoid
  - synthetic_geometry
  - parallelogram_construction
  - cosine_rule
source: Sigma 139, Zadaca 1898
type: geometry
---

# Текст на задачата
Во трапезот $ABCD$ бочната страна $BC$ е нормална на дијагоналата $BD$, $\angle DCB = \frac{1}{2} \angle ADC$ и $\overline{AB} = \frac{1}{2} \overline{AD}$. Докажи дека $\overline{AC} = \overline{CD}$.

# Решение
## Стратегија
За да го решиме овој проблем чисто синтетички, ќе користиме помошна конструкција која е стандардна за трапези: повлекување на права низ едно теме паралелна со спротивниот крак.
1.  Ќе конструираме паралелограм за да ги пренесеме должините и аглите во еден триаголник.
2.  Ќе ги искористиме дадените услови за да ги изразиме сите страни преку еден параметар $x$.
3.  Ќе докажеме дека триаголникот $ACD$ е рамнокрак со пресметка на неговите страни.

## Чекор по чекор

**Чекор 1: Ознаки и конструкција**
Нека $\angle DCB = \alpha$. Според условот, $\angle ADC = 2\alpha$.
Нека $AB = x$. Според условот, $AD = 2x$.
Низ темето $B$ повлекуваме права паралелна со кракот $AD$, која ја сече основата $CD$ во точка $K$.
Четириаголникот $ABKD$ е паралелограм (бидејќи $AB \parallel DK$ и $AD \parallel BK$).
Од својствата на паралелограм следи:
*   $DK = AB = x$
*   $BK = AD = 2x$
*   $\angle BKC = \angle ADC = 2\alpha$ (согласни агли).

**Чекор 2: Анализа на триаголникот $BKC$**
Во $\triangle BKC$:
*   $\angle BCK = \alpha$ (дадено).
*   $\angle BKC = 2\alpha$ (од конструкцијата).
*   $\angle KBC = 180^\circ - (2\alpha + \alpha) = 180^\circ - 3\alpha$.

Применуваме Синусна теорема за $\triangle BKC$:
$$ \frac{BK}{\sin \alpha} = \frac{BC}{\sin 2\alpha} $$
Заменуваме $BK = 2x$:
$$ \frac{2x}{\sin \alpha} = \frac{BC}{2\sin \alpha \cos \alpha} $$
Кратиме $\sin \alpha$ (бидејќи $\alpha \neq 0$):
$$ 2x = \frac{BC}{2\cos \alpha} \implies BC = 4x \cos \alpha $$

**Чекор 3: Анализа на правоаголниот триаголник $BCD$**
Дадено е дека $BC \perp BD$, што значи $\triangle BCD$ е правоаголен со прав агол кај $B$ (во однос на дијагоналата, т.е. $\angle DBC = 90^\circ$).
Во овој триаголник:
$$ \cos(\angle DCB) = \frac{BC}{CD} $$
$$ \cos \alpha = \frac{4x \cos \alpha}{CD} $$
Кратиме $\cos \alpha$ (бидејќи $\alpha < 90^\circ$):
$$ 1 = \frac{4x}{CD} \implies CD = 4x $$

**Чекор 4: Наоѓање на вредноста на $\cos \alpha$**
Сега да го разгледаме триаголникот $ABD$.
$\angle ADB = \angle ADC - \angle BDC$.
Во правоаголниот $\triangle BCD$, $\angle BDC = 90^\circ - \alpha$.
Значи $\angle ADB = 2\alpha - (90^\circ - \alpha) = 3\alpha - 90^\circ$.
Применуваме Синусна теорема за $\triangle ABD$:
$$ \frac{AB}{\sin(3\alpha - 90^\circ)} = \frac{AD}{\sin(\angle ABD)} $$
Знаеме дека $\angle ABD = \angle BDC = 90^\circ - \alpha$ (наизменични агли).
$$ \frac{x}{-\cos 3\alpha} = \frac{2x}{\cos \alpha} $$
$$ \frac{1}{-\cos 3\alpha} = \frac{2}{\cos \alpha} \implies \cos \alpha = -2\cos 3\alpha $$
Користиме формула за троен агол $\cos 3\alpha = 4\cos^3 \alpha - 3\cos \alpha$:
$$ \cos \alpha = -2(4\cos^3 \alpha - 3\cos \alpha) $$
$$ \cos \alpha = -8\cos^3 \alpha + 6\cos \alpha $$
$$ 8\cos^3 \alpha = 5\cos \alpha $$
Делиме со $\cos \alpha$:
$$ 8\cos^2 \alpha = 5 \implies \cos^2 \alpha = \frac{5}{8} $$

**Чекор 5: Доказ дека $AC = CD$**
Во $\triangle ACD$, ги знаеме страните $AD = 2x$, $CD = 4x$ и аголот меѓу нив $\angle ADC = 2\alpha$.
Применуваме Косинусна теорема за да ја најдеме страната $AC$:
$$ AC^2 = AD^2 + CD^2 - 2 \cdot AD \cdot CD \cdot \cos 2\alpha $$
$$ AC^2 = (2x)^2 + (4x)^2 - 2(2x)(4x)(2\cos^2 \alpha - 1) $$
$$ AC^2 = 4x^2 + 16x^2 - 16x^2 \left( 2 \cdot \frac{5}{8} - 1 \right) $$
$$ AC^2 = 20x^2 - 16x^2 \left( \frac{5}{4} - 1 \right) $$
$$ AC^2 = 20x^2 - 16x^2 \left( \frac{1}{4} \right) $$
$$ AC^2 = 20x^2 - 4x^2 = 16x^2 $$
$$ AC = \sqrt{16x^2} = 4x $$

Бидејќи $CD = 4x$ (од Чекор 3) и $AC = 4x$, заклучуваме дека:
$$ AC = CD $$

**Заклучок:**
Докажавме дека страните $AC$ и $CD$ се еднакви.

# Pedagogical Notes
1.  **Основна идеја:** Конструкцијата на паралелограм ($ABKD$) е клучниот чекор што овозможува пренесување на должината $AD$ и аголот $D$ на исто место со $BC$, формирајќи триаголник ($BKC$) кој може лесно да се реши.
2.  **Совет од Олимпиец:** Воведувањето на параметар $x$ за најмалата страна ($AB$) е многу корисно. Наместо да работите со имиња на отсечки ($AB, CD$), работите со алгебарски изрази ($x, 2x, 4x$), што е многу попрегледно.
3.  **Синтеза:** Ова решение е убав спој на геометриска конструкција и тригонометриски идентитети. Иако користиме косинуси, суштината е геометриска (односи во триаголник).

# Manim Code
```python
from manim import *

class TrapezoidFinalProof(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Setup parameters
        # cos^2(alpha) = 5/8
        alpha_val = np.arccos(np.sqrt(5/8))
        x = 1.5
        
        # Coordinates
        D = ORIGIN
        C = RIGHT * (4 * x)
        # A is at distance 2x from D at angle 2*alpha
        A = 2 * x * np.array([np.cos(2*alpha_val), np.sin(2*alpha_val), 0])
        # B is at distance x from A, parallel to DC
        B = A + RIGHT * x
        
        # Draw Trapezoid
        trap = Polygon(A, B, C, D, color=BLACK, stroke_width=4)
        diag_BD = Line(B, D, color=BLUE)
        diag_AC = Line(A, C, color=RED)
        
        # Labels
        lbls = VGroup(
            MathTex("A").next_to(A, UL),
            MathTex("B").next_to(B, UR),
            MathTex("C").next_to(C, DR),
            MathTex("D").next_to(D, DL)
        ).set_color(BLACK)
        
        self.play(Create(trap))
        self.play(Write(lbls))
        
        # Construction K
        K = RIGHT * x # On DC such that DK = x
        line_BK = DashedLine(B, K, color=GREEN)
        lbl_K = MathTex("K", color=BLACK).next_to(K, DOWN)
        
        self.play(Create(line_BK), Write(lbl_K))
        
        # Length annotations
        txt_x = MathTex("x", color=BLACK).next_to(Line(A, B), UP)
        txt_2x = MathTex("2x", color=BLACK).next_to(Line(A, D), LEFT)
        txt_2x_bk = MathTex("2x", color=GREEN).next_to(line_BK, RIGHT)
        
        self.play(Write(txt_x), Write(txt_2x), Write(txt_2x_bk))
        
        # Proof steps text
        step1 = MathTex(r"1. \ \triangle BKC \implies BC = 4x \cos \alpha", color=BLACK).to_corner(UL).scale(0.7)
        step2 = MathTex(r"2. \ \triangle BCD \implies CD = 4x", color=BLACK).next_to(step1, DOWN, aligned_edge=LEFT).scale(0.7)
        step3 = MathTex(r"3. \ \triangle ABD \implies \cos^2 \alpha = 5/8", color=BLACK).next_to(step2, DOWN, aligned_edge=LEFT).scale(0.7)
        step4 = MathTex(r"4. \ \triangle ACD \implies AC^2 = 16x^2 \implies AC=4x", color=RED).next_to(step3, DOWN, aligned_edge=LEFT).scale(0.7)
        
        self.play(Write(step1))
        self.wait(1)
        self.play(Write(step2))
        self.wait(1)
        self.play(Write(step3))
        self.wait(1)
        self.play(Create(diag_AC))
        self.play(Write(step4))
        
        # Final highlight
        self.play(Indicate(diag_AC), Indicate(Line(C, D)))
        
        self.wait(2)