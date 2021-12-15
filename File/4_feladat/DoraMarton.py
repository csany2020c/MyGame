import string
from typing import TextIO
from typing import List

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.helyezes: int = int(fields[0])
        self.sportolok: int = int(fields[1])
        self.sport: str = fields[2]
        self.versenyszam: str = fields[3]

    def __str__(self) -> str:
        return "{h}; {s}; {s2}; {v}".format(h=self.helyezes, s=self.sportolok, s2=self.sport, v=self.versenyszam)

class sziahogyvagy:
    def __init__(self):
        super().__init__()
        f: TextIO = open("!_Specs/helsinki.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(0, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
            print(d)
        f.close()

sziahogyvagy()