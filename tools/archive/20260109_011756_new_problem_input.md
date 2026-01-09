# Highlight points
        dot_y = Dot(Y, color=RED, radius=0.12)
        cross = Cross(Y, color=RED, stroke_width=4).scale(0.5)
        highlight = SurroundingRectangle(dot_y, color=RED, buff=0.08)

        # ...existing code...
        self.add(ext_line, triangle, bisector_a, bisector_b, dot_y, cross, highlight, gamma_arc, ayb_arc)
        self.add(lbl_A, lbl_B, lbl_C, lbl_Y, res)