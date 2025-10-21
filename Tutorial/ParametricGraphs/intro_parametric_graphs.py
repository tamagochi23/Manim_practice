from manim import *

class ParametricGraphExample(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-2, 2],
            x_length=6,
            y_length=4,
            axis_config={"color": BLUE},
            tips=False,
        ).scale(1.5)
        
        a = 2
        b = 1

        parametric_curve = ParametricFunction(
            lambda t: np.array([
                np.cos(2*t),
                np.sin(1*t),
                0
            ]),
            t_range=[-PI, PI],
            color=RED
        ).scale(1.5)
        


        self.add(axes)
        self.play(Create(parametric_curve), run_time=4)
        self.wait(1)
        self.wait()

class ParametricGraphUpdater(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-2, 2],
            x_length=6,
            y_length=4,
            axis_config={"color": BLUE},
            tips=False,
        ).scale(1.5)
        
        a = ValueTracker(1)
        b = ValueTracker(1)

        parametric_curve = ParametricFunction(
            lambda t: np.array([
                np.cos(a.get_value()*t),
                np.sin(b.get_value()*t),
                0
            ]),
            t_range=[-PI, PI],
            color=RED
        ).scale(1.5)
        
        parametric_curve.add_updater(
            lambda m: m.become(
                ParametricFunction(
                    lambda t: np.array([
                        np.cos(a.get_value()*t),
                        np.sin(b.get_value()*t),
                        0
                    ]),
                    t_range=[-PI, PI],
                    color=RED
                ).scale(1.5)
            )
        )

        parametric_text = MathTex(r"f(t) = ( \cos(","a",r"t), \sin(", "b", r"t) )", font_size=50).move_to(3.5*UP)

        parametric_text[1].set_color(PURPLE_A)
        parametric_text[3].set_color(GREEN)

        a_text = MathTex("a = 1.00", font_size=50).move_to(2.7*UP + 3.7*LEFT).set_color(PURPLE_A)  
        b_text = MathTex("b = 1.00", font_size=50).move_to(2.7*UP + 3.7*RIGHT).set_color(GREEN)

        a_text.add_updater(lambda m: m.become(MathTex(f"a = {a.get_value():.2f}", font_size=50).move_to(2.5*UP + 3.7*LEFT).set_color(PURPLE_A)))
        b_text.add_updater(lambda m: m.become(MathTex(f"b = {b.get_value():.2f}", font_size=50).move_to(2.5*UP + 3.7*RIGHT).set_color(GREEN)))

        self.add(axes, a_text, b_text, parametric_text) 
        self.play(Create(parametric_curve), run_time=2)
        self.wait(1)
        self.play(a.animate.set_value(4),run_time=8)
        self.play(b.animate.set_value(4),run_time=8)
        self.wait()

class ParametricGraphUpdater_2(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-2, 2],
            x_length=6,
            y_length=4,
            axis_config={"color": BLUE},
            tips=False,
        ).scale(1.5)
        
        a = ValueTracker(1)
        b = ValueTracker(1)

        parametric_curve = ParametricFunction(
            lambda t: np.array([
                np.sin(a.get_value()*t + t/6),
                np.cos(b.get_value()*t - t/6),
                0
            ]),
            t_range=[-PI, PI],
            color=RED
        ).scale(1.5)
        
        parametric_curve.add_updater(
            lambda m: m.become(
                ParametricFunction(
                    lambda t: np.array([
                        np.sin(a.get_value()*t + t/6),
                        np.cos(b.get_value()*t - t/6),
                        0
                    ]),
                    t_range=[-PI, PI],
                    color=RED
                ).scale(1.5)
            )
        )

        parametric_text = MathTex(r"f(t) = ( \sin(","a",r"t + t/6), \cos(", "b", r"t - t/6) )", font_size=50).move_to(3.5*UP)

        parametric_text[1].set_color(PURPLE_A)
        parametric_text[3].set_color(GREEN)

        a_text = MathTex("a = 1.00", font_size=50).move_to(2.7*UP + 3.7*LEFT).set_color(PURPLE_A)  
        b_text = MathTex("b = 1.00", font_size=50).move_to(2.7*UP + 3.7*RIGHT).set_color(GREEN)

        a_text.add_updater(lambda m: m.become(MathTex(f"a = {a.get_value():.2f}", font_size=50).move_to(2.5*UP + 3.7*LEFT).set_color(PURPLE_A)))
        b_text.add_updater(lambda m: m.become(MathTex(f"b = {b.get_value():.2f}", font_size=50).move_to(2.5*UP + 3.7*RIGHT).set_color(GREEN)))

        self.add(axes, a_text, b_text, parametric_text) 
        self.play(Create(parametric_curve), run_time=2)
        self.wait(1)
        self.play(a.animate.set_value(4), run_time=8)
        # self.play(a.animate.set_value(4),run_time=8)
        self.play(b.animate.set_value(4),run_time=8)
        self.wait()

