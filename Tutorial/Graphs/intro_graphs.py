from manim import *

class GraphExample(Scene):
    def construct(self):

        def floor_func(x):
            return np.floor(x)

        self.next_section()
        axes = Axes(x_range = [-5,5], y_range = [-2,5],
        x_length = 10, y_length = 7,
        axis_config = {"include_tip":False, "numbers_to_exclude": [0]}
        ).add_coordinates()
        ##axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label = "x", y_label = "f(x)")

        t = ValueTracker(-2)

        def func(x):
            return x**2

        graph = axes.plot(func)

        initial_point = axes.c2p(-2, func(-2))
        dot = Dot(point=initial_point, color=RED)

        dot.add_updater(lambda m: m.move_to(axes.c2p(t.get_value(), func(t.get_value()))))


        eq1 = MathTex("f(x) = x^2").move_to(4*RIGHT + 2*UP)

        x_text = MathTex("x=", t.get_value()).move_to(4*LEFT + 2*UP)

        x_text.add_updater(lambda m: m.become(MathTex("x=", floor_func(t.get_value())).move_to(4*LEFT + 2*UP)))

        self.play(Create(axes), Write(axis_labels), Write(eq1))
        self.play(Create(graph), Write(x_text), run_time=1)
        self.play(Create(dot))
        self.play(t.animate.set_value(2), run_time=3, rate_func=linear)
        self.wait(1)

        self.play(FadeOut(dot), FadeOut(graph), FadeOut(x_text), FadeOut(eq1), run_time=1)

        self.next_section()

        t = ValueTracker(-2)

        def func2(x):
            return 2*x

        graph = axes.plot(func2)

        initial_point = axes.c2p(-2, func2(-2))
        dot = Dot(point=initial_point, color=RED)

        dot.add_updater(lambda m: m.move_to(axes.c2p(t.get_value(), func2(t.get_value()))))

        eq2 = MathTex("f(x) = 2x").move_to(4*RIGHT + 2*UP)

        x_text = MathTex("x=", t.get_value()).move_to(4*LEFT + 2*UP)

        x_text.add_updater(lambda m: m.become(MathTex("x=", floor_func(t.get_value())).move_to(4*LEFT + 2*UP)))

        self.play(Create(graph), Write(eq2), run_time=1)
        self.play(Create(dot), Write(x_text))
        self.play(t.animate.set_value(2), run_time=3, rate_func=linear)
        self.wait(1)



