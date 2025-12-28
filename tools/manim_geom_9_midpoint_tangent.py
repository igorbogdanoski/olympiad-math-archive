from manim import *

class Problem_geom_9_midpoint_tangent(Scene):
    def construct(self):
        # Scale everything up
        scale = 2.5
        
        # Circle at origin
        circle = Circle(radius=1 * scale, color=BLUE)
        
        # Points based on calculation
        # O at (2, 0)
        O_coord = np.array([2, 0, 0]) * scale
        # A at (0.5, -sqrt(3)/2)
        A_coord = np.array([0.5, -np.sqrt(3)/2, 0]) * scale
        # B at (0.5, sqrt(3)/2)
        B_coord = np.array([0.5, np.sqrt(3)/2, 0]) * scale
        # C at (-1, 0)
        C_coord = np.array([-1, 0, 0]) * scale
        # D at (1, 0)
        D_coord = np.array([1, 0, 0]) * scale
        
        # Midpoint M of OA
        M_coord = (O_coord + A_coord) / 2
        
        # Shift everything to center the view
        # Center of bounding box of O, C, B, A is roughly (0.5, 0)
        shift_vec = LEFT * 0.5 * scale
        
        circle.shift(shift_vec)
        O_coord += shift_vec
        A_coord += shift_vec
        B_coord += shift_vec
        C_coord += shift_vec
        D_coord += shift_vec
        M_coord += shift_vec
        
        # Define points
        O = Dot(O_coord, color=WHITE)
        A = Dot(A_coord, color=WHITE)
        B = Dot(B_coord, color=WHITE)
        C = Dot(C_coord, color=WHITE)
        D = Dot(D_coord, color=WHITE)
        M = Dot(M_coord, color=RED)
        
        # Lines
        line_OA = Line(O_coord, A_coord, color=YELLOW)
        line_OB = Line(O_coord, B_coord, color=YELLOW)
        line_BC = Line(B_coord, C_coord, color=GREEN)
        line_OC = Line(O_coord, C_coord, color=GRAY) # This is the x-axis in our setup
        line_BD = Line(B_coord, D_coord, color=RED)
        
        # Extend line BD to show it passes through M?
        # M is on OA. BD intersects OA at M.
        # Let's draw line BD extending a bit.
        line_BD_full = Line(B_coord, M_coord, color=RED)
        
        # Labels
        label_O = MathTex("O").next_to(O, RIGHT)
        label_A = MathTex("A").next_to(A, DR)
        label_B = MathTex("B").next_to(B, UR)
        label_C = MathTex("C").next_to(C, LEFT)
        label_D = MathTex("D").next_to(D, DL)
        label_M = MathTex("M").next_to(M, RIGHT)
        
        self.add(circle)
        self.add(line_OA, line_OB)
        self.add(line_BC)
        self.add(line_OC)
        self.add(line_BD_full)
        self.add(O, A, B, C, D, M)
        self.add(label_O, label_A, label_B, label_C, label_D, label_M)
        
        # Add parallel marker for BC and OA
        # BC is parallel to OA?
        # In our calc: OA slope tan(30) = 1/sqrt(3). BC slope tan(30). Yes.
        # Add arrows to show parallel
        arrow_OA = Arrow(line_OA.get_start(), line_OA.get_end(), color=YELLOW, tip_length=0.2).scale(0.5).move_to(line_OA.get_center())
        arrow_BC = Arrow(line_BC.get_end(), line_BC.get_start(), color=GREEN, tip_length=0.2).scale(0.5).move_to(line_BC.get_center())
        # Wait, BC direction vs OA direction.
        # OA goes right-down (from O to A).
        # BC goes right-up (from C to B).
        # They are parallel lines, but vectors might be anti-parallel or something.
        # Slope is same.
        
