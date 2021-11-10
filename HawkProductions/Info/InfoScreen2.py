from HawkProductions.Info.Infostage2 import *

class IScreen2(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(1, 122, 10)
        self.add_stage(Istage2())