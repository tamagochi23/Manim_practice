from manim import *

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

class Sphere_Shape(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=PI / 6, theta=PI / 6)
        
        sphere1 = Sphere(
            center=(3, 0, 0),
            radius=1,
            resolution=(20, 20),
            u_range=[0.001, PI - 0.001],
            v_range=[0, TAU]
        )
        sphere1.set_color(RED)
        self.add(sphere1)
        sphere2 = Sphere(center=(-1, -3, 0), radius=2, resolution=(18, 18))
        sphere2.set_color(GREEN)
        self.add(sphere2)
        sphere3 = Sphere(center=(-1, 2, 0), radius=2, resolution=(16, 16))
        sphere3.set_color(BLUE)
        self.add(sphere3)

class Cylinder_Shape(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=PI / 3, theta=PI / 6, zoom=0.5)
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
        self.wait(2)
        cylinder2 = Cylinder(radius=2, height=3).move_to([3,3,0])
        self.play(ReplacementTransform(cylinder, cylinder2))
        self.wait(2)
        #self.play(ReplacementTransform(cylinder, cylinder2))