import game
import random
import pygame
from Weathersim.NemethCsongor.SwStage import *


class SwScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(SwStage())


"""class SwGame(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = SwScreen()


SwGame().run()"""
