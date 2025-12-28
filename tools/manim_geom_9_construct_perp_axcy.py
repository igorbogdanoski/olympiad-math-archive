from manim import *

class Problem_geom_9_construct_perp_axcy(Scene):
    def construct(self):
        # Scale
        scale = 1.5
        
        # Coordinates
        # A at (-2, 0), B at (2, 0)
        R = 2.0
        A = LEFT * R
        B = RIGHT * R
        
        # C at (0.5, 0)
        c_val = 0.5
        C = RIGHT * c_val
        
        # Circle
        circle = Circle(radius=R, color=BLUE)
        
        # Midpoint M of CB
        # B is at x=2. C is at x=0.5.
        # M is at x = (2+0.5)/2 = 1.25
        m_val = (R + c_val) / 2
        M = RIGHT * m_val
        
        # X and Y
        # x = m_val
        # y = sqrt(R^2 - m_val^2)
        y_val = np.sqrt(R**2 - m_val**2)
        X = np.array([m_val, y_val, 0])
        Y = np.array([m_val, -y_val, 0])
        
        # Shift to center
        # Center of circle is origin.
        # Just scale.
        A *= scale
        B *= scale
        C *= scale
        M *= scale
        X *= scale
        Y *= scale
        circle.scale(scale)
        
        # Objects
        line_AB = Line(A, B, color=WHITE)
        line_XY = DashedLine(X, Y, color=GRAY)
        
        line_AX = Line(A, X, color=YELLOW)
        line_CY = Line(C, Y, color=YELLOW)
        
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_X = Dot(X, color=RED)
        dot_Y = Dot(Y, color=RED)
        dot_M = Dot(M, color=WHITE).scale(0.5)
        
        label_A = MathTex("A").next_to(dot_A, LEFT)
        label_B = MathTex("B").next_to(dot_B, RIGHT)
        label_C = MathTex("C").next_to(dot_C, DOWN)
        label_X = MathTex("X").next_to(dot_X, UR)
        label_Y = MathTex("Y").next_to(dot_Y, DR)
        label_M = MathTex("M").next_to(dot_M, DR).scale(0.7)
        
        # Right angle at intersection of AX and CY?
        # Intersection point P
        # Line AX: y - 0 = (yX / (xX - xA)) * (x - xA)
        # Line CY: y - yY = (yY / (xY - xC)) * (x - xY) ? No.
        # Line CY passes through C(xC, 0) and Y(xY, yY).
        # Slope m2 = yY / (xY - xC).
        # Slope m1 = yX / (xX - xA).
        # Check m1 * m2 = -1.
        # m1 = y_val / (m_val - (-R)) = y_val / (m_val + R)
        # m2 = -y_val / (m_val - c_val)
        # m1 * m2 = -y_val^2 / ((m_val + R)(m_val - c_val))
        # y_val^2 = R^2 - m_val^2 = (R-m_val)(R+m_val)
        # m1 * m2 = - (R-m_val)(R+m_val) / ((m_val+R)(m_val-c_val))
        # = - (R-m_val) / (m_val - c_val)
        # m_val = (R+c_val)/2
        # R - m_val = R - (R+c)/2 = (R-c)/2
        # m_val - c_val = (R+c)/2 - c = (R-c)/2
        # Ratio is 1. So m1 * m2 = -1. Correct.
        
        # Intersection P
        # Solve for intersection
        # ... visual is enough usually, but let's add angle.
        intersection = line_intersection(
            [A, X],
            [C, Y]
        )
        right_angle = RightAngle(
            Line(intersection, X),
            Line(intersection, Y),
            length=0.3, color=RED
        )
        
        self.add(circle)
        self.add(line_AB, line_XY)
        self.add(line_AX, line_CY)
        self.add(right_angle)
        self.add(dot_A, dot_B, dot_C, dot_X, dot_Y, dot_M)
        self.add(label_A, label_B, label_C, label_X, label_Y, label_M)
        
        # Add text
        text = MathTex(r"AX \perp CY").to_corner(UL)
        self.add(text)
