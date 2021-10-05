import game
from Weathersim.KisKornel.Stage import *

class SunnyScreen(game.scene2d.MyScreen):


    def __init__(self):
        super().__init__()
        self.r = 0
        self.g = 1
        self.b = 0
        self.add_stage(SunnyStage())


class Sunny2Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 50
        self.g = 41
        self.b = 40
        self.add_stage(SunnyStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 1:
            self.game.screen = SunnyScreen()