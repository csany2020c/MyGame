import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.nev: str = fields[1]
        self.elet: str = fields[2]
        self.kod: str = fields[3]

    def __str__(self) -> str:
        return "x = {x}; y = {y}; text = {txt}; color = {col}".format(x=self.ev, y=self.nev, txt=self.elet, col=self.kod)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        print(lines)
        print("Load to List")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
        print("Print list")
        for d in datalist:
            print(d)

        print("...")
        f.close()

Main()