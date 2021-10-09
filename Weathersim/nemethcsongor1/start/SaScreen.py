from Weathersim.nemethcsongor1.start.SaStage import *


class SaScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(80, 58, 48)
        self.add_stage(SaStage())
