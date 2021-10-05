import game
from Weathersim.DoraMarton.DMactors import *

class sunnystage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()
        self.add_actor(sunny())
        self.add_actor(landscape())
        self.add_actor(sun())

class snowystage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()
        self.add_actor(cloudy())
        self.add_actor(landscape())
        self.add_actor(snow())