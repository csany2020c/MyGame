import game
from Weathersim.marcontamas.HavasEsoStage import *

class HavasEsoScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(HavasEsoStage())