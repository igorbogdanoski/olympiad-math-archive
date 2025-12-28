from manim import *

class Problem_geom_9_touching_circles_tangent(Scene):
    def construct(self):
        # Parameters
        R = 2.0
        r = 1.0
        rho = r * (r + R) / R  # 1.5
        
        # Coordinates
        # Shift everything so the scene is centered
        # O2 is at origin initially
        O2_pos = ORIGIN
        O1_pos = LEFT * (r + R)
        M_pos = LEFT * r
        N_pos = RIGHT * r
        
        # O3 calculation
        # x_3 = r - rho
        # y_3 = sqrt(4 * r * rho)
        y3 = np.sqrt(4 * r * rho)
        O3_pos = np.array([r - rho, y3, 0])
        
        # Tangent line t is x = r
        # We'll draw a vertical line at x = r
        
        # Create objects
        k1 = Circle(radius=R, color=BLUE).move_to(O1_pos)
        k2 = Circle(radius=r, color=GREEN).move_to(O2_pos)
        k3 = Circle(radius=rho, color=RED).move_to(O3_pos)
        
        line_t = Line(np.array([r, -3, 0]), np.array([r, 4, 0]), color=YELLOW)
        
        # Points
        dot_O1 = Dot(O1_pos)
        dot_O2 = Dot(O2_pos)
        dot_O3 = Dot(O3_pos)
        dot_M = Dot(M_pos)
        dot_N = Dot(N_pos)
        
        # Labels
        label_k1 = MathTex("k_1").next_to(k1, UP)
        label_k2 = MathTex("k_2").next_to(k2, DOWN)
        label_k3 = MathTex("k_3").next_to(k3, UP)
        label_t = MathTex("t").next_to(line_t, RIGHT, buff=0.1).shift(UP*2)
        
        label_M = MathTex("M").next_to(dot_M, DL, buff=0.1).scale(0.7)
        label_N = MathTex("N").next_to(dot_N, DR, buff=0.1).scale(0.7)
        
        # Group and center
        group = VGroup(k1, k2, k3, line_t, dot_O1, dot_O2, dot_O3, dot_M, dot_N, 
                       label_k1, label_k2, label_k3, label_t, label_M, label_N)
        group.move_to(ORIGIN)
        
        self.add(k1, k2, k3, line_t)
        self.add(dot_M, dot_N)
        self.add(label_k1, label_k2, label_k3, label_t, label_M, label_N)
        
        # Add radius labels? Maybe too cluttered.
        # Just the main elements.
