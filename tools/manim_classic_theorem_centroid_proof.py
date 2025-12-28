from manim import *

class Problem_classic_theorem_centroid_proof(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Triangle ABC
        A = np.array([-2, -1.5, 0])
        B = np.array([3, -1.5, 0])
        C = np.array([0, 2.5, 0])
        
        tri = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        
        # Midpoints
        Ma = (B + C) / 2
        Mb = (A + C) / 2
        Mc = (A + B) / 2
        
        # Medians
        median_A = Line(A, Ma, color=RED)
        median_B = Line(B, Mb, color=GREEN)
        median_C = Line(C, Mc, color=ORANGE)
        
        # Centroid G
        G = (A + B + C) / 3
        dot_G = Dot(G, color=BLACK)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, DL, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, DR, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, UP, buff=0.1)
        
        lbl_Ma = Text("Ma", font_size=20, color=BLACK).next_to(Ma, RIGHT, buff=0.1)
        lbl_Mb = Text("Mb", font_size=20, color=BLACK).next_to(Mb, LEFT, buff=0.1)
        lbl_Mc = Text("Mc", font_size=20, color=BLACK).next_to(Mc, DOWN, buff=0.1)
        
        lbl_G = Text("G", font_size=24, color=BLACK).next_to(G, UR, buff=0.05)
        
        self.add(tri)
        self.add(median_A, median_B, median_C)
        self.add(dot_G)
        self.add(lbl_A, lbl_B, lbl_C, lbl_Ma, lbl_Mb, lbl_Mc, lbl_G)
        
        # Text
        text = MathTex(r"\text{Medians intersect at } G", color=BLACK).to_corner(UL)
        self.add(text)
