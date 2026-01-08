from manim import *

class Problem_2022_mun_g9_3(Scene):
    def construct(self):
        # Scale
        scale = 1.5
        
        # Parameters
        h = 4.0
        a = h
        
        # Coordinates
        # Base on x-axis, centered at origin
        A = LEFT * a / 2
        B = RIGHT * a / 2
        C = UP * h
        
        # Shift to center
        center = (A + B + C) / 3
        shift = -center
        
        A += shift
        B += shift
        C += shift
        
        # Apply scale
        A *= scale
        B *= scale
        C *= scale
        
        # Objects
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        
        # Altitude
        H = (A + B) / 2
        altitude = Line(C, H, color=RED)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, UP)
        
        label_h = MathTex("h").next_to(altitude, RIGHT, buff=0.05)
        label_a = MathTex("a=h").next_to(Line(A, B), DOWN)
        
        # Right angle
        ra = RightAngle(Line(C, H), Line(H, B), length=0.3)
        
        # Text
        text = MathTex(
            r"b^2 = h^2 + (a/2)^2 = h^2 + (h/2)^2 = \frac{5h^2}{4}",
            r"b = \frrac{h\sqrt{5}}{2}",
            r"L = a + 2b = h + h\sqrrt{5} = (1 + \sqrt{5})h",
            r"x=1, y=5 \implies x+y=6"
        ).arrange(DOWN).to_corner(UL).scale(0.8)
        
        self.add(triangle, altitude)
        self.add(label_A, label_B, label_C)
        self.add(label_h, label_a)
        self.add(ra)
        self.add(text)
