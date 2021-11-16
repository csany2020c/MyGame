from typing import List
from typing import TextIO

class lista:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.ev: int = int(fields[0])
        self.helyezes: int = int(fields[1])
        self.dalid: int = int(fields[2])

    def __str__(self) -> str:
        return "ev = {x}; helyezes = {y}; dalID = {txt}".format(x=self.ev, y=self.helyezes, txt=self.dalid)




class eloado:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.eloadoID: int = int(fields[0])
        self.nev: str = fields[1]
        self.zenekar: int = int(fields[2])

    def __str__(self) -> str:
        return "eloadoID = {x}; nev = {y}; zenekar = {txt}".format(x=self.eloadoID, y=self.nev, txt=self.zenekar)

class Dal:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.dalid: int = int(fields[0])
        self.eloadoid: int = int(fields[1])
        self.cim: str = fields[2]
        self.megjelenes: int = int(fields[3])

    def __str__(self) -> str:
        return "dalID = {x}; eloadoID = {y}; cim = {txt}; megjelenes = {col}".format(x=self.dalid, y=self.eloadoid, txt=self.cim, col=self.megjelenes)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/lista.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Lista'] = list()
        for i in range(1, len(lines) - 1):
            l = Lista(lines[i])
            datalist.append(l)

        for d in datalist:
            print(d)
        f.close()

Main()