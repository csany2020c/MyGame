import game
from bruhmomento.menustage import *

class menuscreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 0
        self.g = 100
        self.b = 0
        self.add_stage(menustage())