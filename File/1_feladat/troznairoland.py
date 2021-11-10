import string
from typing import TextIO
from typing import List

class Adat:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.ev: str = fields[0]
        self.nev: str = fields[1]
        self.szuletes_halalozas: str = fields[2]
        self.orszagkod: str = fields[3]

    def __str__(self) -> str:
        return "{x};   {y};   {txt};   {col}".format(x=self.ev, y=self.nev, txt=self.szuletes_halalozas, col=self.orszagkod)

class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("orvosi_nobeldijak.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Adat'] = list()
        for i in range(1, len(lines) - 1):
            d = Adat(lines[i])
            datalist.append(d)
        for d in datalist:
            print(d)
        f.close()


Main()