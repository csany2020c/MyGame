import pygame
from Weathersim.ZsuppanFlorian.mainactors import *


class MainStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.bg = taj()
        self.bg.height = 720
        self.bg.width = 1280
        self.add_actor(self.bg)
