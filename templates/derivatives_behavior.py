from manim import *

class DerivativesBehavior(Scene):
    def construct(self):
      
        
        def func1(x):
            return np.log(x)

        def func2(x):
            return 1/x

        eq1 = MathTex("f(x) = \ln(x)").set_color(ORANGE).scale(1)
        eq2 = MathTex("f'(x) = \\frac{1}{x}").set_color(ORANGE).scale(1)

        ax1 = Axes(x_range=[0, 3], y_range=[-3, 4], axis_config={"color": BLUE}, x_length=8, y_length=6, tips = False).add_coordinates().scale(0.7)
        ax2 = Axes(x_range=[0, 3], y_range=[-3, 4], axis_config={"color": BLUE}, x_length=8, y_length=6, tips = False).add_coordinates().scale(0.7)

        title = Text("Function behavior and its Derivative").scale(0.7)

        a = VGroup(eq1, ax1).arrange(DOWN, buff=0.1)
        b = VGroup(eq2, ax2).arrange(DOWN, buff=0.1)


        c = VGroup(a, b).arrange()
        #VGroup(title, c).arrange(DOWN, buff=1.5)
        title.next_to(c, UP, buff=0.8)
        c.shift(DOWN*0.3)

        x_start = 0.15
        x_end = 3

        graph1 = ax1.plot(func1, color=GREEN, x_range=[x_start, x_end])
        graph2 = ax2.plot(func2, color=GREEN, x_range=[x_start, x_end])
        dot1 = Dot(point=ax1.c2p(x_start, func1(x_start)), color=RED)
        dot2 = Dot(point=ax2.c2p(x_start, func2(x_start)), color=RED)


        t = ValueTracker(x_start)

        dot1.add_updater(lambda m: m.move_to(ax1.c2p(t.get_value(), func1(t.get_value()))))
        dot2.add_updater(lambda m: m.move_to(ax2.c2p(t.get_value(), func2(t.get_value()))))

        line_1 = ax1.get_vertical_line(ax1.input_to_graph_point(x_start, graph1), color = RED, stroke_width=5)
        line_2 = ax1.get_horizontal_line(ax1.input_to_graph_point(x_start, graph1), color = RED, stroke_width=5)

        line_1.add_updater(lambda m: m.become(ax1.get_vertical_line(ax1.input_to_graph_point(t.get_value(), graph1), color = RED, stroke_width=5)))
        line_2.add_updater(lambda m: m.become(ax1.get_horizontal_line(ax1.input_to_graph_point(t.get_value(), graph1), color = RED, stroke_width=5)))

        line_3 = ax2.get_vertical_line(ax2.input_to_graph_point(x_start, graph2), color = RED, stroke_width=5)
        line_4 = ax2.get_horizontal_line(ax2.input_to_graph_point(x_start, graph2), color = RED, stroke_width=5)

        line_3.add_updater(lambda m: m.become(ax2.get_vertical_line(ax2.input_to_graph_point(t.get_value(), graph2), color = RED, stroke_width=5)))
        line_4.add_updater(lambda m: m.become(ax2.get_horizontal_line(ax2.input_to_graph_point(t.get_value(), graph2), color = RED, stroke_width=5)))
        logo = ImageMobject("./media/images/logo_pi_x_bit.jpg")

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(logo.scale(0.25).to_corner(DR).shift(DOWN*0.5 + RIGHT*0.5)))
        self.play(Create(ax1), Write(eq1),Create(ax2), Write(eq2))
        self.play(Create(graph1), Create(graph2))
        self.add(line_1, line_2, line_3, line_4)
        self.wait(1)
        self.play(Create(dot1), Create(dot2))
        self.wait(0.5)
        self.play(t.animate.set_value(3), run_time=10, rate_func=linear)
