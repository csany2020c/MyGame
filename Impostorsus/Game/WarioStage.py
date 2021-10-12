import game
from Impostorsus.Game.WarioActor import *

class WarioStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.Warrio = WarioActor()
        self.add_actor(self.Warrio)