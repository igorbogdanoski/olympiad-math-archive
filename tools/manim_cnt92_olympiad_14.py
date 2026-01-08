from manim import *

class Problem_cnt92_olympiad_14(Scene):
    def construct(self):
        # Axes
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 7, 1],
            axis_config={"color": BLUE},
        )
        
        # Line function
        def line_func(x):
            return np.sqrt(2) * x + np.sqrt(3)
        
        # Plot line
        line_graph = axes.plot(line_func, color=YELLOW)
        line_label = axes.get_graph_label(line_graph, label=r"y = \\sqrrt{2}x + \\sqrt{3}", x_val=3, direction=UP)
        
        # Points
        A_coords = [1, 3]
        B_coords = [2, 5]
        
        A_point = axes.c2p(*A_coords)
        B_point = axes.c2p(*B_coords)
        
        dot_A = Dot(A_point, color=RED)
        dot_B = Dot(B_point, color=GREEN)
        
        label_A = MathTex("A(1, 3)").next_to(dot_A, DOWN)
        label_B = MathTex("B(2, 5)").next_to(dot_B, UP)
        
        # Projections to line to show above/below
        # Point on line for x=1
        y_line_A = line_func(1)
        pt_line_A = axes.c2p(1, y_line_A)
        line_A_proj = DashedLine(A_point, pt_line_A, color=GRAY)
        
        # Point on line for x=2
        y_line_B = line_func(2)
        pt_line_B = axes.c2p(2, y_line_B)
        line_B_proj = DashedLine(B_point, pt_line_B, color=GRAY)
        
        self.add(axes, line_graph, line_label)
        self.add(dot_A, label_A, line_A_proj)
        self.add(dot_B, label_B, line_B_proj)
        
        # Conclusion text
        text_A = Text("A is below", font_size=24).next_to(label_A, DOWN)
        text_B = Text("B is above", font_size=24).next_to(label_B, UP)
        
        self.add(text_A, text_B)
