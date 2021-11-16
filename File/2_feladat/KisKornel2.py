import string
from typing import TextIO
from typing import List


class Data:



    def __init__(self, parseString: str) -> None:
        super().__init__()
        print("Create Data from String")
        print(parseString)

        fields: List['str'] = parseString.split("   ")

        self.dalid: str = fields[1]
        self.nev: str = fields[2]
        self.list: str = fields[3]


    def __str__(self) -> str:

        return "x = {x}; y = {y}; text = {txt};".format(x=self.dalid, y=self.nev, txt=self.list)


class Main:
    def __init__(self) -> None:
        super().__init__()
        i: int = 0
        f: TextIO = open("!_Specs/lista.txt", "r")
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

        g: TextIO = open("!_Specs/dalok.txt", "r")
        content: str = g.read()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="/\n")
        print("Split content")
        print(lines)
        print("Load to list")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            a = Data(lines[i])
            datalist.append(a)
        print("Print list")
        for a in datalist:
            print(a)

        f.close()
Main()