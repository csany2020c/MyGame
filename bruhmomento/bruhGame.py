from bruhmomento.bruhScreen import *
import game



class bruh(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = bruhScreen()



bruh().run()