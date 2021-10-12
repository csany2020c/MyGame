import game
from Weathersim.marcontamas.MenuScreen import *

class Starter(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False,
                 debug: bool = False):
        super().__init__(width, height, autorun, autosize, debug)
        self.screen = MenuScreen()

Starter().run()