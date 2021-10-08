from Weathersim.horvathboldizsar.GameScreen import *
from Weathersim.horvathboldizsar.MenuScreen import *

class Simulator(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720):
        super().__init__(width, height)
        self.screen = MenuScreen()

Simulator().run()