import game
from bruhmomento.bruhStage import *

class bruhScreen(game.scene2d.MyScreen):


    def __init__(self):
        super().__init__()
        self.add_stage(bruhstage())
    #def act(self, delta_time: float):
    #        super().act(delta_time)
    #        if self.elapsed_time > 1:
    #            self.game.screen =brruhScreen()

class brruhScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(bruhstage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 1:
            self.game.screen = bruhScreen()

class level2Screen(game.scene2d.MyScreen):
    def __init__(self):
        super.__init__()
        self.add_stage(level2())
