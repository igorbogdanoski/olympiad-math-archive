from manim import *

class Problem_geom_9_contact_tri_sides(Scene):
    def construct(self):
        # Scale
        scale = 1.5
        
        # Coordinates
        # Right triangle 3-4-5
        C = ORIGIN
        A = RIGHT * 4
        B = UP * 3
        
        # Incenter
        r = 1.0
        I = np.array([r, r, 0])
        
        # Contact points
        # On AC (y=0)
        N = np.array([r, 0, 0])
        # On BC (x=0)
        M = np.array([0, r, 0])
        # On AB
        # P calculation from thought process
        P = np.array([1.6, 1.8, 0])
        
        # Shift to center
        center = (A + B + C) / 3
        shift = -center
        
        A += shift
        B += shift
        C += shift
        I += shift
        M += shift
        N += shift
        P += shift
        
        # Scale
        A *= scale
        B *= scale
        C *= scale
        I *= scale
        M *= scale
        N *= scale
        P *= scale
        r *= scale
        
        # Objects
        triangle = Polygon(A, B, C, color=BLUE)
        incircle = Circle(radius=r, color=GREEN).move_to(I)
        contact_tri = Polygon(M, N, P, color=RED, fill_opacity=0.2)
        
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_M = Dot(M, color=RED)
        dot_N = Dot(N, color=RED)
        dot_P = Dot(P, color=RED)
        
        label_A = MathTex("A").next_to(dot_A, DR)
        label_B = MathTex("B").next_to(dot_B, UL)
        label_C = MathTex("C").next_to(dot_C, DL)
        label_M = MathTex("M").next_to(dot_M, LEFT)
        label_N = MathTex("N").next_to(dot_N, DOWN)
        label_P = MathTex("P").next_to(dot_P, UR)
        
        # Add text
        text = MathTex(r"\triangle MNP").to_corner(UL).set_color(RED)
        
        self.add(triangle)
        self.add(incircle)
        self.add(contact_tri)
        self.add(dot_A, dot_B, dot_C, dot_M, dot_N, dot_P)
        self.add(label_A, label_B, label_C, label_M, label_N, label_P)
        self.add(text)
