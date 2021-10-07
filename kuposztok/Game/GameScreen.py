import game
from kuposztok.Game.Gamestage import *


class GameScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(r=0,g=0, b=255)
        self.add_stage(GameStage())

