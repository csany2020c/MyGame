import game
from Weathersim.faterlaszlo.f_sun1.f_stage1 import *

class f_screen1(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(f_stage1())