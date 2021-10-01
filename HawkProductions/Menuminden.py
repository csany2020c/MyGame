import game
from HawkProductions.MenuScreen import *


class Menuminden(game.scene2d.MyGame):
    def __init__(self):
        super().__init__()
        self.set_screen(MenuScreen())