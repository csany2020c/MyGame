import game
from Kancsalmate27megilyenek.InfoScreen import *

class InfoGame(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = InfoScreen()
        self.run()

InfoGame()