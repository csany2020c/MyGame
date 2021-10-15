import game
import pygame


class ActorA(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sunny.png")


class ActorB(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += -delta_time*10


class ActorC(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("landscape.png")


class ActorD(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("alma.png")
        self.set_width(30)
        self.set_height(30)


class Stage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.a = ActorA()
        self.b = ActorB()
        self.c = ActorC()
        self.d = ActorD()
        self.b.set_x(400).set_y(50)
        self.d.set_x(110).set_y(650)
        self.add_actor(self.a)
        self.add_actor(self.b)
        self.add_actor(self.c)
        self.add_actor(self.d)
        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()


class NapsutesesScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(Stage())
