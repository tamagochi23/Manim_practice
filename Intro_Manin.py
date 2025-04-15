from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

class Ecuations(Scene):
    def construct(self):
        eqn0 = MathTex("2x^2+6x+7=0").move_to(UP * 3)
        eqn1 = MathTex("x = \\frac{-b\\pm \\sqrt{b^2-4ac}} {2a}").move_to(UP*1.5)
        eqn2 = MathTex(r"x = \frac{-b\pm \sqrt{b^2-4ac}} {2a}").move_to(UP*1.5)
        eqn3 = MathTex(r"\left(\begin{array}{cc} 1 & 2 \\ 3 & 4 \end{array}\right)").move_to(DOWN*2)
        self.play(Write(eqn0))
        self.wait(3)
        self.play(Write(eqn1))
        self.wait(3)
        self.play(Write(eqn2))
        self.wait(3)
        self.play(Write(eqn3))
        self.wait(3)

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
                                       
class Imagess(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        img = ImageMobject("./Images/pista.png").rotate(PI/2).scale(1.5)
        self.add(img)
        titulo = Text("Movimiento rectilineo", color = BLACK).move_to(UP * 3.5)
        self.play(Write(titulo))
        self.wait(3)
        lugar0 = ImageMobject("./Images/car.png").move_to(DOWN * 1.5 + LEFT * 4).scale(0.1)
        self.add(lugar0)
        self.wait(3)
        lugar1 = lugar0.copy().move_to(DOWN * 1.5 + RIGHT * 4)
        self.play(Transform(lugar0, lugar1), run_time = 5)
        self.wait(3)

class Graph(Scene):
    def construct(self):
        ax = Axes(x_range=[-1,14,1],
                  y_range=[-3.5,3.5,1],
                  x_length=9,
                  y_length=6,
                  tips=True,
                  axis_config={'tip_shape': StealthTip}
                  #x_axis_config={"numbers_to_include": [3.14, 6.28, 9.42, 12.56]}
                  )
        labels = ax.get_axis_labels(
            Tex("x").scale(0.7), Tex("y").scale(0.7)
        )
        p1 = MathTex('\pi').move_to(ax.coords_to_point(PI, -0.5))
        p2 = MathTex('2\pi').move_to(ax.coords_to_point(2*PI, -0.5))
        p3 = MathTex('3\pi').move_to(ax.coords_to_point(3*PI, -0.5))
        p4 = MathTex('4\pi').move_to(ax.coords_to_point(4*PI, -0.5))
        self.add(ax, p1, p2, p3, p4, labels)
        self.wait(3)
        curva0 = ax.plot(lambda x : np.sin(x), x_range=[0, 4 * PI])
        curva1 = curva0.copy()
        curva2 = ax.plot(lambda x : 3*np.sin(x), x_range=[0, 4 * PI])
        curva3 = ax.plot(lambda x : 0.5*np.sin(x), x_range=[0, 4 * PI])
        eqn0 = MathTex('y = \sin{x}').move_to(UP * 3.0).scale(2)
        eqn1 = eqn0.copy()
        eqn2 = MathTex('y = 3\sin{x}').move_to(UP * 3.0).scale(2)
        eqn3 = MathTex('y = 0.5\sin{x}').move_to(UP * 3.0).scale(2)
        self.play(Write(curva1), Write(eqn1))
        self.play(Transform(curva1, curva2), Transform(eqn1, eqn2), run_time = 3)
        self.play(Transform(curva1, curva3), Transform(eqn1, eqn3), run_time = 3)
        self.play(Transform(curva1, curva0), Transform(eqn1, eqn0), run_time = 3)
        self.wait(3)

class zoom(MovingCameraScene):
    def construct(self):
        img = ImageMobject("./Images/pista.png").rotate(PI/2).scale(1.5)
        self.add(img)
        self.wait(3)
        self.camera.frame.save_state()
        rejilla = NumberPlane().set_color(RED)
        self.add(rejilla)
        self.wait(3)
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(np.array([-3.5, 2, 0]))
        )

