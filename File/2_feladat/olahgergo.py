from typing import List
from typing import TextIO


class Eloado:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split("\t")
        self.eloadoid: int = int(fields[0])
        self.helyezes: str = fields[1]
        self.zenekar: str = fields[2]

    def __str__(self) -> str:
        return "Helyezés = {x}; Előadó = {y}; Zenekar = {txt}".format(x=self.eloadoid, y=self.helyezes, txt=self.zenekar)

class read:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/eloadok.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Eloado'] = list()
        for s in range(1, len(lines) - 1):
            c = Eloado(lines[s])
            datalist.append(c)

        for d in datalist:
            print(d)
        f.close()

read()