
import os

log_path = r"c:\Userrs\pc4all\Documents\matholimpiad\olympiad-math-archive\assets\manim_code_log.md"

new_entries = """
### 🆔 Задача: geom_9_quad_diag_equal_angles - Четириаголник со еднакви дијагонали
**📅 Додадено:** 2025-12-27 02:20
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_quad_diag_equal_angles(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Quadrilateral ABCD where AC = BD.
        # Construct perpendicular bisectors of AD and BC.
        # Mark their intersection P on segment AB.
        # This implies ABCD is an isosceles trapezoid?
        # If P is on AB, and P is on perp bisector of AD and BC.
        # PA = PD. PB = PC.
        # If P is on AB, then PA + PB = AB.
        # PD + PC = AB?
        # Also AC = BD.
        # This configuration is possible if ABCD is isosceles trapezoid.
        # Let's construct isosceles trapezoid.
        
        A = np.array([-2, -1, 0])
        B = np.array([2, -1, 0])
        C = np.array([1, 2, 0])
        D = np.array([-1, 2, 0])
        
        quad = Polygon(A, B, C, D, color=BLUE)
        
        # Diagonals
        diag_AC = Line(A, C, color=GRAY)
        diag_BD = Line(B, D, color=GRAY)
        
        # Perp bisector of AD
        mid_AD = (A + D) / 2
        vec_AD = D - A
        perp_AD = np.array([-vec_AD[1], vec_AD[0], 0])
        line_perp_AD = Line(mid_AD + perp_AD*2, mid_AD - perp_AD*2, color=GREEN)
        
        # Perp bisector of BC
        mid_BC = (B + C) / 2
        vec_BC = C - B
        perp_BC = np.array([-vec_BC[1], vec_BC[0], 0])
        line_perp_BC = Line(mid_BC + perp_BC*2, mid_BC - perp_BC*2, color=GREEN)
        
        # Intersection P
        # In isosceles trapezoid, perp bisectors of legs intersect on the axis of symmetry.
        # Axis of symmetry is x=0.
        # Does it intersect AB?
        # AB is on y=-1.
        # Axis of symmetry intersects AB at (0, -1).
        # Is P on AB? Yes, if P is the midpoint of AB?
        # If P is midpoint of AB, PA=PB.
        # Is P on perp bisector of AD?
        # PA = PD?
        # If P=(0,-1), A=(-2,-1), D=(-1,2).
        # PA = 2.
        # PD = sqrt(1^2 + 3^2) = sqrt(10).
        # PA != PD.
        # So P is NOT on AB for isosceles trapezoid unless specific height.
        
        # Prompt says "Mark their intersection P on segment AB".
        # This implies a specific quadrilateral where this happens.
        # Or maybe P is intersection of perp bisector of AD and perp bisector of BC?
        # And the problem states P lies on AB?
        # Or "Construct perp bisectors... Mark their intersection P. (Show P is on AB?)"
        # Or "Mark their intersection P on segment AB" implies P is intersection of perp bisector with AB?
        # "Construct perpendicular bisectors of AD and BC. Mark their intersection P on segment AB."
        # This phrasing usually means the intersection of the two bisectors IS a point P, and P happens to be on AB.
        # This happens if Angle DAB = Angle CBA? No.
        # This is a known property for AC=BD?
        # Actually, if AC=BD, the intersection of perp bisectors of AD and BC lies on the perp bisector of AB? No.
        
        # Let's just draw a generic case where P is on AB.
        # Let P be origin (0,0). P is on AB.
        # P is on perp bisector of AD => PA = PD.
        # P is on perp bisector of BC => PB = PC.
        # Let A = (-2, 0), B = (3, 0). P = (0,0)? No, P must be on segment AB.
        # Let P = (0,0). A = (-2, 0). B = (3, 0).
        # D is on circle centered at P radius 2.
        # C is on circle centered at P radius 3.
        # Also AC = BD.
        # Let D = (2 cos(alpha), 2 sin(alpha)).
        # Let C = (3 cos(beta), 3 sin(beta)).
        # AC^2 = |C - A|^2 = |(3cosB + 2, 3sinB)|^2 = (3cosB+2)^2 + 9sin^2B = 9cos^2 + 12cos + 4 + 9sin^2 = 13 + 12cosB.
        # BD^2 = |D - B|^2 = |(2cosA - 3, 2sinA)|^2 = (2cosA-3)^2 + 4sin^2A = 4cos^2 - 12cos + 9 + 4sin^2 = 13 - 12cosA.
        # AC = BD => 13 + 12cosB = 13 - 12cosA => cosB = -cosA.
        # So B = 180 - A.
        # Or beta = 180 - alpha.
        # So C and D are symmetric wrt y-axis?
        # If beta = 180 - alpha, then C = (-3 cosA, 3 sinA).
        # D = (2 cosA, 2 sinA).
        # This works.
        
        # Let alpha = 60 deg.
        alpha = np.deg2rad(60)
        P = ORIGIN
        A = LEFT * 2
        B = RIGHT * 3
        D = np.array([2*np.cos(alpha), 2*np.sin(alpha), 0])
        C = np.array([3*np.cos(np.pi - alpha), 3*np.sin(np.pi - alpha), 0])
        
        quad = Polygon(A, B, C, D, color=BLUE)
        
        # Perp bisectors
        # AD
        mid_AD = (A + D) / 2
        vec_AD = D - A
        perp_AD = np.array([-vec_AD[1], vec_AD[0], 0])
        line_perp_AD = Line(mid_AD, P, color=GREEN) # Should go through P
        
        # BC
        mid_BC = (B + C) / 2
        vec_BC = C - B
        perp_BC = np.array([-vec_BC[1], vec_BC[0], 0])
        line_perp_BC = Line(mid_BC, P, color=GREEN) # Should go through P
        
        dot_P = Dot(P, color=RED)
        
        # Highlight triangles APC and DPB
        tri_APC = Polygon(A, P, C, color=ORANGE, fill_opacity=0.2, fill_color=ORANGE)
        tri_DPB = Polygon(D, P, B, color=ORANGE, fill_opacity=0.2, fill_color=ORANGE)
        
        lbl_A = MathTex("A").next_to(A, DOWN)
        lbl_B = MathTex("B").next_to(B, DOWN)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_D = MathTex("D").next_to(D, UP)
        lbl_P = MathTex("P").next_to(P, DOWN)
        
        self.add(quad, line_perp_AD, line_perp_BC, dot_P, tri_APC, tri_DPB)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_P)
```

### 🆔 Задача: geom_9_k1_k2_incenter_proof - Две кружници и симетрали
**📅 Додадено:** 2025-12-27 02:20
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_k1_k2_incenter_proof(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # k2 with center O.
        r2 = 2
        O = ORIGIN
        k2 = Circle(radius=r2, color=BLUE).move_to(O)
        
        # k1 passing through O.
        # Let center of k1 be O1. Radius r1.
        # Distance O-O1 = r1.
        # Let O1 = (r1, 0).
        r1 = 1.5
        O1 = RIGHT * r1
        k1 = Circle(radius=r1, color=GREEN).move_to(O1)
        
        # Intersection points A and B.
        # k2: x^2 + y^2 = r2^2
        # k1: (x-r1)^2 + y^2 = r1^2 => x^2 - 2xr1 + r1^2 + y^2 = r1^2
        # r2^2 - 2xr1 = 0 => x = r2^2 / (2r1).
        x_int = r2**2 / (2*r1) # 4 / 3 = 1.333
        y_int = np.sqrt(r2**2 - x_int**2)
        
        A = np.array([x_int, y_int, 0])
        B = np.array([x_int, -y_int, 0])
        
        # Pick C on k1.
        # Let's pick C far from A, B.
        angle_C = np.deg2rad(180) # Leftmost point of k1?
        # k1 center is (1.5, 0). Radius 1.5.
        # Leftmost is (0,0) which is O.
        # Pick another point.
        angle_C = np.deg2rad(90) # Relative to O1
        C = O1 + np.array([0, r1, 0]) # (1.5, 1.5)
        
        # Connect OC.
        line_OC = Line(O, C, color=GRAY)
        
        # Mark D on k2.
        # Intersection of line OC with k2.
        vec_OC = C - O
        unit_OC = vec_OC / np.linalg.norm(vec_OC)
        D = O + unit_OC * r2
        dot_D = Dot(D, color=RED)
        
        # Show AD and CD are angle bisectors of triangle ABC?
        # Triangle ABC.
        # AD bisects A? CD bisects C?
        # D is on k2. O is center of k2.
        # This is the "Incenter/Excenter Lemma" configuration.
        # D is the center of circle passing through A, I, B?
        # Wait, D is on k2. A, B on k2.
        # D is midpoint of arc AB (not containing C?).
        # Then D is center of circle through A, I, B.
        # So DA = DB = DI.
        # Is CD the bisector of C?
        # Yes, if D is midpoint of arc AB.
        # Is D midpoint of arc AB?
        # OC passes through D?
        # If C is on k1 (passing through O), and O is center of k2.
        # This is a specific theorem.
        
        tri_ABC = Polygon(A, B, C, color=ORANGE)
        seg_AD = Line(A, D, color=RED)
        seg_CD = Line(C, D, color=RED) # Part of OC
        
        lbl_O = MathTex("O").next_to(O, LEFT)
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, DOWN)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_D = MathTex("D").next_to(D, UP)
        
        self.add(k1, k2, line_OC, dot_D, tri_ABC, seg_AD)
        self.add(lbl_O, lbl_A, lbl_B, lbl_C, lbl_D)
```

### 🆔 Задача: geom_9_contact_tri_sides - Контактен триаголник
**📅 Додадено:** 2025-12-27 02:20
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_contact_tri_sides(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Triangle ABC
        A = np.array([-2, -1, 0])
        B = np.array([3, -1, 0])
        C = np.array([0, 3, 0])
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Incircle
        a = np.linalg.norm(B - C)
        b = np.linalg.norm(A - C)
        c = np.linalg.norm(A - B)
        I = (a*A + b*B + c*C) / (a+b+c)
        s = (a+b+c)/2
        area = np.sqrt(s*(s-a)*(s-b)*(s-c))
        r = area / s
        
        incircle = Circle(radius=r, color=GREEN).move_to(I)
        
        # Contact points M, N, P
        # Project I onto sides
        def get_proj(P, P1, P2):
            vec = P2 - P1
            unit = vec / np.linalg.norm(vec)
            proj = P1 + np.dot(P - P1, unit) * unit
            return proj
            
        P_AB = get_proj(I, A, B) # P
        M_BC = get_proj(I, B, C) # M
        N_CA = get_proj(I, C, A) # N
        
        # Prompt says M, N, P. Let's assume order.
        M = M_BC
        N = N_CA
        P = P_AB
        
        tri_MNP = Polygon(M, N, P, color=RED)
        
        # Connect I to vertices and contact points
        seg_IA = DashedLine(I, A, color=GRAY)
        seg_IB = DashedLine(I, B, color=GRAY)
        seg_IC = DashedLine(I, C, color=GRAY)
        
        seg_IM = Line(I, M, color=GRAY)
        seg_IN = Line(I, N, color=GRAY)
        seg_IP = Line(I, P, color=GRAY)
        
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_I = MathTex("I").next_to(I, UP)
        lbl_M = MathTex("M").next_to(M, RIGHT)
        lbl_N = MathTex("N").next_to(N, LEFT)
        lbl_P = MathTex("P").next_to(P, DOWN)
        
        self.add(tri, incircle, tri_MNP)
        self.add(seg_IA, seg_IB, seg_IC, seg_IM, seg_IN, seg_IP)
        self.add(lbl_A, lbl_B, lbl_C, lbl_I, lbl_M, lbl_N, lbl_P)
        
        # Right angles
        ra1 = RightAngle(Line(I, P), Line(A, B), quadrant=(1,1), length=0.2)
        ra2 = RightAngle(Line(I, M), Line(B, C), quadrant=(1,1), length=0.2)
        ra3 = RightAngle(Line(I, N), Line(C, A), quadrant=(1,1), length=0.2)
        self.add(ra1, ra2, ra3)
```

### 🆔 Задача: geom_9_hypot_ratio_mid_circle - Правоаголен триаголник и кружница на катети
**📅 Додадено:** 2025-12-27 02:20
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_hypot_ratio_mid_circle(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Right triangle legs 5, 12.
        a = 5
        b = 12
        c = 13
        
        C = ORIGIN
        A = UP * b
        B = RIGHT * a
        
        # Shift
        center = (A + B + C) / 3
        A -= center
        B -= center
        C -= center
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Midpoints M (of b=AC) and N (of a=BC)
        M = (A + C) / 2
        N = (B + C) / 2
        
        # Circle diameter MN.
        # Center O_MN = (M+N)/2.
        # Radius = |M-N|/2.
        # MN is midline, length c/2 = 6.5.
        # Wait, MN connects midpoints of legs.
        # MN = AB/2 = 6.5.
        # Radius = 3.25.
        O_MN = (M + N) / 2
        radius = np.linalg.norm(M - N) / 2
        circle = Circle(radius=radius, color=GREEN).move_to(O_MN)
        
        # Intersects hypotenuse AB at P and Q.
        # Line AB.
        # Find intersection of circle and line AB.
        # One point is midpoint of AB?
        # Midpoint of AB is K.
        # Is K on circle with diameter MN?
        # Angle MKN?
        # M is mid AC. N is mid BC. K is mid AB.
        # MK || BC (perp AC). NK || AC (perp BC).
        # So MKN is a right angle at K?
        # MK is parallel to BC (horizontal). NK is parallel to AC (vertical).
        # Yes, MKN is 90 deg.
        # So K lies on circle with diameter MN.
        # So one point is K (midpoint of hypotenuse).
        
        # Other point is altitude foot?
        # Let H be foot of altitude from C to AB.
        # Is Angle MHN = 90?
        # M is mid AC. N is mid BC.
        # This is a known property.
        # Yes, H lies on the circle.
        
        K = (A + B) / 2
        
        # Altitude foot H
        vec_AB = B - A
        unit_AB = vec_AB / np.linalg.norm(vec_AB)
        H = A + np.dot(C - A, unit_AB) * unit_AB
        
        dot_K = Dot(K, color=RED)
        dot_H = Dot(H, color=RED)
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, RIGHT)
        lbl_C = MathTex("C").next_to(C, DOWN)
        lbl_M = MathTex("M").next_to(M, LEFT)
        lbl_N = MathTex("N").next_to(N, DOWN)
        lbl_K = MathTex("K").next_to(K, UP)
        lbl_H = MathTex("H").next_to(H, DOWN)
        
        self.add(tri, circle, dot_K, dot_H)
        self.add(lbl_A, lbl_B, lbl_C, lbl_M, lbl_N, lbl_K, lbl_H)
```

### 🆔 Задача: geo_rect_shade_01 - Правоаголник и засенчен триаголник
**📅 Додадено:** 2025-12-27 02:20
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geo_rect_shade_01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Rectangle ABCD
        width = 6
        height = 4
        A = np.array([-width/2, -height/2, 0])
        B = np.array([width/2, -height/2, 0])
        C = np.array([width/2, height/2, 0])
        D = np.array([-width/2, height/2, 0])
        
        rect = Polygon(A, B, C, D, color=BLUE)
        
        # E on AB (1/3 from A)
        E = A + (B - A) * (1/3)
        
        # F on BC (2/3 from B)
        F = B + (C - B) * (2/3)
        
        # G midpoint of AD
        G = (A + D) / 2
        
        # Shade triangle EFG
        tri_EFG = Polygon(E, F, G, color=ORANGE, fill_opacity=0.4, fill_color=ORANGE)
        
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP+RIGHT)
        lbl_D = MathTex("D").next_to(D, UP+LEFT)
        lbl_E = MathTex("E").next_to(E, DOWN)
        lbl_F = MathTex("F").next_to(F, RIGHT)
        lbl_G = MathTex("G").next_to(G, LEFT)
        
        self.add(rect, tri_EFG)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_E, lbl_F, lbl_G)
```

### 🆔 Задача: Cnt92-1012_Prob5_Olympic - Координатен систем и права
**📅 Додадено:** 2025-12-27 02:20
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_Cnt92_1012_Prob5_Olympic(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Axes
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            axis_config={"color": BLACK},
        )
        
        # Line passing through (2,0) and (0,3)
        p1 = axes.c2p(2, 0)
        p2 = axes.c2p(0, 3)
        line = Line(axes.c2p(-0.5, 3.75), axes.c2p(3, -1.5), color=BLUE) # Extended
        
        # Triangle formed by axes and line
        O = axes.c2p(0, 0)
        tri = Polygon(O, p1, p2, color=ORANGE, fill_opacity=0.2, fill_color=ORANGE)
        
        lbl_2 = MathTex("2").next_to(p1, DOWN)
        lbl_3 = MathTex("3").next_to(p2, LEFT)
        lbl_O = MathTex("O").next_to(O, DOWN+LEFT)
        
        self.add(axes, line, tri)
        self.add(lbl_2, lbl_3, lbl_O)
```

### 🆔 Задача: Cnt92-1012_Prob8_Synthetic - Правоаголен триаголник до правоаголник
**📅 Додадено:** 2025-12-27 02:20
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_Cnt92_1012_Prob8_Synthetic(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Right triangle ABC with hypotenuse AB.
        # C=90.
        C = ORIGIN
        A = UP * 3
        B = RIGHT * 4
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Completed into rectangle ACBD.
        # D = A + B - C = (0,3) + (4,0) - (0,0) = (4,3).
        D = A + B - C
        
        rect_dashed = DashedLine(A, D, color=GRAY)
        rect_dashed2 = DashedLine(B, D, color=GRAY)
        
        # Diagonals AB and CD intersect at M.
        diag_AB = Line(A, B, color=BLUE) # Already part of tri
        diag_CD = Line(C, D, color=GRAY)
        
        M = (A + B) / 2
        dot_M = Dot(M, color=RED)
        
        lbl_A = MathTex("A").next_to(A, UP+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, DOWN+LEFT)
        lbl_D = MathTex("D").next_to(D, UP+RIGHT)
        lbl_M = MathTex("M").next_to(M, UP)
        
        self.add(tri, rect_dashed, rect_dashed2, diag_CD, dot_M)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_M)
```
"""

with open(log_path, "a", encoding="utf-8") as f:
    f.write(new_entries)

print("Successfully appended batch 7 to log.")
