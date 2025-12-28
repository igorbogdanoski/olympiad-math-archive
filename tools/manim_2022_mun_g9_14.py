from manim import *

class Problem_2022_mun_g9_14(Scene):
    def construct(self):
        # Scale
        scale = 1.5
        
        # Parameters
        # Ratios: AB:BC:CD = 2020:2021:2022
        # Let k be the unit.
        # AB = 2020k, BC = 2021k, CD = 2022k
        # Tangential quad property: AB + CD = BC + AD
        # 2020k + 2022k = 2021k + AD
        # 4042k = 2021k + AD => AD = 2021k
        
        # Perimeter L = 40.42 km = 40420 m
        # L = AB + BC + CD + AD = 2020k + 2021k + 2022k + 2021k = 8084k
        # 8084k = 40420 => k = 5
        
        # Sides:
        # AB = 2020 * 5 = 10100
        # BC = 2021 * 5 = 10105
        # CD = 2022 * 5 = 10110
        # AD = 2021 * 5 = 10105
        
        # Longest side is CD = 10110 m
        
        # Visualization
        # Let's draw a tangential quadrilateral with sides roughly proportional to 2020, 2021, 2022, 2021.
        # These are very close to equal (square-ish).
        # Let's draw a square/rhombus-like shape.
        
        # Incircle radius r = 1 (arbitrary for visualization)
        r = 1.5
        circle = Circle(radius=r, color=GREEN)
        
        # Tangent points
        # Let's pick 4 points on the circle.
        # To get specific side lengths is hard geometrically.
        # But since sides are almost equal, a square is a good approximation.
        # Or a kite.
        # Let's just draw a generic tangential quadrilateral.
        
        # Tangent points angles
        angles = [0, 90*DEGREES, 180*DEGREES, 270*DEGREES]
        # Adjust angles slightly to make it not a square
        angles = [0, 85*DEGREES, 190*DEGREES, 280*DEGREES]
        
        tangent_points = [
            r * np.array([np.cos(theta), np.sin(theta), 0])
            for theta in angles
        ]
        
        # Tangent lines at these points
        # Line equation: x*cos(theta) + y*sin(theta) = r
        # Intersection of line i and i+1 gives vertex.
        
        vertices = []
        for i in range(4):
            p1 = tangent_points[i]
            p2 = tangent_points[(i+1)%4]
            theta1 = angles[i]
            theta2 = angles[(i+1)%4]
            
            # Intersection of tangents at theta1 and theta2
            # x cos t1 + y sin t1 = r
            # x cos t2 + y sin t2 = r
            
            mat = np.array([
                [np.cos(theta1), np.sin(theta1)],
                [np.cos(theta2), np.sin(theta2)]
            ])
            rhs = np.array([r, r])
            sol = np.linalg.solve(mat, rhs)
            vertices.append(np.array([sol[0], sol[1], 0]))
            
        A, B, C, D = vertices
        # Note: Order might be different depending on angles.
        # With 0, 85, 190, 280:
        # 0-85 -> Vertex 1 (between 0 and 85) -> ~42.5 deg (First quadrant)
        # 85-190 -> Vertex 2 (between 85 and 190) -> ~137.5 deg (Second quadrant)
        # 190-280 -> Vertex 3 (between 190 and 280) -> ~235 deg (Third quadrant)
        # 280-0 -> Vertex 4 (between 280 and 360) -> ~320 deg (Fourth quadrant)
        
        # Let's map them to A, B, C, D
        # A = Vertex 4 (bottom right)
        # B = Vertex 1 (top right)
        # C = Vertex 2 (top left)
        # D = Vertex 3 (bottom left)
        
        A_pt = vertices[3]
        B_pt = vertices[0]
        C_pt = vertices[1]
        D_pt = vertices[2]
        
        # Shift to center
        center = (A_pt + B_pt + C_pt + D_pt) / 4
        shift = -center
        
        A_pt += shift
        B_pt += shift
        C_pt += shift
        D_pt += shift
        circle.shift(shift)
        
        # Apply scale (already scaled by r)
        
        quad = Polygon(A_pt, B_pt, C_pt, D_pt, color=BLUE)
        
        label_A = MathTex("A").next_to(A_pt, DR)
        label_B = MathTex("B").next_to(B_pt, UR)
        label_C = MathTex("C").next_to(C_pt, UL)
        label_D = MathTex("D").next_to(D_pt, DL)
        
        label_AB = MathTex("2020k").next_to(Line(A_pt, B_pt), RIGHT)
        label_BC = MathTex("2021k").next_to(Line(B_pt, C_pt), UP)
        label_CD = MathTex("2022k").next_to(Line(C_pt, D_pt), LEFT)
        label_AD = MathTex("AD").next_to(Line(D_pt, A_pt), DOWN)
        
        # Text
        text = MathTex(
            r"AB + CD = BC + AD",
            r"2020k + 2022k = 2021k + AD \implies AD = 2021k",
            r"L = 8084k = 40420 \implies k = 5",
            r"\max(Side) = CD = 2022 \cdot 5 = 10110"
        ).arrange(DOWN).to_corner(UL).scale(0.8)
        
        self.add(quad, circle)
        self.add(label_A, label_B, label_C, label_D)
        self.add(label_AB, label_BC, label_CD, label_AD)
        self.add(text)
