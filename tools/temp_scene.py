from manim import *

class Task_geom_9_sum_altitudes(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Equilateral triangle for symmetry looks nice, but prompt says "triangle ABC".
        # Let's use equilateral for clarity of "Viviani-like" setup, or generic.
        # Prompt says "triangle ABC".
        A = np.array([-2, -1.5, 0])
        B = np.array([3, -1.5, 0])
        C = np.array([0.5, 2.5, 0])
        
        tri = Polygon(A, B, C, color=BLUE)
        
        # Point M inside
        M = np.array([0.5, -0.5, 0])
        dot_M = Dot(M, color=BLACK)
        lbl_M = MathTex("M").next_to(M, UP, buff=0.1)
        
        # Perpendiculars to sides
        # To BC (x)
        vec_BC = C - B
        unit_BC = vec_BC / np.linalg.norm(vec_BC)
        # Normal vector to BC
        normal_BC = np.array([-unit_BC[1], unit_BC[0], 0])
        # Project M-B onto normal? No, just project M onto line BC.
        proj_x = B + np.dot(M - B, unit_BC) * unit_BC
        line_x = Line(M, proj_x, color=RED)
        lbl_x = MathTex("x", color=RED).next_to(line_x, RIGHT, buff=0.1)
        
        # To AC (y)
        vec_AC = C - A
        unit_AC = vec_AC / np.linalg.norm(vec_AC)
        proj_y = A + np.dot(M - A, unit_AC) * unit_AC
        line_y = Line(M, proj_y, color=RED)
        lbl_y = MathTex("y", color=RED).next_to(line_y, LEFT, buff=0.1)
        
        # To AB (z)
        proj_z = np.array([M[0], A[1], 0])
        line_z = Line(M, proj_z, color=RED)
        lbl_z = MathTex("z", color=RED).next_to(line_z, LEFT, buff=0.1)
        
        # Segments MA, MB, MC
        seg_MA = DashedLine(M, A, color=GRAY)
        seg_MB = DashedLine(M, B, color=GRAY)
        seg_MC = DashedLine(M, C, color=GRAY)
        
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP)
        
        self.add(tri, dot_M, lbl_M)
        self.add(line_x, lbl_x, line_y, lbl_y, line_z, lbl_z)
        self.add(seg_MA, seg_MB, seg_MC)
        self.add(lbl_A, lbl_B, lbl_C)


config.media_width = '100%'
config.verbosity = 'ERROR'
