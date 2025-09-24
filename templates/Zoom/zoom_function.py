from manim import *

class Zoom_function(MovingCameraScene):
    def construct(self):
        a = self.camera.frame.save_state()

        ax = Axes(x_range = [-1,2*PI], 
                    y_range = [-1.5,1.5], 
                    tips = False,
                    axis_config={"include_numbers": True, "font_size": 36, "numbers_to_include": [0]},)
        graph = ax.plot(lambda x: np.sin(x), x_range = [0, 2*PI], color = BLUE)

        graph_2 = ax.plot(lambda x: x, x_range = [0, 1], color = GREEN)

        x_start = PI/2
        moving_dot = Dot(ax.i2gp(PI/2, graph), color = ORANGE)
        title = MathTex(r"\sin(x) \sim x, x \leqslant \frac{\pi}{6}", font_size = 50).to_edge(UP)       
        t = ValueTracker(x_start)
        grade_30_text = MathTex(r"\frac{\pi}{6}", font_size = 48).next_to(ax.coords_to_point(PI/6, 0), DOWN)
        line_30 = ax.get_vertical_line(ax.input_to_graph_point(PI/6, graph), color = RED, stroke_width=5)

        self.add(ax)
        self.play(Create(graph), Write(moving_dot), Write(title), run_time = 3)
        self.add(line_30, grade_30_text)

        x_label = ax.get_graph_label(graph_2, label = MathTex("y = x"), x_val = 1, direction = UP/2, color = GREEN)
        self.play(Create(graph_2), Write(x_label))


        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
             mob.move_to(moving_dot.get_center())

        moving_dot.add_updater(lambda m: m.move_to(ax.i2gp(t.get_value(), graph)))

        self.camera.frame.add_updater(update_curve)
        self.play(t.animate.set_value(PI/6), run_time=5, rate_func=linear)
        self.wait(1)

        error_label = MathTex("E_a = " , font_size = 10).next_to(moving_dot, UP/2 + LEFT).set_color(ORANGE)
        error_label.add_updater(lambda m: m.next_to(moving_dot, UP/2 + LEFT))
        error_value = np.abs(np.sin(t.get_value()) - t.get_value())
        error_value_text = Tex(f"{error_value:.5f}", font_size = 10).next_to(error_label, RIGHT/4).set_color(ORANGE)
        error_value_text.add_updater(lambda m: m.become(Tex(f"{np.abs(np.sin(t.get_value()) - t.get_value()):.5f}", font_size = 10).next_to(error_label, RIGHT/4).set_color(ORANGE)))

        self.add(error_label, error_value_text)
        self.play(self.camera.frame.animate.scale(0.3).move_to(moving_dot))
        self.play(t.animate.set_value(0), run_time=5, rate_func=linear)
        self.wait(1)
        self.remove(error_label,error_value_text)
        self.camera.frame.remove_updater(update_curve)
        self.play(Restore(a))