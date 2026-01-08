from manim import *
import numpy as np

class Problem_numerus_4331(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parameters
        x_deg = 20
        x_rad = x_deg * DEGREES
        a = 2.5 # Scale
        
        # Coordinates
        # C at origin
        C = np.array([0.0, 0.0, 0.0])
        B = np.array([a, 0.0, 0.0])
        
        # A is at (a, a * tan(60))
        # Angle ACB = 3x = 60 degrees
        y_A = a * np.tan(60 * DEGREES)
        A = np.array([a, y_A, 0.0])
        
        # M is on AB such that Angle MCB = x = 20
        y_M = a * np.tan(x_rad)
        M = np.array([a, y_M, 0.0])
        
        # K is on line through A parallel to BC (y = y_A)
        # And on line CM.
        # Line CM: y = x * tan(20).
        # y_K = y_A.
        # x_K = y_A / tan(20).
        x_K = y_A / np.tan(x_rad)
        K = np.array([x_K, y_A, 0.0])
        
        # L is midpoint of MK
        L = (M + K) / 2
        
        # Center the view
        center_of_mass = (C + K + A) / 3
        shift = -center_of_mass
        
        # Apply shift
        A += shift
        B += shift
        C += shift
        K += shift
        M += shift
        L += shift
        
        # Scale down if necessary to fit screen
        # Current width approx x_K = 2.5 * 1.73 / 0.36 = 12.
        # Screen width is 14. So it fits but tight.
        scale_factor = 0.8
        A *= scale_factor
        B *= scale_factor
        C *= scale_factor
        K *= scale_factor
        M *= scale_factor
        L *= scale_factor
        
        # Elements
        triangle_ABC = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        line_p = DashedLine(A + LEFT*1, K + RIGHT*1, color=GRAY)
        line_CK = Line(C, K, color=BLACK)
        line_AB_full = Line(B, A, color=BLACK) # Segment AB
        line_MK = Line(M, K, color=RED, stroke_width=4)
        line_AL = Line(A, L, color=GREEN)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, UP, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, DR, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, DL, buff=0.1)
        lbl_K = Text("K", font_size=24, color=BLACK).next_to(K, UP, buff=0.1)
        lbl_M = Text("M", font_size=24, color=BLACK).next_to(M, RIGHT, buff=0.1)
        lbl_L = Text("L", font_size=24, color=BLACK).next_to(L, UP, buff=0.1)
        
        # Angles
        angle_KCB = Angle(Line(C, B), Line(C, K), radius=1.5, color=ORANGE)
        lbl_x = MathTex("x", color=BLACK, font_size=20).next_to(angle_KCB, RIGHT, buff=0.1)
        
        angle_ACB = Angle(Line(C, B), Line(C, A), radius=0.8, color=BLUE)
        # lbl_3x = MathTex("3x", color=BLACK).next_to(angle_ACB, RIGHT, buff=0.1)
        
        # Right angle
        right_angle = RightAngle(Line(B, C), Line(B, A), length=0.3, color=BLACK)
        
        # Annotations
        # Mark AL = LK = LM
        # Tick marks
        tick_AL = Line(L, A).get_center()
        tick_LK = Line(L, K).get_center()
        tick_LM = Line(L, M).get_center()
        
        # Draw ticks
        def get_tick(point, angle):
            return Line(point + UP*0.1, point + DOWN*0.1, color=BLACK).rotate(angle)

        # Add to scene
        self.add(line_p)
        self.add(triangle_ABC)
        self.add(line_CK)
        self.add(line_MK)
        self.add(line_AL)
        self.add(lbl_A, lbl_B, lbl_C, lbl_K, lbl_M, lbl_L)
        self.add(angle_KCB, lbl_x)
        self.add(right_angle)
        
        # Add text info
        info = VGroup(
            MathTex("MK = 2AC", color=RED, font_size=24),
            MathTex(r"\\angle ACB = 3 \\angle KCB", color=BLACK, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
