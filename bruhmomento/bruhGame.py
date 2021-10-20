from bruhmomento.bruhScreen import *
from bruhmomento.bruhActor import *
import game



class bruh(game.scene2d.MyGame):

    def __init__(self, width: int =1280, height: int = 720):
        super().__init__(width, height)
        self.screen = bruhScreen()

bruh().run()