import string
from typing import TextIO
from typing import List

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.het: int = int(fields[1])
        self.fordulo: int = int(fields[2])
        self.telitalalat: int = int(fields[3])
        self.nyeremeny: int = int(fields[4])
        eredmenyek:List['str'] = fields[2].split("x")

    def __str__(self) -> str:
        return "ev = {ev}; het = {h}; fordulo = {f}; telitalalat = {t}; nyeremeny = {ny}; eredmenyek = {e} ".format(ev=self.ev, h=self.het, f=self.fordulo, t=self.telitalalat, ny=self.nyeremeny, e=self.eredmenyek)


class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("gyakorlas/toto.txt", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(0, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
        f.close()
        #3.feladat
        print("Fordulok száma: " + str(len(lines)))
        #4.feladat
        t = 0


Main()