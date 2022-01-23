from typing import TextIO, List

import game

class Enemys:
    def __init__(self) -> None:
        super().__init__()
        f:TextIO = open("enemyTypes.txt","r",encoding="utf8")
        content:str = f.read()
        lines:List['str'] = content.split("\n")
        self.enemys:List['Enemy'] = list()
        for i in range(1,len(lines)):
            self.enemys.append(Enemy(lines[i]))


    def getEnemys(self) -> List['Enemy']:
        return self.enemys


class Enemy:

    def __init__(self,parseStr:str) -> None:
        super().__init__()
        fields:List['str'] = parseStr.split(";")
        self.name = fields[0]
        self.hp = fields[1]
        self.damage = fields[2]
        self.chance = fields[3]
        self.image = fields[4]

    def __str__(self) -> str:
        return "NEV: " + self.name + "HP: " + self.hp + "DAMAGE: " + self.damage + "ESELY: " + self.chance
