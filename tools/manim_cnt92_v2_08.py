from manim import *

class Problem_cnt92_v2_08(Scene):
    def construct(self):
        # Scale
        scale = 0.8
        
        # Parameters
        a = 8.0
        b = 6.0
        
        # Coordinates
        C = ORIGIN
        A = UP * b
        B = RIGHT * a
        
        # Midpoint of hypotenuse
        M = (A + B) / 2
        
        # Shift to center
        center = (A + B + C) / 3 # Centroid of triangle, or just center of bounding box
        center = (C + B + A)/3
        # Better center: circumcenter M is the center of the circle.
        # Let's center the scene at M.
        shift = -M
        
        A += shift
        B += shift
        C += shift
        M += shift # M becomes ORIGIN
        
        # Apply scale
        A *= scale
        B *= scale
        C *= scale
        M *= scale
        
        # Objects
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        median = Line(C, M, color=RED)
        
        # Circumcircle
        radius = np.linalg.norm(A - M)
        circle = Circle(radius=radius, color=GREEN, arc_center=M)
        
        # Labels
        label_C = MathTex("C").next_to(C, DL)
        label_A = MathTex("A").next_to(A, UP)
        label_B = MathTex("B").next_to(B, RIGHT)
        label_M = MathTex("M").next_to(M, UR)
        
        label_a = MathTex("8").next_to(Line(C, B), DOWN)
        label_b = MathTex("6").next_to(Line(C, A), LEFT)
        label_c = MathTex("c=10").next_to(Line(A, B), UR)
        
        label_mc = MathTex("m_c = 5").next_to(median, DR, buff=0.1)
        
        # Right angle
        ra = RightAngle(Line(C, A), Line(C, B), length=0.4)
        
        # Text
        text = MathTex(
            r"c = \sqrt{6^2 + 8^2} = 10",
            r"m_c = \frac{c}{2} = 5"
        ).arrange(DOWN).to_corner(UL)
        
        self.add(triangle, median, circle)
        self.add(label_C, label_A, label_B, label_M)
        self.add(label_a, label_b, label_c, label_mc)
        self.add(ra)
        self.add(text)
