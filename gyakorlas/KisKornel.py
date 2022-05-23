from typing import list
from typing import list


class Het:
    def __init__(self, parse: str) -> None:
        super().__init__()
        fields: List['string'] = parse.split(" ")
        self.ev: int = int(fields[0])
        self.het: int = int(fields[1])
        self.fordulo: int = int(fields[2])
        self.t13p1: int = int(fields[3])
        self.ny13p1: int = int(fields[4])
        self.ev: str = fields[5]

class Feladat:
    def __init__(self, filename: str) -> None:
        super().__init__()
        self.hetek: List['Het'] = list()
        f= open(filename, encoding="utf-8", mode="r")
        content: List['str'] = f.read().strip().split(sep="\n")
        print (content)


Feladat("toto.txt")
