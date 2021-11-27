from HawkProductions.Game.GameStage import *


class GameScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())


class GameScreen1(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())