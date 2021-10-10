import game
from HawkProductions.GameScreen import *


class Game(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = GameScreen()


Game().run()
