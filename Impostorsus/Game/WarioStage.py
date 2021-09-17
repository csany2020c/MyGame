import game
from Susactor import *
from WarioActor import *

class WarioStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.Sus = SusActor()
        self.Warrio = WarioActor()
        self.add_actor(self.Sus)
        self.add_actor(self.Warrio)