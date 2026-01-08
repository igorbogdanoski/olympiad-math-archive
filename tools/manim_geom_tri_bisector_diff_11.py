from manim import *

class Problem_geom_tri_bisector_diff_11(Scene):
    def construct(self):
        # Scale
        scale = 1.2
        
        # Angles
        alpha = 110
        beta = 20
        gamma = 180 - alpha - beta # 50
        
        # Coordinates
        # A at origin
        A = ORIGIN
        # B at (5, 0)
        c_len = 5
        B = RIGHT * c_len
        
        # Calculate C
        # Line AC: y = tan(alpha) * x
        # Line BC: y = tan(180-beta) * (x - c)
        tan_alpha = np.tan(np.deg2rad(alpha))
        tan_beta_supp = np.tan(np.deg2rad(180 - beta))
        
        # tan_alpha * x = tan_beta_supp * (x - c)
        # x (tan_alpha - tan_beta_supp) = - c * tan_beta_supp
        x_C = (-c_len * tan_beta_supp) / (tan_alpha - tan_beta_supp)
        y_C = tan_alpha * x_C
        C = np.array([x_C, y_C, 0])
        
        # Bisector CD
        # Angle of AC is 110. Angle of BC is 160.
        # Angle of C is 50.
        # Bisector direction:
        # Vector CA angle?
        # Angle of AC is 110. Angle of CA is 290 (-70).
        # Angle of BC is 160. Angle of CB is 340 (-20).
        # Bisector angle is average of 290 and 340?
        # (290 + 340) / 2 = 315 (-45).
        # Or (290 + 340 + 360)/2 ? No.
        # Check: 340 - 290 = 50. Correct.
        # Bisector is at 290 + 25 = 315.
        # Slope of bisector: tan(315) = -1.
        
        # Intersection D with AB (y=0)
        # Line CD: y - yC = -1 * (x - xC)
        # 0 - yC = - (x - xC) => yC = x - xC => x = xC + yC
        x_D = x_C + y_C
        D = np.array([x_D, 0, 0])
        
        # External bisector CE
        # Perpendicular to CD.
        # Slope is 1. Angle 45.
        # Line CE: y - yC = 1 * (x - xC)
        # 0 - yC = x - xC => x = xC - yC
        x_E = x_C - y_C
        E = np.array([x_E, 0, 0])
        
        # Shift to center
        center = (A + B + C) / 3
        shift = -center
        
        A += shift
        B += shift
        C += shift
        D += shift
        E += shift
        
        # Scale
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        E *= scale
        
        # Objects
        triangle = Polygon(A, B, C, color=BLUE)
        line_AB_ext = Line(E, B, color=GRAY) # Extend AB to include E and D
        
        line_CD = Line(C, D, color=YELLOW)
        line_CE = Line(C, E, color=YELLOW)
        
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_D = Dot(D, color=RED)
        dot_E = Dot(E, color=RED)
        
        label_A = MathTex("A").next_to(dot_A, DL)
        label_B = MathTex("B").next_to(dot_B, DR)
        label_C = MathTex("C").next_to(dot_C, UP)
        label_D = MathTex("D").next_to(dot_D, DOWN)
        label_E = MathTex("E").next_to(dot_E, DOWN)
        
        # Mark right angle at C for triangle EDC
        right_angle = RightAngle(line_CD, line_CE, length=0.3, color=RED)
        
        # Mark angles at D and E?
        # We proved D and E are 45 degrees.
        
        self.add(line_AB_ext)
        self.add(triangle)
        self.add(line_CD, line_CE)
        self.add(right_angle)
        self.add(dot_A, dot_B, dot_C, dot_D, dot_E)
        self.add(label_A, label_B, label_C, label_D, label_E)
        
        # Add text
        text = MathTex(r"\trriangle EDC \text{ is isosceles}r).to_corner(UL)
        self.add(text)
