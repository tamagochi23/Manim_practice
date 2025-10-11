from manim import *

class GetRiemannRectangles(Scene):

    def calculate_riemann_sum(self, func, a, b, dx):
        n = int(np.floor((b-a)/dx))
        total_sum = 0
        for i in range(n):
            x_i = a + i*dx
            total_sum += func(x_i) * dx
        return total_sum

    def construct(self):
        ax = Axes(
                y_range = [-1,1],
                x_range = [0,2*PI],
                tips = False,
                x_axis_config={"include_numbers": True, "font_size": 36, "numbers_to_include": [0]},
                y_axis_config={"include_numbers": True, "font_size": 56, "numbers_to_include": [-1,0,1]}
            ).scale(0.8)
        graph = ax.plot(lambda x: np.sin(x), x_range = [0,2*PI], color = BLUE)

        i = 0
        n_values = [2, 5, 10, 20, 33, 55]
        n = n_values[i]
        dx = np.pi/n

        title = MathTex(r"\int_0^{\pi} \sin(x) \, dx = 2", font_size = 48).to_edge(UP+LEFT*5)

        sum_riemann_value = self.calculate_riemann_sum(lambda x: np.sin(x), 0, PI, dx)

        sum_riemann_text = MathTex(r"\sum_{i=1}^{",f"{n}", "}", "\sin(x_i)", f"{round(dx,2):.2f}", f"={round(sum_riemann_value,3)}", font_size = 48).to_edge(UP+RIGHT*5)

        origin_label = MathTex("0", font_size = 48).next_to(ax.c2p(0,0), DOWN*4.5+RIGHT*0.5)
        pi_label = MathTex(r"\pi", font_size = 48).next_to(ax.c2p(PI,0), DOWN*4.5)
        a = VGroup(ax,graph).to_edge(DOWN)

        self.play(Write(title), Write(sum_riemann_text))
        self.play(FadeIn(a), FadeIn(origin_label), FadeIn(pi_label))

        rects_initial = ax.get_riemann_rectangles(
            graph,
            x_range = [0, PI],
            dx = dx,
            color = ORANGE
        )

        self.play(Create(rects_initial), run_time = 2)
        self.wait(1)

        sum_riemann_text.add_updater(
            lambda x: x.become(MathTex(r"\sum_{i=1}^{",f"{n}", "}", "\sin(x_i)", f"{round(dx,2):.2f}", f"={round(sum_riemann_value,3)}", font_size = 48).to_edge(UP+RIGHT*5))
        )

        i += 1

        n_values = [2, 5, 10, 20, 33, 55]
        n = n_values[i]
        dx = np.pi/n


        while True:
            rects_next = ax.get_riemann_rectangles(
                graph,
                x_range = [0, PI],
                dx = dx,
                color = ORANGE
            )
            sum_riemann_value = self.calculate_riemann_sum(lambda x: np.sin(x), 0, PI, dx)
            self.play(ReplacementTransform(rects_initial, rects_next), run_time = 1.5)
            self.wait(1)
            n = n_values[i]
            dx = np.pi/n
            i += 1
            rects_initial = rects_next
            if i > 5:
                break

        



