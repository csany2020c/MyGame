import game
from f_stage import *

class f_screen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        #self.set_background_color(120, 100, 90)
        self.add_stage(f_stage())
