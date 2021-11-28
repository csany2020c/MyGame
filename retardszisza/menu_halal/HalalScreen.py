import game
from retardszisza.menu_halal.HalalStage import *

class halalscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 10
        self.g = 30
        self.b = 80
        self.add_stage(halalstage())