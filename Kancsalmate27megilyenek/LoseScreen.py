import game

from Kancsalmate27megilyenek.LoseStage import *

class LoseScreen(game.scene2d.MyScreen):
    def __init__(self,mLevel:int,pLevel:int):
        super().__init__()
        self.add_stage(LoseStage(mLevel,pLevel))