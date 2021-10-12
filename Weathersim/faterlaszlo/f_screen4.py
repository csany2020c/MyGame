from Weathersim.faterlaszlo.f_stage4 import *

class f_screen4(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(f_stage4())