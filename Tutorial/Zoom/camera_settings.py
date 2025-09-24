from manim import *

class FollowingGraphCamera(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        ax = Axes(x_range = [-1,2*PI], 
                    y_range = [-1.5,1.5], 
                    tips = False,
                    axis_config={"include_numbers": True, "font_size": 36})
        graph = ax.plot(lambda x: np.sin(x), x_range = [0, 2*PI], color = BLUE)

        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color = ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))

        self.add(ax, graph,moving_dot, dot_1, dot_2) 
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera.frame.remove_updater(update_curve)
        self.play(Restore(self.camera.frame))