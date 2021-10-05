import game
from Weathersim.TothAkos.stage import *

class Sunnyscr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 0
        self.g = 0
        self.b = 0
        self.add_stage(Sunnystage())