from Weathersim.HorvathMark.Stages import *

class Sunnyscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Sunnystage())

class Snowyscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Snowystage())