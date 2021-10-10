import game
from Weathersim.faterlaszlo.f_screen_m import *


class f_game(game.scene2d.MyGame):
    def __init__(self, width=1280, height=720):
        super().__init__(width, height)
        self.screen = f_screen_m()