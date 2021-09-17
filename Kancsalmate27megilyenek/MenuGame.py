from Kancsalmate27megilyenek.MenuScreen import *
import game


class MainGame(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720):
        super().__init__(width, height)
        self.screen = MenuScreen3()


MainGame()
