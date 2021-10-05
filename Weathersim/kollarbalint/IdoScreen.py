import game
import pygame
from Weathersim.kollarbalint.IdoStage import *

class NapsutesScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(NapsutesStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 10:
            self.game.screen = EsoScr()

class EsoScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(EsoStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 10:
            self.game.screen = HavazasScr()

class HavazasScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavazasStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 10:
            self.game.screen = HavasesoScr()

class HavasesoScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavasesoStage())

class MenuScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(252, 98, 3)
        self.add_stage(MenuStage())
