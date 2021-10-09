from Weathersim.nemethcsongor1.Sun.SuStage import *


class SuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(SuStage())
