from manim import *
class Sphere_Test(ThreeDScene):
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

def Spherical_to_Cartesian_coords(p,phi, theta):
    print(p, phi,theta)
    x = p*np.sin(phi)*np.cos(theta)
    y = p*np.sin(phi)*np.sin(theta)
    z = p*np.cos(phi)
    return [x,y,z]

class Cylinder_Test(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        radius = 1
        height = 2
        #mob= Brace([0,1,1],text= r'2 \, \text{cm}', color= YELLOW, buff=0.1) 
        #mob.submobjects[1].set_color(YELLOW) 
        #self.add_fixed_in_frame_mobjects(mob.move_to(RIGHT*1,UP*3)) 
        param_cylinder = Surface(
            lambda u, v: np.array([
                radius * np.cos(v), #
                radius * np.sin(v),
                u
            ]), v_range=[-PI, PI], u_range=[0, height],
            #checkerboard_colors=[RED_D, RED_D], 
            #resolution=None
        )
        param_cylinder.set_color(RED_D)
        c_down = Circle(radius=radius).set_fill(color=RED_D, opacity=0.5)
        c_top = Circle(radius=radius).set_fill(color=RED_D, opacity=0.5).move_to([0,0,height])    
        cylinder_with_circle =  VGroup(c_down,c_top,param_cylinder)
        cylinder_with_circle.move_to([-3,2,0])
        #brace_r = BraceLabel(c_down, text=r'2r', buff=0.1)
        #brace_r.move_to([-4.5,-1.8,0])
        #brace_h = BraceLabel(c_down, brace_direction=RIGHT, text=r'h', buff=0.1)
        #brace_h.move_to([-2.8,0,0])
        
        #l=Line(ORIGIN, RIGHT*1.4) 
        #mob= BraceLabel(l, text= r'14 \, \text{cm}', color= YELLOW, buff=0.1) 
        #mob.submobjects[1].set_color(YELLOW) 
        #self.add(VGroup(l,mob).move_to(ORIGIN)) 
        #self.add_fixed_in_frame_mobjects(brace_r, brace_h)
        a = param_cylinder.get_center()
        point = Point([a[0] + radius,a[1]+(height/2), a[2]], color=YELLOW)
        line = Line([a[0] + radius,a[1]+(height/2), 0],[a[0] + radius,a[1]+(height),0], color = WHITE)
        mob = BraceLabel(line, text= r'14 \, \text{cm}', color= YELLOW, buff=0.5, brace_direction=RIGHT)
        mob.submobjects[1].set_color(YELLOW)
        self.add_fixed_in_frame_mobjects(point, mob, line)
        self.add(cylinder_with_circle)
        #self.add(cylinder_with_circle) #orden de derecha a izquierda
        self.set_camera_orientation(phi = 65 * DEGREES, theta= 65 * DEGREES, focal_distance=100)

class V_Cylinder(ThreeDScene):
    def construct(self):

        # CANVAS

        title = Text("Volúmen de un cilindro").move_to(UP*3)
        marco = Rectangle(height= 5, width= 6).move_to([-3,-0.5,0])
        self.add_fixed_in_frame_mobjects(marco, title)
        # CREATE 3D FIGURE

        self.set_camera_orientation(phi = 78 * DEGREES, theta= 65 * DEGREES, focal_distance=100)
        radius = 1.5
        height = 1.5
        cylinder = Cylinder(radius = radius, height = height).move_to([4,1.5,0])
        #self.add(axes)
        self.play(Write(cylinder), run_time= 2)

        #PARAMETERS

        r = Line(start=[-3,0.15,0], end=[-1.55,0.15,0], color = YELLOW)
        Brace_r = BraceLabel(r, text= r'r', color = YELLOW, buff= 0.2, brace_direction= UP)
        h = Line(start=[-1.55,-1.5,0], end=[-1.55,0.15,0], color = YELLOW)
        Brace_h = BraceLabel(h, text= r'h', color = YELLOW, buff= 0.2, brace_direction= RIGHT)

        self.add_fixed_in_frame_mobjects(r, Brace_r, Brace_h)
        self.play(FadeIn(Brace_r), FadeIn(Brace_h))

        # EQUATION

        VC_equa = MathTex("V=\\pi","r","^2" ,"h").move_to(UP*1.5 + RIGHT * 2)
        self.add_fixed_in_frame_mobjects(VC_equa[0],VC_equa[2])
        self.play(Write(VC_equa[0]), Write(VC_equa[2]))

        #self.add_fixed_in_frame_mobjects(VC_equa[1],VC_equa[2])
        self.play(Transform(Brace_r.submobjects[1], VC_equa[1]),run_time= 2)
        self.play(Transform(Brace_h.submobjects[1], VC_equa[3]), run_time = 2)
        self.wait(2)
        #self.play(Write(cylinder), run_time = 0.5)

class V_Sphere(ThreeDScene):
    def construct(self):

        # CANVAS

        title = Text("Volúmen de una esfera").move_to(UP*3)
        marco = Rectangle(height= 5, width= 6).move_to([-3,-0.5,0])
        self.add_fixed_in_frame_mobjects(marco, title)
        # CREATE 3D FIGURE

        self.set_camera_orientation(phi = 78 * DEGREES, theta= 65 * DEGREES, focal_distance=100)
        radius = 1.5
        sphere = Sphere(radius = radius).move_to([4,1.5,0])

        self.play(Write(sphere), run_time= 2)
        self.wait(2)

        #PARAMETERS

        r = Line(start=[-3,-0.7,0], end=[-1.55,-0.7,0], color = YELLOW)
        Brace_r = BraceLabel(r, text= r'r', color = YELLOW, buff= 0.2, brace_direction= UP)
        self.add_fixed_in_frame_mobjects(r, Brace_r)
        self.play(FadeIn(Brace_r))

        # EQUATION

        VC_equa = MathTex("V=\\frac{4}{3}\\pi","r", "^3").move_to(UP*1.5 + RIGHT * 2)
        self.add_fixed_in_frame_mobjects(VC_equa[0], VC_equa[2])
        self.play(Write(VC_equa[0]))

        self.play(Transform(Brace_r.submobjects[1], VC_equa[1]),run_time= 2)
        #self.play(Transform(Brace_h.submobjects[1], VC_equa[3]), run_time = 2)
        self.wait(2)

class V_Prism(ThreeDScene):
    def construct(self):

        # CANVAS

        title = Text("Volúmen de un prisma").move_to(UP*3)
        marco = Rectangle(height= 5, width= 6).move_to([-3,-0.5,0])
        self.add_fixed_in_frame_mobjects(marco, title)
        # CREATE 3D FIGURE

        self.set_camera_orientation(phi = 78 * DEGREES, theta= 60 * DEGREES, focal_distance=100)
        a = 2
        b = 2
        c = 2
        prism = Prism([a, b, c]).move_to([4.2,1.5,0.5])

        self.add(prism)
        #self.play(Write(prim), run_time= 2)
        #self.wait(2)

        
        #PARAMETERS
        dot1 = Dot([-4.4,-1.25,0])
        dot2 = Dot([-3.4,-1.65,0])
        a = Line(start=dot1.get_center(), end= dot2.get_center(), color = YELLOW)
        Brace_a = Brace(a, direction = a.copy().rotate(3*PI/2).get_unit_vector())
        Brace_a_text = Brace_a.get_tex("a")
        self.add_fixed_in_frame_mobjects(Brace_a, Brace_a_text)

        dot3 = Dot([-3.4,-1.65,0])
        dot4 = Dot([-1.55,-1.4,0])
        b = Line(start=dot3.get_center(), end= dot4.get_center(), color = YELLOW)
        Brace_b = Brace(b, direction = b.copy().rotate(3*PI/2).get_unit_vector())
        Brace_b_text = Brace_b.get_tex("b")
        self.add_fixed_in_frame_mobjects(Brace_b, Brace_b_text)
        #self.play(FadeIn(a))
        
        dot5 = Dot([-1.55,-1.4,0])
        dot6 = Dot([-1.55,0.7,0])
        c = Line(start=dot5.get_center(), end= dot6.get_center(), color = YELLOW)
        Brace_c = Brace(c, direction = c.copy().rotate(3*PI/2).get_unit_vector())
        Brace_c_text = Brace_c.get_tex("c")
        self.add_fixed_in_frame_mobjects(Brace_c, Brace_c_text)

        # EQUATION

        VC_equa = MathTex("V=","a","b", "c").move_to(UP*1.5 + RIGHT * 2)
        self.add_fixed_in_frame_mobjects(VC_equa[0])
        #elf.add_fixed_in_frame_mobjects(VC_equa[0], VC_equa[2])
        self.play(Write(VC_equa[0]))

        self.play(Transform(Brace_a_text, VC_equa[1]),run_time= 2)
        self.play(Transform(Brace_b_text, VC_equa[2]),run_time= 2)
        self.play(Transform(Brace_c_text, VC_equa[3]),run_time= 2)
        #self.play(Transform(Brace_h.submobjects[1], VC_equa[3]), run_time = 2)
        #self.wait(2)
        
class V_Cylinder_variable(ThreeDScene):
    def construct(self):

        # CANVAS

        title = Text("Volúmen de un cilindro").move_to(UP*3)
        marco = Rectangle(height= 5, width= 6).move_to([-3,-0.5,0])
        self.add_fixed_in_frame_mobjects(marco, title)
        # CREATE 3D FIGURE

        self.set_camera_orientation(phi = 78 * DEGREES, theta= 65 * DEGREES, focal_distance=100)
        radius = 1.5
        height = 1.5
        cylinder1 = Cylinder(radius = radius, height = height).move_to([4,1.5,0])
        #self.add(axes)
        self.add(cylinder1)

        equa0 = MathTex("r=", "1.5").move_to(RIGHT,UP)
        self.add_fixed_in_frame_mobjects(equa0)
        for i in np.linspace(1.5,2,8):
            radius = i
            cylinder2 = Cylinder(radius = radius, height = height).move_to([4,1.5,0])
            self.play(Transform(cylinder1, cylinder2))
            self.play(FadeOut(equa0))
            equa0 = MathTex("r=", str(radius)).move_to(RIGHT,UP)
            self.add_fixed_in_frame_mobjects(equa0)



class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.add(line1, line_moving, a, tex)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(tex.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))