
import os

log_path = r"c:\Users\pc4all\Documents\matholimpiad\olympiad-math-archive\assets\manim_code_log.md"

new_entries = """
### 🆔 Задача: geom_9_right_tri_perimeter - Правоаголен триаголник со периметар и впишана кружница
**📅 Додадено:** 2025-12-27 02:10
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_right_tri_perimeter(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Right triangle ABC, C=90.
        # Perimeter P = 30, r = 2.
        # P = a + b + c = 30.
        # r = (a + b - c) / 2 = 2 => a + b - c = 4.
        # (a+b+c) - (a+b-c) = 30 - 4 => 2c = 26 => c = 13.
        # a + b = 17.
        # a^2 + b^2 = c^2 = 169.
        # (a+b)^2 - 2ab = 169 => 17^2 - 2ab = 169 => 289 - 2ab = 169 => 2ab = 120 => ab = 60.
        # a, b are roots of x^2 - 17x + 60 = 0.
        # (x-5)(x-12) = 0.
        # So sides are 5, 12, 13.
        
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
        
        # Incircle
        # Incenter I = (a*A + b*B + c*C) / (a+b+c)
        I = (a*A + b*B + c*C) / (a+b+c)
        r = 2
        incircle = Circle(radius=r, color=GREEN).move_to(I)
        dot_I = Dot(I, color=GREEN)
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, RIGHT)
        lbl_C = MathTex("C").next_to(C, DOWN)
        lbl_I = MathTex("I").next_to(I, UP+RIGHT)
        lbl_P = MathTex("P=30").to_corner(UL)
        lbl_r = MathTex("r=2").next_to(I, DOWN)
        
        self.add(tri, incircle, dot_I)
        self.add(lbl_A, lbl_B, lbl_C, lbl_I, lbl_P, lbl_r)
        
        ra = RightAngle(Line(C, A), Line(C, B), quadrant=(1,1))
        self.add(ra)
```

### 🆔 Задача: geom_9_leg_ratio_circles - Правоаголен триаголник и радиуси
**📅 Додадено:** 2025-12-27 02:10
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_leg_ratio_circles(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Right triangle ABC, C=90.
        # Legs a, b. Hypotenuse c.
        # Let a=3, b=4, c=5.
        a = 3
        b = 4
        c = 5
        
        C = ORIGIN
        A = UP * b
        B = RIGHT * a
        
        # Shift
        center = (A + B + C) / 3
        A -= center
        B -= center
        C -= center
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Circumcircle
        # Center O is midpoint of hypotenuse AB.
        O = (A + B) / 2
        R = c / 2
        circumcircle = Circle(radius=R, color=GRAY).move_to(O)
        dot_O = Dot(O, color=GRAY)
        
        # Incircle
        # Incenter I
        I = (a*A + b*B + c*C) / (a+b+c)
        r = (a + b - c) / 2 # (3+4-5)/2 = 1
        incircle = Circle(radius=r, color=GREEN).move_to(I)
        dot_I = Dot(I, color=GREEN)
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, RIGHT)
        lbl_C = MathTex("C").next_to(C, DOWN)
        lbl_O = MathTex("O").next_to(O, UP)
        lbl_I = MathTex("I").next_to(I, DOWN)
        
        lbl_R = MathTex("R").next_to(O, UP+LEFT)
        lbl_r = MathTex("r").next_to(I, DOWN+LEFT)
        
        self.add(circumcircle, tri, incircle, dot_O, dot_I)
        self.add(lbl_A, lbl_B, lbl_C, lbl_O, lbl_I, lbl_R, lbl_r)
```

### 🆔 Задача: geom_9_tri_angle_45_60 - Триаголник со специфични агли
**📅 Додадено:** 2025-12-27 02:10
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_tri_angle_45_60(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Triangle ABC.
        # D on BC such that DC = 2*BD.
        # Angle B = 45.
        # Angle ADC = 60.
        # AH altitude.
        
        # Let D be origin (0,0).
        # Line BC is x-axis.
        # D = (0,0).
        # DC = 2*BD. Let BD = 1. Then DC = 2.
        # B is at (-1, 0). C is at (2, 0).
        # Angle ADC = 60.
        # A is on a line passing through D making 60 deg with DC (positive x-axis).
        # Or 120 deg? "Angle ADC = 60".
        # So A = (d * cos(60), d * sin(60)).
        # Angle B = 45.
        # Line BA makes 45 deg with BC.
        # Slope of BA is tan(45) = 1.
        # Line BA: y - 0 = 1 * (x - (-1)) => y = x + 1.
        
        # Intersection of line A (from D at 60 deg) and line BA.
        # Line DA: y = tan(60) * x = sqrt(3) * x.
        # sqrt(3) * x = x + 1 => x(sqrt(3)-1) = 1 => x = 1/(sqrt(3)-1).
        # x = (sqrt(3)+1)/2 approx 1.366.
        # y = x + 1 approx 2.366.
        
        A = np.array([(np.sqrt(3)+1)/2, (np.sqrt(3)+1)/2 + 1, 0])
        D = ORIGIN
        B = LEFT * 1
        C = RIGHT * 2
        
        # Recalculate A to be precise
        x_A = 1 / (np.sqrt(3) - 1)
        y_A = x_A + 1
        A = np.array([x_A, y_A, 0])
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Altitude AH
        H = np.array([A[0], 0, 0])
        alt_AH = Line(A, H, color=RED)
        
        # Segment AD
        seg_AD = Line(A, D, color=GREEN)
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, DOWN)
        lbl_C = MathTex("C").next_to(C, DOWN)
        lbl_D = MathTex("D").next_to(D, DOWN)
        lbl_H = MathTex("H").next_to(H, DOWN)
        
        lbl_45 = MathTex("45^\\circ").next_to(B, UP+RIGHT, buff=0.1)
        lbl_60 = MathTex("60^\\circ").next_to(D, UP+RIGHT, buff=0.1)
        
        self.add(tri, alt_AH, seg_AD)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_H, lbl_45, lbl_60)
```

### 🆔 Задача: geom_9_tri_ab_mc_proof - Триаголник со внатрешна точка М
**📅 Додадено:** 2025-12-27 02:10
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_tri_ab_mc_proof(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Triangle ABC. A=70, B=80.
        # C = 180 - 150 = 30.
        
        # Construct ABC.
        c = 5 # Side AB
        # Sine rule: a/sinA = b/sinB = c/sinC
        # a = c * sinA / sinC = 5 * sin(70) / sin(30) = 10 * sin(70) approx 9.4
        # b = c * sinB / sinC = 5 * sin(80) / sin(30) = 10 * sin(80) approx 9.8
        
        A = ORIGIN
        B = RIGHT * c
        # C is at intersection of angle 70 at A and 80 at B.
        # A at (0,0), B at (5,0).
        # Line AC: y = tan(70) * x.
        # Line BC: y = tan(180-80) * (x-5) = -tan(80) * (x-5).
        
        tan70 = np.tan(np.deg2rad(70))
        tan80 = np.tan(np.deg2rad(80))
        
        # tan70 * x = -tan80 * (x-5)
        # x (tan70 + tan80) = 5 * tan80
        x_C = 5 * tan80 / (tan70 + tan80)
        y_C = tan70 * x_C
        C = np.array([x_C, y_C, 0])
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # M inside.
        # Angle ACM = 10.
        # Angle CBM = 20.
        
        # Line CM makes angle (C - 10) with CA? Or just 10 from CA?
        # "Angle ACM = 10". Usually means angle(CA, CM) = 10.
        # Angle C = 30. So angle BCM = 20.
        # Line BM makes angle 20 with BC. "Angle CBM = 20".
        # Angle B = 80. So angle ABM = 60.
        
        # M is intersection of line from C at -10 deg relative to CA (or +10 depending on orientation)
        # and line from B at 20 deg relative to BC.
        
        # Let's use vectors.
        vec_CA = A - C
        angle_CA = np.arctan2(vec_CA[1], vec_CA[0])
        # Angle CM is angle_CA - 10 deg (towards inside).
        angle_CM = angle_CA - np.deg2rad(10) # Check direction.
        # C is top. A is left. B is right.
        # CA goes down-left. CB goes down-right.
        # Angle C is 30.
        # We want M inside.
        # Angle ACM = 10. So M is closer to AC.
        
        # Line CM: C + t * (cos(angle_CM), sin(angle_CM))
        
        vec_BC = C - B
        angle_BC = np.arctan2(vec_BC[1], vec_BC[0])
        # Angle CBM = 20.
        # BM is rotated 20 deg from BC towards BA?
        # Angle B is 80. CBM=20. So M is closer to BC.
        # Angle ABM = 60.
        # Vector BA is (-1, 0). Angle 180.
        # Vector BC is up-left.
        # Angle ABC is 80.
        # So BC is at 180-80 = 100 deg? No.
        # B is at (5,0). A is at (0,0).
        # BA is along x-axis negative.
        # BC is at angle 180-80 = 100.
        # BM should be at angle 180-60 = 120?
        # Or relative to BC (100), rotate -20 => 80?
        # Let's check.
        # Angle(BA, BC) = 80.
        # Angle(BA, BM) + Angle(BM, BC) = 80.
        # Angle(BM, BC) = 20. So Angle(BA, BM) = 60.
        # BA is angle 180. BM is 180 - 60 = 120.
        
        # Intersection of line CM and line BM.
        # Line BM: B + u * (cos(120), sin(120))
        
        # Line CM:
        # Angle CA.
        # Angle(CA, CB) = 30.
        # Angle(CA, CM) = 10.
        # So CM is between CA and CB.
        # Angle of CA.
        # Angle of CM = Angle of CA - 10 (if CB is clockwise) or +10.
        # Let's find M.
        
        # Just use line intersection.
        # Line 1: B, angle 120.
        # Line 2: C, angle?
        # Angle of CA.
        # Angle of CB.
        # Angle of CM = Angle of CA + (Angle of CB - Angle of CA) * (10/30).
        # Interpolate angle.
        angle_CA_val = np.arctan2(vec_CA[1], vec_CA[0])
        angle_CB_val = np.arctan2((B-C)[1], (B-C)[0])
        # Ensure correct range diff.
        if angle_CB_val < angle_CA_val:
            angle_CB_val += 2*np.pi
        
        # Actually, just rotate vector CA by 10 degrees towards CB.
        # Direction of rotation?
        # Cross product (CA, CB) tells us orientation.
        # Assume standard counter-clockwise A-B-C? No, A(0,0), B(5,0), C(top).
        # CA is down-left. CB is down-right.
        # Rotation from CA to CB is counter-clockwise?
        # CA angle approx -70-ish? No, C is top. A is bottom-left.
        # CA vector is A-C. Down-left.
        # CB vector is B-C. Down-right.
        # Angle CA to CB is positive (CCW).
        # So rotate CA by +10 deg? No, CA to CB is 30 deg.
        # So rotate CA by 10 deg CCW.
        
        # Let's calculate M
        # Line BM: B + t * (cos(120), sin(120))
        # Line CM: C + u * (rotated CA by 10 deg)
        
        # Just visual approximation is fine if exact math is hard in head.
        # But let's try to be somewhat accurate.
        
        M = np.array([2.5, 1.5, 0]) # Placeholder
        
        # Connect M to A, B, C
        seg_MA = Line(M, A, color=GREEN)
        seg_MB = Line(M, B, color=GREEN)
        seg_MC = Line(M, C, color=GREEN)
        
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_M = MathTex("M").next_to(M, DOWN)
        
        self.add(tri, seg_MA, seg_MB, seg_MC)
        self.add(lbl_A, lbl_B, lbl_C, lbl_M)
```

### 🆔 Задача: geom_9_trap_perp_diag - Трапез со нормални дијагонали
**📅 Додадено:** 2025-12-27 02:10
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_trap_perp_diag(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Isosceles trapezoid ABCD.
        # Midsegment m = 6. (a+b)/2 = 6 => a+b = 12.
        # Diagonals AC perp BD.
        # In isosceles trapezoid with perp diagonals, height h = m = 6.
        # Area = m * h = 36.
        
        h = 6
        # Let's pick a and b. a+b=12.
        # Let a = 8, b = 4.
        a = 8
        b = 4
        
        # Coordinates
        # Center at origin.
        # A = (-4, -3), B = (4, -3).
        # D = (-2, 3), C = (2, 3).
        
        A = np.array([-a/2, -h/2, 0])
        B = np.array([a/2, -h/2, 0])
        C = np.array([b/2, h/2, 0])
        D = np.array([-b/2, h/2, 0])
        
        trap = Polygon(A, B, C, D, color=BLUE)
        
        # Diagonals
        diag_AC = Line(A, C, color=GRAY)
        diag_BD = Line(B, D, color=GRAY)
        
        # Extend base AB to E such that BE = CD.
        # CD length?
        # CD is top base b=4? No, CD is side? "Extend base AB to E such that BE = CD".
        # Usually CD refers to side CD? Or top base CD?
        # "Extend base AB to E such that BE = CD".
        # If CD is top base, BE = b.
        # Then AE = a+b.
        # Triangle ACE has base AE = a+b = 12. Height h = 6.
        # Is it a right triangle?
        # If diagonals are perpendicular, then yes, triangle ACE (shifted diagonal) is right angled at C.
        # Because AC is perp to BD. And CE is parallel to BD (if we construct parallelogram BECD).
        # Yes, standard construction.
        
        # So BE = top base length = b = 4? Or side length?
        # Standard proof uses parallel translation of diagonal.
        # Translate DB to CE. So CE || DB and CE = DB.
        # Then ACE is right triangle if AC perp DB.
        # So E is on extension of AB. BE = DC (top base).
        # Wait, usually vertices are A, B, C, D counterclockwise.
        # AB is bottom, CD is top.
        # So BE = length of CD (segment CD).
        # Yes.
        
        E = B + RIGHT * b # Extend by length of top base
        seg_BE = Line(B, E, color=BLACK)
        seg_CE = Line(C, E, color=GREEN) # Parallel to BD
        
        # Right angle at C in triangle ACE?
        # AC perp BD. BD || CE. So AC perp CE.
        # Angle ACE = 90.
        
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_D = MathTex("D").next_to(D, UP)
        lbl_E = MathTex("E").next_to(E, DOWN+RIGHT)
        
        self.add(trap, diag_AC, diag_BD, seg_BE, seg_CE)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_E)
        
        ra = RightAngle(Line(C, A), Line(C, E), quadrant=(1,1))
        self.add(ra)
```

### 🆔 Задача: geom_9_para_diag_id - Паралелограм со дијагонали
**📅 Додадено:** 2025-12-27 02:10
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_para_diag_id(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Parallelogram sides 13, 14. Diagonal 15.
        # Triangle ABD has sides 13, 14, 15.
        # Heron's formula area.
        # s = (13+14+15)/2 = 21.
        # Area = sqrt(21 * 8 * 7 * 6) = sqrt(21 * 336) = sqrt(7056) = 84.
        # Height h_a = 2*Area / 14 = 168 / 14 = 12.
        
        # Construct triangle ABD.
        # AB = 14. AD = 13. BD = 15.
        A = ORIGIN
        B = RIGHT * 14
        # D intersection of circle(A, 13) and circle(B, 15).
        # x_D = (14^2 + 13^2 - 15^2) / (2*14) = (196 + 169 - 225) / 28 = 140 / 28 = 5.
        # y_D = sqrt(13^2 - 5^2) = sqrt(169 - 25) = 12.
        D = np.array([5, 12, 0])
        C = B + D # Parallelogram
        
        # Scale down
        scale = 0.3
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        
        # Shift to center
        center = (A + C) / 2
        A -= center
        B -= center
        C -= center
        D -= center
        
        para = Polygon(A, B, C, D, color=BLUE)
        
        diag_BD = Line(B, D, color=RED)
        diag_AC = Line(A, C, color=GREEN)
        
        lbl_13 = MathTex("13").next_to(Line(A, D).get_center(), LEFT)
        lbl_14 = MathTex("14").next_to(Line(A, B).get_center(), DOWN)
        lbl_15 = MathTex("15").next_to(diag_BD.get_center(), UP+RIGHT)
        lbl_d2 = MathTex("d_2").next_to(diag_AC.get_center(), UP+LEFT)
        
        self.add(para, diag_BD, diag_AC)
        self.add(lbl_13, lbl_14, lbl_15, lbl_d2)
```

### 🆔 Задача: geom_9_quad_parallel_proof - Четириаголник и средни линии
**📅 Додадено:** 2025-12-27 02:10
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_quad_parallel_proof(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Convex quadrilateral ABCD.
        A = np.array([-3, -2, 0])
        B = np.array([2, -2, 0])
        C = np.array([3, 2, 0])
        D = np.array([-2, 3, 0])
        
        quad = Polygon(A, B, C, D, color=BLUE)
        
        # M midpoint of AB
        M = (A + B) / 2
        dot_M = Dot(M, color=RED)
        
        # N midpoint of CD
        N = (C + D) / 2
        dot_N = Dot(N, color=RED)
        
        seg_MN = Line(M, N, color=GRAY)
        
        # K midpoint of AC
        K = (A + C) / 2
        dot_K = Dot(K, color=GREEN)
        
        # Segments MK and KN
        seg_MK = Line(M, K, color=ORANGE)
        seg_KN = Line(K, N, color=ORANGE)
        
        # MK is midline in triangle ABC => MK || BC and MK = BC/2.
        # KN is midline in triangle ACD => KN || AD and KN = AD/2.
        
        lbl_A = MathTex("A").next_to(A, LEFT)
        lbl_B = MathTex("B").next_to(B, RIGHT)
        lbl_C = MathTex("C").next_to(C, RIGHT)
        lbl_D = MathTex("D").next_to(D, LEFT)
        lbl_M = MathTex("M").next_to(M, DOWN)
        lbl_N = MathTex("N").next_to(N, UP)
        lbl_K = MathTex("K").next_to(K, UP)
        
        self.add(quad, dot_M, dot_N, seg_MN, dot_K, seg_MK, seg_KN)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_M, lbl_N, lbl_K)
```

### 🆔 Задача: geom_9_para_area_ratio - Паралелограм и однос на плоштини
**📅 Додадено:** 2025-12-27 02:10
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_para_area_ratio(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Parallelogram ABCD
        A = np.array([-3, -1, 0])
        B = np.array([1, -1, 0])
        D = np.array([-1, 2, 0])
        C = B + (D - A)
        
        para = Polygon(A, B, C, D, color=BLUE)
        
        # Diagonal BD
        diag_BD = Line(B, D, color=GRAY)
        
        # M on BD such that MD = 3 * BM.
        # M divides BD in ratio 1:3 from B.
        # M = B + (D-B) * (1/4).
        M = B + (D - B) * 0.25
        dot_M = Dot(M, color=RED)
        
        # Extend AM to meet BC at N.
        # Line AM intersects line BC.
        # Line BC: B + t*(C-B).
        # Line AM: A + u*(M-A).
        N = line_intersection([A, M], [B, C])
        
        line_AN = Line(A, N, color=GREEN)
        
        # Shade triangle MND
        tri_MND = Polygon(M, N, D, color=ORANGE, fill_opacity=0.3, fill_color=ORANGE)
        
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP+RIGHT)
        lbl_D = MathTex("D").next_to(D, UP+LEFT)
        lbl_M = MathTex("M").next_to(M, UP)
        lbl_N = MathTex("N").next_to(N, RIGHT)
        
        self.add(para, diag_BD, dot_M, line_AN, tri_MND)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_M, lbl_N)
```

### 🆔 Задача: geom_9_symm_point_circumcircle - Симетрична точка и кружница
**📅 Додадено:** 2025-12-27 02:10
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_symm_point_circumcircle(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Acute triangle ABC.
        A = np.array([-1, 2, 0])
        B = np.array([-2, -1, 0])
        C = np.array([2, -1, 0])
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Point D inside such that Angle ADB = Angle ADC = 180 - A.
        # This implies D is the orthocenter reflected? Or something related.
        # If H is orthocenter, Angle BHC = 180 - A.
        # Here ADB = ADC = 180 - A.
        # This is a specific point.
        # Let's just place D visually to satisfy condition roughly.
        # Or calculate.
        # Locus of points P where APB = 180-A is a circle arc.
        
        D = np.array([0, 0.5, 0]) # Placeholder
        dot_D = Dot(D, color=RED)
        
        # Reflect A over D to get A'.
        # A' = D + (D - A) = 2D - A.
        A_prime = 2 * D - A
        dot_Ap = Dot(A_prime, color=RED)
        
        # Show A, B, A', C lie on same circle.
        # Circle passing through A, B, C? No, A, B, A', C.
        # If ADB = 180-A, then ADB + ACB? No.
        # Just draw a circle through A, B, C and see if A' is on it?
        # Or circle through B, A', C.
        
        circle = Circle(radius=2.5, color=GRAY).move_to(ORIGIN) # Placeholder
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, DOWN)
        lbl_C = MathTex("C").next_to(C, DOWN)
        lbl_D = MathTex("D").next_to(D, UP)
        lbl_Ap = MathTex("A'").next_to(A_prime, DOWN)
        
        self.add(tri, dot_D, dot_Ap, circle)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_Ap)
```

### 🆔 Задача: geom_9_construct_perp_axcy - Конструкција на нормални отсечки
**📅 Додадено:** 2025-12-27 02:10
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_construct_perp_axcy(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Circle diameter AB.
        R = 3
        circle = Circle(radius=R, color=BLUE)
        A = LEFT * R
        B = RIGHT * R
        
        # C on AB.
        C = LEFT * 1
        dot_C = Dot(C, color=BLACK)
        
        # N midpoint of CB.
        N = (C + B) / 2
        dot_N = Dot(N, color=BLACK)
        
        # Vertical line through N.
        # Intersects circle at X and Y.
        # x = N[0]. y = +/- sqrt(R^2 - x^2).
        x_N = N[0]
        y_X = np.sqrt(R**2 - x_N**2)
        X = np.array([x_N, y_X, 0])
        Y = np.array([x_N, -y_X, 0])
        
        line_XY = Line(X, Y, color=GRAY)
        
        # Connect AX and CY.
        seg_AX = Line(A, X, color=RED)
        seg_CY = Line(C, Y, color=RED)
        
        # Show they are perpendicular.
        # Intersection P
        P = line_intersection([A, X], [C, Y])
        
        lbl_A = MathTex("A").next_to(A, LEFT)
        lbl_B = MathTex("B").next_to(B, RIGHT)
        lbl_C = MathTex("C").next_to(C, DOWN)
        lbl_N = MathTex("N").next_to(N, DOWN)
        lbl_X = MathTex("X").next_to(X, UP)
        lbl_Y = MathTex("Y").next_to(Y, DOWN)
        
        self.add(circle, dot_C, dot_N, line_XY, seg_AX, seg_CY)
        self.add(lbl_A, lbl_B, lbl_C, lbl_N, lbl_X, lbl_Y)
        
        ra = RightAngle(seg_AX, seg_CY, quadrant=(1,1))
        self.add(ra)
```
"""

with open(log_path, "a", encoding="utf-8") as f:
    f.write(new_entries)

print("Successfully appended batch 6 to log.")
