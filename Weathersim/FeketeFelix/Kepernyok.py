import game
from Weathersim.FeketeFelix.Stages import *

class SunnyScreen(game.scene2d.MyScreen):


    def __init__(self):
        super().__init__()
        self.add_stage(SunnyStage())

    def act(self, delta_time: float):
            super().act(delta_time)
            if self.elapsed_time > 1:
                self.game.screen = SunnyScreen2()


class SunnyScreen2(game.scene2d.MyScreen):


    def __init__(self):
        super().__init__()
        self.add_stage(SunnyStage())

        def act(self, delta_time: float):
            super().act(delta_time)
            if self.elapsed_time > 1:
                self.game.screen = SunnyScreen()

