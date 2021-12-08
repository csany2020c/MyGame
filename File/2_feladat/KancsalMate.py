import string
from typing import TextIO
from typing import List

class Artists:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split("\t")
        self.id: int = int(fields[0])
        self.name: str = str(fields[1])
        self.band: str = str(fields[2])
    def __str__(self) -> str:
        return "Id = {x}; Név = {y}; Zenekar = {txt}; ".format(x=self.id, y=self.name, txt=self.band,)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs//dalok.txt", "r", encoding = "UTF-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Artists'] = list()
        for i in range(1, len(lines)):
            d = Artists(lines[i])
            datalist.append(d)

        for d in datalist:
            print(d)
        f.close()

Main()