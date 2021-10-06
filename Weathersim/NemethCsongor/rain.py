import game
import random
import pygame
from Weathersim.NemethCsongor.blizzard import *
from Weathersim.NemethCsongor.snow import *


class Bg3(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/landscape.png")


class Cloudy3(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/cloudy.png")


class Rain3(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/rain.png")

    def act(self, delta_time: float):
        self.y += 75 * delta_time


class Stage3(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.C = Cloudy3()
        self.add_actor(self.C)

        self.Bg = Bg3()
        self.add_actor(self.Bg)
        for i in range(23):
            self.R = Rain3()
            self.add_actor(self.R)
            self.R.set_size(width=50, height=50)
            self.R.x = random.randint(0, 1280)
            self.R.y = random.randint(0, 720)

        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        if event.key == pygame.K_KP2:
            self.screen.game.set_screen(Screen2())
        if event.key == pygame.K_KP4:
            self.screen.game.set_screen(Screen4())


class Screen3(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Stage3())


class Game3(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = Screen3()


Game3().run()
