import game
from kuposztok.Menu.MenuScreen import MenuScreen


class Game(game.scene2d.MyGame):

    def __init__(self, width: int = 1270, height: int = 720, autorun: bool = False, autosize: bool = True):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen()


Game().run()