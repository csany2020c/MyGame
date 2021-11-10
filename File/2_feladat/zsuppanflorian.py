import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split("\t")
        self.elso: int = int(fields[0])
        self.masodik: str = fields[1]
        self.harmadik: str = fields[2]

    def __str__(self) -> str:
        return " ArtistID = {a}; Name = {b}; Band = {c}".format(a=self.elso, b=self.masodik, c=self.harmadik)

class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs//eloadok.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
        for d in datalist:
            print(d)
        f.close()

Main()