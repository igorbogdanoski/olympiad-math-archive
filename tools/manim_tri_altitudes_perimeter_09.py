from manim import *

class Problem_tri_altitudes_perimeter_09(Scene):
    def construct(self):
        # Sides
        a = 4
        b = 6
        c = 2.4
        
        # Scale
        scale = 1.0
        a_s = a * scale
        b_s = b * scale
        c_s = c * scale
        
        # Coordinates
        # A at origin
        A = ORIGIN
        # B at (c, 0)
        B = RIGHT * c_s
        
        # Calculate C
        # x = (b^2 + c^2 - a^2) / (2c)
        # x = (36 + 5.76 - 16) / 4.8 = 25.76 / 4.8 = 5.3666
        x_C = (b_s**2 + c_s**2 - a_s**2) / (2 * c_s)
        y_C = np.sqrt(b_s**2 - x_C**2)
        C = np.array([x_C, y_C, 0])
        
        # Shift to center
        center = (A + B + C) / 3
        shift = -center
        A += shift
        B += shift
        C += shift
        
        # Create triangle
        triangle = Polygon(A, B, C, color=BLUE)
        
        # Altitudes
        # h_a from A to BC
        # Project A onto line BC
        v_BC = C - B
        unit_BC = v_BC / np.linalg.norm(v_BC)
        proj_A = B + np.dot(A - B, unit_BC) * unit_BC
        h_a_line = DashedLine(A, proj_A, color=YELLOW)
        
        # h_b from B to AC
        v_AC = C - A
        unit_AC = v_AC / np.linalg.norm(v_AC)
        proj_B = A + np.dot(B - A, unit_AC) * unit_AC
        h_b_line = DashedLine(B, proj_B, color=YELLOW)
        
        # h_c from C to AB
        # AB is horizontal (before rotation/shift), but after shift it's still parallel to x-axis?
        # No, shift preserves orientation. AB was on x-axis.
        # So h_c is vertical distance.
        # Project C onto line AB
        v_AB = B - A
        unit_AB = v_AB / np.linalg.norm(v_AB)
        proj_C = A + np.dot(C - A, unit_AB) * unit_AB
        h_c_line = DashedLine(C, proj_C, color=YELLOW)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, UP)
        
        label_ha = MathTex("h_a").next_to(h_a_line, LEFT, buff=0.05).scale(0.7)
        label_hb = MathTex("h_b").next_to(h_b_line, DOWN, buff=0.05).scale(0.7)
        label_hc = MathTex("h_c").next_to(h_c_line, RIGHT, buff=0.05).scale(0.7)
        
        # Side labels
        label_a = MathTex("a=4").next_to(Line(B, C).get_center(), RIGHT)
        label_b = MathTex("b=6").next_to(Line(A, C).get_center(), UP)
        label_c_val = MathTex("c=2.4").next_to(Line(A, B).get_center(), DOWN)
        
        # Equation
        eq = MathTex("h_c = h_a + h_b").to_corner(UL)
        res = MathTex("L = 12.4").next_to(eq, DOWN).set_color(YELLOW)
        
        self.add(triangle)
        self.add(h_a_line, h_b_line, h_c_line)
        self.add(label_A, label_B, label_C)
        self.add(label_ha, label_hb, label_hc)
        self.add(label_a, label_b, label_c_val)
        self.add(eq, res)
