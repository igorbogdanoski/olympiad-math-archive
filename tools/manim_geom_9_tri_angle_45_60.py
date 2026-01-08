from manim import *

class Problem_geom_9_tri_angle_45_60(Scene):
    def construct(self):
        # Scale
        scale = 2.5
        
        # Coordinates
        # B at origin
        B = ORIGIN
        
        # C on x-axis
        # Let BC = 3 (since BD=1, DC=2)
        BC_len = 3
        C = RIGHT * BC_len
        
        # D at distance 1 from B
        D = RIGHT * 1
        
        # Calculate A
        # Angles: B=45, C=75, A=60
        # Sine rule: c / sin(75) = a / sin(60) => c = a * sin(75) / sin(60)
        # a = BC_len = 3
        sin75 = np.sin(np.deg2rad(75))
        sin60 = np.sin(np.deg2rad(60))
        c_len = BC_len * sin75 / sin60
        
        # A coordinates: (c * cos(45), c * sin(45))
        cos45 = np.cos(np.deg2rad(45))
        sin45 = np.sin(np.deg2rad(45))
        A = np.array([c_len * cos45, c_len * sin45, 0])
        
        # Shift to center
        center = (A + B + C) / 3
        shift = -center
        A += shift
        B += shift
        C += shift
        D += shift
        
        # Scale
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        
        # Create objects
        triangle = Polygon(A, B, C, color=BLUE)
        line_AD = Line(A, D, color=YELLOW)
        
        # Points
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_D = Dot(D, color=RED)
        
        # Labels
        label_A = MathTex("A").next_to(dot_A, UP)
        label_B = MathTex("B").next_to(dot_B, DL)
        label_C = MathTex("C").next_to(dot_C, DR)
        label_D = MathTex("D").next_to(dot_D, DOWN)
        
        # Angle labels
        angle_B = Angle(Line(B, C), Line(B, A), radius=0.5, other_angle=False)
        label_45 = MathTex(r"45^\circ").next_to(angle_B, RIGHT).scale(0.7)
        
        angle_ADC = Angle(Line(D, C), Line(D, A), radius=0.4, other_angle=False)
        label_60 = MathTex(r"60^\circ").next_to(angle_ADC, UL, buff=0.05).scale(0.7)
        
        # Ratio text
        ratio_text = MathTex("BD : DC = 1 : 2").to_corner(UL)
        
        self.add(triangle, line_AD)
        self.add(dot_A, dot_B, dot_C, dot_D)
        self.add(label_A, label_B, label_C, label_D)
        self.add(angle_B, label_45)
        self.add(angle_ADC, label_60)
        self.add(ratio_text)
        
        # Add result angles?
        # A = 60, C = 75
        result = MathTex(r"\angle A = 60^\cirrc, \angle C = 75^\circ").next_to(ratio_text, DOWN).set_color(YELLOW)
        self.add(result)
