import game
import pygame
import random


class ActorA(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("cloudy.png")


class ActorB(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("landscape.png")


class ActorC(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("rain.png")
        self.set_width(30)
        self.set_height(30)

    def act(self, delta_time: float):
        game.scene2d.MyLabel.act(self, delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.y += delta_time * 160


class ActorD(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("villam.png")


class ActorE(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("villamketo.png")
        self.set_width(200)


class ActorF(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("felho2.png")
        self.set_width(800)


class Stage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.a = ActorA()
        self.b = ActorB()
        self.c = ActorC()
        self.d = ActorD()
        self.d.set_x(700).set_y(100)
        self.e = ActorE()
        self.e.set_x(900).set_y(100)
        self.f = ActorF()
        self.f.set_x(525).set_y(-150)
        self.add_actor(self.a)
        self.add_actor(self.b)
        self.add_actor(self.c)
        self.add_actor(self.d)
        self.add_actor(self.e)
        self.add_actor(self.f)
        self.set_on_key_down_listener(self.key_down)

        for i in range(1500):
            self.rain = ActorC()
            self.add_actor(self.rain)
            self.rain.x = random.Random().randint(0, 1230)
            self.rain.y = random.Random().randint(-3000, 750)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()


class EsosScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(Stage())


class Start(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = EsosScreen()


Start().run()
