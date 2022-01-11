from typing import TextIO
from typing import List

class Data:
    def __init__(self, parseString) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.valami: str = fields[0]


    def __str__(self):
        return ("{x}".format(x=self.valami))

class Main
    def __init__(self):
        super().__init__()
        f: TextIO = open("map2.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines))