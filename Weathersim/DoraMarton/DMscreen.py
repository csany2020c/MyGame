import game
from Weathersim.DoraMarton.DMstage import *


class sunnyscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(sunnystage())

class snowyscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(snowystage())