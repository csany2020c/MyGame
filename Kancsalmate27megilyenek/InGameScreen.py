import game

from Kancsalmate27megilyenek.InGameStage import *

class InScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(InStage())