from Weathersim.nemethcsongor1.start.SaStage import *


class SaScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(SaStage())
