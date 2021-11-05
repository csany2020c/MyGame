from HawkProductions.Select.SelectStage import *


class SelectScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(120, 125, 125)
        self.add_stage(SelectStgage())


class SelectScreen2(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(120, 125, 125)
        self.add_stage(SelectStage2())


class SelectScreen3(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(120, 125, 125)
        self.add_stage(SelectStage3())
