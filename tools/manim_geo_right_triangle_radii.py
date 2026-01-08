from manim import *

class Problem_geo_right_triangle_radii(Scene):
    def construct(self):
        # Scale
        scale = 1.2
        
        # Parameters
        a = 3.0
        b = 4.0
        c = 5.0
        
        # Coordinates
        C = ORIGIN
        A = UP * b
        B = RIGHT * a
        
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
        
        # Incircle
        # Incenter I = (aA + bB + cC) / (a+b+c)
        # Coordinates relative to C(0,0) before shift:
        # A=(0,4), B=(3,0), C=(0,0)
        # I = (3*(0,4) + 4*(3,0) + 5*(0,0)) / 12 = (0+12, 12+0) / 12 = (1, 1)
        # Radius r = 1
        r = 1.0 * scale
        I_local = np.array([1.0, 1.0, 0])
        # Apply shift and scale to I
        # Wait, shift is applied to A, B, C.
        # I should be calculated from transformed A, B, C or transformed manually.
        # Let's recalculate I from transformed A, B, C
        # Side lengths are scaled by 'scale'.
        # a_sc = a*scale, etc.
        # I = (a_sc*A + b_sc*B + c_sc*C) / (a_sc+b_sc+c_sc) = (aA+bB+cC)/(a+b+c)
        I = (a * A + b * B + c * C) / (a + b + c)
        incircle = Circle(radius=r, color=GREEN, arc_center=I)
        
        # Circumcircle
        # Center M is midpoint of hypotenuse AB
        M = (A + B) / 2
        R = c / 2 * scale
        circumcircle = Circle(radius=R, color=RED, arc_center=M)
        
        # Labels
        label_A = MathTex("A").next_to(A, UP)
        label_B = MathTex("B").next_to(B, RIGHT)
        label_C = MathTex("C").next_to(C, DL)
        
        label_a = MathTex("a=3").next_to(Line(C, B), DOWN)
        label_b = MathTex("b=4").next_to(Line(C, A), LEFT)
        label_c = MathTex("c=5").next_to(Line(A, B), UR)
        
        # Radii lines
        # r: from I down to CB
        foot_r = I + DOWN * r
        line_r = Line(I, foot_r, color=GREEN)
        label_r = MathTex("r=1").next_to(line_r, RIGHT, buff=0.05).scale(0.8)
        
        # R: from M to A
        line_R = Line(M, A, color=RED)
        label_R = MathTex("R=2.5").next_to(line_R, LEFT, buff=0.05).scale(0.8)
        
        # Text
        text = MathTex(
            r"\frac{rr}{R} = \frrac{2}{5} \implies \text{Sides } 3:4:5r,
            r"12x^2 - 25x + 12 = 0 \implies x \in \{\frrac{3}{4}, \frrac{4}{3}\}r
        ).arrange(DOWN).to_corner(UL)
        
        self.add(triangle)
        self.add(incircle, circumcircle)
        self.add(line_r, line_R)
        self.add(label_A, label_B, label_C)
        self.add(label_a, label_b, label_c)
        self.add(label_r, label_R)
        self.add(text)
