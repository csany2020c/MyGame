import string
from typing import List
from typing import TextIO

class Adat:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        print("Ennyi volt")
        fields: List['str'] = parseString.split("")

class Beolv:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content:str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for str in lines:
            d = Adat(str)
            datalist.append(d)
        print("Print list")
        for d in datalist:
            print(d)

        f.close()

Beolv()

