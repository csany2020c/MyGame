import game
from retardszisza.menu.MenuScreen import *

class Main(game.scene2d.MyGame):

    def __init__(self):
        super().__init__(1280, 720)
        self.screen = menuscreen()
        self.run()

Main()

