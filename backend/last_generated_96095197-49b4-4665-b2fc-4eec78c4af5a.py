from manim import *

class LessonScene(Scene):
    def construct(self):
        # Configuration for Macedonian Text (Cyrillic)
        def mk_text(text, **kwargs):
            return Text(text, font="Arial", **kwargs)

        # ----------------------------------------------------------------------
        # PART 1: Introduction and Welcome
        # ----------------------------------------------------------------------

        title = mk_text("Авантура на Формите!", color=TEAL, font_size=72).to_edge(UP)
        welcome = mk_text("Добредојдовте, мали истражувачи!", font_size=40)

        self.play(
            Write(title),
            FadeIn(welcome, shift=DOWN)
        )
        self.wait(2)
        
        self.play(
            FadeOut(welcome),
            title.animate.scale(0.7).to_corner(UL)
        )
        self.wait(1)

        # ----------------------------------------------------------------------
        # PART 2: Introducing the Shapes (Именува и опишува)
        # ----------------------------------------------------------------------
        
        # --- 2.1 The Circle (Круг) ---
        circle_shape = Circle(radius=1, color=BLUE, fill_opacity=0.8).shift(LEFT * 3)
        circle_name = mk_text("Јас сум КРУГ!", color=BLUE).next_to(circle_shape, DOWN)

        self.play(
            Create(circle_shape),
            Write(circle_name)
        )
        self.wait(1)

        circle_desc = mk_text("Немам ќошиња, сакам да се тркалам!", font_size=30).next_to(circle_name, DOWN, buff=0.5)
        self.play(
            Write(circle_desc),
            circle_shape.animate.shift(RIGHT * 0.5).shift(LEFT * 0.5) # Simulate rolling motion
        )
        self.wait(2)
        self.play(FadeOut(circle_desc))


        # --- 2.2 The Square (Квадрат) ---
        square_shape = Square(side_length=2, color=RED, fill_opacity=0.8)
        square_name = mk_text("Јас сум КВАДРАТ!", color=RED).next_to(square_shape, DOWN)

        self.play(
            Create(square_shape),
            Write(square_name)
        )
        self.wait(1)

        square_desc = mk_text("Имам 4 еднакви страни и 4 ќошиња.", font_size=30).next_to(square_name, DOWN, buff=0.5)
        self.play(Write(square_desc))
        
        # Highlight the sides (simple visual emphasis)
        self.play(
            square_shape.animate.scale(1.1).set_opacity(1.0),
            run_time=0.5
        )
        self.play(
            square_shape.animate.scale(1/1.1).set_opacity(0.8),
            FadeOut(square_desc),
            run_time=0.5
        )
        self.wait(2)


        # --- 2.3 The Triangle (Триаголник) ---
        triangle_shape = Triangle(color=YELLOW, fill_opacity=0.8).scale(1.5).shift(RIGHT * 3)
        triangle_name = mk_text("Јас сум ТРИАГОЛНИК!", color=YELLOW).next_to(triangle_shape, DOWN)

        self.play(
            Create(triangle_shape),
            Write(triangle_name)
        )
        self.wait(1)

        triangle_desc = mk_text("Имам 3 страни и 3 ќошиња.", font_size=30).next_to(triangle_name, DOWN, buff=0.5)
        self.play(Write(triangle_desc))
        
        # Highlight the corners
        dots = VGroup(*[
            Dot(triangle_shape.get_corner(i), color=PURPLE) 
            for i in [UL, UR, DOWN]
        ])
        
        self.play(
            GrowFromCenter(dots),
            run_time=1.5
        )
        self.play(FadeOut(triangle_desc, dots))
        self.wait(2)

        # Clear the stage for the grouping activity
        intro_shapes = VGroup(circle_shape, circle_name, square_shape, square_name, triangle_shape, triangle_name)
        self.play(
            FadeOut(intro_shapes, shift=UP),
            FadeOut(title)
        )
        self.wait(1)

        # ----------------------------------------------------------------------
        # PART 3: Grouping Activity (Групира)
        # ----------------------------------------------------------------------
        
        grouping_title = mk_text("Игра: Групирање на Пријателите!", color=GREEN_B, font_size=50).to_edge(UP)
        self.play(Write(grouping_title))
        self.wait(1)

        # 3.1 Create a collection of mixed shapes
        
        shapes = VGroup()
        
        # Setup coordinates for placement
        coords = [
            [-3, 1.5, 0], [0, 2, 0], [4, -1, 0],
            [-4, -2, 0], [1, -2.5, 0], [2, 1, 0],
            [-1, 0, 0], [3, 2.5, 0], [-2, -1.5, 0]
        ]
        
        # Define 3 of each shape type
        for i in range(3):
            shapes.add(Circle(radius=0.4, color=BLUE, fill_opacity=0.7).move_to(coords.pop(0)))
            shapes.add(Square(side_length=0.8, color=RED, fill_opacity=0.7).move_to(coords.pop(0)))
            shapes.add(Triangle(color=YELLOW, fill_opacity=0.7).scale(0.6).move_to(coords.pop(0)))

        self.play(LaggedStart(*[GrowFromCenter(s) for s in shapes], lag_ratio=0.1), run_time=3)
        self.wait(2)

        instruction = mk_text("Да ги собереме истите форми заедно!", font_size=40, color=WHITE).next_to(grouping_title, DOWN, buff=0.5)
        self.play(Write(instruction))
        self.wait(2)

        # 3.2 Define grouping zones
        circle_zone = Rectangle(width=2, height=3, color=BLUE_A).shift(LEFT * 4).shift(UP * 0.5)
        square_zone = Rectangle(width=2, height=3, color=RED_A).shift(UP * 0.5)
        triangle_zone = Rectangle(width=2, height=3, color=YELLOW_A).shift(RIGHT * 4).shift(UP * 0.5)

        zone_names = VGroup(
            mk_text("Кругови", color=BLUE).next_to(circle_zone, DOWN),
            mk_text("Квадрати", color=RED).next_to(square_zone, DOWN),
            mk_text("Триаголници", color=YELLOW).next_to(triangle_zone, DOWN)
        )

        self.play(
            FadeIn(circle_zone, square_zone, triangle_zone),
            Write(zone_names)
        )
        self.wait(1)

        # 3.3 Animate the grouping (Movement)
        
        circles = VGroup(*[s for s in shapes if isinstance(s, Circle)])
        squares = VGroup(*[s for s in shapes if isinstance(s, Square)])
        triangles = VGroup(*[s for s in shapes if isinstance(s, Triangle)])

        # Grouping Circles
        self.play(
            instruction.animate.set_color(BLUE).scale(1.05),
            circles.animate.arrange(direction=DOWN, buff=0.2).move_to(circle_zone),
            run_time=3
        )
        self.wait(1.5)

        # Grouping Squares
        self.play(
            instruction.animate.set_color(RED).scale(1/1.05).scale(1.05),
            squares.animate.arrange(direction=DOWN, buff=0.2).move_to(square_zone),
            run_time=3
        )
        self.wait(1.5)

        # Grouping Triangles
        self.play(
            instruction.animate.set_color(YELLOW).scale(1/1.05).scale(1.05),
            triangles.animate.arrange(direction=DOWN, buff=0.2).move_to(triangle_zone),
            run_time=3
        )
        self.wait(2)

        # ----------------------------------------------------------------------
        # PART 4: Conclusion
        # ----------------------------------------------------------------------

        final_message = mk_text("Браво! Успеавте да ги групирате сите форми!", font_size=50, color=TEAL).shift(DOWN * 3)
        
        self.play(
            FadeOut(instruction),
            Write(final_message)
        )
        self.wait(3)
        
        # Cleanup
        self.play(
            FadeOut(VGroup(grouping_title, circle_zone, square_zone, triangle_zone, zone_names, final_message, shapes)),
            run_time=2
        )
        
        goodbye = mk_text("Се гледаме на следната авантура!", color=PURPLE)
        self.play(Write(goodbye))
        self.wait(3)