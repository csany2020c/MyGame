from HawkProductions.Game.GameStage import *


class GameScreen(game.scene2d.MyScreen):
    def __init__(self, puska: int):
        super().__init__()
        self.add_stage(GameStage(puska))
