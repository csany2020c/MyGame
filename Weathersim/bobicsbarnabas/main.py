import game
from Weathersim.bobicsbarnabas.menu.menuscreen import *

class kep(game.scene2d.MyGame):

    def __init__(self):
        super().__init__(1280, 720)
        self.screen = menuscreen()
        self.run()


kep()