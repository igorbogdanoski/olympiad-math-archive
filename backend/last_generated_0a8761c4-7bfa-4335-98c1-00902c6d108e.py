from manim import *

class LessonScene(Scene):
    def construct(self):
        # --- 1. Introduction ---
        
        # Use gradient for playful title effect
        title = Text("Добредојдовте на Забавата на Формите!", 
                     font="Arial", 
                     color=YELLOW_A, 
                     gradient=(RED, YELLOW))
        
        subtitle = Text("Учиме за Круг, Квадрат и Триаголник.", 
                        font="Arial", 
                        color=BLUE_A).scale(0.8)

        self.play(Write(title))
        self.wait(1.5)
        self.play(
            title.animate.to_edge(UP), 
            FadeIn(subtitle, shift=DOWN)
        )
        self.wait(2)
        self.play(FadeOut(subtitle))
        
        
        # --- 2. Introducing Shapes Individually ---

        # 2a. Circle (Круг)
        
        # Reset title position for clean transition
        self.play(title.animate.scale(0.7).to_edge(UP)) 
        
        circle_obj = Circle(radius=1.5, color=RED, fill_opacity=0.8).shift(LEFT * 4)
        circle_name = Text("Јас сум Круг!", font="Arial", color=RED).next_to(circle_obj, DOWN, buff=0.5)
        circle_desc = Text("Јас сум тркалезен и немам агли!", font="Arial", color=RED).scale(0.7).next_to(circle_name, DOWN)

        self.play(Create(circle_obj), Write(circle_name))
        self.wait(1.5)
        self.play(Write(circle_desc))
        self.wait(2)
        
        # Move the shape aside for reference
        circle_group = VGroup(circle_obj, circle_name, circle_desc)
        self.play(circle_group.animate.scale(0.4).to_corner(UP + LEFT))
        
        
        # 2b. Square (Квадрат)
        
        square_obj = Square(side_length=1.5, color=BLUE, fill_opacity=0.8).shift(LEFT * 4)
        square_name = Text("Јас сум Квадрат!", font="Arial", color=BLUE).next_to(square_obj, DOWN, buff=0.5)
        square_desc = Text("Имам 4 исти страни и 4 агли.", font="Arial", color=BLUE).scale(0.7).next_to(square_name, DOWN)

        self.play(Create(square_obj), Write(square_name))
        self.wait(1.5)
        self.play(Write(square_desc))
        self.wait(2)
        
        # Move the shape aside for reference
        square_group = VGroup(square_obj, square_name, square_desc)
        self.play(square_group.animate.scale(0.4).to_corner(UP))
        
        
        # 2c. Triangle (Триаголник)
        
        triangle_obj = Triangle(color=YELLOW, fill_opacity=0.8).scale(1.5).shift(LEFT * 4)
        triangle_name = Text("Јас сум Триаголник!", font="Arial", color=YELLOW).next_to(triangle_obj, DOWN, buff=0.5)
        triangle_desc = Text("Имам само 3 страни и 3 агли!", font="Arial", color=YELLOW).scale(0.7).next_to(triangle_name, DOWN)

        self.play(Create(triangle_obj), Write(triangle_name))
        self.wait(1.5)
        self.play(Write(triangle_desc))
        self.wait(2)
        
        # Move the shape aside for reference
        triangle_group = VGroup(triangle_obj, triangle_name, triangle_desc)
        self.play(triangle_group.animate.scale(0.4).to_corner(UP + RIGHT))
        
        
        # --- 3. Grouping Activity Setup ---
        
        # Fade out individual descriptions, keep only the small reference shapes (as titles)
        self.play(FadeOut(VGroup(circle_group, square_group, triangle_group)))
        
        grouping_title = Text("Време е за Групирање!", font="Arial", color=TEAL).to_edge(UP)
        self.play(Transform(title, grouping_title)) # Transform old title to new title
        self.wait(1)

        # Create 9 randomly scattered shapes
        shapes = VGroup()
        colors = [RED, BLUE, YELLOW]
        
        # Create 3 of each
        for i in range(3):
            shapes.add(Circle(radius=0.4, color=RED, fill_opacity=0.7))
            shapes.add(Square(side_length=0.8, color=BLUE, fill_opacity=0.7))
            shapes.add(Triangle(color=YELLOW, fill_opacity=0.7).scale(0.8))

        # Scatter them randomly across the screen center
        for shape in shapes:
            shape.move_to(np.random.rand(3) * 6 - 3)
            shape.shift(DOWN * 0.5)

        self.play(LaggedStart(*[FadeIn(s, scale=0.5) for s in shapes], lag_ratio=0.1))
        self.wait(2)

        # Create sorting areas (Visualizing the 'boxes')
        area_circle = Circle(radius=1.5, color=RED).shift(LEFT * 3)
        area_square = Square(side_length=3.0, color=BLUE).shift(CENTER)
        area_triangle = Triangle().scale(2.5).set_stroke(color=YELLOW, width=4).shift(RIGHT * 3)

        label_circle = Text("Кругови", font="Arial", color=RED).next_to(area_circle, UP)
        label_square = Text("Квадрати", font="Arial", color=BLUE).next_to(area_square, UP)
        label_triangle = Text("Триаголници", font="Arial", color=YELLOW).next_to(area_triangle, UP)

        sorting_areas = VGroup(area_circle, area_square, area_triangle, label_circle, label_square, label_triangle)
        self.play(Create(sorting_areas), run_time=1.5)
        self.wait(1.5)


        # --- 4. Sorting and Grouping ---
        
        # Define target positions for stacking the sorted shapes
        target_pos_circle = LEFT * 3
        target_pos_square = CENTER
        target_pos_triangle = RIGHT * 3

        # Helper lists to manage sorting
        circles_to_sort = [s for s in shapes if isinstance(s, Circle)]
        squares_to_sort = [s for s in shapes if isinstance(s, Square)]
        # Filter Triangles (Manim Triangle is a specific Polygon)
        triangles_to_sort = [s for s in shapes if s.get_num_vertices() == 3 and isinstance(s, Polygon)] 

        
        # 4a. Group 1: Circles
        
        instruction_c = Text("Прво ги групираме Круговите!", font="Arial", color=RED).scale(0.7).to_corner(DOWN)
        self.play(Write(instruction_c))
        
        animations_c = []
        for i, c in enumerate(circles_to_sort):
            c.target = target_pos_circle + (i - 1) * UP * 0.7 
            animations_c.append(c.animate.move_to(c.target))
            
        self.play(LaggedStart(*animations_c, lag_ratio=0.5), run_time=3)
        self.wait(1.5)
        self.play(FadeOut(instruction_c)) 


        # 4b. Group 2: Squares

        instruction_s = Text("Сега се Квадратите на ред!", font="Arial", color=BLUE).scale(0.7).to_corner(DOWN)
        self.play(Write(instruction_s))

        animations_s = []
        for i, s in enumerate(squares_to_sort):
            s.target = target_pos_square + (i - 1) * UP * 0.7 
            animations_s.append(s.animate.move_to(s.target))
            
        self.play(LaggedStart(*animations_s, lag_ratio=0.5), run_time=3)
        self.wait(1.5)
        self.play(FadeOut(instruction_s)) 


        # 4c. Group 3: Triangles

        instruction_t = Text("На крај, Триаголниците!", font="Arial", color=YELLOW).scale(0.7).to_corner(DOWN)
        self.play(Write(instruction_t))

        animations_t = []
        for i, t in enumerate(triangles_to_sort):
            t.target = target_pos_triangle + (i - 1) * UP * 0.7
            animations_t.append(t.animate.move_to(t.target))

        self.play(LaggedStart(*animations_t, lag_ratio=0.5), run_time=3)
        self.wait(2)
        self.play(FadeOut(instruction_t)) 
        
        
        # --- 5. Conclusion ---
        
        conclusion = Text("Одлично! Успеавме да ги групираме сите форми!", 
                          font="Arial", 
                          color=GREEN_A).scale(1.2)
        
        all_shapes = VGroup(*circles_to_sort, *squares_to_sort, *triangles_to_sort)
        
        self.play(
            FadeOut(title),
            FadeOut(sorting_areas),
            all_shapes.animate.scale(1.2).center(),
            run_time=2
        )
        
        self.play(
            Transform(all_shapes, conclusion),
            run_time=2
        )
        self.wait(3)
        
        self.play(FadeOut(conclusion))