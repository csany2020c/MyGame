from typing import TextIO
from typing import List
import string

class Data:
    def __init__(self, paraString: str) -> None:
        super().__init__()
        print(paraString)

        lines: List['str'] = paraString.split("\t")
        print(lines)
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)


class dalok:
    def __init__(self) -> None:
        super().__init__()
        d: TextIO = open("!_Specs/dalok.txt", "r", encoding="utf-8")
        content: str = d.read()

        print(content)


class eloado:
    def __init__(self) -> None:
        super().__init__()
        e: TextIO = open("!_Specs/eloadok.txt", "r", encoding="utf-8")

        content: str = e.read()
        print(content)

class lista:
    def __init__(self) -> None:
        super().__init__()
        l: TextIO = open("!_Specs/lista.txt", "r", encoding="utf-8")

        content: str = l.read()
        print(content)

#eloado()
dalok()
#lista()