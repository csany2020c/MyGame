import  game
from Weathersim.FellnerMilan.InActors import *
from game.scene2d import MyTickTimer
from random import Random
class RainStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.l = LandScape()
        self.add_actor(self.l)
        self.l.z_index = 1


        self.cloud = Rainy()
        self.add_actor(self.cloud)
        self.cloud.z_index = 0

        self.rain = Rain()
        self.add_actor(self.rain)
        self.rain.z_index = 2

        self.r = Random()

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.rain.y == self.rain.y + 5:
            pass

    def timerhandler(self,sender):
        self.rain2 = Rain()
        self.add_actor(self.rain2)
        self.rain2.x = self.r.randint(0,1280)
        self.rain2.y = self.rain2.y

