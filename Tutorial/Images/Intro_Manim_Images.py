from manim import *

                                       
class Imagess(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        img = ImageMobject("./media/images/Intro_Manim_Images/pista.png").rotate(PI/2).scale(1.5)
        self.add(img)
        titulo = Text("Movimiento rectilineo", color = BLACK).move_to(UP * 3.5)
        self.play(Write(titulo))
        self.wait(2)
        lugar0 = ImageMobject("./media/images/Intro_Manim_Images/car.png").move_to(DOWN * 1.5 + LEFT * 4).scale(0.1)
        self.add(lugar0)
        self.wait(2)
        lugar1 = lugar0.copy().move_to(DOWN * 1.5 + RIGHT * 4)
        self.play(Transform(lugar0, lugar1), run_time = 5)
        self.wait(2)

class zoom(MovingCameraScene):
    def construct(self):
        img = ImageMobject("./media/images/Intro_Manim_Images/car.png").rotate(PI/2).scale(0.1)
        self.add(img)
        self.wait(2)
        self.camera.frame.save_state()
        rejilla = NumberPlane().set_color(RED)
        self.add(rejilla)
        self.wait(2)
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(np.array([-3.5, 2, 0]))
        )
        self.wait(2)
        self.play(Restore(self.camera.frame))