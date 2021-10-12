import game
from Weathersim.bobicsbarnabas.stage import *

class napsutesscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(napsutesstage())
