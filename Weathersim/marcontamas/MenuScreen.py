import game
from Weathersim.marcontamas.MenuStage import *

class MenuScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(MenuStage())
