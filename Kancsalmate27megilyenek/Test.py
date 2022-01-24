import math
from typing import List

from pygame import Vector2
from Kancsalmate27megilyenek.TestActor import TestActor
from game.scene2d import MyActor, MyStage


class Test():

    def __init__(self) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
        self.X:List['int'] = list()
        self.Y:List['int'] = list()
    def getPositions(self,x1,x2,y1,y2):
        if (x2 - x1 >= 0):
            for i in range(int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))):
                self.y = ((y2-y1)/(x2-x1)) * (i-x1) + y1
                self.x = i
                self.X.append(self.x)
                self.Y.append(self.y)
                #actor.x = x
                #actor.y = y
        else:
            y=y2-y1
            for i in range(y2 -y1 ):
                self.y+=1
Test()