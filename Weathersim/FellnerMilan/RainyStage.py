import  game
from Weathersim.FellnerMilan.InActors import *
class RainStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.l = LandScape()
        self.add_actor(self.l)