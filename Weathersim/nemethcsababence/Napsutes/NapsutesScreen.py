from Weathersim.nemethcsababence.Napsutes.NapsutesStage import *

class NapsutesScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(NapsutesStage())