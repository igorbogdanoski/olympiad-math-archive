from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Define points
        # Rectangle ABCD. Width 6, Height 4.
        # Center at origin.
        # A = (-3, -2), B = (3, -2), C = (3, 2), D = (-3, 2)
        
        w = 6.0
        h = 4.0
        A = np.array([-w/2, -h/2, 0])
        B = np.array([w/2, -h/2, 0])
        C = np.array([w/2, h/2, 0])
        D = np.array([-w/2, h/2, 0])
        
        # E on AB such that AE = 1/3 AB.
        # Vector AB = (w, 0). AE = (w/3, 0).
        # E = A + (w/3, 0) = (-3 + 2, -2) = (-1, -2)
        E = A + np.array([w/3, 0, 0])
        
        # F on BC such that BF = 2/3 BC.
        # Vector BC = (0, h). BF = (0, 2h/3).
        # F = B + (0, 2h/3) = (3, -2 + 8/3) = (3, 0.666)
        F = B + np.array([0, 2*h/3, 0])
        
        # G is midpoint of AD.
        # G = (A + D) / 2 = (-3, 0)
        G = (A + D) / 2
        
        # Create objects
        rectangle = Polygon(A, B, C, D, color=BLUE, stroke_width=4)
        triangle_EFG = Polygon(E, F, G, color=GREEN, fill_opacity=0.4, stroke_width=3)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, UR)
        label_D = MathTex("D").next_to(D, UL)
        label_E = MathTex("E").next_to(E, DOWN)
        label_F = MathTex("F").next_to(F, RIGHT)
        label_G = MathTex("G").next_to(G, LEFT)
        
        # Dimensions / Ratios
        # AE = 1/3 AB. Mark AE and EB? Or just text.
        # BF = 2/3 BC.
        # G midpoint AD.
        
        # Group
        scene_group = VGroup(rectangle, triangle_EFG, label_A, label_B, label_C, label_D, label_E, label_F, label_G)
        scene_group.move_to(ORIGIN)
        
        # Animations
        self.play(Create(rectangle), run_time=2)
        self.play(Create(triangle_EFG), run_time=2)
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Write(label_E), Write(label_F), Write(label_G))
        
        self.wait(2)
