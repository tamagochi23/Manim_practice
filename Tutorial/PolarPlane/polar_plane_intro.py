from manim import *

class PolarPlaneIntro(Scene):
    def construct(self):
        polar_plane = PolarPlane(size=6, azimuth_units="PI radians").set_color(BLUE_E).move_to(RIGHT*2+DOWN*0.5)
        a = ValueTracker(1)
        r = lambda theta: 3*np.sin(a.get_value()*theta)
        graph = polar_plane.plot_polar_graph(r, [0, 2*PI],color=RED_E)

        title = Text("Polar Coordinates", font_size=40, font = "Castellar").move_to(3.5*UP).set_color_by_gradient(BLUE_C, GREEN_C)

        polar_eq = MathTex(r"r = 3\sin(", "a", r"\theta)", font_size=60).move_to(4.0*LEFT + 1*UP)
        polar_eq[1].set_color(PURPLE_A)

        a_text = MathTex("a = 1.00", font_size=60).move_to(4.0*LEFT).set_color(PURPLE_A)  

        graph.add_updater(
            lambda m: m.become(polar_plane.plot_polar_graph(r, [0, 2*PI], color=RED_E))
        )

        a_text.add_updater(lambda m: m.become(MathTex(f"a = {a.get_value():.2f}", font_size=60).move_to(4.0*LEFT).set_color(PURPLE_A)))

        logo = ImageMobject("../../templates/media/images/logo_pi_x_bit.jpg")

        self.add(title, polar_plane, graph, polar_eq, a_text)
        self.play(FadeIn(logo.scale(0.27).to_corner(DR)))
        self.play(a.animate.set_value(5), run_time=13)
        self.wait()

class PolarPlane_2(Scene):
    def construct(self):
        polar_plane = PolarPlane(size=6, azimuth_units="PI radians").set_color(BLUE_E).move_to(RIGHT*2+DOWN*0.5)
        a = ValueTracker(1)
        r = lambda theta: 3*np.sin((theta/a.get_value()))
        graph = polar_plane.plot_polar_graph(r, [0, 2*PI],color=RED_E)

        title = Text("Polar Coordinates", font_size=40, font = "Castellar").move_to(3.5*UP).set_color_by_gradient(BLUE_C, GREEN_C)

        polar_eq = MathTex(r"r = 3\sin(\frac{\theta}{", "a", r"})", font_size=60).move_to(4.0*LEFT + 1*UP)
        polar_eq[1].set_color(PURPLE_A)

        a_text = MathTex("a = 1.00", font_size=60).move_to(4.0*LEFT + 0.5*DOWN).set_color(PURPLE_A)  

        graph.add_updater(
            lambda m: m.become(polar_plane.plot_polar_graph(r, [0, 2*PI], color=RED_E))
        )

        a_text.add_updater(lambda m: m.become(MathTex(f"a = {a.get_value():.2f}", font_size=60).move_to(4.0*LEFT + 0.5*DOWN).set_color(PURPLE_A)))

        
        logo = ImageMobject("../../templates/media/images/logo_pi_x_bit.jpg")

        self.add(title, polar_plane, graph, polar_eq, a_text)
        self.play(FadeIn(logo.scale(0.27).to_corner(DR)))
        self.play(a.animate.set_value(16), run_time=14)
        self.wait()

