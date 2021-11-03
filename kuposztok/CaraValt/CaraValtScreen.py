import game
from kuposztok.CaraValt.CaraValtStage import *


class CaraValtScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(r=0,g=0, b=0)
        self.add_stage(CaraValtStage())


