import game
from Weathersim.FellnerMilan.SnowyRainStage import *

class SnowyRainScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(SnowyRainStage())