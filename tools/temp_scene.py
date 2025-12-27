from manim import *

class Task_geom_angle_alt_bisector_03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Triangle ABC, AC > AB.
        # Let A = (0, 3), B = (-1, 0), C = (4, 0)
        A = UP * 3
        B = LEFT * 1
        C = RIGHT * 4
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Altitude AD
        D = np.array([A[0], B[1], 0])
        alt_AD = Line(A, D, color=RED)
        
        # Angle bisector AS
        # S on BC.
        # BS / SC = AB / AC
        len_AB = np.linalg.norm(B - A)
        len_AC = np.linalg.norm(C - A)
        ratio = len_AB / (len_AB + len_AC)
        S = B + (C - B) * ratio
        bisector_AS = Line(A, S, color=GREEN)
        
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, DOWN+LEFT)
        lbl_C = MathTex("C").next_to(C, DOWN+RIGHT)
        lbl_D = MathTex("D").next_to(D, DOWN)
        lbl_S = MathTex("S").next_to(S, DOWN)
        
        lbl_beta = MathTex("\beta").next_to(B, UP+RIGHT, buff=0.5)
        lbl_gamma = MathTex("\gamma").next_to(C, UP+LEFT, buff=0.5)
        
        self.add(tri, alt_AD, bisector_AS)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_S, lbl_beta, lbl_gamma)
        
        # Right angle at D
        ra = RightAngle(Line(D, A), Line(D, C), quadrant=(1,1))
        self.add(ra)


config.media_width = '100%'
config.verbosity = 'ERROR'
