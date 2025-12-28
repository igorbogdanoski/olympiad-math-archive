from manim import *

class Problem_geom_9_quad_parallel_proof(Scene):
    def construct(self):
        # Scale
        scale = 1.0
        
        # Coordinates
        # AD parallel to BC
        # AD on top, BC on bottom
        y_top = 2.0
        y_bot = -2.0
        
        A = np.array([-1.0, y_top, 0.0])
        D = np.array([2.0, y_top, 0.0])
        
        B = np.array([-2.0, y_bot, 0.0])
        C = np.array([5.0, y_bot, 0.0])
        
        # Midpoints
        M = (A + B) / 2
        N = (C + D) / 2
        
        # Shift to center
        center = (A + B + C + D) / 4
        shift = -center
        
        A += shift
        B += shift
        C += shift
        D += shift
        M += shift
        N += shift
        
        # Scale
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        M *= scale
        N *= scale
        
        # Objects
        quad = Polygon(A, B, C, D, color=BLUE)
        line_MN = Line(M, N, color=YELLOW)
        
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_D = Dot(D, color=WHITE)
        dot_M = Dot(M, color=RED)
        dot_N = Dot(N, color=RED)
        
        label_A = MathTex("A").next_to(dot_A, UL)
        label_B = MathTex("B").next_to(dot_B, DL)
        label_C = MathTex("C").next_to(dot_C, DR)
        label_D = MathTex("D").next_to(dot_D, UR)
        label_M = MathTex("M").next_to(dot_M, LEFT)
        label_N = MathTex("N").next_to(dot_N, RIGHT)
        
        # Add text
        text_cond = MathTex(r"MN = \frac{AD + BC}{2}").to_corner(UL)
        text_res = MathTex(r"\Rightarrow AD \parallel BC").next_to(text_cond, DOWN).set_color(YELLOW)
        
        self.add(quad)
        self.add(line_MN)
        self.add(dot_A, dot_B, dot_C, dot_D, dot_M, dot_N)
        self.add(label_A, label_B, label_C, label_D, label_M, label_N)
        self.add(text_cond, text_res)
