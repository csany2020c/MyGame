from typing import List, TextIO

class Adatok:
    def __init__(self, Parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = Parsestring.strip().split(" ")
        self.ev: int = int(fields[0])
        self.het: int = int(fields[1])
        self.fordulo: int = int(fields[2])
        self.T13p1: int = int(fields[3])
        self.Ny13p1: int = int(fields[4])
        self.eredmenyek: str = fields[5]

    def __str__(self):
        return "Év = {a}, Hét = {b}, Forduló = {c}, T13p1 = {d}, Ny13p1e = {e}, Eredmények = {f}".format(a=self.ev, b=self.het, c=self.fordulo, d=self.T13p1, e=self.Ny13p1, f=self.eredmenyek)

    def osszfizetett(self) -> int:
        return self.T13p1 * self.Ny13p1

    def dontetlenek(self) -> int:
        d: int = 0
        for i in self.eredmenyek:
            if i == "X":
                d += 1
        return d

class Program:
    def __init__(self, fajl: str) -> None:
        super().__init__()
        lista: List['Adatok'] = list()
        for i in open(fajl, mode="r").read().strip().split("\n"):
            lista.append(Adatok(i))
        #3
        print(len(lista))
        #4
        s: int = 0
        for i in lista:
            s += i.T13p1
        print(s)
        #9
    def dontnelkuli(self, lista: List['Adatok']):
        for i in lista:
            if i.dontetlenek() == 0:
                return True
        return False

Program("toto.txt")