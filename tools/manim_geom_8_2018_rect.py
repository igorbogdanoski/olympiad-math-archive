from manim import *
import numpy as np

class RectangleTriangleArea(Scene):
    def construct(self):
        # Parameters
        AB = 9 # Scaled down by 2 (18 -> 9)
        BC = 6 # Scaled down by 2 (12 -> 6)
        
        # Coordinates
        # A bottom-left
        A = ORIGIN
        B = RIGHT * AB
        C = RIGHT * AB + UP * BC
        D = UP * BC
        
        # Points
        # AE = 1/3 AB -> 3
        E = RIGHT * (AB / 3)
        # BF = 2/3 BC -> 4
        F = B + UP * (BC * 2/3)
        # G midpoint AD -> 3
        G = UP * (BC / 2)
        
        # Create points
        pA = Dot(A)
        pB = Dot(B)
        pC = Dot(C)
        pD = Dot(D)
        pE = Dot(E)
        pF = Dot(F)
        pG = Dot(G)
        
        # Shapes
        rect = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        triangle = Polygon(E, F, G, color=YELLOW, fill_opacity=0.4)
        
        # Labels
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP+RIGHT)
        lbl_D = MathTex("D").next_to(D, UP+LEFT)
        lbl_E = MathTex("E").next_to(E, DOWN)
        lbl_F = MathTex("F").next_to(F, RIGHT)
        lbl_G = MathTex("G").next_to(G, LEFT)
        
        # Dimensions
        # AB = 18, BC = 12
        # AE = 6, EB = 12
        # BF = 8, FC = 4
        # AG = 6, GD = 6
        
        lbl_AE = MathTex("6").next_to(Line(A,E), DOWN)
        lbl_EB = MathTex("12").next_to(Line(E,B), DOWN)
        lbl_BF = MathTex("8").next_to(Line(B,F), RIGHT)
        lbl_FC = MathTex("4").next_to(Line(F,C), RIGHT)
        lbl_AG = MathTex("6").next_to(Line(A,G), LEFT)
        lbl_GD = MathTex("6").next_to(Line(G,D), LEFT)
        
        # Group
        scene_objects = VGroup(
            rect, triangle,
            lbl_A, lbl_B, lbl_C, lbl_D, lbl_E, lbl_F, lbl_G,
            lbl_AE, lbl_EB, lbl_BF, lbl_FC, lbl_AG, lbl_GD
        )
        
        scene_objects.scale(0.7)
        scene_objects.shift(LEFT * 2.5)
        
        # Text
        text = VGroup(
            MathTex(r"P = 2(AB + BC) = 60 \implies AB + BC = 30"),
            MathTex(r"BC = \frac{2}{3}AB \implies AB + \frac{2}{3}AB = 30 \implies AB = 18, BC = 12"),
            MathTex(r"AE = \frac{1}{3}AB = 6, \quad EB = 12"),
            MathTex(r"BF = \frac{2}{3}BC = 8, \quad FC = 4"),
            MathTex(r"AG = GD = 6"),
            MathTex(r"Area(EFG) = Area(ABCD) - \sum Area(\text{corners})"),
            MathTex(r"Area(ABCD) = 18 \cdot 12 = 216"),
            MathTex(r"Area(AGE) = \frac{1}{2} \cdot 6 \cdot 6 = 18"),
            MathTex(r"Area(EBF) = \frac{1}{2} \cdot 12 \cdot 8 = 48"),
            MathTex(r"Area(GDCF) = \frac{6+4}{2} \cdot 18 = 90"),
            MathTex(r"Area(EFG) = 216 - (18 + 48 + 90) = 216 - 156 = 60")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.6)
        
        self.add(scene_objects)
        self.add(text)
