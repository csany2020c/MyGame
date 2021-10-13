import game
from Weathersim.marcontamas.NaposStage import *

class NaposScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(NaposStage())