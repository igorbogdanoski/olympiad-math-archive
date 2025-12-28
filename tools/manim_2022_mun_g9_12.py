from manim import *

class Problem_2022_mun_g9_12(Scene):
    def construct(self):
        # Scale
        scale = 0.8
        
        # Parameters
        L = 16.0
        
        # Coordinates
        A = LEFT * L / 2
        B = RIGHT * L / 2
        
        # Point M: 3:5 ratio from A
        # AM = 3/8 * L = 3/8 * 16 = 6
        # M is at A + 6 * RIGHT
        M = A + RIGHT * 6
        
        # Point N: midpoint
        # AN = 1/2 * L = 8
        # N is at A + 8 * RIGHT
        N = A + RIGHT * 8
        
        # Shift to center
        # Already centered at origin (midpoint of AB is origin)
        # N is at origin.
        
        # Apply scale
        A *= scale
        B *= scale
        M *= scale
        N *= scale
        
        # Objects
        line = Line(A, B, color=BLUE)
        
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_M = Dot(M, color=RED)
        dot_N = Dot(N, color=GREEN)
        
        label_A = MathTex("A").next_to(dot_A, DOWN)
        label_B = MathTex("B").next_to(dot_B, DOWN)
        label_M = MathTex("M").next_to(dot_M, DOWN)
        label_N = MathTex("N").next_to(dot_N, DOWN)
        
        # Braces
        brace_AM = Brace(Line(A, M), UP)
        label_AM = brace_AM.get_text("6")
        
        brace_AN = Brace(Line(A, N), UP, buff=0.5)
        label_AN = brace_AN.get_text("8")
        
        brace_MN = Brace(Line(M, N), DOWN)
        label_MN = brace_MN.get_text("x")
        
        # Text
        text = MathTex(
            r"L = 16",
            r"AM = \frac{3}{8} \cdot 16 = 6",
            r"AN = \frac{1}{2} \cdot 16 = 8",
            r"MN = |AN - AM| = |8 - 6| = 2"
        ).arrange(DOWN).to_corner(UL)
        
        self.add(line)
        self.add(dot_A, dot_B, dot_M, dot_N)
        self.add(label_A, label_B, label_M, label_N)
        self.add(brace_AM, label_AM)
        self.add(brace_AN, label_AN)
        self.add(brace_MN, label_MN)
        self.add(text)
