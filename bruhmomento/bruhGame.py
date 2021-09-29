from bruhmomento.bruhScreen import *
import game



class bruh(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = bruhScreen()



bruh().run()