import game
from Weathersim.vizdakmate.Stage import *

class SunnyScreen(game.scene2d.MyScreen):


    def __init__(self):
        super().__init__()
        self.r = 10
        self.g = 45
        self.b = 39
        self.add_stage(SunnyStage())







