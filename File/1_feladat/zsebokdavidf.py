import string
from typing import TextIO
from typing import List


class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.nev: str = fields[1]
        self.elethalal: str = fields[2]
        self.orszagkod: str = fields[3]

    def __str__(self) -> str:
        return "{x};   {y};   {txt};   {col}".format(x=self.ev, y=self.nev, txt=self.elethalal, col=self.orszagkod)


class Fajlbeolvasas:

    def __init__(self):
        szoveg: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = szoveg.read()
        szoveg.close()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            data = Data(lines[i])
            datalist.append(data)
        print(data)


Fajlbeolvasas()
