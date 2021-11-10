import string
from typing import List
from typing import TextIO


class Adat:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split(";")
        self.text: str = " "


class Beolv:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Adat'] = list()
        for i in range(1, len(lines) - 1):
            d = Adat(lines[i])
            datalist.append(d)

        f.close()


Beolv()

