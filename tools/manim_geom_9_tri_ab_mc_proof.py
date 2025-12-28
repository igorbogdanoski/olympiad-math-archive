from manim import *

class Problem_geom_9_tri_ab_mc_proof(Scene):
    def construct(self):
        # Scale
        scale = 2.5
        
        # Coordinates
        # A at origin? Let's put midpoint of AB at origin.
        # AB length = 2 (scaled later)
        c_len = 2
        A = np.array([-c_len/2, 0, 0])
        B = np.array([c_len/2, 0, 0])
        
        # Calculate C
        # A = (xA, yA), B = (xB, yB)
        # Line AC: y - yA = tan(70) * (x - xA)
        # Line BC: y - yB = tan(180-80) * (x - xB) = tan(100) * (x - xB)
        
        tan70 = np.tan(np.deg2rad(70))
        tan100 = np.tan(np.deg2rad(100))
        
        # Solve for C(x, y)
        # y = tan70 * (x - xA)
        # y = tan100 * (x - xB)
        # tan70 * (x - xA) = tan100 * (x - xB)
        # x * (tan70 - tan100) = tan70 * xA - tan100 * xB
        x_C = (tan70 * A[0] - tan100 * B[0]) / (tan70 - tan100)
        y_C = tan70 * (x_C - A[0])
        C = np.array([x_C, y_C, 0])
        
        # Calculate M
        # M is intersection of:
        # Ray from B at 60 degrees to AB (since angle ABM = 80 - 20 = 60)
        # Ray from C at 10 degrees to CA.
        # Angle of CA: 70 degrees.
        # Angle of CM: 70 - 10 = 60 degrees? No.
        # Vector CA = A - C. Angle of AC is 70. Angle of CA is 70+180 = 250.
        # M is inside.
        # Angle of AC is 70.
        # Angle of CM relative to CA is 10.
        # Angle of BC is 100. Angle of CB is 280 (-80).
        # Angle C is 30.
        # Line AC angle is 70. Line BC angle is 100.
        # At C, angle between CA and CB is 30.
        # Ray CM is 10 from CA.
        # Direction of AC is 70. Direction of CA is 250.
        # Direction of BC is 100. Direction of CB is 280.
        # 280 - 250 = 30. Correct.
        # Ray CM should be 10 degrees from CA towards CB.
        # So direction is 250 + 10 = 260 degrees.
        # Or 280 - 20 = 260.
        # So line CM has angle 260 (or -100).
        
        # Line BM: Angle 60 from AB. AB is 0. So angle 60.
        # Line BM: y - yB = tan(60) * (x - xB)
        # Line CM: y - yC = tan(260) * (x - xC)
        
        tan60 = np.tan(np.deg2rad(60))
        tan260 = np.tan(np.deg2rad(260))
        
        x_M = (tan60 * B[0] - tan260 * C[0] + C[1] - B[1]) / (tan60 - tan260)
        y_M = tan60 * (x_M - B[0]) + B[1]
        M = np.array([x_M, y_M, 0])
        
        # Shift to center
        center = (A + B + C) / 3
        shift = -center
        A += shift
        B += shift
        C += shift
        M += shift
        
        # Scale
        A *= scale
        B *= scale
        C *= scale
        M *= scale
        
        # Create objects
        triangle = Polygon(A, B, C, color=BLUE)
        
        # Points
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_M = Dot(M, color=RED)
        
        # Lines
        line_AM = Line(A, M, color=YELLOW)
        line_BM = Line(B, M, color=YELLOW)
        line_CM = Line(C, M, color=YELLOW)
        
        # Labels
        label_A = MathTex("A").next_to(dot_A, DL)
        label_B = MathTex("B").next_to(dot_B, DR)
        label_C = MathTex("C").next_to(dot_C, UP)
        label_M = MathTex("M").next_to(dot_M, LEFT)
        
        # Angles
        # angle_A = Angle(Line(A, B), Line(A, C), radius=0.5)
        # label_70 = MathTex("70^\circ").next_to(angle_A, UP)
        
        self.add(triangle)
        self.add(line_AM, line_BM, line_CM)
        self.add(dot_A, dot_B, dot_C, dot_M)
        self.add(label_A, label_B, label_C, label_M)
        
        # Highlight AB and MC
        line_AB = Line(A, B, color=RED, stroke_width=6)
        line_MC = Line(M, C, color=RED, stroke_width=6)
        self.add(line_AB, line_MC)
        
        # Add text
        text = MathTex("AB = MC").to_edge(UP)
        self.add(text)
