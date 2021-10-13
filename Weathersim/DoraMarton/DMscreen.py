import pygame
import game
from Weathersim.DoraMarton.DMstage import *


class Sunnyscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(sunnystage())

    def act(self, delta_time: float):
        super().act(delta_time)

class Snowyscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(snowystage())

    def act(self, delta_time: float):
        super().act(delta_time)

class Rainyscreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(rainystage())

    def act(self, delta_time: float):
        super().act(delta_time)

class snowyrainyscreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(snowyrainy())

    def act(self, delta_time: float):
        super().act(delta_time)

class Menuscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(menustage())