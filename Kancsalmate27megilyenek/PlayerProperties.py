from typing import TextIO, List


class PlayerProperties:
    def __init__(self) -> None:
        super().__init__()
        d:TextIO = open("../Files/playerDatas.txt","r",encoding="utf8")
        content:str = d.read()
        lines:List['str'] = content.split("\n")
        for i in range(1,len(lines)):
            PlayerPropertie(lines[i])
        d.close()

class PlayerPropertie:
    def __init__(self,szoveg:str) -> None:
        super().__init__()
        self.playerLevel:str = str(szoveg[0])
        self.maxAchievedLevel:str = str(szoveg[1])
        self.playerHP:str = str(szoveg[2])
        self.playerDamage:str = str(szoveg[3])
        self.money:str = str(szoveg[4])




class WritePlayerPropertie:

    def __init__(self,pLevel:int,maxLvl:int,playerHP:int,playerDMG:int,money:int) -> None:
        super().__init__()
        self.playerLevel: int = pLevel
        self.maxAchievedLevel: int = maxLvl
        self.playerHP: int = playerHP
        self.playerDamage: int =playerDMG
        self.money: int = money

    def __str__(self) -> str:
        return str(self.playerLevel) + ";" + str(self.maxAchievedLevel) + ";" + str(self.playerHP) + ";" + str(self.playerDamage) + ";" + str(self.money) + ";"

    def writeIt(self):
        w:TextIO = open("../Files/playerDatas.txt","w",encoding="utf8")
        w.write(self.__str__())
PlayerProperties()