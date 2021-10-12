import game
from Weathersim.RigoDonat.actor import *
import random
import pygame

class SunnyStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.SunnySky = SunnySky()
        self.add_actor(SunnySky())
        self.Sun = Sun()
        self.add_actor(self.Sun)
        self.Forest = Forest()
        self.add_actor(Forest())

class RainStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.CloudySky = CloudySky()
        self.add_actor(CloudySky())
        self.add_actor(Forest())
        for a in range(700):
            self.RainDrop = RainDrop()
            self.add_actor(self.RainDrop)
            self.RainDrop.width = 30
            self.RainDrop.height = 30
            self.RainDrop.x = random.Random().randint(-1500, 1500)
            self.RainDrop.y = random.Random().randint(-1000, 1000)
