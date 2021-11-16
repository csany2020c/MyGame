from typing import TextIO
from typing import List

class Eloadok:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.eloadoid: str = fields[0]
        self.nev: str = fields[1]
        self.zenekar: str = fields[2]

    def __str__(self) -> str:
        return " eloadoid= {x}; nev = {y}; zenekar = {txt} ".format(x=self.eloadoid, y=self.nev, txt=self.zenekar)

class Dalok:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.dalid: str = fields[0]
        self.eloadoid: str = fields[1]
        self.cim: str = fields[2]
        self.megjelenes: str = fields[3]

class Lista:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.ev: str = fields[0]
        self.helyezes: str = fields[1]
        self.dalid: str = fields[2]

    def __str__(self) -> str:
        return " ev= {x}; helyezes = {y}; dalid = {txt}; ".format(x=self.ev, y=self.helyezes, txt=self.dalid)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/eloadok.txt", 'r', endcoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Eloadok'] = list()
        for i in range(1, len(lines) -1):
            E = Eloadok(lines[i])
            datalist.append(E)

        for d in datalist:
            print(d)
        f.close()

        f: TextIO = open("!_Specs/dalok.txt", 'r')
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Dalok'] = list()
        for i in range(1, len(lines) -1):
            D = Dalok(lines[i])
            datalist.append(D)
        for d in datalist:
            print(d)
        f.close()

        f: TextIO = open("!_Specs/lista.txt", 'r')
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Lista'] = list()
        for i in range(1, len(lines) -1):
            L = Lista(lines[i])
            datalist.append(L)
        for d in datalist:
            print(d)
        f.close()


Main()