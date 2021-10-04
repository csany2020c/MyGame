from Weathersim.FellnerMilan.RainyStage import *
import game


class RainScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(RainStage())
