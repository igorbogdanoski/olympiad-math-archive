
import os

log_path = r"c:\Userrs\pc4all\Documents\matholimpiad\olympiad-math-archive\assets\manim_code_log.md"

new_entries = """
### 🆔 Задача: tri_altitudes_perimeter_09 - Периметар преку однос на висини
**📅 Додадено:** 2025-12-27 02:00
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_tri_altitudes_perimeter_09(Scene):
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
        
        # Altitudes
        def get_alt(P, P1, P2):
            vec = P2 - P1
            unit = vec / np.linalg.norm(vec)
            proj = P1 + np.dot(P - P1, unit) * unit
            return Line(P, proj, color=RED)
            
        h_a = get_alt(A, B, C)
        h_b = get_alt(B, C, A)
        h_c = get_alt(C, A, B)
        
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP)
        
        lbl_ha = MathTex("h_a").next_to(h_a.get_center(), LEFT, buff=0.1)
        lbl_hb = MathTex("h_b").next_to(h_b.get_center(), UP, buff=0.1)
        lbl_hc = MathTex("h_c").next_to(h_c.get_center(), RIGHT, buff=0.1)
        
        self.add(tri, h_a, h_b, h_c)
        self.add(lbl_A, lbl_B, lbl_C, lbl_ha, lbl_hb, lbl_hc)
```

### 🆔 Задача: geom_right_tri_bisect_09 - Правоаголен триаголник со висина, тежишна и симетрала
**📅 Додадено:** 2025-12-27 02:00
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_right_tri_bisect_09(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Right triangle ABC, C=90
        # A = 40 deg.
        # Let C = (0,0).
        # CA along y-axis, CB along x-axis? No, usually C is top or bottom.
        # Let's put C at origin.
        C = ORIGIN
        # A at (0, 4)
        # B at (x, 0). Angle A = 40.
        # In triangle ABC, angle B = 90 - 40 = 50.
        # Wait, if C=90, A=40, B=50.
        # Let's rotate so hypotenuse AB is horizontal for better view of CD, CM, CL.
        
        # Or just standard position.
        # C = (0,0)
        # A = (0, 3)
        # B = (3 * tan(40), 0) ? No.
        # tan(A) = a/b = BC/AC.
        # tan(40) approx 0.839
        # Let AC = 4. BC = 4 * 0.839 = 3.356
        
        AC = 4
        BC = AC * np.tan(np.deg2rad(40))
        
        C = ORIGIN
        A = UP * AC
        B = RIGHT * BC
        
        # Shift to center
        center = (A + B + C) / 3
        A -= center
        B -= center
        C -= center
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Altitude CD to AB
        vec_AB = B - A
        unit_AB = vec_AB / np.linalg.norm(vec_AB)
        D = A + np.dot(C - A, unit_AB) * unit_AB
        alt_CD = Line(C, D, color=RED)
        
        # Median CM to AB
        M = (A + B) / 2
        med_CM = Line(C, M, color=GREEN)
        
        # Angle bisector CL to AB
        # L divides AB in ratio AC/BC
        len_AC = np.linalg.norm(C - A)
        len_BC = np.linalg.norm(C - B)
        ratio = len_AC / (len_AC + len_BC)
        L = A + (B - A) * ratio
        bis_CL = Line(C, L, color=ORANGE)
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, RIGHT)
        lbl_C = MathTex("C").next_to(C, DOWN)
        lbl_D = MathTex("D").next_to(D, UP)
        lbl_M = MathTex("M").next_to(M, UP)
        lbl_L = MathTex("L").next_to(L, UP)
        
        lbl_40 = MathTex(r"40^\\circ").next_to(A, DOWN+RIGHT, buff=0.5)
        
        self.add(tri, alt_CD, med_CM, bis_CL)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_M, lbl_L, lbl_40)
        
        ra = RightAngle(Line(C, A), Line(C, B), quadrant=(1,1))
        self.add(ra)
```

### 🆔 Задача: geom_iso_bisector_intersect_10 - Ранокрак триаголник со пресек на висина и симетрала
**📅 Додадено:** 2025-12-27 02:00
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_iso_bisector_intersect_10(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Isosceles ABC, AC=BC.
        # Wait, prompt says "AB as base". So AC=BC.
        # Altitude CD from C.
        # Angle bisector AE from A.
        # Intersection I.
        # Angle AIC = 130 (obtuse).
        
        # Let angle A = alpha. Angle C = gamma.
        # In triangle AIC:
        # Angle IAC = alpha/2.
        # Angle ICA = gamma/2.
        # Angle AIC = 180 - (alpha/2 + gamma/2).
        # 130 = 180 - (alpha+gamma)/2 => (alpha+gamma)/2 = 50 => alpha+gamma = 100.
        # Also 2*alpha + gamma = 180.
        # gamma = 100 - alpha.
        # 2*alpha + 100 - alpha = 180 => alpha = 80.
        # gamma = 20.
        
        # Construct with these angles.
        base_width = 4
        # alpha = 80 deg.
        # height = (base/2) * tan(80)
        h = (base_width / 2) * np.tan(np.deg2rad(80))
        
        A = np.array([-base_width/2, -1, 0])
        B = np.array([base_width/2, -1, 0])
        C = np.array([0, -1 + h, 0])
        
        # Scale down if too big
        if h > 6:
            scale = 5/h
            A *= scale
            B *= scale
            C *= scale
            
        tri = Polygon(A, B, C, color=BLUE)
        
        # Altitude CD
        D = (A + B) / 2
        alt_CD = Line(C, D, color=RED)
        
        # Bisector AE
        # E on BC
        len_AB = np.linalg.norm(B - A)
        len_AC = np.linalg.norm(C - A)
        ratio = len_AB / (len_AB + len_AC) # Bisector theorem on triangle ABC? No, bisector of A.
        # Ratio BE/EC = AB/AC.
        # E = B + (C-B) * (AB / (AB+AC)) ? No.
        # Vector BC. E divides BC in ratio c/b.
        # E = (b*B + c*C) / (b+c) ? No.
        # E = (AC*B + AB*C) / (AC+AB)
        E = (len_AC * B + len_AB * C) / (len_AC + len_AB)
        bis_AE = Line(A, E, color=GREEN)
        
        # Intersection I
        I = line_intersection([C, D], [A, E])
        dot_I = Dot(I, color=BLACK)
        
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_D = MathTex("D").next_to(D, DOWN)
        lbl_E = MathTex("E").next_to(E, RIGHT)
        lbl_I = MathTex("I").next_to(I, LEFT)
        lbl_130 = MathTex(r"130^\\circ").next_to(I, UP+RIGHT, buff=0.1)
        
        self.add(tri, alt_CD, bis_AE, dot_I)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_E, lbl_I, lbl_130)
```

### 🆔 Задача: geom_iso_side_bisector_08 - Ранокрак триаголник со симетрала на страна и агол
**📅 Додадено:** 2025-12-27 02:00
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_iso_side_bisector_08(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Isosceles AC = BC.
        # Perpendicular bisector of AC.
        # Angle bisector of A.
        # Intersection D on BC.
        
        # Let's calculate angles.
        # D is on BC.
        # D is on perp bisector of AC => DA = DC.
        # So triangle ADC is isosceles. Angle DAC = Angle DCA = gamma.
        # AD is angle bisector of A => Angle DAB = Angle DAC = gamma.
        # So Angle A = 2*gamma.
        # Since AC=BC, Angle B = Angle A = 2*gamma.
        # Sum: A + B + C = 180 => 2g + 2g + g = 5g = 180 => g = 36.
        
        # Construct triangle with gamma = 36.
        # Base angle = 72.
        base_width = 4
        h = (base_width / 2) * np.tan(np.deg2rad(72))
        
        A = np.array([-base_width/2, -2, 0])
        B = np.array([base_width/2, -2, 0])
        C = np.array([0, -2 + h, 0])
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Perp bisector of AC
        mid_AC = (A + C) / 2
        vec_AC = C - A
        perp_vec = np.array([-vec_AC[1], vec_AC[0], 0])
        # Line through mid_AC with direction perp_vec
        # Intersects BC at D.
        
        # Line BC: B + t*(C-B)
        # Line perp: mid_AC + u*perp_vec
        D = line_intersection(
            [mid_AC, mid_AC + perp_vec],
            [B, C]
        )
        
        perp_bisector = Line(mid_AC + perp_vec*2, mid_AC - perp_vec*2, color=RED) # Make it long enough
        # Trim to D?
        perp_bisector = Line(mid_AC, D, color=RED) # Or extend a bit
        
        # Angle bisector of A
        # Should go through D
        bis_A = Line(A, D, color=GREEN)
        
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_D = MathTex("D").next_to(D, RIGHT)
        lbl_gamma = MathTex(r"\\gamma").next_to(C, DOWN, buff=0.3)
        
        self.add(tri, perp_bisector, bis_A)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_gamma)
        
        # Mark right angle at mid_AC
        ra = RightAngle(Line(mid_AC, A), Line(mid_AC, D), quadrant=(1,1))
        self.add(ra)
```

### 🆔 Задача: geom_9_midpoint_tangent - Кружница тангентна на краци на агол
**📅 Додадено:** 2025-12-27 02:00
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_midpoint_tangent(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Angle O.
        O = np.array([-3, -2, 0])
        # Arms OA, OB.
        # Circle k tangent to OA at A and OB at B.
        # This means O is external point, OA=OB tangents.
        # Center K of circle lies on bisector of O.
        
        radius = 2
        dist_O_K = 4
        # Angle bisector along x-axis for simplicity, then rotate?
        # Or just place K at (-3+4, -2) = (1, -2).
        K = np.array([1, -2, 0])
        circle = Circle(radius=radius, color=BLUE).move_to(K)
        
        # Tangent points A, B
        # Tangent from O to circle.
        # Angle K-O-A = asin(r/d) = asin(2/4) = 30 deg.
        # So angle AOB = 60 deg.
        
        # Rotate vector OK by 30 and -30 to get directions OA and OB.
        vec_OK = K - O
        angle_OK = 0 # Horizontal
        
        angle_OA = np.deg2rad(30)
        angle_OB = np.deg2rad(-30)
        
        len_OA = np.sqrt(dist_O_K**2 - radius**2) # sqrt(16-4) = sqrt(12) approx 3.46
        
        A = O + np.array([np.cos(angle_OA), np.sin(angle_OA), 0]) * len_OA
        B = O + np.array([np.cos(angle_OB), np.sin(angle_OB), 0]) * len_OA
        
        line_OA = Line(O, A, color=BLACK) # Extend?
        line_OB = Line(O, B, color=BLACK)
        
        # Line BC parallel to OA.
        # C on circle? Or just line?
        # "Draw line BC parallel to OA."
        # Usually implies C is intersection with something or just a direction.
        # "Draw segment OC intersecting circle at D."
        # So C is a point. Where is C?
        # Maybe C is on the circle? Or C is on the line parallel to OA through B?
        # Let's assume C is on the circle? Or C is just a point on the parallel line.
        # "Draw segment OC intersecting circle at D."
        # If C is far away, OC intersects circle.
        # Let's pick C on the parallel line such that OC intersects circle.
        
        vec_OA = A - O
        unit_OA = vec_OA / np.linalg.norm(vec_OA)
        # Line through B parallel to OA: B + t * unit_OA
        # Let's pick a C.
        C = B + unit_OA * 4 # Arbitrary C
        line_BC = Line(B, C, color=GREEN)
        
        # Segment OC
        seg_OC = Line(O, C, color=ORANGE)
        
        # Intersect OC with circle at D.
        # Line OC: O + u * (C-O)
        # Circle: |P-K| = r
        # Find intersection.
        # Or just visual approximation if hard to calc.
        # Let's calc.
        vec_OC = C - O
        unit_OC = vec_OC / np.linalg.norm(vec_OC)
        # P = O + t * unit_OC
        # |O + t*u - K| = r
        # |(O-K) + t*u| = r
        # Let V = O-K. |V + t*u|^2 = r^2
        # (V+tu).(V+tu) = r^2
        # V.V + 2t(V.u) + t^2 = r^2
        # t^2 + 2(V.u)t + (V.V - r^2) = 0
        V = O - K
        a_eq = 1
        b_eq = 2 * np.dot(V, unit_OC)
        c_eq = np.dot(V, V) - radius**2
        
        delta = b_eq**2 - 4*a_eq*c_eq
        t1 = (-b_eq - np.sqrt(delta)) / 2
        t2 = (-b_eq + np.sqrt(delta)) / 2
        # We want the one closer to O? Or further?
        # D is usually the first intersection.
        # Since O is outside, there are two.
        # Let's take the smaller positive t.
        # Wait, O is outside. t1, t2 should be positive if direction is towards circle.
        t = min(t1, t2) if t1 > 0 else max(t1, t2)
        D = O + unit_OC * t
        dot_D = Dot(D, color=RED)
        
        # Line BD intersecting OA at S.
        line_BD_full = Line(B, D, color=GRAY).scale(2) # Extend
        # Intersection S of line(B,D) and line(O,A)
        S = line_intersection([B, D], [O, A])
        dot_S = Dot(S, color=RED)
        seg_BS = Line(B, S, color=GRAY)
        
        lbl_O = MathTex("O").next_to(O, LEFT)
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, DOWN)
        lbl_C = MathTex("C").next_to(C, RIGHT)
        lbl_D = MathTex("D").next_to(D, UP)
        lbl_S = MathTex("S").next_to(S, UP)
        
        self.add(circle, line_OA, line_OB, line_BC, seg_OC, dot_D, seg_BS, dot_S)
        self.add(lbl_O, lbl_A, lbl_B, lbl_C, lbl_D, lbl_S)
```

### 🆔 Задача: geom_9_pentagon_incenter - Конвексен петаголник и тангентни отсечки
**📅 Додадено:** 2025-12-27 02:00
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_pentagon_incenter(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Convex pentagon ABCDE circumscribed about a circle?
        # Prompt: "Mark potential tangent points K, L, M, N, P... Label tangent segments x, y, z, u, v"
        # This implies it IS circumscribed (tangential pentagon).
        
        circle = Circle(radius=2, color=GRAY)
        center = ORIGIN
        
        # Generate 5 points on circle for tangency
        angles = np.linspace(0, 2*np.pi, 6)[:-1] + 0.2 # Shift a bit
        tangent_points = []
        for ang in angles:
            tangent_points.append(np.array([2*np.cos(ang), 2*np.sin(ang), 0]))
            
        # Tangent lines at these points
        # Intersection of adjacent tangent lines gives vertices.
        vertices = []
        for i in range(5):
            p1 = tangent_points[i]
            p2 = tangent_points[(i+1)%5]
            
            # Tangent at p1: normal is p1. Line: p1 + t * rot(p1)
            # Tangent at p2: normal is p2.
            
            # Intersection formula
            # Or simpler: vertex is intersection of tangent at p1 and tangent at p2?
            # No, vertices are between tangent points.
            # Tangent points are ON the sides.
            # So side AB touches at K. Side BC touches at L.
            # So we need tangent lines at K, L, M, N, P.
            # Vertices are intersections of these lines.
            pass
            
        # Let's compute vertices
        def get_tangent_line(P):
            # Normal is P (since center is origin)
            # Line equation: P.x * x + P.y * y = r^2
            return P
            
        # Intersection of tangent at P1 and P2
        # x*x1 + y*y1 = r^2
        # x*x2 + y*y2 = r^2
        # Solve linear system.
        verts = []
        r_sq = 4
        for i in range(5):
            p1 = tangent_points[i]
            p2 = tangent_points[(i+1)%5] # Wait, points are K, L, M...
            # Vertex A is between P_i and P_{i+1}? No.
            # Side 1 touches at P1. Side 2 touches at P2.
            # Vertex is intersection of Side 1 and Side 2.
            
            # Solve:
            # x*p1x + y*p1y = r^2
            # x*p2x + y*p2y = r^2
            
            mat = [[p1[0], p1[1]], [p2[0], p2[1]]]
            res = [r_sq, r_sq]
            sol = np.linalg.solve(mat, res)
            verts.append(np.array([sol[0], sol[1], 0]))
            
        A, B, C, D, E_pt = verts
        pentagon = Polygon(A, B, C, D, E_pt, color=BLUE)
        
        # Tangent points
        K, L, M, N, P = tangent_points
        dots = VGroup(*[Dot(pt, color=RED) for pt in tangent_points])
        
        lbl_A = MathTex("A").next_to(A, OUT)
        lbl_B = MathTex("B").next_to(B, OUT)
        lbl_C = MathTex("C").next_to(C, OUT)
        lbl_D = MathTex("D").next_to(D, OUT)
        lbl_E = MathTex("E").next_to(E_pt, OUT)
        
        # Labels for segments x, y, z...
        # x is AK?
        lbl_x = MathTex("x").move_to((A+K)/2 + UP*0.2)
        
        self.add(circle, pentagon, dots)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_E)
```

### 🆔 Задача: geom_9_touching_circles_tangent - Допирни кружници и тангента
**📅 Додадено:** 2025-12-27 02:00
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_touching_circles_tangent(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # k1, k2 touching externally at M.
        r1 = 1.5
        r2 = 1.0
        C1 = np.array([-r1, 0, 0])
        C2 = np.array([r2, 0, 0])
        # Touching at origin (0,0) if we shift.
        # Let M = (0,0).
        # C1 = (-1.5, 0), C2 = (1.0, 0).
        M = ORIGIN
        C1 = LEFT * r1
        C2 = RIGHT * r2
        
        k1 = Circle(radius=r1, color=BLUE).move_to(C1)
        k2 = Circle(radius=r2, color=BLUE).move_to(C2)
        
        # Vertical tangent t touching k2 at N.
        # k2 is from 0 to 2. Center at 1.
        # Vertical tangent at rightmost point? Or leftmost?
        # "touching k2 at N".
        # Could be x = 2*r2 = 2.
        N = C2 + RIGHT * r2
        line_t = Line(N + UP*3, N + DOWN*3, color=BLACK)
        
        # k3 touching k1, k2, and t.
        # This is a classic Apollonius or Descartes circle problem case.
        # k3 is in the gap between k1, k2, t.
        # Let k3 have radius r3 and center (x3, y3).
        # Touching t (x=2): x3 + r3 = 2 => x3 = 2 - r3.
        # Touching k2 (ext): dist(C3, C2) = r2 + r3.
        # Touching k1 (ext): dist(C3, C1) = r1 + r3.
        
        # Solve for r3, y3.
        # (x3 - 1)^2 + y3^2 = (1 + r3)^2
        # (x3 - (-1.5))^2 + y3^2 = (1.5 + r3)^2
        # Substitute x3 = 2 - r3.
        
        # Eq 1: (2 - r3 - 1)^2 + y3^2 = (1 + r3)^2
        # (1 - r3)^2 + y3^2 = (1 + r3)^2
        # 1 - 2r3 + r3^2 + y3^2 = 1 + 2r3 + r3^2
        # y3^2 = 4r3
        
        # Eq 2: (2 - r3 + 1.5)^2 + y3^2 = (1.5 + r3)^2
        # (3.5 - r3)^2 + y3^2 = (1.5 + r3)^2
        # 12.25 - 7r3 + r3^2 + y3^2 = 2.25 + 3r3 + r3^2
        # 10 - 10r3 + y3^2 = 0
        # y3^2 = 10r3 - 10
        
        # Equate y3^2:
        # 4r3 = 10r3 - 10
        # 6r3 = 10 => r3 = 10/6 = 5/3 approx 1.66
        # Wait, r3 should be small.
        # Did I assume k3 is "inside"?
        # k1 is left of 0. k2 is right of 0. t is at 2.
        # k3 is likely above or below.
        # Let's recheck logic.
        # x3 = 2 - r3.
        # C2 = (1, 0). r2 = 1.
        # C1 = (-1.5, 0). r1 = 1.5.
        
        # (2-r3 - 1)^2 + y3^2 = (1+r3)^2
        # (1-r3)^2 + y3^2 = (1+r3)^2
        # 1 - 2r3 + r3^2 + y3^2 = 1 + 2r3 + r3^2
        # y3^2 = 4r3. Correct.
        
        # (2-r3 + 1.5)^2 + y3^2 = (1.5+r3)^2
        # (3.5-r3)^2 + y3^2 = (1.5+r3)^2
        # 12.25 - 7r3 + r3^2 + y3^2 = 2.25 + 3r3 + r3^2
        # 10 - 10r3 + y3^2 = 0.
        # y3^2 = 10r3 - 10. Correct.
        
        # 4r3 = 10r3 - 10 => 10 = 6r3 => r3 = 5/3.
        # This is a large circle.
        # y3^2 = 4 * 5/3 = 20/3. y3 = sqrt(6.66) approx 2.58.
        # x3 = 2 - 5/3 = 1/3.
        
        # Is there a smaller solution?
        # Maybe touching t on the left?
        # t is at x=2. k3 is to the left of t. So x3 = 2 - r3. Correct.
        # Maybe k3 touches k1 internally? No, "touching k1, k2". Usually external.
        
        # Let's draw this one.
        r3 = 5/3
        y3 = np.sqrt(20/3)
        x3 = 1/3
        C3 = np.array([x3, y3, 0])
        k3 = Circle(radius=r3, color=GREEN).move_to(C3)
        
        # Also symmetric solution below
        C3_down = np.array([x3, -y3, 0])
        k3_down = Circle(radius=r3, color=GREEN).move_to(C3_down)
        
        lbl_M = MathTex("M").next_to(M, DOWN)
        lbl_N = MathTex("N").next_to(N, RIGHT)
        
        self.add(k1, k2, line_t, k3, k3_down)
        self.add(lbl_M, lbl_N)
```

### 🆔 Задача: geom_9_midpoints_parallelogram - Средини во четириаголник и паралелограм
**📅 Додадено:** 2025-12-27 02:00
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_midpoints_parallelogram(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # General quadrilateral ABCD
        A = np.array([-3, -1, 0])
        B = np.array([2, -2, 0])
        C = np.array([3, 2, 0])
        D = np.array([-2, 3, 0])
        
        quad = Polygon(A, B, C, D, color=BLUE)
        
        # E midpoint of AB
        E = (A + B) / 2
        dot_E = Dot(E, color=RED)
        
        # K midpoint of CD
        K = (C + D) / 2
        dot_K = Dot(K, color=RED)
        
        # Connect AK, CE, BK, DE
        seg_AK = Line(A, K, color=GRAY)
        seg_CE = Line(C, E, color=GRAY)
        seg_BK = Line(B, K, color=GRAY)
        seg_DE = Line(D, E, color=GRAY)
        
        # Midpoints M1 (AK), M2 (CE), M3 (BK), M4 (DE)
        M1 = (A + K) / 2
        M2 = (C + E) / 2
        M3 = (B + K) / 2
        M4 = (D + E) / 2
        
        dots_M = VGroup(Dot(M1), Dot(M2), Dot(M3), Dot(M4))
        
        # Draw diagonal EK? "Draw diagonal EK"
        seg_EK = DashedLine(E, K, color=GREEN)
        
        lbl_A = MathTex("A").next_to(A, LEFT)
        lbl_B = MathTex("B").next_to(B, RIGHT)
        lbl_C = MathTex("C").next_to(C, RIGHT)
        lbl_D = MathTex("D").next_to(D, LEFT)
        lbl_E = MathTex("E").next_to(E, DOWN)
        lbl_K = MathTex("K").next_to(K, UP)
        
        self.add(quad, dot_E, dot_K, seg_AK, seg_CE, seg_BK, seg_DE)
        self.add(dots_M, seg_EK)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_E, lbl_K)
```

### 🆔 Задача: geom_9_centroid_plane_dist - Тежиште и растојание до рамнина
**📅 Додадено:** 2025-12-27 02:00
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_centroid_plane_dist(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # 3D effect in 2D
        # Plane pi represented by a parallelogram at bottom
        p1 = np.array([-4, -3, 0])
        p2 = np.array([2, -3, 0])
        p3 = np.array([4, -1, 0])
        p4 = np.array([-2, -1, 0])
        plane = Polygon(p1, p2, p3, p4, color=GRAY, fill_opacity=0.2, fill_color=GRAY)
        lbl_pi = MathTex(r"\\pi").next_to(p3, RIGHT)
        
        # Triangle ABC above
        A = np.array([-2, 2, 0])
        B = np.array([1, 3, 0])
        C = np.array([3, 1, 0])
        tri = Polygon(A, B, C, color=BLUE)
        
        # Projections A', B', C'
        # Assume projection is just vertical drop to y = -2 (approx plane level)
        # Or better, project onto the plane geometry.
        # Let's just drop straight down by some amount?
        # No, "perpendicular segments to the plane".
        # Let's assume plane is z=0 in 3D, but we are viewing from side.
        # Let's just draw vertical lines downwards to the visual plane.
        
        # Define a "floor" y-level for the plane visually
        floor_y = -2
        
        A_prime = np.array([A[0], floor_y, 0])
        B_prime = np.array([B[0], floor_y + 0.5, 0]) # Slight perspective offset?
        # Actually, if plane is flat horizontal, y is constant?
        # But drawn in perspective.
        # Let's project onto the line segment p4-p3? Or inside.
        # Let's just use vertical lines to some y.
        
        # Better: define plane equation ax+by+cz=d? Too complex.
        # Just drop to y = -1.5 + x*0.1 (slanted floor)
        def get_floor_y(x):
            return -2 + x * 0.2
            
        A_prime = np.array([A[0], get_floor_y(A[0]), 0])
        B_prime = np.array([B[0], get_floor_y(B[0]), 0])
        C_prime = np.array([C[0], get_floor_y(C[0]), 0])
        
        line_AA = DashedLine(A, A_prime, color=RED)
        line_BB = DashedLine(B, B_prime, color=RED)
        line_CC = DashedLine(C, C_prime, color=RED)
        
        # Centroid T
        T = (A + B + C) / 3
        dot_T = Dot(T, color=BLACK)
        
        # Projection T'
        T_prime = np.array([T[0], get_floor_y(T[0]), 0])
        line_TT = DashedLine(T, T_prime, color=GREEN)
        dot_T_prime = Dot(T_prime, color=BLACK)
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, UP)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_T = MathTex("T").next_to(T, UP)
        
        lbl_Ap = MathTex("A'").next_to(A_prime, DOWN)
        lbl_Bp = MathTex("B'").next_to(B_prime, DOWN)
        lbl_Cp = MathTex("C'").next_to(C_prime, DOWN)
        lbl_Tp = MathTex("T'").next_to(T_prime, DOWN)
        
        self.add(plane, lbl_pi)
        self.add(tri, line_AA, line_BB, line_CC)
        self.add(dot_T, line_TT, dot_T_prime)
        self.add(lbl_A, lbl_B, lbl_C, lbl_T, lbl_Ap, lbl_Bp, lbl_Cp, lbl_Tp)
```

### 🆔 Задача: geom_9_incenter_intersect - Пресечни кружници и центар
**📅 Додадено:** 2025-12-27 02:00
**🐍 Python/Manim Код:**
```python
from manim import *

class Task_geom_9_incenter_intersect(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # k1, k2 intersecting.
        # Center O of k2 lies on k1.
        r1 = 2
        O1 = LEFT * 1
        k1 = Circle(radius=r1, color=BLUE).move_to(O1)
        
        # O (center of k2) is on k1.
        O = O1 + RIGHT * r1 # Point (1, 0)
        r2 = 1.5
        k2 = Circle(radius=r2, color=GREEN).move_to(O)
        
        # Intersection points A and B
        # Solve intersection
        # (x+1)^2 + y^2 = 4
        # (x-1)^2 + y^2 = 2.25
        # Subtract: (x+1)^2 - (x-1)^2 = 1.75
        # (x^2+2x+1) - (x^2-2x+1) = 4x = 1.75 => x = 0.4375
        x_int = 0.4375
        y_int = np.sqrt(4 - (x_int + 1)**2)
        
        A = np.array([x_int, y_int, 0])
        B = np.array([x_int, -y_int, 0])
        
        # Pick C on k1
        # "Pick a point C on k1"
        # Let's pick C at angle 120 deg from O1
        angle_C = np.deg2rad(120)
        C = O1 + np.array([np.cos(angle_C), np.sin(angle_C), 0]) * r1
        
        # Draw line OC
        line_OC = Line(O, C, color=GRAY) # O is center of k2
        
        # Intersection with k2 as D
        # Line OC intersects k2.
        # D is on k2.
        vec_OC = C - O
        unit_OC = vec_OC / np.linalg.norm(vec_OC)
        D = O + unit_OC * r2 # Intersection in direction of C
        
        # Draw triangle ABC and segments AD, BD
        tri_ABC = Polygon(A, B, C, color=ORANGE)
        seg_AD = Line(A, D, color=RED)
        seg_BD = Line(B, D, color=RED)
        
        lbl_O = MathTex("O").next_to(O, RIGHT)
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, DOWN)
        lbl_C = MathTex("C").next_to(C, LEFT)
        lbl_D = MathTex("D").next_to(D, UP)
        
        self.add(k1, k2, line_OC, tri_ABC, seg_AD, seg_BD)
        self.add(lbl_O, lbl_A, lbl_B, lbl_C, lbl_D)
```
"""

with open(log_path, "a", encoding="utf-8") as f:
    f.write(new_entries)

print("Successfully appended batch 5 to log.")
