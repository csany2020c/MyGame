from Weathersim.KisKornel.Stage import *

class SunnyScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(SunnyStage())


class SnowyScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(SnowStage())

class RainScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(RainStage())

class MenuScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(MenuStage())

