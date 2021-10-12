import game
from Weathersim.bobicsbarnabas.menu.menustage import *

class menuscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 50
        self.g = 80
        self.b = 90
        self.add_stage(menustage())