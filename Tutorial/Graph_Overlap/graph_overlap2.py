from manim import *
import numpy as np

class OneGraphOverlapping2(Scene):
    def construct(self):

        title = Text("Graph Overlap Problem", font_size=40, font = "Castellar").set_color_by_gradient(BLUE_C, GREEN_C)


        #ADD BACKGROUND
        background = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=BLACK,   
            fill_opacity=1,
            stroke_width=0
        )

        #CREATE AXES
        axes1 = Axes(x_range=[-3,3], y_range=[-3,3]).scale(0.5).add_coordinates()
        axes2 = Axes(x_range=[-3,3], y_range=[-3,3]).scale(0.5).add_coordinates()
        VGroup(title,axes1, axes2).arrange(DOWN, buff=0.5)

        #CREATE DISPLAY RECTANGLE
        rectangle_display_1 =  Rectangle(
            width=axes1.width,
            height=axes1.height,
            fill_color=RED,   
            fill_opacity=0,
            stroke_width=0
        ).move_to(axes1.get_center())

        rectangle_display_2 =  Rectangle(
            width=axes2.width,
            height=axes2.height,
            fill_color=RED,   
            fill_opacity=0,
            stroke_width=0
        ).move_to(axes2.get_center())

        shape_with_hole = Difference(background, rectangle_display_1)
        shape_with_hole = Difference(shape_with_hole, rectangle_display_2)

        shape_with_hole.set_fill(color=BLACK, opacity=1).set_stroke(width=0)


        #CREATE GRAPHS
        g1 = axes1.plot(lambda x: x**3, color=BLUE, x_range=axes1.x_range)
        g2 = axes2.plot(lambda x: x**3, color=RED, x_range=axes2.x_range)

        #SET Z-INDEX
        title.set_z_index(5)
        shape_with_hole.set_z_index(3)
        g1.set_z_index(2)
        axes1.set_z_index(2)
        g2.set_z_index(1)
        axes2.set_z_index(1)

        #CREATE BORDER

        border = SurroundingRectangle(rectangle_display_1, color=GRAY)
        border2 = SurroundingRectangle(rectangle_display_2, color=GRAY)
        border.set_z_index(4)
        border2.set_z_index(4)

        #CREATE ANIMATION
        self.add(title, shape_with_hole, border, border2)
        self.add(axes1, axes2)
        self.play(Create(g1), Create(g2))
        #self.play(a.animate.set_value(2), run_time=2)

        self.wait()