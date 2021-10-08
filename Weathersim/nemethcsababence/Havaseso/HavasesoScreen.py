import game
from Weathersim.nemethcsababence.Havaseso.HavasesoStage import *

class HavasesoScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(HavasesoStage())