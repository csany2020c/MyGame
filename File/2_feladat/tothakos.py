from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.eloadoid: str = fields[0]
        self.nev: str = fields[1]
        self.zenekar: str = fields[2]

    def __str__(self) -> str:
        return " eloadoid= {x}; nev = {y}; zenekar = {txt} ".format(x=self.eloadoid, y=self.nev, txt=self.zenekar)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/eloadok.txt")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['eloadoid'] = list()
        for s in range(1, len(lines) -1):
            c = Data(lines[s])
            datalist.append(c)
        for d in datalist:
            print(d)
        f.close()

Main()