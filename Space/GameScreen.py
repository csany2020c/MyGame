import game
from GameStage import *


class GameScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(200, 100, 22)


        self.add_stage(GameStage())
