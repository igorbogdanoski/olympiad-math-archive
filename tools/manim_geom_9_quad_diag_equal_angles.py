from manim import *

class Problem_geom_9_quad_diag_equal_angles(Scene):
    def construct(self):
        # Scale
        scale = 1.5
        
        # Parameters
        a = 2.5
        b = 1.5
        theta_deg = 70
        theta = theta_deg * DEGREES
        
        # Coordinates
        # P is origin
        P = ORIGIN
        A = LEFT * a
        B = RIGHT * b
        
        # D = (a cos theta, a sin theta)
        D = np.array([a * np.cos(theta), a * np.sin(theta), 0])
        
        # C = (-b cos theta, b sin theta)
        C = np.array([-b * np.cos(theta), b * np.sin(theta), 0])
        
        # Shift to center
        center = (A + B + C + D) / 4
        shift = -center
        
        A += shift
        B += shift
        C += shift
        D += shift
        P += shift
        
        # Scale
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        P *= scale
        
        # Objects
        quad = Polygon(A, B, C, D, color=BLUE)
        
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_D = Dot(D, color=WHITE)
        dot_P = Dot(P, color=RED)
        
        label_A = MathTex("A").next_to(dot_A, DL)
        label_B = MathTex("B").next_to(dot_B, DR)
        label_C = MathTex("C").next_to(dot_C, UP)
        label_D = MathTex("D").next_to(dot_D, UP)
        label_P = MathTex("P").next_to(dot_P, DOWN)
        
        # Diagonals
        diag_AC = Line(A, C, color=YELLOW)
        diag_BD = Line(B, D, color=YELLOW)
        
        # Perp bisectors
        # Midpoint AD
        M_AD = (A + D) / 2
        # Vector AD
        v_AD = D - A
        # Normal to AD
        n_AD = np.array([-v_AD[1], v_AD[0], 0])
        # Line through M_AD along n_AD
        # It should pass through P
        line_perp_AD = Line(M_AD + n_AD, M_AD - n_AD, color=GREEN).set_length(4)
        # Adjust length to go through P
        line_perp_AD = Line(P, M_AD + (M_AD-P)*0.5, color=GREEN)
        line_perp_AD_full = Line(P + (P-M_AD)*0.5, M_AD + (M_AD-P)*0.5, color=GREEN)

        # Midpoint BC
        M_BC = (B + C) / 2
        line_perp_BC_full = Line(P + (P-M_BC)*0.5, M_BC + (M_BC-P)*0.5, color=GREEN)
        
        # Mark right angles at midpoints
        ra_AD = RightAngle(Line(A, D), Line(P, M_AD), length=0.2)
        ra_BC = RightAngle(Line(B, C), Line(P, M_BC), length=0.2)
        
        self.add(quad)
        self.add(diag_AC, diag_BD)
        self.add(line_perp_AD_full, line_perp_BC_full)
        self.add(ra_AD, ra_BC)
        self.add(dot_A, dot_B, dot_C, dot_D, dot_P)
        self.add(label_A, label_B, label_C, label_D, label_P)
        
        # Add text
        text = MathTex(r"\angle DAB = \angle ABC").to_corner(UL)
        self.add(text)
