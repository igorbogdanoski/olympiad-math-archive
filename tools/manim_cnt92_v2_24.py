from manim import *

class Problem_cnt92_v2_24(Scene):
    def construct(self):
        # Scale
        scale = 1.5
        
        # Parameters
        a = 5.0
        b = 5.0
        angle_deg = 30
        angle_rad = angle_deg * DEGREES
        
        # Coordinates
        A = ORIGIN
        B = RIGHT * a
        D = np.array([b * np.cos(angle_rad), b * np.sin(angle_rad), 0])
        C = B + D
        
        # Shift to center
        center = (A + B + C + D) / 4
        shift = -center
        
        A += shift
        B += shift
        C += shift
        D += shift
        
        # Apply scale
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        
        # Objects
        parallelogram = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.2)
        
        # Labels
        label_a = MathTex("a=5").next_to(Line(A, B), DOWN)
        label_b = MathTex("b=5").next_to(Line(B, C), RIGHT)
        
        # Angle
        angle_arc = Angle(Line(A, B), Line(A, D), radius=0.5, color=YELLOW)
        label_angle = MathTex("30^\\circ").next_to(angle_arc, RIGHT, buff=0.1)
        
        # Text
        text = MathTex(
            r"S = ab \sin(30^\circ) = 12.5 \implies ab = 25",
            r"\min(a+b) \text{ when } a=b=\sqrt{25}=5",
            r"P = 2(a+b) = 2(5+5) = 20"
        ).arrange(DOWN).to_corner(UL)
        
        self.add(parallelogram)
        self.add(label_a, label_b)
        self.add(angle_arc, label_angle)
        self.add(text)
