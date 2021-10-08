from Weathersim.horvathboldizsar.GameStage import *


class NaposScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(NaposStage())

class EsosScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(EsosStage())

class HavasScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavasStage())

class HavasesoScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavasesosStage())