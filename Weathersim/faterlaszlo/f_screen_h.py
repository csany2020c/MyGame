from Weathersim.faterlaszlo.f_stage_h import *

class f_screen_h(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(100, 12, 12)
        self.add_stage(f_stage_h())