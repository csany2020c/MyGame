import game
from kuposztok.Menu.MenuScreen import MenuScreen
from kuposztok.Devicesave.DeviceSaveScreen import DeviceSaveScreen


class Game(game.scene2d.MyGame):

    def __init__(self, width: int = 1920, height: int = 1080, autorun: bool = False, autosize: bool = True):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen()



Game().run()