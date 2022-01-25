from typing import TextIO
from typing import List
class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.nev: str = str(fields[0])
        self.hossz: float = float(fields[1])
        self.kiterjedes: float = float(fields[2])
        self.melyseg: float = float(fields[3])
        self.magassag: float = float(fields[4])
        self.telepules: str = str(fields[5])

    def __str__(self) -> str:
        return "Nev: = {x}; Hossz: = {y}; Kiterjedes: = {c}; Melyseg: = {v}; Magassag: = {b}; Telepules: = {n}".format(x = self.nev, y = self.hossz, c = self.kiterjedes, v = self.melyseg, b = self.magassag, n = self.telepules)

class Main:

    def __init__(self) -> None:
        super().__init__()