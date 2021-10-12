import game
from Weathersim.vizdakmate.Stage import *

class SunnyScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(SunnyStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 7:
            self.game.screen = SnowScreen()


class BackgroundScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(BackgroundStage())

class RainScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(RainStage())
    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 5:
            self.game.screen = SunnyScreen()


class SnowScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(SnowStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 6:
            self.game.screen = SrScreen()

class CloudyScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(CloudyStage())

class SrScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(SrStage())