from typing import List
from typing import TextIO


class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.het: int = int(fields[1])
        self.fordulo: int = int(fields[2])
        self.Telitalalat: int = int(fields[3])
        self.Nyeremeny: int = int(fields[4])
        self.eredmenyek: str = fields[5]

    def __str__(self) -> str:
        return "ev = {ev}; het = {h}; fordulo = {f}; Telitalalat = {t}; Nyeremeny = {ny}; eredmenyek = {er} ".format(ev=self.ev, h=self.het, f=self.fordulo, t=self.Telitalalat, ny=self.Nyeremeny, er=self.eredmenyek)


class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("toto.txt", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()

        for i in range(0, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
        f.close()


Main()
