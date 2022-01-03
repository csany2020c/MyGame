from typing import List
from typing import TextIO

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(" ")
        self.helyezes: int = int(fields[0])
        self.szam: int = int(fields[1])
        self.sportag: str = fields[2]
        self.versenyszam: str = fields[3]


    def __str__(self) -> str:
        return "Helyezés = {x}; Szám = {y}; Sportág = {txt}; Versenyszám = {col}".format(x=self.helyezes, y=self.szam, txt=self.sportag, col=self.versenyszam)



class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/helsinki.txt", encoding="utf8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            datalist.append(Data(lines[i]))
        f.close()