from manim import *

class Task_cnt92_v2_03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_cnt92_v2_03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], axis_config={"color": BLACK})
        
        # Case a = 1
        # y = x - 1
        line1 = axes.plot(lambda x: x - 1, color=BLUE)
        lbl1 = MathTex("y = x - 1", color=BLUE).next_to(line1, DR)
        
        # y = x + 1
        line2 = axes.plot(lambda x: x + 1, color=RED)
        lbl2 = MathTex("y = x + 1", color=RED).next_to(line2, UL)
        
        title = MathTex("a=1: \\text{Parallel}", color=BLACK).to_corner(UL)
        
        self.add(axes, line1, lbl1, line2, lbl2, title)
        # --- AI GENERATED CODE END ---



config.media_width = '100%'
config.verbosity = 'ERROR'
