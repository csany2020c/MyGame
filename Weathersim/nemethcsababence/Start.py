import game
from Weathersim.nemethcsababence import *
from Weathersim.nemethcsababence.Napsutes import NapsutesScreen
from Weathersim.nemethcsababence.menuuj import MenuScreen
from game.scene2d.MyScreen import *


class Program(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen()
        self.set_on_key_down_listener(self.key_down)

    def set_screen_napsutes(self):
        self.set_screen(NapsutesScreen())

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_4:
            self.screen.add_stage(self.set_screen_napsutes())

Program().run()