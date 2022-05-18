from typing import List, TextIO

class Adatok:
    def __int__(self, bemenetistring: str):
        string: str = bemenetistring
        string.split(sep='\n')
        fieldls: List['str'] = string.strip().split(" ")
        self.ev: int = int(fieldls[0])
        self.het: int = int(fieldls[1])
        self.fordulo: int = int(fieldls[2])
        self.t13p1: int = int(fieldls[3])
        self.ny13p1: int = int(fieldls[4])
        self.eredmenyek: str = fieldls[5]



