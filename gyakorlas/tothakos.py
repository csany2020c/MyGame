from typing import List
from typing import TextIO

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.het: int = int(fields[1])
        self.fordulo: int = int(fields[2])
        self.T13p1: int = int(fields[3])
        self.Ny13p1: int = int(fields[4])
        self.eredmenyek: str = fields[5]

    def __str__(self) -> str:
        return "Év = {x}; Hét = {y}; Forduló = {txt}; T13p1 = {col}; Ny13p1 = {z}; Eredmények = {v}".format(x=self.ev, y=self.het, txt=self.fordulo, col=self.T13p1, z=self.Ny13p1, v=self.eredmenyek)

class Feladat:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("toto.txt", encoding="utf-8")
        content: str = f.read()

Feladat()