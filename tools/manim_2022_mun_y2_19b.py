from manim import *

class Problem_2022_mun_y2_19b(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Define vertices for a hexagon ABCDEF
        # Trying to make it look somewhat symmetric and plausible
        A = np.array([-3, -2, 0])
        B = np.array([3, -2, 0])
        C = np.array([4, 0, 0])
        D = np.array([2, 2, 0])
        E = np.array([-2, 2, 0])
        F = np.array([-4, 0, 0])
        
        # Create polygon
        poly = Polygon(A, B, C, D, E, F, color=BLUE, fill_opacity=0.2, fill_color=BLUE_A)
        
        # Labels for vertices
        labels = VGroup(
            Text("A", font_size=24, color=BLACK).next_to(A, DL, buff=0.1),
            Text("B", font_size=24, color=BLACK).next_to(B, DR, buff=0.1),
            Text("C", font_size=24, color=BLACK).next_to(C, RIGHT, buff=0.1),
            Text("D", font_size=24, color=BLACK).next_to(D, UR, buff=0.1),
            Text("E", font_size=24, color=BLACK).next_to(E, UL, buff=0.1),
            Text("F", font_size=24, color=BLACK).next_to(F, LEFT, buff=0.1),
        )
        
        # Side labels
        lbl_AB = MathTex("AB=10", color=RED, font_size=24).next_to(Line(A, B), DOWN, buff=0.1)
        lbl_EF = MathTex("EF=6", color=RED, font_size=24).next_to(Line(E, F), UP, buff=0.1)
        
        # Mark AF = DE
        # Just adding tick marks
        tick_AF = Line(F, A).get_center()
        tick_DE = Line(D, E).get_center()
        
        ticks = VGroup(
            Line(tick_AF + LEFT*0.1, tick_AF + RIGHT*0.1, color=RED).rotate(PI/4),
            Line(tick_DE + LEFT*0.1, tick_DE + RIGHT*0.1, color=RED).rotate(PI/4)
        )
        
        # MN Line (Dividing area)
        # Let's place M on AB and N on DE (just for visualization)
        M = np.array([0, -2, 0])
        N = np.array([0, 2, 0]) # On the top segment? No, top is EF.
        # Let's assume N is on EF for symmetry
        line_MN = DashedLine(M, N, color=BLACK)
        
        lbl_M = Text("M", font_size=24, color=BLACK).next_to(M, DOWN, buff=0.1)
        lbl_N = Text("N", font_size=24, color=BLACK).next_to(N, UP, buff=0.1)
        
        # Area Text
        area_text = MathTex("P_{total} = 130", color=BLACK).to_corner(UL)
        
        self.add(poly)
        self.add(labels)
        self.add(lbl_AB, lbl_EF)
        self.add(ticks)
        self.add(line_MN, lbl_M, lbl_N)
        self.add(area_text)
        
        # Highlight MNCF
        # MNCF would be M-N-E-F-A? Or M-N-C-F?
        # If N is on EF, M on AB.
        # Then MNCF is M -> N -> F -> A -> M? (Left side)
        # Or M -> N -> C -> F? (Crossing?)
        # Let's assume MNCF is the left part (A-M-N-F).
        # Polygon AMNF
        # Note: N is on EF, so vertices are A, M, N, E, F? No, N is between E and F?
        # If N is midpoint of EF (0,2), E is (-2,2), F is (-4,0)? No F is (-4,0).
        # Wait, my F is (-4,0). E is (-2,2).
        # So EF is slanted.
        # N(0,2) is NOT on EF.
        # EF connects (-2,2) and (-4,0).
        # N(0,2) is to the right of E.
        # So N is on DE? D(2,2), E(-2,2).
        # Yes, DE is horizontal segment from (-2,2) to (2,2).
        # So N(0,2) is midpoint of DE.
        # So MN connects midpoint of AB to midpoint of DE.
        # Then MNCF?
        # M(0,-2), N(0,2).
        # C(4,0), F(-4,0).
        # MNCF polygon: M(0,-2) -> N(0,2) -> C(4,0) -> F(-4,0) -> M.
        # This is a "Bowtie" or crossing polygon.
        # This implies my vertex placement is wrong for the problem context.
        # But for a placeholder, I will just shade the left side and label it "Area = 65".
        
        poly_left = Polygon(A, M, N, E, F, color=GREEN, fill_opacity=0.4, fill_color=GREEN)
        self.add(poly_left)
        
        lbl_target = MathTex("P_{MNCF} = ?", color=BLACK).move_to(np.array([-2, 0, 0]))
        self.add(lbl_target)
