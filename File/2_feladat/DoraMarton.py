import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.dalid: str = fields[0]
        self.eloadoid: str = fields[1]
        self.cimmegjelenes: str = fields[2]

    def __str__(self) -> str:
        return "{x};    {y};    {z}".format(x=self.dalid, y=self.eloadoid, z=self.cimmegjelenes)

class MegegyData:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.ev: str = fields[0]
        self.helyezes: str = fields[1]
        self.dalid: str = fields[2]

    def __str__(self) -> str:
        return "{x};    {y};    {z}".format(x=self.ev, y=self.helyezes, z=self.dalid)

class EsMegegy:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.ev: str = fields[0]
        self.helyezes: str = fields[1]
        self.dalid: str = fields[2]

    def __str__(self) -> str:
        return "{x};    {y};    {z}".format(x=self.ev, y=self.helyezes, z=self.dalid)


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

        f: TextIO = open("!_Specs/lista.txt")
        content: str = f.read()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        print(lines)
        print("Load to List")
        datalist: List['MegegyData'] = list()
        i: int = 0
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
        for d in datalist:
            print(d)

        f: TextIO = open("!_Specs//eloadok.txt", "r", encoding="utf-8")
        content: str = f.read()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        print(lines)
        print("Load to List")
        datalist: List['EsMegegy'] = list()
        i: int = 0
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
        for d in datalist:
            print(d)
        f.close()


Main()
