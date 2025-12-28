from manim import *

class Problem_geo_two_circles_incenter(Scene):
    def construct(self):
        # Scale
        scale = 1.5
        
        # Parameters
        R1 = 2.0
        R2 = 1.8
        
        # Coordinates
        O1 = ORIGIN
        O = RIGHT * R1 # O is on k1
        
        # Intersections A, B
        # x^2 + y^2 = R1^2
        # (x-R1)^2 + y^2 = R2^2 => x^2 - 2xR1 + R1^2 + y^2 = R2^2
        # R1^2 - 2xR1 + R1^2 = R2^2 => 2R1^2 - 2xR1 = R2^2
        # 2xR1 = 2R1^2 - R2^2 => x = (2R1^2 - R2^2) / (2R1) = R1 - R2^2/(2R1)
        x_A = R1 - R2**2 / (2 * R1)
        y_A = np.sqrt(R1**2 - x_A**2)
        
        A = np.array([x_A, y_A, 0])
        B = np.array([x_A, -y_A, 0])
        
        # Point C on k1
        # Angle for C. A is at angle acos(x_A/R1).
        angle_A = np.arccos(x_A / R1)
        # C should be on arc AB not containing O.
        # O is at angle 0. A is at angle_A, B is at -angle_A.
        # Arc not containing O is from angle_A to 2pi - angle_A?
        # No, O is at 0. Arc containing O is small arc near 0.
        # Arc NOT containing O is the large arc.
        # Let's pick angle pi (180 degrees).
        angle_C = np.pi
        C = np.array([R1 * np.cos(angle_C), R1 * np.sin(angle_C), 0])
        
        # Point D
        # Intersection of OC and k2.
        # Vector OC = C - O.
        v_OC = C - O
        u_OC = v_OC / np.linalg.norm(v_OC)
        D = O + u_OC * R2
        
        # Shift to center
        center = (O1 + O) / 2
        shift = -center
        
        O1 += shift
        O += shift
        A += shift
        B += shift
        C += shift
        D += shift
        
        # Apply scale
        O1 *= scale
        O *= scale
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        R1 *= scale
        R2 *= scale
        
        # Objects
        k1 = Circle(radius=R1, color=BLUE, arc_center=O1)
        k2 = Circle(radius=R2, color=GREEN, arc_center=O)
        
        triangle = Polygon(A, B, C, color=WHITE, fill_opacity=0.1)
        
        line_OC = Line(O, C, color=YELLOW)
        
        dot_O = Dot(O, color=GREEN)
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_D = Dot(D, color=RED)
        
        label_O = MathTex("O").next_to(dot_O, RIGHT)
        label_A = MathTex("A").next_to(dot_A, UR)
        label_B = MathTex("B").next_to(dot_B, DR)
        label_C = MathTex("C").next_to(dot_C, LEFT)
        label_D = MathTex("D").next_to(dot_D, UP)
        
        # Incenter proof visualization
        # Draw bisectors AD and BD
        line_AD = DashedLine(A, D, color=RED)
        line_BD = DashedLine(B, D, color=RED)
        
        # Mark angles
        # Angle CAD and DAB
        a1 = Angle(Line(A, C), Line(A, D), radius=0.4, color=YELLOW)
        a2 = Angle(Line(A, D), Line(A, B), radius=0.5, color=YELLOW)
        
        # Angle CBD and DBA
        b1 = Angle(Line(B, D), Line(B, C), radius=0.4, color=YELLOW)
        b2 = Angle(Line(B, A), Line(B, D), radius=0.5, color=YELLOW)
        
        self.add(k1, k2)
        self.add(triangle)
        self.add(line_OC)
        self.add(line_AD, line_BD)
        self.add(dot_O, dot_A, dot_B, dot_C, dot_D)
        self.add(label_O, label_A, label_B, label_C, label_D)
        self.add(a1, a2, b1, b2)
        
        # Text
        text = MathTex(r"D = \text{Incenter of } \triangle ABC").to_corner(UL)
        self.add(text)
