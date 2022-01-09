import string
from typing import TextIO
from typing import List

class Lista:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split("\t")
        self.dalid: int = int(fields[0])
        self.eloadoid: str = str(fields[1])
        self.cim: str = str(fields[2])
        self.megjelenes: str = str(fields[3])
    def __str__(self) -> str:
        return "Dalid = {x}; Eloadoid = {y}; Cim = {txt}; Megjelenes = {col}".format(x=self.id, y=self.name, txt=self.band, col=self.megjelenes)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs//dalok.txt", "r", encoding = "UTF-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")

        dalokszam: List['Lista'] = list()

        for i in range(1, len(lines) - 1):
            dalokszam.append(Lista(lines[i]))

        #kiírja a dalok számát
        print("Dalok száma: {db} szám".format(db=len(dalokszam)))







        f.close()

Main()