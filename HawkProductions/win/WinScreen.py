from HawkProductions.win.WinStage import *
import game


class WinScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(WinStage())