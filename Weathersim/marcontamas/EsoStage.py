import game
from Weathersim.marcontamas.EsoActorok import *

class EsoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        #landscape
        self.a = Alap()
        self.add_actor(self.a)
        self.a.z_index = 0
        #felhos
        self.c = Felhos()
        self.add_actor(self.c)
        self.c.z_index = -1
        #eso
        for i in range(30):
            self.rain = Eso()
            self.add_actor(self.rain)

        self.rain.z_index = 1