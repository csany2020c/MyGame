import game
from Nike.NikeStage import *

class Menu(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(100,0,100)
        self.add_stage(MenuStage())

class Game(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())
