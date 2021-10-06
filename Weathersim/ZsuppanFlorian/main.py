from Weathersim.ZsuppanFlorian.mainscreen import *
import game

class MainStage(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MainScreen()


MainStage().run()
