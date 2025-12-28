from manim import *

class Problem_geom_9_k1_k2_incenter_proof(Scene):
    def construct(self):
        # Scale
        scale = 1.5
        
        # k1 parameters
        R = 2.0
        O1 = LEFT * 1.0 # Center of k1
        
        # O is on k1. Let O be at (1, 0) relative to O1?
        # O1 = (-1, 0). O = (1, 0). Distance = 2 = R. Correct.
        O = RIGHT * 1.0
        
        # k2 parameters
        r = 1.5
        
        # Create circles
        k1 = Circle(radius=R, color=BLUE).move_to(O1)
        k2 = Circle(radius=r, color=GREEN).move_to(O)
        
        # Intersections A and B
        # x = 0.4375 relative to origin (0,0) which is midpoint of O1O?
        # No, my previous calc assumed O1 at (-1,0) and O at (1,0).
        # x intersection was 0.4375.
        x_int = 0.4375
        y_int = np.sqrt(r**2 - (x_int - O[0])**2)
        
        A = np.array([x_int, y_int, 0])
        B = np.array([x_int, -y_int, 0])
        
        # Point C on k1
        # Angle from O1. O is at 0 degrees.
        # A is at angle arccos((0.4375 - (-1))/2) = arccos(1.4375/2) = arccos(0.718) ~ 44 deg
        # B is at -44 deg.
        # Arc not containing O is from 44 to 316.
        # Let's pick C at 150 degrees.
        angle_C = 150 * DEGREES
        C = O1 + np.array([R * np.cos(angle_C), R * np.sin(angle_C), 0])
        
        # Point D
        # Intersection of OC and k2
        # Vector OC
        v_OC = C - O
        u_OC = v_OC / np.linalg.norm(v_OC)
        D = O + r * u_OC
        
        # Shift to center
        center = (O1 + O) / 2
        shift = -center
        
        O1 += shift
        O += shift
        A += shift
        B += shift
        C += shift
        D += shift
        
        k1.move_to(O1)
        k2.move_to(O)
        
        # Scale
        O1 *= scale
        O *= scale
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        k1.scale(scale)
        k2.scale(scale)
        
        # Objects
        line_OC = Line(O, C, color=YELLOW)
        triangle = Polygon(A, B, C, color=WHITE)
        
        dot_O = Dot(O, color=WHITE)
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_D = Dot(D, color=RED)
        
        label_O = MathTex("O").next_to(dot_O, RIGHT)
        label_A = MathTex("A").next_to(dot_A, UR)
        label_B = MathTex("B").next_to(dot_B, DR)
        label_C = MathTex("C").next_to(dot_C, LEFT)
        label_D = MathTex("D").next_to(dot_D, UL)
        
        label_k1 = MathTex("k_1").next_to(k1, UP)
        label_k2 = MathTex("k_2").next_to(k2, DOWN)
        
        # Incenter proof visualization
        # Draw lines AD, BD, CD
        line_AD = DashedLine(A, D, color=RED)
        line_BD = DashedLine(B, D, color=RED)
        # CD is part of OC
        
        self.add(k1, k2)
        self.add(line_OC)
        self.add(triangle)
        self.add(line_AD, line_BD)
        self.add(dot_O, dot_A, dot_B, dot_C, dot_D)
        self.add(label_O, label_A, label_B, label_C, label_D)
        self.add(label_k1, label_k2)
        
        # Add text
        text = MathTex("D = I_{ABC}").to_corner(UL)
        self.add(text)
