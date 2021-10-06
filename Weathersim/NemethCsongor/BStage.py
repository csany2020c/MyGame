import game
import random
import pygame
from Weathersim.NemethCsongor.Actorok import *


class BStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.C = Cloudy()
        self.add_actor(self.C)

        self.Bg = Bg()
        self.add_actor(self.Bg)

        for i in range(23):
            self.R = Rain()
            self.add_actor(self.R)
            self.R.set_size(width=30, height=30)
            self.R.x = random.randint(a=0, b=1280)
            self.R.y = random.randint(a=-0, b=720)

        for i in range(30):
            self.S = Snow()
            self.add_actor(self.S)
            self.S.set_size(width=30, height=30)
            self.S.x = random.randint(a=0, b=1280)
            self.S.y = random.randint(a=-0, b=720)

