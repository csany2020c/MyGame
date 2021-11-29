import game
from Impostorsus.Game.WarioActor import *
from Impostorsus.Game.WarioMinden import *

class WarioScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 245
        self.g = 71
        self.b = 146
        self.add_stage(ASD())


class MenuScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 200
        self.g = 100
        self.b = 0
        self.add_stage(ASD2())

class BindingsScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 92
        self.g = 148
        self.b = 252
        self.add_stage(BindingsStage())

class CreditScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 92
        self.g = 148
        self.b = 252
        self.add_stage(CreditStage())


