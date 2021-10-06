from Weathersim.olahgergo.mainstage import *
from Weathersim.olahgergo.eso import *
from Weathersim.olahgergo.havazas import *


class MainScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(MainStage())
        self.add_stage(HoStage())




