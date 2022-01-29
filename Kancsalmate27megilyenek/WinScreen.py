import game

from Kancsalmate27megilyenek.WinStage import *

class WinScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(WinStage())