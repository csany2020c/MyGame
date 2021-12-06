from HawkProductions.over.OverStage import *


class OverScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(OverStage())


class OverScreen2(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(OverStage2())
