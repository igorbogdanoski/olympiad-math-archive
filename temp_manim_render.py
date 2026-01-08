from manim import *

class Task_2025_mun_g9_5(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        sq = Square(side_length=4, color=BLUE, fill_opacity=0.5)
        lbl = MathTex("a=5", color=BLACK).move_to(sq.get_center())
        self.add(sq, lbl)
        
        eq_sys = MathTex("q-4", "=", "q", "=", "q+4").set_color(BLACK)
        eq_sys.next_to(sq, DOWN)
        self.add(eq_sys)
        
        triplet = Text(r"{q-4, q, q+4}", color=BLACK).next_to(eq_sys, DOWN)
        self.add(triplet)
        mod_check = Text("Единствена тројка прости броеви:", font_size=24, color=BLACK).next_to(triplet, DOWN)
        self.add(mod_check)
        final_set = Text("{3, 7, 11}", color=RED).next_to(mod_check, DOWN)
        self.add(final_set)