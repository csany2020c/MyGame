import game
from bruhmomento.bruhActor import *


class bruhstage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()
        self.add_actor(bruhActor())
        self.add_actor(enemy2())
        self.add_actor(horthy())
        self.add_actor(enemy1())