import game
from Weathersim.RigoDonat.stages import *

class Menu(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(MenuStage())

class Sunny(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(SunnyStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 15:
            self.game.screen = Rain()

class Rain(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(RainStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 15:
            self.game.screen = RainSnow()

class RainSnow(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(RainSnowStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 15:
            self.game.screen = Snow()

class Snow(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(SnowStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 15:
            self.game.screen = End()


class End(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(EndStage())
    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 5:
            self.game.screen = Menu()


