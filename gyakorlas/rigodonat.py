from typing import List
from typing import TextIO

class data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.het: int = int(fields[1])
        self.fordulo: int = int(fields[2])
        self.T13p1: int = int(fields[3])
        self.Ny13p1: int = int(fields[4])


    def __str__(self) -> str:
        return "Év = {x}; Hét = {y}; Forduló = {txt}; T13p1 = {col}; Ny13p1 = {z};".format(x=self.ev, y=self.het, txt=self.fordulo, col=self.T13p1, z=self.Ny13p1)

class main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("toto.txt", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n" )
        datalist: List['data'] = list()
        for i in range(0, len(lines)):
            d = data(lines[i])
            datalist.append(d)

        f.close()

main()