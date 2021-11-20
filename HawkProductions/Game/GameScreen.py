from HawkProductions.Game.GameStage1 import *


class GameScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(GameStage1())
