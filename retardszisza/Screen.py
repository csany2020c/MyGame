import game
from retardszisza.Stage import *


class GameScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(150, 70, 35)
        self.add_stage(GameStage())

