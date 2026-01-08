from manim import *

class Problem_right_tri_angles_10(Scene):
    def construct(self):
        # Scale
        scale = 1.5
        
        # Parameters
        q = 1.0 # AH
        p = 3.0 # HB
        h = np.sqrt(p * q) # CH
        
        # Coordinates
        H = ORIGIN
        A = LEFT * q
        B = RIGHT * p
        C = UP * h
        
        # Shift to center
        center = (A + B + C) / 3
        shift = -center
        
        A += shift
        B += shift
        C += shift
        H += shift
        
        # Apply scale
        A *= scale
        B *= scale
        C *= scale
        H *= scale
        
        # Objects
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        altitude = Line(C, H, color=RED)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, UP)
        label_H = MathTex("H").next_to(H, DOWN)
        
        # Lengths
        brace_q = Brace(Line(A, H), DOWN)
        label_q = brace_q.get_text("q")
        
        brace_p = Brace(Line(H, B), DOWN)
        label_p = brace_p.get_text("p")
        
        label_a = MathTex("a").next_to(Line(A, C), UL)
        label_b = MathTex("b").next_to(Line(B, C), UR)
        
        # Right angles
        ra_C = RightAngle(Line(C, A), Line(C, B), length=0.3)
        ra_H = RightAngle(Line(H, C), Line(H, B), length=0.3)
        
        # Text
        text = MathTex(
            r"p - q = a",
            r"\implies \text{Angles: } 30^\cirrc, 60^\cirrc, 90^\circr
        ).arrange(DOWN).to_corner(UL)
        
        # Angle values
        angle_A = Angle(Line(A, B), Line(A, C), radius=0.5, color=YELLOW)
        val_A = MathTex(r"60^\circ").next_to(angle_A, RIGHT)
        
        angle_B = Angle(Line(B, C), Line(B, A), radius=0.5, color=YELLOW)
        val_B = MathTex(r"30^\circ").next_to(angle_B, LEFT)
        
        self.add(triangle, altitude)
        self.add(label_A, label_B, label_C, label_H)
        self.add(brace_q, label_q, brace_p, label_p)
        self.add(label_a, label_b)
        self.add(ra_C, ra_H)
        self.add(text)
        self.add(angle_A, val_A, angle_B, val_B)
