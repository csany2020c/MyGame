from typing import List
from typing import TextIO

class Feladat:
    def __init__(self):
        f: TextIO = open("toto.txt")
        tartalom: str = f.read()

        print(tartalom)

        sor: List['str'] = tartalom.split(sep="\n")
        print(sor)

#3.feladat
        print("3.feladat")
        sorokszama = 0
        for i in range(len(sor)):
            sorokszama += 1
        print(sorokszama)

#4.feladat
        # print("4.feladat")
        # telitalalat = 0
        # for i in range(sorokszama):
        #     telitalalat
        # print(telitalalat)
        #

class Data:
    def __init__(self, vesszo: str):
        szelet: List['str'] = vesszo.split(",")
        self.ev: int = int(szelet[0])
        self.het: int = int(szelet[1])
        self.fordulo: int = int(szelet[2])
        self.t13p1: int = int(szelet[3])
        self.ny13p1: int = int(szelet[4])
        self.eredmenyek: str = szelet[5]

    def __str__(self):
        return "Év = {}; Hét = {}; Forduló = {}; T13p1 = {}; Ny13p1 = {}; Eredmények = {}".format(self.ev, self.het, self.fordulo, self.t13p1, self.ny13p1, self.eredmenyek)

Feladat()