from manim import *

class MyScene(Scene):
    def construct(self):
        # Define points
        A = LEFT + UP
        B = RIGHT + UP
        C = ORIGIN
        Y = (A + B) / 2

        # Create dots for points
        dot_A = Dot(A, color=RED, radius=0.12)
        dot_B = Dot(B, color=RED, radius=0.12)
        dot_C = Dot(C, color=RED, radius=0.12)
        dot_Y = Dot(Y, color=RED, radius=0.12)

        # Create lines
        AB = Line(A, B, color=WHITE)
        AC = Line(A, C, color=WHITE)
        BC = Line(B, C, color=WHITE)
        AY = Line(A, Y, color=WHITE, stroke_width=2)
        BY = Line(B, Y, color=WHITE, stroke_width=2)

        # Create labels
        lbl_A = Tex("A").next_to(A, LEFT)
        lbl_B = Tex("B").next_to(B, RIGHT)
        lbl_C = Tex("C").next_to(C, DOWN)
        lbl_Y = Tex("Y").next_to(Y, UP)
        res = Tex("Result").next_to(Y, DOWN)

        # Create arcs
        gamma_arc = Arc(radius=0.4, start_angle=PI/2, angle=-PI/2, color=YELLOW).move_to(Y)
        ayb_arc = Arc(radius=0.4, start_angle=0, angle=PI, color=YELLOW).move_to(Y)

        # Create cross and highlight
        cross = Cross(dot_Y, color=RED, stroke_width=4).scale(0.5)
        highlight = SurroundingRectangle(dot_Y, color=RED, buff=0.08)

        # Add everything to the scene
        self.add(AB, AC, BC, AY, BY, dot_A, dot_B, dot_C, dot_Y, cross, highlight, gamma_arc, ayb_arc)
        self.add(lbl_A, lbl_B, lbl_C, lbl_Y, res)