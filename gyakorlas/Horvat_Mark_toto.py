from typing import List
from typing import TextIO

class data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(" ")
        self.ev: int = int(fields[0])
        self.het: int = int(fields[1])
        self.fordulo: int = int(fields[2])
        self.T13p1: int = int(fields[3])
        self.Ny13p1: int = int(fields[4])
        self.eredmenyek: str = fields[5]

    def __str__(self) -> str:
        return "Év = {x}; Hét = {y}; Forduló = {txt}; T13p1 = {col}; Ny13p1 = {z}; Eredmények = {v}".format(x=self.ev, y=self.het, txt=self.fordulo, col=self.T13p1, z=self.Ny13p1, v=self.eredmenyek)

class feladat:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("toto.txt", encoding="utf-8")
        content: str = f.read().strip()
        lines: List['str'] = content.split(sep="\n" )
        datalist: List['data'] = list()
        for i in range(0, len(lines)):
            d = data(lines[i])
            datalist.append(d)
        #for d in datalist:
        #   print(d)
        f.close()

        print("Feladat 3")
        F = 0
        for i in (0, len(datalist)):
            F += i
        print(F)

        print("Feladat 4")
        T = 0
        for i in (0, len(datalist) - 1):
            T += datalist[i].T13p1
        print(T)

        #print("Feladat 5")

        #print("Feladat 7")

        #print("Feladat 8")

        #print("Feladat 9")
feladat()