import game
from Kancsalmate27megilyenek.WinScreen import *

class WinGame(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = WinScreen()
        self.run()

WinGame()