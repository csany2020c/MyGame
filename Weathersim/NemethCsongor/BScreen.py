import game
import random
import pygame
from Weathersim.NemethCsongor.BStage import *


class BScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(BStage())


class BGame(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = BScreen()


BGame().run()
