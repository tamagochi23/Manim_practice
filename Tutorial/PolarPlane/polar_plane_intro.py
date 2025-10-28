from manim import *

class PolarPlaneIntro(Scene):
    def construct(self):
        polar_plane = PolarPlane(size=6, azimuth_units="PI radians").set_color(BLUE_E).move_to(DOWN*0.5)
        a = ValueTracker(1)
        r = lambda theta: 3*np.sin(a.get_value()*theta)
        graph = polar_plane.plot_polar_graph(r, [0, 2*PI],color=RED_E)
        polar_eq = MathTex(r"r = 3\sin(", "a", r"\theta)", font_size=50).move_to(3.5*UP)
        polar_eq[1].set_color(PURPLE_A)

        a_text = MathTex("a = 1.00", font_size=50).move_to(2.7*UP + 3.7*LEFT).set_color(PURPLE_A)  

        graph.add_updater(
            lambda m: m.become(polar_plane.plot_polar_graph(r, [0, 2*PI], color=RED_E))
        )

        a_text.add_updater(lambda m: m.become(MathTex(f"a = {a.get_value():.2f}", font_size=50).move_to(2.5*UP + 3.7*LEFT).set_color(PURPLE_A)))

        self.add(polar_plane, graph, polar_eq, a_text)
        self.play(a.animate.set_value(3), run_time=6)
        self.wait()

class PolarPlane_2(Scene):
    def construct(self):
        polar_plane = PolarPlane(size=8, azimuth_units="PI radians")
        a = ValueTracker(0.5)
        r = lambda theta: 3*np.sin(a.get_value()*(theta**2))
        graph = polar_plane.plot_polar_graph(r, [0, 2*PI],color=RED_E)

        graph.add_updater(
            lambda m: m.become(polar_plane.plot_polar_graph(r, [0, 2*PI], color=RED_E))
        )
        
        self.add(polar_plane, graph)
        self.play(a.animate.set_value(7), run_time=6)
        self.wait()

class PolarPlane_3(Scene):
    def construct(self):
        polar_plane = PolarPlane(size=8, azimuth_units="PI radians")
        a = ValueTracker(0.2)
        r = lambda theta: a.get_value() - np.cos(theta)
        graph = polar_plane.plot_polar_graph(r, [0, 2*PI],color=RED_E)

        graph.add_updater(
            lambda m: m.become(polar_plane.plot_polar_graph(r, [0, 2*PI], color=RED_E))
        )
        
        self.add(polar_plane, graph)
        self.play(a.animate.set_value(2), run_time=6)
        self.wait()