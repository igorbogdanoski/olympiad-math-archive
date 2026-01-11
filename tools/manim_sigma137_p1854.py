from manim import *
import numpy as np

class EquilateralTriangleRotationScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        title = Text("Рамностран триаголник и ротација", font_size=36, color=DARK_BLUE)
        title.to_edge(UP)
        self.add(title)
        
        A = np.array([-2, -1.5, 0])
        B = np.array([2, -1.5, 0])
        C = np.array([0, 1.5, 0])
        
        triangle_ABC = Polygon(A, B, C, color=BLUE, stroke_width=2)
        self.add(triangle_ABC)
        
        F = A + 0.4 * (B - A)
        E = A + 0.4 * (C - A)
        
        triangle_AFE = Polygon(A, F, E, color=GREEN, stroke_width=2, fill_opacity=0.1, fill_color=GREEN)
        self.add(triangle_AFE)
        
        dot_A = Dot(A, color=BLACK, radius=0.1)
        dot_B = Dot(B, color=BLACK, radius=0.1)
        dot_C = Dot(C, color=BLACK, radius=0.1)
        dot_F = Dot(F, color=GREEN, radius=0.08)
        dot_E = Dot(E, color=GREEN, radius=0.08)
        
        self.add(dot_A, dot_B, dot_C, dot_F, dot_E)
        
        lbl_A = Text("A", font_size=20, color=BLACK).next_to(A, LEFT, buff=0.15)
        lbl_B = Text("B", font_size=20, color=BLACK).next_to(B, RIGHT, buff=0.15)
        lbl_C = Text("C", font_size=20, color=BLACK).next_to(C, UP, buff=0.15)
        lbl_F = Text("F", font_size=16, color=GREEN).next_to(F, DOWN, buff=0.1)
        lbl_E = Text("E", font_size=16, color=GREEN).next_to(E, LEFT, buff=0.1)
        
        self.add(lbl_A, lbl_B, lbl_C, lbl_F, lbl_E)
        
        G = (A + F + E) / 3
        dot_G = Dot(G, color=RED, radius=0.08)
        lbl_G = Text("G (тежиште)", font_size=14, color=RED).next_to(G, DOWN, buff=0.1)
        
        self.add(dot_G, lbl_G)
        
        M_mid = (B + E) / 2
        dot_M = Dot(M_mid, color=PURPLE, radius=0.08)
        lbl_M = Text("M (средина на BE)", font_size=14, color=PURPLE).next_to(M_mid, RIGHT, buff=0.1)
        
        self.add(dot_M, lbl_M)
        
        line_BE = Line(B, E, color=PURPLE, stroke_width=1.5)
        self.add(line_BE)
        
        parallel_line = Line(E - 0.5, F + 0.5, color=GRAY, stroke_width=1)
        self.add(parallel_line)
        
        info_text = Text("EF ║ BC", font_size=18, color=GRAY).shift(DOWN * 3)
        self.add(info_text)
