import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str, ):
        fields: List['str'] = parseString.split("\t")

        self.eloadoid: int = int(fields[0])
        self.helyezes: str = fields[1]
        self.zenekar: str = fields[2]

    def __str__(self) -> str:
        return "Előadó = {x}; Helyezés = {y}; Zenekar = {txt}".format(x=self.eloadoid, y=self.helyezes, txt=self.zenekar)

class Fajl:

    def __init__(self):
        f: TextIO = open("!_Specs/eloadok.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for s in range(1, len(lines) - 1):
            c = Data(lines[s])
            datalist.append(c)

        for d in datalist:
            print(d)
        f.close()

Fajl()
