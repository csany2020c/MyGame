from bruhmomento.bruhScreen import *
from bruhmomento.bruhActor import *
import game



class bruh(game.scene2d.MyGame):

    def __init__(self, width: int =1280, height: int = 720):
        super().__init__(width, height)
        self.screen = bruhScreen()
        if bruhActor.x == 1200 and bruhActor.y == 720:
            self.screen = level2Screen()



bruh().run()