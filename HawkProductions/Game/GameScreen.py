from HawkProductions.Game.GameStage import *


class GameScreen(game.scene2d.MyScreen):
    def __init__(self, puska: int, a: int):
        super().__init__()
        self.add_stage(GameStage(puska, a))
