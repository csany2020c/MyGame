import game
from Kancsalmate27megilyenek.MenuStage import *


class MenuScreen3(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 80
        self.g = 80
        self.b = 80
        self.add_stage(Stage3())
