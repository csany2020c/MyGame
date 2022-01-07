import game
from Kancsalmate27megilyenek.ArenaStage import *

class ArenaScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(ArenaStage())