class PolarPlane_3(Scene):
    def construct(self):
        polar_plane = PolarPlane(size=6, azimuth_units="PI radians").set_color(BLUE_E).move_to(RIGHT*2+DOWN*0.5)
        a = ValueTracker(0.1)
        r = lambda theta: a.get_value() - np.cos(2*theta)
        graph = polar_plane.plot_polar_graph(r, [0, 2*PI],color=RED_E)

        title = Text("Polar Coordinates", font_size=40, font = "Castellar").move_to(3.5*UP).set_color_by_gradient(BLUE_C, GREEN_C)

        polar_eq = MathTex(r"r = ", "a", r" - \cos(2\theta)", font_size=60).move_to(4.0*LEFT + 1*UP)
        polar_eq[1].set_color(PURPLE_A)

        a_text = MathTex(f"a = {a.get_value():.2f}", font_size=60).move_to(4.0*LEFT + 0.5*DOWN).set_color(PURPLE_A)  


        graph.add_updater(
            lambda m: m.become(polar_plane.plot_polar_graph(r, [0, 2*PI], color=RED_E))
        )

        a_text.add_updater(lambda m: m.become(MathTex(f"a = {a.get_value():.2f}", font_size=60).move_to(4.0*LEFT + 0.5*DOWN).set_color(PURPLE_A)))
        
        logo = ImageMobject("../../templates/media/images/logo_pi_x_bit.jpg")


        self.add(title, polar_plane, graph, polar_eq, a_text)
        self.play(FadeIn(logo.scale(0.27).to_corner(DR)))
        self.play(a.animate.set_value(3), run_time=8)
        self.play(a.animate.set_value(0.1), run_time=8)
        self.wait()

class PolarPlane_4(Scene):
    def construct(self):
        polar_plane = PolarPlane(
            radius_max=5,
            size=6, 
            azimuth_units="PI radians",
            azimuth_step=16,
            azimuth_label_font_size=33.6,
            radius_step=1,
            radius_config={"font_size": 33.6},
        ).set_color(BLUE_A).add_coordinates().move_to(RIGHT*2.5+DOWN*0.5)
        a = ValueTracker(0.1)
        r = lambda theta: np.sqrt(abs((a.get_value()**2) * 2*np.cos(a.get_value()*theta)))
        graph = polar_plane.plot_polar_graph(r, [0, 2*PI],color=RED_E)

        title = Text("Polar Coordinates", font_size=40, font = "Castellar").move_to(3.5*UP).set_color_by_gradient(BLUE_C, GREEN_C)

        polar_eq = MathTex(r"r = \sqrt{|", "a", r"^2 2\cos(","a",r"\theta)|}", font_size=60).move_to(4.0*LEFT + 1*UP)
        polar_eq[1].set_color(PURPLE_A)
        polar_eq[3].set_color(PURPLE_A)

        a_text = MathTex(f"a = {a.get_value():.2f}", font_size=60).move_to(4.0*LEFT + 0.5*DOWN).set_color(PURPLE_A)  


        graph.add_updater(
            lambda m: m.become(polar_plane.plot_polar_graph(r, [0, 2*PI], color=RED_E))
        )

        a_text.add_updater(lambda m: m.become(MathTex(f"a = {a.get_value():.2f}", font_size=60).move_to(4.0*LEFT + 0.5*DOWN).set_color(PURPLE_A)))
        
        logo = ImageMobject("../../templates/media/images/logo_pi_x_bit.jpg")


        self.add(title, polar_plane, graph, polar_eq, a_text)
        self.play(FadeIn(logo.scale(0.27).to_corner(DR)))
        self.play(a.animate.set_value(3), run_time=8)
        self.play(a.animate.set_value(0.1), run_time=8)
        self.wait()

