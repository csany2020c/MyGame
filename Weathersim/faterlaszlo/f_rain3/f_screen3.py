import game
from Weathersim.faterlaszlo.f_rain3.f_stage3 import *

class f_screen3(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(f_stage3())