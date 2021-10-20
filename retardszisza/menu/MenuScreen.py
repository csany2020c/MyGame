import game
from retardszisza.menu.MenuStage import *

class menuscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 80
        self.g = 10
        self.b = 120
        self.add_stage(menustage())