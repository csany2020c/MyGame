import game
import random
import pygame
from Weathersim.NemethCsongor.RStage import *


class RScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(RStage())


"""class RGame(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = RScreen()


RGame().run()"""
