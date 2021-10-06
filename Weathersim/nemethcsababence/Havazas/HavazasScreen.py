import game
from Weathersim.nemethcsababence.Havazas.HavazasStage import *


class HavazasScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavazasStage())