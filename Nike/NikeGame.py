import game
from Nike.NikeScreen import *


class Nike(game.scene2d.MyGame):

    def __init__(self):
        super().__init__(1280, 720)
        self.set_screen(NikeScreen())
        self.run()