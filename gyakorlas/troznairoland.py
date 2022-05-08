from typing import List
from typing import TextIO

class Data:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(";")
        self.ev: str = str(fields[0])
        self.het: str = fields[1]
        self.fordulo: str = fields[2]
        self.t13p1: str = fields[3]
        self.ny13p1: str = fields[4]
        self.eredmenyek: str = fields[5]

    def __str__(self) -> str:
        return "Év = {ev}; Hét = {het}; Forduló = {ford}; T13p1 = {t13p1}; Ny13p1 = {ny13p1}; Eredmények = {eredm}".format(ev=self.ev, het=self.het, ford=self.fordulo, t13p1=self.t13p1, ny13p1= self.ny13p1, eredm=self.eredmenyek)

class Feladatok:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("toto.txt", "r", encoding="utf-8")
        content: str = f.read()
        line: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(line)):
            d = Data(line[i])
            datalist.append(d)
            print(d)

Feladatok()