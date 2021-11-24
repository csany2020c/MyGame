from HawkProductions.Game.GameStage1 import *
from HawkProductions.Game.GameStage import *


class GameScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage1())


class GameScreen2(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())
