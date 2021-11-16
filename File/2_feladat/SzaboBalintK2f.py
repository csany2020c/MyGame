import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.dalid: str = fields[0]
        self.nev: str = fields[1]
        self.list: str = fields[2]

    def __str__(self) -> str:
        return "{a};   {b};   {c}".format(a=self.dalid, b=self.nev, c=self.list)

class DataLista:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.dalid: str = fields[0]
        self.nev: str = fields[1]
        self.list: str = fields[2]

    def __str__(self) -> str:
        return "{x};   {y};   {z}".format(x=self.dalid, y=self.nev, z=self.list)


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs//lista.txt", "r")
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

        f: TextIO = open("!_Specs//dalok.txt", "r")
        content: str = f.read()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        print(lines)
        print("Load to List")
        datalist: List['DataLista'] = list()
        for i in range(1, len(lines) - 1):
            d = DataLista(lines[i])
            datalist.append(d)

        print("Print list")
        for d in datalist:
            print(d)


Main()
