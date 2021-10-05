import game
from Weathersim.KisKornel.Actor import *
from game.scene2d import MyTickTimer
import random

class SunnyStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.add_actor(skyActor())
        self.add_actor(backgroundActor())
        self.SunnyActor = SunnyActor()
        self.add_actor(self.SunnyActor)
        #self.backgroundactor = backgroundActor
        #self.add_actor(self.backgroundactor)
        #self.skyactor = skyActor
        #self.add_actor(self.skyactor)