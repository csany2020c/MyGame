from typing import List

import game

class ArrowActor(game.scene2d.MyActor):
    def __init__(self,cords:list):
        super().__init__("arrow.png")
        self.thiscord = cords
        self.cords:List['int'] = list()
        self.count = 0
        self.fly = True
        self.width = 69
        self.height = 19

    def act(self, delta_time: float):
        super().act(delta_time)
        if (self.fly == True):
            self.x = self.defineCords(self.count+1)[0]
            self.y = self.defineCords(self.count + 1)[1]
            self.count+=1


    def defineCords(self,index) -> list:
        if index< len(self.thiscord):
            self.fly = True
            return self.thiscord[index]
        else:
            self.fly = False
            return [0,0]


class ArrowActor2(game.scene2d.MyActor):
    def __init__(self,cords:list,damage:int):
        super().__init__("arrow.png")
        self.thiscord = cords
        self.damage = damage
        self.cords:List['int'] = list()
        self.count = 0
        self.fly = True
        self.width = 69
        self.height = 19

    def act(self, delta_time: float):
        super().act(delta_time)
        if (self.fly == True):
            self.x = self.defineCords(self.count+1)[0]
            self.y = self.defineCords(self.count + 1)[1]
            self.count+=1


    def defineCords(self,index) -> list:
        if index< len(self.thiscord):
            self.fly = True
            return self.thiscord[index]
        else:
            self.fly = False
            return [-9999999,0]








