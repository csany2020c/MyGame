import game
from Impostorsus.Game.WarioActor import *
from Impostorsus.Game.WarioStage import *


class WarioScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 245
        self.g = 71
        self.b = 146
        self.add_stage(WarioStage())