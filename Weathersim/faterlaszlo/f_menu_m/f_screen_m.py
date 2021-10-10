import game
from Weathersim.faterlaszlo.f_menu_m.f_stage_m import *

class f_screen_m(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(f_stage_m())