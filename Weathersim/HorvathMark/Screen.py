from Weathersim.HorvathMark.Stages import *

class Sunnyscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Sunnystage())

class Snowyscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Snowystage())

class Rainyscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Rainystage())

class SnowyRainscreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(SnowyRainstage())
