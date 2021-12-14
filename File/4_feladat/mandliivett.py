from typing import TextIO
from typing import List


class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/helsinki.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
            print(d)
        f.close()

Main()
