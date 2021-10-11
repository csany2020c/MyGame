from HawkProductions.InfoStage import *


class IScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(IStage())
