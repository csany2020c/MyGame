from kuposztok.Lose.LoseStage import *
import game
from kuposztok.Lose.LoseStage import LoseStage


class LoseScreen(game.scene2d.MyScreen):

    def __init__(self, score: int, maxScore: int):
        super().__init__()
        self.set_background_color(r=0,g=0, b=0)
        self.add_stage(LoseStage(score=score, maxScore=maxScore))