import game
from Weathersim.nemethcsababence.Havazas.HavazasScreen import *

class Program(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = HavazasScreen()


Program().run()