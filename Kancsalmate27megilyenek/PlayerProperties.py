from typing import TextIO, List


class PlayerProperties:
    def __init__(self) -> None:
        super().__init__()
        d:TextIO = open("../Files/playerDatas.txt","r",encoding="utf8")
        content:str = d.read()
        self.playerpropertie = None
        lines:List['str'] = content.split("\n")
        for i in range(1,len(lines)):
            self.playerpropertie = PlayerPropertie(lines[i])
        d.close()

    def update(self):
        WritePlayerPropertie(self.playerpropertie.pLevel,self.playerpropertie.mLevel,self.playerpropertie.pHP,self.playerpropertie.pDMG,self.playerpropertie.penz)
        d: TextIO = open("../Files/playerDatas.txt", "r", encoding="utf8")
        content: str = d.read()
        lines: List['str'] = content.split("\n")
        for i in range(1, len(lines)):
            self.playerpropertie = PlayerPropertie(lines[i])
        d.close()

class PlayerPropertie:
    def __init__(self,szoveg:str) -> None:
        super().__init__()
        fields:List['str'] = szoveg.split(";")
        self.playerLevel:str = str(fields[0])
        self.maxAchievedLevel:str = str(fields[1])
        self.playerHP:str = str(fields[2])
        self.playerDamage:str = str(fields[3])
        self.money:str = str(fields[4])

        self.pLevel:float = float(self.playerLevel)
        self.mLevel:int = int(self.maxAchievedLevel)
        self.pHP:int = int(self.playerHP)
        self.pDMG:int = int(self.playerDamage)
        self.penz:int = int(self.money)




class WritePlayerPropertie:

    def __init__(self,pLevel:float,maxLvl:int,playerHP:int,playerDMG:int,money:int) -> None:
        super().__init__()
        self.playerLevel: float = pLevel
        self.maxAchievedLevel: int = maxLvl
        self.playerHP: int = playerHP
        self.playerDamage: int =playerDMG
        self.money: int = money
        w: TextIO = open("../Files/playerDatas.txt", "w", encoding="utf8")
        w.write(self.__str__())

    def __str__(self) -> str:
        return "PlayerLevel;MaxEnemyLevel;PlayerHP;PlayerDamage;Money;"+"\n" + str(self.playerLevel) + ";" + str(self.maxAchievedLevel) + ";" + str(self.playerHP) + ";" + str(self.playerDamage) + ";" + str(self.money) + ";"

PlayerProperties()