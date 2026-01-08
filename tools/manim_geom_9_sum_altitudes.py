from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Define points
        A = np.array([-2, -1.5, 0])
        B = np.array([3, -1.5, 0])
        C = np.array([0.5, 2.5, 0])
        
        # Triangle
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=4)
        
        # Point M
        M = np.array([0.5, -0.5, 0])
        dot_M = Dot(M, color=YELLOW)
        label_M = MathTex("M").next_to(M, UP, buff=0.1)
        
        # Perpendiculars x, y, z
        # x to BC (a)
        # y to AC (b)
        # z to AB (c)
        
        def get_proj(P, A, B):
            vec_AB = B - A
            unit_AB = vec_AB / np.linalg.norm(vec_AB)
            return A + np.dot(P - A, unit_AB) * unit_AB
            
        proj_M_BC = get_proj(M, B, C)
        proj_M_AC = get_proj(M, A, C)
        proj_M_AB = get_proj(M, A, B)
        
        line_x = DashedLine(M, proj_M_BC, color=RED)
        line_y = DashedLine(M, proj_M_AC, color=RED)
        line_z = DashedLine(M, proj_M_AB, color=RED)
        
        label_x = MathTex("x").next_to(line_x, RIGHT, buff=0.05).scale(0.8)
        label_y = MathTex("y").next_to(line_y, LEFT, buff=0.05).scale(0.8)
        label_z = MathTex("z").next_to(line_z, LEFT, buff=0.05).scale(0.8)
        
        # Segments to vertices
        line_MA = DashedLine(M, A, color=GRAY)
        line_MB = DashedLine(M, B, color=GRAY)
        line_MC = DashedLine(M, C, color=GRAY)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, UP)
        
        # Areas
        area_MBC = Polygon(M, B, C, fill_opacity=0.2, fill_color=GREEN, stroke_width=0)
        area_MCA = Polygon(M, C, A, fill_opacity=0.2, fill_color=ORANGE, stroke_width=0)
        area_MAB = Polygon(M, A, B, fill_opacity=0.2, fill_color=PURPLE, stroke_width=0)
        
        # Equation
        equation = MathTex(r"\frrac{x}{h_a} + \frac{y}{h_b} + \frac{z}{h_c} = 1").to_corner(UL)
        
        # Group
        scene_group = VGroup(triangle, dot_M, label_M, line_x, line_y, line_z, label_x, label_y, label_z, line_MA, line_MB, line_MC, label_A, label_B, label_C, area_MBC, area_MCA, area_MAB, equation)
        scene_group.move_to(ORIGIN)
        
        # Animations
        self.play(Create(triangle), run_time=2)
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.play(Create(dot_M), Write(label_M))
        
        self.play(Create(line_x), Write(label_x))
        self.play(Create(line_y), Write(label_y))
        self.play(Create(line_z), Write(label_z))
        
        self.play(Create(line_MA), Create(line_MB), Create(line_MC))
        
        self.play(FadeIn(area_MBC))
        self.play(FadeIn(area_MCA))
        self.play(FadeIn(area_MAB))
        
        self.play(Write(equation))
        
        self.wait(2)
