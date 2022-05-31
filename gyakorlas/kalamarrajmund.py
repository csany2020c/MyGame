from typing import List
from typing import TextIO

class Adatok:
    def __init__(self, parse: str) -> None:
        super().__init__()
        fields: List['str'] = parse.split(" ")
        self.ev: int = int(fields[0])
        self.het: int = int(fields[1])
        self.fordulo: int = int(fields[2])
        self.t13p1: int = int(fields[3])
        self.ny13p1: int = int(fields[4])
        self.eredmenyek: str = fields[5]



    def __str__(self) -> str:
        return "Év = {x}; Hét = {y}; Forduló = {txt}; T13p1 = {col}; Ny13p1 = {z}; Eredmények = {v}".format(x=self.ev, y=self.het, txt=self.fordulo, col=self.t13p1, z=self.ny13p1, v=self.eredmenyek)

class beolvasas:
    def __init__(self, filename: str) -> None:
        super().__init__()
        self.hetek: List['Het'] = list()
        f = open(filename, encoding="utf-8", mode="r")
        content: List['str'] = f.read().strip().split(sep="\n")
        

    def fordulokszama(self):
        print("3. Feladat:")










f: beolvasas = beolvasas("toto.txt")
f.fordulokszama()