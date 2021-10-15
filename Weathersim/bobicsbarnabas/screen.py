import game
from Weathersim.bobicsbarnabas.stage import *

class napsutesscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(napsutesstage())

class havazasscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(havazasstage())

class havasesoscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(havasesostage())

class esoscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(esostage())