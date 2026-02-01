from manim import *

class LessonScene(Scene):
    def construct(self):
        # --- Configuration for Macedonian Text ---
        # Use a reliable font for Cyrillic
        def get_macedonian_text(text, color=WHITE, size=0.7):
            return Text(text, font="Arial", color=color, font_size=size)

        # ----------------------------------------------------
        # Scene 1: Introduction - Welcome to the Magic Land
        # ----------------------------------------------------

        title = get_macedonian_text(
            "Добредојдовте во Волшебната Земја на Формите!",
            color=YELLOW,
            size=1.0
        )
        self.play(Write(title))
        self.wait(1.5)

        subtitle = get_macedonian_text(
            "Денес ќе ги запознаеме нашите 2Д пријатели!",
            color=TEAL,
            size=0.8
        ).next_to(title, DOWN, buff=0.5)
        
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(2)
        
        self.play(
            FadeOut(title, shift=UP),
            FadeOut(subtitle, shift=UP)
        )
        self.wait(1)

        # ----------------------------------------------------
        # Scene 2: Naming and Describing Shapes
        # ----------------------------------------------------

        header = get_macedonian_text("Запознавање со Формите", color=BLUE_B, size=0.9).to_edge(UP)
        self.play(Write(header))
        self.wait(1)

        # 1. Introducing the Circle (Круг)
        circle_shape = Circle(color=RED, fill_opacity=0.8).scale(1.5).move_to(LEFT * 3)
        circle_name = get_macedonian_text("1. Круг", color=RED).next_to(circle_shape, UP, buff=0.5)
        circle_desc = get_macedonian_text("Нема агли, тој се тркала!", color=WHITE, size=0.6).next_to(circle_shape, RIGHT * 2, buff=0.5)

        self.play(DrawBorderThenFill(circle_shape), Write(circle_name))
        self.wait(1)
        self.play(Write(circle_desc))
        self.wait(2.5)

        # Clear Circle
        self.play(
            FadeOut(circle_shape),
            FadeOut(circle_name),
            FadeOut(circle_desc)
        )
        self.wait(0.5)

        # 2. Introducing the Square (Квадрат)
        square_shape = Square(color=BLUE_A, fill_opacity=0.8).scale(1.5).move_to(LEFT * 3)
        square_name = get_macedonian_text("2. Квадрат", color=BLUE_A).next_to(square_shape, UP, buff=0.5)
        square_desc = get_macedonian_text("Има 4 еднакви страни и 4 агли!", color=WHITE, size=0.6).next_to(square_shape, RIGHT * 2, buff=0.5)

        self.play(DrawBorderThenFill(square_shape), Write(square_name))
        self.wait(1)
        self.play(Write(square_desc))
        self.wait(2.5)

        # Clear Square
        self.play(
            FadeOut(square_shape),
            FadeOut(square_name),
            FadeOut(square_desc)
        )
        self.wait(0.5)

        # 3. Introducing the Triangle (Триаголник)
        triangle_shape = Triangle(color=GREEN_A, fill_opacity=0.8).scale(1.8).move_to(LEFT * 3)
        triangle_name = get_macedonian_text("3. Триаголник", color=GREEN_A).next_to(triangle_shape, UP, buff=0.5)
        triangle_desc = get_macedonian_text("Има 3 страни и 3 агли!", color=WHITE, size=0.6).next_to(triangle_shape, RIGHT * 2, buff=0.5)

        self.play(DrawBorderThenFill(triangle_shape), Write(triangle_name))
        self.wait(1)
        self.play(Write(triangle_desc))
        self.wait(2.5)

        # Clear everything from Scene 2
        self.play(
            FadeOut(triangle_shape),
            FadeOut(triangle_name),
            FadeOut(triangle_desc),
            FadeOut(header)
        )
        self.wait(1)

        # ----------------------------------------------------
        # Scene 3: Grouping the Shapes (Групирање)
        # ----------------------------------------------------

        grouping_header = get_macedonian_text("Време е за игра: Групирање!", color=PURPLE, size=1.0)
        self.play(Write(grouping_header))
        self.wait(1.5)
        self.play(grouping_header.animate.to_edge(UP))

        # 1. Create the initial mixed set of shapes
        
        shapes = VGroup(
            Circle(color=RED, fill_opacity=0.7).shift(UP * 1.5 + LEFT * 4.5).scale(0.5),
            Square(color=BLUE_A, fill_opacity=0.7).shift(UP * 1.5 + LEFT * 1.5).scale(0.6),
            Triangle(color=GREEN_A, fill_opacity=0.7).shift(UP * 1.5 + RIGHT * 1.5).scale(0.7),
            
            Square(color=BLUE_B, fill_opacity=0.7).shift(UP * 0 + LEFT * 4.5).scale(0.4),
            Triangle(color=GREEN_B, fill_opacity=0.7).shift(UP * 0 + LEFT * 1.5).scale(0.5),
            Circle(color=RED_B, fill_opacity=0.7).shift(UP * 0 + RIGHT * 1.5).scale(0.8),

            Triangle(color=GREEN_C, fill_opacity=0.7).shift(DOWN * 1.5 + LEFT * 4.5).scale(0.6),
            Circle(color=RED_C, fill_opacity=0.7).shift(DOWN * 1.5 + LEFT * 1.5).scale(0.7),
            Square(color=BLUE_C, fill_opacity=0.7).shift(DOWN * 1.5 + RIGHT * 1.5).scale(0.5),
            
            # Extra mixed shape
            Circle(color=ORANGE, fill_opacity=0.7).shift(DOWN * 0 + RIGHT * 4.5).scale(0.6),
            Square(color=YELLOW, fill_opacity=0.7).shift(UP * 1.5 + RIGHT * 4.5).scale(0.7),
            Triangle(color=TEAL, fill_opacity=0.7).shift(DOWN * 1.5 + RIGHT * 4.5).scale(0.5),
        )

        self.play(LaggedStart(*[FadeIn(shape) for shape in shapes], lag_ratio=0.1))
        self.wait(2)

        # 2. Define the target grouping areas
        
        group_circle_pos = UP * 1.5 + LEFT * 4
        group_square_pos = UP * 1.5 + RIGHT * 0
        group_triangle_pos = UP * 1.5 + RIGHT * 4
        
        # Define Group Labels
        label_circle = get_macedonian_text("КРУГОВИ", color=RED).next_to(group_circle_pos, UP)
        label_square = get_macedonian_text("КВАДРАТИ", color=BLUE).next_to(group_square_pos, UP)
        label_triangle = get_macedonian_text("ТРИАГОЛНИЦИ", color=GREEN).next_to(group_triangle_pos, UP)
        
        self.play(
            Write(label_circle),
            Write(label_square),
            Write(label_triangle)
        )
        self.wait(1)

        # 3. Animate the Grouping Process (Slowly and deliberately)

        circle_counter = 0
        square_counter = 0
        triangle_counter = 0

        animations = []

        for shape in shapes:
            target_pos = ORIGIN
            
            # Determine type based on shape class
            if isinstance(shape, Circle):
                target_pos = group_circle_pos + DOWN * 1.5 + DOWN * 0.7 * circle_counter
                circle_counter += 1
            elif isinstance(shape, Square):
                target_pos = group_square_pos + DOWN * 1.5 + DOWN * 0.7 * square_counter
                square_counter += 1
            elif isinstance(shape, Triangle):
                target_pos = group_triangle_pos + DOWN * 1.5 + DOWN * 0.7 * triangle_counter
                triangle_counter += 1
            
            animations.append(shape.animate.move_to(target_pos).scale(1.2))

        # Execute the grouping animations simultaneously (but clearly visible)
        self.play(LaggedStart(*animations, lag_ratio=0.5), run_time=5)
        self.wait(2)
        
        # 4. Conclusion
        
        final_message = get_macedonian_text("Одлично! Успеавме да ги групираме сите форми!", color=YELLOW).to_edge(DOWN)
        self.play(Write(final_message))
        self.wait(3)
        
        self.play(FadeOut(*self.mobjects))
        self.wait(1)