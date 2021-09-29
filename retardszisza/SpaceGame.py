import game
from retardszisza.GameScreen import *


class Space(game.scene2d.MyGame):

    def __init__(self):
        super().__init__(1280, 720)
        self.set_screen(GameScreen())
        self.run()

