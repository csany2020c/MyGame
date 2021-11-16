import game

from Impostorsus.Game.WarioActor import *
from Impostorsus.Game.WarioStage import *
from Impostorsus.Game.WarioScreen import *
import Impostorsus.Game.WarioScreen

class Wario(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = WarioScr()
        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        print(sender)
        print(event)

        if event.key == pygame.K_r:
            print("'hoppáré'")
            self.screen = WarioScr()

Wario().run()


