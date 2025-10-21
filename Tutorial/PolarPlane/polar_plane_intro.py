from manim import *

class PolarPlaneIntro(Scene):
    def construct(self):
        polar_plane = PolarPlane(size=8, azimuth_units="PI radians")
        a = ValueTracker(2)
        r = lambda theta: 3*np.sin(a.get_value()*theta)
        graph = polar_plane.plot_polar_graph(r, [0, 2*PI],color=RED_E)

        graph.add_updater(
            lambda m: m.become(polar_plane.plot_polar_graph(r, [0, 2*PI], color=RED_E))
        )
        
        self.add(polar_plane, graph)
        self.play(a.animate.set_value(7), run_time=6)
        self.wait()