class Graph3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        x = MathTex("x").move_to(np.array([5,0.5,0]))
        y = MathTex("y").move_to(np.array([0.5,5,0]))
        self.set_camera_orientation(phi = 65 * DEGREES, theta= 60 * DEGREES)
        self.add(axes, x, y)
        text3d = MathTex("z=(x^2+3y^2)e^{1-x^2-y^2}").to_corner(UL)
        self.add_fixed_in_frame_mobjects(text3d)

        curve = Surface(lambda u, v: np.array([u, v, (u ** 2 + 3 * v ** 2) * np.exp(1 - u ** 2 - v ** 2)]),
                        v_range=[-3,3],
                        u_range=[-3,3],
                        checkerboard_colors=[BLUE,GREEN],
                        resolution=(15,32)
                        )
        curve.set_fill_by_checkerboard(BLUE, GREEN, opacity=0.7)
        self.play(Write(curve))
        self.wait(5)

        text1 = MathTex("\\theta\leftarrow", "0^\\circ").move_to(RIGHT * 5.3 + UP * 3)
        text2 = MathTex("\\phi\leftarrow", "0^\\circ").move_to(RIGHT * 5.3 + UP * 1.7)
        self.add_fixed_in_frame_mobjects(text1, text2)
        self.move_camera(theta = 0, phi = 0)
        self.wait(5)

        text3 = MathTex("\\theta\leftarrow", "0^\\circ").move_to(RIGHT * 5.3 + UP * 3)
        text4 = MathTex("\\phi\leftarrow", "{45}^\\circ").move_to(RIGHT * 5.3 + UP * 1.7)
        self.play(FadeOut(text1[1], text2[1]))
        self.add_fixed_in_frame_mobjects(text3[1], text4[1])
        self.move_camera(theta = 0, phi = PI/4)
        self.wait(5)

        text5 = MathTex("\\theta\leftarrow", "0^\\circ").move_to(RIGHT * 5.3 + UP * 3)
        text6 = MathTex("\\phi\leftarrow", "{90}^\\circ").move_to(RIGHT * 5.3 + UP * 1.7)
        self.play(FadeOut(text3[1], text4[1]))
        self.add_fixed_in_frame_mobjects(text5[1], text6[1])
        self.move_camera(theta = 0, phi = PI/2)
        self.wait(5)

        text7 = MathTex("\\theta\leftarrow", "{45}^\\circ").move_to(RIGHT * 5.3 + UP * 3)
        text8 = MathTex("\\phi\leftarrow", "{90}^\\circ").move_to(RIGHT * 5.3 + UP * 1.7)
        self.play(FadeOut(text5[1], text6[1]))
        self.add_fixed_in_frame_mobjects(text7[1], text8[1])
        self.move_camera(theta = PI/4, phi = PI/2)
        self.wait(5)

        text9 = MathTex("\\theta\leftarrow", "{45}^\\circ").move_to(RIGHT * 5.3 + UP * 3)
        text10 = MathTex("\\phi\leftarrow", "{60}^\\circ").move_to(RIGHT * 5.3 + UP * 1.7)
        self.play(FadeOut(text7[1], text8[1]))
        self.add_fixed_in_frame_mobjects(text9[1], text10[1])
        self.move_camera(theta = PI/4, phi = PI/3)
        self.wait(5)

        self.begin_ambient_camera_rotation(rate = 0.1)
        self.wait(8)

class Sphere(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        '''sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI/2, PI/2],
            checkerboard_colors=[RED_D, RED_D], 
            #resolution=None

        )'''
        sphere = Sphere(
            center = (0,0,0),
            radius=2,
            resolution=(20,20),
            u_range=[0.001, PI - 0.001],
            v_range=[0, TAU]
        )
        sphere.set_color(RED)
        self.add(axes, sphere)
        self.set_camera_orientation(phi = 65 * DEGREES, theta= 60 * DEGREES)
        self.begin_ambient_camera_rotation(rate = 0.1)
        self.wait(6)

class Cylinder(ThreeDScene):
    def construct(self):
        cylinder = Surface(
            lambda u, v: np.array([
                2 * np.cos(v),
                2 * np.sin(v),
                u
            ]), v_range=[-PI, PI], u_range=[-2, 2],
            checkerboard_colors=[RED_D, RED_D], 
            #resolution=None
        )
        self.add(cylinder)
        self.set_camera_orientation(phi = 65 * DEGREES, theta= 60 * DEGREES)