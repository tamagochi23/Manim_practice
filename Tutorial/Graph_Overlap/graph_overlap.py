from manim import *
import numpy as np

class OneGraphOverlapping(Scene):
    def construct(self):
        axes1 = Axes(x_range=[-3,3], y_range=[-3,3]).scale(0.7)
        g1 = axes1.plot(lambda x: x, color=BLUE, x_range=axes1.x_range)

        a = ValueTracker(1)

        def update_graph(m):
            new_graph = axes1.plot(lambda x: a.get_value() * x, color=BLUE, x_range=axes1.x_range)
            m.become(new_graph)

        g1.add_updater(update_graph)

        background = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=BLACK,   # same as background!
            fill_opacity=1,
            stroke_width=0
        )

        rectangle_display =  Rectangle(
            width=axes1.width,
            height=axes1.height,
            fill_color=RED,   # same as background!
            fill_opacity=0.2,
            stroke_width=0
        )


        shape_with_hole = Difference(background, rectangle_display)
        shape_with_hole.set_fill(color=BLACK, opacity=1)
        shape_with_hole.set_stroke(width=0)

        shape_with_hole.set_z_index(2)
        g1.set_z_index(1)
        axes1.set_z_index(1)

        #border = SurroundingRectangle(axes1, color=GRAY)

        self.add(shape_with_hole)
        self.add(g1, axes1)
        #self.play(Create(g1))
        self.play(a.animate.set_value(2), run_time=2)

        self.wait()