import game
import pygame
import random
from WarioActor import *


class WarioActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("Kepek/Enemysus.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100

class Wario2Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("Kepek/kerdosus.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 100

class Wario3Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("Kepek/foldriosus.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 100
        self.x += delta_time * 100

class Wario4Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("Kepek/actorsusus.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class WarioStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(WarioActor())
        self.add_actor(Wario2Actor())
        self.add_actor(Wario3Actor())
        self.lastkeydown = 0
        self.wario = Wario4Actor()
        self.add_actor(self.wario)
        self.wario.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        self.lastkeydown = event.key
        if event.key == pygame.K_f:
            print("FFFFFFFFFFFFFFFFFFFFFFFFFFF")
            # self.wario.x += 100

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.lastkeydown == pygame.K_d:
            self.wario.x += 100 * delta_time




class Wario2Scr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 71
        self.g = 245
        self.b = 233
        self.add_stage(WarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 5:
            self.game.screen = WarioScr()

class WarioScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 245
        self.g = 71
        self.b = 146
        self.add_stage(WarioStage())

    #def act(self, delta_time: float):
        #super().act(delta_time)
        #if self.elapsed_time > 5:
            #self.game.screen = Wario2Scr()

class Wario(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = WarioScr()


Wario().run()