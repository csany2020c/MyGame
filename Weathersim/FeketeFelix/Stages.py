import game
import pygame
import random
from Weathersim.FeketeFelix.Actorok import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer

class SunnyStage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()
        self.add_actor(Sunny())
        self.add_actor(Land())
        self.Sun = Sun()
        self.add_actor(self.Sun)
