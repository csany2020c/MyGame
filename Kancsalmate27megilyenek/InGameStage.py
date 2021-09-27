import game

from Kancsalmate27megilyenek.MapActor import *

class InStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.map = Map()
        self.add_actor(self.map)
