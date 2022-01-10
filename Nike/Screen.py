import  game
from  Nike.Stage import *

class Menu(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(100,0,100)
        self.add_stage(MenuStage())
