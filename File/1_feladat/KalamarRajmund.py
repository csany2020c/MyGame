import string
from typing import TextIO
from typing import List

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        print("Create Data from String")
        print(parseString)

class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        print("Load to List")
        datalist: List['Data'] = list()
        for str in lines:
            d = Data(str)
            datalist.append(d)
        print("Print list")
        for c in datalist:
            print(c)
        f.close()


Main()