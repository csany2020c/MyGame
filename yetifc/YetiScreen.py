from yetifc.YetiMenu import *
import game


class MenuScreen3(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 102, 102)
        self.add_stage(Stage3())
