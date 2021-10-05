import game
import random
import pygame
from Weathersim.NemethCsongor.blizzard import *
from Weathersim.NemethCsongor.rain import *


class Bg4(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/landscape.png")


class Cloudy4(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/cloudy.png")


class Snow4(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/snow.png")

    def act(self, delta_time: float):
        self.y += 75 * delta_time


class Stage4(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.C = Cloudy4()
        self.add_actor(self.C)

        self.Bg = Bg4()
        self.add_actor(self.Bg)
        for i in range(23):
            self.S = Snow4()
            self.add_actor(self.S)
            self.S.set_size(width=50, height=50)
            self.S.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.S.w)
            self.S.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.S.h)

        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        if event.key == pygame.K_KP2:
            self.screen.game.set_screen(Screen2())
        if event.key == pygame.K_KP3:
            self.screen.game.set_screen(Screen3())


class Screen4(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Stage4())


class Game4(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = Screen4()
