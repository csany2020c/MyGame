import game
from WarioStage import *

class WarioScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(245, 71, 146)
        self.add_stage(WarioStage())