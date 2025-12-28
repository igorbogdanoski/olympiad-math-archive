from manim import *

class Problem_geom_9_area_height(Scene):
    def construct(self):
        # Scale
        scale = 1.0
        
        # Parameters
        a = 4.0
        b = 6.0
        c = 2.4
        
        # Coordinates
        # C at origin
        C = ORIGIN
        # B on x-axis
        B = RIGHT * a
        # A at (x, y)
        # b^2 = x^2 + y^2
        # c^2 = (x-a)^2 + y^2 = x^2 - 2ax + a^2 + y^2 = b^2 - 2ax + a^2
        # 2ax = b^2 + a^2 - c^2
        # x = (a^2 + b^2 - c^2) / (2a)
        x_A = (a**2 + b**2 - c**2) / (2 * a)
        y_A = np.sqrt(b**2 - x_A**2)
        A = np.array([x_A, y_A, 0])
        
        # Shift to center
        center = (A + B + C) / 3
        shift = -center
        
        A += shift
        B += shift
        C += shift
        
        # Apply scale
        A *= scale
        B *= scale
        C *= scale
        
        # Objects
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        
        # Altitudes
        # h_a from A to BC
        # BC is on x-axis (before rotation/shift).
        # Let's compute altitudes properly using vector projection
        
        def get_altitude(P, Q, R):
            # Altitude from P to QR
            v_QR = R - Q
            v_QP = P - Q
            proj = np.dot(v_QP, v_QR) / np.dot(v_QR, v_QR) * v_QR
            foot = Q + proj
            return Line(P, foot, color=RED), foot
            
        alt_a, foot_a = get_altitude(A, B, C)
        alt_b, foot_b = get_altitude(B, C, A)
        alt_c, foot_c = get_altitude(C, A, B)
        
        # Labels
        label_A = MathTex("A").next_to(A, UP)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, DL)
        
        label_a = MathTex("a=4").next_to(Line(B, C), DOWN)
        label_b = MathTex("b=6").next_to(Line(A, C), UL)
        label_c = MathTex("c=2.4").next_to(Line(A, B), UR)
        
        label_ha = MathTex("h_a").next_to(alt_a, RIGHT, buff=0.05)
        label_hb = MathTex("h_b").next_to(alt_b, DOWN, buff=0.05)
        label_hc = MathTex("h_c").next_to(alt_c, UP, buff=0.05)
        
        # Text
        text = MathTex(
            r"h_c = h_a + h_b \implies \frac{1}{c} = \frac{1}{a} + \frac{1}{b}",
            r"\frac{1}{c} = \frac{1}{4} + \frac{1}{6} = \frac{5}{12} \implies c = 2.4",
            r"L = 4 + 6 + 2.4 = 12.4"
        ).arrange(DOWN).to_corner(UL)
        
        self.add(triangle)
        self.add(alt_a, alt_b, alt_c)
        self.add(label_A, label_B, label_C)
        self.add(label_a, label_b, label_c)
        self.add(label_ha, label_hb, label_hc)
        self.add(text)
