import game

from Kancsalmate27megilyenek.InfoStage import *

class InfoScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(InfoStage())