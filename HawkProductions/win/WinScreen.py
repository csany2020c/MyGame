from HawkProductions.win.WinStage import *
import game


class WinScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 250)
        self.add_stage(WinStage())
