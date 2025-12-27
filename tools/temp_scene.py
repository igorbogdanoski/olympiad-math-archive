from manim import *

class Task_2025_mun_g5_2(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
class Task_2025_mun_g5_2(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Draw a 5x5 grid representing the front face
        grid = VGroup()
        for i in range(5):
            for j in range(5):
                sq = Square(side_length=1, color=BLACK, fill_opacity=0)
                sq.move_to(RIGHT*(i-2) + UP*(j-2))
                grid.add(sq)
        
        # Highlight the removed cubes (assuming full layer for visual simplicity as per count 25)
        # Or just show the calculation
        
        cube_text = Text("Вкупно: 5 x 5 x 5 = 125", color=BLACK).to_edge(UP)
        removed_text = Text("Отстранети: 25", color=RED).next_to(cube_text, DOWN)
        percent_text = MathTex("\\frac{25}{125} = \\frac{1}{5} = 20\\%", color=BLUE).next_to(removed_text, DOWN)
        
        self.add(grid, cube_text)
        self.play(grid.animate.set_fill(RED, opacity=0.5), Write(removed_text))
        self.wait(1)
        self.play(Write(percent_text))
        # --- AI GENERATED CODE END ---



config.media_width = '100%'
config.verbosity = 'ERROR'
