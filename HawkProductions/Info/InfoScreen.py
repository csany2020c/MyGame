from HawkProductions.Info.InfoStage import *


class IScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(1, 122, 10)
        self.add_stage(IStage())

