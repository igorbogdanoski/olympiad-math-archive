from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Parameters
        x = 115
        angle_PQT = x * DEGREES
        angle_RQT = (x - 50) * DEGREES
        angle_TUR = (x + 25) * DEGREES
        
        # Coordinates
        # Q at origin
        Q = ORIGIN
        # Line PS is horizontal
        P = LEFT * 3
        R = RIGHT * 2
        S = RIGHT * 4
        
        # T is determined by angle RQT = 65
        # T is above the line.
        # Angle of QT with QR (Right) is 65.
        dist_QT = 2.5
        T = Q + dist_QT * np.array([np.cos(angle_RQT), np.sin(angle_RQT), 0])
        
        # Line TU is parallel to PS, so horizontal.
        # U is on the line y = T.y
        # Angle TUR = 140.
        # UT is to the left.
        # Angle between UT (Left) and UR is 140.
        # So UR points Down-Right.
        # Angle of UR with Right is 40.
        # So U is to the left of R?
        # Let's calculate U position relative to R.
        # R is fixed. U is on line y = T.y.
        # Slope of RU is tan(140) relative to Right? No.
        # Angle of RU with Right is 140.
        # So slope is tan(140).
        # y_U - y_R = tan(140) * (x_U - x_R)
        # T.y - 0 = tan(140) * (x_U - 2)
        # x_U = 2 + T.y / tan(140 * DEGREES)
        
        y_U = T[1]
        # tan(140) is negative.
        x_U = R[0] + y_U / np.tan(140 * DEGREES)
        U = np.array([x_U, y_U, 0])
        
        # Create objects
        line_PS = Line(P, S, color=WHITE)
        line_TU_full = Line(T + LEFT*1, U + RIGHT*1, color=WHITE) # Extend a bit
        
        line_QT = Line(Q, T, color=YELLOW)
        line_UR = Line(U, R, color=YELLOW)
        
        # Dots
        dot_P = Dot(P)
        dot_Q = Dot(Q)
        dot_R = Dot(R)
        dot_S = Dot(S)
        dot_T = Dot(T)
        dot_U = Dot(U)
        
        # Labels
        label_P = MathTex("P").next_to(P, DOWN)
        label_Q = MathTex("Q").next_to(Q, DOWN)
        label_R = MathTex("R").next_to(R, DOWN)
        label_S = MathTex("S").next_to(S, DOWN)
        label_T = MathTex("T").next_to(T, UP)
        label_U = MathTex("U").next_to(U, UP)
        
        # Angles
        # PQT
        angle_PQT_arc = Angle(Line(Q, P), line_QT, radius=0.5, color=RED)
        label_x = MathTex("x").next_to(angle_PQT_arc, UP+LEFT)
        
        # RQT
        angle_RQT_arc = Angle(line_QT, Line(Q, R), radius=0.6, color=BLUE)
        label_x_50 = MathTex("x-50").next_to(angle_RQT_arc, UP+RIGHT)
        
        # TUR
        # Angle between UT and UR
        angle_TUR_arc = Angle(Line(U, T), line_UR, radius=0.6, color=GREEN)
        label_x_25 = MathTex("x+25").next_to(angle_TUR_arc, DOWN+LEFT)
        
        # URS
        angle_URS_arc = Angle(line_UR, Line(R, S), radius=0.6, color=ORANGE)
        label_q = MathTex("?").next_to(angle_URS_arc, UP+RIGHT)
        
        # Grouping
        scene_objects = VGroup(
            line_PS, line_TU_full, line_QT, line_UR,
            dot_P, dot_Q, dot_R, dot_S, dot_T, dot_U,
            label_P, label_Q, label_R, label_S, label_T, label_U,
            angle_PQT_arc, label_x,
            angle_RQT_arc, label_x_50,
            angle_TUR_arc, label_x_25,
            angle_URS_arc, label_q
        )
        
        # Scale to fit
        scene_objects.scale(0.8)
        scene_objects.move_to(ORIGIN + LEFT * 2)
        
        # Explanation text
        text_group = VGroup(
            MathTex(r"\angle PQT + \angle RQT = 180^\circ"),
            MathTex(r"x + (x - 50) = 180"),
            MathTex(r"2x = 230 \implies x = 115^\circ"),
            MathTex(r"\angle TUR = x + 25 = 140^\circ"),
            MathTex(r"TU \parallel PS \implies \angle TUR = \angle URS"),
            MathTex(r"\text{(Alternate Interior Angles)}"),
            MathTex(r"\angle URS = 140^\circ")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.8)
        
        self.add(scene_objects)
        self.add(text_group)
