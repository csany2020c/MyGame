import game
from Weathersim.faterlaszlo.f_stage_m import *

class f_screen_m(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(20, 120, 100)
        self.add_stage(f_stage_m())