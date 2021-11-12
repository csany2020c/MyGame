import string
from typing import TextIO
from typing import List
class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("   ")
        self.dalid: str = fields[0]
        self.eloadoid: str = fields[1]
        self.cimmegjelenes: str = fields[2]

    def __str__(self) -> str:
        return "{x}; {y}; {z}".format(x=self.dalid, y=self.eloadoid, z=self.cimmegjelenes)

class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/dalok.txt")
        content: str = f.read()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        print(lines)
        print("Load to List")
        datalist: List['Data'] = list()
        i: int = 0
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
        for d in datalist:
            print(d)
        f.close()


Main()
