from manim import *

class Problem_2022_mun_g6_3(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Two intersecting lines
        # Line 1: Horizontal
        # Line 2: Rotated by 60 degrees
        
        L1 = Line(LEFT*3, RIGHT*3, color=BLACK)
        L2 = Line(LEFT*3, RIGHT*3, color=BLACK).rotate(60*DEGREES)
        
        # Intersection is at origin
        
        # Arcs for angles
        # Angle 1 (Top Right): 0 to 60
        arc1 = Arc(radius=0.5, start_angle=0, angle=60*DEGREES, color=BLUE)
        
        # Angle 2 (Top Left): 60 to 180
        arc2 = Arc(radius=0.6, start_angle=60*DEGREES, angle=120*DEGREES, color=RED)
        
        # Angle 3 (Bottom Left): 180 to 240
        arc3 = Arc(radius=0.5, start_angle=180*DEGREES, angle=60*DEGREES, color=BLUE)
        
        # Angle 4 (Bottom Right): 240 to 360
        arc4 = Arc(radius=0.6, start_angle=240*DEGREES, angle=120*DEGREES, color=RED)
        
        # Labels
        # We know the angles are 60 and 120.
        # But the problem starts with "Sum of 3 is 300".
        # Let's label them alpha and beta.
        
        lbl_alpha = MathTex(r"\alpha", color=BLUE).move_to(0.8*np.array([np.cos(30*DEGREES), np.sin(30*DEGREES), 0]))
        lbl_beta = MathTex(r"\beta", color=RED).move_to(0.9*np.array([np.cos(120*DEGREES), np.sin(120*DEGREES), 0]))
        
        self.add(L1, L2)
        self.add(arc1, arc2, arc3, arc4)
        self.add(lbl_alpha, lbl_beta)
        
        # Text
        text = MathTex(r"\text{Sum of 3 angles} = 300^\circ", color=BLACK).to_corner(UL)
        text2 = MathTex(r"360^\circ - 300^\circ = 60^\circ", color=BLACK).next_to(text, DOWN, aligned_edge=LEFT)
        text3 = MathTex(r"\text{Supplement} = 180^\circ - 60^\circ = 120^\circ", color=BLACK).next_to(text2, DOWN, aligned_edge=LEFT)
        
        self.add(text, text2, text3)
