import game
from bruhmomento.bruhActor import *


class bruhstage(game.scene2d.MyStage):

    def create(self):
        super().create()
        self.add_actor(bruhActor())
        self.add_actor(enemy1())