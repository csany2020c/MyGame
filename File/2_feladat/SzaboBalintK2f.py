import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.dalid: str = fields[1]
        self.nev: str = fields[2]
        self.list: str = fields[3]

    def __str__(self) -> str:
        return "{a};   {b};   {c}".format(a=self.dalid, b=self.nev, c=self.list)


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs//dalok.txt", "r")
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

class Data2:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.dalid: str = fields[1]
        self.nev: str = fields[2]
        self.list: str = fields[3]

        self.eloadoid: str = fields[1]
        self.nev2: str = fields[2]
        self.zenekar: str = fields[3]

    def __str__(self) -> str:
        return "{x};   {y};   {text}".format(x=self.eloadoid, y=self.nev2, text=self.zenekar)


class Main2:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs//eloadok.txt", "r")
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


Main2()
Main()