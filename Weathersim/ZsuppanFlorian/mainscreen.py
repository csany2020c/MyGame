from Weathersim.ZsuppanFlorian.mainstage import *
from Weathersim.ZsuppanFlorian import *
import game
import pygame


class Esik(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(EsoStage())


class Napsutes(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(NapStage())


class Havazik(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HoStage())


class Hoeso(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavasesoStage())
