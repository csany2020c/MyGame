import game
from bruhmomento.bruhStage import *

class bruhScreen(game.scene2d.MyScreen):


    def __init__(self):
        super().__init__()
        self.r = 0
        self.g = 1
        self.b = 0
        self.add_stage(bruhstage())
    #def act(self, delta_time: float):
    #        super().act(delta_time)
    #        if self.elapsed_time > 1:
    #            self.game.screen =brruhScreen()

class brruhScreen(game.scene2d.MyScreen):

    def __init__(self, width: int = 1280, height: int = 720):
        super().__init__(width, height)
        self.r = 50
        self.g = 41
        self.b = 40
        self.add_stage(bruhstage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 1:
            self.game.screen = bruhScreen()

class level2Screen(game.scene2d.MyScreen):
    def __init__(self, width: int = 1280, height: int = 720):
        super.__init__(width, height)
        self.add_stage(level2())
