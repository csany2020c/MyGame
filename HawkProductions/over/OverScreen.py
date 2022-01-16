from HawkProductions.over.OverStage import *


class OverScreen(game.scene2d.MyScreen):
    def __init__(self, a: int):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(OverStage(a))


class OverScreen2(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(OverStage2())


class OverScreen3(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(OverStage3())
