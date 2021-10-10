import game
from Weathersim.faterlaszlo.f_snowyrain2.f_stage2 import *

class f_screen2(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(f_stage2())

