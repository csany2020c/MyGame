import game
from kuposztok.Credit.CreditStage import *


class CreditScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(r=0,g=0, b=255)
        self.add_stage(CreditStage())