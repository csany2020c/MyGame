import game
from Weathersim.RigoDonat.stages import *

class Sunny(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(SunnyStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 10:
            self.game.screen = Rain()

class Rain(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(RainStage())




