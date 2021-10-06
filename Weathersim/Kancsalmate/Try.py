import game
import pygame

class ActorA(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("landscape.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class ActorB(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("sunny.png")

    def act(self, delta_time: float):
        super().act(delta_time)

class ActorC(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("cloudy.png")

    def act(self, delta_time: float):
        super().act(delta_time)

class ActorD(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")


class Stage(game.scene2d.MyStage):

    def Keys(self, sender, event):
        if event.key == pygame.K_a:
            self.isAPressed = True
        if event.key == pygame.K_s:
            self.isSPressed = True
        if event.key == pygame.K_m:
            self.isMPressed = True


    def __init__(self):
        super().__init__()
        self.isWPressed: bool = False
        self.isAPressed: bool = False
        self.isSPressed: bool = False
        self.isDPressed: bool = False
        self.isMPressed: bool = False
        self.set_on_key_down_listener(self.Keys)
        self.a = ActorA()
        self.b = ActorB()
        self.c = ActorC()
        self.d = ActorD()
        self.x = 1
        self.c.set_z_index(self.x)
        self.b.set_z_index(self.x)
        self.d.set_z_index(self.x + 1)
        self.c.set_x(0).set_y(0)
        self.a.set_x(0).set_y(0)
        self.add_actor(self.a)
        self.b.set_x(0).set_y(0)

        for j in range(2, 5):
            print(j)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.isAPressed:
            self.add_actor(self.b)
            self.x = self.x - 1
        if self.isSPressed:
            self.add_actor(self.c)
            self.x = self.x - 1
        if self.isMPressed:
            self.add_actor(self.d)
            self.d.set_x(600)
            self.x = self.x - 1

class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Stage())


class Start(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = Screen()

Start().run()