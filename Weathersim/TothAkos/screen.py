from Weathersim.TothAkos.stage import *

class Sunnyscr(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(Sunnystage())

class Snowyscr(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(Snowystage())

class Rainyscr(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(Rainystage())

class Havasesoscr(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(Havasesostage())
