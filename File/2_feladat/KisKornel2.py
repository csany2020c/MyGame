import string
from typing import TextIO
from typing import List


class Eloadok:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.eloado: str = fields[1]
        self.nev: str = fields[2]
        self.zenekar: str = fields[3]


    def __str__(self) -> str:

        return "x = {x}; y = {y}; text = {txt};".format(x=self.eloado, y=self.nev, txt=self.zenekar)

class dalok:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.dalid: str = fields[1]
        self.eloadoid: str = fields[2]
        self.cim: str = fields[3]
        self.megjelenes: str = fields[4]

    def __str__(self) -> str:
        return "x = {x}; y = {y}; a = {a}; b = {b}".format(x=self.dalid, y=self.eloadoid, a=self.cim, b=self.megjelenes)

class lista:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.ev: str = fields[1]
        self.helyezes: str = fields[2]
        self.dalid: str = fields[3]


    def __str__(self) -> str:
        return "x = {x}; y = {y}; a = {a};".format(x=self.ev, y=self.helyezes, a=self.dalid)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/eloadok.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Eloadok'] = list()
        for i in range(1, len(lines) - 1):
            d = Eloadok(lines[i])
            datalist.append(d)
        for d in datalist:
            print(d)

        f: TextIO = open("!_Specs/dalok.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['dalok'] = list()
        for i in range(1, len(lines) - 1):
            e = dalok(lines[i])
            datalist.append(e)
        for e in datalist:
            print(e)

        f: TextIO = open("!_Specs/lista.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['lista'] = list()
        for i in range(1, len(lines) - 1):
            x = lista(lines[i])
            datalist.append(x)
        for x in datalist:
            print(x)


Main()