class ParametricGraphUpdater_3(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-2, 2],
            x_length=6,
            y_length=4,
            axis_config={"color": BLUE},
            tips=False,
        ).scale(1.5)
        
        a = ValueTracker(1)
        b = ValueTracker(1)

        parametric_curve = ParametricFunction(
            lambda t: np.array([
                np.sin(a.get_value()*(t**2)),
                np.cos(b.get_value()*(t**2)),
                0
            ]),
            t_range=[-PI, PI],
            color=RED
        ).scale(1.5)
        
        parametric_curve.add_updater(
            lambda m: m.become(
                ParametricFunction(
                    lambda t: np.array([
                        np.sin(a.get_value()*(t**2)),
                        np.cos(b.get_value()*(t**2)),
                        0
                    ]),
                    t_range=[-PI, PI],
                    color=RED
                ).scale(1.5)
            )
        )

        parametric_text = MathTex(r"f(t) = ( \sin(","a",r"t^2), \cos(", "b", r"t^2) )", font_size=50).move_to(3.5*UP)

        parametric_text[1].set_color(PURPLE_A)
        parametric_text[3].set_color(GREEN)

        a_text = MathTex("a = 1.00", font_size=50).move_to(2.7*UP + 3.7*LEFT).set_color(PURPLE_A)  
        b_text = MathTex("b = 1.00", font_size=50).move_to(2.7*UP + 3.7*RIGHT).set_color(GREEN)

        a_text.add_updater(lambda m: m.become(MathTex(f"a = {a.get_value():.2f}", font_size=50).move_to(2.5*UP + 3.7*LEFT).set_color(PURPLE_A)))
        b_text.add_updater(lambda m: m.become(MathTex(f"b = {b.get_value():.2f}", font_size=50).move_to(2.5*UP + 3.7*RIGHT).set_color(GREEN)))

        self.add(axes, a_text, b_text, parametric_text) 
        self.play(Create(parametric_curve), run_time=2)
        self.wait(1)
        self.play(a.animate.set_value(4), run_time=8)
        # self.play(a.animate.set_value(4),run_time=8)
        self.play(b.animate.set_value(4),run_time=8)
        self.wait()

class ParametricGraphUpdater_4(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-2, 2],
            x_length=6,
            y_length=4,
            axis_config={"color": BLUE},
            tips=False,
        ).scale(1.5)
        
        a = ValueTracker(1)
        b = ValueTracker(1)

        parametric_curve = ParametricFunction(
            lambda t: np.array([
                np.exp(t/6)*np.sin(a.get_value()*(2*t)),
                np.exp(t/6)*np.cos(b.get_value()*(2*t)),
                0
            ]),
            t_range=[-PI, PI],
            color=RED
        ).scale(1.5)
        
        parametric_curve.add_updater(
            lambda m: m.become(
                ParametricFunction(
                    lambda t: np.array([
                        np.exp(t/6)*np.sin(a.get_value()*(2*t)),
                        np.exp(t/6)*np.cos(b.get_value()*(2*t)),
                        0
                    ]),
                    t_range=[-PI, PI],
                    color=RED
                ).scale(1.5)
            )
        )

        parametric_text = MathTex(r"f(t) = ( \sin(","a",r"t^2), \cos(", "b", r"t^2) )", font_size=50).move_to(3.5*UP)

        parametric_text[1].set_color(PURPLE_A)
        parametric_text[3].set_color(GREEN)

        a_text = MathTex("a = 1.00", font_size=50).move_to(2.7*UP + 3.7*LEFT).set_color(PURPLE_A)  
        b_text = MathTex("b = 1.00", font_size=50).move_to(2.7*UP + 3.7*RIGHT).set_color(GREEN)

        a_text.add_updater(lambda m: m.become(MathTex(f"a = {a.get_value():.2f}", font_size=50).move_to(2.5*UP + 3.7*LEFT).set_color(PURPLE_A)))
        b_text.add_updater(lambda m: m.become(MathTex(f"b = {b.get_value():.2f}", font_size=50).move_to(2.5*UP + 3.7*RIGHT).set_color(GREEN)))

        self.add(axes, a_text, b_text, parametric_text) 
        self.play(Create(parametric_curve), run_time=2)
        self.wait(1)
        self.play(a.animate.set_value(4), run_time=8)
        # self.play(a.animate.set_value(4),run_time=8)
        self.play(b.animate.set_value(4),run_time=8)
        self.wait()