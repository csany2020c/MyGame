from typing import List, TextIO


class Adatok:
    def __init__(self, Parsestring: str) -> None:
        super().__init__()
        fieldls: List['str'] = Parsestring.strip().split(" ")
        self.ev: int = int(fieldls[0])
        self.het: int = int(fieldls[1])
        self.fordulo: int = int(fieldls[2])
        self.T13p1: int = int(fieldls[3])
        self.Ny13p1: int = int(fieldls[4])
        self.Eredmenyek: str = fieldls[5]

    def __str__(self):
        return "ev = {a}, het = {b}, fordulo = {c}, T13p1 = {d}, Ny13p1e = {e}, Eredmenyek = {f}".format(a=self.ev, b=self.het, c=self.fordulo, d=self.T13p1, e=self.Ny13p1, f=self.Eredmenyek)


class Program:

    def __init__(self, fajlnev: str) -> None:
        super().__init__()
        lista: List['Adatok'] = list()
        for i in open(fajlnev, mode="r").read().strip().split("\n"):
            lista.append(Adatok(i))
        for i in lista:
            print(i)


Program("toto.txt")

# egypeldany: Adatok = Adatok("2020 17 1 30 0 2221XX12222121")
# megegypeldany: Adatok = Adatok("2023 10 2 10 2 21112xxxxxxx21")
# print(egypeldany)
# print(megegypeldany)
