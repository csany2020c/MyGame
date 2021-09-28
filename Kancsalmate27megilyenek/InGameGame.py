import game
from Kancsalmate27megilyenek.InGameScreen import *

class InGame(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = InScreen()
        self.run()

InGame()