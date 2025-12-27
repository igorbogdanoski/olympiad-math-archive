from manim import *

class ProblemScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Axes
        axes = Axes(
            x_range=[-3, 4, 1],
            y_range=[-4, 8, 2],
            axis_config={"color": BLACK, "include_numbers": True},
            tips=True
        ).scale(0.8)
        
        # Function y = -x^2 + 2x + 5
        parabola = axes.plot(lambda x: -x**2 + 2*x + 5, color=BLUE)
        
        # Interval [-2, 2]
        interval_line = Line(
            start=axes.c2p(-2, 0),
            end=axes.c2p(2, 0),
            color=GREEN,
            stroke_width=6
        )
        
        # Points of interest
        # x = -2, y = -3 (Minimum on interval)
        pt_min = axes.c2p(-2, -3)
        dot_min = Dot(pt_min, color=RED, radius=0.12)
        label_min = MathTex("min(-2, -3)", color=RED).next_to(dot_min, DOWN+LEFT)
        
        # x = 1, y = 6 (Vertex - Max)
        pt_vertex = axes.c2p(1, 6)
        dot_vertex = Dot(pt_vertex, color=BLACK, radius=0.08)
        label_vertex = MathTex("V(1, 6)", color=BLACK).next_to(dot_vertex, UP)
        
        # x = 2, y = 5 (Other endpoint)
        pt_end = axes.c2p(2, 5)
        dot_end = Dot(pt_end, color=BLACK, radius=0.08)
        
        # Dashed lines for min
        dash_h = DashedLine(start=axes.c2p(0, -3), end=pt_min, color=GRAY)
        dash_v = DashedLine(start=axes.c2p(-2, 0), end=pt_min, color=GRAY)
        
        self.add(axes, parabola, interval_line, dot_min, label_min, dot_vertex, label_vertex, dot_end, dash_h, dash_v)
