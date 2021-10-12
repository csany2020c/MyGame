from Weathersim.horvathboldizsar.GameStage import *
from Weathersim.horvathboldizsar.MiniMenuButtonStage import *


class NaposScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(NaposStage())
        self.add_stage(MiniStage())


class EsosScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(EsosStage())
        self.add_stage(MiniStage())


class HavasScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavasStage())
        self.add_stage(MiniStage())


class HavasesoScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavasesosStage())
        self.add_stage(MiniStage())
