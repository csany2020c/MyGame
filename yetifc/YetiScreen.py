from yetifc.YetiMenu import *
import game


class MenuScreen3(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 0
        self.g = 102
        self.b = 102
        self.add_stage(Stage3())
