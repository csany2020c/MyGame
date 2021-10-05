from Weathersim.nemethcsababence.Eso.EsoStage import *

class EsoScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(EsoStage())