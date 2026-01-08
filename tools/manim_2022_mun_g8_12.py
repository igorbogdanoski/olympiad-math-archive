from manim import *

class Problem_2022_mun_g8_12(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Terrace: 4m x 3m.
        # Tile: 40cm x 30cm = 0.4m x 0.3m.
        # Ratio: 4/0.4 = 10 tiles wide.
        # 3/0.3 = 10 tiles high.
        # Total tiles = 100.
        # Pack = 25 tiles.
        # Packs = 100/25 = 4.
        
        # Visualization:
        # Draw a large rectangle (Terrace).
        # Show grid of tiles.
        # Show dimensions.
        
        # Scale: 4m -> 6 units. 3m -> 4.5 units.
        terrace = Rectangle(width=6, height=4.5, color=BLUE, fill_opacity=0.1)
        
        # Grid
        # 10x10 grid.
        grid = VGroup()
        for i in range(11):
            # Vertical lines
            x = -3 + i * (6/10)
            line = Line(np.array([x, -2.25, 0]), np.array([x, 2.25, 0]), color=BLUE_A, stroke_width=1)
            grid.add(line)
            
            # Horizontal lines
            y = -2.25 + i * (4.5/10)
            line = Line(np.array([-3, y, 0]), np.array([3, y, 0]), color=BLUE_A, stroke_width=1)
            grid.add(line)
            
        # Labels
        lbl_width = MathTex(r"4 \text{ m}", color=BLACK).next_to(terrace, UP, buff=0.1)
        lbl_height = MathTex(r"3 \text{ m}", color=BLACK).next_to(terrace, RIGHT, buff=0.1)
        
        # Highlight one tile
        # Bottom left tile
        tile = Rectangle(width=6/10, height=4.5/10, color=RED, fill_opacity=0.5).move_to(np.array([-3 + 3/10, -2.25 + 2.25/10, 0]))
        
        lbl_tile = MathTex(r"40 \text{ cm} \\times 30 \text{ cm}", color=RED, font_size=24).next_to(tile, UR, buff=0.1)
        arrow = Arrow(lbl_tile.get_bottom(), tile.get_center(), color=RED, buff=0.05)
        
        # Text calculation
        calc1 = MathTex(r"\text{Area Terrace} = 400 \times 300 \text{ cm}^2", color=BLACK, font_size=30).to_corner(UL)
        calc2 = MathTex(r"\text{Arrea Tile} = 40 \times 30 \text{ cm}^2r, color=BLACK, font_size=30).next_to(calc1, DOWN, aligned_edge=LEFT)
        calc3 = MathTex(r"\text{Num Tiles} = \frrac{400}{40} \times \frrac{300}{30} = 10 \times 10 = 100r, color=BLACK, font_size=30).next_to(calc2, DOWN, aligned_edge=LEFT)
        calc4 = MathTex(r"\text{Packs} = \frac{100}{25} = 4", color=BLACK, font_size=30).next_to(calc3, DOWN, aligned_edge=LEFT)
        
        self.add(terrace, grid)
        self.add(lbl_width, lbl_height)
        self.add(tile, lbl_tile, arrow)
        self.add(calc1, calc2, calc3, calc4)
