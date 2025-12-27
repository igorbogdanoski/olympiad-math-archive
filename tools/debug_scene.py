from manim import *

class Task_2025_mun_y2_4a(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_y2_4a(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(x_range=[-3, 3, 1], y_range=[-1, 5, 1], axis_config={"color": BLACK})
        
        # Example a = 0.5
        a = 0.5
        
        # Function f(x) = 2|x-0.5| + 3|x+0.5|
        def func(x):
            return 2*abs(x-a) + 3*abs(x+a)
            
        graph = axes.plot(func, color=BLUE)
        
        # Minimum point at x = -a = -0.5
        # y = 4a = 2
        min_pt = Dot(axes.c2p(-a, 4*a), color=RED)
        lbl_min = MathTex("Min = 4a", color=RED).next_to(min_pt, DOWN)
        
        # Line y = 1
        line_1 = axes.plot(lambda x: 1, color=GREEN)
        lbl_1 = MathTex("y=1", color=GREEN).next_to(line_1, LEFT)
        
        self.add(axes, graph, min_pt, lbl_min, line_1, lbl_1)
        # --- AI GENERATED CODE END ---

config.media_width = '100%'
config.verbosity = 'ERROR'
