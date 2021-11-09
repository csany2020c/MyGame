from typing import List
from typing import TextIO

class Lista:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.ev: int = int(fields[0])
        self.helyezes: int = int(fields[1])
        self.dalid: int = int(fields[2])

    def __str__(self) -> str:
        return "Year = {x}; Place = {y}; SongID = {txt}".format(x=self.ev, y=self.helyezes, txt=self.dalid)


class Dal:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("   ")
        self.dalid: int = int(fields[0])
        self.eloadoid: int = int(fields[1])
        self.cim: int = int(fields[2])
        self.megjelenes: int = int(fields[3])

class Eloado:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("   ")
        self.eloadoid: int = int(fields[0])
        self.nev: str = fields[1]
        self.zenekar: str = fields[2]

class olvasas:
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

olvasas()