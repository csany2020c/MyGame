from Weathersim.FellnerMilan.SnowyStage import *
import game


class SnowScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(SnowStage())
