import random

import game
from game.scene2d import MyStage, MyActor


class HPBAR(game.scene2d.MyActor):
    def __init__(self,x:int,y:int):
        super().__init__("hpbar.png")
        self.x = x
        self.y = y

class REDHP(game.scene2d.MyActor):

    def __init__(self,x:float,y:float):
        super().__init__("red.png")
        self.x:float = float(x+3)
        self.y:float = float(y+3)
        self.height = 19