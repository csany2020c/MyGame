from Weathersim.NemethCsongor.SuScreen import *
from Weathersim.NemethCsongor.SwScreen import *
from Weathersim.NemethCsongor.RScreen import *


class SuGame(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = SuScreen()

        self.set_on_key_down_listener(self.key_down)

    def set_su(self):
        self.set_screen(SuScreen())

    def set_r(self):
        self.set_screen(RScreen())

    def set_sw(self):
        self.set_screen(SwScreen())

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()


SuGame().run()
