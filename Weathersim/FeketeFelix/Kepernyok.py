import game
from Weathersim.FeketeFelix.Stages import *

class SunnyScreen(game.scene2d.MyScreen):


    def __init__(self):
        super().__init__()
        self.add_stage(SunnyStage())


class RainScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(RainStage())

class SnowScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(SnowStage())

class SnowRainScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(SnowRainStage())

