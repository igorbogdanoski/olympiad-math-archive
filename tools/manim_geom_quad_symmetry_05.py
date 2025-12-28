from manim import *

class Problem_geom_quad_symmetry_05(Scene):
    def construct(self):
        # Scale
        scale = 1.0
        
        # Parameters
        b = 3.0
        p = 4.0
        
        # Coordinates
        C = ORIGIN
        B = UP * b
        P = RIGHT * p
        
        # Line PA has slope b/p (reflection of PB across vertical)
        # PB slope is -b/p.
        # Line PA: y = b/p * (x - p)
        
        # Find A such that angle BAP = angle ABC
        # Angle ABC:
        # Vector BC = (0, -b). Vector BA = A - B.
        # Angle beta.
        # Angle BAP:
        # Vector AB = B - A. Vector AP = P - A.
        # Angle beta.
        
        # Let's search for A
        # A = P + t * (1, b/p)
        # A = (p + t, t * b/p)
        # Let's iterate t
        
        def get_angle_diff(t):
            # A coordinates
            x_A = p + t
            y_A = t * b / p
            A_pt = np.array([x_A, y_A, 0])
            
            # Angle ABC
            v_BC = C - B
            v_BA = A_pt - B
            angle_ABC = angle_between_vectors(v_BC, v_BA)
            
            # Angle BAP
            v_AB = B - A_pt
            v_AP = P - A_pt
            angle_BAP = angle_between_vectors(v_AB, v_AP)
            
            return angle_BAP - angle_ABC

        # Binary search or simple scan
        # t must be negative? A is usually to the left?
        # If A is on segment PB', x > p.
        # If A is on other side, x < p.
        # Let's try range -10 to 10
        
        # Solve numerically
        from scipy.optimize import brentq
        try:
            t_sol = brentq(get_angle_diff, 0.1, 10) # Try positive t first
        except:
            try:
                t_sol = brentq(get_angle_diff, -10, -0.1)
            except:
                t_sol = 2.0 # Fallback
        
        x_A = p + t_sol
        y_A = t_sol * b / p
        A = np.array([x_A, y_A, 0])
        
        # D is on x-axis, to the right of P?
        # Problem says P is on CD.
        # So D is (d, 0) with d > p or d < 0?
        # Convex quadrilateral ABCD.
        # C(0,0), B(0,b).
        # If D is (d,0) with d > 0.
        # P is on CD. So P is between C and D?
        # If P is (p,0), then d > p.
        # Let's pick D at (p+2, 0).
        D = np.array([p + 2, 0, 0])
        
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
        
        label_A = MathTex("A").next_to(dot_A, UP)
        label_B = MathTex("B").next_to(dot_B, UL)
        label_C = MathTex("C").next_to(dot_C, DL)
        label_D = MathTex("D").next_to(dot_D, DR)
        label_P = MathTex("P").next_to(dot_P, DOWN)
        
        line_AP = Line(A, P, color=YELLOW)
        line_BP = Line(B, P, color=YELLOW)
        
        # Right angle at C
        right_angle = RightAngle(Line(C, B), Line(C, D), length=0.3, color=RED)
        
        self.add(quad)
        self.add(line_AP, line_BP)
        self.add(right_angle)
        self.add(dot_A, dot_B, dot_C, dot_D, dot_P)
        self.add(label_A, label_B, label_C, label_D, label_P)
        
        # Add text
        text = MathTex(r"BC = \frac{AP + BP}{2}").to_corner(UL)
        self.add(text)
