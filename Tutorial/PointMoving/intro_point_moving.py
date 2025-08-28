from manim import *
import random

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
        self.wait()
        
class PointsAndLine(Scene):
    def construct(self):
        d1,d2 = Dot(color=BLUE), Dot(color = GREEN)
        circle = Circle(radius=3, color=WHITE).move_to(ORIGIN)
        dg = VGroup(d1,d2).arrange(RIGHT)
        l1 = Line(d1.get_center(), d2.get_center()).set_color(RED)
        x = ValueTracker(0)
        y = ValueTracker(0)
        d1.add_updater(lambda m: m.set_x(x.get_value()))
        d2.add_updater(lambda m: m.set_y(y.get_value()))
        l1.add_updater(lambda m: m.become(Line(d1.get_center(), d2.get_center())))
        self.add(d1,d2,l1)
        i = 0
        while i < 5:
            if i % 2 == 0:
                value_x = -1
                value_y = 1
            else:
                value_x = 1
                value_y = -1
            self.play(x.animate.set_value(3* value_x), y.animate.set_value(3*value_y), rate_func=linear, run_time=0.7)
            self.play(GrowFromCenter(circle))
            i += 1

