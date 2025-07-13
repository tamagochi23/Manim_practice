from manim import *
class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(72)
        line1 = Line(LEFT,RIGHT)
        line_moving  = Line(LEFT, RIGHT).set_color(BLUE)
        line_ref = line_moving.copy().set_color(BLUE)
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES,
            about_point=rotation_center
        )
        a = Angle(
            line1, line_moving, radius=0.5,
            other_angle=False
        ).set_color(RED)

        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF,
                other_angle=False
            ).point_from_proportion(0.5)
        )

        self.add(line1, line_moving,a, tex)
        self.wait(1)

        line_moving.add_updater(
            lambda m: m.become(line_ref.copy()).rotate( 
                theta_tracker.get_value() * DEGREES,
                about_point=rotation_center
            )
        )

        a.add_updater(
            lambda m: m.become(
                Angle(
                    line1, line_moving, radius=0.5,
                    other_angle=False
                ).set_color(RED)
            )
        )

        tex.add_updater(
            lambda m: m.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF,
                    other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(theta_tracker.animate.set_value(355))


