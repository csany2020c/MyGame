import game
import random
import pygame
from Weathersim.NemethCsongor.blizzard import *
from Weathersim.NemethCsongor.rain import *
from Weathersim.NemethCsongor.snow import *


class Bg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/landscape.png")


class Sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/sunny.png")


class Sun (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/sun.png")


class Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.S = Sunny()
        self.add_actor(self.S)

        self.Bg = Bg()
        self.add_actor(self.Bg)

        self.Su = Sun()
        self.add_actor(self.Su)
        self.Su.x = 850
        self.Su.y = 5

        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        if event.key == pygame.K_KP2:
            self.screen.game.set_screen(Screen2())
        if event.key == pygame.K_KP3:
            self.screen.game.set_screen(Screen3())
        if event.key == pygame.K_KP4:
            self.screen.game.set_screen(Screen4())


class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Stage())


class Game(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = Screen()
