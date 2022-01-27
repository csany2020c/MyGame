import random

import game
from game.scene2d import MyStage, MyActor


class HPHUD(game.scene2d.MyActor):
    def __init__(self,x:int,y:int):
        super().__init__("hphud.png")
        self.x = x
        self.y = y
        self.width = 200
        self.height = 150

class HPBAR(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("hpbar.png")
        self.width = 280
        self.height = 9