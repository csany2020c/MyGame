import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\n")
        self.helyezes: int = int(fields[0])
        self.tagok: int = int(fields[1])
        self.sport: str = fields[2]
        self.csapat: str = fields[3]

    def __str__(self) -> str:
        return "{a}; {b}; {c}; {d};".format(a=self.helyezes, b=self.tagok, c=self.sport, d=self.csapat)

class Main:

    def __init__(self) -> None:
        super().__init__()
        print("")
        print("Adatok:")
        f: TextIO = open("!_Specs//helsinki.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 0):
            d = Data(lines[i])
            datalist.append(d)

        for d in datalist:
            print(d)
        f.close()

Main()