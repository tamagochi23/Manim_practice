from manim import *
import numpy as np

class Ecuations(Scene):
    def construct(self):
        eqn0 = MathTex("2x^2+6x+7=0").move_to(UP * 3)
        eqn1 = MathTex("x = \\frac{-b\\pm \\sqrt{b^2-4ac}} {2a}").move_to(UP*1.5)
        eqn2 = MathTex(r"x = \frac{-b\pm \sqrt{b^2-4ac}} {2a}")
        eqn3 = MathTex(r"\left(\begin{array}{cc} 1 & 2 \\ 3 & 4 \end{array}\right)").move_to(DOWN*2)
        self.play(Write(eqn0))
        self.wait(1)
        self.play(Write(eqn1))
        self.wait(1)
        self.play(Write(eqn2))
        self.wait(1)
        self.play(Write(eqn3))
        self.wait(1)

class Ecuations2(Scene):
    def construct(self):
        eqn0 = MathTex("2x^2+6x+7=0").move_to(UP).scale(1.5)
        eqn1 = MathTex("2x^2","+6x","+7","=0").move_to(DOWN).scale(1.5)
        self.play(Write(eqn0))
        self.wait(3)
        self.play(Write(eqn1[0]))
        self.wait(1)
        self.play(Write(eqn1[1]))
        self.wait(1)
        self.play(Write(eqn1[2]))
        self.wait(1)
        self.play(Write(eqn1[3]))
        self.wait(1)

class Ecuations3(Scene):
    def construct(self):
        eqn0 = MathTex("2x^2+6x+7=0").move_to(UP).scale(1.5)
        eqn1 = MathTex("{-b\\pm \\sqrt{b^2 - 4ac}}","\\over","{2a}", color=BLUE).move_to(DOWN).scale(1.5)
        eqn1[1].set_color(YELLOW)
        eqn1[2].set_color(GREEN)
        self.play(Write(eqn0))
        self.wait(3)
        self.play(Write(eqn1))
        self.wait(3)

class Equations4(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        eqn0 = MathTex("x=","2.5").move_to(UP*2 + LEFT * 2).scale(1.5)
        eqn1 = MathTex("y=","1.5").move_to(UP*2 + RIGHT * 2).scale(1.5)
        eqn0.set_color(GREEN)
        eqn1.set_color(ORANGE)
        eqn2 = MathTex("z=(" , "2.5", ")^2+(", "1.5", ")^2", color = BLUE).move_to(DOWN).scale(1.5)
        self.play(Write(eqn0))
        self.wait(3)
        self.play(Write(eqn1))
        self.wait(3)
        self.play(Write(eqn2[0]), Write(eqn2[2]), Write(eqn2[4]))
        self.wait(3)
        self.play(Transform(eqn0[1],eqn2[1]), Transform(eqn1[1],eqn2[3]))
        self.wait(3)

class GraphingMovement(Scene):
    def construct(self):


        text = Text('"Dime algo lindo"')
        text1 = Text('Automáticamente yo: ')

        self.play(Write(text))
        self.wait(2)
        self.play(Transform(text, text1), runtime = 3)
        self.wait(2)
        self.play(FadeOut(text))

        text = Text('Le dedico, las siguientes hermosas ecuaciones')
        text1 = Text('tan bonitas como usted <3')

        self.play(Write(text))
        self.wait(2)
        self.play(Transform(text, text1), runtime = 3)
        self.wait(2)
        self.play(FadeOut(text))

        axes = Axes(x_range = [-5,5,1], y_range = [-3,3,1],
        x_length = 10, y_length = 6,
        axis_config = {"include_tip":True, "numbers_to_exclude": [0]}
        ).add_coordinates()
        ##axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label = "x", y_label = "f(x)")

        graph = axes.plot(lambda x: np.sqrt(1 - (abs(x) - 1)**2), x_range = [-2,2], color = RED)
        graph2 = axes.plot(lambda x: -2.5 * np.sqrt(1 - np.sqrt(abs(x)/2)), x_range = [-2,2], color = PINK)
        graphing_stuff = VGroup(axes, graph, graph2,axis_labels)
        ##(
        eqn0 = MathTex("y_1 ="," \\sqrt{1 - (|x| - 1)^2}", color = RED).move_to(UP*3 + LEFT * 4).scale(1)
        eqn1 = MathTex("y_2 ="," -2.5\\sqrt{1 - \\sqrt{\\frac{|x|}{2}}}", color = PINK).move_to(UP*1.5 + LEFT * 4).scale(1)
        condition = MathTex("x \in [-2,2]", color = YELLOW).move_to(UP*2 + RIGHT * 2).scale(1)

        eq_stuff = VGroup(eqn0, eqn1, condition)

        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Write(graph),Write(eqn0))
        self.wait(3)
        self.play(Write(graph2),Write(eqn1))
        self.wait(3)
        self.play(Write(condition))
        self.wait(3)
        self.play(FadeOut(graphing_stuff), FadeOut(eq_stuff))

        text = Text('Para qué complicarme con palabras,\n\n si puedo expresar mi amor con ecuaciones :)')
        text1 = Text("Feliz 2 años y 8 meses, mi amor")

        self.play(Write(text))
        self.wait(2)
        self.play(Transform(text, text1), runtime = 3)
        self.wait(2)
        self.play(FadeOut(text))

        self.play(Write(text))