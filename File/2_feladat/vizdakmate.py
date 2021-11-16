import string
from typing import TextIO
from typing import List

class Eloadok:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        #print("Create Data from String")
        #print(parseString)
        fields: List['str'] = parseString.split(";")
        #self.text: str = ""
        self.eloado: int = fields[0]
        self.nev: str = fields[1]
        self.zenekar: str = fields[2]


class Dalok:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.dalid: int = int(fields[0])
        self.eloadoid: int = int(fields[1])
        self.cim: str = fields[2]
        self.megjelenes: int = int(fields[3])

    def __str__(self) -> str:
        return "DalID = {x}; EloadoID = {y}; Cim = {txt}; Megjelenes = {col}".format(x=self.dalid, y=self.eloadoid,
                                                                                     txt=self.cim, col=self.megjelenes)


class olvasas:

    def __init__(self) -> None:
        f: TextIO = open("!_Specs/dalok.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Dal'] = list()
        for i in range(1, len(lines) - 1):
            D = Dalok(lines[i])
            datalist.append(D)

        for d in datalist:
            print(d)
        f.close()
        f: TextIO = open("!_Specs/eloadok.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Dal'] = list()
        for i in range(1, len(lines) - 1):
            E = Eloadok(lines[i])
            datalist.append(E)

        for d in datalist:
            print(d)
        f.close()

olvasas()