from manim import *

class QuadrilateralArea(Scene):
    def construct(self):
        # Parameters
        AB_len = 6
        AD_len = 4
        # A at origin
        A = ORIGIN
        B = RIGHT * AB_len
        D = UP * AD_len
        
        # C calculation
        # Midpoint of BD
        M = (B + D) / 2
        # Vector BD
        vec_BD = D - B
        # Perpendicular vector (rotate 90 deg)
        # If BD is (-6, 4), perp is (4, 6)
        perp = np.array([-vec_BD[1], vec_BD[0], 0])
        # Normalize perp? No, we need length such that MC = MB = MD.
        # MB = BD / 2.
        # So we just need to add perp/2?
        # Let's check. M + perp/2.
        # M = (3, 2). perp = (-4, -6). perp/2 = (-2, -3). C = (1, -1).
        # Or perp = (4, 6). perp/2 = (2, 3). C = (5, 5).
        # We want the convex quadrilateral ABCD.
        # A=(0,0), B=(6,0), D=(0,4).
        # If C=(1,-1), it's inside? No.
        # If C=(5,5), it's outside.
        C = M + perp / 2
        
        # Create points
        pA = Dot(A)
        pB = Dot(B)
        pC = Dot(C)
        pD = Dot(D)
        
        # Lines
        quad = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        diag_BD = DashedLine(B, D, color=YELLOW)
        
        # Labels
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP+RIGHT)
        lbl_D = MathTex("D").next_to(D, UP+LEFT)
        
        # Side labels
        lbl_x = MathTex("x").next_to(Line(A,B), DOWN)
        lbl_y = MathTex("y").next_to(Line(A,D), LEFT)
        
        # Right angles
        ra_A = RightAngle(Line(A,B), Line(A,D), length=0.4)
        ra_C = RightAngle(Line(C,B), Line(C,D), length=0.4, quadrant=(-1,-1))
        
        # Equal sides marks
        mark_BC = Line(C, B).get_center()
        mark_CD = Line(C, D).get_center()
        tick_BC = Line(mark_BC + UP*0.1 + LEFT*0.1, mark_BC + DOWN*0.1 + RIGHT*0.1).rotate(45*DEGREES)
        tick_CD = Line(mark_CD + UP*0.1 + LEFT*0.1, mark_CD + DOWN*0.1 + RIGHT*0.1).rotate(45*DEGREES)
        
        # Group
        scene_objects = VGroup(
            quad, diag_BD,
            lbl_A, lbl_B, lbl_C, lbl_D,
            lbl_x, lbl_y,
            ra_A, ra_C,
            # tick_BC, tick_CD # Ticks might be hard to place correctly without more math, skipping or using simple lines
        )
        
        # Add ticks manually
        t1 = Line(ORIGIN, UP*0.2).rotate(45*DEGREES).move_to(Line(B,C).get_center())
        t2 = Line(ORIGIN, UP*0.2).rotate(45*DEGREES).move_to(Line(C,D).get_center())
        scene_objects.add(t1, t2)
        
        scene_objects.scale(0.7)
        scene_objects.shift(LEFT * 2.5)
        
        # Text
        text = VGroup(
            MathTex(r"\text{Given: } AB + AD = 10, \angle A = \angle C = 90^\circ, BC = CD"),
            MathTex(r"\text{Let } AB = x, AD = y \implies x + y = 10"),
            MathTex(r"\text{Arrea} = \text{Area}(\trriangle ABD) + \text{Area}(\triangle BCD)"),
            MathTex(r"\text{Arrea}(\triangle ABD) = \frac{1}{2}xy"),
            MathTex(r"\text{In } \trriangle BCD: BC=CD, \angle C=90^\circ \implies BD^2 = 2BC^2"),
            MathTex(r"\text{In } \triangle ABD: BD^2 = x^2 + y^2"),
            MathTex(r"\implies 2BC^2 = x^2 + y^2 \implies \text{Arrea}(\triangle BCD) = \frrac{BC^2}{2} = \frac{x^2+y^2}{4}"),
            MathTex(r"\text{Total Arrea} = \frac{xy}{2} + \frrac{x^2+y^2}{4} = \frac{2xy + x^2 + y^2}{4}"),
            MathTex(r"= \frrac{(x+y)^2}{4} = \frac{10^2}{4} = 25")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.65)
        
        self.add(scene_objects)
        self.add(text)
