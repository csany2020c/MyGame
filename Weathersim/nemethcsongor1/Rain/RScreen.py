from Weathersim.nemethcsongor1.Rain.RStage import *


class RScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(RaStage())
