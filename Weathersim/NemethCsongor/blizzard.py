import game
import random
import pygame
from Weathersim.NemethCsongor.rain import *
from Weathersim.NemethCsongor.sun import *


class Bg2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/landscape.png")


class Cloudy2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/cloudy.png")


class Snow2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/snow.png")

    def act(self, delta_time: float):
        self.y += 75 * delta_time


class Rain2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/rain.png")

    def act(self, delta_time: float):
        self.y += 100 * delta_time


class Stage2(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.C = Cloudy2()
        self.add_actor(self.C)

        self.Bg = Bg2()
        self.add_actor(self.Bg)
        for i in range(23):
            self.S = Snow2()
            self.add_actor(self.S)
            self.S.set_size(width=50, height=50)
            self.S.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.S.w)
            self.S.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.S.h)

        for k in range(23):
            self.R = Rain2()
            self.add_actor(self.R)
            self.R.set_size(width=50, height=50)
            self.R.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.R.w)
            self.R.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.R.h)

        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        if event.key == pygame.KP3:
            self.screen.game.set_screen(Screen3())
        if event.key == pygame.K_KP4:
            self.screen.game.set_screen(Screen4())


class Screen2(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Stage2())


class Game2(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen2 = Screen2()
