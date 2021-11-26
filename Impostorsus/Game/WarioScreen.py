import game
from Impostorsus.Game.WarioActor import *
from Impostorsus.Game.WarioMinden import *


class WarioScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 245
        self.g = 71
        self.b = 146
        self.add_stage(WarioStage1())

class MenuScr(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 200
        self.g = 100
        self.b = 0
        self.add_stage(MenuStage())


class ASDSCR(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 245
        self.g = 71
        self.b = 146
        self.add_stage(ASD())


class ASDSCR2(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 200
        self.g = 100
        self.b = 0
        self.add_stage(ASD2())


