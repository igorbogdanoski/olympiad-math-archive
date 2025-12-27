class Task_2025_mun_g9_5(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        sq = Square(side_length=4, color=BLUE, fill_opacity=0.5)
        lbl = MathTex("a=5", color=BLACK).move_to(sq.get_center())
        self.add(sq, lbl)