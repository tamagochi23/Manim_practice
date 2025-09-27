from manim import *

class GetRiemannRectangles(Scene):
    def construct(self):
        ax = Axes(
                y_range = [-1,1],
                x_range = [0,2*PI],
                tips = False,
                x_axis_config={"include_numbers": True, "font_size": 36, "numbers_to_include": [0]},
                y_axis_config={"include_numbers": True, "font_size": 56, "numbers_to_include": [-1,0,1]}
            ).scale(0.8)
        graph = ax.plot(lambda x: np.sin(x), x_range = [0,2*PI], color = BLUE)


        title = MathTex(r"\int_0^{\pi} \sin(x) \, dx = 2", font_size = 48).to_edge(UP)

        sum_riemann_text = MathTex(r"\sum_{i=1}^{n} f(x_i^*) \Delta x", f"= ", font_size = 48).to_edge(DOWN)

        a = VGroup(ax,graph).to_edge(DOWN)
        b = VGroup(title,sum_riemann_text).arrange(RIGHT, buff = 2).to_edge(UP)
        c = VGroup(b,a).arrange(DOWN, buff = 1)

        self.play(Write(title), Write(sum_riemann_text))
        self.add(a)

        i = 1

        n = PI/0.4

        rects_initial = ax.get_riemann_rectangles(
            graph,
            x_range = [0, PI],
            dx = 0.4,
            color = ORANGE
        )

        self.play(Create(rects_initial), run_time = 1.5)


        while True:

            rects_next = ax.get_riemann_rectangles(
                graph,
                x_range = [0, PI],
                dx = 0.5-(i*0.1),
                color = ORANGE
            )
            self.play(ReplacementTransform(rects_initial, rects_next), run_time = 1.5)
            i += 1
            rects_initial = rects_next
            if i > 4:
                break

        



