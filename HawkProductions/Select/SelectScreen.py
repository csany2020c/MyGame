from HawkProductions.Select.SelectStage import *


class SelectScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(120, 125, 125)
        self.add_stage(SelectStage())

