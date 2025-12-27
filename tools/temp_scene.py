from manim import *

class Task_geom_9_leg_ratio_circles(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Right triangle ABC, C=90.
        # Legs a, b. Hypotenuse c.
        # Let a=3, b=4, c=5.
        a = 3
        b = 4
        c = 5
        
        C = ORIGIN
        A = UP * b
        B = RIGHT * a
        
        # Shift
        center = (A + B + C) / 3
        A -= center
        B -= center
        C -= center
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Circumcircle
        # Center O is midpoint of hypotenuse AB.
        O = (A + B) / 2
        R = c / 2
        circumcircle = Circle(radius=R, color=GRAY).move_to(O)
        dot_O = Dot(O, color=GRAY)
        
        # Incircle
        # Incenter I
        I = (a*A + b*B + c*C) / (a+b+c)
        r = (a + b - c) / 2 # (3+4-5)/2 = 1
        incircle = Circle(radius=r, color=GREEN).move_to(I)
        dot_I = Dot(I, color=GREEN)
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, RIGHT)
        lbl_C = MathTex("C").next_to(C, DOWN)
        lbl_O = MathTex("O").next_to(O, UP)
        lbl_I = MathTex("I").next_to(I, DOWN)
        
        lbl_R = MathTex("R").next_to(O, UP+LEFT)
        lbl_r = MathTex("r").next_to(I, DOWN+LEFT)
        
        self.add(circumcircle, tri, incircle, dot_O, dot_I)
        self.add(lbl_A, lbl_B, lbl_C, lbl_O, lbl_I, lbl_R, lbl_r)


config.media_width = '100%'
config.verbosity = 'ERROR'
