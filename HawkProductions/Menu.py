import game
from HawkProductions.menu.MenuScreen import *


class Menu(game.scene2d.MyGame):
    def __init__(self):
        super().__init__()
        self.screen = MenuScreen()

        self.set_on_key_down_listener(self.katt)

    def katt(self, sender, event):
        print(sender)
        if event.key == pygame.K_ESCAPE:
            quit()


Menu().run()
