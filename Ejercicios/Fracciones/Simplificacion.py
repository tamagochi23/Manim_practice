from manim import *

class Ejercicio1(Scene):
    def construct(self):

        def add_partitions(circle, num_parts):
            arc_list = []
            sector_list = []
            angle = TAU / num_parts
            start_angle = 0
            for i in range(num_parts):
                arc = Arc(start_angle=start_angle, angle=angle, arc_center=circle.get_center(), radius=circle.radius, color=BLUE)
                sector = Sector(radius = circle.radius, start_angle=start_angle, angle=angle, color=BLUE, arc_center=circle.get_center())                
                sector.set_z_index(-1)
                start_angle += angle
                arc_list.append(arc)
                sector_list.append(sector)
            for i in range(num_parts):
                arc_part = arc_list[i]
                line_ini = Line(circle.get_center(), arc_part.point_from_proportion(0), color=ORANGE)  
                self.play(Create(line_ini))  # show the line on screen
                self.wait(0.1)  
            return arc_list, sector_list

        #DEFINE OBJECTS
        title = Text("Ejercicio 1: Simplificación de Fracciones").to_edge(UP)

        circle = Circle(radius=3)  # create a circle
        circle.set_fill(ORANGE, opacity=0.5)  # set the color and transparency
        circle.set_z_index(-1)
        #

        #ORDER

        VGroup(title, circle).arrange(DOWN, buff=0.5)  # arrange the title and circle vertically
        
        arc1 = Arc(start_angle=0, angle=TAU/8, arc_center=circle.get_center(), radius=circle.radius, color=BLUE)  # create an arc representing 1/4 of the circle
        #line = Line(circle.get_center(), arc.point_from_proportion(1), color=ORANGE)  # create a line from the center to the edge of the arc
        arc2 = Arc(start_angle=TAU/8, angle=TAU/8, arc_center=circle.get_center(), radius=circle.radius, color=BLUE)

        self.add(title, circle)  # add the title, circle, dot, arc, and line to the scene
        self.play(Create(circle))  # show the circle on screen
        arc_list, sector_list = add_partitions(circle, 6)
        #sector1 = Sector(radius = circle.radius, start_angle=TAU/8, angle=TAU/8, color=BLUE, arc_center=circle.get_center())
        self.play(Create(sector_list[0]), Create(sector_list[1]), Create(sector_list[2]), Create(sector_list[3]))  # show the arc on screen
        self.wait(2)  # wait for 2 seconds

