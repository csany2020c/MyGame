import string
from typing import TextIO
from typing import List


class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split(" ")

        self.text: str = " "


class Main:

    def __init__(self) -> None:
        super().__init__()

        f: TextIO = open("!_Spec\orvosi_nobeldijak.txt", "r")
        content: str = f.read()

        print(content)
        lines: List['str'] = content.split(sep="\n")

        datalist: List['Data'] = list()
        for s in lines:
            d = Data(s)
            datalist.append(d)
        f.close()

Main()