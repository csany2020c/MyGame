import game
from retardszisza.Stage import *


class GameScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(1, 22, 3)
        self.add_stage(GameStage())

