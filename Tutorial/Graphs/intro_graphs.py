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

class TwoGraphs(Scene):
    def construct(self):

        def func1(x):
            return x**2

        def func2(x):
            return 2*x

        eq1 = MathTex("f(x) = x^2").set_color(ORANGE).scale(1)
        eq2 = MathTex("f'(x) = 2x").set_color(ORANGE).scale(1)

        ax1 = NumberPlane((-3,3), (-4,4)).add_coordinates().scale(0.8)
        ax2 = NumberPlane((-3,3), (-4,4)).add_coordinates().scale(0.8)

        a = VGroup(eq1, ax1).arrange(DOWN, buff=0.1)
        b = VGroup(eq2, ax2).arrange(DOWN, buff=0.1)

        VGroup(a, b).arrange()        
        graph1 = ax1.plot(func1, color=GREEN)
        graph2 = ax2.plot(func2, color=GREEN)
        dot1 = Dot(point=ax1.c2p(-2, func1(-2)), color=RED)
        dot2 = Dot(point=ax2.c2p(-2, func2(-2)), color=RED)


        t = ValueTracker(-2)

        dot1.add_updater(lambda m: m.move_to(ax1.c2p(t.get_value(), func1(t.get_value()))))
        dot2.add_updater(lambda m: m.move_to(ax2.c2p(t.get_value(), func2(t.get_value()))))

        line_1 = ax1.get_vertical_line(ax1.input_to_graph_point(-2, graph1), color = RED, stroke_width=5)
        line_2 = ax1.get_horizontal_line(ax1.input_to_graph_point(-2, graph1), color = RED, stroke_width=5)

        line_1.add_updater(lambda m: m.become(ax1.get_vertical_line(ax1.input_to_graph_point(t.get_value(), graph1), color = RED, stroke_width=5)))
        line_2.add_updater(lambda m: m.become(ax1.get_horizontal_line(ax1.input_to_graph_point(t.get_value(), graph1), color = RED, stroke_width=5)))

        line_3 = ax2.get_vertical_line(ax2.input_to_graph_point(-2, graph2), color = RED, stroke_width=5)
        line_4 = ax2.get_horizontal_line(ax2.input_to_graph_point(-2, graph2), color = RED, stroke_width=5)

        line_3.add_updater(lambda m: m.become(ax2.get_vertical_line(ax2.input_to_graph_point(t.get_value(), graph2), color = RED, stroke_width=5)))
        line_4.add_updater(lambda m: m.become(ax2.get_horizontal_line(ax2.input_to_graph_point(t.get_value(), graph2), color = RED, stroke_width=5)))

        self.add(ax1, ax2, eq1, eq2, graph1, graph2)
        self.add(line_1, line_2, line_3, line_4)
        self.play(Create(dot1), Create(dot2))
        self.wait(0.5)
        self.play(t.animate.set_value(2), run_time=10, rate_func=linear)


class Love_graph(Scene):

    def func(self,t):
        return (16*np.sin(t)**3,
        13*np.cos(t),
        0)

    def construct(self):
        axes = Axes(x_range=[-16, 16],
                    y_range=[-15, 15],
                    axis_config={"color": BLUE},
                    x_length = 8,
                    y_length = 6
                    )
        func = ParametricFunction(self.func, t_range = (0,TAU), color=RED)

        self.play(Create(axes))
        self.add(func.scale(2))
        self.wait(1)


class TwoGraphsVertical(Scene):
    def construct(self):

            def func1(x):
                return x**3

            def func2(x):
                return 3*x**2

            eq1 = MathTex("f(x) = x^3").set_color(ORANGE).scale(1)
            eq2 = MathTex("f'(x) = 3x^2").set_color(ORANGE).scale(1)

            ax1 = Axes(x_range=[-3, 3], y_range=[-4, 4], axis_config={"color": BLUE}, x_length=8, y_length=6, tips = False).add_coordinates().scale(0.8)
            ax2 = Axes(x_range=[-3, 3], y_range=[-4, 4], axis_config={"color": BLUE}, x_length=8, y_length=6, tips = False).add_coordinates().scale(0.8)

            a = VGroup(eq1, ax1).arrange(DOWN, buff=0.1)
            b = VGroup(eq2, ax2).arrange(DOWN, buff=0.1)

            VGroup(a, b).arrange()
            graph1 = ax1.plot(func1, color=GREEN, x_range=[-2, 2])
            graph2 = ax2.plot(func2, color=GREEN, x_range=[-2, 2])
            dot1 = Dot(point=ax1.c2p(-1.5, func1(-1.5)), color=RED)
            dot2 = Dot(point=ax2.c2p(-1.5, func2(-1.5)), color=RED)


            t = ValueTracker(-1.5)

            dot1.add_updater(lambda m: m.move_to(ax1.c2p(t.get_value(), func1(t.get_value()))))
            dot2.add_updater(lambda m: m.move_to(ax2.c2p(t.get_value(), func2(t.get_value()))))

            line_1 = ax1.get_vertical_line(ax1.input_to_graph_point(-1.5, graph1), color = RED, stroke_width=5)
            line_2 = ax1.get_horizontal_line(ax1.input_to_graph_point(-1.5, graph1), color = RED, stroke_width=5)

            line_1.add_updater(lambda m: m.become(ax1.get_vertical_line(ax1.input_to_graph_point(t.get_value(), graph1), color = RED, stroke_width=5)))
            line_2.add_updater(lambda m: m.become(ax1.get_horizontal_line(ax1.input_to_graph_point(t.get_value(), graph1), color = RED, stroke_width=5)))

            line_3 = ax2.get_vertical_line(ax2.input_to_graph_point(-1.5, graph2), color = RED, stroke_width=5)
            line_4 = ax2.get_horizontal_line(ax2.input_to_graph_point(-1.5, graph2), color = RED, stroke_width=5)

            line_3.add_updater(lambda m: m.become(ax2.get_vertical_line(ax2.input_to_graph_point(t.get_value(), graph2), color = RED, stroke_width=5)))
            line_4.add_updater(lambda m: m.become(ax2.get_horizontal_line(ax2.input_to_graph_point(t.get_value(), graph2), color = RED, stroke_width=5)))

            self.add(ax1, ax2, eq1, eq2, graph1, graph2)
            self.add(line_1, line_2, line_3, line_4)
            self.play(Create(dot1), Create(dot2))
            self.wait(0.5)
            self.play(t.animate.set_value(1.5), run_time=15, rate_func=linear)
