from Weathersim.HorvathMark.Stages import *

class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Sunnystage())