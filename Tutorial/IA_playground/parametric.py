from manim import *
import numpy as np

class FourGraphsGrid(Scene):
    def construct(self):
        # Create 4 axes
        axes1 = Axes(x_range=[-3,3], y_range=[-3,3]).scale(0.5)
        axes2 = Axes(x_range=[-3,3], y_range=[-3,3]).scale(0.5)
        axes3 = Axes(x_range=[-3,3], y_range=[-3,3]).scale(0.5)
        axes4 = Axes(x_range=[-3,3], y_range=[-3,3]).scale(0.5)

        # Arrange in 2x2 grid
        grid = VGroup(axes1, axes2, axes3, axes4).arrange_in_grid(2, 2, buff=1)

        # Graphs
        g1 = axes1.plot(lambda x: x, color=BLUE)
        g2 = axes2.plot(lambda x: x**2, color=RED)
        g3 = axes3.plot(lambda x: np.sin(x), color=GREEN)
        g4 = axes4.plot(lambda x: np.cos(x), color=YELLOW)

        graphs = VGroup(g1, g2, g3, g4)

        self.play(Create(grid))
        self.play(Create(graphs))

        self.wait()


class FourGraphsAnimated(Scene):
    def construct(self):
        a = ValueTracker(1)

        # Create 4 axes
        axes = VGroup(*[
            Axes(x_range=[-3,3], y_range=[-3,3]).scale(0.5)
            for _ in range(4)
        ]).arrange_in_grid(2, 2, buff=1)

        boxes = VGroup(*[
            SurroundingRectangle(ax, color=GRAY)
            for ax in axes
            ])
        self.add(boxes)

        # Define animated graphs
        graphs = VGroup(
            always_redraw(lambda: axes[0].plot(
                lambda x: a.get_value() * x, color=BLUE
            )),
            always_redraw(lambda: axes[1].plot(
                lambda x: a.get_value() * x**2, color=RED
            )),
            always_redraw(lambda: axes[2].plot(
                lambda x: np.sin(a.get_value() * x), color=GREEN
            )),
            always_redraw(lambda: axes[3].plot(
                lambda x: np.cos(a.get_value() * x), color=YELLOW
            )),
        )

        self.add(axes, graphs)

        # Animate parameter a → all graphs update together
        self.play(
            a.animate.set_value(3),
            run_time=4,
            rate_func=linear
        )

        self.wait()


class MaskedDashboard(Scene):
    def construct(self):
        a = ValueTracker(1)

        panels = VGroup()

        functions = [
            lambda x: a.get_value() * x,
            lambda x: a.get_value() * x**2,
            lambda x: np.sin(a.get_value() * x),
            lambda x: np.cos(a.get_value() * x),
        ]

        titles_tex = ["y=ax", "y=ax^2", "y=\\sin(ax)", "y=\\cos(ax)"]
        colors = [BLUE, RED, GREEN, YELLOW]

        for func, title_tex, color in zip(functions, titles_tex, colors):
            ax = Axes(
                x_range=[-3, 3],
                y_range=[-3, 3],
                x_length=3,
                y_length=3,
                axis_config={"include_ticks": False}
            )

            graph = always_redraw(
                lambda ax=ax, func=func, color=color: ax.plot(
                    func,
                    x_range=[-3, 3],
                    color=color
                )
            )

            title = MathTex(title_tex).scale(0.5).next_to(ax, UP, buff=0.2)

            panel = VGroup(ax, graph, title)

            # 🔥 Create mask (this is the key)
            mask = Rectangle(
                width=3.2,
                height=3.2
            ).move_to(ax)

            panel.set_clip_path(mask)  # 👈 apply to whole panel

            # Optional border (visual panel)
            border = SurroundingRectangle(panel, color=GRAY, buff=0.2)

            panels.add(VGroup(panel, border))

        # Arrange panels
        panels.arrange_in_grid(2, 2, buff=1.5)

        # Parameter label
        param_label = always_redraw(
            lambda: MathTex(f"a = {a.get_value():.2f}")
            .scale(0.8)
            .to_edge(UP)
        )

        self.add(panels, param_label)

        # Animate
        self.play(
            a.animate.set_value(3),
            run_time=5,
            rate_func=linear
        )

        self.wait()