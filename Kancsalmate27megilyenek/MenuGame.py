from Kancsalmate27megilyenek.MenuScreen import *
import game


class MainGame(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = True):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen3()
        self.run()
MainGame()
