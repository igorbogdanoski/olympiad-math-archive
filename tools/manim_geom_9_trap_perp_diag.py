from manim import *

class Problem_geom_9_trap_perp_diag(Scene):
    def construct(self):
        # Parameters
        m = 6
        # Let a = 4, c = 2 so a+c=6
        a = 4
        c = 2
        
        # Scale down to fit screen
        scale = 0.6
        a_s = a * scale
        c_s = c * scale
        
        # Coordinates
        # Diagonals intersect at origin
        O = ORIGIN
        
        # A = (-a, -a), B = (a, -a)
        A = np.array([-a_s, -a_s, 0])
        B = np.array([a_s, -a_s, 0])
        
        # C = (c, c), D = (-c, c)
        C = np.array([c_s, c_s, 0])
        D = np.array([-c_s, c_s, 0])
        
        # Create trapezoid
        trapezoid = Polygon(A, B, C, D, color=BLUE, stroke_width=4)
        
        # Diagonals
        diag_AC = Line(A, C, color=YELLOW)
        diag_BD = Line(B, D, color=YELLOW)
        
        # Right angle marker at O
        right_angle = RightAngle(Line(O, C), Line(O, B), length=0.3, color=RED)
        
        # Median
        # Midpoint of AD
        M_AD = (A + D) / 2
        # Midpoint of BC
        M_BC = (B + C) / 2
        median_line = Line(M_AD, M_BC, color=GREEN, stroke_width=4)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, UR)
        label_D = MathTex("D").next_to(D, UL)
        
        label_m = MathTex("m = 6").next_to(median_line, UP, buff=0.1).set_color(GREEN)
        
        # Height line
        # Draw height through O? Or on the side?
        # Let's draw height on the side
        H_top = np.array([c_s + 1, c_s, 0])
        H_bot = np.array([c_s + 1, -a_s, 0])
        height_line = DashedLine(H_top, H_bot, color=WHITE)
        label_h = MathTex("h").next_to(height_line, RIGHT)
        
        # Add text
        text_area = MathTex("P = m \cdot h = m^2 = 36").to_edge(UP)
        
        self.add(trapezoid)
        self.add(diag_AC, diag_BD)
        self.add(right_angle)
        self.add(median_line)
        self.add(label_A, label_B, label_C, label_D)
        self.add(label_m)
        self.add(height_line, label_h)
        self.add(text_area)