class PolarPlane_5(Scene):
    def construct(self):
        polar_plane = PolarPlane(
            radius_max=5,
            size=6, 
            azimuth_units="PI radians",
            azimuth_step=16,
            azimuth_label_font_size=33.6,
            radius_step=1,
            radius_config={"font_size": 33.6},
        ).set_color(BLUE_E).add_coordinates().move_to(RIGHT*2.5+DOWN*0.5)
        a = ValueTracker(1)
        r = lambda theta: theta/6 - a.get_value()/6
        #r2 = lambda theta: (-theta/3) + 4
        graph = polar_plane.plot_polar_graph(r, [0, 2*PI],color=RED_E)
        #graph2 = polar_plane.plot_polar_graph(r, [0, 6*PI],color=YELLOW_E)

        title = Text("Polar Coordinates", font_size=40, font = "Castellar").move_to(3.5*UP).set_color_by_gradient(BLUE_C, GREEN_C)

        polar_eq = MathTex(r"r = \theta/6 - ","a",r"/6", font_size=60).move_to(4.0*LEFT + 1*UP)
        polar_eq2 = MathTex(r"\theta \in [","a",r", 2 \pi + 3","a",r"]", font_size=60).move_to(4.0*LEFT + 0.1*UP)
        polar_eq[1].set_color(PURPLE_A)
        polar_eq2[1].set_color(PURPLE_A)
        polar_eq2[3].set_color(PURPLE_A)

        a_text = MathTex(f"a = {a.get_value():.2f}", font_size=60).move_to(4.0*LEFT + 1.6*DOWN).set_color(PURPLE_A)  


        graph.add_updater(
            lambda m: m.become(polar_plane.plot_polar_graph(r, [a.get_value() , 2*PI+3*a.get_value()], color=RED_E))  
        )

        a_text.add_updater(lambda m: m.become(MathTex(f"a = {a.get_value():.2f}", font_size=60).move_to(4.0*LEFT + 1.6*DOWN).set_color(PURPLE_A)))
        
        logo = ImageMobject("../../templates/media/images/logo_pi_x_bit.jpg")


        self.add(title, polar_plane, graph, polar_eq, polar_eq2, a_text)
        self.play(FadeIn(logo.scale(0.1).to_corner(DR)))
        self.play(a.animate.set_value(10), run_time=12)
        #self.play(a.animate.set_value(0.1), run_time=8)
        self.wait()

class PolarPlane_6(Scene):
    def construct(self):
        polar_plane = PolarPlane(
            radius_max=5,
            size=6, 
            azimuth_units="PI radians",
            azimuth_step=16,
            azimuth_label_font_size=33.6,
            radius_step=1,
            radius_config={"font_size": 33.6},
        ).set_color(BLUE_E).add_coordinates().move_to(RIGHT*2.5+DOWN*0.5)
        a = ValueTracker(1)
        b = ValueTracker(1)
        r = lambda theta: 3*abs(np.cos(a.get_value()*theta)) + 2*abs(np.sin(b.get_value()*theta))
        #r2 = lambda theta: (-theta/3) + 4
        graph = polar_plane.plot_polar_graph(r, [0, 2*PI],color=RED_E)
        #graph2 = polar_plane.plot_polar_graph(r, [0, 6*PI],color=YELLOW_E)

        title = Text("Polar Coordinates", font_size=40, font = "Castellar").move_to(3.5*UP).set_color_by_gradient(BLUE_C, GREEN_C)

        polar_eq = MathTex(r"r = 3|\cos(", "a", r"\theta)| + 2|\sin(","b",r"\theta)|", font_size=47).move_to(4.0*LEFT + 1*UP)
        polar_eq[1].set_color(PURPLE_A)
        polar_eq[3].set_color(GREEN)

        a_text = MathTex(f"a = {a.get_value():.2f}", font_size=55).move_to(4.0*LEFT + 0.5*DOWN).set_color(PURPLE_A)  
        b_text = MathTex(f"b = {b.get_value():.2f}", font_size=55).move_to(4.0*LEFT + 1.5*DOWN).set_color(GREEN)  


        graph.add_updater(
            lambda m: m.become(polar_plane.plot_polar_graph(r, [0, 2*PI+a.get_value()*3*PI], color=RED_E))
        )

        a_text.add_updater(lambda m: m.become(MathTex(f"a = {a.get_value():.2f}", font_size=60).move_to(4.0*LEFT + 0.5*DOWN).set_color(PURPLE_A)))
        b_text.add_updater(lambda m: m.become(MathTex(f"b = {b.get_value():.2f}", font_size=60).move_to(4.0*LEFT + 1.5*DOWN).set_color(GREEN)))
                
        logo = ImageMobject("../../templates/media/images/logo_pi_x_bit.jpg")


        self.add(title, polar_plane, graph, polar_eq, a_text, b_text)
        self.play(FadeIn(logo.scale(0.19).to_corner(DR)))
        #self.play(a.animate.set_value(2), run_time=10)
        #self.play(b.animate.set_value(2), run_time=10)
        self.wait()