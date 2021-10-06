from Weathersim.zsebokdavidf.MainScreen import *


class Main(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MainScreen()


Main().run()
