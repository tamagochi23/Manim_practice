from manim import *

class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(radius=2, color = BLUE).shift(3*LEFT)
        square = Square(side_length=3, color = GREEN).shift(RIGHT)
        triangle = Triangle(color=YELLOW).scale(2).shift(4*RIGHT)
        dot = Dot(color=RED).shift(3*LEFT)
        dot2 = dot.copy().shift(2*RIGHT)
        dot3 = Dot(color=RED).move_to(square.get_center()).shift(1.5*RIGHT+1.5*UP)
        dot4 = Dot(color=RED).move_to(triangle.get_center()).shift(1.5*UP)
        self.add(dot)
        self.play(GrowFromCenter(circle), GrowFromCenter(square), GrowFromCenter(triangle))
        self.wait()
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=3, rate_func=linear)
        self.play(Transform(dot, dot3))
        self.play(MoveAlongPath(dot, square), run_time=3, rate_func=linear)
        self.play(Transform(dot, dot4))
        self.play(MoveAlongPath(dot, triangle), run_time=3, rate_func=linear)
