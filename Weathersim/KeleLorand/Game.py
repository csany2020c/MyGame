import game
from Weathersim.KeleLorand.GameScreen import *

class Game(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = True):
        super().__init__(width, height, autorun)
        self.screen = Screen()

Game()