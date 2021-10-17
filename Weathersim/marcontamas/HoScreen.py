import game
from Weathersim.marcontamas.HoStage import *

class HoScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(HoStage())