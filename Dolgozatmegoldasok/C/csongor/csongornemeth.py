import string
from typing import TextIO
from typing import List


class Data:
    def __init__(self, parse: str) -> None:
        super().__init__()
        fields: List['str'] = parse.split("\t")
        self.nev: str = str(fields[0])
        self.hossz: int = int(fields[1])
        self.kiterjedes: int = int(fields[2])
        self.melyseg: int = int(fields[3])
        self.magassag: int = int(fields[4])
        self.telepules: str = str(fields[5])

    def __str__(self) -> str:
        return "nev = {nev}; hossz = {hos}; kiterjedes = {kit}; melyseg = nev{mely}; magassag = {mag}; telepules = {tel}".format(nev=self.nev, hos=self.hossz, kit=self.kiterjedes, mely=self.melyseg, mag=self.magassag, tel=self.telepules)


class Read:
    def __init__(self):
        super().__init__()
        f: TextIO = open("C/csongor/barlang", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(0, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
            print(d)
        f.close()


Read()
