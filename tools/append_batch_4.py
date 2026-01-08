
import os

log_path = r"c:\Userrs\pc4all\Documents\matholimpiad\olympiad-math-archive\assets\manim_code_log.md"

new_entries = """
### 🆔 Задача: geom_angle_alt_bisector_03 - Агол меѓу висина и симетрала
**📅 Додадено:** 2025-12-27 01:50
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_angle_alt_bisector_03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Triangle ABC, AC > AB.
        # Let A = (0, 3), B = (-1, 0), C = (4, 0)
        A = UP * 3
        B = LEFT * 1
        C = RIGHT * 4
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Altitude AD
        D = np.array([A[0], B[1], 0])
        alt_AD = Line(A, D, color=RED)
        
        # Angle bisector AS
        # S on BC.
        # BS / SC = AB / AC
        len_AB = np.linalg.norm(B - A)
        len_AC = np.linalg.norm(C - A)
        ratio = len_AB / (len_AB + len_AC)
        S = B + (C - B) * ratio
        bisector_AS = Line(A, S, color=GREEN)
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, DOWN+LEFT)
        lbl_C = MathTex("C").next_to(C, DOWN+RIGHT)
        lbl_D = MathTex("D").next_to(D, DOWN)
        lbl_S = MathTex("S").next_to(S, DOWN)
        
        lbl_beta = MathTex(r"\\beta").next_to(B, UP+RIGHT, buff=0.5)
        lbl_gamma = MathTex(r"\\gamma").next_to(C, UP+LEFT, buff=0.5)
        
        self.add(tri, alt_AD, bisector_AS)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_S, lbl_beta, lbl_gamma)
        
        # Right angle at D
        ra = RightAngle(Line(D, A), Line(D, C), quadrant=(1,1))
        self.add(ra)
```

### 🆔 Задача: geom_angle_hybrid_04 - Агол меѓу внатрешна и надворешна симетрала
**📅 Додадено:** 2025-12-27 01:50
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_angle_hybrid_04(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        A = np.array([-1, 2, 0])
        B = np.array([-2, -1, 0])
        C = np.array([3, -1, 0])
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Extend CB beyond B
        ext_pt = B + (B - C) * 0.5
        line_ext = Line(B, ext_pt, color=GRAY)
        
        # Internal bisector of A
        # I_A on BC
        len_AB = np.linalg.norm(B - A)
        len_AC = np.linalg.norm(C - A)
        ratio = len_AB / (len_AB + len_AC)
        I_A = B + (C - B) * ratio
        bisector_A = Line(A, I_A, color=GREEN)
        # Extend it further to meet external bisector
        
        # External bisector of B
        # Angle at B is ABC. External angle is 180 - ABC.
        # Bisector direction?
        # Vector BA
        vec_BA = A - B
        vec_BC = C - B
        vec_B_ext = ext_pt - B
        
        # Angle of BA
        ang_BA = np.arctan2(vec_BA[1], vec_BA[0])
        # Angle of B_ext (180 from BC)
        ang_B_ext = np.arctan2(vec_B_ext[1], vec_B_ext[0])
        
        # Bisector angle
        # Need to be careful with ranges.
        # Let's just find a point on it.
        # Unit vectors
        u_BA = vec_BA / np.linalg.norm(vec_BA)
        u_B_ext = vec_B_ext / np.linalg.norm(vec_B_ext)
        bisect_vec = u_BA + u_B_ext
        
        # Intersection Y
        # Line A -> I_A (direction A to I_A)
        # Line B -> B + bisect_vec
        
        Y = line_intersection(
            [A, I_A],
            [B, B + bisect_vec]
        )
        
        bisector_A_ext = Line(A, Y, color=GREEN)
        bisector_B_ext = Line(B, Y, color=ORANGE)
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, DOWN)
        lbl_C = MathTex("C").next_to(C, DOWN)
        lbl_Y = MathTex("Y").next_to(Y, DOWN)
        
        self.add(tri, line_ext, bisector_A_ext, bisector_B_ext)
        self.add(lbl_A, lbl_B, lbl_C, lbl_Y)
```

### 🆔 Задача: geom_angle_overlap_05 - Агол на преклопување на хипотенуза
**📅 Додадено:** 2025-12-27 01:50
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_angle_overlap_05(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Right triangle ABC at A
        # A = (0,0), B = (0, 3), C = (4, 0)
        A = ORIGIN
        B = UP * 3
        C = RIGHT * 4
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # E on BC such that BE = AB = 3
        len_BC = 5
        len_AB = 3
        vec_BC = C - B
        unit_BC = vec_BC / len_BC
        E = B + unit_BC * len_AB
        dot_E = Dot(E, color=RED)
        
        # D on BC such that CD = AC = 4
        len_AC = 4
        vec_CB = B - C
        unit_CB = vec_CB / len_BC
        D = C + unit_CB * len_AC
        dot_D = Dot(D, color=RED)
        
        # Connect AD and AE
        seg_AD = Line(A, D, color=GREEN)
        seg_AE = Line(A, E, color=GREEN)
        
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, UP)
        lbl_C = MathTex("C").next_to(C, RIGHT)
        lbl_D = MathTex("D").next_to(D, UP)
        lbl_E = MathTex("E").next_to(E, UP)
        
        self.add(tri, dot_E, dot_D, seg_AD, seg_AE)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_E)
        
        ra = RightAngle(Line(A, B), Line(A, C), quadrant=(1,1))
        self.add(ra)
```

### 🆔 Задача: para_normals_sum_06 - Збир на нормали во паралелограм
**📅 Додадено:** 2025-12-27 01:50
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_para_normals_sum_06(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Same as geom_8_2018_para_line basically
        # Line p
        p_start = np.array([-4, -2, 0])
        p_end = np.array([4, -1, 0])
        line_p = Line(p_start, p_end, color=BLACK)
        
        # Parallelogram ABCD, D on p
        D = (p_start + p_end) / 2
        A = D + np.array([-1, 2, 0])
        C = D + np.array([3, 1, 0])
        B = A + (C - D)
        
        para = Polygon(A, B, C, D, color=BLUE)
        
        # Diagonals intersection S
        S = (A + C) / 2
        diag_AC = DashedLine(A, C, color=GRAY)
        diag_BD = DashedLine(B, D, color=GRAY)
        
        # Perpendiculars
        vec_p = p_end - p_start
        unit_p = vec_p / np.linalg.norm(vec_p)
        
        def get_proj(Pt):
            return p_start + np.dot(Pt - p_start, unit_p) * unit_p
            
        M = get_proj(A)
        N = get_proj(B)
        O = get_proj(C)
        S_prime = get_proj(S)
        
        perp_A = DashedLine(A, M, color=RED)
        perp_B = DashedLine(B, N, color=RED)
        perp_C = DashedLine(C, O, color=RED)
        perp_S = Line(S, S_prime, color=GREEN)
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, UP)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_D = MathTex("D").next_to(D, DOWN)
        lbl_S = MathTex("S").next_to(S, UP)
        
        self.add(line_p, para, diag_AC, diag_BD)
        self.add(perp_A, perp_B, perp_C, perp_S)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_S)
```

### 🆔 Задача: para_diag_centroid_07 - Пресек на линии во паралелограм
**📅 Додадено:** 2025-12-27 01:50
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_para_diag_centroid_07(Scene):
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
        
        M = (B + C) / 2
        N = (C + D) / 2
        
        seg_DM = Line(D, M, color=RED)
        seg_BN = Line(B, N, color=RED)
        
        # Intersection T
        T = line_intersection([D, M], [B, N])
        dot_T = Dot(T, color=BLACK)
        
        diag_AC = Line(A, C, color=GREEN)
        diag_BD = DashedLine(B, D, color=GRAY)
        
        O = (A + C) / 2
        dot_O = Dot(O, color=BLACK)
        
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP+RIGHT)
        lbl_D = MathTex("D").next_to(D, UP+LEFT)
        lbl_M = MathTex("M").next_to(M, RIGHT)
        lbl_N = MathTex("N").next_to(N, UP)
        lbl_T = MathTex("T").next_to(T, DOWN)
        lbl_O = MathTex("O").next_to(O, UP)
        
        self.add(para, seg_DM, seg_BN, diag_AC, diag_BD)
        self.add(dot_T, dot_O)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_M, lbl_N, lbl_T, lbl_O)
```

### 🆔 Задача: viviani_theorem_08 - Теорема на Вивиани
**📅 Додадено:** 2025-12-27 01:50
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_viviani_theorem_08(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Equilateral Triangle ABC
        side = 6
        h_tri = side * np.sqrt(3) / 2
        A = np.array([-side/2, -h_tri/3, 0])
        B = np.array([side/2, -h_tri/3, 0])
        C = np.array([0, 2*h_tri/3, 0])
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Point S inside
        S = np.array([0.2, 0.2, 0])
        dot_S = Dot(S, color=BLACK)
        
        # Perpendiculars
        def get_perp(P, P1, P2):
            vec = P2 - P1
            unit = vec / np.linalg.norm(vec)
            proj = P1 + np.dot(P - P1, unit) * unit
            return Line(P, proj, color=RED)
            
        perp_a = get_perp(S, B, C)
        perp_b = get_perp(S, C, A)
        perp_c = get_perp(S, A, B)
        
        # Connect S to vertices
        seg_SA = DashedLine(S, A, color=GRAY)
        seg_SB = DashedLine(S, B, color=GRAY)
        seg_SC = DashedLine(S, C, color=GRAY)
        
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_S = MathTex("S").next_to(S, UP)
        
        self.add(tri, dot_S)
        self.add(perp_a, perp_b, perp_c)
        self.add(seg_SA, seg_SB, seg_SC)
        self.add(lbl_A, lbl_B, lbl_C, lbl_S)
```

### 🆔 Задача: right_tri_angles_10 - Агли во правоаголен триаголник
**📅 Додадено:** 2025-12-27 01:50
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_right_tri_angles_10(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Right triangle ABC, C=90
        C = ORIGIN
        A = UP * 4
        B = RIGHT * 6
        
        # Shift
        center = (A + B + C) / 3
        A -= center
        B -= center
        C -= center
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Altitude CD
        vec_AB = B - A
        unit_AB = vec_AB / np.linalg.norm(vec_AB)
        D = A + np.dot(C - A, unit_AB) * unit_AB
        alt_CD = Line(C, D, color=RED)
        
        # E on AD such that DE = BD = q
        len_BD = np.linalg.norm(B - D)
        vec_DA = A - D
        unit_DA = vec_DA / np.linalg.norm(vec_DA)
        E = D + unit_DA * len_BD
        dot_E = Dot(E, color=GREEN)
        
        # Highlight triangles
        tri_CBE = Polygon(C, B, E, color=GREEN, fill_opacity=0.1, fill_color=GREEN)
        tri_AEC = Polygon(A, E, C, color=ORANGE, fill_opacity=0.1, fill_color=ORANGE)
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, RIGHT)
        lbl_C = MathTex("C").next_to(C, DOWN)
        lbl_D = MathTex("D").next_to(D, DOWN)
        lbl_E = MathTex("E").next_to(E, UP)
        
        self.add(tri, alt_CD, dot_E)
        self.add(tri_CBE, tri_AEC)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_E)
```

### 🆔 Задача: geom_quad_symmetry_05 - Симетрија во конвексен четириаголник
**📅 Додадено:** 2025-12-27 01:50
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_quad_symmetry_05(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Quadrilateral ABCD, C=90
        # C at origin
        C = ORIGIN
        # D on x-axis, B on y-axis? No, just C=90.
        # Let's put C at (0,0), D at (3,0), B at (0,2).
        # A can be anywhere.
        D = RIGHT * 3
        B = UP * 2
        A = np.array([-1, 3, 0])
        
        # Shift
        center = (A + B + C + D) / 4
        A -= center
        B -= center
        C -= center
        D -= center
        
        quad = Polygon(A, B, C, D, color=BLUE)
        
        # P on CD
        P = (C + D) * 0.6 # Random point on CD
        dot_P = Dot(P, color=RED)
        
        # Reflect B across CD
        # CD is line through C and D.
        # Project B onto CD
        vec_CD = D - C
        unit_CD = vec_CD / np.linalg.norm(vec_CD)
        proj_B = C + np.dot(B - C, unit_CD) * unit_CD
        vec_perp = B - proj_B
        B_prime = proj_B - vec_perp
        dot_B_prime = Dot(B_prime, color=GRAY)
        
        # Connect A, P, B' - straight line?
        # Prompt says "Connect A, P, and B' as a straight line."
        # This implies P is chosen such that A-P-B' is straight.
        # So P is intersection of AB' and CD.
        P = line_intersection([A, B_prime], [C, D])
        dot_P.move_to(P)
        
        line_APB_prime = DashedLine(A, B_prime, color=GREEN)
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, UP)
        lbl_C = MathTex("C").next_to(C, DOWN)
        lbl_D = MathTex("D").next_to(D, DOWN)
        lbl_P = MathTex("P").next_to(P, DOWN)
        lbl_B_prime = MathTex("B'").next_to(B_prime, DOWN)
        
        self.add(quad, dot_P, dot_B_prime, line_APB_prime)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_P, lbl_B_prime)
        
        ra = RightAngle(Line(C, B), Line(C, D), quadrant=(1,1))
        self.add(ra)
```

### 🆔 Задача: geom_tri_bisector_diff_11 - Триаголник со разлика на агли од 90 степени
**📅 Додадено:** 2025-12-27 01:50
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_tri_bisector_diff_11(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Triangle ABC, A > B.
        A = np.array([-1, 2, 0])
        B = np.array([-3, -1, 0])
        C = np.array([2, -1, 0])
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Internal bisector CD
        # D on AB
        len_AC = np.linalg.norm(C - A)
        len_BC = np.linalg.norm(C - B)
        ratio = len_AC / (len_AC + len_BC)
        D = A + (B - A) * ratio
        bisector_CD = Line(C, D, color=GREEN)
        
        # External bisector CE
        # Perpendicular to CD at C
        # Line through C perpendicular to CD
        # Intersects AB extended at E
        
        # Vector CD
        vec_CD = D - C
        # Perpendicular vector
        perp_vec = np.array([-vec_CD[1], vec_CD[0], 0])
        
        # Intersection of line(C, perp) and line(A, B)
        E = line_intersection(
            [C, C + perp_vec],
            [A, B]
        )
        
        bisector_CE = Line(C, E, color=ORANGE)
        line_AE = Line(A, E, color=GRAY) # Extension of AB
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, DOWN)
        lbl_C = MathTex("C").next_to(C, DOWN)
        lbl_D = MathTex("D").next_to(D, LEFT)
        lbl_E = MathTex("E").next_to(E, UP)
        
        self.add(tri, bisector_CD, bisector_CE, line_AE)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_E)
        
        ra = RightAngle(bisector_CD, bisector_CE, quadrant=(1,1))
        self.add(ra)
```
"""

with open(log_path, "a", encoding="utf-8") as f:
    f.write(new_entries)

print("Successfully appended batch 4 to log.")
