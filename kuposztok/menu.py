from kuposztok.MenuScreen import *


class Menu(game.scene2d.MyGame):

    def __init__(self, width: int = 1920, height: int = 1080, autorun: bool = False, autosize: bool = True):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen()


Menu().run()
