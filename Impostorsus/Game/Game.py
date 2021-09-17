import game
from WarioScreen import *

class Wario(game.scene2d.MyGame):

    def __init__(self):
        super().__init__(1280, 720)
        self.screen = WarioScr()
        self.run()

