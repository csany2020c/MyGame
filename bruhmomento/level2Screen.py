import game
from bruhmomento.level2Stage import *

class Level2Screen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(level2())