from manim import *

class Problem_numerus_4420(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Rectangle ABCD
        # BC = 2 * AB.
        # Let AB = 2. Then BC = 4.
        # A at (-2, -1), B at (-2, 1), C at (2, 1), D at (2, -1).
        # Wait, AB is height?
        # AB = 2. BC = 4.
        # A(-2, -1), B(-2, 1). Length = 2.
        # B(-2, 1), C(2, 1). Length = 4.
        # C(2, 1), D(2, -1). Length = 2.
        # D(2, -1), A(-2, -1). Length = 4.
        # Correct.
        
        A = np.array([-2, -1, 0])
        B = np.array([-2, 1, 0])
        C = np.array([2, 1, 0])
        D = np.array([2, -1, 0])
        
        rect = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        
        # Point P on AD.
        # AD is the bottom side? No, AD is side from A to D.
        # A(-2, -1), D(2, -1).
        # AD length is 4.
        # P is on AD such that AD = BP.
        # AD = 4. So BP = 4.
        # B is at (-2, 1).
        # P is on line AD (y = -1).
        # P = (x, -1).
        # Distance BP = 4.
        # (x - (-2))^2 + (-1 - 1)^2 = 4^2.
        # (x + 2)^2 + (-2)^2 = 16.
        # (x + 2)^2 + 4 = 16.
        # (x + 2)^2 = 12.
        # x + 2 = sqrt(12) or -sqrt(12).
        # x = -2 + 2*sqrt(3) or -2 - 2*sqrt(3).
        # P is on side AD. Side AD is from x=-2 to x=2.
        # x must be between -2 and 2.
        # -2 + 2*sqrt(3) approx -2 + 3.46 = 1.46. (Inside)
        # -2 - 2*sqrt(3) approx -5.46. (Outside)
        # So P is at (-2 + 2*sqrt(3), -1).
        
        x_p = -2 + 2 * np.sqrt(3)
        P = np.array([x_p, -1, 0])
        
        # Find Angle CPD.
        # P is on AD. D is at (2, -1).
        # C is at (2, 1).
        # Triangle PCD is a right triangle at D?
        # P, D are on y=-1. C is at (2, 1).
        # CD is vertical segment from (2, 1) to (2, -1). Length 2.
        # PD is horizontal segment from P to D.
        # Length PD = 2 - x_p = 2 - (-2 + 2*sqrt(3)) = 4 - 2*sqrt(3).
        # Tan(Angle CPD) = CD / PD = 2 / (4 - 2*sqrt(3)) = 1 / (2 - sqrt(3)).
        # 1 / (2 - sqrt(3)) = 2 + sqrt(3).
        # Tan(75 deg) = 2 + sqrt(3).
        # So Angle CPD = 75 degrees.
        
        # Visualization
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, DL, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, UL, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, UR, buff=0.1)
        lbl_D = Text("D", font_size=24, color=BLACK).next_to(D, DR, buff=0.1)
        lbl_P = Text("P", font_size=24, color=BLACK).next_to(P, DOWN, buff=0.1)
        
        line_BP = Line(B, P, color=RED)
        line_CP = Line(C, P, color=GREEN)
        
        # Angle Mark
        angle_mark = Angle(Line(P, D), Line(P, C), radius=0.5, color=ORANGE)
        lbl_angle = MathTex("?", color=ORANGE).next_to(angle_mark, UL, buff=0.05)
        
        # Text
        text_cond = MathTex("BC = 2AB", color=BLACK).to_corner(UL)
        text_cond2 = MathTex("BP = AD", color=BLACK).next_to(text_cond, DOWN, aligned_edge=LEFT)
        
        self.add(rect)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_P)
        self.add(line_BP, line_CP)
        self.add(angle_mark, lbl_angle)
        self.add(text_cond, text_cond2)
