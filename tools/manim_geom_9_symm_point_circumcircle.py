from manim import *

class Problem_geom_9_symm_point_circumcircle(Scene):
    def construct(self):
        # Scale
        scale = 2.5
        
        # Define A, B, C on unit circle
        # Let A be at 90 degrees (top)
        A_angle = 90 * DEGREES
        # Let B be at 210 degrees
        B_angle = 210 * DEGREES
        # Let C be at 330 degrees
        C_angle = 330 * DEGREES
        
        # Adjust angles to make it non-equilateral but acute
        # A at 80 deg
        A_angle = 100 * DEGREES
        # B at 220 deg
        B_angle = 220 * DEGREES
        # C at 320 deg
        C_angle = 320 * DEGREES
        
        # Coordinates
        A = np.array([np.cos(A_angle), np.sin(A_angle), 0]) * scale
        B = np.array([np.cos(B_angle), np.sin(B_angle), 0]) * scale
        C = np.array([np.cos(C_angle), np.sin(C_angle), 0]) * scale
        
        # Circumcircle
        circumcircle = Circle(radius=scale, color=BLUE)
        
        # Calculate Angle A (BAC)
        # Vectors AB and AC
        vec_AB = B - A
        vec_AC = C - A
        angle_A = angle_between_vectors(vec_AB, vec_AC)
        # Convert to degrees for check
        angle_A_deg = np.rad2deg(angle_A)
        
        # Find D
        # Center O1 for circle ADB
        # Triangle AO1B is isosceles with angle at O1 = 2*A
        # Height of O1 from AB
        # Midpoint of AB
        M_AB = (A + B) / 2
        # Vector AB
        v_AB = B - A
        # Perpendicular vector
        perp_AB = np.array([-v_AB[1], v_AB[0], 0])
        # Normalize
        perp_AB = perp_AB / np.linalg.norm(perp_AB)
        
        # Distance from M_AB to O1
        # tan(angle_A) = (AB/2) / h? No.
        # In triangle AO1M: angle at O1 is A. Angle at A is 90-A.
        # tan(90-A) = cot(A) = h / (AB/2).
        # h = (AB/2) * cot(A).
        # Direction: Towards C? Or away?
        # Angle ADB = 180 - A. D is on the side of C?
        # If D is inside, it is on same side of AB as C.
        # Center O1 should be on the other side?
        # If angle is obtuse (180-A), center is on the opposite side of chord AB than the point D.
        # So O1 is on the side away from C.
        
        dist_AB = np.linalg.norm(v_AB)
        h1 = (dist_AB / 2) * (1 / np.tan(angle_A))
        
        # We need to determine direction of perp_AB.
        # Check dot product with C-M_AB.
        if np.dot(perp_AB, C - M_AB) > 0:
            # perp_AB points towards C. We want away.
            perp_AB = -perp_AB
            
        O1 = M_AB + perp_AB * h1
        radius_1 = np.linalg.norm(A - O1)
        
        # Center O2 for circle CDA
        # Triangle CO2A is isosceles with angle at O2 = 2*A
        M_AC = (A + C) / 2
        v_AC = C - A
        perp_AC = np.array([-v_AC[1], v_AC[0], 0])
        perp_AC = perp_AC / np.linalg.norm(perp_AC)
        
        dist_AC = np.linalg.norm(v_AC)
        h2 = (dist_AC / 2) * (1 / np.tan(angle_A))
        
        # Direction away from B
        if np.dot(perp_AC, B - M_AC) > 0:
            perp_AC = -perp_AC
            
        O2 = M_AC + perp_AC * h2
        radius_2 = np.linalg.norm(A - O2)
        
        # Intersect circles (O1, r1) and (O2, r2)
        # One intersection is A. Find the other.
        # Reflection of A across line O1O2.
        # Project A onto O1O2.
        v_O1O2 = O2 - O1
        unit_O1O2 = v_O1O2 / np.linalg.norm(v_O1O2)
        proj = O1 + np.dot(A - O1, unit_O1O2) * unit_O1O2
        D = 2 * proj - A
        
        # Calculate A'
        A_prime = 2 * D - A
        
        # Create objects
        triangle = Polygon(A, B, C, color=WHITE)
        
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_D = Dot(D, color=RED)
        dot_A_prime = Dot(A_prime, color=YELLOW)
        
        line_ADA = Line(A, A_prime, color=YELLOW)
        line_DB = Line(D, B, color=GRAY)
        line_DC = Line(D, C, color=GRAY)
        
        label_A = MathTex("A").next_to(dot_A, UP)
        label_B = MathTex("B").next_to(dot_B, DL)
        label_C = MathTex("C").next_to(dot_C, DR)
        label_D = MathTex("D").next_to(dot_D, DOWN)
        label_A_prime = MathTex("A'").next_to(dot_A_prime, DOWN)
        
        self.add(circumcircle)
        self.add(triangle)
        self.add(line_ADA, line_DB, line_DC)
        self.add(dot_A, dot_B, dot_C, dot_D, dot_A_prime)
        self.add(label_A, label_B, label_C, label_D, label_A_prime)
        
        # Add text
        text = MathTex(r"A' \in k").to_corner(UL)
        self.add(text)
