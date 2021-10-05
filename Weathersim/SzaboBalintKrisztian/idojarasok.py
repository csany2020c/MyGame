import game
import pygame
import random
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer


class NapocskaActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("sun.png")
        self.x += 650
        self.y += 125
        self.set_width(800)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(0.2)

class HatterActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("sunny.png")

class Hatter2Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("cloudy.png")

class LandscapeActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("landscape.png")

class HavzikActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("snow.png")
        self.y -= 50

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(3)
        self.y += delta_time * 100
        self.x += delta_time * 100

class Havzik2Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("snow.png")
        self.x += 300
        self.y -= 50

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(3)
        self.y += delta_time * 100
        self.x += delta_time * 100

class Havzik3Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("snow.png")
        self.x -= 300
        self.y -= 50

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(3)
        self.y += delta_time * 100
        self.x += delta_time * 100

class Havzik4Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("snow.png")
        self.x += 600
        self.y -= 50

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(3)
        self.y += delta_time * 100
        self.x += delta_time * 100

class Havzik5Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("snow.png")
        self.x += 900
        self.y -= 50

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(3)
        self.y += delta_time * 100
        self.x += delta_time * 100

class CseppActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("rain.png")

class NaposStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(HatterActor())
        self.add_actor(NapocskaActor())
        self.add_actor(LandscapeActor())


class HavasStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(Hatter2Actor())
        self.add_actor(LandscapeActor())
        self.add_actor(HavzikActor())
        self.add_actor(Havzik3Actor())
        self.add_actor(Havzik4Actor())
        self.add_actor(Havzik5Actor())
        self.add_actor(Havzik2Actor())
        self.ho = HavzikActor()
        self.t = MyTickTimer(interval=1.5, func=self.tikk)
        self.add_timer(self.t)

    def tikk(self, sender):
        self.add_actor(HavzikActor())
        self.add_actor(Havzik2Actor())
        self.add_actor(Havzik3Actor())
        self.add_actor(Havzik4Actor())
        self.add_actor(Havzik5Actor())

class EsosStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(Hatter2Actor())
        self.add_actor(LandscapeActor())
        self.add_actor(CseppActor())


class Esikaeso(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(EsosStage())

class Sutanap(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(NaposStage())


class Esikaho(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavasStage())


class IdoSim(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = Sutanap()
        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        print(sender)
        if event.key == pygame.K_2:
            print("22222222222222222222222222222")
            self.screen = Esikaho()

        if event.key == pygame.K_3:
            print("333333333333333333333333333333")
            self.screen = Esikaeso()

        if event.key == pygame.K_1:
            print("11111111111111111111111111111")
            self.screen = Sutanap()


IdoSim().run()